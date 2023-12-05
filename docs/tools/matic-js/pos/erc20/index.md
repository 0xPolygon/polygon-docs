# ERC20

The `POSClient` has an `erc20` method which returns an object of an **ERC20** token.

You can then call various methods on the object.

```js
const erc20token = posClient.erc20(<token address>,<isRoot>);
```

Passing second arguments for `isRoot` is optional.

## Child token

Token on polygon can be initiated by using this syntax -

```js
const childERC20Token = posClient.erc20(<child token address>);
```

## Parent token

Token on ethereum can be initiated by providing the second parameter value as `true`.

```js
const parentERC20Token = posClient.erc20(<parent token address>, true);
```
