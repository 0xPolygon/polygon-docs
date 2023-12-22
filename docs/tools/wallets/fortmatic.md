!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

Fortmatic SDK allows you to easily integrate your dApp with the Ethereum blockchain, whether you already have a dApp integrated with Web3 or are starting from scratch. Fortmatic provides a smooth and delightful experience for both you and your decentralized application users.

## Installation

Use the following command to install Fortmatic's wallet latest version:

```bash
npm i --save fortmatic@latest
```

## Example

Here is an example of application using Fortmatic:

```js title="example.js"
import Fortmatic from 'fortmatic';
import Web3 from 'web3';

const customNodeOptions = {
    rpcUrl: 'https://rpc-mumbai.matic.today', // your own node url
    chainId: 80001 // chainId of your own node
}

// Setting network to localhost blockchain
const fm = new Fortmatic('YOUR_TEST_API_KEY', customNodeOptions);
window.web3 = new Web3(fm.getProvider());
```
