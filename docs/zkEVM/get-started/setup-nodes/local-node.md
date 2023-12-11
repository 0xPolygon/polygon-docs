Developers who wish to test their own smart contracts, experiment with new code, or simply test a zk-rollup network on their local machines can do so by setting up Polygon zkEVM's local development environment.

Developers can setup a node with either the Polygon zkEVM's mainnet or the testnet.

This tutorial is a guide to setting up a local but single zkEVM node. It is _single_ because it has no connections to external peers. It is a sandbox environment existing only on the user's local machine.

!!!caution
    Currently the zkProver does not run on ARM-powered Macs. For Windows users, the use of WSL/WSL2 is not recommended.

    Unfortunately, Apple M1 chips are not supported for now - since some optimizations on the zkProver require specific Intel instructions. This means some non-M1 computers won't work regardless of the OS, for example: AMD.

At the end of this tutorial, the following components will be running:

- zkEVM node databases.
- Explorers and their databases.
- L1 network.
- Prover.
- zkEVM node components.

## Prerequisites

The tutorial for current version of the environment requires `go`, `docker` and `docker-compose` to be installed on your machine. If you don’t have these installed, check out the links provided below:

- <https://go.dev/doc/install>
- <https://www.docker.com/get-started>
- <https://docs.docker.com/compose/install/>

### System requirements

- zkEVM Node: 16GB RAM with 4-core CPU.
- zkProver: 1TB RAM with 128-core CPU.

Running a full-fledged zkProver requires at least 1TB of RAM. However, users with less memory can opt to use the mock Prover.

## Setting up zkNode

Start by cloning the [official zkNode repository](https://github.com/0xPolygonHermez/zkevm-node) from Polygon zkEVM Github.

```bash
git clone https://github.com/0xPolygonHermez/zkevm-node.git
```

Build the `zkevm-node` docker image.

```bash
make build-docker
```

The image is built only once and whenever the code has changed.

!!!caution Building Docker Image
    Every testnet version needs to use configuration files from the correct and corresponding tag. For instance: Make sure to use configuration files from RC9 tag in order to build an RC9 image.

    All tags can be found here: https://github.com/0xPolygonHermez/zkevm-node/tags.

Certain commands on the `zkevm-node` can interact with smart contracts, run specific components, create encryption files, and print debug information.

To interact with the binary program, we provide `docker-compose` files and a `Makefile` to spin up/down the various services and components, ensuring smooth local deployment and a better command line interface for developers.

!!!warning
    All the data is stored inside of each docker container. This means once you remove the container, the data will be lost.

The `test/` directory contains scripts and files for developing and debugging.

Change directory to `test/` on your local machine:

```bash
cd test/
```

Run the zkNode environment:

```bash
make run
```

Stop the zkNode with this command:

```bash
make stop
```

Restart the zkNode environment with this command:

```bash
make restart
```

## Configuration parameters

​
The Synchronizer regularly pulls for network updates, mainly from Ethereum but also via the Trusted Sequencer's broadcasting mechanism, in order to stay up-to-date. Unless otherwise specified in the setup, the Synchronizer's default syncing rate is every 2 seconds.

The Keystore file, used to store private keys, is normally required for running the Sequencer and the Aggregator but not for the Synchronizer/RPC-setup.

!!!info
    We have the inconvenient situation where the Keystore file is required to run the node when it shouldn't be the case. For example, if no transactions are sent to L1 then Keystore is not required, especially in the current zkEVM Testnet, where a trusted sequencer and a trusted aggregator are used.

    This will be reviewed when a decentralised zkEVM network is implemented.

## Sample data

Note that the `make run` command only executes containers required to run the environment, but executes nothing else. This means your local zkEVM network is initially empty, and therefore needs to be populated with some data before any testing can begin.

The following scripts are available if you require sample data that has already been deployed to the network.

```bash
# To add some examples of transactions and smart contracts:
make deploy-sc

# To deploy a full Uniswap environment:
make deploy-uniswap

# To grant the MATIC smart contract a set amount of tokens:
make run-approve-matic
```

## Connecting to MetaMask

!!!info
    Metamask requires the network to be running while configuring it, so make sure your network is up.

MetaMask can be configured to use the local zkEVM environment by following the steps below:

1. Log in to your MetaMask wallet.
2. Click on your account picture and then on **Settings**.
3. On the left menu, click on **Networks**.
4. Click on **Add Network** button.
5. Fill up the L2 network information:
    - **Network Name:** Polygon zkEVM - Local
    - **New RPC URL:** <http://localhost:8123>
    - **ChainID:** 1001
    - **Currency Symbol:** ETH
    - **Block Explorer URL:** <http://localhost:4000>
6. Click on **Save**.
7. Click on **Add Network** button.
8. Fill up the L1 network information:
    - **Network Name:** Geth - Local
    - **New RPC URL:** <http://localhost:8545>
    - **ChainID:** 1337
    - **Currency Symbol:** ETH
9. Click on **Save**.

You can now interact with your local zkEVM network and sign transactions from your MetaMask wallet.
