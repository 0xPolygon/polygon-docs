---
id: withdraw-exit
title: withdrawExit
keywords: 
- 'pos client, erc1155, withdrawExit, polygon, sdk'
description:  'Exit the withdraw process using txHash from withdrawStart.'
---

`withdrawExit` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.

```
const erc1155RootToken = posClient.erc1155(<root token address>, true);

const result = await erc1155RootToken.withdrawExit(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
