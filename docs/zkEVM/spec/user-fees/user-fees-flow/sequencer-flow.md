The sequencer is the zkEVM component that is responsible for fetching transactions from the Pool and assembling some of them into a batch. 

It is the sequencer that submits a sequence of batches to the L1, which will then be proved by the Aggregator.

The figure below shows the progress of a transaction within the sequencer component.

It starts from the moment a transaction is fetched from the Pool, until it is executed by the Executor.

![Figure: Transaction flow in the Sequencer](../../../../img/zkEVM/tx-flow-seq-component.png)

Let’s examine the above figure in more detail.

1. The sequencer computes the estimated $\texttt{EffectiveGasPrice}$, or simply $\texttt{EEGP}$, using the $\texttt{GasUsedRPC}$.
    
    Recall that the $\texttt{GasUsedRPC}$ is obtained in the RPC pre-execution using;

    - A previous state root, which has now changed, and 
    - The current $\texttt{L1GasPrice}$, which may also differ from the one used when sending the transaction to the RPC.

2. At this point, we have two options:
    
    - If $\texttt{SignedGasPrice} ≤ \texttt{EEGP}$, even with only an estimated effective gas price, there is a significant risk of loss.

    In such cases, we opt not to adjust the gas price any further, so as to reduce the number of executions needed to do so.

    Henceforth, the user is charged the full $\texttt{SignedGasPrice}$, so the Executor will execute the transaction using it, concluding the sequencing process.

    - Conversely, if $\texttt{SignedGasPrice} > \texttt{EEGP}$, there's room for further adjustment of the gas price that will be charged to the user.

3. In the previous case, it was necessary to compute a more precise effective gas price based on the accurate amount of gas, denoted as $\texttt{GasUsedNew}$, obtained during the transaction’s execution using the correct state root at the time of sequencing transactions.

    Henceforth, the Executor executes the transaction using $\texttt{EEGP}$, obtaining $\texttt{GasUsedNew}$, which the sequencer utilizes to compute a new effective gas price, referred to as $\texttt{NEGP}$.

4. We have two paths:
    
    - If the percentage deviation between $\texttt{EEGP}$ and $\texttt{NEGP}$ is higher than a fixed deviation parameter $\texttt{FinalDeviationParameter}$, which is $10$ in the actual configuration, that is

    $$
    \frac{|\texttt{NEGP} − \texttt{EEGP}|}{\texttt{EEGP}} \cdot 100 < \texttt{FinalDeviationParameter}
    $$

    indicates that there is minimal distinction between charging the user with $\texttt{NEGP}$ compared to $\texttt{EEGP}$.

    Therefore, despite potential losses to the network or the user, though quite small, we end the flow just to avoid re-executions and thus save execution resources.

    So, we charge the user with $\texttt{EEGP}$.

    - On the contrary, if the percentage deviation equals or exceeds the deviation parameter,

    $$
    \frac{|\texttt{NEGP} − \texttt{EEGP}|}{\texttt{EEGP}} \cdot 100 ≥ \texttt{FinalDeviationParameter}
    $$

    there is a big difference between executions and we may want to adjust gas price due to potential losses to the network or the user.

5. In the latter case, two options arise:
    
    - If the gas price signed is less than or equal to the accurately computed effective gas price, with the correct state root, and

    $$
    \texttt{SignedGasPrice} \leq \texttt{NEGP}
    $$

    the network runs the risk of incurring a loss.

    Hence the user is charged the full $\texttt{SignedGasPrice}$, and the executor therefore executes the transaction using the $\texttt{SignedGasPrice}$. And the sequencing process is concluded.

    - Otherwise, if $\texttt{SignedGasPrice} > \texttt{NEGP}$, then there's sufficient margin to adjust the gas price and thus charge the user less than their $\texttt{SignedGasPrice}$.

    However, in order to save executions, we end the adjustment process in this iteration, so that we conclude the flow using a trick explained in the next point.

6. Again, in the latter subcase, we check if the transaction processing includes the two opcodes that use the gas price:
    
    - The $\texttt{GASPRICE}$ opcode.
    - The $\texttt{BALANCE}$ opcode from the source address.

    We have two cases:

    - If the transaction contains the aforementioned opcodes, we impose a penalty on the user for security reasons.

    In such cases, we simply proceed with executing the transaction using the entire $\texttt{SignedGasPrice}$ to minimize potential losses and conclude the flow, as mentioned earlier. 

    This precaution is employed to mitigate potential vulnerabilities in deployed Smart Contracts, that arise from creating a specific condition based on the gas price, for example, to manipulate execution costs.

    - If the transaction does not make use of the gas-price-related opcodes, the executor executes the transaction with the more adjusted gas price, which is $\texttt{NEGP}$, and ends the sequencing process.


### Numerical Example: Sequencer Flow

Let's continue the numerical example we have been using throughout this document.

The figure below indicates the current $\texttt{L1GasPrice}$ at the top of the timeline, while the associated $\texttt{GasPriceSuggested}$ is below the timeline.

$$
 \texttt{GasPriceSuggested} = 0.15 \cdot \texttt{L1GasPrice} 
$$

at the time of sequencing the transaction.

Recall how we previously ended up computing the $\texttt{BreakEvenGasPriceRPC}$ of $2.52\ \texttt{GWei/Gas}$.

![Figure: ](../../../../img/zkEVM/timeline-l1gasprice-suggstd-seq-tx.png)


1. Suppose the user signed a gas price of $3.3\ \texttt{GWei/Gas}$. According to the above figure, the network recommends a gas price of $3$ at the time of transaction sequencing, which corresponds to an L1 gas price of $20$. This results in an $\texttt{EEGP}$ of
    
    $$
    \texttt{EEGP} = 2.722\ \texttt{GWei/Gas}
    $$

    where the $10\%$ increase attributed to prioritization carried out by $\texttt{PriorityRatio}$ set at $0.1$.

2. Since the signed gas price is bigger than the estimated effective gas price,
    
    $$
    \texttt{SignedGasPrice} = 3.3 > 2.772 = \texttt{EEGP}
    $$

    we execute the transaction using the current and correct state and the computed $\texttt{EEGP}$ in order to obtain an accurate measure of the gas used, which we call $\texttt{GasUsedNew}$.

    Suppose that, in this case, we obtain

    $$
    \texttt{GasUsedNew} = 95,000\ \texttt{Gas}
    $$

    which is bigger than the estimated gas of $60,000$ at the **RPC** pre-execution.

3. By using $\texttt{GasUsedNew}$, we can compute and adjusted effective gas price called $\texttt{NEGP}$ as follows:
    
    $$
    \texttt{TxCostNew} = (200 · 16 + 100 · 4) · 20 + 95,000 · 20 · 0.04 = 148,000 \ \texttt{GWei}
    $$

    $$
    \texttt{BreakEvenGasPriceNew} = \frac{148, 000}{95, 000} · 1.2 = 1.869\ \texttt{GWei/Gas}
    $$

    $$
    \texttt{NEGP} = 1.869 · 1.1 = 2.056\ \texttt{GWei/Gas}
    $$

    Observe that the transaction cost is way higher than the estimated one of $126,000$ even when the L1 Gas Price has decreased from 21 to 20 due to a huge increase in Gas.

4. Observe that there is a significative deviation between both effective gas prices:
    
    $$
    \frac{|\texttt{NEGP} − \texttt{EEGP}|}{\texttt{EEGP}}  \cdot 100 = 25.82 > 10
    $$

    This deviation penalizes the user a lot since

    $$
    \texttt{SignedGasPrice}\ = 3.3 > 2.52 =\ \texttt{EEGP} ≫ 2.056 =\ \texttt{NEGP}
    $$

    So we try to charge $\texttt{NEGP}$ to the user to further adjust the gas price.

5. In this case, suppose that the transaction does not have neither $\texttt{GASPRICE}$ nor $\texttt{BALANCE}$ from the source address opcodes, so we execute the transaction with
    
    $$
    \texttt{GasPriceFinal} = \texttt{NEGP} = 2.056\ \texttt{GWei/Gas}
    $$

    Observe that $\texttt{GasUsedFinal}$ should be the same as $\texttt{GasUsedNew} = 95,000$.

    We can now compute $\texttt{EffectivePercentage}$ and $\texttt{EffectivePercentageByte}$ as follows:

    $$
    \texttt{EffectivePercentage} = \frac{\texttt{GasPriceFinal}}{\texttt{SignedGasPrice}} = \frac{2.056}{3.3} = 0.623.
    $$

    $$
    \texttt{EffectivePercentageByte} = \lfloor \texttt{EffectivePercentage} · 256 \rfloor − 1 = 158
    $$

    Observe that the user has been charged $62.3\%$ of the gas price they signed at the time of sending the transaction.
