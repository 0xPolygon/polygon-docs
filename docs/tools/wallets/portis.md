!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

Portis is a web-based wallet built keeping easy user-onboarding in mind. It comes with a JavaScript SDK that integrates into the dApp and creates a local wallet-less experience for the user. Further, it handles setting up the wallet, transactions, and gas fees.

Like Metamask, it is non-custodial - users control their keys, Portis just stores them securely. But, unlike Metamask, it is integrated into the application and not the browser. Users have their keys associated with their login ID and passwords.

- **Type**: Non-custodial/HD.
- **Private Key Storage**: Encrypted and stored on Portis servers.
- **Communication to Ethereum Ledger**: Defined by the developer.
- **Private key encoding**: Mnemonic.

## Set up web3

Install Portis in your dApp:

```sh
npm install --save @portis/web3
```

Now, register your dApp with Portis to obtain a dApp ID using the [Portis Dashboard](https://dashboard.portis.io/).

Import `portis` and `web3` objects:

```js
import Portis from '@portis/web3';
import Web3 from 'web3';
```

Portis constructor takes the first argument as the dApp ID and the second argument as the network you would like to connect with. This can either be a string or an object.

```js
const portis = new Portis('YOUR_DAPP_ID', 'maticTestnet');
const web3 = new Web3(portis.provider);
```

## Set up account

If the installation and instantiation of Web3 was successful, the following should successfully return the connected account:

```js
this.web3.eth.getAccounts()
.then((accounts) => {
  this.account = accounts[0];
})
```

## Instantiating contracts

This is how we should instantiate contracts:

```js
const myContractInstance = new this.web3.eth.Contract(myContractAbi, myContractAddress)
```

## Calling functions

### Calling `call()` function

```js
this.myContractInstance.methods.myMethod(myParams)
.call()
.then (
  // do stuff with returned values
)
```

### Calling `send()` function

```js
this.myContractInstance.methods.myMethod(myParams)
.send({
  from: this.account,gasPrice: 0
})
.then ((receipt) => {
  // returns a transaction receipt
})
```
