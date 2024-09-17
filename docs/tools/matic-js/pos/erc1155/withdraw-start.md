The `withdrawStart` method can be used to initiate the withdraw process which will burn the specified amount of tokenId on polygon chain.

```js

const erc1155Token = posClient.erc1155(<child token address>);

const result = await erc1155Token.withdrawStart(<token id>,<amount>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
