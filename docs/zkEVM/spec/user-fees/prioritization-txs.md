Prioritization of transactions in Ethereum is determined by $\texttt{SignedGasPrice}$ and transactions signed at a higher price are given priority.

In order to implement this, suppose users are only aware of two gas price values:

- The current $\texttt{GasPriceSuggested}$, which is the one provided to the RPC.
- The one signed with the transaction, called $\texttt{SignedGasPrice}$.

It is important to note that this part of the process is not computed in the RPC but in the sequencer.

So it is possible for the suggested gas price at this moment to be different from the one suggested when the transaction was sent.

When transactions are sequenced, we need to prioritize some over the others, depending on both $\texttt{SignedGasPrice}$ and current $\texttt{GasPriceSuggested}$.

In the case where $\texttt{SignedGasPrice} > \texttt{GasPriceSuggested}$, we establish a priority ratio as follows:

$$
\texttt{PriorityRatio} = \frac{\texttt{SignedGasPrice}}{\texttt{GasPriceSuggested}} − 1. 
$$

If $\texttt{SignedGasPrice} ≤ \texttt{GasPriceSuggested}$, it means the user has chosen not to have their transactions prioritized, and the transaction maybe rejected due to low gas price. In this case, we establish a priority ratio to be $0$.

Finally, the $\texttt{EffectiveGasPrice}$ will be computed as:

$$
\texttt{EffectiveGasPrice} = \texttt{BreakEvenGasPrice} \cdot (1 + \texttt{PriorityRatio})
$$

### Numerical example (Priority)

Recall that, in the previous example, we were signing a gas price of $3.3$ at the time of sending the transaction.

Suppose that, at the time of sequencing a transaction, the suggested gas price is $3$:

$$
\texttt{SignedGasPrice} = 3.3,\ \ \texttt{GasPriceSuggested} = 3
$$

The difference between the two values is taken into account in the priority ratio:

$$
\texttt{PriorityRatio} = \frac{3.3}{3} − 1 = 0.1
$$

Henceforth, the estimated $\texttt{EffectiveGasPrice}$ (that is, the one using the RPC gas usage estimations) is:

$$
\texttt{EffectiveGasPrice} = 2.52 · (1 + 0.1) = 2.772 \texttt{ GWei/Gas}
$$
