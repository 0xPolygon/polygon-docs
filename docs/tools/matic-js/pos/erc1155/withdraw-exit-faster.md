The `withdrawExitFaster` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

It is fast because it generates proof in backend. You need to configure [setProofAPI](/docs/tools/matic-js/set-proof-api).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```js
const erc1155RootToken = posClient.erc1155(<root token address>, true);

const result = await erc1155RootToken.withdrawExitFaster(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
