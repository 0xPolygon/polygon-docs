Here's how you can accurately determine the gas price to sign your transactions with when submitting transactions to the Polygon zkEVM network.

Polygon zkEVM implements a mechanism called the Effective Gas Price (EGP) that guarantees fair gas fees in the interest of both the user and the network.

Now that the EGP is in place, you can reduce any chance for a transaction revert, while making sure that accepted transactions receive your preferred prioritization. Meanwhile, the zkEVM network incurs minimal to no loss.

## How gas fees work in Ethereum

In Ethereum, there are two adjustable parameters that have a direct impact on transaction gas fees:

- The $\texttt{gasLimit}$, which is the maximum amount of gas units the user is willing to buy in order for their transactions to be included in a block and processed on chain.
- The $\texttt{gasPrice}$, that is, the amount of ETH a user is willing to pay for 1 gas unit. For instance, a gas price of 10 Gwei means the user is willing to pay 0.00000001 ETH for each unit of gas.

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

Transactions get reverted if the $\texttt{gasUsed}$ is greater than the $\texttt{gasLimit}$. Otherwise, the transaction is successful. 

## Computing L2 gas fees

The L2 gas price cannot simply be set to be the same as the L1 gas price (especially in the case of rollups where the goal is to reduce gas fees).

Hence, we make the distinction between the two gas prices, and denote them as $\texttt{L2GasPrice}$ and $\texttt{L1GasPrice}$ respectively.

It is important to calculate the appropriate L2 gas price while ensuring that transactions are successfully executed.

Although the same formula is used, that is,

$$
\texttt{gasLimit} \cdot \texttt{gasPrice}
$$

and success is guaranteed if $\texttt{gasLimit}$ is greater than $\texttt{gasUsed}$, the gas used is determined by the gas cost for data availability plus the gas cost for transaction execution in L2.

That is, 

$$
\texttt{gasUsed} = \texttt{DataCost} + (\texttt{L2 Execution gas cost})
$$

The total fees paid by the user is given by:

$$
\texttt{TotalTxPrice} = \texttt{DataCost} \cdot \texttt{L1GasPrice} + (\texttt{L2 Execution gas cost}) \cdot \texttt{L2GasPrice}
$$

Note that data availability is charged in L1 using the prevailing L1 gas price at the time of posting data.

The main challenge is adjusting $\texttt{L2GasPrice}$ in terms of the $\texttt{L1GasPrice}$ to account for L2 resources spent when processing transactions.

The general strategy is to use an $\texttt{L1GasPriceFactor}$ such that

$$
\texttt{L2GasPrice} = \texttt{L1GasPrice} \cdot \texttt{L1GasPriceFactor}
$$

### Example (L1 gas price factor)

For a transaction with an L1 gas price of 20 Gwei, the L2 gas price in the Polygon zkEVM network is calculated using a 4% factor as follows:

$$
\texttt{L2GasPrice}\ =\ 20\ \text{Gwei}⋅0.04=0.8\ \text{Gwei}
$$

Current L2 fees can be viewed here [https://l2fees.info](https://l2fees.info/).

The $\texttt{L1GasPriceFactor}$ is used in the Polygon zkEVM network and is set to $0.04$​. 

There are a few complications that need to be carefully considered. 


There are 3 scenarios we aim to avoid when determining the $\texttt{L2GasPrice}$ to sign transactions with:

- Transactions getting rejected due to the $\texttt{SignedGasPrice}$ being less than L2's minimum expected gas price ($\texttt{L2MinGasPrice}$).
- Incurring losses in the L2 network because of high transaction gas costs.
- Transactions receiving the least priority for sequencing.
