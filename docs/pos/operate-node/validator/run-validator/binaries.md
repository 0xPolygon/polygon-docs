
This guide will walk you through running a Polygon validator node from packages.

For system requirements,
follow the [Validator Node System Requirements](/pos/validator/validator-node-system-requirements.md) guide.

!!!tip Snapshots
    Steps in this guide involve waiting for the **Heimdall** and **Bor** services to fully sync.
    This process takes several days to complete. Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours. For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](/pos/how-to/snapshots.md).

    For snapshot download links, see [<ins>Polygon Chains Snapshots</ins>](https://snapshot.polygon.technology/).


## Port configuration details
    
Here are a few instructions on how to configure ports for sentry and validator nodes.

### For sentry nodes

  - **Port 22**: Opening this to the public is not a good idea as the default SSH port 22 is prone to attacks. It is better to secure it by allowing it only in a closed network (VPN).

  - **Port 30303**: To be opened to the public for Bor p2p discovery.

  - **Port 26656**: To be opened to the public for Heimdall/Tendermint p2p discovery.
  
  - **Port 26660**: Prometheus port for Tendermint/Heimdall. Not required to be opened to the public. Only allow for the monitoring systems (Prometheus/Datadog).

  - **Port 7071**: Metric port for Bor. Only needs to be opened for the Monitoring system.

  - **Ports 8545, 8546, 1317**: Can be opened for Bor HTTP RPC, Bor WS RPC, and Heimdall API respectively; but only if really necessary.


### For validator nodes

  - **Port 22**: Opening this to the public is not a good idea as the default SSH port 22 is prone to attacks. It is better to secure it by allowing it only in a closed network (VPN).

  - **Port 30303**: To be opened to only Sentry to which the validator is connected for Bor p2p discovery.

  - **Port 26656**: To be opened to only Sentry to which the validator is connected for Heimdall/Tendermint p2p discovery.

  - **Port 26660**: Prometheus port for Tendermint/Heimdall. Not required to be opened to the public. Only allow for the monitoring systems (Prometheus/Datadog).

  - **Port 7071**: Metric port for Bor. Only needs to be opened for the monitoring system.


This guide will walk you through running a Polygon validator node from binaries.

For system requirements, follow the [Validator Node System Requirements](/pos/validator/validator-node-system-requirements.md) guide.

!!!caution
    
    There is limited space for accepting new validators. New validators can only join the active set when an already active validator unbonds.


## Prerequisites

* Two machines — one sentry and one validator.
* `build-essential` installed on both the sentry and the validator machines.

  To install:

  ```sh
  sudo apt-get install build-essential
  ```

* Go 1.19 installed on both the sentry and the validator machines.

  To install:

  ```sh
  wget https://raw.githubusercontent.com/maticnetwork/node-ansible/master/go-install.sh
  bash go-install.sh
  sudo ln -nfs ~/.go/bin/go /usr/bin/go
  ```

* RabbitMQ installed on both the sentry and the validator machines.

  Here are the commands to install RabbitMQ:

  ```sh
  sudo apt-get update
  sudo apt install build-essential
  sudo apt install erlang
  wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.10.8/rabbitmq-server_3.10.8-1_all.deb
  sudo dpkg -i rabbitmq-server_3.10.8-1_all.deb
  ```

  
!!!tip
    Check more information about downloading and installing RabbitMQ [<ins>here</ins>](https://www.rabbitmq.com/download.html).



## Overview

To get to a running validator node, conduct the following in this **exact sequence of steps**:

!!!caution
    
    You will run into configuration issues if these steps are performed out of sequence.
    It is important to keep in mind that a sentry node must always be set up before the validator node.



1. Prepare two machines, one for the sentry node and one for the validator node.
2. Install the Heimdall and Bor binaries on the sentry and validator machines.
3. Set up the Heimdall and Bor service files on the sentry and validator machines.
4. Set up the Heimdall and Bor services on the sentry and validator machines.
5. Configure the sentry node.
6. Start the sentry node.
7. Configure the validator node.
8. Set the owner and signer keys.
9. Start the validator node.
10. Check node health with the community.

## Installing the Binaries

Polygon node consists of 2 layers: Heimdall and Bor. Heimdall is a tendermint fork that monitors contracts in parallel with the Ethereum network. Bor is basically a Geth fork that generates blocks shuffled by Heimdall nodes.

Both binaries must be installed and run in the correct order to function properly.

### Heimdall

Install the latest version of Heimdall and related services. Make sure you checkout to the correct [release version](https://github.com/maticnetwork/heimdall/releases). Note that the latest version, [Heimdall v1.0.3](https://github.com/maticnetwork/heimdall/releases/tag/v1.0.3), contains enhancements such as:
1. Restricting data size in state sync txs to:
    * **30Kb** when represented in **bytes**
    * **60Kb** when represented as **string**
2. Increasing the **delay time** between the contract events of different validators to ensure that the mempool doesn't get filled very quickly in case of a burst of events which can hamper the progress of the chain.

The following example shows how the data size is restricted:

```
Data - "abcd1234"
Length in string format - 8
Hex Byte representation - [171 205 18 52]
Length in byte format - 4
```

To install **Heimdall**, run the below commands:

```bash
curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <heimdall_version> <network_type> <node_type>
```

**heimdall_version**: `valid v1.0+ release tag from https://github.com/maticnetwork/heimdall/releases`
**network_type**: `mainnet` and `mumbai`
**node_type**: `sentry`

That will install the `heimdalld` and `heimdallcli` binaries. Verify the installation by checking the Heimdall version on your machine:

```bash
heimdalld version --long
```

!!!note
    
    Before proceeding, Heimdall should be installed on both the sentry and validator machines.


### Installing Bor

Install the latest version of Bor, based on valid v1.0+ [released version](https://github.com/maticnetwork/bor/releases).

```bash
curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- <bor_version> <network_type> <node_type>
```

**bor_version**: `valid v1.0+ release tag from https://github.com/maticnetwork/bor/releases`
**network_type**: `mainnet` and `mumbai`
**node_type**: `sentry`

That will install the `bor` binary. Verify the installation by checking the Bor version on your machine:

```bash
bor version
```

!!!note
    
    Before proceeding, Bor should be installed on both the sentry and validator machines.


## Configuring the Sentry Node

Start by logging in to the remote sentry machine.

### Configuring the Heimdall services

Open the Heimdall configuration file for editing:

```sh
vi /var/lib/heimdall/config/config.toml
```

In `config.toml`, change the following parameters:

* `moniker` — any name. Example: `moniker = "my-sentry-node"`.
* `seeds` — the seed node addresses consisting of a node ID, an IP address, and a port.

  Use the following values:

  ```toml
  seeds="1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"
  ```

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

Save the changes in `config.toml`.

### Configuring the Bor Service

Open the Bor configuration file for editing:

```sh
vi /var/lib/bor/config.toml
```

In `config.toml`, add the boot node addresses consisting of a node ID, an IP address, and a port
by adding them under bootnodes in [p2p.discovery] section:

```config
--bootnodes "enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"
```

Save the changes in `start.sh`.

### Configuring a firewall

The sentry machine must have the following ports open to the world `0.0.0.0/0`:

* `26656`- Your Heimdall service will connect your node to other nodes Heimdall service.

* `30303`- Your Bor service will connect your node to other nodes Bor service.

## Starting the Sentry Node

You will first start the Heimdall service. Once the Heimdall service syncs, you will start the Bor service.

!!!note
    
    As mentioned earlier, the Heimdall service takes several days to sync from scratch fully.

    Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours.
    For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://forum.polygon.technology/t/snapshot-instructions-for-heimdall-and-bor/9233).

    For snapshot download links, see [Polygon Chains Snapshots](https://snapshot.polygon.technology/).


### Starting the Heimdall service

Start the Heimdall service:

```sh
sudo service heimdalld start
```
!!!note
    The heimdall-rest service starts along with heimdall.

    Check the Heimdall service logs:

    ```sh
    journalctl -u heimdalld.service -f
    ```

!!!note
    
    In the logs, you may see the following errors:

    * `Stopping peer for error`
    * `MConnection flush failed`
    * `use of closed network connection`

    These logs mean that one of the nodes on the network refused a connection to your node.

    Wait for your node to crawl more nodes on the network; you do not need to do anything to address these errors.


Check the sync status of Heimdall:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value is:

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is fully synced.

Wait for the Heimdall service to sync fully.

### Starting the Bor service

Once the Heimdall service syncs, start the Bor service.

Start the Bor service:

```sh
sudo service bor start
```

Check the Bor service logs:

```sh
journalctl -u bor.service -f
```

## Configuring the Validator Node

!!!note
    
    To complete this section, you must have an RPC endpoint of your fully synced Ethereum mainnet node ready.


### Configuring the Heimdall service

Log in to the remote validator machine.

Open for editing `vi /var/lib/heimdall/config/config.toml`.

In `config.toml`, change the following:

* `moniker` — any name. Example: `moniker = "my-validator-node"`.
* `pex` — set the value to `false` to disable the peer exchange. Example: `pex = false`.
* `private_peer_ids` — comment out the value to disable it. Example: `# private_peer_ids = ""`.

  To get the node ID of Heimdall on the sentry machine:

  1. Log in to the sentry machine.
  1. Run `heimdalld tendermint show-node-id`.

Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.

Save the changes in `config.toml`.

Open for editing `vi /var/lib/heimdall/config/heimdall-config.toml`.

In `heimdall-config.toml`, change the following:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node,
  i.e Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

Save the changes in `heimdall-config.toml`.

### Configuring the Bor service

Open config file for editing using: `vi /var/lib/bor/config.toml`

Change the value of static-nodes parameter as follows:

```json
static-nodes = ["<replace with enode://sentry_machine_enodeID@sentry_machine_ip:30303>"]
// the node ID and IP address of Bor set up on the sentry machine
```

To get the Node ID of Bor on the sentry machine:

- Log in to the sentry machine
- Run `cat /var/lib/bor/data/bor/nodekey`

## Setting the Owner and Signer Key

On Polygon, it is recommended that you keep the owner and signer keys different.

* Signer — the address that signs the checkpoint transactions. The recommendation is to keep at least 1 ETH on the signer address.
* Owner — the address that does the staking transactions. The recommendation is to keep the MATIC tokens on the owner address.

### Generating a Heimdall private key

You must generate a Heimdall private key only on the validator machine. Do not generate a Heimdall
private key on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-validatorkey ETHEREUM_PRIVATE_KEY
```

where

* ETHEREUM_PRIVATE_KEY — your Ethereum wallet’s private key.

This will generate `priv_validator_key.json`. Move the generated JSON file to the Heimdall configuration
directory:

```sh
mv ./priv_validator_key.json  /var/lib/heimdall/config
```

### Generating a Bor keystore file

You must generate a Bor keystore file only on the validator machine. Do not generate a Bor keystore file
on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-keystore ETHEREUM_PRIVATE_KEY
```

where

* ETHEREUM_PRIVATE_KEY — your Ethereum wallet’s private key.

When prompted, set up a password to the keystore file.

This will generate a `UTC-<time>-<address>` keystore file.

Move the generated keystore file to the Bor configuration directory:

```sh
mv ./UTC-<time>-<address> /var/lib/bor/data/keystore
```

### Add password.txt

Make sure to create a `password.txt` file, then add the Bor keystore file password right in the
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

!!!caution
    
    Please ensure that `priv_validator_key.json` & `UTC-<time>-<address>` files have relevant permissions. To set relevant permissions for `priv_validator_key.json`, run `sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key.json` and similarly `sudo chown -R heimdall:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>` for `UTC-<time>-<address>`.

## Starting the Validator Node

At this point, you must have:

* The Heimdall service on the sentry machine syncs and is running.
* The Bor service on the sentry machine running.
* The Heimdall service and the Bor service on the validator machine configured.
* Your owner and signer keys configured.

### Starting the Heimdall service

You will now start the Heimdall service on the validator machine. Once the Heimdall service syncs, you
will start the Bor service on the validator machine.

Start the Heimdall service:

```sh
sudo service heimdalld start
```

!!!note
    The heimdall-rest service and heimdall-bridge starts along with heimdall.

    Check the Heimdall service logs:

    ```sh
    journalctl -u heimdalld.service -f
    ```

    Check the sync status of Heimdall:

    ```sh
    curl localhost:26657/status
    ```


In the output, the `catching_up` value is:

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is synced.

Wait for the Heimdall service to fully sync.

### Starting the Bor service

Once the Heimdall service on the validator machine syncs, start the Bor service on
the validator machine.

Start the Bor service:

```sh
sudo service bor start
```

Check the Bor service logs:

```sh
journalctl -u bor.service -f
```

### Seed nodes and bootnodes

- Heimdall seed nodes:

  ```bash
  moniker=<enter unique identifier>

  # Mainnet:
  seeds="1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"

  # Testnet:
  seeds="9df7ae4bf9b996c0e3436ed4cd3050dbc5742a28@43.200.206.40:26656,d9275750bc877b0276c374307f0fd7eae1d71e35@54.216.248.9:26656,1a3258eb2b69b235d4749cf9266a94567d6c0199@52.214.83.78:26656"
  ```
- Bootnodes:

  ```bash
  # Mainnet:
  bootnode ["enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"]

  # Testnet:
  bootnodes ["enode://bdcd4786a616a853b8a041f53496d853c68d99d54ff305615cd91c03cd56895e0a7f6e9f35dbf89131044e2114a9a782b792b5661e3aff07faf125a98606a071@43.200.206.40:30303", "enode://209aaf7ed549cf4a5700fd833da25413f80a1248bd3aa7fe2a87203e3f7b236dd729579e5c8df61c97bf508281bae4969d6de76a7393bcbd04a0af70270333b3@54.216.248.9:30303"]
  ```


## Health Checks with the Community

Now that your sentry and validator nodes are in sync and running, head over to
[Discord](https://discord.com/invite/0xPolygon) and ask the community to health-check your nodes.

!!!note
    
    As validators, it’s mandatory to always have a check of the signer address. If the ETH balance reaches below 0.5 ETH then it should be refilled. Avoiding this will push out nodes from submitting checkpoint transactions.


## Next Steps: Staking

Now that you have your sentry and validator nodes are health-checked, proceed to
the [Staking](/how-to/operating/validator-node/staking.md) guide to start backing the network.
