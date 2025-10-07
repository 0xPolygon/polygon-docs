<!--
---
comments: true
---
-->

This guide covers running a validator node through packages.

## Prerequisites

* Two machines — one sentry and one validator.
* Bash installed on both the sentry and the validator machines.
* RabbitMQ installed on the validator machine.
  See [Downloading and Installing RabbitMQ](https://www.rabbitmq.com/download.html).

## Overview

To spin up a functioning validator node, follow these steps in the *specified sequence*:

!!! warning

    Performing these steps out of sequence may lead to configuration issues. It's crucial to note that setting up a sentry node must always *precede* the configuration of the validator node.

1. Prepare two machines, one for the sentry node and one for the validator node.
2. Install the Heimdall and Bor binaries on the sentry and validator machines.
3. Set up the Heimdall and Bor services on the sentry and validator machines.
4. Configure the sentry node.
5. Start the sentry node.
6. Configure the validator node.
7. Set the owner and signer keys.
8. Start the validator node.

## Installing packages

### Heimdall

Install the default latest version of sentry and validator for the PoS mainnet/Amoy testnet:

```shell
curl -L https://raw.githubusercontent.com/0xPolygon/install/heimdall-v2/heimdall-v2.sh | bash -s -- <version> <network> <node_type>
```

or install a specific version, node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions can be found on
    [Heimdall GitHub repository](https://github.com/0xPolygon/heimdall-v2/releases).

```shell
  # Example:
  curl -L https://raw.githubusercontent.com/0xPolygon/install/heimdall-v2/heimdall-v2.sh | bash -s -- v0.2.16 mainnet sentry
```

### Bor

Install the default latest version of sentry and validator for the PoS mainnet/Amoy testnet:

```shell
curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash
```

or install a specific version, node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions could be found on [Bor Github repository](https://github.com/0xPolygon/bor/releases).

```shell
# structure
curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash -s -- <version> <network> <node_type>

# Example:
curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash -s -- v2.0.0 mainnet sentry
```

### Check installation

Check Bor installation using the following command:

```shell
bor version
```

!!! info
    
    Before proceeding, please ensure Bor is installed on both the sentry and validator machines.

## Configure sentry node

In this section, we will go through steps to initialize and customize configuration for sentry nodes.

### Configure Heimdall

Edit the configuration files under `/var/lib/heimdall/config`  
The templates for each supported network are available [here](https://github.com/0xPolygon/heimdall-v2/tree/develop/packaging/templates/config)  
Download the `genesis.json` file and place it under `/var/lib/heimdall/config/`
Use the following commands based on your target network:
```bash
cd /var/lib/heimdall/config
curl -fsSL <BUCKET_URL> -o genesis.json
```

Where `BUCKET_URL` is

- https://storage.googleapis.com/amoy-heimdallv2-genesis/migrated_dump-genesis.json for amoy
- https://storage.googleapis.com/mainnet-heimdallv2-genesis/migrated_dump-genesis.json for mainnet

To get the node ID of Heimdall on the validator machine:

1. Log in to the validator machine.
2. Run:
  ```sh
  heimdalld comet show-node-id
  ```

Example: `private_peer_ids = "0ee1de0515f577700a6a4b6ad882eff1eb15f066"`.

Finally, save the changes in `config.toml`.

Check Heimdall installation using the following command:

```shell
heimdalld version
```

It should return the version of Heimdall you installed.  

### Configure Bor

In `/var/lib/bor/config.toml` file, add the following:

```bash
[p2p]
    [p2p.discovery]
        static-nodes = ["<replace with enode://validator_machine_enodeID@validator_machine_ip:30303>"]
```

To get the Node ID of Bor on the validator machine:

1. Log into the validator machine.
2. Run `bor attach /var/lib/bor/bor.ipc`
3. Run `admin.nodeInfo.enode`

!!! info

    The IPC console is only accessible when Bor is running. To get the enode of the validator node, setup the validator node, and then run the above commands.

Example content of static node field in `/var/lib/bor/config.toml`:

```bash
[p2p]
    [p2p.discovery]
        static-nodes = ["enode://410e359736bcd3a58181cf55d54d4e0bbd6db2939c5f548426be7d18b8fd755a0ceb730fe5cf7510c6fa6f0870e388277c5f4c717af66d53c440feedffb29b4b@134.209.100.175:30303"]
```

Finally, save the changes in `/var/lib/bor/config.toml`.

### Seeds and Bootnodes

The latest bor and heimdall seeds can be found [here](https://docs.polygon.technology/pos/reference/seed-and-bootnodes/). Adding them will ensure your node connects to the peers.

### Configuring a firewall

The sentry machine must have the following ports open to the public internet `0.0.0.0/0`:

* Port `26656`: Your Heimdall service will connect your node to other nodes Heimdall service.
* Port `30303`: Your Bor service will connect your node to other nodes Bor service.
* Port `22`: Open this port if your node is servicing validators. You will likely want to restrict what traffic can access this port as it is a sensitive port.

## Starting the sentry node

First, start the Heimdall service. Once the Heimdall service is fully synced, you can start the Bor service.

### Reload service files

Run the following command to reload service files to make sure all changes to service files are loaded correctly:

```sh
sudo systemctl daemon-reload
```

### Starting the Heimdall service

Start the Heimdall services using the following command:

```sh
sudo service heimdalld start
```

Check the Heimdall service logs using the following command:

```sh
journalctl -u heimdalld.service -f
```

!!! bug "Common errors"
     
    In the logs, you may see the following errors:

    * `Stopping peer for error`
    * `MConnection flush failed`
    * `use of closed network connection`

    These logs mean that one of the nodes on the network refused a connection to your node.
    Wait for your node to crawl more nodes on the network; you do not need to do anything to address these errors.

Check the `Heimdalld` logs using the following command:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall using the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value signifies the following:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is fully synced.

Wait for the Heimdall service to sync fully.

### Starting the Bor service

Once the Heimdall service is fully synced, start the Bor service using the following command:

```sh
sudo service bor start
```

Check the Bor service logs using the following command:

```sh
journalctl -u bor.service -f
```

## Installing packages on the validator node

Follow the same [installation steps](#installing-packages) on the validator node.

## Configuring the validator node

!!! note
    
    To complete this section, you must have an RPC endpoint of your fully synced Ethereum mainnet node ready.

### Configure Heimdall

Log in to the remote validator machine.

Then, edit the configuration files under `/var/lib/heimdall/config`  
The templates for each supported network are available [here](https://github.com/0xPolygon/heimdall-v2/tree/develop/packaging/templates/config)  
Download the `genesis.json` file and place it under `/var/lib/heimdall/config/`
Use the following commands based on your target network:
```bash
cd /var/lib/heimdall/config
curl -fsSL <BUCKET_URL> -o genesis.json
```

Where `BUCKET_URL` is

- https://storage.googleapis.com/amoy-heimdallv2-genesis/migrated_dump-genesis.json for amoy
- https://storage.googleapis.com/mainnet-heimdallv2-genesis/migrated_dump-genesis.json for mainnet

Verify the installation by checking the Heimdall version on your machine:

```bash
heimdalld version
```

It should return the version of Heimdall you installed.

To get the node ID of Heimdall on the sentry machine:

1. Log in to the sentry machine.
2. Run `heimdalld comet show-node-id`.

Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

Save the changes in `config.toml`.

Open the `app.toml` file for editing by running: `vi /var/lib/heimdall/config/app.toml`.

In config file, update the following parameters:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node or testnet node,
  e.g., Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

* [Optional] Post [Rio hardfork](https://github.com/0xPolygon/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-73.md), which enables [VeBlop architecture](https://github.com/0xPolygon/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-64.md), validators are able to elect block producers through heimdall config flag `producer_votes`, whose default validator`"91,92,93"`. Change this value if needed, e.g. `producer_votes="91,92,93"`.

Finally, save the changes in `app.toml`.

### Configuring Bor

In the `/var/lib/bor/config.toml` file, add the following:

```bash
[p2p]
    [p2p.discovery]
        static-nodes = ["<replace with enode://validator_machine_enodeID@validator_machine_ip:30303>"]
```

To get the node ID of Bor on the sentry machine, run the following command:

1. Log into the sentry machine.
2. Run `bor attach /var/lib/bor/bor.ipc`
3. Run `admin.nodeInfo.enode`

!!! info

    The IPC console is only accessible when Bor is running.

Example content of `static-nodes` field in `/var/lib/bor/config.toml`:
```bash
[p2p]
    [p2p.discovery]
        static-nodes = ["enode://410e359736bcd3a58181cf55d54d4e0bbd6db2939c5f548426be7d18b8fd755a0ceb730fe5cf7510c6fa6f0870e388277c5f4c717af66d53c440feedffb29b4b@134.209.100.175:30303"]
```

Finally, save the changes in `/var/lib/bor/config.toml`.

## Setting the Owner and Signer Key

On Polygon PoS, it is recommended that you keep the owner and signer keys different.

* Signer: The address that signs the checkpoint transaction. It is advisable to keep at least 1 ETH on the signer address.
* Owner: The address that does the staking transactions. It is advisable to keep the POL tokens on the owner address.

### Generating a Heimdall private key

You must generate a Heimdall private key only on the validator machine. Do not generate a Heimdall
private key on the sentry machine.

To generate the private key, run:

```sh
heimdalld generate-validator-key ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet's private key.

This will generate `priv_validator_key.json`. Move the generated JSON file to the Heimdall configuration directory:

```sh
mv ./priv_validator_key.json /var/lib/heimdall/config
```

### Generating a Bor keystore file

!!! warning
    You must generate a Bor keystore file only on the validator machine. Do not generate a Bor keystore file on the sentry machine.

To generate the private key, run:

```sh
heimdalld generate-keystore ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet's private key.

When prompted, set up a password to the keystore file.

This will generate a `UTC-<time>-<address>` keystore file.

Move the generated keystore file to the Bor configuration directory using the following command:

```sh
mv ./UTC-<time>-<address> /var/lib/bor/data/keystore
```

### Add `password.txt`

Make sure to create a `password.txt` file then add the Bor keystore file password right in the
`/var/lib/bor/password.txt` file.

### Add your Ethereum address

Open config file for editing by running: `vi /var/lib/bor/config.toml`.

```toml
[miner]
  mine = true
  etherbase = "validator address"

[accounts]
  unlock = ["validator address"]
  password = "The path of the file you entered in password.txt"
  allow-insecure-unlock = true
```

!!! warning
    
    Please ensure that `priv_validator_key.json` & `UTC-<time>-<address>` files have relevant permissions. To set relevant permissions for `priv_validator_key.json`, run the following command: 
    ```bash
    sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key.json
    ``` 
    
    And similarly, run the following command to set permissions for `UTC-<time>-<address>`: 
    ```bash
    sudo chown -R bor:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>
    ```

## Starting the validator node

At this point, you must have:

* The Heimdall service on the sentry machine syncs and is running.
* The Bor service on the sentry machine running.
* The Heimdall service and the Bor service on the validator machine configured.
* Your owner and signer keys configured.

### Reload service files

Run the following command to reload the service files to make sure all changes to service files are loaded correctly:

```bash
sudo systemctl daemon-reload
```

### Starting the Heimdall service

Now, start the Heimdall service on the validator machine. Once the Heimdall service is fully synced, you can start the Bor service on the validator machine.

!!! info
    
    In order to ensure you node is able to submit checkpoints normally, make sure that the `-- bridge -- all`  flag is present correctly in `/lib/systemd/system/heimdalld.service` file.


Start the Heimdall services by running the following command:

```sh
sudo service heimdalld start
```

Check the Heimdall service logs by running the following command:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall by running the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value signifies the following:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is synced.

Wait for the Heimdall service to fully sync.

### Starting the Bor service

Once the Heimdall service on the validator machine is fully synced, start the Bor service on
the validator machine.

Start the Bor service by running the following command:

```sh
sudo service bor start
```

Check the Bor service logs using the following command:

```sh
journalctl -u bor.service -f
```
