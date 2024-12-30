### What is Polygon CDK?

Polygon CDK is a modular, open-source framework for building Ethereum-compatible Layer 2 blockchains. It enables developers to configure their Layer 2 to meet specific use cases, such as:

- zk-Rollup: For high throughput and trustless finality using zero-knowledge proofs.
- Validium: For cost-efficient scalability with off-chain data availability.
- Sovereign: For interoperability and shared liquidity secured via pessimistic proofs.

Polygon CDK allows developers to build scalable and customizable Layer 2 blockchains while leveraging Ethereum’s security and existing ecosystem.

---

### Why Should Developers Care?

- **Low costs and high performance**: Polygon CDK chains offer lower transaction fees and faster finality compared to Ethereum Layer 1 and many Layer 2 solutions.
- **Seamless cross-chain interoperability**: With Agglayer integration (currently in testnet), Polygon CDK chains can interact securely with other chains and external networks.
- **Modular and future-ready**: Developers can customize their chain’s architecture to meet specific use cases, ensuring compatibility with emerging technologies.
- **Ethereum-compatible**: Polygon CDK supports EVM tooling, ensuring a smooth developer experience and easy migration for existing applications.

---

### How Does It Work?

Polygon CDK simplifies the process of building Layer 2 blockchains by providing pre-built components for every essential layer of a chain. Here’s how it works at a high level:

#### Execution Layer

- Sequencer Nodes: Handle transaction ordering and provide RPC (Remote Procedure Call) endpoints for interacting with the chain.
- Prover: Ensures transaction validity and supports zk-Rollup configs by generating cryptographic proofs. Developers can use any prover suited to their needs.
- Pool Manager: Optimizes resource allocation for chains to efficiently process transactions.

#### Data Availability

- Ethereum DA: Stores transaction data directly on Ethereum for zk-Rollup configs, ensuring security and decentralization.
- Custom DAC: An off-chain solution for Validium configs, offering scalability and cost-efficiency while maintaining data integrity.
- Agglayer Pessimistic Proofs: Provides security and enables cross-chain functionality for Sovereign configs without requiring zk-SNARKs or on-chain data storage.

#### Settlement Layer

- Ethereum Bridge Contracts: Used by zk-Rollup configs to finalize transactions on Ethereum.
- Agglayer Integration: Sovereign configs settle transactions and enable interoperability through Agglayer using cryptographic pessimistic proofs.

#### Sequencer

- Sequence Sender: Ensures proper transaction ordering and maintains data integrity.

#### Interoperability

- Bridge APIs: Enable cross-chain transfers of assets and data, connecting Polygon CDK chains with Ethereum and other Layer 2s.
- Aggregator: Combines multiple proofs into a single proof for zk-Rollup configs to optimize validation.

---

### A Note on Configurations

Polygon CDK supports three main configurations—zk-Rollup, Validium, and Sovereign—which align with the most common Layer 2 use cases. These configurations use a standard set of components optimized for scalability, security, and interoperability.

While most developers rely on these configurations for simplicity, the stack is fully modular and customizable, allowing teams to adjust or replace components to create a Layer 2 chain tailored to their specific requirements.