The `withdrawExit` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```js
const erc20RootToken = posClient.erc20(<root token address>, true);

const result = await erc20Token.withdrawExit(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();
```

This method does multiple RPC calls to generate the proof and process exit. So it is recommended to use withdrawExitFaster method.
