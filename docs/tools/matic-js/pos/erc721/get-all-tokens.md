The `getAllTokens` method returns all tokens owned by specified user.

```js
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.getAllTokens(<user address>, <limit>);

```

You can also limit the tokens by specifying the limit value in the second parameter.
