In a high level, the RPC is the zkEVM component that handles the acceptance or rejection of incoming transactions, and saves the approved transactions in the Pool.

The figure below shows the progression of a transaction within the RPC component,

-  Starting from when a user sends a transaction to the network.
-  Up until the transaction is either stored in the Pool or rejected.

![Figure: Transaction flow within the RPC](../../../../img/zkEVM/tx-flow-in-rpc.png)

Let’s examine the above figure in detail:

1. Users ask the RPC for the current $\texttt{GasPriceSuggested}$, which is a factor of the current L1 $\texttt{GasPrice}$. More concretely,
    
    $$
    \texttt{GasPriceSuggested} = \texttt{L1GasPrice} \cdot \texttt{SuggestedFactor}
    $$

    where the $\texttt{SuggestedFactor}$ (which is currently of $0.15$) satisfies the condition:

    $$
    \texttt{SuggestedFactor} > \texttt{L1GasPriceFactor}
    $$

    in order to be able to cover data availability costs.

    Observe that the suggested gas price varies over time as $\texttt{L1GasPrice}$ also does.

2. The user selects the gas price to sign the transaction with, $\texttt{SignedGasPrice}$, then sends the transaction.
    
    Observe that there is a time interval between when the user asks for a suggested gas price and when they send the transaction,during which the L1 gas price could have increased.

    And hence, if $\texttt{SignedGasPrice} < \texttt{GasPriceSuggested}$, then the transaction gets rejected. Resulting in a bad UX.

    Alternatively, the user is given a margin of $5$ minutes, which is controlled by the $\texttt{MinAllowedGasPriceInterval}$ parameter.

    If the signed gas price does not exceed the minimum gas price among those suggested within the particular $5$ minutes interval, $\texttt{L2MinGasPrice}$,

    $$
    \texttt{SignedGasPrice} \not> \texttt{L2MinGasPrice}
    $$

    the transaction is automatically rejected, since it will not be possible to cover costs.

3. If the transaction was accepted in the previous step, the RPC uses a cloud executor to pre-execute the transaction.
    
    Note that this pre-execution is only an estimated execution, the used state root is not the correct one as the transaction has not been sequenced.

    Recall that once a transaction is added to the Pool, it is mandatory that it is eventually sequenced.

    The purpose for the pre-execution step is therefore to filter transactions accordingly and estimate a fair gas price as early as possible, to avoid future losses.

    The aim of pre-execution is to obtain and estimate the amount of used gas, which is dubbed $\texttt{GasUsedRPC}$.

    Also, if we run out of counters in the pre-execution stage, the transaction is immediately rejected.

4. If the transaction was not reverted due to an OOC error, we compute the current breakeven gas price, which we will call $\texttt{BreakEvenGasPriceRPC}$.
    
    Recall that we need the current $\texttt{L1GasPrice}$, the transaction size, the $\texttt{GasUsed}$ RPC and the $\texttt{NetProfit}$ parameter that is present, in order to include the network’s profit for the whole transaction’s processing.


5. Now, we have two different paths:
    
    - If the gas price signed by the user at the time of sending the transaction is higher than the $\texttt{BreakEvenGasPriceRPC}$, increased by a factor $\texttt{BreakEvenFactor} ≥ 1$ (which is currently set at $1.3$ for the purpose of protecting the network against bad gas usage estimations in the RPC),

    $$
    \texttt{SignedGasPrice} > \texttt{BreakEvenGasPriceRPC} \cdot \texttt{BreakEvenFactor}
    $$

    then the transaction is immediately _accepted_ and stored in the pool.

    - Otherwise, if

    $$
    \texttt{SignedGasPrice} \leq \texttt{BreakEvenGasPriceRPC} \cdot \texttt{BreakEvenFactor}
    $$

    we are in dangerous zone, because we may be facing losses due either high data availability costs or fluctuations in future computations.

    So we should _reject_ the transaction. However, we are currently not directly rejecting transactions at this stage.

6. In the later stage, we check if the gas price signed with the transaction exceeds the current suggested gas price:
    
    $$
    \texttt{SignedGasPrice} ≥ \texttt{GasPriceSuggested}
    $$

    In this case, we take the risk of possible losses, sponsoring the difference if necessary, and so we introduce the transaction into the Pool.

    However, if $\texttt{SignedGasPrice} < \texttt{GasPriceSuggested}$ we assume that is highly probable that we face a loss and we immediately reject the transaction.

**Final Considerations**

It is important to remark that, as afore-mentioned, once a transaction is included into the pool, we should actually sequence it. That is, we should include it in a block.

Hence, if something goes bad in later steps, and the gas consumption deviates significantly from the initial estimate, we risk incurring losses with no means of rectifying the situation.

On the contrary, if the process goes as estimated and the consumed gas is similar to the estimated one, we can reward the user by modifying the previously introduced $\texttt{effectivePercentage}$.

It's important to observe that, among all the transactions stored in the Pool, those that are prioritized at the time of sequencing are the ones with higher $\texttt{effectiveGasPrice}$, due to the prioritization introduced with $\texttt{PriorityRatio}$.

Observe that $\texttt{effectiveGasPrice}$ is not computed in the RPC but in the sequencer. So, it is possible that the suggested gas price at this moment, differs from the one suggested when the user sent the transaction.

### Numerical example: RPC flow

Let's continue with the numerical example started earlier in this whole document.

In figure below, we indicate the current $\texttt{L1GasPrice}$ at the top of the timeline, while the associated $\texttt{GasPriceSuggested} = 0.15 \cdot \texttt{L1GasPrice}$ is shown at the bottom.

![Figure: Timeline - Current L1GasPrice and suggested Gas price](../../../../img/zkEVM/timeline-current-l1gasprice-suggstd.png)

1. In the above timeline, the time marked with the arrow on the left, is when the user queries the RPC for the suggested gas price. And that's when $\texttt{L1GasPrice}$ is $19$. In response, the user receives the value of $2.85 \texttt{GWei/Gas}$, obtained as shown here:
    
    $$
    \texttt{GasPriceSuggested} = 0.15 \cdot 19 = 2.85\ \texttt{GWei/Gas}
    $$

2. Let's suppose that the user sends a transaction signed with a gas price of $3$:
    
    $$
    \texttt{SignedGasPrice} = 3
    $$

    Observe that the signed gas price is strictly lower than the current suggested gas price, which is $\mathtt{3.15 = 21 \cdot 0.15}$.

    However, recall that at this precise step, we are allowing all the transactions with a signed gas price exceeding the minimum suggested gas price during the 5 minutes before sending the transaction refreshed every $5$ seconds.

    Henceforth, since

    $$
    \texttt{SignedGasPrice} = 3 > 2.85 = \texttt{L2MinGasPrice}
    $$

    we accept the transaction at this point.

3. At this point, the RPC asks for a pre-execution, getting an estimation for the gas used, computed with a state root that differs from the one that will be used when sequencing the transaction.
    
    In this case, we get an estimation of gas used, $\texttt{GasUsedRPC} = 60,000$, without running out of counters.

4. Since we have not run out of counters, we compute $\texttt{BreakEvenGasPriceRPC}$, supposing the same transaction sizes as before, and getting:
    
    $$
    \texttt{BreakEvenGasPriceRPC} = 2.52\ \texttt{GWei/Gas}
    $$

5. Notice that, in this particular scenario, despite having
    
    $$
    \texttt{SignedGasPrice} < \texttt{BreakEvenGasPriceRPC}
    $$

    the introduction of the $\texttt{BreakEvenFactor}$, which acts as a protective measure as previously mentioned, results in the next check for failure:

    $$
    \texttt{SignedGasPrice} < 3.276 = 2.52 \cdot 1.3 = \texttt{BreakEvenGasPrice} \cdot \texttt{BreakEvenFactor}
    $$

6. However, recall that we are currently sponsoring and accepting all transactions as long as 
    
    $$
    \texttt{SignedGasPrice} = 3 ≥ 2.85 = \texttt{GasPriceSuggested}
    $$

    which is the current case.

    Henceforth, we accept the transaction and store it in the Pool, despite the risk of financial loss.
