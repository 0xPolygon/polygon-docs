---
id: usage 
title: How to use   
keywords: 
  - indexer
  - contract
  - polygon
description: "Learn how to use the Chain Indexer Framework"
---
    
[Github Link](https://github.com/0xPolygon/chain-indexer-framework) - Check this out to know more about the technical architecture OR to know how you can contribute to this open source project. For any questions, reach out to us on [Discord](https://discord.com/invite/0xPolygonDevs).

**Installation**
You can install the package using:

- [NPM](https://www.npmjs.com/package/@maticnetwork/chain-indexer-framework)
- [Yarn](https://yarnpkg.com/package/@maticnetwork/chain-indexer-framework)

** Using NPM **
```bash
npm install @maticnetwork/chain-indexer-framework
```
** Using Yarn**

```bash
yarn add @maticnetwork/chain-indexer-framework
```
    
**Usage** 
    
```jsx

// Import the chain-indexer-framework module
const chain-indexer-framework = require('@maticnetwork/chain-indexer-framework');

```


# Examples 
    
To gain a clearer understanding of the entire process, let's consider two straightforward [examples](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/README.md). 

- [First example](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/matic_transfer/README.md) involves indexing MATIC transfer events from the Ethereum blockchain.
- [Second example](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/nft_balancer/README.md) involes indexing NFT Transfer and maintaining NFT Balance

Both these examples encompass all the layers involved, starting from producers, moving through transformers, and concluding with consumers.