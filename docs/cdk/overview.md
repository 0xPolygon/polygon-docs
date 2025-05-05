The **Agglayer Chain Development Kit (CDK)** is a multistack toolkit for building custom Ethereum Layer 2 (L2) chains. Each CDK chain is natively connected to **Agglayer**, enabling seamless cross-chain interoperability, shared liquidity, and unified state across an expanding ecosystem of L2s.

CDK supports multiple execution stacks so developers can choose the architecture that best suits their project. Current options include:

- **cdk-opgeth**: A high-performance, OP Stack-style client built on Ethereum’s most widely adopted execution client, Geth.
- **cdk-erigon**: A customizable, ZK-secure client with advanced configuration options and full Agglayer connectivity.

More stacks will be added soon. Whether you're building a DeFi protocol, launching a high-throughput chain, or creating a security-first enterprise appchain, **CDK provides the flexibility to launch on your terms**—while benefiting from unified liquidity across the Agglayer network.

## Projects Using CDK

- Ternoa
- Merlin Chain
- Magic Labs (Newton)
- Silicon Network
- Witness Chain
- WireX
- Lumia (formerly Orion)
- Okto Wallet
- Palm Network
- Prom
- OKX
- Moonveil  
*...and more*

## CDK-opgeth

### Overview

**cdk-opgeth** enables developers to launch Ethereum-native Layer 2 chains using **Geth**, Ethereum’s most widely adopted execution client. It combines the familiar **OP Stack architecture** with **Agglayer’s infrastructure** for seamless interoperability, high throughput, and ZK-backed scalability.

### Key Highlights

- **Native Agglayer connectivity** via Sovereign mode  
- Built on **Geth**, which powers over 50% of Ethereum clients  
- Designed by **Conduit**, core maintainers of cdk-opgeth and the **G2 sequencer**

### Who Should Use cdk-opgeth?

- **Teams familiar with the OP Stack**: Leverage existing tooling and development workflows without a steep learning curve  
- **Projects seeking fast launch timelines**: Spin up a production-ready L2 in under one day with implementation support  
- **Builders prioritizing Ethereum-native tooling**: Maintain compatibility with widely-used Ethereum clients, debuggers, and dev environments

### Performance

- **60 to 100+ million gas per second (Mgas/s)**  
- **Over 4,700 peak transactions per second (TPS)**  
- **Finality in under 60 minutes**  
- Supports **rapid deployment and testing** with minimal setup

### Supported Modes

- **Sovereign (live)**:  
  Default mode offering Agglayer connectivity secured by **pessimistic proofs**.  
  No prover required. Optimized for **low-cost L2 chains**.

- **Validium (in development)**:  
  **ZK-secured execution** with **offchain data storage** for lower cost and higher throughput.

- **zkRollup (in development)**:  
  Fully **onchain ZK rollup support** for maximum security, scalability, and **Ethereum-aligned trust assumptions**.

## CDK-erigon

### Overview

**cdk-erigon** is the original CDK stack, built on the high-performance **Erigon** client. It offers deep customization capabilities, such as **native gas token support** and **three live rollup modes** backed by **zero-knowledge proofs**. Designed for **enterprise-grade deployments**, cdk-erigon chains are optimized for **scalability**, **configurability**, and **ZK-secured execution**.

### Key Highlights

- **Native token support** with custom gas metering and pricing flexibility  
- Maintained by **Gateway.fm**, with **three ZK-based modes** live in production  
- **Battle-tested** with over **500 million transactions** processed by cdk-erigon-powered chains

### Who Should Use cdk-erigon?

- **Enterprise deployments**: Ideal for security-first environments and high-throughput applications requiring configurable infrastructure  
- **Projects requiring tailored configurations**: Support for custom gas tokens, advanced rollup settings, and multiple data availability strategies  
- **Developers prioritizing ZK security and token control**: Built-in support for fully ZK-secured rollups with native token issuance and validator flexibility

### Performance

- **Over 60 million gas per second (Mgas/s)** in burst capacity  
- **More than 1,000 peak transactions per second (TPS)**  
- **Finality in as little as 30 minutes**  
- **Up to 90% reduction** in node storage footprint  
- **Production deployment timelines** typically around **15 days**

### Supported Modes

- **Sovereign (live)**:  
  Default mode with native Agglayer connectivity secured by **pessimistic proofs**.  
  Optimized for **cost-effective execution** and **cross-chain interoperability** without ZK provers.

- **Validium (live)**:  
  **ZK-secured execution** with **offchain data availability**.  
  Designed for **performance** and **cost savings** while maintaining **Agglayer-backed trust guarantees**.

- **zkRollup (live)**:  
  Fully **onchain ZK rollup** with maximum **security** and **verifiability**.  
  Suitable for applications requiring **onchain data integrity** and the strongest **Ethereum-aligned guarantees**.