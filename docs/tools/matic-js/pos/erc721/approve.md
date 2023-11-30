---
id: approve
title: approve
keywords: 
- 'pos client, erc721, approve, polygon, sdk'
description: 'Approve required amount on root token'
---

`approve` method can be used to approve required amount on root token.

```
const erc721RootToken = posClient.erc721(<root token address>,true);

const approveResult = await erc721RootToken.approve(<token id>);

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```
