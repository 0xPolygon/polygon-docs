!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

[WalletConnect](https://walletconnect.com/) is an open protocol - not a wallet - built to create a communication link between dApps and wallets. A wallet and an application supporting this protocol will enable a secure link through a shared key between any two peers. A connection is initiated by the dApp displaying a QR code with a standard WalletConnect URI and the connection is established when the wallet application approves the connection request. Further requests regarding funds transfer are confirmed on the wallet application itself.

## Set up web3

To set up your dApp to connect with a user’s Polygon Wallet, you can use WalletConnect’s provider to directly connect to Polygon. Install the following in your dApp:

```bash
npm install --save @maticnetwork/walletconnect-provider
```

Install `matic.js` for Polygon integration:

```bash
npm install @maticnetwork/maticjs
```

And add the following code in your dApp;

```js
import WalletConnectProvider from "@maticnetwork/walletconnect-provider"

import Web3 from "web3"
import Matic from "maticjs"
```

Next, set up Polygon and Sepolia provider via WalletConnect’s object:

```javascript
const maticProvider = new WalletConnectProvider(
  {
    host: `https://rpc-amoy.polygon.technology`,
    callbacks: {
      onConnect: console.log('connected'),
      onDisconnect: console.log('disconnected!')
    }
  }
)

const sepoliaProvider = new WalletConnectProvider({
  host: `https://ethereum-sepolia-rpc.publicnode.com`,
  callbacks: {
    onConnect: console.log('connected'),
    onDisconnect: console.log('disconnected')
  }
})
```

We created the above two provider objects to instantiate our Web3 object with:

```js
const maticWeb3 = new Web3(maticProvider)
const sepoliaWeb3 = new Web3(sepoliaProvider)
```

## Instantiating contracts

Once we have our **web3 object**, the instantiating of contracts involves the same steps as for Metamask. Make sure you have your **contract ABI** and **address** already in place.

```js
const myContractInstance = new this.maticWeb3.eth.Contract(myContractAbi, myContractAddress)
```

## Calling functions

!!! info
    The private key will remain in the user’s wallet and the **app does not access it in any way**.

We have two types of functions in Ethereum, depending upon the interaction with the blockchain. We `call()` when we read data and `send()` when we write data.

### Calling `call()` functions

Reading data doesn’t require a signature, therefore the code should be like this:

```js
this.myContractInstance.methods
  .myMethod(myParams)
  .call()
  .then (
  // do stuff with returned values
  )
```

### Calling `send()` functions

Since writing to the blockchain requires a signature, we prompt the user on their wallet (that supports WalletConnect) to sign the transaction.

This involves three steps:

1. Constructing a transaction
2. Getting a signature on the transaction
3. Sending signed transaction

```js
const tx = {
  from: this.account,
  to: myContractAddress,
  gas: 800000,
  data: this.myContractInstance.methods.myMethod(myParams).encodeABI(),
}
```

The above code creates a transaction object which is then sent to user’s wallet for signature:

```js
maticWeb3.eth.signTransaction(tx)
  .then((result) =>{
    maticWeb3.eth.sendSignedTransaction(result)
    .then((receipt) =>
    console.log (receipt)
  )
})
```

`signTransaction()` function prompts the user for their signature and `sendSignedTransaction()` sends the signed transaction (returns a transaction receipt on success).
