The `approve` method can be used to approve required amount on the root token.

approve is required in order to deposit amount on polygon chain.

```js
const erc20RootToken = posClient.erc20(<root token address>,true);

// approve 100 amount
const approveResult = await erc20Token.approve(100);

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```

## `spenderAddress`

The address on which approval is given is called `spenderAddress`. It is a third-party user or a smart contract which can transfer your token on your behalf.

By default spenderAddress value is erc20 predicate address.

You can specify spender address value manually.

```js
const erc20RootToken = posClient.erc20(<root token address>,true);

// approve 100 amount
const approveResult = await erc20Token.approve(100, {
    spenderAddress: <spender address value>
});

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```
