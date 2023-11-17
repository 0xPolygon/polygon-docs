# What is Polygon PoS?

Polygon PoS, originally launched as Matic Network, has undergone significant transformations to address the evolving needs of blockchain scalability and security. Initially designed to scale Ethereum through a hybrid Plasma sidechain, the network is currently in the process of transitioning into a ZK-based validium solution on Ethereum. This evolution aims to offer enhanced scalability and robust security features.

In this transformation, Polygon PoS incorporates the execution environment of Polygon zkEVM along with a dedicated data availability layer. The architecture is inherently modular and composable, enabling it to seamlessly integrate into a broader fleet of layer-two scaling solutions. Despite its place in this diverse ecosystem, Polygon PoS will retain its role as a crucial "mainnet," serving as the foundational infrastructure for a wide array of decentralized applications and services.

## How PoS Works Today

### Transaction Lifecycle
The following cyclical workflow outlines the operational mechanics of today's Polygon PoS architecture:

1. **User Initiates Transaction**: On the Polygon PoS chain, typically via a smart contract function call.
2. **Validation by Public Plasma Checkpoint Nodes**: These nodes validate the transaction against the Polygon chain's current state.
3. **Checkpoint Creation and Submission**: A checkpoint of the validated transactions is created and submitted to the core contracts on the Ethereum mainnet.
4. **Verification by Core Contracts**: Utilizing Fraud Proofs, the core contracts verify the checkpoint's validity.
5. **Transaction Execution**: Upon successful verification, the transaction is executed and state changes are committed to the Matic Sidechain.
6. **Asset Transfer (Optional)**: If needed, assets can be transferred back to the Ethereum mainnet via the Plasma Exit Queue in the core contracts.
7. **Cycle Reiteration**: The process can be initiated again by the user, returning to step 1.

### Core Contracts on Ethereum Mainnet
Ethereum mainnet serves as the foundational layer upon which Polygon's PoS architecture is built. Within the Ethereum ecosystem, a set of core contracts play a pivotal role in connecting the Polygon PoS chain to Ethereum. These core contracts are responsible for a range of functionalities, from anchoring the Polygon chain to handling asset transfers.

The core contracts on the Ethereum mainnet incorporate two key features for security and functionality: Fraud Proofs and the Plasma Exit Queue. Fraud Proofs act as a security layer, enabling the validation of transactions and state changes to ensure transparency and security across operations. On the other hand, the Plasma Exit Queue manages the safe and efficient transfer of assets back to the Ethereum mainnet, allowing users to seamlessly move assets between the Polygon PoS chain and Ethereum without compromising data integrity or security.

### Public Plasma Checkpoint Nodes
Public Plasma Checkpoint Nodes serve as the validators in the Polygon PoS architecture. They perform two primary functions: transaction validation and checkpoint submission. When a transaction is initiated on the Polygon PoS chain, these nodes validate the transaction against the current state of the Polygon chain. After validating a set number of transactions, these nodes create a Merkle root of the transaction hashes, known as a "checkpoint," and submit it to the core contracts on the Ethereum mainnet.

The role of these nodes is crucial as they act as a bridge between the Ethereum mainnet and the Polygon PoS chain. They ensure data integrity and security by submitting cryptographic proofs to the core contracts on Ethereum.

### Polygon Sidechain
The Polygon Sidechain is where the actual transaction processing takes place. Unlike the Ethereum mainnet, which can get congested and has higher transaction costs, the Sidechain offers a more scalable and cost-effective solution. The blocks in the Sidechain are validated by the Public Plasma Checkpoint Nodes and are organized in a manner that allows for high throughput and low latency.