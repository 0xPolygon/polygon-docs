Developers can use CDK to configure custom ZK-rollups by choosing which components should run the Polygon zkEVM protocol. We refer to these chains as CDK sovereign chains.

Developers can, for instance, configure their chains to use provers that are outside the Polygon zkEVM stack.

Specifically, instead of deploying a Polygon zkEVM prover, developers can configure their CDK sovereign chains to utilize Succinct's SP1 prover.

Since CDK sovereign chains are designed to easily connect to the AggLayer, they use a type of ZK-proof called a _pessimistic proof_ to reach finality of transactions.

## What is a pessimistic proof?

A *pessimistic proof* (PP) is a zero-knowledge proof attesting to the fact that a chain's bridge transitions were correctly executed and that all withdrawals are collateralized.

Therefore, pessimistic proofs enable CDK-built chains that interoperate via the [unified bridge](../../zkEVM/architecture/unified-LxLy/index.md) to achieve trustless cross-chain security. 

Pessimistic proofs allow CDK sovereign chains connected to the [AggLayer](../../agglayer/overview.md) interoperate securely

We henceforth refer to CDK sovereign chains as CDK PP chains.

## CDK PP stack

Next, we detail the architectural components of the CDK PP chains.

The table below lists the components of a CDK PP chain and where you can find them.

| Component                | CDK PP stack                                                 | Notes                                                        |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Node = RPC and sequencer | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon)  | Customizable, commonly:<br/>\- Sequencer = 1 node<br/>\- RPC = multiple nodes |
| Contracts                | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a> |                                                              |
| CLI                      | [cdk](https://github.com/0xPolygon/cdk)                      | Included in [CDK](https://github.com/0xPolygon/cdk) repo     |
| AggSender                | <a href=https://github.com/0xPolygon/cdk>cdk</a>             | Included in [CDK](https://github.com/0xPolygon/cdk) repo     |
| Tx pool manager          | <a href=https://github.com/0xPolygon/zkevm-pool-manager>  zkevm-pool-manager</a> |                                                              |

## Component descriptions

Here are brief descriptions for each CDK FEP component.

- CDK Erigon node, a fork of [erigon](https://github.com/ledgerwatch/erigon), that manages the following:
    - Multiple RPC nodes that provide common APIs for sending transactions.
    - Sequencer for executing transactions, and creating blocks and batches.
- Contracts: Various smart contracts deployed on L1 for the full implementation and complete functionality of the Polygon zkEVM protocol:
    - `PolygonRollupManager`
    - `PolygonZkEVMBridgeV2`
    - `PolygonZkEVMGlobalExitRootV2`
    - `FflonkVerifier`
    - `PolygonZkEVMDeployer`
    - `PolygonZkEVMTimelock`
- CLI tool: A single command line interface tool for abstracting away the complexity of deploying or configuring CDK components.
- AggSender is the CDK PP component that accumulates all necessary info in order to generate certificates, which are sent to the SP1 prover via the JSON-RPC API  for the generation of pessimistic proofs.
- Transaction pool manager: For storing transactions submitted by users.

## AggLayer-side components

- Succinct's SP1 prover: A simplified cryptographic tool designed to take Rust-written inputs in order to generate ZK-proofs.

  Unlike in the CDK FEP chain, the prover in a CDK PP chain is not directly connected to the chain. It in fact resides in the AggLayer.

- JSON-RPC API: A component provided by the AggLayer to interface between the CDK PP chain and the SP1 prover.

  In reality, the AggSender sends certificates to the JSON-RPC API, which in turn requests the SP1 prover to generate ZK-proofs. On receipt of the ZK-proofs, it sends the ZK-proofs to L1.

  See the high level view of the CDK PP chain architecture [here](../architecture/high-level-views.md)
