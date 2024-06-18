Over the past few years, several L2 solutions have been developed to enhance the scalability of the Ethereum network, with a focus on increasing transaction throughput. The benefit for users of the Ethereum network is to lower gas fees without compromising decentralization and security.

Polygon zkEVM is an L2 rollup solution that combines data availability and execution verification on L1, the Ethereum network, in order to ensure security and reliability of each L2 state transition.

This section describes the overall design of the Polygon zkEVM. It thus provides an architectural overview of its protocol.

## Components

It takes three main components of the Polygon zkEVM protocol to enable transaction finality while ensuring the correctness of state transitions:

- The trusted sequencer.
- The trusted aggregator.
- The consensus contract (`PolygonZkEVM.sol`, deployed on L1).

### Trusted sequencer

The trusted sequencer receives L2 transactions from users, orders them, generates blocks of transactions, fills batches, and submits them to the consensus contract's storage slots in the form of sequences.

The trusted sequencer processes batches and distributes them to L2 network nodes to achieve immediate finality and reduce costs associated with high network usage, all before submitting them to L1.

The trusted sequencer runs a zkEVM node in sequencer mode and controls an Ethereum account regulated by a consensus contract.

### Trusted aggregator

The trusted aggregator computes the L2 state based on batches of L2 transactions executed by the trusted sequencer.

On the other hand, the primary function of the trusted aggregator is to receive the L2 batches validated by the trusted sequencer and produce zero-knowledge proofs verifying the computational integrity of these batches. The aggregator achieves this by employing a specialized off-chain EVM interpreter to generate the ZK proofs.

The logic within the consensus contract verifies the zero-knowledge proofs, thereby endowing the zkEVM with the security of Layer 1. Before committing new L2 state roots to the consensus contract, verification is essential. A validated proof serves as undeniable evidence that a particular sequence of batches resulted in a specific L2 state.

!!!info
     L2 state root

     An L2 state root is a cryptographic hash value of the L2 state. In case you want to read more about state roots, please check out [this article](https://ethereum.org/en/developers/docs/scaling/zk-rollups/#state-commitments).

The trusted aggregator runs a zkEVM node in aggregator mode and controls an Ethereum account regulated by a consensus contract.

### Consensus contract

The consensus contract used by both the trusted sequencer and the trusted aggregator in their interactions with L1 is the `PolygonZkEVM.sol` contract.

The trusted sequencer can commit batch sequences to L1 and store them in the `PolygonZkEVM.sol` contract, creating a historical repository of sequences.

The `PolygonZkEVM.sol` contract also enables the aggregator to publicly verify transitions from one L2 state root to the next. The consensus contract accomplishes this by validating the aggregator's zk-proofs, which attest to proper execution of transaction batches.

## zkEVM node execution modes

zkEVM node is a software package containing all components needed to run zkEVM network. It can be run in three different modes; as a sequencer, an aggregator, or RPC.

### Sequencer mode

In the sequencer mode, the node holds an instance of L2 state, manages batch broadcasting to other L2 network nodes, and has a built-in API to handle L2 user interactions (transaction requests and L2 State queries).

There is also a database to temporarily store transactions that have not yet been ordered and executed (pending transactions pool), as well as all the components required to interact with L1 in order to sequence transaction batches and keep its local L2 state up to date.

### Aggregator mode

In the aggregator mode, the node has all the components needed to execute transaction batches, compute the resulting L2 state and generate the zero-knowledge proofs of computational integrity.

Also, it has all the components needed to fetch transaction batches committed in L1 by the trusted sequencer and call the functions to publicly verify the L2 state transitions on L1.

### RPC mode

In this mode, the zKEVM node has limited functionality. It primarily maintains an up-to-date instance of the L2 state, initially with respect to batches broadcast by the trusted sequencer, and later with sequences of batches fetched from the consensus contract.

The RPC node continuously interacts with L1 to keep the local L2 state up-to-date and to verify the synchronization of L2 state roots. By default, the synchronizer updates every 2 seconds, unless a different interval is specified in the configuration.
