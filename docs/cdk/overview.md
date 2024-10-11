---
comments: true
---

The Polygon Chain Development Kit (CDK) is a modular, open-source software toolkit that enables blockchain developers to configure ZK-powered chain architectures.

With Polygon CDK, developers can launch new chains running the Polygon zkEVM protocol as Layer 2s on Ethereum.

Developers can configure ZK-powered rollups, validium networks, or even sovereign chains with their own tailored finality mechanisms.

## Trustless finality

Why does Polygon CDK focus on ZK-powered chains?

The power of zero-knowledge technology is seen in enabling chains to achieve trustless finality, where chain users do not have to rely on a few individuals to confirm the finality of their transactions.

With Polygon CDK chains developers can first decide on how they want to configure proving and then choose the right CDK mode to build their chain.

Polygon CDK therefore launches with the CDK rollup/validium mode used for configuring CDK components that run the Polygon zkEVM protocol.

Crucial to the Polygon CDK is the type of ZK-proofs known as full execution proofs.

### Full execution proofs

CDK rollups and validiums utilize *full execution proofs* as part of their finality mechanisms.

A *full execution proof* (FEP) is a zero-knowledge proof attesting to the correctness of the chain's full state transition.

For example, an FEP attests to the fact that the VM (such as the Polygon zkEVM, Succinct's zkVM, or MoveVM) has executed all state transitions in accordance with the specifications.

A ZK-powered chain is therefore by definition an FEP chain.

## Polygon CDK benefits

Polygon CDK provides the components necessary to build a layer 2 blockchain that is secure, scalable, and interoperable with other chains.

- Security: CDK builds highly secure, scalable L2s that utilize the latest innovations in zero-knowledge technology.
- High-performance: CDK Erigon implements fast-syncing Erigon clients that run the battle-tested Polygon zkEVM protocol.
- Modularity: CDK modular components allow developers to easily customize their L2 environment and build a chain that meets their specific needs.
- Interoperability: Opt-in to the [AggLayer](https://docs-dev.polygon.technology/1562/agglayer/overview/) to bootstrap your chain’s ecosystem, enable cross-chain transactions while expanding your reach, user base, and liquidity from other established chains.
- Sovereignty: Maintain full control over your chain’s revenue, governance, security, economic policies, and more.
- Low gas fees: Transaction fees are orders of magnitude lower than in Ethereum, and processed substantially faster. This enables a fast, cheap, and secure user experience unaffected by any high activity experienced on shared networks.

### **Where to now?**

- [Deploy a local CDK on Kurtosis](../cdk/getting-started/local-deployment.md). Follow the guide to deploy a CDK stack on your local machine.

- Check out the [concepts documentation](../cdk/concepts/layer2s.md) to understand the CDK at a high level.

- Have a look at the [CDK architecture docs](../cdk/concepts/architecture.md) to understand the CDK’s components and how they interact with each other.
