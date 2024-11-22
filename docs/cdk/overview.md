<!--
---
comments: true
---
-->

The Polygon Chain Development Kit (CDK) is a modular, open-source software toolkit that enables blockchain developers to deploy and configure ZK-powered chain architectures.

With Polygon CDK, developers can launch new chains that use the Polygon zkEVM protocol as custom Layer 2 solutions on Ethereum.

Developers can configure ZK-powered rollups, validium networks, or even sovereign chains with their own tailored finality mechanisms.

## Trustless finality

Why does Polygon CDK focus on ZK-powered chains?

Polygon CDK focuses on ZK-powered chains because zero-knowledge technology enables chains to achieve *trustless finality*, which means chain users don't need to rely on a small group of individuals to confirm the finality of their transactions, ensuring greater security and a higher degree of decentralization.

With Polygon CDK, developers can choose between a rollup and validium chain setup, and decide on how they want to configure the chain's proving system.

Polygon has launched the CDK rollup/validium mode enabling developers to configure CDK components that run the Polygon zkEVM protocol.

## Key advantages

Polygon CDK provides the essential components to build a Layer 2 blockchain that is secure, scalable, and interoperable with other chains.

- Security: CDK builds highly secure, scalable L2s that utilize the latest innovations in zero-knowledge technology.
- High-performance: CDK Erigon implements fast-syncing Erigon clients that run the battle-tested Polygon zkEVM protocol.
- Modularity: CDK modular components allow developers to easily customize their L2 environment and build a chain that meets their specific needs.
- Interoperability: Opt-in to the [AggLayer](../agglayer/overview.md) to bootstrap your chain’s ecosystem, enable cross-chain transactions while expanding your reach, user base, and liquidity from other established chains.
- Sovereignty: Maintain full control over your chain’s revenue, governance, security, economic policies, and more.
- Low gas fees: Transaction fees are orders of magnitude lower than those on Ethereum and are processed substantially faster. This enables a fast, ultra low-cost, and secure user experience unaffected by any high activity experienced on shared networks.

### Next steps

- [Deploy a local CDK environment using Kurtosis](../cdk/getting-started/local-deployment.md). Follow the guide to deploy a CDK stack on your local machine.

- Check out the [concepts documentation](../cdk/concepts/layer2s.md) to gain a high-level understanding of the CDK.

- Have a look at the [CDK architecture docs](../cdk/concepts/architecture.md) to understand the CDK’s components and how they interact with each other.