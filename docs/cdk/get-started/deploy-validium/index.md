This quick start takes you through the process of deploying a full CDK validium, EVM-compatible network on Sepolia.

The process requires two separate flows with different software requirements. For this reason, these instructions have two distinct sections.

1. [Deploying the contracts](contracts/prerequisites.md).
2. [Deploying the node and services](node/prerequisites.md).

!!! warning
    - The instructions are subject to frequent updates as the software remains at an early development stage.
    - Report any content issues on our docs repo: https://github.com/0xPolygon/polygon-docs

## Git repos

These are code bases we use to set everything up, and in this order.

| Repo | Version |
| --- | --- |
| https://github.com/0xPolygon/cdk-validium-contracts/releases/tag/v0.0.2 | v0.0.2 |
| https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.0.3 | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-prover | v3.0.2 |
| https://github.com/0xPolygon/cdk-data-availability.git | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-bridge-service | v0.3.1 |