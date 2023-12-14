The `isApprovedAll` method checks if all tokens are approved for a user. It returns boolean value.

```js
const erc1155Token = posClient.erc1155(<token address>, true);

const result = await erc1155Token.isApprovedAll(<user Address>);

```
