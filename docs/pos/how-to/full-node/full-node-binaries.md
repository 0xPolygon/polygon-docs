<!--
---
comments: true
---
-->

This deployment guide walks you through starting and running a full node through various methods. For the system requirements, see the [minimum technical requirements](../prerequisites.md) guide.

!!! tip "Snapshots"
    
    Steps in these guide involve waiting for the Heimdall and Bor services to fully sync. This process takes several days to complete.

    Please use snapshots for faster syncing without having to sync over the network. For detailed instructions, see [Sync node using snapshots](../../how-to/snapshots.md).
    

## Overview

!!! warning
    
    It is essential to follow the outlined sequence of actions precisely, as any deviation may lead to potential issues.

- Prepare the machine.
- Install Heimdall and Bor binaries on the full node machine.
- Set up Heimdall and Bor services on the full node machine.
- Configure the full node machine.
- Start the full node machine.
- Check node health with the community.


### Install `build-essential`

This is *required* for your full node. In order to install, run the below command:

```bash
sudo apt-get update
sudo apt-get install build-essential
```

## Install binaries

Polygon node consists of 2 layers: Heimdall and Bor. Heimdall is a Tendermint fork that monitors contracts in parallel with the Ethereum network. Bor is basically a Geth fork that generates blocks shuffled by Heimdall nodes.

Both binaries must be installed and run in the correct order to function properly.

### Heimdall

Install the latest version of Heimdall and related services. Make sure you checkout to the correct [release version](https://github.com/maticnetwork/heimdall/releases).

To install *Heimdall*, run the following commands:

```bash
curl -L https://raw.githubusercontent.com/maticnetwork/install/main/heimdall.sh | bash -s -- <heimdall_version> <network_type> <node_type>
```

You can run the above command with following options:

- `heimdall_version`: Valid v1.0+ release tag from https://github.com/maticnetwork/heimdall/releases
- `network_type`: `mainnet` and `amoy`
- `node_type`: `sentry`

This will install the `heimdalld` and `heimdallcli` binaries. Verify the installation by checking the Heimdall version on your machine:

```bash
heimdalld version --long
```

### Bor

Install the latest version of Bor, based on valid v1.0+ [released version](https://github.com/maticnetwork/bor/releases).

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

### Configure Heimdall and Bor seeds

The latest bor and heimdall seeds can be found [here](https://docs.polygon.technology/pos/reference/seed-and-bootnodes/). To configure them, update the following lines:

- Set the `seeds` value in `/var/lib/heimdall/config/config.toml`
- Set the `bootnodes` in `/var/lib/bor/config.toml`

This will ensure your node connects to the peers.


### Update service config user permission

```bash
sed -i 's/User=heimdall/User=root/g' /lib/systemd/system/heimdalld.service
sed -i 's/User=bor/User=root/g' /lib/systemd/system/bor.service
```

## Start services

Run the full Heimdall node with these commands on your Sentry Node:

```bash
sudo service heimdalld start
```

!!! warning "Wait for Heimdall to complete syncing"

    Ensure that Heimdall is fully synced before starting Bor. Initiating Bor without complete synchronization of Heimdall may lead to frequent issues.

To check if Heimdall is synced:
  1. On the remote machine/VM, run `curl localhost:26657/status`.
  2. In the output, `catching_up` value should be `false`.

Once Heimdall is synced, run the following command:

```bash
sudo service bor start
```

## Logs

Logs can be managed by the `journalctl` linux tool. Here is a tutorial for advanced usage: [How To Use Journalctl to View and Manipulate Systemd Logs](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs).

### Check Heimdall node logs

```bash
journalctl -u heimdalld.service -f
```

### Check Bor node logs

```bash
journalctl -u bor.service -f
```
