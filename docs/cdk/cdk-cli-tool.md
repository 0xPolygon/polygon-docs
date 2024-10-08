The Polygon Chain Development Kit, or simply CDK, is a tool box of components that a chain administrator can use to build a rollup or validium chain.

At a high level, CDK components are like building blocks a chain administrator can select to configure a ZK-powered chain according to their own design.

To abstract away the complexity of running or configuring CDK components, Polygon provides a Rust-based CLI tool which is an interface that chain administrators can use to interact with CDK components.

This CLI tool is an entry point for chain administrators to access the CDK system.

## Installation

To use the CLI tool the chain admin needs only download the precompiled CDK package ([the binaries](https://github.com/0xPolygon/cdk/releases/)).

There is no need to have Golang, checkout the CDK repo, or install anything else. It is also trustless.

## **Running the CLI tool**

!!! info
    
    Requirements

    Get the binaries, packages and docker images published with each release, [here](https://github.com/0xPolygon/cdk/releases/).
    For example, version [v0.2.1](https://github.com/0xPolygon/cdk/releases/tag/v0.2.1).
    
## Commands

### cdk

Here the Admin needs to provide the [cdk-node configuration file](needs a reference to the configuration doc) and a genesis file of the desired chain.

Usage: `cdk --config <CONFIG> --chain <CHAIN> <COMMAND>`

Commands:
* node - Run the cdk-node with the provided configuration    
* erigon - Run cdk-erigon node with the provided default configuration
* help    Print this message or the help of the given subcommand(s)

Options:
  -c, --config <CONFIG>  The path to the configuration file [env: CDK_CONFIG_PATH=]
  -g, --chain <CHAIN>    The path to a chain specification file [env: CDK_GENESIS_PATH=]
  -h, --help             Print help

### cdk node

To run cdk-node use the `node` subcommand

Usage: cdk --config <CONFIG> --chain <CHAIN> node [OPTIONS]

Options:
  -c, --components <COMPONENTS>  Components to run [env: CDK_COMPONENTS=]
  -h, --help                     Print help

### cdk erigon

Chain administrators can run a cdk-erigon RPC node that syncs to an existing chain with default parameters.

This subcommand is intended for quickly spin-up of an RPC node or to test existing chains with default configuration values. In order fine tune and to access all configuration values, [check the full cdk-erigon documentation](reference to erigon configuration docs).

Usage: cdk --config <CONFIG> --chain <CHAIN> erigon

Options:
  -h, --help  Print help

The above command generates all the required configuration files for cdk-erigon on-the-fly and run the node.
