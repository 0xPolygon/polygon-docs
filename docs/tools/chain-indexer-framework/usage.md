---
comments: true
---

!!! info "Git repo and contact details"
    - For details about the technical architecture and if you want to contribute, head over to the repo https://github.com/0xPolygon/chain-indexer-framework
    - For any questions, reach out to us on the [Polygon R&D Discord](https://discord.com/invite/0xpolygonrnd).

## Installation

You can install the package using:

- [NPM](https://www.npmjs.com/package/@maticnetwork/chain-indexer-framework)
- [Yarn](https://yarnpkg.com/package/@maticnetwork/chain-indexer-framework)

### Using npm

```bash
npm install @maticnetwork/chain-indexer-framework
```
### Using Yarn

```bash
yarn add @maticnetwork/chain-indexer-framework
```
  
## Usage
    
```jsx
// Import the chain-indexer-framework module
const chain-indexer-framework = require('@maticnetwork/chain-indexer-framework');
```

## Examples 
    
To gain a clearer understanding of the entire process, check out our prebuilt [examples](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/README.md). 

- [The first example](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/matic_transfer/README.md) involves indexing MATIC transfer events from the Ethereum blockchain.
- [The second example](https://github.com/0xPolygon/chain-indexer-framework/blob/main/examples/nft_balancer/README.md) involves indexing NFT transfers and maintaining NFT balances.

Both these examples encompass all the layers involved, starting from producers, moving through transformers, and concluding with consumers.