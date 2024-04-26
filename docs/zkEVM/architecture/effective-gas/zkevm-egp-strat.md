This document presents an outline of the Polygon zkEVM's strategy toward executing transactions with the most accurate effective gas price.

- **Poll for L1 gas price regularly**
    
    Since the L1 gas price fluctuates and the L2 gas price relies on it, it is necessary to run frequent polls on the L1 gas price, and thus have the most recent value at a given point in time.

    The Polygon zkEVM polls for the L1 gas price in regular intervals of 5 seconds.

    The polled gas prices are used to set the expected 'signed gas price', called $\texttt{MinL2GasPrice}$.


- **Provide suggested gas prices**
    
    The polled L1 gas price values are sent to users as per individual request.

    A grace time-interval of 5 minutes, called $\texttt{MinAllowedPriceInterval}$, is given to the user.

    It is recommended that the user sign their transactions with a gas price that is greater than the least of the gas prices in the 5-minute interval, otherwise is rejected for the RPC pre-execution stage.


- **Pre-execute transactions at the RPC level**
    
    Pre-execution of transactions involves:
        
    (a) Estimation of each transaction's possible consumption of L2 resources. That is, determining an approximate gas cost.

    (b) Checking user’s signed gas price against the expected $\texttt{MinL2GasPrice}$. Store the transaction in the Pool if $\texttt{SignedGasPrice} < \texttt{MinL2GasPrice}$​. Otherwise discard it.

    (c\) The Pool here refers to a collection of transactions waiting to be selected for execution by the sequencer.


- **Put in place a criterion for determining which transactions to store in the Pool**
    
    Not all transactions qualify to be stored in the Pool, but only those that satisfy this criterion.

    The user's signed gas price is checked against either some breakeven factor or the gas price suggested to the user.


- **Establish a criterion for when to execute transactions with user's signed gas price**
    
    Some users' signed gas prices may be sufficiently high for the user to deserve some savings. In such cases the sequencer can execute transactions with a much lower gas price.

    Hence, there's a need for a criterion that determines whether a transaction gets executed with the user's signed gas price, or the effective gas price as per the RPC estimation.


- **Set a criterion for when to execute transactions with RPC-estimated EGP**
    
    The effective gas price computed with the RPC-estimated gas price could be a lot higher than the actual gas price computed with the current state. In this case, the system can further optimize gas usage and help the user save on gas fees.

    The strategy here is to have a criterion that determines whether a transaction should get executed with the RPC-estimated effective gas price (EEGP) or the new effective gas price (NEGP), which results from the actual gas price.


- **Checking whether transactions include special opcodes**
    
    The presence of opcodes such as $\texttt{GASPRICE}$ and $\texttt{BALANCE}$ in transactions can result in higher gas usage.

    zkEVM executes such transactions with the user's signed gas price.


- **Enhancing prioritization of transactions**
    
    Since transactions are sequenced according to the value they carry, with high preference given to large values, users need to provision sufficient gas price to allow for prioritization of transactions according to their needs.

    ![Figure: Pre-excution scheme](../../../img/zkEVM/rpc-tx-preexec.png)