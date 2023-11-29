This deployment guide walks you through starting and running a full node through various methods.

!!! tip "Snapshots"

    Steps in these guide involve waiting for the Heimdall and Bor services to fully sync. This process takes several days to complete. For snapshot download links, see the [Polygon Chains Snapshots](https://snapshots.polygon.technology/) page.

## Overview

In this section, we will guide you through a sequential process to ensure the successful setup of your Polygon full Proof of Stake (PoS) node. Adhering to this sequence is crucial for a smooth setup experience and optimal functioning of your node. The steps include:

1. **Machine Preparation**: This initial step involves readying your machine for the installation. We will guide you through ensuring that your system meets the necessary hardware and software requirements and preparing it for the subsequent steps.

2. **Installation of Heimdall and Bor Binaries**: After preparing your machine, the next critical phase is the installation of Heimdall and Bor binaries. These are essential components of the Polygon network, and we provide detailed instructions to simplify their installation on your full node machine.

3. **Setting Up Heimdall and Bor Services**: Once the binaries are installed, the focus shifts to setting up Heimdall and Bor as services on your full node machine. This process is pivotal for ensuring that these components run efficiently and are properly managed by your system.

4. **Configuration of the Full Node Machine**: With the services in place, the next step is to configure your full node machine. This involves fine-tuning various settings to optimize the node’s performance and ensure its compatibility with the Polygon network.

5. **Starting the Full Node Machine**: After configuration, we guide you through the process of starting your full node machine. This step is where your setup comes to life, and your machine begins its role as a Polygon node.

6. **Monitoring Node Health with the Community**: Finally, we emphasize the importance of monitoring the health of your node. This involves not just technical checks but also engaging with the Polygon community, a valuable resource for support and best practices.

It is imperative to follow these steps in the given order. Deviating from this sequence can lead to complications and potential issues in the setup and operation of your full PoS node. By adhering to this structured approach, you will ensure a successful and efficient node setup, ready to contribute to the Polygon network.

## Initial setup

To establish a robust foundation for your Polygon full node, begin by installing `build-essential`. This package is a prerequisite, containing essential tools for compiling and managing your node. Execute the following commands to install it:

```bash
sudo apt-get update
sudo apt-get install build-essential
```

## Installing Polygon node components

Polygon's node architecture is dual-layered, comprising Heimdall and Bor. Heimdall, a Tendermint-based layer, oversees Ethereum contracts, while Bor, derived from Geth, is responsible for block production.

**Critical Note:** The correct installation sequence of both binaries is essential for the node's functionality.

### Installing Heimdall

1. **Acquire the Latest Heimdall Version**: Ensure you download the latest Heimdall release from [here](https://github.com/maticnetwork/heimdall/releases). For instance, Heimdall v1.0.3 introduces critical enhancements like data size restrictions in state sync transactions.

2. **Installation Process**: Use the following command to install Heimdall, replacing `<heimdall_version>`, `<network_type>`, and `<node_type>` with appropriate values:

   ```bash
   curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <heimdall_version> <network_type> <node_type>
   ```

3. **Verification**: Confirm the installation by checking the version:

   ```bash
   heimdalld version --long
   ```

### Configuring Heimdall seeds

- For **Mainnet**, execute the following commands to configure seeds and set ownership:

  ```bash
  # Configuration Command
  sed -i 's|^seeds =.*|seeds = "seed_details"|g' /var/lib/heimdall/config/config.toml
  # Ownership Command
  chown heimdall /var/lib/heimdall
  ```

- For **Mumbai**, follow similar steps:

  ```bash
  # Configuration Command for Mumbai
  sed -i 's|^seeds =.*|seeds = "mumbai_seed_details"|g' /var/lib/heimdall/config/config.toml
  # Ownership Command
  chown heimdall /var/lib/heimdall
  ```

### Installing Bor

1. **Download Bor**: Install the latest Bor version from its [releases page](https://github.com/maticnetwork/bor/releases). Use this command:

   ```bash
   curl -L https://raw.githubusercontent.com/maticnetwork/install/main/bor.sh | bash -s -- <bor_version> <network_type> <node_type>
   ```

2. **Verification**: Check the Bor version post-installation:

   ```bash
   bor version
   ```

### Configuring Bor seeds

- **Mainnet Configuration** involves setting bootnodes and ownership:

  ```bash
  # Bootnodes Setting
  sed -i 's|.*bootnodes =.*|bootnodes = "mainnet_bootnodes"|g' /var/lib/bor/config.toml
  # Ownership Setting
  chown bor /var/lib/bor
  ```

- **Mumbai Configuration** follows a similar pattern:

  ```bash
  # Bootnodes Setting for Mumbai
  sed -i 's|.*bootnodes =.*|bootnodes = "mumbai_bootnodes"|g' /var/lib/bor/config.toml
  # Ownership Setting
  chown bor /var/lib/bor
  ```

## Updating service configuration and user permissions

Adjust user permissions for both Heimdall and Bor services by editing the respective service files:

```bash
# Heimdall Service User Update
sed -i 's/User=heimdall/User=root/g' /lib/systemd/system/heimdalld.service
# Bor Service User Update
sed -i 's/User=bor/User=root/g' /lib/systemd/system/bor.service
```

## Initiating services

Ensure Heimdall is fully synchronized before launching Bor. Use these commands to start and verify synchronization:

```bash
# Starting Heimdall
sudo service heimdalld start
# Verification Command
curl localhost:26657/status
```

Once Heimdall is synced (catching_up: false), start Bor:

```bash
sudo service bor start
```

## Monitoring and log management

Utilize `journalctl` for log management. Here's how to access logs for Heimdall and Bor:

```bash
# Heimdall Node Logs
journalctl -u heimdalld.service -f
# Bor Service Logs
journalctl -u bor.service -f
```

## Firewall and port configuration

Ensure proper network configuration by opening ports 22, 26656, and 30303. Additionally, consider

VPN options for enhanced security.
