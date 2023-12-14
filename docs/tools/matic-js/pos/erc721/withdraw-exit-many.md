The `withdrawExitMany` method can be used to exit the withdraw process by using the txHash from `withdrawStartMany` method.

```js
const erc721RootToken = posClient.erc721(<root token address>, true);

const result = await erc721RootToken.withdrawExitMany(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
