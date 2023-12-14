Matic.js is a javascript library which helps in interacting with the various components of Matic Network.

In this get started document we will learn about how we can setup and interact with the POS bridge.

In case you face any issues or have any queries, feel free to raise a [ticket](https://support.polygon.technology/support/tickets/new) to our Support Team or reach out to us on [Discord](https://discord.gg/32j4qNDn).

## Installation

**Install the maticjs package via npm:**

```bash
npm install @maticnetwork/maticjs
```

**Install the web3js plugin**

```bash
npm install @maticnetwork/maticjs-web3
```

## Setup

```javascript
import { use } from '@maticnetwork/maticjs'
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'

// install web3 plugin
use(Web3ClientPlugin)
```

In the above code we are initiating maticjs with `web3js` but you can also similarly initiate with [ethers](setup/ethers.md).

## POS client

`POSClient` helps us to interact with POS Bridge.

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

After `POSClient` is initiated, we need to initiate the required token types like - `erc20`, `erc721` etc.

### ERC20

**Create erc20 child token**

```
const erc20ChildToken = posClient.erc20(<token address>);
```

**Create erc20 parent token**

```
const erc20ParentToken = posClient.erc20(<token address>, true);

```

Once erc20 is initaited, you can call various methods that are available, like - `getBalance`, `approve`, `deposit` , `withdraw` etc.

#### `getBalance`

```
const balance = await erc20ChildToken.getBalance(<userAddress>)
console.log('balance', balance)
```

#### `approve`

```
// approve amount 10 on parent token
const approveResult = await erc20ParentToken.approve(10);

// get transaction hash
const txHash = await approveResult.getTransactionHash();

// get transaction receipt
const txReceipt = await approveResult.getReceipt();
```

As you can see, with its simple APIs maticjs makes it very easy to interact with maticjs bridge.

## Useful links

- [Examples](https://github.com/maticnetwork/matic.js/tree/master/examples)
