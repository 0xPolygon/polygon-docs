---
comments: true
---

## Node system requirements

Please note that all system requirements listed below are presented in a *Minimum/Recommended* format.

### Mainnet specs

| Node type             | RAM         | CPU            | Storage                                                                       | Network bandwidth |
| --------------------- | ----------- | -------------- | ----------------------------------------------------------------------------- | ----------------- |
| Full Node/Sentry Node | 32 GB/64 GB | 8 core/16 core | 4 TB/6 TB                                                                     | 1 Gbit/s          |
| Validator Node        | 32 GB/64 GB | 8 core/16 core | 4 TB/6 TB                                                                     | 1 Gbit/s          |
| Archive Node (Erigon) | 64 GB       | 16 core        | 16 TB(`io1` or above with at least 20k+ iops and RAID-0 based disk structure) | 1 Gbit/s          |


### Testnet (Amoy) specs

| Node type             | RAM        | CPU            | Storage                                                                            | Network bandwidth |
| --------------------- | ---------- | -------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Full Node/Sentry Node | 8 GB/16 GB | 8 core/16 core | 1 TB/2 TB                                                                          | 1 Gbit/s          |
| Validator Node        | 8 GB/16 GB | 8 core/16 core | 1 TB/2 TB                                                                          | 1 Gbit/s          |
| Archive Node (Erigon) | 16 GB      | 16 core        | 1 TB/2 TB (`io1` or above with at least 20k+ iops and RAID-0 based disk structure) | 1 Gbit/s          |

## Downloading the snapshot

It is recommended that you keep your snapshots handy before setting up the node. Link to the snapshot documentation [here](https://docs.polygon.technology/pos/how-to/snapshots/).

## Open necessary ports

### Sentry/full nodes

|          Port           | Description                                                                                                                                   |
| :---------------------: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|         `26656`         | Heimdall service connects your node to another node’s Heimdall service using this port.                                                       |
|         `30303`         | Bor service connects your node to another node’s Bor service using this port.                                                                 |
|          `22`           | For the validator to be able to SSH from wherever they are.                                                                                   |
|         `26660`         | Prometheus port for Tendermint/Heimdall. Not required to be opened to the public. Only allow for the monitoring systems (Prometheus/Datadog). |
|         `7071`          | Metric port for Bor. Only needs to be opened for the Monitoring system.                                                                       |
| `8545`, `8546`,  `1317` | Can be opened for Bor HTTP RPC, Bor WS RPC, and Heimdall API respectively; but only if really necessary.                                      |

### Validator nodes

|  Port   | Description                                                                                                                                                            |
| :-----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  `22`   | Opening this to the public is not a good idea as the default SSH port 22 is prone to attacks. It is better to secure it by allowing it only in a closed network (VPN). |
| `30303` | To be opened to only Sentry to which the validator is connected for Bor P2P discovery.                                                                                 |
| `26656` | To be opened to only Sentry to which the validator is connected for Heimdall/Tendermint P2P discovery.                                                                 |
| `26660` | Prometheus port for Tendermint/Heimdall. Not required to be opened to the public. Only allow for the monitoring systems (Prometheus/Datadog).                          |
| `7071`  | Metric port for Bor. Only needs to be opened for the monitoring system.                                                                                                |

## Install RabbitMQ

!!! info "Only for validator nodes"

    This step is only relevant for validator nodes.

Before setting up your validator node, it’s advisable to install the RabbitMQ service. You can use the following commands to set up RabbitMQ (if it’s not already installed):

```bash
sudo apt-get update
sudo apt install build-essential
sudo apt install erlang
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.10.8/rabbitmq-server_3.10.8-1_all.deb
sudo dpkg -i rabbitmq-server_3.10.8-1_all.deb
```
## Connect to Ethereum RPC endpoint

!!! info "Only for validator nodes"

    This step is only relevant for validator nodes.

Validator nodes need to connect to an Ethereum RPC endpoint. You may use your own Ethereum node, or utilize [external infrastructure providers](https://www.alchemy.com/chain-connect/chain/ethereum).

## Mandatory checklist for validators

Please follow the below checklist in order to set up your validator node using binaries, Ansible, or packages.

| Checklist           | Binaries                                                                                   | Ansible                                                                                  | Packages                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Machines required   | 2 Machines - *sentry* & *validator*                                                        | 3 Machines - *local machine*, *sentry* and *validator*                                   | 2 Machines - *sentry* & *validator*                                                        |
| Install Go packages | Yes                                                                                        | No                                                                                       | No                                                                                         |
| Install Python      | No                                                                                         | Yes (only on the local machine where the Ansible Playbook runs)                          | No                                                                                         |
| Install Ansible     | No                                                                                         | Yes (only on one machine)                                                                | No                                                                                         |
| Install Bash        | No                                                                                         | No                                                                                       | Yes                                                                                        |
| Run Build Essential | Yes                                                                                        | No                                                                                       | No                                                                                         |
| Node setup          | [Using binaries](https://docs.polygon.technology/pos/how-to/validator/validator-binaries/) | [Using Ansible](https://docs.polygon.technology/pos/how-to/validator/validator-ansible/) | [Using packages](https://docs.polygon.technology/pos/how-to/validator/validator-packages/) |

