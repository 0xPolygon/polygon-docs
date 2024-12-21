# What is Polygon CDK?

Polygon CDK is a modular, open-source framework for building Ethereum-compatible Layer 2 blockchains. It allows developers to create scalable, customizable chains, including:
- **zk-Rollups**: Chains using zero-knowledge proofs for high throughput and trustless finality.
- **Validiums**: Chains with off-chain data availability for cost-efficient scalability.
- **Sovereign Chains**: Chains natively connected to the Agglayer, secured via pessimistic proofs, enabling interoperability and shared liquidity.

With Polygon CDK, developers can build chains tailored to their needs while leveraging Ethereum’s security and existing ecosystem.

---

## How Does It Work?

Polygon CDK simplifies the process of building Layer 2 blockchains by providing pre-built components for every essential layer of a chain. Here’s how it works at a high level:

### Execution Layer
- **Sequencer Nodes**: Handle transaction ordering and provide RPC (Remote Procedure Call) endpoints for interacting with the chain. These nodes are essential for processing and validating transactions.
- **zkEVM Prover (Hermes)**: For zk-Rollups, this component generates zero-knowledge proofs to ensure transactions are secure and trustless. This is optional for other configurations.
- **Pool Manager**: Optimizes resource allocation for zkEVM-based chains, used in zk-Rollup configurations to process transactions efficiently.

### Data Availability
- **Ethereum DA**: Stores transaction data directly on Ethereum for zk-Rollup configurations, ensuring maximum security and decentralization.
- **Custom DAC (Data Availability Committee)**: For Validium configurations, this off-chain solution provides scalability and cost-efficiency while maintaining data integrity.
- **Agglayer Pessimistic Proofs**: Used in Sovereign Chains, Agglayer ensures security and enables cross-chain functionality without requiring zk-SNARKs or on-chain data storage.

### Settlement Layer
- **Ethereum Bridge Contracts**: Used by zk-Rollups to finalize transactions on Ethereum, ensuring trustless settlement.
- **Agglayer Integration**: Sovereign Chains settle transactions and enable interoperability through Agglayer, which uses cryptographic pessimistic proofs to secure cross-chain interactions.

### Sequencer
- **Sequence Sender**: Ensures that transactions are ordered properly and maintains the chain’s data integrity.

### Interoperability
- **Bridge APIs**: Enable cross-chain transfers of assets and data, connecting Polygon CDK chains with Ethereum and other Layer 2s.
- **Aggregator**: Combines multiple proofs into a single proof for zk-Rollups, optimizing validation processes.

### A Note on Sovereign Chains
Sovereign Chains built with Polygon CDK don’t use a prover like zk-SNARKs. Instead, they rely on the Agglayer for security via cryptographic pessimistic proofs. This approach ensures interoperability and scalability while allowing Sovereign Chains to maintain full independence.

By combining these components, Polygon CDK provides the flexibility to build zk-Rollups, Validiums, or Sovereign Chains based on your project's requirements. The framework is designed to deliver high performance, low costs, and seamless interoperability.

---

## Why Should Developers Care?

- **Low Costs and High Performance**: Polygon CDK chains offer significantly lower transaction fees and faster finality compared to Ethereum Layer 1 and many other Layer 2 solutions, making them ideal for high-throughput applications.

- **Seamless Cross-Chain Interoperability**: With Agglayer integration (currently in testnet), Polygon CDK chains can securely interact with other chains and external networks. This enables shared liquidity, cross-chain functionality, and ecosystem bootstrapping.

- **Modular and Future-Ready**: Developers can customize their chain’s architecture to fit specific needs, whether creating zk-Rollups, Validiums, or Sovereign Chains. The modular design ensures compatibility with emerging technologies.

- **Ethereum-Compatible**: Polygon CDK supports EVM tooling, ensuring a smooth developer experience and easy migration for existing applications while tapping into Ethereum's established ecosystem.