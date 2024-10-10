---
comments: true
---

!!! important
    Make sure you have set up Matic.js by following the [get started](../get-started.md) guide.

The `POSClient` interacts with the POS bridge.

```js
import { POSClient,use } from "@maticnetwork/maticjs"
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'
import HDWalletProvider from "@truffle/hdwallet-provider"

// install web3 plugin
use(Web3ClientPlugin);

const posClient = new POSClient();
await posClient.init({
    network: 'testnet',
    version: 'amoy',
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

After the `POSClient` is initiated, we can work with token types, such as `erc20`, `erc721` etc.

### ERC20

#### Create ERC20 child token

```js
const erc20ChildToken = posClient.erc20(<token address>);
```

#### Create ERC20 parent token

```js
const erc20ParentToken = posClient.erc20(<token address>, true);
```

Once erc20 is initaited, you can call various methods that are available, like - `getBalance`, `approve`, `deposit` , `withdraw` etc.

#### `getBalance`

```js
const balance = await erc20ChildToken.getBalance(<userAddress>)
console.log('balance', balance)
```

#### `approve`

```js
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

Once the `POSClient` is initiated, you can interact with all available APIs.
