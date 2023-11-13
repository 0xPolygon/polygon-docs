---
id: validium-attributes
title: Validium System Attributes
sidebar_label: System Attributes
description: "Learn about the key metrics for the validium offering part of the Polygon CDK."
keywords:
  - docs
  - polygon
  - layer 2
  - validium
  - zkValidium
  - development kit
  - sdk
  - cdk
  - chain development kit
---

CDK-developed chains operate with a commitment to cost-effectiveness. The cost structure is thoughtfully constructed, factoring in several key considerations to help maintain competitive and predictable expenses.

The following tables outline the key system attributes and costs within a CDK-developed chain and specify where each measurement is taken.

### Metrics Overview

| Metric              | Measurement        | Measurement Context   | Description                                                            | Key Term Definition |
|---------------------|--------------------|-----------------------|------------------------------------------------------------------------|---------------------|
| Unified Liquidity   | High               | Polygon 2.0 | Seamlessly interacts across chains via LXLY Bridge for high liquidity  | Seamless flow of assets between different chains. |
| Future-Proof        | Essential          | Polygon 2.0 | Key component of the Polygon 2.0 framework for future-ready operations | Preparation and composability of the product suite for future advancements. |
| Gas Availability    | Unlimited | L2 | Supports virtually unlimited processing capacity due to unlimited L2 gas | The amount of computational effort required to process transactions. |
| Transaction Fees    | Very Low           | L2 | Designed for efficiency, resulting in significantly reduced fees due to off-chain DA and ZKPs       | Costs associated with executing transactions. |
| Decentralization    | Customizable                | L2 | Employs Ethereum for transaction proofs to ensure decentralized control; Permissioned DAC; Customizable Access Control | Distribution of processing and management across the network. |
| Data Availability   | Validium           | DAC | Incorporates a Data Availability Committee for reliable off-chain data | Assurance of consistent data access, even in case of failures. |
| Security            | High          | L2 | Inherits Ethereum's robust security mechanisms, ensuring transaction proof integrity      | Built on Ethereum's tested security infrastructure, offering a high level of protection against network attacks. |
| Interoperability    | High               | Polygon 2.0 | Promotes cross-chain interaction via LXLY Bridge for greater reach     | Ability of a system to work with other systems with ease. |
| Initial Stake       | Not Required       | L2 | Eliminates barriers to entry with no initial stake or collateral       | Initial capital or resources required to participate in a network. |

> The DAC serves as independent entity holding the up-to-date chain data. In case of chain disruptions, The DAC assures data availability, enabling chain reconstruction from any DAC member's data.

<!--

### Layer 1 (Ethereum) Costs

| Metric              | Measurement        | Measurement Context   | Description                                                            | Key Term Definition |
|---------------------|--------------------|-----------------------|------------------------------------------------------------------------|---------------------|
| Transaction Aggregation | Up to 10M gas per batch* | Aggregator | Aggregates high volume of transactions into batches. Each batch, accommodating up to 10M gas, is sent as a single transaction to L1. 350,000 gas is reserved for ZKP verification. | The collection and organization of multiple transactions into a single batch, processed as a unit. |

> * Each batch accommodates varying transaction counts, aggregated into a single transaction sent to L1. The L1 gas limit applies for the whole batch and not for each individual transaction within the batch.

-->

### What are the Transaction Fees?

Compared to zkEVM and similar architectures, CDK-developed chains` cost structure can lead to an approximately **80% reduction** in transaction fees due to the data availability layer.

Through ongoing optimization and innovation, we project further significant reductions in transaction fees in the future.

> Transaction costs in CDK-developed chains are primarily influenced by the volume of transactions processed by the app-chain and withdrawal frequency. External factors such as Ethereum price and L1 gas price also contribute. Notably, L2 gas price can be adjusted for an optimal cost-profit balance.

### What is Meant by "Unified Liquidity"?

As a fundamental component of Polygon 2.0, CDK-developed chains adopt an advanced interoperability layer, facilitating seamless cross-chain interaction for projects.

<!--
- **Access to a Robust and Liquid Ecosystem**: Projects and validators become part of a network already supported by a proven set of validators, offering unified liquidity and enhancing their confidence.
- **Flexibility and Control**: Validators, through administrative access, can customize system capabilities to fit their needs.
- **Earning Potential Across Networks**: Validators have opportunities to secure the network and earn rewards across multiple chains.
- **Contribution to the Ecosystem's Security**: Staking contributes to the overall security of the Polygon ecosystem, supporting its growth and robustness.

Remember, while CDK-developed chains eliminate the need for an initial stake, validators still play a crucial role in ensuring network security and integrity.
-->

**Stay tuned for more information.**

<div align="center">
  <img src="/img/cdk/polygon2.0-layers.png" alt="bridge" width="99%" height="30%" />
</div>

<!--
## How do CDK-developed chains Compare to Other Polygon-based Layer 2 Solutions?

| Features / Systems       | zkPoS (Proposed Upgrades)       | zkEVM (Current State)     | CDK-developed chains (Based on Design Principles)      |
|--------------------------|---------------------------------|---------------------------|--------------------------------------|
| Underlying Technology    | zkEVM Validium + PoS              | zkEVM Rollup              | zkEVM Validium + DAC                   |
| Execution Efficiency     | Optimized for higher throughput | Optimized for Security for efficient execution throughput | Optimized for high volume transactions |
| Security Model           | High, Ethereum + zk proofs, but data availability depends on PoS validators  | Very High, Ethereum + zk proofs, fully on-chain data availability | Medium, Ethereum + zk proofs, but data availability depends on DAC |
| Scalability              | Very High scalability | High, but limited by Ethereum's data capacity | Extremely scalable for app-specific use cases |
| Interoperability         | Very High within Polygon 2.0 via LXLY bridge | Very High within Polygon 2.0 via LXLY bridge | Very High within Polygon 2.0 via LXLY bridge  |
| Transaction Costs        | Very Low due to data availability layer                    | High due to being bound by Ethereum's gas cost | Extremely Low due to data availability layer                        |
| Staking Requirements     | Uses $POL for staking on shared staking layer | Uses $POL for staking on shared staking layer | Uses $POL for staking on shared staking layer |
| Decentralization         | Medium, depends on PoS validators | Medium, inherits from Ethereum and depends on centralized Prover | Medium, centralized DAC and depends on app-chain configurations             |
| Network Compatibility    | Compatible with Polygon 2.0 | Compatible with Polygon 2.0 & Ethereum-based networks | Extensively compatible due to Polygon 2.0 architecture |
| Developer Experience     | Seamless within Ethereum ecosystem | Seamless within Ethereum ecosystem | Seamless with understanding of application development |
-->
