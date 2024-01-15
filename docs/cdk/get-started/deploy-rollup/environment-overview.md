## Overview of the full environment

Implementing the full stack Polygon CDK zkRollup EVM-compatible network involves more than just running a node and the prover to validate batches and deploy smart contracts. In its entirety, it encompasses all these processes and more.

The common rollup actors are the sequencer, the aggregator, the synchroniser and the JSON RPC node. All these affect the L2 state.

Also, the aggregator uses the prover to avail verifiable proofs of sequenced batches. And the sequenced batches are composed of transactions taken from the pool database.

This highlights just a few main components. The rest of the components and those working in the background, are listed in the next subsection.

### Why you need Docker

The modular design of the CDK zkRollup EVM-compatible network allows for most components to be separately instantiated, and we therefore run each of these instances in a separate Docker container.

The below table enlists all the CDK zkRollup EVM-compatible components/services and their corresponding container-names.

Our CDK zkRollup deployment-guide provides CLI commands to automatically create these Docker containers.

| Component         | Container            | Brief\ Description                                           |
| :---------------- | :------------------- | ------------------------------------------------------------ |
| Sequencer         | zkevm-sequencer      | Fetches txs from the pool DB, checks if valid, then puts valid ones into a batch. |
| Aggregator        | zkevm-aggregator     | Validates sequenced batches by generating verifiable zero-knowledge proofs. |
| Synchronizer      | zkevm-sync           | Updates the state by fetching data from Ethereum through the Etherman. |
| JSON RPC          | zkevm-rpc            | An interface for interacting with the network. e.g., Metamask, Etherscan or Bridge. |
| State DB          | zkevm-state-db       | A database for permanently storing state data (apart from the Merkle tree). |
| Prover            | zkevm-prover-server  | Used by the aggregator to create zk-proofs. Runs on an external cloud server. |
| Pool DB           | zkevm-pool-db        | Stores txs from the RPC nodes, waiting to be put in a batch by the sequencer. |
| Executor          | zkevm-executor       | Executes all processes. Collects results’ metadata (state root, receipts, logs) |
| Etherman          | zkevm-eth-tx-manager | Implements methods for all interactions with the L1 network and smart contracts. |
| Bridge UI         | zkevm-bridge-ui      | User-interface for bridging ERC-20 tokens between L2 and L1 or another L2. |
| Bridge DB         | zkevm-bridge-db      | A database for storing bridge-related transactions data.     |
| Bridge service    | zkevm-bridge-service | A backend service enabling clients like the web UI to interact with bridge smart contracts. |
| zkEVM explorer    | zkevm-explorer-l2    | L2 network's block explorer. i.e., The zkRollup Etherscan [rxplorer](https://zkevm.polygonscan.com). |
| zkEVM explorer DB | zkevm-explorer-l2-db | Database for the L2 network's Block explorer. i.e., Where all the zkRollup Etherscan explorer queries are made. |
| Gas pricer        | zkevm-l2gaspricer    | Responsible for suggesting the gas price for the L2 network fees. |
| Goërli execution  | goerli-execution     | L1 node's execution layer.                                   |
| Goërli consensus  | goerli-consensus     | L1 node's consensus layer.       