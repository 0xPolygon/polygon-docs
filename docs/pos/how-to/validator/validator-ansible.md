---
comments: true
---

This section guides you through starting and running the validator node through an Ansible playbook. Check out the [Git repository](https://github.com/maticnetwork/node-ansible/tree/master?tab=readme-ov-file#sentry-node-setup) for details.

!!! info "Limited spots for new validators"
    
    There is limited space for accepting new validators. New validators can only join the active set when an already active validator unbonds.

## Prerequisites

* Three machines: One local machine on which you will run the Ansible playbook; two remote machines — one sentry and one validator.
* [Ansible](https://www.ansible.com/) installed on the local machine.
* [Python 3.x](https://www.python.org/downloads/) installed on the local machine.
* On the remote machines, make sure Go is *not* installed.
* Your local machine's SSH public key added to the remote machines, allowing Ansible to connect to them.

## Overview

To deploy a running validator node, follow these steps in the *exact sequence*:

!!! warning

    Performing these steps out of sequence may lead to configuration issues. It's crucial to note that setting up a sentry node must always *precede* the configuration of the validator node.

1. Have the three machines prepared.
2. Set up a sentry node through Ansible.
3. Set up a validator node through Ansible.
4. Configure the sentry node.
5. Start the sentry node.
6. Configure the validator node.
7. Set the owner and signer keys.
8. Start the validator node.

## Set up the sentry node

On your local machine, clone the [node-ansible repository](https://github.com/maticnetwork/node-ansible):

```sh
git clone https://github.com/maticnetwork/node-ansible
```

Change the working directory to the cloned repository using:

```sh
cd node-ansible
```

Add the IP addresses of the remote machines that will become a sentry node and a validator node to the `inventory.yml` file.

```yml
all:
  hosts:
  children:
    sentry:
      hosts:
        xxx.xxx.xx.xx: # <----- Add IP for sentry node
        xxx.xxx.xx.xx: # <----- Add IP for second sentry node (optional)
    validator:
      hosts:
        xxx.xxx.xx.xx: # <----- Add IP for validator node
```

Example:

```yml
all:
  hosts:
  children:
    sentry:
      hosts:
        188.166.216.25:
    validator:
      hosts:
        134.209.100.175:
```

Check that the remote sentry machine is reachable. On the local machine, run:

```sh
ansible sentry -m ping
```

You should get this as output:

```sh
xxx.xxx.xx.xx | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

Do a test run of the sentry node setup by running the following command:

```sh
ansible-playbook playbooks/network.yml --extra-var="bor_version=v1.3.7 heimdall_version=v1.0.7 network=mainnet node_type=sentry" --list-hosts
```

You should see an output like this:

```sh
playbook: playbooks/network.yml
  pattern: ['all']
  host (1):
    xx.xxx.x.xxx
```

Run the sentry node setup with sudo privileges:

```sh
ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v1.1.0 ansible-playbook playbooks/network.yml --extra-var="bor_version=v1.3.7 heimdall_version=v1.0.7 network=mainnet node_type=sentry"
```

Once the setup is complete, you will see a message of completion on the terminal.

!!! tip "How to start over"
    
    If you run into an issue and would like to start over, run:

    ```sh
    ansible-playbook -l sentry playbooks/clean.yml
    ```

## Set up the validator node

At this point, you have the sentry node set up.

Your local machine is also configured with an Ansible playbook to run the validator node setup.

To check that the remote validator machine is reachable, run `ansible validator -m ping` on your local machine.

You should see the following output:

```sh
xxx.xxx.xx.xx | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

Do a test run of the validator node setup by running the following command:

```sh
ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v1.1.0 ansible-playbook playbooks/network.yml --extra-var="bor_version=v1.3.7 heimdall_version=v1.0.7 network_version=mainnet-v1 node_type=validator heimdall_network=mainnet" --list-hosts
```

You should see an output like this:

```sh
playbook: playbooks/network.yml
  pattern: ['all']
  host (1):
    xx.xxx.x.xxx
```

Run the validator node setup with sudo privileges:

```sh
ansible-playbook playbooks/network.yml --extra-var="bor_version=v1.3.7 heimdall_version=v1.0.7  network_version=mainnet-v1 node_type=validator heimdall_network=mainnet"
```

Once the setup is complete, you will see a message of completion on the terminal.

!!! info
    
    If you run into an issue and would like to start over, run:

    ```sh
    ansible-playbook -l validator playbooks/clean.yml
    ```

## Configure the sentry node

Start by logging into the remote sentry machine.

### Configure Heimdall

Open the config file for editing by running `vi /var/lib/heimdall/config/config.toml`.

In the `config.toml` file, update the following parameters:

* `moniker` — any name. Example: `moniker = "my-full-node"`.
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

1. Log into the validator machine.
2. Run: `heimdalld tendermint show-node-id`.

Example: `private_peer_ids = "0ee1de0515f577700a6a4b6ad882eff1eb15f066"`.

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.
* `max_open_connections` — set the value to `100`. Example: `max_open_connections = 100`.

Finally, save the changes in `config.toml`.

### Configure the Bor service

Open the config file for editing by running: `vi /var/lib/bor/config.toml`.

In `config.toml`, ensure the boot node addresses consisting of a node ID, an IP address, and a port by adding them under bootnodes in `[p2p.discovery]` section:

```toml
-bootnodes "enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"
```

!!! info "Amoy node seeds"

    The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

In `config.toml`, ensure the `static-nodes` parameter has the following values:

* `"enode://validator_machine_enodeID@validator_machine_ip:30303"` — the node ID and IP address of Bor set up on the validator machine.

To get the node ID of Bor on the validator machine:

1. Log into the validator machine.
2. Run: `bor attach /var/lib/bor/bor.ipc`
3. Run: `admin.nodeInfo.enode`

!!! info

    Please note that the IPC console is only accessible when Bor is running. To get the enode of the validator node, setup the validator node and then run the above commands.

Finally, save the changes in `config.toml`.

### Configure firewall

The sentry machine must have the following ports accessible from the public internet `0.0.0.0/0`:

* Port `26656`- Your Heimdall service will connect your node to other nodes' Heimdall service.

* Port `30303`- Your Bor service will connect your node to other nodes' Bor service.

!!! note "Sentry node with a VPN enabled"
    
    If the sentry node utilizes a VPN connection, it may restrict incoming SSH connections solely to the VPN IP address.


## Start the sentry node

First, start the Heimdall service. Once the Heimdall service is fully synced, start the Bor service.

!!! note "Syncing node using snapshots"
    
    The Heimdall service takes several days to fully sync from scratch. Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours. For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://forum.polygon.technology/t/snapshot-instructions-for-heimdall-and-bor/9233).


### Start the Heimdall service

Start the Heimdall service by running the following command:

```sh
sudo service heimdalld start
```

To check the Heimdall service logs, run the following command:

```sh
journalctl -u heimdalld.service -f
```

!!! bug "Common errors"
    
    In the logs, you may see the following errors:

    * `Stopping peer for error`
    * `MConnection flush failed`
    * `use of closed network connection`

    These logs mean that one of the nodes on the network refused a connection to your node. Wait for your node to crawl more nodes on the network. You don't need to do anything manually to address these errors.


Check the sync status of Heimdall using the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value signifies the following:

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is fully synced.

Wait for the Heimdall service to fully sync.

### Start the Bor service

Once the Heimdall service is fully synced, start the Bor service using the following command.

```sh
sudo service bor start
```

Check the Bor service logs using the following command:

```sh
journalctl -u bor.service -f
```

## Configure the validator node

!!! note "RPC endpoint"
    
    To complete this section, you must have your own RPC endpoint of your own fully synced Ethereum mainnet node ready.

### Configure the Heimdall service

Log into the remote validator machine.

Open the config file for editing by running: `vi /var/lib/heimdall/config/config.toml`.

Next, update the following parameters in the config file:

* `moniker` — any name. Example: `moniker = "my-validator-node"`.
* `pex` — set the value to `false` to disable the peer exchange. Example: `pex = false`.
* `private_peer_ids` — comment out the value to disable it. Example: `# private_peer_ids = ""`.

To get the node ID of Heimdall on the sentry machine, run the following command:

1. Login to the sentry machine.
2. Run `heimdalld tendermint show-node-id`.

Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.

Save the changes in `config.toml`.

Now, open `heimdall-config.toml` for editing by running: `vi /var/lib/heimdall/config/heimdall-config.toml`.

In the `heimdall-config.toml` file, update the following parameters:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node, i.e Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

Finally, save the changes in `heimdall-config.toml`.

### Configure the Bor service

Open the config file for editing by running: `vi /var/lib/bor/config.toml`.

Update the value of `static-nodes` parameter as follows:

```toml
static-nodes = ["<replace with enode://sentry_machine_enodeID@sentry_machine_ip:30303>"]
```

To get the node ID of Bor on the sentry machine:

1. Log into the sentry machine.
2. Run `bor attach /var/lib/bor/bor.ipc`
3. Run `admin.nodeInfo.enode`

Finally, save the changes in `config.toml` file.

## Set the owner and signer key

On Polygon PoS, it is recommended that you keep the owner and signer keys different.

* Signer: The address that signs the checkpoint transactions. It is advisable to keep at least 1 ETH on the signer address.
* Owner: The address that does the staking transactions. It is advisable to keep the POL tokens on the owner address.

### Generate a Heimdall private key

!!! warning

    The Heimdall private key must be generated only on the validator machine. Do not generate it on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-validatorkey ETHEREUM_PRIVATE_KEY
```

Here `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet’s signer private key.


This will generate the `priv_validator_key.json` file. Move the newly generated JSON file to the Heimdall configuration directory using the following command:

```sh
mv ./priv_validator_key.json /var/lib/heimdall/config/
```

### Generate a Bor keystore file

!!! warning

    The Bor keystore file must be generated only on the validator machine. Do not generate it on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-keystore ETHEREUM_PRIVATE_KEY
```

Here `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet’s signer private key.

When prompted, set up a password to the keystore file.

This will generate a `UTC-<time>-<address>` keystore file.

Move the generated keystore file to the Bor configuration directory:

```sh
mv ./UTC-<time>-<address> /var/lib/bor/data/keystore/
```

### Add `password.txt`

Make sure to create a `password.txt` file, and then add the Bor keystore file password right in the `/var/lib/bor/password.txt` file.

### Add your Ethereum address

Open the config file for editing by running: `vi /var/lib/bor/config.toml`.

```bash
[miner]
  mine = true
  etherbase = "validator address"

[accounts]
  unlock = ["validator address"]
  password = "The path of the file you entered in password.txt"
  allow-insecure-unlock = true
```

!!! warning

    Please ensure that `priv_validator_key.json` & `UTC-<time>-<address>` files have relevant permissions. To set relevant permissions for `priv_validator_key.json`, run the following command:
    ```
    sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key
    ```
    Similarly, to set the permissions for `UTC-<time>-<address>`, run the following command:
    ```
    sudo chown -R bor:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>
    ```

Finally, save the changes in `/var/lib/bor/config.toml`.

## Start the validator node

### Start the Heimdall service

First, start the Heimdall service on the validator machine. Once the Heimdall service is fully synced, you can run the Bor service.

Start the Heimdall service using the following command:

```sh
sudo service heimdalld start
```

!!! info

    The `heimdall-rest` service and the `heimdall-bridge` both start along with Heimdall.

Check the Heimdall service logs by running the following command:

```sh
journalctl -u heimdalld.service -f
```

Check the sync status of Heimdall by running the following command:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value signifies the following:

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is fully synced.

Wait for the Heimdall service to fully sync.

### Start the Bor service

Once the Heimdall service on the validator machine is fully synced, start the Bor service on the validator machine.

Start the Bor service by running the following command:

```sh
sudo service bor start
```

Check the Bor service logs by running the following command:

```sh
journalctl -u bor.service -f
```
