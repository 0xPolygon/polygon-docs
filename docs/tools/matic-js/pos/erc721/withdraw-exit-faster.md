The `withdrawExitFaster` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

It is fast because it generates proof in the back-end. You need to configure [setProofAPI](../../set-proof-api.md).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```js
const erc721RootToken = posClient.erc721(<root token address>, true);

const result = await erc721RootToken.withdrawExitFaster(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
