---
comments: true
---

[Matic.js](https://github.com/maticnetwork/matic.js) a JavaScript library that facilitates interaction with the Polygon network. It provides developers with simplified operations such as depositing, transferring, and withdrawing assets, allowing them to focus on building dApps without requiring in-depth knowledge of blockchain systems. 

Matic.js supports two popular libraries:

1. [Web3.js](https://web3js.readthedocs.io/)
2. [Ethers](https://docs.ethers.io/)

## Prerequisites

Ensure that your [Node.js](https://nodejs.org/en/) version is up to date. 

We recommend using Node.js version v18.19.1 for optimal compatibility.

## Installation

### Matic.js core library

The library contains core logic and provides different APIs. The user interacts mostly with this library.

```sh
npm i @maticnetwork/maticjs
```

### Matic.js ethers library

The ethers library allows us to use any ethers function. It is injected into Matic.js using plugins.

```sh
npm install @maticnetwork/maticjs-ethers
```

### Matic.js web3 library

The web3 library allows us to use any web3 function.

```sh
npm install @maticnetwork/maticjs-web3
```

## Initializing

To code with matic, import the relevant libraries in your scripts. For example:

```javascript
import { use } from '@maticnetwork/maticjs'
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'

// install web3 plugin
use(Web3ClientPlugin)
```

- Click for more details on POS applications that use [`web3js`](setup/web3js.md).
- Click for more details on POS applications that use [`ethers`](setup/ethers.md).

## Support

In case you face any issues or have any queries, feel free to raise a [ticket](https://support.polygon.technology/support/tickets/new) to our Support Team or reach out to us on [Discord](https://discord.com/invite/0xPolygonCommunity).