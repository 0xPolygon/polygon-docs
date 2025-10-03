<!--
---
comments: true
---
-->

This section guides you through starting and running the validator node through an Ansible playbook. Check out the [Git repository](https://github.com/0xPolygon/node-ansible/tree/master?tab=readme-ov-file#sentry-node-setup) for details.

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

On your local machine, clone the [node-ansible repository](https://github.com/0xPolygon/node-ansible):

```sh
git clone https://github.com/0xPolygon/node-ansible
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
ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v2.0.0 ansible-playbook playbooks/network.yml --extra-var="bor_version=v2.0.0 heimdall_version=v1.2.0 network=mainnet node_type=sentry"
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
ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v2.0.0 ansible-playbook playbooks/network.yml --extra-var="bor_version=v2.0.0 heimdall_version=v1.2.0 network_version=mainnet-v1 node_type=validator heimdall_network=mainnet" --list-hosts
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

### Configure the Bor service

Open the config file for editing by running: `vi /var/lib/bor/config.toml`.

In `config.toml`, ensure the boot node addresses consisting of a node ID, an IP address, and a port by adding them under bootnodes in `[p2p.discovery]` section. The bootnodes are provided in the next section.

In `config.toml`, ensure the `static-nodes` parameter has the following values:

* `"enode://validator_machine_enodeID@validator_machine_ip:30303"` — the node ID and IP address of Bor set up on the validator machine.

To get the node ID of Bor on the validator machine:

1. Log into the validator machine.
2. Run: `bor attach /var/lib/bor/bor.ipc`
3. Run: `admin.nodeInfo.enode`

!!! info

    Please note that the IPC console is only accessible when Bor is running. To get the enode of the validator node, setup the validator node and then run the above commands.

Finally, save the changes in `config.toml`.

### Seeds and Bootnodes

The latest bor and heimdall seeds can be found [here](https://docs.polygon.technology/pos/reference/seed-and-bootnodes/). Adding them will ensure your node connects to the peers.

### Configure firewall

The sentry machine must have the following ports accessible from the public internet `0.0.0.0/0`:

* Port `26656`- Your Heimdall service will connect your node to other nodes' Heimdall service.

* Port `30303`- Your Bor service will connect your node to other nodes' Bor service.

!!! note "Sentry node with a VPN enabled"
    
    If the sentry node utilizes a VPN connection, it may restrict incoming SSH connections solely to the VPN IP address.


## Start the sentry node

First, start the Heimdall service. Once the Heimdall service is fully synced, start the Bor service.

!!! note "Syncing node using snapshots"
    
    The Heimdall service takes several days to fully sync from scratch. Alternatively, you can use a maintained snapshot, which will reduce the sync time to a few hours. For detailed instructions, see [<ins>Snapshot Instructions for Heimdall and Bor</ins>](https://docs.polygon.technology/pos/how-to/snapshots/).


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


To get the node ID of Heimdall on the sentry machine, run the following command:

1. Login to the sentry machine.
2. Run `heimdalld comet show-node-id`.

Example: `persistent_peers = "sentry_machineNodeID@sentry_instance_ip:26656"`

* `prometheus` — set the value to `true` to enable the Prometheus metrics. Example: `prometheus = true`.

Save the changes in `config.toml`.

Now, open `app.toml` for editing by running: `vi /var/lib/heimdall/config/app.toml`.

In the `app.toml` file, update the following parameters:

* `eth_rpc_url` — an RPC endpoint for a fully synced Ethereum mainnet node, i.e Infura. `eth_rpc_url =<insert Infura or any full node RPC URL to Ethereum>`

Example: `eth_rpc_url = "https://nd-123-456-789.p2pify.com/60f2a23810ba11c827d3da642802412a"`

* [Optional] Post [Rio hardfork](https://github.com/0xPolygon/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-73.md), which enables [VeBlop architecture](https://github.com/0xPolygon/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-64.md), validators are able to elect block producers through heimdall config flag `producer_votes`, whose default validator`"91,92,93"`. Change this value if needed, e.g. `producer_votes="91,92,93"`.

Finally, save the changes in `app.toml`.

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
heimdalld generate-validator-key ETHEREUM_PRIVATE_KEY
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
heimdalld generate-keystore ETHEREUM_PRIVATE_KEY
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

    The rest service and the bridge both start along with Heimdall.

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
