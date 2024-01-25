## Dependency Checking
Dependencies required for this section:

| Dependency | Version | Version Check Command |
| --- | --- | --- |
| node | ^20 | git —version |
| npm | ^10 | npm —version |
| foundry | ^0.2 | forge —version |
| jq | ^1.6 | jq -V |

## Sepolia Access

For Polygon CDK to function properly, it needs connection to a layer 1 EVM blockchain. For the purpose of this guide, we will be deploying the CDK contracts to [Sepolia testnet](https://www.alchemy.com/overviews/sepolia-testnet).

You have a couple options on connecting to the Sepolia testnet

1. Node Provider (easiest)
2. Run your own node (recommended for a production setup)

For the sake of simplicity, we will use a node provider ([Infura](https://www.infura.io)) for this guide.

You can use a different provider by modifying your hardhat config (see here)

The deployment is expected to use up to **2 Sepolia ETH**. You can get Sepolia ETH from public faucets such as the ones listed here:

[Infura Faucet](https://www.infura.io/faucet/sepolia)

[Chainstack Faucet](https://chainstack.com/sepolia-faucet/)

[Quicknode Faucet](https://faucet.quicknode.com/ethereum/sepoli)

## Configuration Environment

For this guide we will create a new folder inside `/tmp/` named `/cdk/` this will store all our configuration files along with a `.env` to store important values. This will also allow us to streamline the processs using `jq` and `tomlq`

```bash
mkdir /tmp/cdk/
touch /tmp/cdk/.env
```