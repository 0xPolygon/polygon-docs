---
id: get-balance
title: getBalance
keywords: 
- 'pos client, erc1155, getBalance, polygon, sdk'
description: 'Get balance of ERC1155 token using matic.js.'
---

`getBalance` method can be used to get the balance of user for a token. It is available on both child and parent token.

```
const erc1155Token = posClient.erc1155(<token address>);

// get balance of user
const balance = await erc1155Token.getBalance(<userAddress>, <token id>);
```
