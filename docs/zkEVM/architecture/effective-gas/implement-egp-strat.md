In this section we provide an elaborate discussion on how Polygon zkEVM network ensures transactions are executed with the best gas price for the user, while incurring minimal or no losses.

You will learn how to sign transactions with the appropriate gas price ensuring:

- There is minimal likelihood for your transactions to be reverted.
- The sequencer prioritizes your transactions for execution.

## How to avert rejection of transactions

The first step is to ensure that users sign transactions with sufficient gas price, and thus ensure the transactions are included in the L2's pool of transactions.

Polygon zkEVM's strategy is to use pre-execution of transactions so as to estimate each transaction's possible gas costs.

### Suggested gas prices

Due to fluctuations in the L1 gas price, the L2 network polls for L1 gas price every 5 seconds.

The polled L1 gas prices are used to determine the appropriate L2 gas price to suggest to users.

Since the L1 gas price is likely to change between when a user signs a transaction and when the transaction is pre-executed, the following parameters are put in place:

-  A $5$-minute interval of several suggested gas prices, called $\texttt{MinAllowedPriceInterval}$.
- During the $\texttt{MinAllowedPriceInterval}$, the user's transactions can be accepted for pre-execution, provided the $\texttt{SignedGasPrice}$ is above the least among the suggested gas prices in the interval.
- The least of the suggested gas prices is called $\texttt{L2MinGasPrice}$.

![Figure: minimum allowed gas interval](../../../img/zkEVM/min-allowed-gas-interval.png)

All transactions such that $\texttt{SignedGasPrice} > \texttt{L2MinGasPrice}$ are accepted for pre-execution.

## How to avoid incurring losses in L2

There are basically three measures put in place to avoid incurring losses in the L2 network:

- Pre-execution of transactions. 
- The breakeven gas price: $\texttt{BreakEvenGasPrice}$.
- The L2's net profit.

### Transaction pre-execution

Pre-execution of transactions is used to estimate L2 resources each transaction will spent when processed.

These resources are measured in terms of counters in the zkEVM's ROM, but are converted to gas units for better UX.

This is the stage where transactions are either discarded or stored in the pool database, a pool of transactions waiting to be processed by the sequencer.

The price of posting transaction data to L1 is charged to the zkEVM network at a full L1 price.

Although computational costs in L2 may be accurately estimated, in cases where there is a reduction in such costs due to fewer L2 resources being spent, the user may be justified to sign a transaction with a very low gas price. But by signing such a low gas price, the user runs the risk of exhausting their wei reserves when transaction data is posted to L1.

So then, if the use of $\texttt{L1GasPriceFactor = 0.04}$ is the only precautionary measure the L2 network takes in computing suggested gas prices, the L2 network will most likely incur losses.

A $\texttt{suggestedFactor = 0.15}$ is therefore used to calculate each suggested gas price:

$$
\texttt{suggestedL2GasPrice} = \texttt{L1GasPrice} \cdot \texttt{suggestFactor}
$$

Such a factor is justifiable considering the fact that, the sequencer is obliged to process every transaction stored in the pool database, irrespective of its $\texttt{SignedGasPrice}$ and the prevailing L1 gas price.

### Breakeven gas price

Calculating the breakeven gas price is another measure used in the Polygon zkEVM network to mitigate possible losses.

The breakeven gas price is calculated as a ratio of the total transaction cost and the amount of gas used:

$$
\texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsed}}
$$

In order to attain some profit for processing transactions, a marginal profit factor called $\texttt{NetProfit}$ is incorporated in the $\texttt{BreakEvenGasPrice}$ formula as follows:

$$
\texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsed}} \cdot \texttt{NetProfit}
$$

The breakeven gas price factor is set to $1.3$​, resulting in a 30% net profit.
