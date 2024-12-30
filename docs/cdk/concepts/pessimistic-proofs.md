## What Are Pessimistic Proofs?

**Pessimistic Proofs (PP)** are zero-knowledge proofs that attest to the correctness of a chain’s bridge transitions and the collateralization of all withdrawals. They provide a trustless mechanism for ensuring cross-chain security for CDK sovereign chain configurations.

### Key Features of Pessimistic Proofs:
- **Bridge Validation**: Ensures the correctness of transactions processed through the unified bridge.
- **Withdrawal Collateralization**: Confirms that all withdrawals are properly collateralized, preventing unauthorized asset transfers.
- **Trustless Interoperability**: Enables secure cross-chain interactions between chains built with sovereign chain configurations and the AggLayer.

---

## Why Use Pessimistic Proofs?

- **Secure Cross-Chain Interactions**: Trustlessly connects chains built with sovereign chain configurations to the AggLayer, ensuring robust interoperability.
- **Robust Finality Mechanism**: Validates bridge transitions and withdrawal collateralization for every transaction.
- **Developer-Friendly Architecture**: Modular components simplify implementation and accelerate development timelines.

By using Pessimistic Proofs, CDK sovereign chain configurations achieve seamless interoperability with the AggLayer, creating a robust foundation for cross-chain ecosystems.

---

## How Pessimistic Proofs Work

Pessimistic Proofs validate all cross-chain transactions by generating cryptographic proofs of correctness. These proofs are processed by the AggLayer’s infrastructure, ensuring secure communication between chains configured with sovereign chain configurations.

### Workflow:
1. **Transaction Submission**: Transactions are submitted to the sequencer of a chain built with a sovereign chain configuration.
2. **Certificate Generation**: The AggSender aggregates data from the chain and sends certificates to the AggLayer node.
3. **Proof Generation**: The AggLayer’s SP1 prover generates zero-knowledge proofs from the submitted certificates.
4. **Validation**: The AggLayer node validates the proofs and finalizes the transactions.

This workflow ensures that transactions are secure, transparent, and trustlessly verified.

---

## Architectural Components of CDK Sovereign Chain Configurations

The table below outlines the key components required for sovereign chain configurations operating with Pessimistic Proofs.

| Component                | Repository                                                                                   | Notes                                                       |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **Node (RPC and Sequencer)** | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon)                                | Customizable; typically: <br>- Sequencer = 1 node <br>- RPC = multiple nodes |
| **Contracts**            | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts)                         | Includes Layer 1 contracts for functionality               |
| **CLI Tool**             | [cdk](https://github.com/0xPolygon/cdk)                                                      | Included in the CDK repository                             |
| **AggSender**            | [cdk](https://github.com/0xPolygon/cdk)                                                      | Sends certificates to the AggLayer node                    |
| **Transaction Pool Manager** | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager)                     | Manages transaction storage                                |
| **SP1 Prover**           | Resides in the AggLayer                                                                      | Generates cryptographic proofs                             |
| **AggLayer Node**        | Component of the AggLayer                                                                    | Handles proof validation and cross-chain interactions      |

---

## Component Descriptions

- **CDK Erigon Node**: A fork of [Erigon](https://github.com/ledgerwatch/erigon), managing:
  - Multiple RPC nodes for transaction submission.
  - A sequencer for executing transactions, and creating blocks and batches.
- **Contracts**: Smart contracts deployed on Layer 1 to implement bridge validation and withdrawal collateralization:
    - `PolygonRollupManager`
    - `PolygonZkEVMBridgeV2`
    - `PolygonZkEVMGlobalExitRootV2`
    - `FflonkVerifier`
    - `PolygonZkEVMDeployer`
    - `PolygonZkEVMTimelock`
- **CLI Tool**: Simplifies deployment and configuration of CDK components through an easy-to-use command-line interface.
- **AggSender**: Aggregates data and sends certificates to the AggLayer node for proof generation and validation.
- **Transaction Pool Manager**: Stores and manages user-submitted transactions.
- **SP1 Prover**: A cryptographic tool residing in the AggLayer, responsible for generating Pessimistic Proofs.
- **AggLayer Node**: Interfaces between CDK sovereign chain configurations and the SP1 prover, validating proofs and ensuring secure cross-chain interactions.

---

## Support Services

### Bridge Services
- **[Bridge Service](https://github.com/0xPolygonHermez/zkevm-bridge-service)**: A backend service enabling interactions with bridge contracts via Merkle proofs.
- **[Bridge UI](https://portal.polygon.technology/)**: A user-friendly portal for managing deposits and withdrawals.

### Explorer Services
- **[Blockscout](https://github.com/0xPolygonHermez/blockscout)**: Recommended for inspecting transactions and cross-chain operations. Alternative explorer services can also be used.

---