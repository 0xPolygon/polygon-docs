The central entity responsible for assembling batches for sequencing is the trusted sequencer, which is built and managed by Polygon.

This sequencer may omit Layer 2 transactions therefore we have implemented [anti-censorship mechanism](https://docs.polygon.technology/zkEVM/architecture/protocol/malfunction-resistance/sequencer-resistance/).

The diagram below shows the sequencing workflow.

![Figure: ](../../../img/zkEVM/sqb-l2-txs-seq-batches.png)

1. L2 transactions via JSON RPC.
2. Transactions stored in the pool DB.
3. Trusted sequencer selects transactions from pool DB.
4. Trusted sequencer batches and sequences transactions.

## Batch pre-execution

The initial step in creating a batch involves verifying whether the chosen transactions align with execution parameters and do not surpass the gas limit. This step is known as _batch pre-execution_.

It is carried out by the sequencer through an executor, as depicted in the figure below.

![Figure: Pre-execution](../../../img/zkEVM/sqb-batch-preexecution.png)

While no proof is generated during the pre-execution stage, it ensures that the subsequent proof generation process by the prover can be successfully accomplished. This expedites the overall sequencing of batches.

A fast executor is employed, which is a _single-computation_ executor, making it capable of executing within blocktime.

The sequencer communicates with this executor to perform the pre-execution process swiftly.

Upon determining the transactions that correctly fill a specific batch through successful batch pre-execution, the sequencer records the batch in the node’s StateDB as a _closed batch_. 

Closure may occur when either one of the following conditions is fulfilled:

- The maximum number of execution trace rows is reached. 
- The maximum gas limit is attained. 
- The allocated time expires.

During batch pre-execution, and for batch closure, the sequencer and the executor update the Merkle tree of the zkEVM with L2 state changes, which is stored in the Prover HashDB. This is illustrated the figure below.

![Figure: Update L2 state](../../../img/zkEVM/sqb-l2-state-update-01.png)

The zkEVM's throughput depends highly on the speed at which we are able to close batches, which is directly impacted by the batch pre-execution process.

In fact, most of the performance problems occur here because excessive interaction with the HashDB is inefficient.

Efforts are currently underway to optimize this process:

- Reducing the time spent on frequent updates during transaction processing, by accumulating all state changes caused by a transaction, and only update the HashDB at the end of a transaction's pre-execution.

## Sending batches to L1

The next step is to send a call to the smart contract to sequence batches.

Once a batch is closed, the sequencer stores the data of the batch in the node’s StateDB.

Then, the $\texttt{sequenceSender}$ looks for closed batches and sends them to the [L1 smart contract](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVM.sol) via the $\texttt{EthTxManager}$, who makes sure that the transaction is included in a batch.

This process is depicted in the figure below.

![Figure: Sequence sender and ETH Tx Manager](../../../img/zkEVM/sqb-seq-sender-tx-manager.png)

In order to sequence a batch, the sequencer calls the $\texttt{sequenceBatches()}$ function in the L1 Smart Contract.

The name of the function is in plural because it is capable of sequencing several batches at once.

This step provides L2 data availability in the L1 execution layer, because we are registering in L1 all the bytes of the L2 transactions.

The calldata for the L1 $\texttt{sequenceBatches()}$​ function needs to include the following information:

- The L2 transactions’ data, which is an array containing data for each batch. It includes all transactions within the batch along with a timestamp indicating its closure time. 
- Additionally, the L2 coinbase address, representing the Ethereum address for receiving user fees.
- Lastly, a timestamp indicating when the L2 transactions were sequenced.

The L2 coinbase address serves as a critical destination for rewards earned by the sequencer in the Layer 2 environment.

The sequencer undertakes the responsibility of paying for data availability in Layer 1 using L1 Ether.

When the sequencer successfully closes a batch and executes transactions, they receive a reward for their services. This reward, denominated in L2 Ether, is routed to the L2 coinbase address.

Crucially, the L2 coinbase address is situated within Layer 2 because users compensate the sequencer with L2 Ether. 

This L2 Ether, representing the reward, is a reflection of the Ether in L1 that users have previously transferred to L2 through transactions via the Bridge.

Importantly, there exists a direct and fixed one-to-one correspondence between L1 ETH and L2 ETH, as we can observe in the figure below.

![Figure: L1 ETH and L2 ETH equivalence](../../../img/zkEVM/sqb-l1-and-l2-eth-equiv.png)

## Accumulated input hash pointers

Let's briefly explain how the sequencing operation and the proving process link up.

In particularly, we look at how the prover can match each sequenced batch with its data.

When the smart contract receives a call to sequence batches, it initiates creation of cryptographic pointers for each batch.

These pointers play a crucial role in identifying a batch uniquely, specifying its position, and encapsulating its data.

Subsequently, provers utilize these pointers as references during the proving process, allowing them to precisely identify the batch being proved and retrieve its associated data.

The use of cryptographic pointers ensures a robust and unambiguous link between the sequencing operation and the corresponding batch data for subsequent verification.

![Figure: Sequence of batches - ... timeline](../../../img/zkEVM/sqb-batches-timeline.png)

These pointers are constructed using a hash that accumulates data, incorporating information from all preceding blocks.

The procedural steps for this process are illustrated in the figure below:

![Figure: Stringing together batch hash data](../../../img/zkEVM/sqb-stringing-batches-together.png)

Pointers are generated by executing the KECCAK hash function on:

- The preceding pointer.
- The transactions encompassed within the L2 batch.
- The batch timestamp. 
- The L2 coinbase.

Due to the inter-connected nature of their creation, with each pointer encapsulating the previous one in the input of the hash, they are aptly referred to as *accumulated input hash* or $\texttt{accInputHash}$.

Such a construction, where previous pointers are linked to the current pointer, guarantees that batch data is proved in the correct and sequential order.

Upon completion of the sequencing process, the batch enters a state of being *virtualized*, residing within a _virtual state_.
