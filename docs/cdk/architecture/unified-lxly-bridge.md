
## The LxLy bridge: current scenario 

Simply put, the LxLy bridge is the native bridging infrastructure for all CDK chains. The way it works is each individual CDK chain deploys an instance of the LxLy bridge that connects to an L1 (Ethereum by default) by deploying the necessary contracts that help carry out deposit and withdrawal of assets, along with the escrow management. These contracts are managed by node operators corresponding to the respective CDK chains.

This changes as the AggLayer v1 (AL1) goes online, and introduces an upgrade to the existing LxLy architecture in the form of a **unified instance** of the LxLy bridge that multiple chains can connect to.

## What's "unified" LxLy bridge?

Polygon AggLayer envisions a scalability solution that leverages shared and state and unified liquidity across multiple ZK-powered chains within the Polygon ecosystem, all powered by the CDK infrastructure.

!!! tip "What's AggLayer?"

    Want to learn more about what AggLayer is and what it looks to achieve? Check out [this doc in the Learn space](../../learn/agglayer.md).

All of this cool infrastructure needs a unified channel for easy transmission of assets and messages between the multiple chains connected via the AggLayer. And this is where the **unified LxLy (uLxLy) bridge** comes into play. It allows all chains to take advantage of the AggLayer's unified liquidity, lower transaction costs, and more.

## uLxLy bridge implementation

The new unified model of the LxLy bridge introduced as a part of AL1

