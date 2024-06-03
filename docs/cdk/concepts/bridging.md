# Bridging

[Bridges](https://ethereum.org/en/developers/docs/bridges/) are a fundamental component of L2s. They allow users to bridge funds from the L1 (Ethereum) seamlessly, to pay for gas fees or interact with dApps on the L2, and optionally bridge funds back to the L1.

CDK chains come with a built-in bridge service and customizable UI that enables users to move assets (both native and ERC20 tokens) between L1 and L2.

A key benefit to building ZK-powered L2s with the CDK is that there are no challenge periods unlike [optimistic rollups](./zk-vs-optimistic.md#optimistic-rollups), meaning users can move funds from the L2 to the L1 immediately after the [aggregation](./transaction-lifecycle.md#aggregated) process is complete (i.e. a ZK proof is posted & verified).

![Bridge UI for CDK](../../img/cdk/bridge-ui.png)
