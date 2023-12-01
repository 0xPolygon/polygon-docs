[ethers.js](https://docs.ethers.io/) is a library for interacting with the Ethereum Blockchain and its ecosystem.

## Setup ether.js

ether.js support is available via separate package as a plugin for matic.js.

### Installation

```sh
npm install @maticnetwork/maticjs-ethers
```

### Setup

```js
import { use } from '@maticnetwork/maticjs'
import { Web3ClientPlugin } from '@maticnetwork/maticjs-ethers'

// install ethers plugin
use(Web3ClientPlugin)
```

Let's see one example of creating `POSClient` using ethers -

```js
import { POSClient,use } from "@maticnetwork/maticjs"
import { Web3ClientPlugin } from '@maticnetwork/maticjs-ethers'
import { providers, Wallet } from "ethers";


// install web3 plugin
use(Web3ClientPlugin);

const parentProvider = new providers.JsonRpcProvider(rpc.parent);
const childProvider = new providers.JsonRpcProvider(rpc.child);

const posClient = new POSClient();
await posClient.init({
    network: 'testnet',
    version: 'mumbai',
    parent: {
      provider: new Wallet(privateKey, parentProvider),
      defaultConfig: {
        from : fromAddress
      }
    },
    child: {
      provider: new Wallet(privateKey, childProvider),
      defaultConfig: {
        from : fromAddress
      }
    }
});
```

## Examples

The examples for different cases are available on [ethers plugin repo](https://github.com/maticnetwork/maticjs-ethers).
