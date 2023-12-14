This guide will assist you in setting up a Polygon validator node using packages, with a focus on maintaining optimal node performance and security.

## System Requirements

Before starting, ensure your setup meets the criteria outlined in the [system requirements for validator nodes](index.md).

### Utilizing snapshots for efficiency

Syncing the **Heimdall** and **Bor** services from scratch can take several days. To expedite this, consider using a maintained snapshot, reducing sync time to just a few hours. Detailed instructions and snapshot download links are available at:

- [Snapshot Instructions for Heimdall and Bor](../../../how-to/snapshots.md)
- [Polygon Chains Snapshots](https://snapshot.polygon.technology/)

### Port configuration

Proper port configuration is crucial for both Sentry and Validator nodes, involving open and restricted port settings to balance accessibility and security. Detailed instructions are available in the "Port Configuration Details" section below.

### Prerequisites

- Two machines: one for the Sentry node and one for the Validator node.
- Install `build-essential` on both machines:

  ```sh
  sudo apt-get install build-essential
  ```

- Go 1.19 installation on both machines:

  ```sh
  wget https://raw.githubusercontent.com/maticnetwork/node-ansible/master/go-install.sh
  bash go-install.sh
  sudo ln -nfs ~/.go/bin/go /usr/bin/go
  ```

- RabbitMQ installation on both machines (refer to [Downloading and Installing RabbitMQ](https://www.rabbitmq.com/download.html) for guidance).

## Installation process

### Heimdall installation

Install Heimdall using either the latest version for the Polygon Mainnet or a specific version for the desired network type (`mainnet` or `mumbai`):

- Latest version:

  ```shell
  curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash
  ```

- Specific version:

  ```shell
  curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <version> <network> <node_type>
  ```

### Bor installation

Similarly, install Bor with either the latest version or a specific version:

- Latest version:

  ```shell
  curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash
  ```

- Specific version:

  ```shell
  curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- <version> <network> <node_type>
  ```

### Verification

After installation, verify Heimdall and Bor:

- Heimdall: `heimdalld version --long`
- Bor: `bor version`

### Configuration

Configure your Sentry and Validator nodes according to specific guidelines, including modifying `config.toml` and other configuration files for Heimdall and Bor. Ensure all settings are correctly adjusted to facilitate secure and efficient node operation.

### Starting the nodes

Begin with the Sentry node:

1. Start the Heimdall service and wait for full sync.
2. Subsequently, start the Bor service.

Once the Sentry node is operational, proceed with the Validator node:

1. Start the Heimdall service after syncing.
2. Start the Bor service.

### Health checks and community support

After setting up, engage with the Polygon community on [Discord](https://discord.gg/polygon) for node health checks and support.

### Staking and validator participation

Once your nodes are verified and operational, follow the [Staking](staking.md) guide to participate actively in the network as a validator.

### Port configuration details

#### Sentry node ports

- **SSH (Port 22)**: Secure with VPN or restrict access.
- **Bor p2p (Port 30303)**: Open to public.
- **Heimdall/Tendermint p2p (Port 26656)**: Open to public.
- **Monitoring Ports (Ports 26660, 7071, 8545, 8546, 1317)**: Restrict access, open only for monitoring systems.

#### Validator node ports

- **SSH (Port 22)**: Secure with VPN or restrict access.
- **Bor p2p and Heimdall/Tendermint p2p (Ports 30303, 26656)**: Open only to the connected Sentry node.
- **Monitoring Ports (Ports 26660, 7071)**: Restrict access, open only for monitoring systems.

!!! warning "Limited validator slots"

    Note that new validators can join the active set only when an existing validator unbonds, due to the limited number of available slots.

By following these steps meticulously, you can ensure a secure and efficient setup of your Polygon validator node, contributing meaningfully to the network's performance and security.
