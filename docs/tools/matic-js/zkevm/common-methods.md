## `isDeposited`

The `isDeposited` method can be used to check if a deposit has been completed.

```js
const isDeposited = await zkEvmClient.isDeposited(tx_hash);
```

## `isDepositClaimable`

The `isDepositClaimable` method checks if a deposit can be claimed on the network.

```js
const isDepositClaimable = await zkEvmClient.isDepositClaimable(tx_hash);
```

## `isWithdrawExitable`

This method checks if the withdrawal process can be exited.

```js
const isWithdrawExitable = await zkEvmClient.isWithdrawExitable(tx_hash);
```

## `isExited`

isExited method checks if a withdrawal has been exited. It returns a boolean value.

```js
const isExited = await zkEvmClient.isExited(tx_hash);
```
