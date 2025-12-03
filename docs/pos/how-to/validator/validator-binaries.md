<!--
---
comments: true
---
-->

This guide will walk you through running a Polygon validator node using binaries.

!!! info "Limited spots for new validators"
    
    There is limited space for accepting new validators. New validators can only join the active set when an already active validator unbonds.

## Prerequisites

* Two machines - one sentry and one validator.
* `build-essential` installed on both the sentry and the validator machines.

  To install:

  ```bash
  sudo apt-get install build-essential
  ```
* Go 1.24+ installed on both the sentry and the validator machines.

* RabbitMQ installed on the validator machine.

  Here are the commands to install RabbitMQ:

  ```bash
  sudo apt-get update
  sudo apt install build-essential
  sudo apt install erlang
  wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.10.8/rabbitmq-server_3.10.8-1_all.deb
  sudo dpkg -i rabbitmq-server_3.10.8-1_all.deb
  ```

## Overview

To set up a running validator node, follow these steps in the *exact sequence*:

!!! warning

    Performing these steps out of sequence may lead to configuration issues. It's crucial to note that setting up a sentry node must always *precede* the configuration of the validator node.

1. Prepare two machines, one for the sentry node and one for the validator node.
2. Install the Heimdall and Bor binaries on the sentry and validator machines.
3. Set up the Heimdall and Bor service files on the sentry and validator machines.
4. Configure the sentry node.
5. Start the sentry node.
6. Configure the validator node.
7. Set the owner and signer keys.
8. Start the validator node.

## Installing the binaries

Polygon node consists of 2 layers: Heimdall and Bor.  
Heimdall is a Cosmos-SDK/CometBFT fork that monitors contracts in parallel with the Ethereum network.  
Bor is basically a Geth fork that generates blocks shuffled by Heimdall nodes.

Both binaries must be installed and run in the correct order to function properly.

### Install Heimdall

Install the latest version of Heimdall and related services. Make sure you checkout to the correct [release version](https://github.com/0xPolygon/heimdall-v2/releases).

To install Heimdall, run the following command:

```bash
curl -L https://raw.githubusercontent.com/0xPolygon/install/heimdall-v2/heimdall-v2.sh | bash -s -- <heimdall_version> <network_type> <node_type>
```
You can run the above command with the following options:

- `heimdall_version`: valid v0.2+ release tag from https://github.com/0xPolygon/heimdall-v2/releases
- `network_type`: `mainnet` and `amoy`
- `node_type`: `sentry`

That will install the `heimdalld` binary.  

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

!!! note
    
    Before proceeding, ensure that Heimdall is installed on both the sentry and validator machines.


### Install Bor

Install the latest version of Bor. Make sure you checkout to the correct [release version](https://github.com/0xPolygon/bor/releases).

```bash
curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash -s -- <bor_version> <network_type> <node_type>
```
You can run the above command with the following options:

- `bor_version`: valid v2.0+ release tag from https://github.com/0xPolygon/bor/releases
- `network_type`: `mainnet` and `amoy`
- `node_type`: `sentry`

That will install the `bor` binary. Verify the installation by checking the Bor version on your machine:

```bash
bor version
```

!!! note
    
    Before proceeding, make sure that Bor is installed on both the sentry and validator machines.


### Configure Bor

Open the Bor configuration file for editing using:

```sh
vi /var/lib/bor/config.toml
```

In `config.toml`, add the boot node addresses consisting of a node ID, an IP address, and a port
by adding them under bootnodes in [p2p.discovery] section, shared in the next section.

Now, add the following in the `config.toml` file:

```toml
[p2p]
    [p2p.discovery]
        static-nodes = ["<replace with enode://validator_machine_enodeID@validator_machine_ip:30303>"]
```

To fetch the Node ID of Bor on the validator machine:

- Log in to the validator machine
- Run `bor attach /var/lib/bor/bor.ipc`
- Run `admin.nodeInfo.enode`

!!! info

    PC console is only accessible when Bor is running. To get the enode of the validator node, setup the validator node and then run the above commands.

Finally, save the changes in `config.toml`.

### Seeds and Bootnodes

The latest bor and heimdall seeds can be found [here](https://docs.polygon.technology/pos/reference/seed-and-bootnodes/). Adding them will ensure your node connects to the peers.

### Configuring a firewall

The sentry machine must have the following ports open to the world `0.0.0.0/0`:

* `26656`- Your Heimdall service will connect your node to other nodes Heimdall service.
* `30303`- Your Bor service will connect your node to other nodes Bor service.

## Starting the sentry node

First, start the Heimdall service. Then, once the Heimdall service syncs, start the Bor service.

!!! info "Sync node using snapshots"
    
    The Heimdall service can take several days to sync from scratch fully.

    Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours.
    For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://docs.polygon.technology/pos/how-to/snapshots/).

### Starting the Heimdall service

Start the Heimdall service:

```sh
sudo service heimdalld start
```

Check the Heimdall service logs using the following command:

```sh
journalctl -u heimdalld.service -f
```

!!! bug "Common error"
    
    In the logs, you may see the following errors:

    * `Stopping peer for error`
    * `MConnection flush failed`
    * `use of closed network connection`

    These logs mean that one of the nodes on the network refused a connection to your node.

    Wait for your node to crawl more nodes on the network; you do not need to do anything manually to address these errors.

Check the sync status of Heimdall using the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` signifies the following:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is fully synced.

Wait for the Heimdall service to sync fully.

### Starting the Bor service

Once the Heimdall service is fully synced, start the Bor service.

Start the Bor service:

```sh
sudo service bor start
```

Check the Bor service logs:

```sh
journalctl -u bor.service -f
```

## Configuring the validator node

!!! info
    
    In order to proceed, you'll need to have access to an RPC endpoint of a fully synced Ethereum mainnet node ready.

### Configuring the Bor service

Open config file for editing using: `vi /var/lib/bor/config.toml`

Change the value of `static-nodes` parameter as follows:

```json
static-nodes = ["<replace with enode://sentry_machine_enodeID@sentry_machine_ip:30303>"]
// the node ID and IP address of Bor set up on the sentry machine
```

To get the Node ID of Bor on the sentry machine:

1. Log in to the sentry machine.
2. Run `bor attach /var/lib/bor/bor.ipc`.
3. Run `admin.nodeInfo.enode`.

## Setting the Owner and Signer Key

On Polygon PoS, it is recommended that you keep the owner and signer keys different.

* Signer: The address that signs the checkpoint transactions. It is advisable to keep at least 1 ETH on the signer address.
* Owner: The address that is used to perform the staking transactions. It is advisable to keep the POL tokens on the owner address.

### Generating a Heimdall private key

You must generate a Heimdall private key only on the validator machine. Do not generate a Heimdall
private key on the sentry machine.

To generate the private key, run:

```sh
heimdalld generate-validator-key ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet’s private key.

This will generate `priv_validator_key.json`. Move the generated JSON file to the Heimdall configuration directory using the following command:

```sh
mv ./priv_validator_key.json  /var/lib/heimdall/config
```

### Generating a Bor keystore file

You must generate a Bor keystore file only on the validator machine. Do not generate a Bor keystore file on the sentry machine.

To generate the private key, run:

```sh
heimdalld generate-keystore ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet’s private key.

When prompted, set up a password to the keystore file.

This will generate a `UTC-<time>-<address>` keystore file.

Move the generated keystore file to the Bor configuration directory using the following command:

```sh
mv ./UTC-<time>-<address> /var/lib/bor/data/keystore
```

### Add `password.txt`

Make sure to create a `password.txt` file, then add the Bor keystore file password in the
`/var/lib/bor/password.txt` file.

### Add your Ethereum address

Open `config.toml` for editing: `vi /var/lib/bor/config.toml`.

```toml
[miner]
  mine = true
  etherbase = "validator address"

[accounts]
  unlock = ["validator address"]
  password = "The path of the file you entered in password.txt"
  allow-insecure-unlock = true
```

!!! info "Set file permissions"
    
    Please ensure that `priv_validator_key.json` & `UTC-<time>-<address>` files have relevant permissions. 
    
    To set the permissions for `priv_validator_key.json`, run: 
    ```bash
    sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key.json
    ```
    and similarly, for the `UTC-<time>-<address>` file, run:
    ```bash
    sudo chown -R heimdall:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>
    ```

## Starting the Heimdall service

You will now start the Heimdall service on the validator machine. Once the Heimdall service syncs, you will start the Bor service on the validator machine.

Start the Heimdall service using the following command:

```sh
sudo service heimdalld start
```

!!! info

    The rest service and the bridge starts along with heimdall.

Check the Heimdall service logs using the following command:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall using the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` signifies the following:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is synced.

Wait for the Heimdall service to fully sync.

## Starting the Bor service

Once the Heimdall service on the validator machine is fully synced, start the Bor service on the validator machine.

Start the Bor service using the following command:

```sh
sudo service bor start
```

Check the Bor service logs using the following command:

```sh
journalctl -u bor.service -f
```
