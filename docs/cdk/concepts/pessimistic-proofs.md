### What are Pessimistic Proofs?

Pessimistic Proofs (PP) are zero-knowledge proofs that validate the correctness of bridge transitions and ensure the collateralization of all withdrawals. They provide a trustless mechanism for secure cross-chain interactions between chains configured with the CDK Sovereign Config and the Agglayer.

#### Key Features:
- **Bridge validation:** Ensures transactions processed through the unified bridge are correct.
- **Withdrawal collateralization:** Confirms all withdrawals are properly collateralized, preventing unauthorized asset transfers.
- **Trustless interoperability:** Facilitates secure and seamless cross-chain communication.

---

### Why use Pessimistic Proofs?

- **Secure cross-chain interactions:** Ensures trustless interoperability between chains using the Sovereign Config and the Agglayer.
- **Robust validation mechanism:** Validates bridge transitions and withdrawal collateralization for every transaction.
- **Developer-friendly architecture:** Modular components simplify implementation and accelerate development timelines.

Pessimistic Proofs enable developers to build robust, secure, and interoperable chains that seamlessly interact with the Agglayer.

---

### How Pessimistic Proofs work

Pessimistic Proofs validate cross-chain transactions by using cryptographic zero-knowledge proofs to ensure secure and trustless interactions between chains. These proofs safeguard the integrity of bridge operations and withdrawal processes.

#### Workflow:
1. **Transaction submission:** Transactions are sent to the chain’s sequencer.
2. **Certificate generation:** The AggSender aggregates transaction data and sends certificates to the Agglayer node.
3. **Proof generation:** The SP1 prover in the Agglayer generates zero-knowledge proofs based on the certificates.
4. **Validation:** The Agglayer node validates the proofs and finalizes the transactions.

This ensures that all transactions are secure, trustlessly verified, and transparently executed.

---

### Architectural Components of Sovereign Configs with Pessimistic Proofs

| Component                | Repository                                                                                   | Notes                                                       |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Node (RPC and Sequencer) | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon)                                | Customizable; typically:<br>- Sequencer = 1 node<br>- RPC = multiple nodes |
| Contracts                | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts)                       | Includes Layer 1 contracts for functionality               |
| CLI tool                 | [cdk](https://github.com/0xPolygon/cdk)                                                    | Simplifies deployment and configuration                     |
| AggSender                | [cdk](https://github.com/0xPolygon/cdk)                                                    | Sends certificates to the Agglayer node                    |
| Transaction pool manager | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager)                       | Manages transaction storage                                 |
| SP1 prover               | Resides in the Agglayer                                                                     | Generates cryptographic proofs                             |
| Agglayer node            | Component of the Agglayer                                                                   | Interfaces between chains and the SP1 prover               |

---

### Component Descriptions

- **Node (RPC and Sequencer):** A fork of [Erigon](https://github.com/ledgerwatch/erigon) responsible for managing multiple RPC nodes and running a sequencer to execute transactions and create blocks and batches.
- **Contracts:** Smart contracts deployed on Layer 1 to implement bridge transitions and withdrawal collateralization:
  - `PolygonRollupManager`
  - `PolygonZkEVMBridgeV2`
  - `PolygonZkEVMGlobalExitRootV2`
  - `FflonkVerifier`
  - `PolygonZkEVMDeployer`
  - `PolygonZkEVMTimelock`
- **CLI tool:** A command-line interface that simplifies the deployment and configuration of CDK components.
- **AggSender:** Aggregates chain data and sends certificates to the Agglayer node for proof generation and validation.
- **Transaction pool manager:** Stores and manages user-submitted transactions, ensuring efficient and secure handling.
- **SP1 prover:** A cryptographic tool in the Agglayer responsible for generating Pessimistic Proofs.
- **Agglayer node:** Interfaces between chains using the Sovereign Config and the Agglayer’s SP1 prover, handling proof validation and facilitating cross-chain security.

---

### Support Services

#### Bridge Services
- [Bridge service](https://github.com/0xPolygonHermez/zkevm-bridge-service): A backend service enabling interactions with bridge contracts via Merkle proofs.
- [Bridge UI](https://portal.polygon.technology/): A user-friendly portal for managing deposits and withdrawals.

#### Explorer Services
- [Blockscout](https://github.com/0xPolygonHermez/blockscout): Recommended for inspecting transactions and cross-chain operations. Alternative explorers can also be integrated.