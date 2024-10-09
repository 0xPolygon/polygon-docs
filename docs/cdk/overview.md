---
comments: true
---

The Polygon Chain Development Kit (CDK) is a modular, open-source software toolkit that enables blockchain developers to configure ZK-powered chain architectures.

With Polygon CDK, developers can launch new chains running the Polygon zkEVM protocol as Layer 2s on Ethereum.

Developers can configure ZK-powered rollups, validium networks, or even sovereign chains with their own tailored finality mechanisms.

Polygon CDK utilizes an especially developed CLI tool to abstract away the complexity of running or configuring CDK components. It is an interface that developers use in the command line to run the CDK.

## Trustless finality

Why does Polygon CDK focus on ZK-powered chains?

The power of zero-knowledge technology is seen in enabling chains to achieve trustless finality, where chain users do not have to rely on a few individuals to confirm finality of their transactions.

With Polygon CDK, developers can first decide how they want to configure proving and then choose the right CDK mode to build their chain.

Polygon CDK therefore has two modes:

- The CDK rollup/validium mode used for configuring CDK components that run the Polygon zkEVM protocol.
- The CDK sovereign chain mode used for custom chains. For instance a chain that uses a prover external to Polygon, such as Succinct's SP1.

These two Polygon CDK modes are released in the chronological order given above, with the Polygon-centric CDK mode coming first and then followed by the sovereign chain CDK mode.

There are two types of ZK-proofs that are crucial to the Polygon ecosystem: Full execution proofs and Pessimistic proofs.

### Full execution proofs

CDK rollups and validiums utilize *full execution proofs* as part of their finality mechanisms.

A *full execution proof* (FEP) is a zero-knowledge proof attesting to the correctness of the chain's full state transition.

For example, an FEP attests to the fact that the VM (such as the Polygon zkEVM, Succinct's zkVM, or MoveVM) has executed all state transitions in accordance with the specifications.

A ZK-powered chain is therefore by definition an FEP chain.

### Pessimistic proofs

CDK-built chains that interoperate via the [unified bridge](https://www.notion.so/CDK-Overview-11580500116a80aa8f2ef9565d4e32bf?pvs=21) achieve cross-chain security through the use of *pessimistic proofs*.

A *pessimistic proof* (PP) is a zero-knowledge proof attesting to the fact that a chain's bridge transitions were properly executed and all withdrawals are collateralized.

Pessimistic proofs are the best solution to achieving trustless and secure interoperability for any network of [AggLayer-connected CDK chains](https://www.notion.so/CDK-Overview-11580500116a80aa8f2ef9565d4e32bf?pvs=21).

## Polygon CDK benefits

Polygon CDK provides the components necessary to build a layer 2 blockchain that is secure, scalable, and interoperable with other chains.

- Modularity: CDK modular components allow developers to easily customize their L2 environment and build a chain that meets their specific needs.
- Interoperability: Opt-in to the [AggLayer](https://docs-dev.polygon.technology/1562/agglayer/overview/) to bootstrap your chain’s ecosystem, enable cross-chain transactions while expanding your reach, user base, and liquidity from other established chains.
- Sovereignty: Maintain full control over your chain’s revenue, governance, security, economic policies, and more.
- Low gas fees: Transaction fees are orders of magnitude lower than in Ethereum, and processed substantially faster. This enables a fast, cheap, and secure user experience unaffected by any high activity experienced on shared networks.

### What you can do

- [Deploy a local CDK on Kurtosis](https://docs-dev.polygon.technology/1562/cdk/getting-started/local-deployment/). Follow the guide to deploy a CDK stack on your local machine.
- Check out the [concepts documentation](https://docs-dev.polygon.technology/1562/cdk/concepts/layer2s/) to understand the CDK at a high level.
- Have a look at the [CDK architecture docs](https://docs.polygon.technology/cdk/architecture/cdk-zkevm/) to understand the CDK’s components and how they interact with each other.

