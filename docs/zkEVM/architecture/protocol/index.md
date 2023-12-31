Various layer 2 solutions aimed at improving the scalability of the Ethereum network, primarily transaction throughput, have been developed over the past years. The ultimate and intended benefit for Ethereum network users is a reduction in gas fees, while maintaining decentralisation and security.

Polygon zkEVM is a layer 2 rollup solution that combines data availability and execution verification in layer 1 of the Ethereum blockchain to ensure L2 state transition security and reliability.

This section will describe the infrastructure that Polygon designed and implemented for its zkEVM, with a focus on providing an overview of the components used in the development of the zkEVM Protocol.

## Components

This section describes the components used in the Polygon zkEVM to enable transaction finality while ensuring the correctness of state transitions.

The three main components of zkEVM protocol are:

- Trusted sequencer.
- Trusted aggregator.
- Consensus contract (PolygonZkEVM.sol, deployed on L1).

### Trusted sequencer

The trusted sequencer component is in charge of receiving L2 transactions from users, ordering them, generating batches, and submitting them to the consensus contract's storage slots in the form of sequences.

The sequencer executes and broadcasts batches of transactions to L2 network nodes in order to achieve fast finality and reduce costs associated with high network usage. That's before even submitting them to L1.

The Trusted sequencer must run a zkEVM node in sequencer mode and be in control of a consensus contract-enforced Ethereum account.

### Trusted aggregator

The trusted aggregator component can compute the L2 State based on batches of L2 transactions executed by the trusted sequencer.

The main role of the trusted aggregator, on the other hand, is to take the L2 batches committed by the trusted sequencer and generate zero-Knowledge proofs attesting to the batches' computational integrity. These ZK proofs are generated by the aggregator using a special off-chain EVM interpreter.

The consensus contract's logic validates the zero-Knowledge proofs, resulting in the zkEVM inheriting the L1 security. Verification is required before committing new L2 state roots to the consensus contract. A verified proof is an irrefutable evidence that a given sequence of batches led to a specific L2 state.

!!!info
     L2 state root

     An L2 state root is a concise cryptographic digest of the L2 state. In case you want to read more about state roots, please check out [this article](https://ethereum.org/en/developers/docs/scaling/zk-rollups/#state-commitments).

The trusted aggregator should run a zkEVM node in aggregator mode and must control a specific Ethereum account enforced in a consensus contract.

### Consensus contract

The consensus contract used by both the trusted sequencer and the trusted aggregator in their interactions with L1 is the `PolygonZkEVM.sol` contract.

The trusted sequencer can commit batch sequences to L1 and store them in the `PolygonZkEVM.sol` contract, creating a historical repository of sequences.

The `PolygonZkEVM.sol` contract also enables the aggregator to publicly verify transitions from one L2 state root to the next. The consensus contract accomplishes this by validating the aggregator's zk-proofs, which attest to the proper execution of transaction batches.

## zkEVM node execution modes

zkEVM node is a software package containing all components needed to run zkEVM network. It can be run in three different modes; as a sequencer, an aggregator, or RPC.

### Sequencer mode

In the sequencer mode, the node holds an instance of L2 state, manages batch broadcasting to other L2 network nodes, and has a built-in API to handle L2 user interactions (transaction requests and L2 State queries).

There is also a database to temporarily store transactions that have not yet been ordered and executed (pending transactions pool), as well as all the components required to interact with L1 in order to sequence transaction batches and keep its local L2 state up to date.

### Aggregator mode

In the aggregator mode, the node has all the components needed to execute transaction batches, compute the resulting L2 state and generate the zero-knowledge proofs of computational integrity.

Also, has all the components needed to fetch transaction batches committed in L1 by the trusted sequencer and call the functions to publicly verify the L2 state transitions on L1.

### RPC mode

In the RPC mode, the zKEVM node has a limited functionality. It primarily maintains an up-to-date instance of L2 state, initially with respect to batches broadcast by the trusted sequencer, and later with sequences of batches fetched from the consensus contract.

The node continuously interacts with L1 in order to keep the local L2 state up to date, as well as to check the synchronization of L2 state roots. The default syncing rate for the synchronizer is every 2 seconds, unless stipulated otherwise in the configuration.
