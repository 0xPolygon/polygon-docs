The Polygon Chain Development Kit (CDK) is an open-source stack for blockchain developers to build sovereign layer 2 blockchains powered by zero-knowledge (ZK) proofs.

It consists of modular components designed to be fully composable; empowering developers to customize each aspect of their chain to meet their specific needs.

## CDK Features

The CDK provides the components necessary to build a layer 2 blockchain that is secure, scalable, and interoperable with other chains. Below are some of the key features of the CDK:

- **Security**: The Polygon Labs team are pioneers in the zero-knowledge ecosystem and have built many of the most advanced ZK technologies in production today such as [plonky3](https://docs.polygon.technology/learn/plonky/?h=plonky3#plonky-3). The CDK leverages allows developers to build high-performance, high-security, scalable L2s that utilize the latest innovations in zero-knowledge technology.

- **Scalability**: Transaction fees and finality on chains built with the CDK are orders of magnitude lower and faster than Ethereum. By building a chain with the CDK, developers can provide users with a seamless experience that is fast, cheap, secure and unaffected by any extraneous high activity on shared networks.

- **Modularity**: As logic is separated into modular components, developers can easily swap out components in a "plug and play" fashion to customize their chain, for example, by replacing entire components such as the data availability layer, or making granular-level configurations to each component; such as modifying the sequencer logic to comply with legal regulations.

- **Interoperability**: Chains built with the CDK can access the users and liquidity of all other chains that have opted into the [AggLayer](https://docs.polygon.technology/cdk/glossary/#agglayer-v1-al1). This enables cross-chain transactions and access to the users & liquidity of other chains out of the box without forcing users to manually bridge assets to your chain.

- **Sovereignty**: There is no sacrifice required when building a chain with the CDK or joining the AggLayer. Developers maintain full control over the chain&rsquo;s revenue, governance, security, economic policies, etc.

## Dive Deeper into the CDK

Whether you&rsquo;re a developer looking to build a new chain or a researcher interested in looking under the hood, the CDK documentation provides a comprehensive guide to the CDK&rsquo;s architecture, components, and how to get started building with the CDK:

- [Concepts](https://docs.polygon.technology/cdk/concepts/layer2s) to understand the CDK at a high level
- [Getting Started](https://docs.polygon.technology/cdk/getting-started) to deploy a CDK stack on your local machine
- [Architecture](https://docs.polygon.technology/cdk/architecture/cdk-zkevm/) to understand the CDK&rsquo;s components and how they interact with each other
