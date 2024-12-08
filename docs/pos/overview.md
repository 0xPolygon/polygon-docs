The Polygon Proof-of-Stake (PoS) network is designed to address scalability challenges within the Ethereum ecosystem. It operates as an EVM-compatible Layer-2 (L2) scaling solution for Ethereum, enhancing its throughput while also significantly bringing down  gas costs, i.e., transaction fees.

## Dual layer architecture

Polygon PoS is a Proof-of-Stake Layer-2 (L2) network anchored to Ethereum, and is composed of the following two layers:

- Heimdall layer, a consensus layer consisting of a set of proof-of-stake Heimdall nodes for monitoring staking contracts deployed on the Ethereum mainnet, and committing the Polygon PoS network checkpoints to the Ethereum mainnet. The new version of Heimdall is based on [CometBFT](https://docs.cometbft.com/).

- Bor layer, an execution layer which is made up of a set of block-producing Bor nodes shuffled by Heimdall nodes. Bor is based on Go Ethereum (Geth).

## Transaction lifecycle

The following cyclical workflow outlines the operational mechanics of today's Polygon PoS architecture:

1. User initiates transaction: On the Polygon PoS chain, typically via a smart contract function call.
2. Validation by public checkpoint nodes: These nodes validate the transaction against the Polygon chain's current state.
3. Checkpoint creation and submission: A checkpoint of the validated transactions is created and submitted to the core contracts on the Ethereum mainnet every 30 minutes or so.
4. Verification by core contracts: Core contracts verify checkpoint validity
5. Transaction execution: Upon successful verification, the transaction is executed and state changes are committed to Polygon PoS.
6. Asset transfer (optional): If needed, assets can be withdrawn to the Ethereum mainnet via the exit queue in the core contracts.
7. Cycle reiteration: The process can be initiated again by the user, returning to step 1.

!!! info "Checkpoint verification and L2 transactions"

    Checkpoint verification plays an important role in ensuring the security of the PoS network, especially in the case of bridging, and other cross-chain transactions. In the case of simple transactions such as an L2 to L2 token transfer, the state finality is near instantaneous.

## Core contracts on Ethereum 

Ethereum serves as the foundational layer upon which Polygon's PoS architecture is built. Within the Ethereum ecosystem, a set of core contracts play an important role connecting Polygon PoS to Ethereum. These core contracts are responsible for a range of functionalities, from anchoring the Polygon chain to handling asset transfers.

The core contracts on the Ethereum mainnet incorporate a key feature for security and functionality: the exit queue. The exit queue manages the safe and efficient transfer of assets back to the Ethereum mainnet, allowing users to seamlessly move assets between the Polygon PoS chain and Ethereum without compromising data integrity or security.


## Public checkpoint nodes

Public checkpoint nodes serve as validators in the Polygon PoS architecture. They perform two primary functions: transaction validation and checkpoint submission. When a transaction is initiated on the Polygon PoS chain, these nodes validate the transaction against the current state of the Polygon chain. After validating a set number of transactions, these nodes create a Merkle root of the transaction hashes, known as a "checkpoint," and submit it to the core contracts on the Ethereum mainnet.

The role of these nodes is crucial as they act as a bridge between the Ethereum mainnet and the Polygon PoS chain. They ensure data integrity and security by submitting cryptographic proofs to the core contracts on Ethereum.

## Upcoming developments

Originally launched as Matic Network in June 2020, Polygon PoS has undergone numerous upgrades since its inception. Initially designed to scale Ethereum through a sidechain, a new proposal on the Polygon forum suggests upgrading Polygon PoS into a zero-knowledge (ZK)-based validium on Ethereum. Polygon PoS will soon adopt the execution environment of Polygon zkEVM along with a dedicated data availability layer. This new architecture would be inherently interoperable with a broader network of ZK-powered Ethereum L2s via the [AggLayer](../agglayer/overview.md).

Polygon PoS will continue to be the foundational infrastructure for a wide array of decentralized applications and services. More details about the overarching vision of a unified ecosystem of L2s on Ethereum can be found in [the innovation & design space](../innovation-design/index.md).