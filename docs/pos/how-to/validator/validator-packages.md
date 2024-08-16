---
comments: true
---

## Prerequisites

* Two machines — one sentry and one validator.

* Bash is installed on both the sentry and the validator machines.

* RabbitMQ installed on both the sentry and the validator machines.
  See [Downloading and Installing RabbitMQ](https://www.rabbitmq.com/download.html).

## Overview

To spin up a functioning validator node, follow these steps in the *specified sequence*:

!!! warning
    
    Please ensure you strictly adhere to the outlined sequence of actions to avoid encountering issues. For instance, it's imperative to set up a sentry node before configuring the validator node.


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

## Installing package

### Heimdall

- Install the default latest version of sentry for the Polygon mainnet:

    ```shell
    curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash
    ```

    or install a specific version, node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions can be found on
    [Heimdall GitHub repository](https://github.com/maticnetwork/heimdall/releases).

    ```shell
    curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <version> <network> <node_type>
    # Example:
    # curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- v1.0.3 mainnet sentry
    ```

### Bor

- Install the default latest version of sentry for mainnet:

    ```shell
    curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash
    ```

    or install a specific version,  node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions could be found on
    [Bor Github repository](https://github.com/maticnetwork/bor/releases).

    ```shell
    curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- <version> <network> <node_type>

    # Example:
    # curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- v1.1.0 mainnet sentry
    ```

### Check installation

- Check Heimdall installation

    ```shell
    heimdalld version --long
    ```

- Check Bor installation

    ```shell
    bor version
    ```

!!! note
    
    Before proceeding, Bor should be installed on both the sentry and validator machines.

## Configuration

In this section, we will go through steps to initialize and customize configurations nodes.

!!! warning
    
    Bor v1.1.0 and Heimdall v1.0.3 use standardized paths for configuration files and chain data. If you have existing config files and chain data on your node, please skip this section and refer to the [migration](https://www.notion.so/polygontechnology/Bor-Heimdall-Mainnet-Upgrade-v0-3-0-6575b2672a1d4ecc8cea8e1703bcc2df) guide to learn about migrating configs and data to standardized file locations. This is not relevant for new validators.


### Configure Heimdall

- Initialize Heimdall configs using:

```shell
# For mainnet
sudo -u heimdall heimdalld init --chain=mainnet --home /var/lib/heimdall

# For testnet
sudo -u heimdall heimdalld init --chain=amoy --home /var/lib/heimdall
```

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

### Configure Bor

In `/var/lib/bor/config.toml`, add the following:

```
[p2p]
    [p2p.discovery]
        static-nodes = ["<replace with enode://validator_machine_enodeID@validator_machine_ip:30303>"]
```

To get the Node ID of Bor on the validator machine:

1. Log into the validator machine.
2. Run `bor bootnode -node-key /var/lib/bor/data/bor/nodekey -dry-run`.

Example content of static node field in `/var/lib/bor/config.toml`:

```
[p2p]
    [p2p.discovery]
        static-nodes = ["enode://410e359736bcd3a58181cf55d54d4e0bbd6db2939c5f548426be7d18b8fd755a0ceb730fe5cf7510c6fa6f0870e388277c5f4c717af66d53c440feedffb29b4b@134.209.100.175:30303"]
```

Save the changes in `/var/lib/bor/config.toml`.

### Configuring a firewall

The sentry machine must have the following ports open to the world `0.0.0.0/0`:

* Port `26656`: Your Heimdall service will connect your node to other nodes Heimdall service.

* Port `30303`: Your Bor service will connect your node to other nodes Bor service.

* Port `22`: Open this port if your node is servicing validators. You will likely want to restrict what traffic can access this port as it is a sensitive port.

## Configure service files for Bor and Heimdall

After successfully installing Bor and Heimdall through [packages](#installing-package), their service file could be found under `/lib/systemd/system`, and Bor's config
file could be found under `/var/lib/bor/config.toml`.

You will need to check and modify these files accordingly.

    - In the service file, set `--chain` to `mainnet` or `amoy` accordingly

  Save the changes in `/lib/systemd/system/heimdalld.service`.

- Make sure the chain is set correctly in `/var/lib/bor/config.toml` file. Open the file with following command `sudo vi /var/lib/bor/config.toml`

    - In the config file, set `chain` to `mainnet` or `amoy` accordingly.

    - To enable Archive mode, you can optionally enable the following flags:

      ```
      gcmode "archive"

      [jsonrpc]
        [jsonrpc.ws]
          enabled = true
          port = 8546
          corsdomain = ["*"]
      ```

  Save the changes in `/var/lib/bor/config.toml`.


## Starting the sentry node

You will first start the Heimdall service. Once the Heimdall service syncs, you will start the Bor service.


### Reload service files

Reloading service files to make sure all changes to service files are loaded correctly.

```sh
sudo systemctl daemon-reload
```

### Starting the Heimdall service

Start the Heimdall services:

```sh
sudo service heimdalld start
```

Check the Heimdall service logs:

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


Check the Heimdalld logs:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value is:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is fully synced.

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

## Installing packages on the validator node

Follow the same [installation steps](#installing-package) on validator node.

## Configuring the validator node

!!! note
    
    To complete this section, you must have an RPC endpoint of your fully synced Ethereum mainnet node ready.


!!! warning
    
    Bor v1.1.0 and Heimdall v1.0.3 use standardized paths for configuration files and chain data. If you have existing config files and chain data on your node, please skip this section and refer to the [migration](https://www.notion.so/polygontechnology/Bor-Heimdall-Mainnet-Upgrade-v0-3-0-6575b2672a1d4ecc8cea8e1703bcc2df) guide to learn about migrating configs and data to standardized file locations. This is not relevant for new validators.

### Configure Heimdall

Log in to the remote validator machine.

Initialize heimdall configs

```shell
# For mainnet
sudo -u heimdall heimdalld init --chain=mainnet --home /var/lib/heimdall

# For testnet
sudo -u heimdall heimdalld init --chain=amoy --home /var/lib/heimdall
```

Open the Heimdall configuration file for editing:

```sh
vi /var/lib/heimdall/config/config.toml
```

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

In `heimdall-config.toml`, change the following:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node or testnet node,
  i.e Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

Save the changes in `heimdall-config.toml`.


### Configuring Bor


In `/var/lib/bor/config.toml`, add the following:

```
[p2p]
    [p2p.discovery]
        static-nodes = ["<replace with enode://validator_machine_enodeID@validator_machine_ip:30303>"]
```

To get the node ID of Bor on the sentry machine:

1. Log into the sentry machine.
2. Run `bor bootnode -node-key /var/lib/bor/data/bor/nodekey -dry-run`.

Example content of static node field in `/var/lib/bor/config.toml`:
```
[p2p]
    [p2p.discovery]
        static-nodes = ["enode://410e359736bcd3a58181cf55d54d4e0bbd6db2939c5f548426be7d18b8fd755a0ceb730fe5cf7510c6fa6f0870e388277c5f4c717af66d53c440feedffb29b4b@134.209.100.175:30303"]
```

Save the changes in `/var/lib/bor/config.toml`.

## Setting the Owner and Signer Key

On Polygon, it is recommended that you keep the owner and signer keys different.

* Signer: The address that signs the checkpoint transaction. It is advisable to keep at least 1 ETH on the signer address.
* Owner: The address that does the staking transactions. It is advisable to keep the MATIC tokens on the owner address.

### Generating a Heimdall private key

You must generate a Heimdall private key only on the validator machine. Do not generate a Heimdall
private key on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-validatorkey ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet's private key.

This will generate `priv_validator_key.json`. Move the generated JSON file to the Heimdall configuration directory:

```sh
mv ./priv_validator_key.json /var/lib/heimdall/config
```

### Generating a Bor keystore file

You must generate a Bor keystore file only on the validator machine. Do not generate a Bor keystore file
on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-keystore ETHEREUM_PRIVATE_KEY
```

where `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet's private key.

When prompted, set up a password to the keystore file.

This will generate a `UTC-<time>-<address>` keystore file.

Move the generated keystore file to the Bor configuration directory:

```sh
mv ./UTC-<time>-<address> /var/lib/bor/data/keystore
```

### Add `password.txt`

Make sure to create a `password.txt` file then add the Bor keystore file password right in the
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

!!! warning
    
    Please ensure that `priv_validator_key.json` & `UTC-<time>-<address>` files have relevant permissions. To set relevant permissions for `priv_validator_key.json`, run `sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key.json` and similarly `sudo chown -R heimdall:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>` for `UTC-<time>-<address>`.


## Configure service files for Bor and Heimdall

After successfully installing Bor and Heimdall through [packages](#installing-packages-on-the-validator-node), their service file could be found under `/lib/systemd/system`, and Bor's config file could be found under `/var/lib/bor/config.toml`.

You will need to check and modify these files accordingly.

- Make sure the chain is set correctly in `/lib/systemd/system/heimdalld.service` file. Open the file with following command `sudo vi /lib/systemd/system/heimdalld.service`

    - In the service file, set `--chain` to `mainnet` or `amoy` accordingly
    - Add `--bridge --all` to the heimdall command line for validator, example:
      ```
        ExecStart=/usr/local/bin/heimdalld start --home /var/lib/heimdall \
          --chain=mainnet \
          --bridge --all \
          --rest-server
      ```

  Save the changes in `/lib/systemd/system/heimdalld.service`.

- Make sure the chain is set correctly in `/var/lib/bor/config.toml` file. Open the file with following command `sudo vi /var/lib/bor/config.toml`

    - In the config file, set `chain` to `mainnet` or `amoy` accordingly.

    - Enable validator flags, example:
      ```
      [miner]
        mine = true
        gaslimit = 20000000
        gasprice = "30000000000"
        etherbase = "VALIDATOR ADDRESS"

      [accounts]
        allow-insecure-unlock = true
        password = "/var/lib/bor/password.txt"
        unlock = ["VALIDATOR ADDRESS"]
      ```

  Save the changes in `/var/lib/bor/config.toml`.

## Starting the validator node

At this point, you must have:

* The Heimdall service on the sentry machine syncs and is running.
* The Bor service on the sentry machine running.
* The Heimdall service and the Bor service on the validator machine configured.
* Your owner and signer keys configured.

### Reload service files

Reloading service files to make sure all changes to service files are loaded correctly.

```
sudo systemctl daemon-reload
```

### Starting the Heimdall service

You will now start the Heimdall service on the validator machine. Once the Heimdall service syncs, you
will start the Bor service on the validator machine.

!!!note
    
    The Heimdall service takes several days to sync from scratch fully.

    Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours.
    For detailed instructions, see [Snapshot Instructions for Heimdall and Bor](https://forum.polygon.technology/t/snapshot-instructions-for-heimdall-and-bor/9233).

    For snapshot download links, see [Polygon Chains Snapshots](https://snapshot.polygon.technology/).


Start the Heimdall services:

```sh
sudo service heimdalld start
```

Check the Heimdall service logs:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value is:

* `true`: The Heimdall service is syncing.
* `false`: The Heimdall service is synced.

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

!!! tip "Amoy node seeds"

    The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

- Heimdall seed nodes:

  ```bash
  moniker=<enter unique identifier>

  # Mainnet:
  seeds="1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"
  ```

- Bootnodes:

  ```bash
  # Mainnet:
  bootnode ["enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"]
  ```

## Health checks with the community

Now that your sentry and validator nodes are in sync and running, head over to
[Discord](https://discord.gg/polygon) and ask the community to health-check your nodes.

!!!note
    
    As validators, it’s mandatory to always have a check of the signer address. If the ETH balance reaches below 0.5 ETH then it should be refilled. Avoiding this will push out nodes from submitting checkpoint transactions.


## Next steps: Staking

Now that you have your sentry and validator nodes are health-checked, proceed to
the [staking](../operate-validator-node/validator-staking-operations.md) guide to start backing the network.
