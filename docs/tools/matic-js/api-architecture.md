The Matic.js library follows common api architecture throughout and the APIs are divided into two types:

1. Read API
2. Write API

## Read API

Read methods do not publish anything on blockchain, so they do not consume any gas. For example:

```js
const erc20 = posClient.erc20('<token address>');
const balance = await erc20.getBalance('<user address>')
```

Read methods are very simple and return results directly.

## Write API

Write methods publish some data on the blockchain, so they consumes gas. Example of write methods are `approve`, `deposit` etc.

A write method returns (at least) two data items:

1. `TransactionHash`
2. `TransactionReceipt`

For example:

```js
// get a contract object
const erc20 = posClient.erc20('<token address>');

// send the transaction
const result = await erc20.approve(10);

// get transaction hash

const txHash = await result.getTransactionHash();

// get receipt

const receipt = await result.getReceipt();

```

## Transaction option

There are some configurable options that are available for all API's. These configurations can be passed as parameters.

Available configurations are -

- `from?`: string | number - The address transactions should be made from.
- `to?`: string - The address transactions should be made to.
- `value?`: number | string | BN - The value transferred for the transaction in wei.
- `gasLimit?`: number | string - The maximum gas provided for a transaction (gas limit).
- `gasPrice?`: number | string | BN - The gas price in wei to use for transactions.
- `data?`: string - The byte code of the contract.
- `nonce?`: number;
- `chainId?`: number;
- `chain?`: string;
- `hardfork?`: string;
- `returnTransaction?`: boolean - making it true will return the transaction object which can be used to send transaction manually.

This example configures the gas price:

```js
// get a contract object
const erc20RootToken = posClient.erc20(<root token address>,true);

// approve 100 amount
const approveResult = await erc20Token.approve(100, {
    gasPrice: '4000000000',
});

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();
```
