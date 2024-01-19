The Polygon Proof-of-Stake (PoS) network, originally launched as Matic Network in June 2020, has been upgraded a number of times since inception. Initially designed to scale Ethereum through a sidechain, a new discussion on the Polygon forum proposes upgrading Polygon PoS into a zero-knowledge (ZK)-based validium on Ethereum.

If passed, Polygon PoS would adopt the execution environment of Polygon zkEVM along with a dedicated data availability layer. The new architecture would be inherently interoperable, through an in-development interop-layer, with a broader network of ZK-powered Layer 2 (L2) chains on Ethereum.

Polygon PoS will continue to be foundational infrastructure for a wide array of decentralized applications and services. More details about the overarching vision of a unified ecosystem of L2s on Ethereum can be found in the Learn section.

## Transaction lifecycle

The following cyclical workflow outlines the operational mechanics of today's Polygon PoS architecture:

1. **User initiates transaction**: On the Polygon PoS chain, typically via a smart contract function call.
2. **Validation by public checkpoint nodes**: These nodes validate the transaction against the Polygon chain's current state.
3. **Checkpoint creation and submission**: A checkpoint of the validated transactions is created and submitted to the core contracts on the Ethereum mainnet.
4. **Verification by core contracts**: Core contracts verify the checkpoint's validity, with the added security of fraud proofs. 
5. **Transaction execution**: Upon successful verification, the transaction is executed and state changes are committed to the Polygon sidechain.
6. **Asset transfer (optional)**: If needed, assets can be transferred back to the Ethereum mainnet via the exit queue in the core contracts.
7. **Cycle reiteration**: The process can be initiated again by the user, returning to step 1.


## Core contracts on Ethereum 

Ethereum serves as the foundational layer upon which Polygon's PoS architecture is built. Within the Ethereum ecosystem, a set of core contracts play an important role connecting Polygon PoS to Ethereum. These core contracts are responsible for a range of functionalities, from anchoring the Polygon chain to handling asset transfers.

The core contracts on the Ethereum mainnet incorporate two key features for security and functionality: fraud proofs and the exit queue. Fraud proofs act as a security layer, enabling the validation of transactions and state changes to ensure transparency and security across operations. The exit queue manages the safe and efficient transfer of assets back to the Ethereum mainnet, allowing users to seamlessly move assets between the Polygon PoS chain and Ethereum without compromising data integrity or security.


## Public checkpoint nodes

Public checkpoint nodes serve as validators in the Polygon PoS architecture. They perform two primary functions: transaction validation and checkpoint submission. When a transaction is initiated on the Polygon PoS chain, these nodes validate the transaction against the current state of the Polygon chain. After validating a set number of transactions, these nodes create a Merkle root of the transaction hashes, known as a "checkpoint," and submit it to the core contracts on the Ethereum mainnet.

The role of these nodes is crucial as they act as a bridge between the Ethereum mainnet and the Polygon PoS chain. They ensure data integrity and security by submitting cryptographic proofs to the core contracts on Ethereum.

## Polygon sidechain

The Polygon sidechain is where transaction processing occurs. Unlike the Ethereum mainnet, which can get congested and has higher transaction costs, the sidechain offers a more scalable and cost-effective solution. The blocks in the sidechain are validated by the public checkpoint nodes and are organized in a manner that allows for high throughput and low latency.
