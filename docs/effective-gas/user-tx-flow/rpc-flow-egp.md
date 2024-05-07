The RPC flow phase of transactions consists of two stages:

- The gas price suggestion.
- Pre-execution of transactions. 

This flow ends with transactions being stored in a pool waiting to be executed by the sequencer.

## Gas price suggestion

The L2 network (the zkEVM) polls for L1 gas price values and uses them to:

- Suggest L2 gas price to users as per user requests.
- Sets the minimum acceptable L2 gas price, denoted by $\texttt{L2MinGasPrice}$.

The user then signs transactions with the appropriate gas price, called $\texttt{GasPriceSigned}$, based on the suggested L2 gas price, $\texttt{GasPriceSuggested}$.

Transactions are accepted for pre-execution only if

$$
\texttt{GasPriceSigned} > \texttt{L2MinGasPrice}
$$

## Pre-execution of transactions

Pre-execution of transactions, which happens at the RPC level, involves estimating the gas required for processing the transactions submitted by the users. 

This is internally measured (internal to the zkEVM) in terms of resources spent to execute the transactions. These resources are the numbers of counters used up in the zkEVM ROM. 

A transaction is said to be _out of counters_ (OOC) if the signed gas price is insufficient to pay for the required gas units.

OOC transactions get rejected straight away, while those with no OOC stand a chance to be added to the pool.

At this stage of the flow, the RPC also computes the "breakeven gas price", denoted by $\texttt{BreakEvenGasPriceRPC}$. That is, 

$$
  \texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsedRPC}} \cdot \texttt{NetProfit},
$$

 where $\texttt{NetProfit}$ is the L2's marginal profit  for transaction processing.   

Transactions with no OOC get added to the pool of transactions if,

- Either $\texttt{GasPriceSigned} > \texttt{BreakEvenGasPriceRPC} \cdot \texttt{BreakEvenFactor}$.
  
  where $\texttt{GasUsedRPC}$ is the RPC's estimated gas cost.
  
- Or $\texttt{GasPriceSigned} \geq \texttt{GasPriceSuggested}$.

The total fees paid by the user is given by:

$$
\texttt{TotalTxPrice} = \texttt{DataCost} \cdot \texttt{L1GasPrice} + (\texttt{L2 Execution gas cost}) \cdot \texttt{L2GasPrice}
$$

The RPC flow is summarized in the figure below.

![Figure: RPC flow](../../../../img/zkEVM/gas-price-flows-i.png)


## Example (RPC tx flow)

Consider a scenario where a user sends a query for a suggested gas price during a 5-minute interval, as shown in the figure below.

Values of L1 gas prices, polled every 5 seconds, are displayed above the timeline, while the corresponding L2 gas prices are depicted below the timeline. See the figure below.

![Figure: Suggested gas price (first)](../../../../img/zkEVM/timeline-current-l1gasprice-suggstd.png)

1. Observe that, in the above timeline, the user sends a query at the time indicated by the dotted-arrow on the left. And that's when $\texttt{L1GasPrice}$ is $19$.
    
    The RPC node responds with a $2.85 \texttt{ GWei/Gas}$, as the value of the suggested L2 gas price.

    This value is obtained as follows:

    $$
    \texttt{GasPriceSuggested} = 0.15 \cdot 19 = 2.85 \texttt{ GWei/Gas}
    $$

    where $0.15$ is the zkEVM's suggested factor.

2. Let's suppose the user sends a transaction signed with a gas price of $3$. That is, $\texttt{SignedGasPrice} = 3$.
    
    However, by the time the user sends the signed transaction, the L1 gas price is no longer $19$ but $21$. And its correponding suggested gas price is $\mathtt{3.15 = 21 \cdot 0.15}$.

    Note that the minimum suggested L2 gas price, in the 5-min time interval, is $2.85$. And since

    $$
    \texttt{SignedGasPrice} = 3 > 2.85 = \texttt{L2MinGasPrice}
    $$

    the transaction gets accepted for pre-execution.

3. At this point, the RPC makes a request for pre-execution. That is, getting an estimation for the gas used, computed with a state root that differs from the one used when the transaction is sequenced.
    
    In this case, suppose an estimation of gas used is $\texttt{GasUsedRPC} = 60,000$, without an out of counters (OOC) error.

4. Since there's no out of counters (OOC) error, the next step is to compute the $\texttt{BreakEvenGasPriceRPC}$.
    
    Suppose it works out to be:
    
    $$
    \texttt{BreakEvenGasPriceRPC} = 2.52\ \texttt{GWei/Gas}
    $$

    (Details on how this calculation are covered later in the [Implementing EGP strategy section](../implement-egp-strat.md).)

5. As noted in the outline of the RPC transaction flow, one more check needs to be done. That is, testing whether:
    
    $$
    \texttt{SignedGasPrice} > \texttt{BreakEvenGasPriceRPC} \cdot \texttt{BreakEvenFactor}
    $$

    Using the $\texttt{BreakEvenFactor} = 1.3$ yields:

    $$
    \texttt{BreakEvenGasPrice} \cdot \texttt{BreakEvenFactor} = 2.52 \cdot 1.3 =  3.276
    $$

    And since $\texttt{SignedGasPrice}  = 3 <  3.276$, the transaction is not immediately stored in the transaction pool.

6. However, since
    
    $$
    \texttt{SignedGasPrice} = 3 ≥ 2.85 = \texttt{GasPriceSuggested}
    $$

    and despite the risk of the network sponsoring the transaction, it is included in the transaction pool.
    
