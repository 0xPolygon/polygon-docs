The `deposit` method can be used to deposit required amount from root token to child token.

```js
const erc20RootToken = posClient.erc20(<root token address>, true);

//deposit 100 to user address
const result = await erc20Token.deposit(100, <user address>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

It might take some time to see the deposited amount on polygon chain. You can use [isDeposited](../is-deposited.md) method for checking status.
