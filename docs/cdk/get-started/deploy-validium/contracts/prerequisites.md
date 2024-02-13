## Hardware

Make sure you have the following minimum hardware requirements.

- A Linux-based OS (e.g., Ubuntu Server 22.04 LTS).
- At least 8GB RAM with a 2-core CPU.
- An AMD64 architecture system.

## Software

Make sure you have the following minimum software requirements.

| Download link | Version | Check version | 
| --- | --- | --- |
| [Node](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) | ^20 | `node --version` |
| npm | ^10 | `npm --version` |
| [Foundry](https://book.getfoundry.sh/getting-started/installation) | ^0.2 | `forge --version` |
| [jq](https://jqlang.github.io/jq/download/) | ^1.6 | `jq -V` |

## Sepolia access

!!! info    
    You can run your own Sepolia node if you wish and we recommend this for a production set up. However, for simplicity and brevity, we demonstrate by using a node provider.

You will need the following:

- A Sepolia node RPC URL: e.g. https://sepolia.infura.io/v3/YOUR-INFURA-API-KEY.
- An account holding a minimum of 2 Sepolia ETH that you must send to a generated address to make for contract calls.

### Faucets

Use a public faucet to get Sepolia test ETH. 

- [Infura faucet](https://www.infura.io/faucet/sepolia).
- [Chainstack faucet](https://chainstack.com/sepolia-faucet/).
- [Quicknode faucet](https://faucet.quicknode.com/ethereum/sepoli).

## Configuration files

!!! warning
    We will be working with two separate `.env` files.

    - One `.env` file resides in the contracts project directory. We will set this up in the [contract set up](set-up.md#create-the-env-configuration) section.
    - Another `.env` resides in a shared system directory so that it is accessible to the node and all running processes. We will populate this file as we go along.

Create a folder `/tmp/cdk/` to store the shared `.env` file which will be used by all running processes.

```bash
mkdir /tmp/cdk/
```

!!! danger
    - Any files in the `tmp/` directory are deleted on shutdown.
    - For this reason, we recommend that you save this folder in your home directory once the shared configuration set up is complete.

### Shared environment variables

Create a `.env` file to store the environment variables that all running processes will share. This shared `.env` file allows us to use `jq` and `tomlq` to easily setup the configuration for the node and running processes.

This file will be populated throughout the [deploy node](../node/prerequisites.md) instructions.

```bash
nano /tmp/cdk/.env
```

!!! danger
    Don't forget, the system removes this file on shutdown.
