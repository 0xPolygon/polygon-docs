The latest CDK release has two modes:

1. The CDK rollup/validium mode with full execution proofs is the first mode for release.
2. The CDK sovereign chain mode with pessimistic proofs, and no full execution proofs, is coming shortly after.

This document details the full stack components for the first mode of release: CDK with full execution proofs.

## CDK stack with full execution proofs (FEP)

In the CDK with full execution proofs release, any zkEVM components can be considered as part of a CDK stack in rollup mode. 

The following table lists the components and where you can find them for CDK rollup and validium stacks. You will notice only small differences in the component makeup of the two stacks; differences which are now mostly use case specific.

| Component | CDK rollup (FEP) | CDK validium (FEP) | Notes |
| --- | --- | --- | --- |
| Node = RPC and sequencer | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | Customizable but usually sequencer=1 node, multiple for RPC |
| Data availability | None | <a href=https://github.com/0xPolygon/cdk-data-availability>cdk-data-availability</a> |  |
| Contracts | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a> | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a>  | Same code for both: 8.0.0-rc.2-fork.12 |
| Data streamer | <a href=https://github.com/0xPolygon/zkevm-data-streamer>zkevm-data-streamer</a> | <a href=https://github.com/0xPolygon/zkevm-data-streamer>zkevm-data-streamer</a>  | Same code for both |
| CLI | <a href=https://github.com/0xPolygon/cdk>CLI included</a> | <a href=https://github.com/0xPolygon/cdk>CLI included</a>  | Same code for both |
| Sequence sender | <a href=https://github.com/0xPolygon/cdk>Sequence sender included</a> | <a href=https://github.com/0xPolygon/cdk>Sequence sender included</a>  | Same code for both |
| Aggregator | <a href=https://github.com/0xPolygon/cdk>Aggregator included</a> | <a href=https://github.com/0xPolygon/cdk>Aggregator included</a> | Same code for both |
| Tx pool manager | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager | Same code for both |
| Prover | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover</a> | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover</a> | Same code for both - wip |
| Bridge service | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-service>zkevm-bridge-service</a> | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | tbc |
| Bridge UI | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | Same UI for both |
| Blockscout | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | Same code for both |

!!! important
    For specific release tags, please reference the [version matrix document](version-matrix.md).

### Component descriptions

Next are the brief descriptions of each CDK component.

- CLI tool: A single command line interface tool for abstracting away the complexity of deploying or configuring CDK components.
- Sequencer: For executing transactions, and creating blocks and batches.
- RPC node: Each user can spin up an RPC node through which transactions are submitted.
- Tx-pool-manager: For storing transactions submitted by users.
- Sequence sender: For sequencing batches.
    - In the case of a rollup, the SequenceSender sends batch data and the `sequenceBatches` transaction to L1.
    - In the case of a validium, the SequenceSender sends batch data to the Data Availability Committee (DAC), requests for signatures from the DAC, and sends the `sequenceBatchesValidium` transaction to L1.
- Aggregator: For facilitating proving and verification, fetching and providing batch data and witness to the Prover.
- Prover: A complex cryptographic tool capable of producing ZK-proofs of hundreds of batches, and aggregating these into a single ZK-proof which is published as the validity proof.
- Data streamer: A library developed to serve raw block data to nodes that need to maintain an up-to-date L2 state, irrespective of the required amount of data.
- DAC: The Data Availability Committee, specifically for the validium case, is a set of *trusted actors* who keep custody of all transaction data, including monitoring and validating hash values the sequencer sender proposes to publish on L1.
- Contracts: Various smart contracts deployed on L1 for the full implementation and complete functionality of the Polygon zkEVM protocol
    - Here's the list: `PolygonRollupManager`, `PolygonZkEVMBridgeV2`, `PolygonZkEVMGlobalExitRootV2`, `FflonkVerifier`, `PolygonZkEVMDeployer`, and `PolygonZkEVMTimelock`.
- Bridge service: A backend service, written in Go, for enabling clients like the [web UI](https://github.com/0xPolygonHermez/zkevm-bridge-ui) to interact with the [bridge smart contract](https://github.com/0xPolygonHermez/zkevm-contracts) by providing Merkleproofs.
- Bridge UI: The Polygon bridge portal which abstracts away the backend operations involved in bridge deposits and withdrawals.
- Blockscout: An application that allows to view, confirm, and inspect transactions on EVM chains, optimistic rollups and zkrollups. EVM chains include the POA Network, Gnosis Chain, Ethereum Classic and other Ethereum testnets, private networks and sidechains.

## CDK stack with pessimistic proofs

The CDK with pessimistic proofs release follows on shortly after the CDK FEP release.

!!! tip 
    Coming soon.
