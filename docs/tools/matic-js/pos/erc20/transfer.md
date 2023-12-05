The `transfer` method can be used to transfer amount from one address to another address.

```js
const erc20Token = posClient.erc20(<token address>);

const result = await erc20Token.transfer(<amount>,<to>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
