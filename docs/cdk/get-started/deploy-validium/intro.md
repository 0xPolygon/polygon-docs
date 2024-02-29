---
comments: true
---

This guide takes you through the process of deploying a fully EVM-compatible, CDK validium on the Sepolia network.

We have hidden most of the configuration complexity in scripts to make the process straightforward and easy to follow.

## Process steps

The process requires two separate flows with different software requirements. For this reason, we have separated the instructions into two distinct sections.

1. [Deploying the contracts](contracts/prerequisites.md): The node and services require a bunch of [deployed contracts](https://github.com/0xPolygon/cdk-validium-contracts) so we complete this step first.
2. [Deploying the node and services](node/prerequisites.md): Once the contracts are deployed, we can run the [validium node](https://github.com/0xPolygon/cdk-validium-node), [mock prover](https://github.com/0xPolygonHermez/zkevm-prover), [data availability layer](https://github.com/0xPolygon/cdk-data-availability), and [zkEVM bridge service](https://github.com/0xPolygonHermez/zkevm-bridge-service).

!!! warning
    - The instructions are subject to frequent updates as the software remains at an early development stage.
    - Report any technical issue on the relevant [repo](#git-repos-and-running-order).
    - Report any content issues on our docs repo: https://github.com/0xPolygon/polygon-docs.

## Git repos and running order

These are the code bases we used to set everything up for this deployment guide, and in this order.

!!! warning
    The versions below may not be the most recent.

| Repo | Version |
| --- | --- |
| https://github.com/0xPolygon/cdk-validium-contracts/releases/tag/v0.0.2 | v0.0.2 |
| https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.0.3 | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-prover | v3.0.2 |
| https://github.com/0xPolygon/cdk-data-availability | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-bridge-service | v0.3.1 |

## Instructions for deploying contracts

You are now ready to follow the [pre-requisite steps](contracts/prerequisites.md) for setting up the contracts.