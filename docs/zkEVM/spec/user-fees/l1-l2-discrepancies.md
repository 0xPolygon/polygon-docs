As mentioned above, gas in Ethereum is used to account for the resources used by a transaction.

It takes two elements into account:

- **data availability**, which is measured in the transaction bytes.
- **processing resources**, such as CPU, Memory and Storage.

A notable challenge arises when certain operations consume low gas in L1, but represent a major cost in L2.

In other words, the reduction factor expressed in the L1-L2 gas price relationship:

$$
\texttt{L2GasPrice} = \texttt{L1GasPrice} · \texttt{L1GasPriceFactor}
$$

may not be constant among all the computational resources, introducing a problem.

L2 execution costs are variable, depending on the state of the transaction and typically offer a smaller cost per gas. 

However, the costs associated with data availability are fixed once the transaction is known, and they are directly proportional to L1 data availability costs. 

Consequently, in the zkEVM pricing schema, L2 transactions with high data availability costs and small execution costs are a significant challenge. This presents another pricing misalignment issue we need to face.

### Possible solutions

Recall that the Ethereum fees in L1 are computed as:

$$
\texttt{gasUsed} \cdot \texttt{gasPrice}
$$

giving us two ways of solving the misalignment problem between costs in L1 and L2:

**Option A**: Increasing the $\texttt{gasUsed}$, which is the approach taken by Arbitrum.

This approach involves modifying the gas schema to elevate the gas costs associated with data availability. While this strategy is relatively straightforward to implement and comprehend, it comes with a notable implication: **it changes the Ethereum protocol**. 

An L1 Ethereum transaction may execute different when compared to the same transaction executed in L2.

**Option B**: Increasing the $\texttt{gasPrice}$ to what is herein referred to as the **Effective Gas Price Approach**.

If we aim to avoid modifying the gas model, the alternative is to increase the gas price to cover the costs. 

Unlike the Option A approach, this doesn’t alter the Ethereum specifications.

However, determining a fair gas price becomes a complex task. Moreover, we have to take into account the need for L2 user to add incentive for their transactions to be prioritized, which further increases gas price.

This is the approach taken by the zkEVM team.

### Effective gas price approach

We will now develop how the **Effective Gas Price Approach** works.

First, the user signs a relatively high gas price at the time of sending the L2 transaction. Later on, by pre-executing the sent transaction, the sequencer establishes a fair gas price according to the amount of resources to be used.

To do so, the sequencer provides an $\texttt{EffectivePercentage}$, which represents the portion of the total charged to the user.

In other words, this percentage will be used to compute the factor of the signed transaction’s gas price which should be refunded to the user.

In order to calculate the $\texttt{EffectivePercentage}$, one option is to consider the pricing resources based on the number of consumed counters within our proving system.

However, understanding this metric can be challenging for users because stating the efficiency through counters is not intuitive at the time of prioritizing their transactions.

For the sake of a positive user experience, a better alternative is to consider a formula where gas is used, as it is more user-friendly.

So, the primary objective is to compute $\texttt{EffectivePercentage}$ exclusively using gas, while allowing users to prioritize their transactions through the use of gas price, without the need for intricate counter-based considerations.

The effective percentage is computed as follows:

$$
\texttt{EffectivePercentage} = \frac{ \texttt{GasPriceFinal}}{ \texttt{SignedGasPrice}}
$$

where $\texttt{GasPriceFinal}$ is the gas price charged at the end of the entire processing by the sequencer. 

Observe that, by modifying $\texttt{GasPriceFinal}$, the amount of Wei that the user is charged for processing their sent transactions can be adjusted.

This $\texttt{EffectivePercentage}$ is provided by the sequencer as a single byte:

$$
\texttt{EffectivePercentageByte} \in \{ 0, 1, . . . , 255 \}
$$

which is computed from the $\texttt{EffectivePercentage}$:

$$
\texttt{EffectivePercentageByte} = (\texttt{EffectivePercentage} · 256) − 1
$$

Since having $\texttt{EffectivePercentage}$ implies having $\texttt{EffectivePercentageByte}$ and vice versa, the two terms can be used interchangeably. So, the $\texttt{EffectivePercentageByte}$ is often referred to as just $\texttt{EffectivePercentage}$.

**Example**

Setting an $\texttt{EffectivePercentageByte}$ of $255\ (= \texttt{0xFF})$ means the $\texttt{EffectivePercentage} = 1$. 

In which case the user would pay the totality of the gas price they signed with, when sending the transaction. That is:

$$
\texttt{GasPriceFinal} = \texttt{SignedGasPrice}
$$

In contrast, setting $\texttt{EffectivePercentageByte}$ to $127$ means:

$$
\texttt{EffectivePercentage} = 0.5
$$

so, only a half of the gas price the user signed with gets charged as the transaction cost:

$$
\texttt{GasPriceFinal} = \frac{\texttt{SignedGasPrice}}{2}
$$

The user therefore gets a refund which is half of the price he initially signed with.

Observe that users must trust the sequencer in this schema.
