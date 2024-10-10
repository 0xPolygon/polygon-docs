---
comments: true
---

This deployment guide walks you through starting and running a full node through various methods. For the system requirements, see the [minimum technical requirements](../prerequisites.md) guide.

!!! tip "Snapshots"
    
    Steps in these guide involve waiting for the Heimdall and Bor services to fully sync. This process takes several days to complete.

    Please use snapshots for faster syncing without having to sync over the network. For detailed instructions, see [Sync node using snapshots](../../how-to/snapshots.md).

    For snapshot download links, see the [Polygon Chains Snapshots](https://snapshots.polygon.technology/) page.


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

### Configure Heimdall seeds (Mainnet)

```bash
sed -i 's|^seeds =.*|seeds = "1500161dd491b67fb1ac81868952be49e2509c9f@52.78.36.216:26656,dd4a3f1750af5765266231b9d8ac764599921736@3.36.224.80:26656,8ea4f592ad6cc38d7532aff418d1fb97052463af@34.240.245.39:26656,e772e1fb8c3492a9570a377a5eafdb1dc53cd778@54.194.245.5:26656,6726b826df45ac8e9afb4bdb2469c7771bd797f1@52.209.21.164:26656"|g' /var/lib/heimdall/config/config.toml
chown heimdall /var/lib/heimdall
```

### Configure Heimdall seeds (Amoy)

The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

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

### Configure Bor seeds (mainnet)

```bash
sed -i 's|.*\[p2p.discovery\]|  \[p2p.discovery\] |g' /var/lib/bor/config.toml
sed -i 's|.*bootnodes =.*|    bootnodes = ["enode://b8f1cc9c5d4403703fbf377116469667d2b1823c0daf16b7250aa576bacf399e42c3930ccfcb02c5df6879565a2b8931335565f0e8d3f8e72385ecf4a4bf160a@3.36.224.80:30303", "enode://8729e0c825f3d9cad382555f3e46dcff21af323e89025a0e6312df541f4a9e73abfa562d64906f5e59c51fe6f0501b3e61b07979606c56329c020ed739910759@54.194.245.5:30303"]|g' /var/lib/bor/config.toml
chown bor /var/lib/bor
```

### Configure Bor seeds (Amoy)

The Heimdall and Bor seeds don't need to be configured manually for Amoy testnet since they've already been included at genesis.

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