The CDK Ares+ release has two modes:

1. The CDK rollup/validium mode with full execution proofs is the first mode for release.
2. The CDK sovereign chain mode with pessimistic proofs, and no full execution proof, is coming shortly after.

This document details the full stack components for the first mode of release: CDK Ares+ with full execution proofs.

!!! note
    We are going to leave a placeholder for the pessimistic proof mode stack; and for good measure and completeness we'll add details of the previous stack in which zkEVM and CDK components were more disparate.

## CDK stack with full execution proofs (FEP)

In this release, the zkEVM components can be considered as a CDK stack in rollup mode. 

The following table lists the components and where you can find them for CDK rollup and validium stacks. You will notice only small differences in the component makeup of the two stacks which are now mostly use case specific.

| Component | CDK rollup (FEP) | CDK validium (FEP) | Notes |
| --- | --- | --- | --- |
| Node = RPC and sequencer | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | Customizable but usually sequencer=1 node, multiple for RPC |
| Data availability | None | <a href=https://github.com/0xPolygon/cdk-data-availability>cdk-data-availability</a> |  |
| Contracts | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a> | <a href=https://github.com/0xPolygonHermez/zkevm-contracts>zkevm-contracts</a>  | Same code for both: 8.0.0-rc.2-fork.12 |
| Data streamer | tbc | tbc  | tbc |
| CLI | tbc | tbc  | tbc |
| Sequence sender | <a href=https://github.com/0xPolygon/cdk>Sequence sender included</a> | <a href=https://github.com/0xPolygon/cdk>Sequence sender included</a>  | Same code for both |
| Aggregator | <a href=https://github.com/0xPolygon/cdk>Aggregator included</a> | <a href=https://github.com/0xPolygon/cdk>Aggregator included</a> | Same code for both |
| Tx pool manager | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager | Same code for both |
| Prover | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover</a> | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover</a> | Same code for both - wip |
| Bridge service | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-service>zkevm-bridge-service</a> | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | tbc |
| Bridge UI | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | <a href=https://portal.polygon.technology/>Polygon Portal</a>  | Same UI for both |
| Blockscout | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | Same code for both |

!!! important
    For specific release tags, please reference the [version matrix document](version-matrix.md).

## CDK stack with pessimistic proofs

This release will follow on shortly after the Ares+ FEP release.

## Previous release

| Component | zkEVM stack | CDK stack | Notes |
| --- | --- | --- | --- |
|  Node | <a href=https://github.com/0xPolygonHermez/zkevm-node/tree/feature/fork-11>zkevm-node</a> | <a href=https://github.com/0xPolygon/cdk-validium-node>cdk-validium-node</a> | - zkEVM for rollup </br>- CDK for validium </br>Both include sequencer |
| Contracts | <a href=https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v6.0.0-rc.1-fork.9>zkevm-contracts</a> | <a href=https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v6.0.0-rc.1-fork.9>zkevm-contracts</a> | Same for both |
| Erigon RPC | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | Same for both |
| Erigon sequencer | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | <a href=https://github.com/0xPolygonHermez/cdk-erigon>cdk-erigon</a> | Same for both |
| Sequence sender | <a href=https://github.com/0xPolygonHermez/zkevm-sequence-sender>zkevm-sequence-sender</a> | <a href=https://github.com/0xPolygon/cdk-sequence-sender>cdk-sequence-sender</a> |  |
| Aggregator | <a href=https://github.com/0xPolygonHermez/zkevm-aggregator>zkevm-aggregator</a>  | <a href=https://github.com/0xPolygon/cdk>cdk</a> |  |
| Pool manager | <a href=https://github.com/0xPolygon/zkevm-pool-manager>zkevm-pool-manager</a> using with cdk-erigon | No explicit pool manager as persistence is built in |  |
| Prover | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover<a>  | <a href=https://github.com/0xPolygonHermez/zkevm-prover>zkevm-prover<a> | Versions in flight |
| Bridge service | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-service>zkevm-bridge-service</a> | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-service>zkevm-bridge-service</a> | Same for both |
| Bridge UI | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-ui>zkevm-bridge-ui</> | <a href=https://github.com/0xPolygonHermez/zkevm-bridge-ui>zkevm-bridge-ui</> | Same for both with modifications |
| Blockscout | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | <a href=https://github.com/0xPolygonHermez/blockscout>blockscout</a> | Same for both |

!!! important
    For specific release tags, please reference the [version matrix document](version-matrix.md).