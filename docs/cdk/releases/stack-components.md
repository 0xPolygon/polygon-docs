The latest CDK release has two modes:

1. The CDK rollup/validium mode with full execution proofs is the first mode for release.
2. The CDK sovereign chain mode with pessimistic proofs, and no full execution proofs, is coming shortly after.

This document details the full stack components for the first mode of release: CDK with full execution proofs.

## CDK stack with full execution proofs (FEP)

In the CDK with full execution proofs release, any zkEVM components can be considered as part of a CDK stack in rollup mode. 

The following table lists the components and where you can find them for CDK rollup and validium stacks. You will notice only small differences in the component makeup of the two stacks; differences which are now mostly use case specific.

| Component                                | CDK rollup (FEP)                                                                         | Notes                                                       |
|------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Node = RPC and sequencer                 | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a>                     | Customizable, commonly: <br/>- Sequencer = 1 node</br>- RPC = multiple nodes |
| Data availability                        | <a href=https://github.com/0xPolygon/cdk-data-availability>cdk-data-availability</a>     | **Only** for validium mode                                       |
| Contracts                                | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a>           |                                                             |
| CLI                                      | <a href=https://github.com/0xPolygon/cdk>cdk<a> |          Included in CDK repo                                                   |
| Sequence sender                          | <a href=https://github.com/0xPolygon/cdk>cdk</a>                    |         Included in CDK repo                                                                    |
| Aggregator                               | <a href=https://github.com/0xPolygon/cdk>cdk</a>                         |     Included in CDK repo                                                                        |
| Tx pool manager                          | <a href=https://github.com/0xPolygon/zkevm-pool-manager>  zkevm-pool-manager</a>                               |                                                             |
| Prover                                   | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover</a>                 |                                                             |
| Bridge service                           | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-service>zkevm-bridge-service</a> |                                                             |
| Bridge UI                                | <a href=https://portal.polygon.technology/>Polygon Portal</a>                            |                                                             |
| Recommended explorer service  | <a href=https://github.com/0xPolygonHermez/blockscout>Blockscout</a>                     | IP free to implement another explorer service           |

!!! important
    For specific release tags, please reference the [version matrix document](version-matrix.md).

### Component descriptions

Next are the brief descriptions of each CDK component.

- CDK Erigon node, a fork of [erigon](https://github.com/ledgerwatch/erigon), that manages the following:
    - Multiple RPC nodes that provide common APIs for sending transactions.
    - Sequencer for executing transactions, and creating blocks and batches.
- DAC: The Data Availability Committee, specifically for validium mode, is a set of *trusted actors* who keep custody of all transaction data, including monitoring and validating hash values the sequencer sender proposes to publish on L1.
- Contracts: Various smart contracts deployed on L1 for the full implementation and complete functionality of the Polygon zkEVM protocol:
    - `PolygonRollupManager`
    - `PolygonZkEVMBridgeV2`
    - `PolygonZkEVMGlobalExitRootV2`
    - `FflonkVerifier`
    - `PolygonZkEVMDeployer`
    - `PolygonZkEVMTimelock`
- CLI tool: A single command line interface tool for abstracting away the complexity of deploying or configuring CDK components.
- Sequence sender: For sequencing batches.
    - In the case of a rollup, the sequence sender sends batch data and the `sequenceBatches` transaction to L1.
    - In the case of a validium, the sequence sender sends batch data to the Data Availability Committee (DAC), requests for signatures from the DAC, and sends the `sequenceBatchesValidium` transaction to L1.
- Aggregator: For facilitating proving and verification, fetching and providing batch data and witness to the prover.
- Transaction pool manager: For storing transactions submitted by users.
- Prover: A complex cryptographic tool capable of producing ZK-proofs of hundreds of batches, and aggregating these into a single ZK-proof which is published as the validity proof.
- Bridge service: A backend service for enabling clients like the [web UI](https://github.com/0xPolygonHermez/zkevm-bridge-ui) to interact with the [bridge smart contract](https://github.com/0xPolygonHermez/zkevm-contracts) by providing Merkle proofs.
- Bridge UI: The Polygon bridge portal which abstracts away the backend operations involved in bridge deposits and withdrawals.
- Blockscout: An application that allows to view, confirm, and inspect transactions on EVM chains, optimistic rollups and zk rollups. EVM chains include the POA Network, Gnosis Chain, Ethereum Classic and other Ethereum testnets, private networks and side chains. Users may opt to use a different explorer service.

## CDK stack with pessimistic proofs

The CDK with pessimistic proofs release follows on shortly after the CDK FEP release.

!!! tip 
    Coming soon.
