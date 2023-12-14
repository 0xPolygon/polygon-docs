The `withdrawStart` method can be used to initiate the withdraw process which will burn the specified amount on polygon chain.

```js
const erc20Token = posClient.erc20(<child token address>);

// start withdraw process for 100 amount
const result = await erc20Token.withdrawStart(100);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

The received transaction hash will be used to exit the withdraw process. So we recommend to store it.
