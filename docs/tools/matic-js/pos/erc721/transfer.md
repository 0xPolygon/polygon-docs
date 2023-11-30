---
id: transfer
title: transfer
keywords: 
- 'pos client, erc721, transfer, polygon, sdk'
description: 'Transfer tokens from one user to another user.'
---

`transfer` method can be used to transfer tokens from one user to another user.

```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.transfer(<tokenid>,<from>,<to>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
