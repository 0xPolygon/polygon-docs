In this phase of the end-to-end transaction flow, transactions go through different stages, depending on the user's $\texttt{GasPriceSigned}$:

1. Sequencing transactions from the pool.
2. Estimating the effective gas price (EEGP) using the current $\texttt{L1GasPrice}$ and RPC's estimated $\texttt{GasUsedRPC}$.
    
    $$
    \texttt{EffectiveGasPrice} = \texttt{BreakEvenGasPrice} \cdot \big(1 + \texttt{PriorityRatio}\big)
    $$

    where the priority ratio is given by:

    $$
    \texttt{PriorityRatio} = \frac{\texttt{SignedGasPrice}}{\texttt{suggestedGasPrice}} - 1
    $$

    Depending on whether $\texttt{GasPriceSigned} \leq \texttt{EEGP}$ or not, transactions get executed with either the $\texttt{GasPriceSigned}$ or the $\texttt{EEGP}$.

3. Amongst the transactions that are computed with the $\texttt{EEGP}$, further savings can be made by:
    
    - Computing the new effective gas price (NEGP), using the current state and the EEGP.
    - Calculating the gas consumption deviation percentage and compare it to a fixed deviation parameter. i.e., $\texttt{FinalDeviationParameter} = 10$.
    - There's no further execution if the gas consumption deviation percentage is less than the fixed parameter, $\texttt{FinalDeviationParameter} = 10$.
    - Otherwise, check if $\texttt{GasPriceSigned} \leq \texttt{NEGP}$. If true, then execute transactions again using the $\texttt{GasPriceSigned}$. If false, continue to the next stage.

4. Checking the usage of $\texttt{GASPRICE}$ and $\texttt{BALANCE}$ opcodes.
    
    - Transactions with these two opcodes get executed with the $\texttt{GasPriceSigned}$.
    - Otherwise, they are executed with the $\texttt{NEGP}$.

   Since the sequencer is obliged to execute all transactions in the pool, any of the above stages leads to some execution of transactions.

   The entire sequencer flow is summarized in the figure below.

   ![Figure: Sequencer flow](../../../../img/zkEVM/tx-flow-seq-component.png)
