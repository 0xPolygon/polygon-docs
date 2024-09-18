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

## CDK stack with pessimistic proofs

The CDK with pessimistic proofs release follows on shortly after the CDK FEP release.

!!! tip 
    Coming soon.
