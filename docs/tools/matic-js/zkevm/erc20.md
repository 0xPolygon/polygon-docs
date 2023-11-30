
## Calling the ERC20 method

`ZkEvmClient` provides `erc20` method which helps you to interact with an **ERC20** token on the zkEVM network. The method returns an object which has various other methods.

```js
const erc20token = zkEvmClient.erc20(<token address> , <isRoot>);
```

Passing second argument for `isRoot` is optional.

### For child token

Token on the zkEVM network can be initiated by using this syntax:

```js
const childERC20Token = zkEvmClient.erc20(<child token address>);
```

### For root token

Token on ethereum can be initiated by providing the **second parameter value as `true`**.

```js
const rootERC20Token = zkEvmClient.erc20(<root token address>, true);
```

## Check balance

You can use the `getBalance` method to get the balance of a user account. It is available for both child and root token.

```js
// get balance of user
const balance = await erc20Token.getBalance(<user Address>);
```

## Approve methods

### `approve`

The `approve` method can approve the required amount on the root and child token. It is needed for both deposit and withdrawal on the zkEVM network. Some tokens require this method during withdrawal while others require it during deposit.

```js
const erc20Token = zkEvmClient.erc20(<root token address>, true); // root token

// approve 1000 amount
const result = await erc20Token.approve(1000);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

#### `spenderAddress`

The address on which approval is given is called the `spenderAddress`. It is a third-party user or a smart contract which can transfer your token on your behalf.

By default, `spenderAddress` value is the `PolygonZkEVMBridge` contract address. You can specify `spenderAddress` value manually.

```js
// approve 1000 amount
const result = await erc20Token.approve(1000, {
    spenderAddress: <spender address value>
});
```

### `approveMax`

The `approveMax` method can approve the maximum amount on the root and child tokens.

```js
const erc20Token = zkEvmClient.erc20(<root token address>, true); // root token

const result = await erc20Token.approveMax();

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

#### `spenderAddress`

You can specify `spenderAddress` value manually.

```js
// approve 100 amount
const result = await erc20Token.approveMax({
    spenderAddress: <spender address value>
});
```

### `isApprovalNeeded`

`isApprovalNeeded` checks if approval is needed for the root or child token.

```js
const erc20Token = zkEvmClient.erc20(<token address>, true); // root token

const result = await erc20Token.isApprovalNeeded();
```

### `getAllowance`

`getAllowance` method can be used to get the approved amount for the user.

```js
const erc20Token = zkEvmClient.erc20(<token address>, true); // root token

const result = await erc20Token.getAllowance(<user address>);
```

#### `spenderAddress`

You can specify spender address value manually.

```js
const result = await erc20Token.getAllowance(<user Address>, {
    spenderAddress: <spender address value>
});
```

## Transfer method

The `transfer` method can be used to transfer amount from one address to another.

```js
const erc20Token = zkEvmClient.erc20(<token address>);

const result = await erc20Token.transfer(<amount>, <to>);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

## Deposit methods

### `deposit`

`deposit` method can be used to deposit the required amount from root chain to the child chain. We recommend users to store the transaction hash in order to be able to call `depositClaim` using that `txHash`.

```js
const erc20Token = zkEvmClient.erc20(<root token address>, true); // root token

//deposit 100 to user address
const result = await erc20Token.deposit(100, <user address>);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

### `depositEther`

`depositEther` method can be used to deposit required amount of **ether** from Ethereum to zkEVM.

```js
// ether address = 0x0000000000000000000000000000000000000000
const etherToken = zkEvmClient.erc20(<ether address>, true);

const result = await etherToken.deposit(<amount>, <user Address>);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

### `depositWithPermit`

`depositWithPermit` method can be used to deposit required amount of tokens from Ethereum to zkEVM along with the permit, so that user doesn't have to do multiple transactions for `approve` and `deposit`.

```js
const erc20Token = zkEvmClient.erc20(<root token address>, true); // root token

const result = await erc20Token.depositWithPermit(<amount>, <user address>);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

### `depositClaim`

`depositClaim` method is used for child tokens to claim their ERC20 token deposits.

```js
const erc20Token = zkEvmClient.erc20(<child token address>); // child token

const result = await erc20Token.depositClaim(<transaction hash);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

## Token withdrawal methods

### `withdraw`

`withdraw` method can be used to initiate the withdrawal process which transfers tokens from zkEVM network to Ethereum.

```js
const erc20Token = zkEvmClient.erc20(<child token address>); // child token

const result = await erc20Token.withdraw(<amount>, <user address);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```

The received transaction hash will be used to exit the withdraw process. So we recommend to store it.

### `withdrawExit`

`withdrawExit` method can be used to exit the withdrawal process by using the transaction hash from `withdraw` method. Note that the validity proof of `withdraw` transaction must be submitted in order to exit the withdrawal process.

```js
const erc20Token = zkEvmClient.erc20(<root token address>, true); // root token

const result = await erc20Token.withdrawExit(<transaction hash>);

const txHash = await result.getTransactionHash();
const receipt = await result.getReceipt();
```
