Here's how you can accurately determine the gas price to sign your transactions with when submitting transactions to the Polygon zkEVM network.

Polygon zkEVM implements a mechanism called the Effective Gas Price (EGP) that guarantees fair gas fees in the interest of both the user and the network.

Now that the EGP is in place, you can reduce any chance for a transaction revert, while making sure that accepted transactions receive your preferred prioritization. Meanwhile, the zkEVM network incurs minimal to no loss.

## How gas fees work in Ethereum

In Ethereum, gas fees for a transaction are decided using two adjustable parameters:

- The $\texttt{gasLimit}$, which is the maximum amount of gas units the user is willing to buy, in order for their transactions to be completed.
- The $\texttt{gasPrice}$, that is, the amount of wei a user is willing to pay for 1 gas unit.

At the beginning of each transaction, the amount of wei sufficient to cover transaction costs is deducted from the user's account balance. 

That amount of wei is calculated as:

$$
\texttt{gasLimit} \cdot \texttt{gasPrice}
$$

The actual amount spent for the transaction is given by:

$$
\texttt{gasUsed} \cdot \texttt{gasPrice}
$$

And thus, any refund to the user is simply:

$$
\texttt{gasLimit} \cdot \texttt{gasPrice} - \texttt{gasUsed} \cdot \texttt{gasPrice}
$$

Transactions get reverted if the $\texttt{gasUsed}$ is greater than the $\texttt{gasLimit}$. Otherwise, transaction succeed. 

## Computing L2 gas fees

The L2 gas price cannot be simply set to be the same as L1 gas price (more especially in the particular case of rollups, where the main benefit for using a rollup is to reduce gas fees).

For this reason we henceforth distinguish between the two gas prices, and denote them as: $\texttt{L2GasPrice}$ and $\texttt{L1GasPrice}$.

But how can you calculate the appropriate L2 gas price while ensuring that transactions are successfully executed?

Although the same formula is used, that is,

$$
\texttt{gasLimit} \cdot \texttt{gasPrice}
$$

and success is guaranteed if $\texttt{gasLimit}$ is greater than $\texttt{gasUsed}$, the gas used is determined by the gas cost for data availability plus the gas cost for transaction execution in the L2.

That is, 

$$
\texttt{gasUsed} = \texttt{DataCost} + (\texttt{L2 Execution gas cost})
$$

The total fees paid by the user is given by:

$$
\texttt{TotalTxPrice} = \texttt{DataCost} \cdot \texttt{L1GasPrice} + (\texttt{L2 Execution gas cost}) \cdot \texttt{L2GasPrice}
$$

Note that data availability is charged in L1 using the prevailing L1 gas price at the time of posting data.

The main challenge is "How to adjust $\texttt{L2GasPrice}$ in terms of the $\texttt{L1GasPrice}$, so as to account for L2 resources spent when processing the user's transaction?"

The general strategy is to use an $\texttt{L1GasPriceFactor}$ such that

$$
\texttt{L2GasPrice} = \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor}
$$

### Example. (L1 gas price factor)

For a transaction with an L1 gas price of 20 Gwei, the L2 gas price in the Polygon zkEVM network is obtained with a 4% factor as follows:

$$
\texttt{L2GasPrice}\ =\ 20\ \text{Gwei}⋅0.04=0.8\ \text{Gwei}
$$

Current L2 fees can be viewed here [https://l2fees.info](https://l2fees.info/).

Although this factor is used in the Polygon zkEVM network, in fact $\texttt{L1GasPriceFactor}$ is set to $0.04$​, there are a few complications that need to be carefully considered. 

So the question remains: What gas price should the user sign transactions with?

There are 3 scenarios we aim to avoid when determining the $\texttt{L2GasPrice}$ to sign transactions with:

- Transactions getting rejected due to the $\texttt{SignedGasPrice}$ being less than L2's minimum expected gas price ($\texttt{L2MinGasPrice}$).
- Incurring losses in the L2 network because of high transaction gas costs.
- Transactions receiving the least priority for sequencing.
