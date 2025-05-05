This section answers common questions about the Agglayer Chain Development Kit (CDK), including multistack support, execution stack differences, Agglayer integration, and how to get started. If you're exploring CDK for development or deployment, this is a great place to begin.


## What is the Agglayer Chain Development Kit (CDK)?

CDK is a toolkit for launching Ethereum Layer 2 chains that come with **native Agglayer connectivity**. It supports multiple stacks—such as **cdk-opgeth** and **cdk-erigon**—allowing developers to build **performant, interoperable chains** without being locked into a single architecture.

## What does it mean for CDK to go multistack?

**Multistack support** means CDK allows developers to select from different execution stacks based on their needs. Each stack is fully integrated with Agglayer and offers unique benefits around **performance**, **tooling**, and **flexibility**.

## What is cdk-opgeth, and what does it offer?

**cdk-opgeth** is a CDK stack based on Ethereum’s **Geth client** and the **OP Stack** architecture. It offers a **familiar developer environment**, **high throughput**, **native Agglayer connectivity**, and **future support for zkRollup and Validium modes**.

## How does cdk-erigon differ from cdk-opgeth?

**cdk-erigon** is optimized for **customization** and **ZK security**. It supports:
- Native gas tokens
- Three rollup modes (zkRollup, Validium, Sovereign)
- Advanced configuration options

**cdk-opgeth** is designed for developers familiar with the OP Stack who want **familiar tooling** and **performance**, with an **upgrade path to ZK**.

## What is a sovereign chain in CDK?

A **sovereign chain** operates **without a prover**. Instead, it uses **pessimistic proofs via Agglayer** to enforce safety and ensure that no chain can withdraw more than it deposits. This enables **secure, low-cost execution** with **fast finality**.

## Why is Agglayer integration important for CDK chains?

**Agglayer** enables CDK chains to share **liquidity**, **state**, and **messaging** across an interconnected network. This creates **seamless user experiences** and **interoperability** between chains, regardless of their execution stack.

## Do I need to use Agglayer with CDK?

CDK chains are **connected to Agglayer by default**. While it's technically possible to disable this, doing so removes the benefits of **unified liquidity** and **cross-chain UX**.

## How can I start building with CDK?

Visit the **CDK developer documentation** to deploy a **local testnet**. For **production-ready deployments**:
- Contact **Conduit** for **cdk-opgeth**
- Contact **Gateway.fm** for **cdk-erigon**