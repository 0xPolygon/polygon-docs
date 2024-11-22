<!--
---
comments: true
---
-->

The Polygon zkEVM beta mainnet is available for developers to launch smart contracts, execute transactions, and experiment. This document shows you how to launch your own production zkNode.

Developers can setup a production node with either the Polygon zkEVM mainnet or the Cardona testnet.

After spinning up an instance of the production node, you can run the synchronizer and utilize the JSON-RPC interface.

!!!info
    - Sequencer and prover functionalities are not covered in this document as they are still undergoing development and rigorous testing.
    - Syncing the zkNode currently takes anywhere between 1-2 days depending on various factors. The team is working on snapshots to improve the syncing time.

## Prerequisites

This tutorial requires a [`docker-compose`](https://docs.docker.com/compose/install/) installation.

Run the following to create a directory:

```sh
mkdir -p ~/zkevm-node
```

### Minimum hardware requirements

!!!caution
    - The zkProver does not work on ARM-based Macs yet. 
    - For Windows users, the use of WSL/WSL2 is not recommended.
    - Currently, zkProver optimizations require CPUs that support the AVX2 instruction, which means some non-M1 computers, such as AMD, won't work with the software regardless of the OS.

- 16GB RAM
- 4-core CPU
- ~250/350GB storage (increasing over time)

### Software requirements

- An Ethereum node; Geth or any service providing a JSON RPC interface for accessing the L1 network.
- zkEVM node (or zkNode) for the L2 network.
- Synchronizer which is responsible for synchronizing data between L1 and L2.
- A JSON RPC server which acts as an interface to the L2 network.

## Ethereum node setup

We set up the Ethereum node first as it takes a long time to synchronize.

We recommend using Geth but a Sepolia node is OK too.

Follow the instructions provided in this [guide to setup and install Geth](https://geth.ethereum.org/docs/getting-started/installing-geth).

If you plan to have more than one zkNode in your infrastructure, we advise using a machine that is specifically dedicated to this implementation.

## zkNode setup

Once the L1 installation is complete, we can start the zkNode setup. This is the most straightforward way to run a zkEVM node and it's fine for most use cases. However, if you want to provide service to a large number of users, you should modify the default configuration.

Furthermore, this method is purely subjective and feel free to run this software in a different manner. For example, Docker is not required, you could simply use the Go binaries directly.

Let's start setting up our zkNode:

1. Launch your command line/terminal and set the variables using below commands:

    ```bash
    # define the network("mainnet" or "cardona")
    ZKEVM_NET=cardona

    # define installation path
    ZKEVM_DIR=./path_to_install

    # define your config directory
    ZKEVM_CONFIG_DIR=./path_to_config
    ```

2. Download and extract the artifacts. Note that you may need to [install unzip](https://formulae.brew.sh/formula/unzip) before running this command. 
    
    ```bash
    curl -L https://github.com/0xPolygonHermez/zkevm-node/releases/latest/download/$ZKEVM_NET.zip > $ZKEVM_NET.zip && unzip -o $ZKEVM_NET.zip -d $ZKEVM_DIR && rm $ZKEVM_NET.zip
    ```

3. Copy the `example.env` file with the environment parameters:
    
    ```sh
    cp $ZKEVM_DIR/$ZKEVM_NET/example.env $ZKEVM_CONFIG_DIR/.env
    ```

4. The `example.env` file must be modified according to your configurations.

        Edit the .env file with your favorite editor (we use nano): 
    
        ```sh
        nano $ZKEVM_CONFIG_DIR/.env
        ```

        ```bash
        # ZKEVM_NETWORK = "mainnet" or ZKEVM_NETWORK = "cardona"
        
        # URL of a JSON RPC for Sepolia
        ZKEVM_NODE_ETHERMAN_URL = "http://your.L1node.url"

        # PATH WHERE THE STATEDB POSTGRES CONTAINER WILL STORE PERSISTENT DATA
        ZKEVM_NODE_STATEDB_DATA_DIR = "/path/to/persistent/data/stetedb"

        # PATH WHERE THE POOLDB POSTGRES CONTAINER WILL STORE PERSISTENT DATA
        ZKEVM_NODE_POOLDB_DATA_DIR = "/path/to/persistent/data/pooldb"
        ```

5. To run the zkNode instance, run the following command:

    ```bash
    sudo docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d
    ```

6. Run this command to check if everything went well and all the components are running properly:

    ```bash
    docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml ps
    ```

    You will see a list of the following containers:
      - **zkevm-rpc**
      - **zkevm-sync**
      - **zkevm-state-db**
      - **zkevm-pool-db**
      - **zkevm-prover**

7. You should now be able to run queries to the JSON-RPC endpoint at `http://localhost:8545`.

## Testing

Run the following query to get the most recently synchronized L2 block; if you call it every few seconds, you should see the number grow:

```bash
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}' http://localhost:8545
```

## Stopping the zkNode

Use the below command to stop the zkNode instance:

```bash
sudo docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml down
```

## Updating the zkNode

To update the zkNode software, repeat the setup steps, being careful not to overwrite the configuration files that you have modified.

In other words, instead of running ```cp $ZKEVM_DIR/testnet/example.env $ZKEVM_CONFIG_DIR/.env```, check if the variables of ```$ZKEVM_DIR/testnet/example.env``` have been renamed or there are new ones, and update ```$ZKEVM_CONFIG_DIR/.env``` accordingly.

## Troubleshooting

- It's possible that the machine you're using already uses some of the necessary ports. In this case you can change them directly in `$ZKEVM_DIR/testnet/docker-compose.yml`.

- If one or more containers are crashing, please check the logs using the below command:

    ```bash
    docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs <cointainer_name>
    ```

!!!info "Batch rate"
    - Batches are closed every 10s, or whenever they are full.
    - The frequency of closing batches is subject to change as it depends on the prevailing configurations.
    - The batch rate always needs to be updated accordingly.