Users can sign transactions with gas prices higher than the suggested gas price for prioritized sequencing. That is,

$$
\texttt{SignedGasPrice} > \texttt{suggestedGasPrice}
$$

The priority ratio is defined as:

$$
\texttt{PriorityRatio} = \frac{\texttt{SignedGasPrice}}{\texttt{suggestedGasPrice}} - 1
$$

Any transaction with $\mathtt{SignedGasPrice \leq GasPriceSuggested}$, implies that the user has chosen not to have the transaction prioritized.

## Computing effective gas price

The computation of the effective gas price (or EGP) involves both the break even gas price and the priority ratio: 

$$
\texttt{EffectiveGasPrice} = \texttt{BreakEvenGasPrice} \cdot \big(1 + \texttt{PriorityRatio}\big)
$$

Among the transactions stored in the pool database, the transactions with higher $\texttt{effectiveGasPrice}$ are prioritized at the time of sequencing due to the added $\texttt{PriorityRatio}$.

### Gas consumption deviations

Since the actual gas consumed can deviate from the estimated gas consumption, we denote the estimated $\texttt{EGP}$ and the 'new' $\texttt{EGP}$ as $\texttt{EEGP}$ and $\texttt{NEGP}$, respectively.

The extent of the deviation can be computed as a percentage:

$$
\frac{|{\texttt{NEGP} - \texttt{EEGP}}|}{\texttt{EEGP}} \cdot 100
$$

The deviation percentage is compared to a parameter called $\texttt{FinalDeviationParameter}$, which is set to $10$.

This presents 2 scenarios and their corresponding consequences:

1. If the percentage deviation is lower than the final deviation parameter,
   
   $$
   \frac{|\texttt{NEGP} − \texttt{EEGP}|}{\texttt{EEGP}} \cdot 100 < \texttt{FinalDeviationParameter} = 10,
   $$
   
   it indicates that there is minimal distinction between charging the user with $\texttt{NEGP}$ compared to $\texttt{EEGP}$.
   
   Despite potential losses to the network, the user gets charged the $\texttt{EEGP}$ amount as the gas price. 

2. On the contrary, if the percentage deviation equals or exceeds the deviation parameter,
   
   $$
   \frac{|\texttt{NEGP} − \texttt{EEGP}|}{\texttt{EEGP}} \cdot 100 ≥ \texttt{FinalDeviationParameter}  = 10,
   $$
   
   the difference between executions can be so big it warrants adjustment of the gas price to be $\texttt{NEGP}$​, and thus mitigate against potential losses to the network.
   
### Effective percentage

The last parameter called the $\texttt{EffectivePercentage}$ is used to measure the unused portion of the user's signed gas price. 

In order to calculate the $\texttt{EffectivePercentage}$, one option is to consider pricing resources based on the number of consumed counters within the Polygon zkEVM's proving system.

However, understanding this metric can be challenging for users because stating the efficiency through counters is a bit complicated.

In favor of better UX, a formula involving gas is applied as it is more user-friendly.

The primary objective is to compute $\texttt{EffectivePercentage}$ exclusively using gas, while allowing users to prioritize their transactions through the use of gas price, without the need for complex considerations such as used ROM counters.

The effective percentage is computed as follows:

$$
\texttt{EffectivePercentage} = \frac{ \texttt{GasPriceFinal}}{ \texttt{SignedGasPrice}}
$$

where $\texttt{GasPriceFinal}$ is the gas price charged at the end of the entire processing by the sequencer. 

Note that the amount of wei that the user is charged for processing their transactions can be adjusted by modifying $\texttt{GasPriceFinal}$.

This $\texttt{EffectivePercentage}$ is provided by the sequencer as a single byte:

$$
\texttt{EffectivePercentageByte} \in \{ 0, 1, . . . , 255 \}
$$

which is computed from the $\texttt{EffectivePercentage}$ as follows:

$$
\texttt{EffectivePercentageByte} = \lfloor \texttt{EffectivePercentage} · 256 \rfloor − 1
$$

Since having $\texttt{EffectivePercentage}$ implies having $\texttt{EffectivePercentageByte}$ and vice versa, the two terms are used interchangeably. 

So, $\texttt{EffectivePercentageByte}$ is often referred to as $\texttt{EffectivePercentage}$.

**Example (Effective percentage)**

Setting an $\texttt{EffectivePercentageByte}$ of $255\ (= \texttt{0xFF})$ means the $\texttt{EffectivePercentage} = 1$. 

In which case the user would pay the gas price they signed with, when sending the transaction, in total. That is:

$$
\texttt{GasPriceFinal} = \texttt{SignedGasPrice}
$$

In contrast, setting $\texttt{EffectivePercentageByte}$ to $127$ means:

$$
\texttt{EffectivePercentage} = 0.5
$$

Thus, only half of the gas price the user signed with gets charged as the transaction cost:

$$
\texttt{GasPriceFinal} = \frac{\texttt{SignedGasPrice}}{2}
$$

The transaction execution incurs only half of the signed gas price.

## Concluding remarks

The effective gas price scheme, as outlined above, although steeped in details, takes all necessary factors and eventualities into consideration.

Ultimately, the scheme is accurate and fair to both the users and the zkEVM network.

Check out this [repo](https://github.com/0xPolygonHermez/zkevm-rom/issues/316) for a detailed example of how the effective gas price is calculated.

A more elaborate and expanded documentation of the EGP scheme can be found in the specifications section [here](../../spec/user-fees/index.md).
