This page covers the key features and capabilities of the Agglayer Chain Development Kit (CDK), including supported execution stacks, EVM compatibility, Agglayer integration, performance benchmarks, rollup modes, and target audiences. Whether you're a developer, startup founder, or enterprise team, this guide will help you understand how CDK can power your custom Ethereum Layer 2 chain.

## Multistack Support

CDK gives developers the flexibility to choose from multiple execution stacks based on their technical goals. Use **cdk-opgeth** for OP Stack familiarity and Geth-based performance, or choose **cdk-erigon** for deep customization and advanced ZK integration. More stacks will be supported in the future.

## EVM Compatibility

CDK chains are fully EVM-equivalent. Developers can deploy existing smart contracts, use familiar Ethereum tooling, and preserve current workflows without rewrites or reconfiguration.

## Native Agglayer Integration

All CDK chains connect to **Agglayer** by default. This provides unified liquidity, shared state, and seamless messaging across chains—without requiring additional setup or bridging infrastructure.

## High Performance

- **cdk-opgeth** supports 60 to 100+ million gas per second (Mgas/s) when paired with the G2 sequencer.  
- **cdk-erigon** delivers up to 60+ Mgas/s in burst throughput, with native support for ZK proving and advanced configuration.

## Flexible Rollup Modes

Soon, both **cdk-opgeth** and **cdk-erigon** will support zkRollup, Validium, and Sovereign modes. Developers can choose the configuration that best balances cost, trust assumptions, and data availability for their specific use case.

## Who Is CDK For?

### Web3 Developers

Deploy purpose-built Layer 2 chains with precise control over execution logic, rollup mode, data availability, and token design. CDK supports EVM tooling and workflows out of the box.

### Founders and Builders

Launch performant, production-ready chains quickly with help from trusted implementation providers:

- **Conduit** supports **cdk-opgeth** and the G2 sequencer.  
- **Gateway.fm** supports **cdk-erigon** production deployments.

### Enterprises

Build secure and scalable blockchain infrastructure with enterprise-level configurability. For example, **cdk-erigon** offers full customization, including:

- Native gas token support  
- Three live ZK-secured rollup modes  
- Enhanced flexibility for enterprise-grade Layer 2s