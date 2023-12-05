The `approveAllForMintable` method can be used to approve all mintable tokens on root token.

```js
const erc115RootToken = posClient.erc115(<root token address>,true);

const approveResult = await erc115RootToken.approveAllForMintable();

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```
