Polygon CDK therefore has two modes:

- The CDK rollup/validium mode used for configuring CDK components that run the Polygon zkEVM protocol.
- The CDK sovereign chain mode used for custom chains. For instance a chain that uses a prover external to Polygon, such as Succinct's SP1.

These two Polygon CDK modes are released in the chronological order given above, with the Polygon-centric CDK mode coming first and then followed by the sovereign chain CDK mode.

Next, we detail the architectural components of the Polygon-prover CDK mode.

## Polygon-prover CDK mode

The CDK CLI tool is what developers can use to configure ZK-powered chains.

Developers can use the CDK CLI tool to easily configure ZK-powered blockchain networks.

| Component | CDK rollup (FEP) | CDK validium (FEP) | Notes |
| --- | --- | --- | --- |
| CLI | [CLI included](https://github.com/0xPolygon/cdk) | [CLI included](https://github.com/0xPolygon/cdk) | Same code for both |
| Node = RPC and sequencer | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon) | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon) | Customizable but usually sequencer=1 node, multiple for RPC |
| Tx pool manager | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager) | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager) | Same code for both |
| Sequence sender | [Sequence sender included](https://github.com/0xPolygon/cdk) | [Sequence sender included](https://github.com/0xPolygon/cdk) | Same code for both |
| Aggregator | [Aggregator included](https://github.com/0xPolygon/cdk) | [Aggregator included](https://github.com/0xPolygon/cdk) | Same code for both |
| Prover | [zkevm-prover](https://github.com/0xPolygonHermez/zkevm-prover) | [zkevm-prover](https://github.com/0xPolygonHermez/zkevm-prover) | Same code for both - wip |
| Data streamer | [zkevm-data-streamer](https://github.com/0xPolygon/zkevm-data-streamer) | [zkevm-data-streamer](https://github.com/0xPolygon/zkevm-data-streamer) | Same code for both |
| DA Layer | None | [cdk-data-availability](https://github.com/0xPolygon/cdk-data-availability) |  |
| Contracts | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) | Same code for both: 8.0.0-rc.2-fork.12 |
| Bridge service | [zkevm-bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) | [Polygon Portal](https://portal.polygon.technology/) | tbc |
| Bridge UI | [Polygon Portal](https://portal.polygon.technology/) | [Polygon Portal](https://portal.polygon.technology/) | Same UI for both |
| Blockscout | [blockscout](https://github.com/0xPolygonHermez/blockscout) | [blockscout](https://github.com/0xPolygonHermez/blockscout) | Same code for both |

!!! important
    
    For specific release tags, please reference the [version matrix document](https://www.notion.so/polygontechnology/version-matrix.md).

## Component descriptions

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

## CDK sovereign stack

The PP-based CDK sovereign chain mode release follows on shortly after the CDK FEP release.

!!! tip
    
    Coming soon.
