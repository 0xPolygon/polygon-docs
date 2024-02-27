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

## Access to a Sepolia node

Use a node provider like Infura or Alchemy. We use Infura throughout but you can [use a different node provider](deploy-contracts.md#use-a-different-node-provider) if you want.

!!! important
    We recommend running your own Sepolia node for a production set up. 

You will need the following:

- A Sepolia node RPC URL: e.g. https://sepolia.infura.io/v3/YOUR-INFURA-API-KEY.
- An account holding a minimum of 2 Sepolia ETH that you must send to a generated address to make for contract calls.

### Faucets

Use a public faucet to get Sepolia test ETH. 

- [Infura faucet](https://www.infura.io/faucet/sepolia).
- [Chainstack faucet](https://chainstack.com/sepolia-faucet/).
- [Quicknode faucet](https://faucet.quicknode.com/ethereum/sepoli).

## Configuration with environment variables

We will be working with two separate `.env` files to manage the contracts and node configurations.

- One `.env` file resides in the contracts project directory. We will set this up in the [contracts environment variables set up](set-up.md#create-the-contracts-env-configuration) section.
- Another `.env` resides in a shared system directory, `/tmp/cdk/`, which is accessible to the node and all running processes. We set this up in the [system-wide environment variables set up](set-up.md#create-the-shared-system-env-configuration) section. This shared `.env` file allows us to use `jq` and `tomlq` to easily setup the configuration for the node and running processes.

!!! danger
    - Any files in the `tmp/` directory are deleted on shutdown.
    - For this reason, we recommend that you copy this folder and paste it into your home directory once the shared configuration set up is complete. That way, you can just add it back when you need to.