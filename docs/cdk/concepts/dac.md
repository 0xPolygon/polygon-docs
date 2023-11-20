Validiums are blockchain solutions that don't store transaction data.

!!! quote
    See the [definition of validium](https://ethereum.org/en/developers/docs/scaling/validium/) on Ethereum.org's glossary.

Data availability in blockchain technology refers to whether or not transaction data is available onchain or off-chain. If data is available onchain, then each node has to store every piece of data related to every transaction. This can be costly for node operators as hardware and storage requirements are high. Moving data off-chain streamlines node architecture and operations.

A data availability committee (DAC) implements a data storage layer in a modular chain architecture like CDK.

## What is a DAC?

A data availability committee (DAC) is an off-chain network of nodes that provides data to a blockchain network. The advantages are:

- **Lower transaction fees**: Reduced computational requirements lead to lower fees.
- **State privacy**: A secure copy of state transitions ensures data integrity and privacy.

DACs store the data required to reconstruct the state of the blockchain and make that data accessible so that, if the blockchain goes down, users can still access their assets and data.

Delegating blockchain data to a DAC in this way can be costly. However, a DAC improves finality and thus supports Enterprise use cases which require cheap and fast transactions with a private and secure data layer.

The CDK validium DAC is a secure consortium of nodes that ensures off-chain data access. 

## DAC data flow

![CDK validium DAC dataflow](../../img/cdk/zksupernets-dac.png)

The DAC works together with the sequencer to control the flow of data. The process can be broken down as follows:

1. **Batch formation**: The sequencer collects user transactions and organizes them into batches.

2. **Batch authentication**: Once the batches are assembled, they are authenticated. The sequencer forwards the batch data and its corresponding hash to the DAC.

3. **Data validation and storage**:  The DAC nodes independently validate the batch data. Once validated, the hash is stored in each node's local database for future reference.

4. **Signature generation**: Each DAC node generates a signature for the batch hash. This serves as an endorsement of the batch's integrity and authenticity.

5. **Communication with Ethereum**: The sequencer collects the DAC members' signatures and the original batch hash and submits them to the Ethereum network for verification.

6. **Verification on Ethereum**: A designated smart contract on Ethereum verifies the submitted signatures against a list of valid DAC members and confirms that sufficient approval has been provided for the batch hash.

7. **Final settlement with zero-knowledge proof**: The aggregator prepares a proof for the batch via the prover and submits it to Ethereum. This proof confirms the validity of the batch's transactions without revealing their details. The chain state updates on Ethereum.


INCORPORATING:



## What do you Mean by Data Availability Layer?

In the realm of blockchain, data availability ensures that all nodes can access and verify the complete transaction history, which is crucial for maintaining the network's transparency, security, and integrity.

However, storing all transaction data on the main chain (L1) can lead to high costs and compromise privacy. Data availability layers tackle these issues by separating transaction execution from data storage. This allows for transaction data to be stored off-chain, reducing costs and enhancing privacy, while still being accessible for validation.

This separation introduces new challenges, such as ensuring the secure and reliable management of off-chain data. Features like the [<ins>DAC</ins>](#what-are-dacs) within the Polygon CDK framework address these concerns, offering trusted oversight of off-chain data.

The diagram below provides a high-level overview of the Polygon CDK Validium's approach to blockchain infrastructure.

<div align="center">
  <img src="" alt="bridge" width="90%" height="30%" />
</div>

## What are DACs?

Data Availability Committees (DACs) are a crucial element in many blockchain protocols, tasked with ensuring the reliability and accessibility of off-chain data. In essence, they verify the availability of data associated with specific blockchain blocks.

In the context of L2 solutions, DACs play a pivotal role in enhancing scalability. They aid in transferring significant computational work and data storage off-chain, thereby alleviating the burden on the main L1 blockchain.

The DAC is an integral element in the validium framework of the CDK, functioning as a secure consortium of nodes to maintain the accessibility and security of off-chain data. For an overview of how the DAC functions within the CDK, please explore the DAC guide, available [<ins>here</ins>](/docs/cdk/validium/dac.md).

> For a more detailed understanding of data availability, the Ethereum Foundation's guide on Data Availability is a great resource, accessible [<ins>here</ins>](https://ethereum.org/en/developers/docs/data-availability/).
## How do L2s Built with Polygon CDK Validium Function as App-chains?

Leveraging the power of Polygon's advanced [zkEVM technology](/docs/zkevm/), chains developed using the Polygon CDK offer a high-performance L2 scaling solution. Developers have the flexibility to choose the validium framework, which integrates a secure data availability layer managed by a [Data Availability Committee (DAC)](/docs/cdk/validium/dac.md). Chains built with the CDK can function like L1 blockchains tailored to specific business logic. However, as L2 solutions, they provide the advantage of near-infinite scalability. Designed with a user-centric approach, these chains prioritize core business functions and user engagement strategies without compromising on performance and scalability. The following diagram illustrates the high-level architecture of a chain developed using the Polygon CDK.

