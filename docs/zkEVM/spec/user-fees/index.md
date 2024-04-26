The aim with this document is to describe the Effective Gas Price (EGP), a mechanism by which the Polygon zkEVM network charges gas fees in a more fair and accurate manner. These fees cover L1 data-availability and L2 execution costs. It is meant to help users set the $\texttt{gasPrice}$ such that there's little chance for a transaction revert or failure.

## Basic Ethereum fee schema

Let's make a quick recollection of the basic fee schema used in Ethereum.

Firstly, gas is a unit that accounts for resources used when processing a transaction. At the time of sending a transaction, the user can decide on two parameters; $\texttt{gasLimit}$ and $\texttt{gasPrice}$:

- $\texttt{gasLimit}$ is the maximum amount of gas units that a user is willing to buy in order to complete a transaction.

- $\texttt{gasPrice}$ refers to the amount of wei a user is willing to pay for $1$ gas unit.

Note that transactions with higher $\texttt{gasPrice}$ receive faster confirmation. So, if a user wants their transactions to be prioritized, then they would have to set a high $\texttt{gasPrice}$ for their transactions.

At the start of the transaction processing, the following amount of Wei is subtracted from the source account balance:

$$
\texttt{gasLimit} \cdot \texttt{gasPrice}
$$

If $\texttt{gasUsed}$ is greater than $\texttt{gasLimit}$, the transaction is reverted because the transaction cost is higher than what the user is willing to pay.

But, if the $\texttt{gasUsed}$ is less than or equal to $\texttt{gasLimit}$, the transaction gets processed and the unused amount of Wei is refunded.

The refunded amount of Wei is added back to the source account, and it is calculated as follows:

$$
\texttt{gasLimit} · \texttt{gasPrice} - \texttt{gasUsed} \cdot \texttt{gasPrice}
$$

It is important to observe that while the transaction is being processed, the balance of the source account may differ from its state at the time of sending the transaction. 

More specifically, if the `BALANCE` opcode is invoked during the transaction processing, the output will be:

$$
\texttt{initialBalance} − \texttt{gasLimit} \cdot \texttt{gasPrice}
$$

where $\texttt{initialBalance}$ represents the balance of the source account before the execution of the transaction.

## Generic gas fee strategy for L2s

What about setting $\texttt{gasPrice}$ in L2 networks?

L2 user's $\texttt{gasPrice}$ estimation needs to include two factors; the L2 transaction costs, as well as the cost for availing transaction data in L1.

In general, L2 solutions charge an L2 gas price that is a percentage of the L1 $\texttt{gasPrice}$:

$$
\texttt{L2GasPrice} = \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor}
$$

**Example**.

For an L1 gas price of $20$ Gwei, a 4% factor can be set for a particular L2 solution. The L2 gas price is obtained as follows:

$$
\texttt{L2GasPrice} = 20 \text{ Gwei} \cdot 0.04 = 0.8 \text{ Gwei}
$$

Current L2 fees can be viewed here https://l2fees.info.

However, setting an L2 gas fee is not as simple as choosing a factor to multiply with the L1 gas price. There are other aspects to be considered.

Let's think about the following aspects:

1. The $\texttt{gasPrice}$ in L1 fluctuates with time. 
2. High $\texttt{gasPrice}$ values work as incentives for prioritization of transactions in L1.
3. The L1 $\texttt{gas/gasPrice}$ schema may not be aligned with the actual resources spent by the L2 solution.

Their corresponding pertinent questions are:

- How does the zkEVM's transaction processing mechanism mitigate against L1 $\texttt{gasPrice}$ fluctuations?

- How do L2 solutions effectively manage these prioritizations?

- How do L2 solutions address and reconcile any discrepancies between the L1 gas schema and the real resource utilization on L2?
