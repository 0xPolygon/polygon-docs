---
id: withdraw-exit-many
title: withdrawExitMany
keywords: 
- 'pos client, erc1155, withdrawExitMany, polygon, sdk'
description: 'Exit the withdraw process using txHash from withdrawStart.'
---

`withdrawExitMany` method can be used to exit the withdraw process by using the txHash from `withdrawStartMany` method.

```
const erc1155RootToken = posClient.erc1155(<root token address>, true);

const result = await erc1155RootToken.withdrawExitMany(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
