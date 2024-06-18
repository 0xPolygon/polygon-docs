# Bridging

[Bridges](https://ethereum.org/en/developers/docs/bridges/) are a fundamental component of L2s. A core feature of chains built with the CDK is **interoperability**, which allows developers to access funds from Ethereum as well as other L2s when building dApps on your chain.

## L1 <-> L2 Bridge

CDK chains come with a built-in bridge service and customizable UI that enables users to move assets (both native and ERC20 tokens) between L1 and L2 or between different L2s.

A key benefit to building ZK-powered L2s with the CDK is that there are no challenge periods unlike [optimistic rollups](./zk-vs-optimistic.md#optimistic-rollups), meaning users can move funds from the L2 to the L1 immediately after the [aggregation](./transaction-lifecycle.md#aggregated) process is complete (i.e. a ZK proof is posted & verified).

## Unified Bridge

By default, chains launched using the CDK are opt-in to the AggLayer, enabling cross-chain transactions via the unified bridge. The unified bridge enables cross-chain L2 to L2 transactions to other chains that have opted-in to the [AggLayer](https://polygon.technology/blog/aggregated-blockchains-a-new-thesis).

This allows developers to build unique cross-chain experiences by integrating a `bridgeAndCall` function into their smart contracts, enabling users to call smart contract functions on other L2 chains without requiring users to bridge or hold tokens on the target chain.

## Further Reading

- [Unified Bridge Overview](https://docs.polygon.technology/zkEVM/architecture/protocol/unified-LxLy/lxly-bridge/)
