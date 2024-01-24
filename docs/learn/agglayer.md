# Aggregation layer

Solving the scalability problem in blockchains means scaling access to shared state and liquidity across many chains. To do so requires a new approach to blockchain architecture, namely, aggregated blockchains. Polygon Labs researchers and engineers have designed a solution–the **aggregation layer**, or **AggLayer**–which will seamlessly connect any ZK-enabled L2 or L1 chain.

In this document, we look at:

* What AggLayer is and the problems it addresses.
* A brief overview of how the AggLayer is implemented.
* The advantages of using an aggregated solution.

**![img](https://lh7-eu.googleusercontent.com/gusTl_jWu_eVU4RF32Y3LvQYG63nR9Ydi_qZQDNxTGyuhjlNsWvuRNMXJvr05bWZznFfedIu1smvHJsGP9nQgxbHipfpmrhQfN9dmvED20B4BSRI5fSP3MV3ztoYuqEAVIStTR-_Aynv7zVGLOPox9o)**

### Fragmented liquidity

Although developers have now the freedom to build on chains that suit their needs, or design their own chains, the current setup lacks cross-chain interoperability.

As seen in the above diagram, each chain connects directly to Ethereum. Since every chain has its separate and exclusive bridge contract, any transfer of assets from Chain A to Chain B must go via Ethereum. This means a simple cross-chain transfer of assets involves more chain interactions than necessary.

Reliance on bridging in order to connect what are essentially isolated networks, is a common interoperability solution. But it translates to fragmented liquidity, and a less than ideal user experience.

### Atomic guarantees

Let's take a deeper look at cross-chain transfers.

First of all, we understand execution of atomic cross-chain transactions to mean that, with every set of transactions a user submits to multiple chains, the user has the guarantee that either all transactions are executed successfully or none of them is included in any chain.[^1]

Consider the following example as a typical cross-chain transfer.

#### Atomic transfer example

Suppose Alice, who is on rollup A, wants to send 1 ETH to Bob who is on rollup B.

Assuming a shared native bridge for both rollups; 

- Alice burns her 1 ETH on rollup A and mints 1 ETH on rollup B.
- The 1 ETH minted by Alice gets transferred to Bob.

Critical in this is to guarantee that it should be impossible for Alice to do any of the following two things:
  
  1. Mint 1 ETH on rollup B without burning 1 ETH on rollup A.
  2. Burn 1 ETH on rollup A without being able to mint 1 ETH on B.

The security of atomic transactions is based on this critical guarantee that users do not lose their funds and cannot double spend their tokens.

Therefore, key to realizing a unified Polygon ecosystem is atomic guarantees. 


## AggLayer design

The solution to the current fragmentation is a single AggLayer, which can be setup as either centralized or decentralized.

This means L2 chains submit proofs and state updates to the AggLayer, where the proofs are aggregated and submitted to Ethereum. 

The overall design of AggLayer is outlined in three parts:

- Proof aggregation.
- Optimistic batch confirmation.
- Atomic cross-chain interaction.

Let's go over each part in detail.


### Proof aggregation

<!-- Multiple chains post proofs to the AggLayer that are then aggregated before being published to Ethereum. This way, the Polygon ecosystem can post an unlimited number of chain updates for the cost of a single chain’s update, amortizing the cost of proof verification across many more transactions, and allowing for more frequent finalization. -->

Here's what happens in the AggLayer when users interact with individual Polygon chains $C_i$.

<!-- These can be thought of as copies of the Polygon zkEVM chain.  -->
  
  1. Users submit transactions to each chain $C_i$. As usual, the sequencer of each $C_i$ (whether centralized or decentralized) orders and executes the transactions. Then generates a proof $\pi_i$ attesting to the fact that the updated state $S_i'$ of each $C_i$ is valid and is consistent with a list of messages for each chain $M_i$.

  2. Rather than submitting proofs $\{ \pi_i \}$ to Ethereum, chains submit $\{\pi_i, S_i', M_i\}$ to the AggLayer, which can run as a centralized or decentralized service.

  3. The AggLayer takes as inputs the proofs $\{\pi_i\}$ and the associated states $\{S'_i\}$ and the message list $\{M_i\}$. It arranges the proofs $\{\pi_i\}$ in a binary tree ordered by index, where each $\pi_i$ is assigned to a leaf node.

  4. For each proof $\pi_i$, the AggLayer generates a commitment to all messages $\{M_j\}$ associated with that proof. 
  
  5. At each parent node, the AggLayer generates a recursive proof $\pi'_i$ that verifies that both child proofs are valid, and a commitment to the union of messages associated with both child nodes.

  6. For the root node, the AggLayer produces an aggregated proof $\pi_{\text{final}}'$ which guarantees that all proofs for all chains in the Polygon ecosystem are valid, and that the messages $\{M_i\}$ associated with all chains are consistent with the proof $\pi_{\text{final}}'$.
  
  7. Optionally, the aggregated proof can also guarantee that a list of updated state roots $S_i$ is valid.

After producing the aggregated proof $\pi_{\text{final}}'$, the AggLayer posts that proof to Ethereum, along with a commitment to the message lists $M_i$.

The above procedure is depicted in the simplified diagram below.


**![img](https://lh7-eu.googleusercontent.com/5GJavrjHtRP1LC-N-MmG6yZjaN9QG0N4Xk8hl_lRAMIuuKl1KKLB2pQJz9AMX5u19renKi7acrVMQ2aos5X2bAmEFBnADlVTKpbHOxvny7luASdK_qYI-3L5u4GFb8PBjRpI2KOjYNFh-C-UoLdBbpE)**



#### Validium-case caveat

There's a subtle detail about validiums that needs to be noted.

For all rollup chains, we have all data necessary to retrieve the proof of inclusion for a particular message in some list $M_i$.

But this is not so with validium chains. For instance, there could be a 'data withholding' attack.

So we need to ensure that 'data withholding' attacks do no affect validium users' ability to process an exit or message from a rollup.

The solution that enables validium users to circumvent 'data withholding' attacks is, segmentation of rollup and validium message lists, as well as optionally posting the commitment to the message list for all validium nodes to Ethereum.  


#### Proof aggregation interface

The `submitBatch` data interface, used to transmit proofs between chains and the AggLayer, involves the following data elements. The below table records the interface data elements, their types and brief descriptions.

|          Field           |      Type       | Description                                                               |
| :----------------------: | :-------------: | ------------------------------------------------------------------------- |
|         Chain ID         |       Int       | Identifier for chain submitting a batch and proof                         |
|      New State Root      |      u256       | Commitment to the updated chain state                                     |
|       Batch Proof        | Plonky2/3 Proof | Proof guaranteeing validity of batch of tx                                |
|     Consensus Proof      | Plonky2/3 Proof | Proof of consensus for decentralized sequencers/signature for centralized |
|      Message Queue       |  Vec&lt;Message&gt;   | LxLy message queue resulting from batch                                   |
|         Calldata         |  Vec&lt;Calldata&gt;  | Calldata that must be posted to Ethereum                                  |
| Cross-Chain Dependencies |     Vec<*>      | Cross-chain state root dependencies and bundles that the batch builds on. |




### Optimistic confirmation

The problem with the aggregation layer, as described, is that it suffers from high latency. For a user to trust a message from another chain, they must have a proof that the message is the output of a valid batch, and a guarantee that the batch that produced the message has either already been, or will be finalized on Ethereum.
    
Currently, proving time for a batch is a few minutes, and batches are posted to Ethereum every 30-60 minutes, which prohibits fast cross-chain messaging and interoperability.
    
In order to reduce latency to levels that make cross-chain interactions feel like using a single chain, we need to safely confirm batches before:

  1. A proof is generated (validity).
  2. A batch is posted to Ethereum (finality).


#### Finality
    
We can derive the finality property from the aggregation layer: as soon as a batch is pre-confirmed by the aggregation layer, it is considered weakly finalized, meaning that it's only possible to revert a pre-confirmed batch and post a conflicting batch to Ethereum if both the aggregator layer and the chain collude. 

While it's possible that a chain could collude with the aggregation layer to fork, it's possible to slash both the aggregation layer and the chain for equivocation. Moreover, this attack already exists ith a single L2, as the sequencer RPC can confirm transactions for users before the transactions are posted to L1 and then publish a conflicting batch.
    
#### Validity
    
We can allow batches to be optimistically confirmed without proofs if we ensure that chains can safely receive messages. We do so as follows.
    
1. Chain A submits a batch and message queue without a validity proof to the AggLayer.
2. A user on Chain B submits a transaction that reads a message from Chain A before the validity proof is generated.
3. Chain B can confirm with the AggLayer the current pre-confirmed state of Chain A.
4. Chain B submits a batch and includes a claimed Batch Root and Message Queue for Chain A.
5. The validity proof for Chain B commits to the claimed Message Queue for Chain A.
6. The recursive proof generated by the AggLayer checks that the Message Queue for Chain A is consistent with the *claimed* Message Queue for Chain A by Chain B.
7. Either:
    - Chain A submits a validity proof that is consistent with the pre-confirmed batch, in which case the recursive proof can be generated.
    - Chain A fails to submit a validity proof. Chain B must roll back the transaction that depends on Chain A. Chain A is slashed. 

Fundamentally, this approach provides safety because it guarantees that a batch from Chain B that relies on a pre-confirmed batch from Chain A cannot be submitted to Ethereum if Chain A equivocates or has pre-confirmed an invalid batch. 
    
This is critical, because otherwise Chain B could read a message from Chain A, mint some number of tokens, and then Chain A could equivocate and mint the same number of tokens on Chain C, undercollateralizing the bridge. Using this approach, we can obtain both low latency and safety.

#### Optimistic-case interface

The `SubmitBatchWithoutProof` data interface is used to post batches to the Agglayer without a validity proof, and is of the form:

|           Field            |      Type      | Description                                                                 |
| :------------------------: | :------------: | :-------------------------------------------------------------------------- |
|          Chain ID          |      Int       | Identifier for chain submitting a batch and proof                           |
|       New State Root       |      u256      | Commitment to the updated chain state                                       |
|     Consensus Witness      | Vec&lt;Signature&gt; | Witness required to verify consensus for a chain                            |
|       Message Queue        |  Vec&lt;Message&gt;  | LxLy message queue resulting from batch                                     |
|          Calldata          | Vec&lt;Calldata&gt;  | Calldata that must be posted to Ethereum                                    |
| *Cross-Chain Dependencies* |     Vec<*>     | *Cross-chain state root dependencies and bundles that the batch builds on.* |




### Atomic Cross-Chain Interaction
    
The final part of the unified liquidity vision is to enable cross-chain atomic interactions. Cross-chain interactions as we've described them are only asynchronous - Chain A must submit a batch and message queue, then Chain B must submit a transaction in a new batch that reads from Chain A's message queue, and so on.
    
We want to instead provide truly seamless interaction and give users the experience of using a multi-chain ecosystem that feels like using a single chain. We can achieve this with atomicity. Users can submit a bundle of transactions to many chains in the Polygon ecosystem, with the guarantee that all transactions will be successfully executed, or none will be included.
    
#### AggLayer data interfaces 
    
**`SubmitBundle`**

|    Field     |               Type                | Description                                              |
| :----------: | :-------------------------------: | :------------------------------------------------------- |
| Bundle Root  |               u256                | Unique identifier or commitment for a transaction bundle |
| Transactions | Vec&lt;(ChainID, Transaction)&gt; | Chain, Transaction pairs                                 |

**`ConfirmBundle`**

|    Field    | Type  | Description                                              |
| :---------: | :---: | :------------------------------------------------------- |
| Bundle Root | u256  | Unique identifier or commitment for a transaction bundle |
    
#### Chain Interface
    
**`SubmitBundleTransaction`**

|    Field    |    Type     | Description                                              |
| :---------: | :---------: | :------------------------------------------------------- |
| Bundle Root |    u256     | Unique identifier or commitment for a transaction bundle |
| Transaction | Transaction | EVM Transaction                                          |
    
**`ConfirmBundleTransaction`**

|    Field    |     Type      | Description                                              |
| :---------: | :-----------: | :------------------------------------------------------- |
| Bundle Root |     u256      | Unique identifier or commitment for a transaction bundle |
| Transaction | TransactionID | Transaction Identifier                                   |


The atomic mode for cross-chain interaction largely follows the Shared Validity Sequencing approach, with the caveat that no shared sequencer is required for all chains. 
    
1. Users submit atomic bundles of transactions to the aggregator layer. For each bundle, an Aggregator Worker is spun up. The worker is a process running on a single node, charged with ensuring execution of all transactions in the bundle before the bundle can be included in a batch. 
2. Transactions from the bundle are forwarded to their respective chains by the worker.
3. Chains take a lock on the state affected by each transaction and sequence the bundle in a new block, returning the resulting message queue to the worker. If another transaction is received that touches state affected by the bundle, it's queued for execution until after the bundle is either confirmed or rejected.
4. If each transaction in the bundle executed correctly and the resulting message queues are consistent (ie tokens minted matches tokens burned), then the bundle is included by the aggregation layer.
5. Each chain generates a validity proof for the block containing the bundle. When all validity proofs are received by the AggLayer, chains can release the lock on affected state and execute queued transactions.


![](../img/learn/agglayer-1.png)


#### Failure Modes
    
**Liveness**: A malicious user can collude with a malicious chain and submit a bundle that's known to fail on a specific chain. The colluding chain will claim successful execution, the remaining chains will generate proofs, but the colluding chain will never submit a proof, causing the bundle to time out. 
    
This is an attack, but it's not unique to the atomic case. It also exists in the optimistic interop case, where Chain A might have a pre-confirmed batch that Chain B relies on for messages, but this batch is invalid or Chain A never submits a proof. Ultimately, the solution is to blacklist the colluding or unreliable chain from participating in atomic bundles or optimistic pre-confirmations.
    
**Griefing**: A malicious user and colluding chain can submit a bundle that touches a large amount of state on another chain, and then run the same liveness attack, preventing fast confirmations for many transactions on that chain.
    
Similar to the liveness attack, this will cause degradation of UX, but it's not a directly profitable attack, and it comes with a significant penalty for the misbehaving chain. Possible mitigation approaches include only allowing slashable chains to participate in atomic interop and optimistic confirmations.

## Aggregation vs. Modularity

Aggregation presents a solution to the monolithic vs. modular chain design dilemma. It takes the performance gains and efficient resource usage of modular architecture and combines it with the unified experience of a monolithic system.

The AggLayer will allow a single ZK proof to verify state across all chains in the ecosystem and use Ethereum as the settlement layer. Once any chain publishes a ZK proof of its latest state to the AggLayer, all other chains can trust the value (state) of that chain.


!!! credits

    The contents of this document were sourced from [a blog post](https://mirror.xyz/0xfa892B19c72c2D2C6B10dFce8Ff8E7a955b58A61/TXMyZhhRFa-bjr7YHwmJpKBwt2-_ysirbh_VpNy3qZY) originally written by Brendan Farmer, Co-founder @ Polygon on Sep 2023.


[^1]: Definition taken from "Shared Sequencing: Defragmenting the L2 Rollup Ecosystem" https://hackmd.io/@EspressoSystems/SharedSequencing by Espresso Systems
