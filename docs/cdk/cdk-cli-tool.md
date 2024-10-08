The Polygon Chain Development Kit, or simply CDK, is a tool box of components that a chain administrator can use to build a rollup or validium chain.

At a high level, CDK components are like building blocks a chain administrator can select to configure a ZK-powered chain according to their own design.

To abstract away the complexity of running or configuring CDK components, Polygon provides a RUST-based CLI tool which is an interface that chain administrators can use to deploy components.

This CLI tool is an entry point for chain administrators to access the CDK system.

## **Running the CLI tool**

!!! info
    
    Requirements

    Get the binaries, packages and docker images published with each release, [here](https://github.com/0xPolygon/cdk/releases/).
    For example, version [v0.2.1](https://github.com/0xPolygon/cdk/releases/tag/v0.2.1).
    

Chain administrators can configure an RPC node or a CDK Erigon node by running a single command:

```
 cdk --config ../kurtosis-cdk/genesis/cdk-node-config.toml --chain ../kurtosis-cdk/genesis/genesis.json erigon
```

Here the Admin simply provides a small configuration file and a genesis file.

The above command generates all the required configuration files, configures the node, and syncs with the network.

## **Advantages of using the CLI tool**

The main advantage with using the CLI is in providing a small config file and a genesis file instead of having to run a Go script four times in order to generate [four configuration files](https://github.com/0xPolygonHermez/cdk-erigon/?tab=readme-ov-file#dynamic-chain-configuration), and download them.

For instance,

```
 go run cmd/hack/allocs/main.go [your-file-name]
```

That is, without this CLI, every new user who wants to configure an RPC node would have to first,

- Checkout the CDK Erigon repo.
- Install Golang.
- Run the script.

Another alternative is for the user to request a trusted chain builder to provide the four configuration files. The chain builder generates the files and sends them to user for downloading.

But this requires the user to trust such a provider of the files.

To use the CLI tool the chain admin needs only download the precompiled CDK package ([the binaries](https://github.com/0xPolygon/cdk/releases/)).

There is no need to have Golang, checkout the CDK repo, or install anything else. It is also trustless.

## **Why RUST-based CLI?**

The CLI is written in RUST language to align with Polygon's vision to ensure easy integration of Polygon technology stack with popular RUST-based platforms and libraries (such as Succinct's SP1).

This is also in anticipation of new RPC endpoints implementation to enable integration of the CDK system with external systems, and thus accommodate vanilla execution clients that use pessimistic proofs.

With such endpoints Reth, Cosmos space chains, or other execution clients can be introduced without code modifications.
