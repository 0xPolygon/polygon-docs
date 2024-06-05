---
comments: true
---

This section guides you through starting and running the validator node through an Ansible playbook.

For the system requirements, see [validator node system requirements](validator-system-requirements.md).

If you would like to start and run the validator node from binaries, see the guide on [spinning up a validator node using binaries](./validator-binaries.md).

!!! note "Limited spots for new validators"
    
    There is limited space for accepting new validators. New validators can only join the active set when an already active validator unbonds.


## Prerequisites

* Three machines: One local machine on which you will run the Ansible playbook; two remote machines — one sentry and one validator.
* On the local machine, [Ansible](https://www.ansible.com/) installed.
* On the local machine, [Python 3.x](https://www.python.org/downloads/) installed.
* On the remote machines, make sure Go is *not* installed.
* On the remote machines, your local machine's SSH public key is on the remote machines to let Ansible connect to them.
* We have Bloxroute available as a relay network. If you need a gateway to be added as your Trusted Peer please contact *@validator-support-team* in [Polygon Discord](https://discord.com/invite/0xPolygon) > POS VALIDATORS | FULL NODE PROVIDERS | PARTNERS > bloxroute.

## Overview

!!! warning
    
    Please ensure you strictly adhere to the outlined sequence of actions to avoid encountering issues. For instance, it's imperative to set up a sentry node before configuring the validator node.


To get to a running validator node, do the following:

1. Have the three machines prepared.
2. Set up a sentry node through Ansible.
3. Set up a validator node through Ansible.
4. Configure the sentry node.
5. Start the sentry node.
6. Configure the validator node.
7. Set the owner and signer keys.
8. Start the validator node.
9. Check node health with the community.

## Set up the sentry node

On your local machine, clone the [node-ansible repository](https://github.com/maticnetwork/node-ansible):

```sh
git clone https://github.com/maticnetwork/node-ansible
```

Change to the cloned repository:

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
$ ansible sentry -m ping
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

Do a test run of the sentry node setup:

```sh
ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/sentry heimdall_network=mainnet" --list-hosts
```

This will be the output:

```sh
playbook: playbooks/network.yml
  pattern: ['all']
  host (1):
    xx.xxx.x.xxx
```

Run the sentry node setup with sudo privileges:

```sh
ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/sentry heimdall_network=mainnet" --ask-become-pass
```

Once the setup is complete, you will see a message of completion on the terminal.

!!! note "How to start over"
    
    If you run into an issue and would like to start over, run:

    ```sh
    ansible-playbook -l sentry playbooks/clean.yml
    ```

## Set up the validator node

At this point, you have the sentry node set up.

On your local machine, you also have the Ansible playbook set up to run the validator node setup.

Check that the remote validator machine is reachable. On the local machine, run `ansible validator -m ping`.

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

Do a test run of the validator node setup:

```sh
ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3 network_version=mainnet-v1 node_type=sentry/validator heimdall_network=mainnet" --list-hosts
```

You should get this as output:

```sh
playbook: playbooks/network.yml
  pattern: ['all']
  host (1):
    xx.xxx.x.xxx
```

Run the validator node setup with sudo privileges:

```sh
ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/validator heimdall_network=mainnet" --ask-become-pass
```

Once the setup is complete, you will see a message of completion on the terminal.

!!!note
    
    If you run into an issue and would like to start over, run:

    ```sh
    ansible-playbook -l validator playbooks/clean.yml
    ```

## Configure the sentry node

Log into the remote sentry machine.

### Configure the Heimdall Service

Open `config.toml` for editing `vi /var/lib/heimdall/config/config.toml`.

Change the following:

* `moniker` — any name. Example: `moniker = "my-full-node"`.
* `seeds` — the seed node addresses consisting of a node ID, an IP address, and a port.

  Should already have the following values:

  ```toml
  seeds="1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"
  ```

* `pex` — set the value to `true` to enable the peer exchange. Example: `pex = true`.
* `private_peer_ids` — the node ID of Heimdall set up on the validator machine.

  To get the node ID of Heimdall on the validator machine:

  1. Log into the validator machine.
  1. Run `heimdalld tendermint show-node-id`.

  Example: `private_peer_ids = "0ee1de0515f577700a6a4b6ad882eff1eb15f066"`.

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.
* `max_open_connections` — set the value to `100`. Example: `max_open_connections = 100`.

Save the changes in `config.toml`.

### Configure the Bor service

Open for editing `vi /var/lib/bor/config.toml`.

In `config.sh`, ensure the boot node addresses consisting of a node ID, an IP address, and a port by the bootnode paramater:

```config
bootnodes "enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"
```

Save the changes in `config.toml`.

Open for editing `vi /var/lib/bor/config.toml`.

In `config.toml`, ensure the `static-nodes` parameter has the following values:

* `"enode://validator_machine_enodeID@validator_machine_ip:30303"` — the node ID and IP address of Bor set up on the validator machine.

  To get the node ID of Bor on the validator machine:

  1. Log into the validator machine.
  1. Run `bor bootnode -node-key /var/lib/bor/data/bor/nodekey`, this command only works while Bor is not running. If the IP address is `0.0.0.0` then replace it with external facing IP address.

Save the changes in `config.toml`.

### Configure firewall

The sentry machine must have the following ports open to the world `0.0.0.0/0`:

* Port `26656`- Your Heimdall service will connect your node to other nodes using the Heimdall service.

* Port `30303`- Your Bor service will connect your node to other nodes using the Bor service.

* Port `22`- Open this port if your node is servicing validators. You will likely want to restrict what traffic can access this port as it is a sensitive port.

!!! note "Sentry node with a VPN enabled"
    
    If the sentry node utilizes a VPN connection, it may restrict incoming SSH connections solely to the VPN IP address.


## Start the sentry node

You will first start the Heimdall service. Once the Heimdall service syncs, you will start the Bor service.

!!! note "Syncing node using snapshots"
    
    The Heimdall service takes several days to fully sync from scratch.

    Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours. For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://forum.polygon.technology/t/snapshot-instructions-for-heimdall-and-bor/9233).

    For snapshot download links, see [Polygon Chains Snapshots](https://snapshot.polygon.technology/).


### Start the Heimdall service

The latest version, [Heimdall v1.0.3](https://github.com/maticnetwork/heimdall/releases/tag/v1.0.3), contains a few enhancements such as:
1. Restricting data size in state sync txs to:
    * *30Kb* when represented in `bytes`
    * *60Kb* when represented as `string`.
2. Increasing the *delay time* between the contract events of different validators to ensure that the mempool doesn't get filled very quickly in case of a burst of events which can hamper the progress of the chain.

The following example shows how the data size is restricted:

```text
Data - "abcd1234"
Length in string format - 8
Hex Byte representation - [171 205 18 52]
Length in byte format - 4
```

Start the Heimdall service:

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

    These mean that one of the nodes on the network refused a connection to your node. You do not need to do anything to address these errors. Wait for your node to crawl more nodes on the network.


Check the sync status of Heimdall:

```sh
curl localhost:26657/status
```

In the output, the `catching_up` value is:

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is fully synced.

Wait for the Heimdall service to fully sync.

### Start the Bor service

Once the Heimdall service is fully synced, start the Bor service.

Start the Bor service:

```sh
sudo service bor start
```

Check the Bor service logs:

```sh
journalctl -u bor.service -f
```

## Configure the validator node

!!! note "RPC endpoint"
    
    To complete this section, you must have your own RPC endpoint of your own fully synced Ethereum mainnet node ready. The use of Infura and Alchemy is also sufficient and widely used among validators.


### Configure the Heimdall service

Log into the remote validator machine.

Open `config.toml` for editing `vi /var/lib/heimdall/config/config.toml`.

Change the following:

* `moniker` — any name. Example: `moniker = "my-validator-node"`.
* `pex` — set the value to `false` to disable the peer exchange. Example: `pex = false`.
* `private_peer_ids` — comment out the value to disable it. Example: `# private_peer_ids = ""`.


  To get the node ID of Heimdall on the sentry machine:

  1. Login to the sentry machine.
  1. Run `heimdalld tendermint show-node-id`.

  Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.

Save the changes in `config.toml`.

Open for editing `vi /var/lib/heimdall/config/heimdall-config.toml`.

In `heimdall-config.toml`, change the following:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node, i.e Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`


Save the changes in `heimdall-config.toml`.

### Configure the Bor service

Open for editing `vi /var/lib/bor/config.toml`.

In `config.toml`, ensure the trusted-nodes parameter has the following values:

* `"enode://sentry_machine_enodeID@sentry_machine_ip:30303"` — the node ID and IP address of Bor set up on the sentry machine.

  To get the node ID of Bor on the sentry machine:

  1. Log into the sentry machine.
  1. Run ```bor bootnode -node-key /var/lib/bor/data/bor/nodekey```, this command only works while Bor is not running. If the IP address is `0.0.0.0`, replace it with external facing IP address.

Save the changes in `config.toml` file.

## Set the owner and signer key

!!!note
    
    To complete this section, you must have already created two Ethereum wallets and have the private keys available as needed. One address will be used as the `Signer` and the other address as the `Owner`. Only the `Signer` address will be used in this section at the moment.



On Polygon, you should keep the owner and signer keys different.

* Signer — the address that signs the checkpoint transactions. The recommendation is to keep at least 1 ETH on the signer address.
* Owner — the address that does the staking transactions. The recommendation is to keep the MATIC tokens on the owner address.

### Generate a Heimdall private key

!!! warning

    Generate a Heimdall private key exclusively on the validator machine. Avoid generating a Heimdall private key on the sentry machine.

To generate the private key, run:

```sh
heimdallcli generate-validatorkey ETHEREUM_PRIVATE_KEY
```

Here `ETHEREUM_PRIVATE_KEY` is your Ethereum wallet’s signer private key.


This will generate `priv_validator_key.json`. Move the generated JSON file to the Heimdall configuration directory:

```sh
mv ./priv_validator_key.json /var/lib/heimdall/config/
```

### Generate a Bor keystore file

You must generate a Bor keystore file only on the validator machine. **Do not generate a Bor keystore file on the sentry machine.**

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

Ensure the `keystore` parameter in `/var/lib/bor/config.toml` matches the directory `/var/lib/bor/data/keystore/`

### Add `password.txt`

Make sure to create a `password.txt` file then add the Bor keystore file password right in the `/var/lib/bor/password.txt` file.

Ensure that `password` parameter in `/var/lib/bor/config.toml` matches the location of the password file.

### Add your Ethereum address

Open for editing `vi /var/lib/bor/config.toml`.

In the `[accounts]` table, you should have paramater `password` already defined from previous step, now add your Ethereum address to `unlock` parameter and also ensure `allow-insecure-unlock` is set to `true`.

Example: 

```sh
 [accounts]
    allow-insecure-unlock = true
    password = "/var/lib/bor/password.txt"
    unlock = ["0xca67a8D767e45056DC92384b488E9Af654d78DE2"]
```

Save the changes in `/var/lib/bor/config.toml`.

## Start the validator node

At this point, you must have:

* The Heimdall service on the sentry machine fully synced and running.
* The Bor service on the sentry machine running.
* The Heimdall service and the Bor service on the validator machine configured.
* Your owner and signer keys configured.

### Start the Heimdall service

You will now start the Heimdall service on the validator machine. Once the Heimdall service syncs, you will start the Bor service on the validator machine.

Start the Heimdall service:

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

* `true` — the Heimdall service is syncing.
* `false` — the Heimdall service is fully synced.

Wait for the Heimdall service to fully sync.

### Start the Bor service

Once the Heimdall service on the validator machine is fully synced, start the Bor service on the validator machine.

Start the Bor service:

```sh
sudo service bor start
```

Check the Bor service logs:

```sh
journalctl -u bor.service -f
```

### Seed nodes and bootnodes

!!! tip "Amoy testnet seeds"

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

## Check node health with the community

Now that your Sentry and Validator nodes are synced and running, head over to [Discord](https://discord.com/invite/0xPolygon) and ask the community to health-check your nodes.

!!!note
    
    As validators, it’s mandatory to always have a check of the signer address. If the ETH balance reaches below 0.5 ETH then it should be refilled. Avoiding this will push out nodes from submitting checkpoint transactions.

## Proceed to staking

Now that you have your Sentry and Validator nodes health-checked, proceed to [Staking](../../how-to/operate-validator-node/validator-staking-operations.md).
