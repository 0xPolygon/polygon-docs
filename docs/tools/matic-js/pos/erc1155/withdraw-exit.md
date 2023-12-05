The `withdrawExit` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

```js
const erc1155RootToken = posClient.erc1155(<root token address>, true);

const result = await erc1155RootToken.withdrawExit(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
