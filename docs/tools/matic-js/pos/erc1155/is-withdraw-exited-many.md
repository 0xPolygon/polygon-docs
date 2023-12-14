The `isWithdrawExitedMany` method check if withdraw has been exited for multiple tokens. It returns boolean value.

```js
const erc1155Token = posClient.erc1155(<token address>);

const result = await erc1155Token.isWithdrawExitedMany(<exit tx hash>);

```
