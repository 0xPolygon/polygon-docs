# Bridging

[Bridges](https://ethereum.org/en/developers/docs/bridges/) are fundamental components of L2s. A core feature of chains built with the CDK is _interoperability_, which allows developers to access funds from Ethereum as well as other L2s. This is crucial for building dApps on your chain.

## L1 <-> L2 bridge

CDK-built chains come with a built-in bridge service and customizable UI that enables users to move assets (both native and ERC20 tokens) between L1 and L2 or between different L2s.

A key benefit to building ZK-powered L2s with the CDK is that there are no challenge periods, as those experienced in [optimistic rollups](./zk-vs-optimistic.md#optimistic-rollups). This means, as soon as the [aggregation](./transaction-lifecycle.md#aggregated) process is complete (i.e. a ZK proof is posted & verified), users can move funds from a CDK-built L2 to the L1.

## Unified bridge

By default, chains launched using the CDK are opt-in to the AggLayer. The unified bridge enables cross-chain transactions amongst chains that have opted-in to the [AggLayer](https://polygon.technology/blog/aggregated-blockchains-a-new-thesis).

This allows developers to build unique cross-chain experiences by integrating a `bridgeAndCall` function into their smart contracts, enabling users to call smart contract functions on other L2 chains without requiring users to bridge or hold tokens on the target chain.

## Further reading

- [Unified Bridge Overview](https://docs.polygon.technology/zkEVM/architecture/protocol/unified-LxLy/lxly-bridge/)
