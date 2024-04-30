The aim here is for the Polygon zkEVM network to avoid accepting transactions that result in financial losses.

In order to achieve this objective, the $\texttt{BreakEvenGasPrice}$ is set to the lowest gas price at which the Polygon zkEVM network incurs no losses.

As explained before, the computation is split in two; costs associated with data availability, and costs associated with the use of resources when transactions are processed.

### Costs associated with data availability

The cost associated with data availability is computed as,

$$
\texttt{DataCost} \cdot \texttt{L1GasPrice}
$$

where $\texttt{DataCost}$ is the cost in gas for data stored in L1.

The cost of data in Ethereum varies according to whether it involves zero bytes or non-zero bytes. In particular, non-zero bytes cost $16$ gas units, while zero bytes cost $4$ gas unints. 

Also, recall that the computation of the cost for _non-zero bytes_ must take into account the constant data which always appear in a transaction but not included in the RLP:

- The signature, which consists of $65$ bytes.
- The previously defined $\texttt{EffectivePercentageByte}$, which consists in a single byte. 

This results in a total of $66$ constantly present bytes.

Taking all in consideration, $\texttt{DataCost}$ can be computed as:

$$
\texttt{DataCost} = (\texttt{TxConstBytes} + \texttt{TxNonZeroBytes}) \cdot \texttt{NonZeroByteGasCost} \\
+\ \texttt{TxZeroBytes} \cdot \texttt{ZeroByteGasCost}
$$

where $\texttt{TxNonZeroBytes}$ represents the count of non-zero bytes in a raw transaction, and similarly $\texttt{TxZeroBytes}$ represents the count of zero bytes in a raw transaction sent by the user.

### Computational costs

Costs associated with transaction execution is denoted by $\texttt{ExecutionCost}$, and it is measured in gas.

In contrast to costs for data availability, calculating computational costs necessecitates transactions to be executed.

So then,

$$
\texttt{GasUsed} = \texttt{DataCost} + \texttt{ExecutionCost}
$$

The total fees received by L2 are calculated with the following formula:

$$
\texttt{GasUsed} \cdot \texttt{L2GasPrice}
$$

where $\texttt{L2GasPrice}$ is obtained by multiplying $\texttt{L1GasPrice}$ by a chosen factor less than $1$,

$$
\texttt{L2GasPrice} = \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor}
$$

In particular, we choose a factor of $0.04$.

### Total price of a transaction

The total transaction cost is simply the sum of data availability and computational costs:

$$
\texttt{TotalTxPrice} = \big( \texttt{DataCost} \cdot \texttt{L1GasPrice} \big) + \big(\texttt{GasUsed} \cdot \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor} \big)
$$

In order to establish the gas price at which the total transaction cost is covered, we can compute $\texttt{BreakEvenGasPrice}$ as the following ratio:

$$
\texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsed}}
$$

Additionally, we incorporate a factor $\texttt{NetProfit ≥ 1}$ that allows us to achieve a slight profit margin:

$$
\texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsed}} \cdot \texttt{NetProfit}
$$

We then conclude that it is financially safe to accept the transaction if

$$
\texttt{SignedGasPrice} > \texttt{BreakEvenGasPrice}.
$$

However, a  problem arises:

In the RPC component, we’re only pre-executing the transaction, meaning we’re using an incorrect state root. Consequently, the $\texttt{GasUsed}$ is only an approximation.

This implies that we need to multiply the result by a chosen factor before comparing it to the signed price.

This ensures that the costs are covered in case more gas is ultimately required to execute the transaction. This factor is named $\texttt{BreakEvenFactor}$.

Now we can conclude that if

$$
\texttt{SignedGasPrice} > \texttt{BreakEvenGasPrice} \cdot \texttt{BreakEvenFactor}
$$

then it is safe to accept the transaction.

Observe that we still need to introduce gas price prioritization, which will be covered later on.

### Numerical example: Computing BreakEvenGasPrice

Recall the example proposed before, where the $\texttt{GasPriceSuggested}$ provided by RPC was $2.85$ gwei per gas, but the user ended up setting $\texttt{SignedGasPrice}$ to $3.3$.

The figure below depicts the current situation.

![Figure: Timeline current L1GasPrice](../../../img/zkEVM/timeline-current-l1gasprice.png)

Suppose the user sends a transaction that has $200$ non-zero bytes, including the constant ones and $100$ zero bytes. 

Moreover, at the time of pre-executing the transaction, which is done without getting an out-of-counters (OOC) error, $60,000$ gas units are consumed.

Recall that, since we are using a "wrong" state root, this gas is only an estimation. 

Hence, using the previously explained formulas, the total transaction cost is:

$$
\begin{aligned}
&\texttt{TotalTxPrice} = \texttt{DataCost} \cdot \texttt{L1GasPrice} + \texttt{GasUsed} \cdot \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor}\\
&\implies  \texttt{TotalTxPrice} = (200 · 16 + 100 · 4) · 21 + 60, 000 · 21 · 0.04 = 126, 000\ \texttt{GWei}
\end{aligned}
$$

Observe that the $21$ appearing in the substitution is the $\texttt{L1GasPrice}$ at the time of sending the transaction.

Now, we are able to compute the $\texttt{BreakEvenGasPrice}$ as:

$$
\texttt{BreakEvenGasPrice} = \frac{\texttt{TotalTxPrice}}{\texttt{GasUsed}} = \frac{126,000\ \texttt{GWei}}{60,000\ \texttt{Gas}} \cdot 1, 2  =  2.52\ \texttt{ GWei/Gas}
$$

We have introduced a $\texttt{NetProfit}$ value of $1.2$, indicating a target of a $20\%$ gain in this process. 

At a first glance, we might conclude acceptance since:

$$
 \texttt{SignedGasPrice} = 3.3 > 2.52
$$

but, recall that this is only an estimation, the gas consumed with the correct state root can differ.

To avoid this, we introduce a $\texttt{BreakEvenFactor}$ of $30\%$ to account for estimation uncertainties:

$$
\texttt{SignedGasPrice} = 3.3 > 3.276 = 2.52 · 1.3 = \texttt{BreakEvenGasPrice} \cdot \texttt{BreakEvenFactor}
$$

Consequently, we decide to accept the transaction.

### Numerical example (Importance of BreakEvenFactor)

Suppose we disable the $\texttt{BreakEvenFactor}$ by setting it to $1$. 

Our original transaction’s pre-execution consumed $60,000$ gas:

$$
\texttt{GasUsedRPC} = 60, 000
$$

However, let's assume the correct execution at the time of sequencing consumes $35,000$ gas.

If we recompute $\texttt{BreakEvenGasPrice}$ using this updated used gas, we get $3.6\ \texttt{GWei/Gas}$, which is way higher than the original one. 

That means we should have charged the user a higher gas price in order to cover the whole transaction cost, standing at $105,000\ \texttt{GWei}$.

But, since we are accepting all the transactions that sign more than $2.85$ of gas price, we do not have any margin to increase more. 

In the worst case we are losing:

$$
105, 000 − 35, 000 · 2.85 = 5,250\ \texttt{GWei}
$$

By introducing $\texttt{BreakEvenFactor}$, we are limiting the accepted transactions to the ones with,

$$
\texttt{SignedGasPrice} ≥ 3.27
$$

in order to compensate for such losses.

In this case, we have the flexibility to avoid losses and adjust both the user's and Polygon zkEVM network's benefits since:

$$
105, 000 − 35, 000 · 3.27 < 0
$$

**Final Note**: In the above example, even though we assumed that the decrease in $\texttt{BreakEvenGasPrice}$ is a result of executing with a correct state root, it can also decrease significantly due to a substantial reduction in $\texttt{L1GasPrice}$.
