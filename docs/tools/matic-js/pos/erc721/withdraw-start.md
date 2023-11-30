The `withdrawStart` method can be used to initiate the withdraw process which will burn the specified token on polygon chain.

```js
const erc721Token = posClient.erc721(<child token address>);

const result = await erc721Token.withdrawStart(<token id>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
