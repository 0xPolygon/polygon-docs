The `approve` method can be used to approve required amount on root token.

```js
const erc721RootToken = posClient.erc721(<root token address>,true);

const approveResult = await erc721RootToken.approve(<token id>);

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```
