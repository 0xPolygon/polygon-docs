---
id: withdraw-start-many
title: withdrawStartMany
keywords: 
- 'pos client, erc721, withdrawStartMany, polygon, sdk'
description: 'Initiate the withdraw process.'
---

`withdrawStartMany` method can be used to initiate the withdraw process which will burn the multiple token on polygon chain.

```
const erc721Token = posClient.erc721(<child token address>);

const result = await erc721Token.withdrawStartMany([<token id1>, <token id2>]);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
