Use the `depositEther` method to deposit **ETH** from ethereum to polygon. For example:

```js
const result = await posClient.depositEther(<amount>, <userAddress>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();
```
