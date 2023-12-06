`withdrawExit` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

```js
const erc721RootToken = posClient.erc721(<root token address>, true);

const result = await erc721RootToken.withdrawExit(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

This method does multiple RPC calls to generate the proof and process exit. So it is recommended to use withdrawExitFaster method.
