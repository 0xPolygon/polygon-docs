The `isApprovedAll` method checks if all token is approved. It returns boolean value.

```js
const erc721Token = posClient.erc721(<token address>, true);

const result = await erc721Token.isApprovedAll(<user Address>);

```
