<!--
---
comments: true
---
-->

This glossary defines technical concepts used throughout the Agglayer CDK documentation. Whether you're building with `cdk-opgeth`, `cdk-erigon`, or deploying a multistack rollup, this reference provides clear definitions of key terms and components.

### Agglayer

Agglayer is a cross-chain settlement layer that connects the liquidity and users of any blockchain for fast, low-cost interoperability and growth. It enables trustless bridging, shared messaging, and unified state across Layer 2s using zero-knowledge (ZK) proofs.

[Visit Agglayer.dev](https://www.agglayer.dev/)

### Agglayer CDK (Chain Development Kit)

A multistack toolkit for building custom Ethereum Layer 2 chains. Each CDK chain is natively connected to Agglayer for seamless interoperability, shared liquidity, and integrated messaging. Developers can choose between stacks such as `cdk-opgeth` and `cdk-erigon`, with more to be added in the future.

### CDK-erigon

An execution stack in the Agglayer CDK optimized for customization and ZK security. It provides native token support, custom gas metering, multiple rollup modes (zkRollup, Validium, Sovereign), and extensive configuration options.

### CDK-opgeth

An execution stack based on Ethereum’s Geth client and the OP Stack architecture. Designed for fast, high-throughput deployments and OP Stack familiarity, with native Agglayer integration. Supports Sovereign mode now, with zkRollup and Validium support forthcoming.

### Chain Operator

An individual, team, or DAO responsible for launching and managing a CDK-based chain. Operators may handle sequencing, bridge operations, infrastructure deployment, data availability configuration, and other network responsibilities.

### Data Availability (DA)

The requirement that transaction data remains accessible to Layer 1 validators for verifying off-chain execution. DA ensures the security of modular rollups. CDK chains can use on-chain DA (e.g., Ethereum), off-chain DACs, or local solutions.

### Data Availability Committee (DAC)

A decentralized set of nodes that ensures off-chain data availability for CDK chains using Validium mode. DAC nodes fetch transaction data, verify it, sign it, and store it for later retrieval.

### Implementation Providers (IPs)

External infrastructure teams that assist developers with launching and maintaining CDK chains. Notable IPs include Conduit (for `cdk-opgeth`) and Gateway.fm (for `cdk-erigon`).

### Multistack

An architectural feature of CDK that allows developers to select from multiple execution stacks based on their project needs. All stacks integrate natively with Agglayer.

### Rollups

Layer 2 solutions that execute transactions off-chain and post state data to Ethereum. CDK supports multiple rollup types, including:

- [Optimistic rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/)
- [ZK rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/)
- Validium (ZK with off-chain DA)
- Sovereign (non-ZK with pessimistic proofs)

### Sovereign Mode

A rollup configuration that does not use a ZK prover. Instead, Agglayer enforces security through pessimistic proofs, ensuring that no chain can withdraw more than it deposits. Available in both `cdk-opgeth` and `cdk-erigon`.

### Stake the Bridge (STB)

A feature of the Unified Bridge that allows CDK chain operators to stake and manage assets deposited to their networks. Enables custom staking, liquidity incentives, or economic configurations at the L2 level.

### Unified Bridge

The shared bridge infrastructure for CDK chains, providing secure cross-chain asset transfers and messaging. Replaces the LxLy bridge. It supports shared escrow, sovereign and ZK rollup flows, and seamless Agglayer integration.

### Unified Escrow

A component of the Unified Bridge that holds tokens either bridged from Ethereum or minted natively on Layer 2. Ensures consistent accounting and solvency across all CDK chains.

### Validium

A rollup configuration that uses ZK proofs for execution but stores transaction data off-chain, reducing costs and increasing throughput. CDK Validium chains rely on DACs for off-chain data availability.

[Learn more about Validium](https://ethereum.org/en/developers/docs/scaling/validium/)

### ZK Proofs

Zero-knowledge proofs validate computations without revealing input data. Agglayer uses ZK proofs to provide cryptographic guarantees for execution, enabling fast finality and trustless security across chains.
