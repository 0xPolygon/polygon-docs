---
id: withdraw-exit-faster-many
title: withdrawExitFasterMany
keywords: 
- 'pos client, erc721, withdrawExitFasterMany, polygon, sdk'
description: 'Exit the withdraw process using txHash from `withdrawStartMany`.'
---

`withdrawExitFasterMany` method can be used to exit the withdraw process by using the txHash from `withdrawStartMany` method.


It is fast because it generates proof in backend. You need to configure [setProofAPI](/docs/tools/matic-js/set-proof-api).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```
const erc721RootToken = posClient.erc721(<root token address>, true);

const result = await erc721RootToken.withdrawExitFasterMany(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
