[Matic.js](https://github.com/maticnetwork/matic.js) a JavaScript library that facilitates interaction with the Polygon network. It provides developers with simplified operations such as depositing, transferring, and withdrawing assets; allowing them to focus on building dApps without the need for in-depth knowledge of blockchain systems. 

Matic.js supports two popular libraries:

1. [Web3.js](https://web3js.readthedocs.io/)
2. [Ethers](https://docs.ethers.io/)

## Prerequisites

Ensure that your [Node.js](https://nodejs.org/en/)version is up to date. 

We recommend using Node.js version v18.19.1 for optimal compatibility.

## Matic.js core library

The library contains core logic and provides different APIs. The user interacts mostly with this library.

```sh
npm i @maticnetwork/maticjs
```

## Matic.js ethers library

The ethers library allows us to use any ethers function. It is injected into Matic.js using plugins.

```sh
npm install @maticnetwork/maticjs-ethers
```

### Matic.js web3 library

The web3 library allows us to use any web3 function.

```sh
npm install @maticnetwork/maticjs-web3
```
