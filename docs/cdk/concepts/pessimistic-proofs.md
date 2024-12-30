### What are Pessimistic Proofs?

Pessimistic Proofs (PP) are zero-knowledge proofs that validate a chain’s bridge transitions and the collateralization of all withdrawals. They provide a trustless mechanism for ensuring cross-chain security in sovereign configs built with the CDK stack.

#### Key features:
- Bridge validation: Ensures the correctness of transactions processed through the unified bridge.
- Withdrawal collateralization: Confirms that all withdrawals are properly collateralized, preventing unauthorized asset transfers.
- Trustless interoperability: Enables secure cross-chain interactions between sovereign configs and the AggLayer.

---

### Why use Pessimistic Proofs?

- Secure cross-chain interactions: Trustlessly connects chains built with sovereign configs to the AggLayer, ensuring robust interoperability.
- Robust finality mechanism: Validates bridge transitions and withdrawal collateralization for every transaction.
- Developer-friendly architecture: Modular components simplify implementation and accelerate development timelines.

By using Pessimistic Proofs, sovereign configs achieve seamless interoperability with the AggLayer, creating a robust foundation for cross-chain ecosystems.

---

### How Pessimistic Proofs work

Pessimistic Proofs validate all cross-chain transactions by generating cryptographic proofs of correctness. These proofs are processed by the AggLayer’s infrastructure, ensuring secure communication between sovereign configs.

#### Workflow:
1. Transaction submission: Transactions are sent to the sequencer of a chain configured as a sovereign chain.
2. Certificate generation: The AggSender aggregates data from the chain and sends certificates to the AggLayer node.
3. Proof generation: The AggLayer’s SP1 prover generates zero-knowledge proofs from the submitted certificates.
4. Validation: The AggLayer node validates the proofs and finalizes the transactions.

This ensures that transactions are secure, transparent, and trustlessly verified.

---

### Architectural components of sovereign configs with Pessimistic Proofs

| Component                | Repository                                                                                   | Notes                                                       |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Node (RPC and Sequencer) | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon)                                | Customizable; typically:<br>- Sequencer = 1 node<br>- RPC = multiple nodes |
| Contracts                | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts)                         | Includes Layer 1 contracts for functionality               |
| CLI tool                 | [cdk](https://github.com/0xPolygon/cdk)                                                      | Included in the CDK repository                             |
| AggSender                | [cdk](https://github.com/0xPolygon/cdk)                                                      | Sends certificates to the AggLayer node                    |
| Transaction pool manager | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager)                       | Manages transaction storage                                |
| SP1 prover               | Resides in the AggLayer                                                                      | Generates cryptographic proofs                             |
| AggLayer node            | Component of the AggLayer                                                                    | Handles proof validation and cross-chain interactions      |

---

### Component descriptions

- Node (RPC and Sequencer): A fork of [Erigon](https://github.com/ledgerwatch/erigon), managing multiple RPC nodes and a sequencer to execute transactions and create blocks and batches.
- Contracts: Smart contracts deployed on Layer 1 to implement bridge validation and withdrawal collateralization:
  - PolygonRollupManager
  - PolygonZkEVMBridgeV2
  - PolygonZkEVMGlobalExitRootV2
  - FflonkVerifier
  - PolygonZkEVMDeployer
  - PolygonZkEVMTimelock
- CLI tool: Simplifies deployment and configuration of CDK components through an easy-to-use command-line interface.
- AggSender: Aggregates data and sends certificates to the AggLayer node for proof generation and validation.
- Transaction pool manager: Stores and manages user-submitted transactions.
- SP1 prover: A cryptographic tool in the AggLayer, responsible for generating Pessimistic Proofs.
- AggLayer node: Interfaces between sovereign configs and the SP1 prover, validating proofs and ensuring secure cross-chain interactions.

---

### Support services

#### Bridge services
- [Bridge service](https://github.com/0xPolygonHermez/zkevm-bridge-service): A backend service enabling interactions with bridge contracts via Merkle proofs.
- [Bridge UI](https://portal.polygon.technology/): A user-friendly portal for managing deposits and withdrawals.

#### Explorer services
- [Blockscout](https://github.com/0xPolygonHermez/blockscout): Recommended for inspecting transactions and cross-chain operations. Alternative explorer services can also be used.