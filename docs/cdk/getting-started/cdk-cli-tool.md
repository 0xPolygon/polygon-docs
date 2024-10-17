To simplify the process of running and configuring CDK components, Polygon provides a Rust-based CLI tool which is an interface that chain administrators can use to interact with the components.

This CLI tool is an entry point for chain administrators to access the CDK system.

## Installation

As the chain admin, you simply need to download the precompiled [CDK package binaries](https://github.com/0xPolygon/cdk/releases/).

## Running the CLI tool

!!! info
    
    Requirements:

    Get the binaries, packages and docker images published with each release, [here](https://github.com/0xPolygon/cdk/releases/).
    
## Commands

### CDK

Here, you need to provide the CDK node configuration file and the genesis file for your desired chain.

Usage: `cdk <COMMAND>`

Commands:
* `node` - Run the cdk-node with the provided configuration
* `erigon` - Run cdk-erigon node with the provided default configuration
* `versions` - Output the corresponding versions of the components
* `help`    Print this message or the help of the given subcommand(s)

Options:
* `-h, --help` - Print help

### `cdk node`

To run cdk-node use the `node` subcommand with one of the options mentioned below.

Usage: `cdk node [OPTIONS]`

Options:
* `-C, --config <CONFIG>` - The path to the configuration file [env: `CDK_CONFIG_PATH=`]
* `-c, --components <COMPONENTS>` - Components to run [env: `CDK_COMPONENTS=`]
* `-h, --help` - Print help

Example:

```
cdk node --config /etc/cdk/cdk-node-config.toml --components sequence-sender,aggregator
```

### `cdk erigon`

You can run a cdk-erigon RPC node that syncs to an existing chain using the default parameters.

This subcommand is intended for quickly spinning up an RPC node or testing existing chains with default configuration values. In order to fine-tune settings and access all available configuration options, refer to the [full cdk-erigon documentation](../../cdk/getting-started/cdk-erigon/index.md) on Erigon configuration.

Usage: `cdk erigon [OPTIONS]`

Options:
* `-C, --config <CONFIG>` - The path to the configuration file [env: `CDK_CONFIG_PATH=`]
* `-g, --chain <CHAIN>` - The path to a chain specification file [env: `CDK_GENESIS_PATH=`]
* `-h, --help` - Print help

### `cdk versions`

The above command generates all the required configuration files for cdk-erigon on the fly and runs the node.

To print the corresponding versions of the components, run the following command:

Usage: `cdk versions`

Options:
* `-h, --help` - Print help

Example:

```
cdk erigon --config /etc/cdk/cdk-node-config.toml --chain genesis.json
```
