Deploying the full stack Polygon CDK validium EVM-compatible network requires installing and deploying a number of different components.

| Component         | Container            | Description                                           |
| :---------------- | :------------------- | ------------------------------------------------------------ |
| Sequencer         | `zkevm-sequencer`      | Fetches txs from the pool DB, checks if valid, then puts valid ones into a batch. |
| Aggregator        | `zkevm-aggregator`     | Validates sequenced batches by generating verifiable zero-knowledge proofs. |
| Synchronizer      | `zkevm-sync`        | Updates the state by fetching data from Ethereum through the Etherman. |
| JSON RPC          | `zkevm-rpc`           | An interface for interacting with the network. e.g., Metamask, Etherscan or Bridge. |
| State DB          | `zkevm-state-db`       | A database for permanently storing state data (apart from the Merkle tree). |
| Prover            | `zkevm-prover-server`  | Used by the aggregator to create zk-proofs. The full prover is extremely resource-heavy and runs on an external cloud server. Use the mock prover for evaluation/test purposes. |
| Pool DB           | `zkevm-pool-db`        | Stores txs from the RPC nodes, waiting to be put in a batch by the sequencer. |
| Executor          | `zkevm-executor`      | Executes all processes. Collects results’ metadata (state root, receipts, logs) |
| Etherman          | `zkevm-eth-tx-manager` | Implements methods for all interactions with the L1 network and smart contracts. |
| Bridge UI         | `zkevm-bridge-ui`      | User-interface for bridging ERC-20 tokens between L2 and L1 or another L2. |
| Bridge DB         | `zkevm-bridge-db`     | A database for storing bridge-related transactions data.     |
| Bridge service    | `zkevm-bridge-service` | A backend service enabling clients like the web UI to interact with bridge smart contracts. |
| zkEVM explorer    | `zkevm-explorer-l2`    | L2 network's block explorer. i.e., The zkRollup Etherscan [explorer](https://zkevm.polygonscan.com). |
| zkEVM explorer DB | `zkevm-explorer-l2-db` | Database for the L2 network's Block explorer. i.e., Where all the zkRollup Etherscan explorer queries are made. |
| Gas pricer        | `zkevm-l2gaspricer`    | Responsible for suggesting the gas price for the L2 network fees. |
| Goërli execution  | `goerli-execution`     | L1 node's execution layer.                                   |
| Goërli consensus  | `goerli-consensus`     | L1 node's consensus layer.       