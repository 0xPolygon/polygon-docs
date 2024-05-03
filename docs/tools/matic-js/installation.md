# Installation

## Matic.JS

[Matic.js](https://github.com/maticnetwork/matic.js) a JavaScript library that facilitates interaction with the Polygon network. It provides developers with simplified operations such as depositing, transferring, and withdrawing assets; allowing developers to focus on building (dApps) without the need for in-depth knowledge of blockchain systems. 

Matic.js is made up of a main library and an Ethereum library:

## Main library

The main library has the core logic and provides different APIs. The user interacts mostly with this library.

```sh
npm i @maticnetwork/maticjs
```
## Ethereum library

The Ethereum library allows us to use any favorite ether library. It is injected into maticjs using plugins.

matic.js supports two popular library -

1. [Web3.js](https://web3js.readthedocs.io/)
2. [Ethers](https://docs.ethers.io/)

### Web3.js

```sh
npm install @maticnetwork/maticjs-web3
```

### ethers

```sh
npm install @maticnetwork/maticjs-ethers
```
### System Requirements

Ensure that your [Node.js](https://nodejs.org/en/)version is up to date. We recommend using Node.js version v18.19.1 for optimal compatibility.