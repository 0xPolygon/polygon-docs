## What is the Chain Development Kit (CDK)?
CDK is a multistack toolkit by Polygon Labs for building Ethereum L2 chains with native Agglayer integration. It offers developers stack flexibility, shared liquidity, and zero-knowledge security options.

## What does it mean for CDK to go multistack?
CDK’s multistack approach means you can build with OP Stack (`cdk-opgeth`), Erigon (`cdk-erigon`), and more stacks coming soon—all while maintaining Agglayer-native connectivity.

## What is cdk-opgeth, and what does it offer?
Built on Geth (Ethereum’s leading client), `cdk-opgeth` supports fast launch timelines, Sovereign mode with pessimistic proof security, and upcoming zkRollup/Validium options via SP1 prover.

## How does cdk-erigon differ from cdk-opgeth?
`cdk-erigon` offers deep customization for projects that need native tokens, advanced pricing, and tailored performance. It’s ZK-powered and enterprise-ready with proven production usage.

## What is a sovereign chain in CDK?
Sovereign mode enables chains to skip full ZK proving while maintaining security through pessimistic proofs. It ensures no chain can extract more than it deposits—low-cost and safe.

## Why is Agglayer integration important for CDK chains?
Agglayer provides a unified liquidity layer, shared state, and seamless UX across all connected chains—eliminating fragmentation and powering aggregation.

## Do I need to use Agglayer with CDK chains?
Agglayer connectivity is enabled by default, but technically optional. Developers can opt out for isolated deployments.

## How can I start building a CDK chain?
Check out the CDK Quickstart guides. For production-ready launches, contact implementation providers like Conduit (cdk-opgeth) or Gateway.fm (cdk-erigon).