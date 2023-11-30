The `isWithdrawExited` method can be used to know whether the withdraw has been exited or not.

```js
const erc20RootToken = posClient.erc20(<root token address>,true);

const isExited = await erc20Token.isWithdrawExited(<burn tx hash>);
```
