The `isWithdrawExitedMany` method check if withdraw has been exited for multiple tokens. It returns boolean value.

```js
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.isWithdrawExitedMany(<exit tx hash>);

```
