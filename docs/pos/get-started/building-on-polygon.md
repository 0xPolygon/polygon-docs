---
comments: true
---

Ethereum developers are by default Polygon developers. Welcome. Simply switch to the [Polygon RPC](https://polygon-rpc.com/) and get started. All familiar tools used on Ethereum are supported on Polygon. Whether it is Foundry, Remix or Web3.js, Polygon offers the same UX as Ethereum.

Connect your wallet and deploy any decentralized application to either PoS mainnet or Amoy testnet (Sepolia-anchored).

## Overview

Polygon is a Layer-2 (L2) network to Ethereum, employing a Proof-of-Stake (PoS) consensus mechanism, and thus composed of the following two layers:

  - Heimdall layer, a consensus layer consisting of a set of proof-of-stake Heimdall nodes for monitoring staking contracts deployed on the Ethereum mainnet, and committing the Polygon PoS network checkpoints to the Ethereum mainnet. Heimdall is based on Tendermint.
  - Bor layer, an execution layer which is made up of a set of block-producing Bor nodes shuffled by Heimdall nodes. Bor is based on Go Ethereum (Geth).

In order to be a validator on the Polygon PoS network, you need to:

- Run a sentry node, which is a separate machine running a Heimdall node and a Bor node. A sentry node is open to all nodes on the Polygon PoS network.
- Run a validator node, which is a separate machine running a Heimdall node and a Bor node. A validator node is only open to its sentry node and closed to the rest of the network.
- Stake the MATIC tokens in the staking contracts deployed on the Ethereum mainnet.

## Network details

To access network-related details, including the chain ID, RPC URL, and more, for both the mainnet and Amoy testnet, refer to the [network documentation](../reference/rpc-endpoints.md).

## Wallets

You'll need an Ethereum-based wallet to interact with Polygon because the network runs on Ethereum Virtual Machine (EVM). You can choose to set up a [MetaMask](https://support.metamask.io/getting-started/getting-started-with-metamask/), or [Venly](../../tools/wallets/venly/create-wallet.md) (Arkane) Wallet. 

There are several other third-party wallet options available to choose from, and you'll find them listed out on [this page here](../../tools/wallets/getting-started.md).

!!! tip "Set up web3 provider"

    Refer to the following guides and follow along to set up your wallet for making web3 function calls:
    
    - [MetaMask](../../tools/wallets/metamask/index.md)
    - [Venly](../../tools/wallets/venly/index.md)

## Common tasks

Token bridging between Polygon PoS and Ethereum and vice-versa, and inter-layer communication are basic and essential actions that most dApps need to perform. Use the links below to navigate to guides that'll help you get started with these tasks.

* [Bridge tokens from Ethereum to PoS](../how-to/bridging/ethereum-polygon/ethereum-to-matic.md)
* [Bridge tokens from PoS to Ethereum](../how-to/bridging/ethereum-polygon/matic-to-ethereum.md)
* [L1 - L2 communication and state transfer](../how-to/bridging/l1-l2-communication/state-transfer.md)

## Connecting to Polygon

You can add Polygon to MetaMask, or directly use Venly (Arkane), which allows you to connect to Polygon using RPC.

In order to connect with the Polygon PoS network to read blockchain information, you can use a node provider like Alchemy SDK.

```js
// Javascript
// Setup: npm install alchemy-sdk
const { Alchemy, Network } = require("alchemy-sdk");

const settings = {
  apiKey: "demo", // Replace with your API Key from https://www.alchemy.com
  network: Network.MATIC_MAINNET, // Replace with MATIC_AMOY for testnet config
};

const alchemy = new Alchemy(settings);

async function main() {
  const latestBlock = await alchemy.core.getBlockNumber();
  console.log("The latest block number is", latestBlock);
}

main();
```

!!! note "Take it easy!"

    If this is overwhelming, that’s alright! You can jump right into the action and start hacking. Here are some notes before you start diving into resources, repositories, and docs:

    1. **Beware the cost of being on the bleeding edge**: Like typical niche programming, dApps and blockchain development moves very quickly. While researching, you may find complex code repositories, 404s on a documentation site, or even no documentation. Use that opportunity to [open an issue on the Polygon Knowledge Layer's GitHub repository](https://github.com/0xPolygon/polygon-docs/issues).
    2. **The learning curve may be daunting, but the barrier to entry is low**: The community is very open and welcoming! Projects welcome pull requests from outsiders and resolve any blockers actively. We’re working on creating a better world and contribution in any form is appreciated. We’ll be grateful to onboard you into this amazing Web3 ecosystem.

## Building a new dApp on Polygon?

Decentralized applications (dApps) act as the bridge between users and their data privacy on the blockchain. The increasing number of dApps validates their usefulness within the blockchain ecosystem, solving challenges like executing transactions between two participants without the need for central authority via smart contracts.

Suppose you have no prior experience building dApps. In that case, the below-mentioned resources will give you a head start on the tools required to build, debug, and deploy dApps on the Polygon PoS network.

- [Full Stack dApp: Tutorial Series](https://kauri.io/full-stack-dapp-tutorial-series/5b8e401ee727370001c942e3/c)
- [Web3.js](https://www.dappuniversity.com/articles/web3-js-intro)
- [Ethers.js](https://docs.ethers.io/v5/)
- [thirdweb](https://portal.thirdweb.com)
- [Remix](https://remix.ethereum.org/)
- [Hardhat](https://hardhat.org/hardhat-runner/docs/getting-started)
- [Foundry](https://github.com/foundry-rs/foundry/blob/master/README.md)
- [Metamask](https://support.metamask.io/getting-started/)
- [Venly (previously Arkane)](https://docs.venly.io/docs/getting-started-with-venly)
- [Develop a dApp using Fauna, Polygon, and React](https://github.com/hello-ashleyintech/polygon-fauna-app)

## Polygon DID

You can refer to the elaborate startup guide for users who wish to implement the Polygon DID, which is a three-part package consisting of an identity-registrar, identity-resolver, and identity-registry-contract.

* [Polygon DID integration guide](../how-to/polygon-did.md)

## Already have a dApp?

If you already have a decentralized application (dApp) and are looking for a platform to help you scale efficiently, then you are at the right place because Polygon allows you to:

1. Easily migrate from Ethereum Virtual Machine (EVM) based chain: Polygon prides itself in being the ultimate Layer-2 scaling solution for Ethereum. You don't have to worry about the underlying architecture while moving or deploying your dApps to the Polygon PoS network as long as it is EVM-compatible.
2. Use Polygon PoS as a faster transaction layer: Deploying your dApp to the PoS mainnet allows you to leverage Polygon as a faster transaction layer for your dApp. Additionally, you can get your tokens mapped by us. You can join our [technical discussions group](http://bit.ly/matic-technical-group) on Telegram to learn more.