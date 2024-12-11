Developers can use the CDK stack to build layer 2 chains that are natively connected to the AggLayer (**CDK sovereign chains**).

Out of the box, CDK sovereign chains are built to connect to the AggLayer, and so they rely on a type of ZK-proof called a _pessimistic proof_ to finalize transactions.

## What is a pessimistic proof?

A *pessimistic proof* (PP) is a zero-knowledge proof attesting to the correctness of a chain’s bridge transitions and the collateralization of all withdrawals.

These proofs enable CDK sovereign chains that interoperate via the [unified bridge](../../zkEVM/architecture/unified-LxLy/index.md) to achieve trustless cross-chain security. 

Pessimistic proofs ensure that CDK sovereign chains connected to the [AggLayer](../../agglayer/overview.md) interoperate securely, providing a robust mechanism for cross-chain interactions.

---

## CDK sovereign chain components

The architectural components of CDK sovereign chains are detailed in the table below:

| Component                | CDK Stack                                                    | Notes                                                        |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Node = RPC and sequencer | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon)  | Customizable, commonly:<br/>\- Sequencer = 1 node<br/>\- RPC = multiple nodes |
| Contracts                | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a> | Includes L1 contracts for functionality                     |
| CLI                      | [cdk](https://github.com/0xPolygon/cdk)                      | Included in [CDK](https://github.com/0xPolygon/cdk) repo     |
| AggSender                | <a href=https://github.com/0xPolygon/cdk>cdk</a>             | A sub-component of the CDK client that sends certificates to the AggLayer node |
| Tx pool manager          | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager</a> | Manages transaction storage                                  |

---

## Component descriptions

Here are brief descriptions of the key CDK components:

- **CDK Erigon Node**: A fork of [Erigon](https://github.com/ledgerwatch/erigon), providing:
  - Multiple RPC nodes for transaction submission.
  - A sequencer for executing transactions, and creating blocks and batches.
- **Contracts**: Smart contracts deployed on L1 to ensure full implementation and functionality:
    - `PolygonRollupManager`
    - `PolygonZkEVMBridgeV2`
    - `PolygonZkEVMGlobalExitRootV2`
    - `FflonkVerifier`
    - `PolygonZkEVMDeployer`
    - `PolygonZkEVMTimelock`
- **CLI tool**: A command-line tool that simplifies deploying and configuring CDK components.
- **AggSender**: A functionality within the CDK client that aggregates necessary data and sends certificates to the AggLayer node for proof generation. It works in conjunction with other sub-components, such as the bridge syncer.
- **Transaction pool manager**: Handles storage of user-submitted transactions.
- **Succinct's SP1 prover**: A cryptographic tool that generates ZK-proofs using Rust-based inputs. The prover resides in the AggLayer and is not directly connected to CDK sovereign chains.
- **AggLayer node**: A critical component of the AggLayer that interfaces between CDK sovereign chains and the SP1 prover. It handles certificate validation and proof requests.

The AggSender within the CDK client communicates with the AggLayer node to facilitate proof generation and finalization of transactions.

See the high level view of the architecture [here](../architecture/cdk-pp-highlevel-arch.md)
