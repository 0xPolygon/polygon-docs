---
comments: true
---

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

* Go 1.19 installed on both the sentry and the validator machines.

  To install:

  ```bash
  wget https://raw.githubusercontent.com/maticnetwork/node-ansible/master/go-install.sh
  bash go-install.sh
  sudo ln -nfs ~/.go/bin/go /usr/bin/go
  ```

* RabbitMQ installed on both the sentry and the validator machines.

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

Polygon node consists of 2 layers: Heimdall and Bor. Heimdall is a tendermint fork that monitors contracts in parallel with the Ethereum network. Bor is basically a Geth fork that generates blocks shuffled by Heimdall nodes.

Both binaries must be installed and run in the correct order to function properly.

### Install Heimdall

Install the latest version of Heimdall and related services. Make sure you checkout to the correct [release version](https://github.com/maticnetwork/heimdall/releases).

To install Heimdall, run the following commands:

```bash
curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <heimdall_version> <network_type> <node_type>
```
You can run the above command with following options:

- `heimdall_version`: valid v1.0+ release tag from https://github.com/maticnetwork/heimdall/releases
- `network_type`: `mainnet` and `amoy`
- `node_type`: `sentry`

That will install the `heimdalld` and `heimdallcli` binaries. Verify the installation by checking the Heimdall version on your machine using the following command:

```bash
heimdalld version --long
```

!!! note
    
    Before proceeding, ensure that Heimdall is installed on both the sentry and validator machines.


### Install Bor

Install the latest version of Bor. Make sure you checkout to the correct [release version](https://github.com/maticnetwork/bor/releases).

```bash
curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- <bor_version> <network_type> <node_type>
```
You can run the above command with following options:

- `bor_version`: valid v1.0+ release tag from https://github.com/maticnetwork/bor/releases
- `network_type`: `mainnet` and `amoy`
- `node_type`: `sentry`

That will install the `bor` binary. Verify the installation by checking the Bor version on your machine:

```bash
bor version
```

!!! note
    
    Before proceeding, make sure that Bor is installed on both the sentry and validator machines.


## Configuring the sentry node

Start by logging in to the remote sentry machine.

### Configure Heimdall

Open the Heimdall configuration file for editing:

```sh
vi /var/lib/heimdall/config/config.toml
```

In `config.toml`, change the following parameters:

* `moniker` — any name. Example: `moniker = "my-sentry-node"`.
* `seeds` — the seed node addresses consisting of a node ID, an IP address, and a port.

Use the following values for mainnet:

```toml
seeds="1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"
```

!!! info "Amoy node seeds"

    The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

* `pex` — set the value to `true` to enable the peer exchange. Example: `pex = true`.
* `private_peer_ids` — the node ID of Heimdall set up on the validator machine.

To get the node ID of Heimdall on the validator machine:

1. Log in to the validator machine.
2. Run:

  ```sh
  heimdalld tendermint show-node-id
  ```

Example: `private_peer_ids = "0ee1de0515f577700a6a4b6ad882eff1eb15f066"`.

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.
* `max_open_connections` — set the value to `100`. Example: `max_open_connections = 100`.

Finally, save the changes in `config.toml`.

### Configure Bor

Open the Bor configuration file for editing using:

```sh
vi /var/lib/bor/config.toml
```

In `config.toml`, add the boot node addresses consisting of a node ID, an IP address, and a port
by adding them under bootnodes in [p2p.discovery] section:

```config
--bootnodes "enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"
```

!!! info "Amoy node seeds"

    The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

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

### Configuring a firewall

The sentry machine must have the following ports open to the world `0.0.0.0/0`:

* `26656`- Your Heimdall service will connect your node to other nodes Heimdall service.
* `30303`- Your Bor service will connect your node to other nodes Bor service.

## Starting the sentry node

First, start the Heimdall service. Then, once the Heimdall service syncs, start the Bor service.

!!! info "Sync node using snapshots"
    
    The Heimdall service can take several days to sync from scratch fully.

    Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours.
    For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://forum.polygon.technology/t/snapshot-instructions-for-heimdall-and-bor/9233).

### Starting the Heimdall service

Start the Heimdall service:

```sh
sudo service heimdalld start
```
!!! info
    The `heimdall-rest` service starts along with heimdall.

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

### Configuring the Heimdall service

Log in to the remote validator machine.

Open for editing `vi /var/lib/heimdall/config/config.toml`.

In `config.toml`, change the following:

* `moniker` — any name. Example: `moniker = "my-validator-node"`.
* `pex` — set the value to `false` to disable the peer exchange. Example: `pex = false`.
* `private_peer_ids` — comment out the value to disable it. Example: `# private_peer_ids = ""`.

To get the node ID of Heimdall on the sentry machine:

1. Log in to the sentry machine.
2. Run `heimdalld tendermint show-node-id`.

Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.

Save the changes in `config.toml`.

Open for editing `vi /var/lib/heimdall/config/heimdall-config.toml`.

In `heimdall-config.toml`, update the following:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node,
  e.g., Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

Save the changes in `heimdall-config.toml`.

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
heimdallcli generate-validatorkey ETHEREUM_PRIVATE_KEY
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
heimdallcli generate-keystore ETHEREUM_PRIVATE_KEY
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

    The `heimdall-rest` service and `heimdall-bridge` starts along with heimdall.

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