This guide provides a step-by-step approach to deploy a Polygon validator node through an Ansible playbook, ensuring an efficient and reliable setup.

## Setup requirements and options

Before beginning, confirm your system aligns with the [system requirements for validator nodes](index.md). If you prefer running the validator node from binaries instead of Ansible, refer to [the manual installation instructions](manual-install.md).

!!! warning "Limited Validator Slots"

    New validators can only join when an existing validator leaves the network.

## Prerequisites

- Three machines: One local machine for Ansible playbook execution and two remote machines (one sentry, one validator).
- [Ansible](https://www.ansible.com/) installed on the local machine.
- [Python 3.x](https://www.python.org/downloads/) installed on the local machine.
- Ensure Go is *not* installed on the remote machines.
- SSH public key of your local machine must be present on the remote machines for Ansible connectivity.
- Access to Bloxroute as a relay network is available. For adding a gateway as a Trusted Peer, contact **@validator-support-team** on [Polygon Discord](https://discord.com/invite/0xPolygon).

## Setting up the nodes

### Preparing the Machines

1. Prepare three machines: two remote (sentry and validator) and one local (for running Ansible).
2. Install Ansible and Python 3.x on the local machine.

### Ansible Repository Setup

First, clone the [node-ansible repository](https://github.com/maticnetwork/node-ansible) on your local machine:

   ```sh
   git clone https://github.com/maticnetwork/node-ansible
   cd node-ansible
   ```

Then, edit the `inventory.yml` file to add IP addresses of the sentry and validator nodes:

   ```yml
   all:
     hosts:
     children:
       sentry:
         hosts:
           sentry_ip_1: # Sentry Node IP
       validator:
         hosts:
           validator_ip: # Validator Node IP
   ```

3. Test connectivity to the sentry node:

   ```sh
   ansible sentry -m ping
   ```

   Expected output:

   ```sh
   sentry_ip_1 | SUCCESS => {
       "changed": false,
       "ping": "pong"
   }
   ```

### Sentry node setup

Execute a test run of the sentry node setup:

   ```sh
   ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/sentry heimdall_network=mainnet" --list-hosts
   ```

Run the sentry node setup with sudo privileges:

   ```sh
   ansible-playbook -l sentry playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/sentry heimdall_network=mainnet" --ask-become-pass
   ```

   On completion, a success message will appear.

!!! note

    To restart the setup due to any issues, use `ansible-playbook -l sentry playbooks/clean.yml`.

### Validator node setup

After the sentry node setup:

Ensure the validator machine is reachable:

   ```sh
   ansible validator -m ping
   ```

Perform a test run for the validator setup:

   ```sh
   ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3 network_version=mainnet-v1 node_type=sentry/validator heimdall_network=mainnet" --list-hosts
   ```

Execute the validator node setup with sudo privileges:

   ```sh
   ansible-playbook -l validator playbooks/network.yml --extra-var="bor_version=v1.1.0 heimdall_version=v1.0.3  network_version=mainnet-v1 node_type=sentry/validator heimdall_network=mainnet" --ask-become-pass
   ```

A success message will indicate completion.

!!! note

    Use `ansible-playbook -l validator playbooks/clean.yml` for a fresh start in case of any issues.

### Configuring sentry node

Configure the Heimdall and Bor services on the sentry node:

1. Edit Heimdall's `config.toml` and Bor's `config.toml` as per the provided guidelines. Key parameters include `moniker`, `seeds`, `pex`, and `private_peer_ids`.
2. Set firewall rules to open ports `26656`, `30303`, and optionally `22` with restricted access.

### Starting sentry node

1. Start the Heimdall service and check its logs for successful execution.
2. Once Heimdall is synced, start the Bor service and monitor its logs for successful operation.

### Configuring validator node

1. Configure Heimdall and Bor similar to the sentry setup, ensuring correct Ethereum RPC endpoint settings.
2. Generate and place Heimdall's `priv_validator_key.json` and Bor's keystore file in their respective directories.
3. Add `password.txt` file in the Bor directory and include it in Bor's `config.toml`.

### Starting validator node

1. Start the Heimdall service on the validator node and wait for it to sync.
2. Start the Bor service and monitor its operation through logs.

## Health check and staking

- After setting up the nodes, request a health check by the community on [Polygon's Discord](https://discord.com/invite/0xPolygon).
- Maintain sufficient ETH balance in the signer address for transaction fees.
- Proceed to [Staking](staking.md) to participate in network validation.

By following these steps, you can effectively set up and run a Polygon validator node using Ansible.
