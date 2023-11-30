# ERC1155

`POSClient` provides `erc1155` method which helps you to interact with a erc1155 token.

The method returns instance of **ERC1155** class which contains different methods.

```js
const erc721token = posClient.erc1155(<token address>, <isRoot>);
```

Passing second arguments for `isRoot` is optional.

## Child token

The token on Polygon can be initiated by using this syntax -

```js
const childERC20Token = posClient.erc1155(<child token address>);
```

## Parent token

The token on Ethereum can be initiated by providing second parameter value as `true`.

```js
const parentERC20Token = posClient.erc1155(<parent token address>, true);
```
