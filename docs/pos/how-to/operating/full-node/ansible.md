To configure and effectively manage a Polygon full node, we employ an [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html). This tool streamlines the process, ensuring a consistent and error-free setup.

## Prerequisites

- **Ansible with Python 3.x**: Your local machine must have Ansible installed with Python version 3.x. Note that Python 2.x is incompatible with this setup. Use the following command to install Ansible using pip (Python's package installer). If pip is not installed, refer to [pip installation guidelines](https://pip.pypa.io/en/stable/):

  ```bash
  pip3 install ansible
  ```

- **Reviewing Requirements**: Before proceeding, check the specific requirements listed in the [Polygon PoS Ansible repository](https://github.com/maticnetwork/node-ansible#requirements).

- **Environment Setup**: Ensure that Go is not installed on your environment. Ansible requires specific Go packages, and existing installations could lead to conflicts. Additionally, any pre-existing setups of Polygon Validator, Heimdall, or Bor on your VM/machine must be removed to avoid setup conflicts.

## Setting up the full node

- **Remote Machine Access**: Confirm access to the VM or machine where the full node will be set up. Detailed setup instructions are available at the [node-ansible setup guide](https://github.com/maticnetwork/node-ansible#setup).

- **Repository Cloning**: Clone the [node-ansible repository](https://github.com/maticnetwork/node-ansible) and navigate to the cloned directory:

  ```bash
  git clone https://github.com/maticnetwork/node-ansible
  cd node-ansible
  ```

- **Configuration File Editing**: In the `node-ansible` directory, edit the `inventory.yml` file to include your machine's IP address under the `sentry->hosts` section. Detailed instructions can be found [here](https://github.com/maticnetwork/node-ansible#inventory).

- **Connectivity Check**: Verify the remote machine's connectivity:

  ```bash
  ansible sentry -m ping
  ```

- **Testing Machine Configuration**: Run the following commands to ensure you have configured the correct machine:

  ```bash
  # For Mainnet:
  ansible-playbook playbooks/network.yml --extra-vars="bor_version=v1.0.0 heimdall_version=v1.0.3 network=mainnet node_type=sentry" --list-hosts

  # For Testnet:
  ansible-playbook playbooks/network.yml --extra-vars="bor_version=v1.1.0 heimdall_version=v1.0.3 network=mumbai node_type=sentry" --list-hosts
  ```

- **Full Node Setup**: Execute these commands to set up the full node:

  ```bash
  # For Mainnet:
  ansible-playbook playbooks/network.yml --extra-vars="bor_version=v1.1.0 heimdall_version=v1.0.3 network=mainnet node_type=sentry"

  # For Testnet:
  ansible-playbook playbooks/network.yml --extra-vars="bor_version=v1.0.0 heimdall_version=v1.0.3 network=mumbai node_type=sentry"
  ```

- **Troubleshooting**: In case of issues, use the following command to clean and reset the setup:

  ```bash
  ansible-playbook playbooks/clean.yml
  ```

- **Post-Setup Verification**: Log in to the remote machine and verify that the seeds and bootnodes in Heimdall and Bor `config.toml` files match the provided values. Update them if necessary.

- **Syncing Heimdall**: To check if Heimdall is fully synced:

  ```bash
  curl localhost:26657/status
  # The 'catching_up' value should be 'false'
  ```

- **Starting Bor**: Once Heimdall is synced, initiate Bor:

  ```bash
  sudo service bor start
  ```

## Managing logs and permissions

- **Logs**: Use `journalctl` for log management. For advanced usage, refer to [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs).

  - **Heimdall Node Logs**: `journalctl -u heimdalld.service -f`
  - **Bor Service Logs**: `journalctl -u bor.service -f`

- **Permission Issues**: If Bor encounters permission issues, run:

  ```bash
  sudo chown bor /var/lib/bor
  ```

## Network security and port configuration

- **Firewall Setup**: Open ports 22, 26656, and 30303 to all (0.

0.0.0/0) on the sentry node firewall.

- **Enhanced Security**: Consider using a VPN to restrict access to port 22 as per your security needs.

Congratulations! You have successfully configured and started a Polygon full node using Ansible. Remember to routinely check your setup for optimal performance and security compliance.
