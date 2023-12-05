The `isApproved` method checks if token is approved for specified tokenId. It returns boolean value.

```js
const erc721Token = posClient.erc721(<token address>, true);

const result = await erc721Token.isApproved(<tokenId>);

```
