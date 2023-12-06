The `deposit` method can be used to deposit required amount of a token from ethereum to polygon chain.

```js
const erc1155RootToken = posClient.erc1155(<root token address>, true);
 
const result = await erc1155RootToken.deposit({
    amount: 1,
    tokenId: '123',
    userAddress: <from address>,
    data: '0x5465737445524331313535', // data is optional
});

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

Supplying **data** is optional.
