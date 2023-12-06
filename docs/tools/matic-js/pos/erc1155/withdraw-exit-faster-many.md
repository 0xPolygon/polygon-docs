The `withdrawExitFasterMany` method can be used to exit the withdraw process by using the txHash from `withdrawStartMany` method.

It is fast because it generates proof in backend. You need to configure [setProofAPI](../../set-proof-api.md).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```js
const erc1155RootToken = posClient.erc1155(<root token address>, true);

const result = await erc1155RootToken.withdrawExitFasterMany(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();
```
