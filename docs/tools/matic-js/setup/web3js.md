[Web3.js](https://web3js.readthedocs.io/) is a collection of libraries that allow you to interact with a local or remote Ethereum node using HTTP, IPC or WebSocket.

## Setup web3.js

web3.js support is available via separate package as a plugin for matic.js.

### Installation

```sh
npm install @maticnetwork/maticjs-web3
```

### Setup

```js
import { use } from '@maticnetwork/maticjs'
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'

// install web3 plugin
use(Web3ClientPlugin)
```

Let's see an example of creating `POSClient` using web3 -

```js
import { POSClient,use } from "@maticnetwork/maticjs"
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'
import HDWalletProvider from "@truffle/hdwallet-provider"

// install web3 plugin
use(Web3ClientPlugin);

const posClient = new POSClient();
await posClient.init({
    network: 'testnet',
    version: 'mumbai',
    parent: {
      provider: new HDWalletProvider(privateKey, mainRPC),
      defaultConfig: {
        from : fromAddress
      }
    },
    child: {
      provider: new HDWalletProvider(privateKey, childRPC),
      defaultConfig: {
        from : fromAddress
      }
    }
});

```

## Examples

The examples for different cases are available in [web3 plugin repo](https://github.com/maticnetwork/maticjs-web3).
