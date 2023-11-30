---
id: withdraw-exit-faster
title: withdrawExitFaster
keywords: 
- 'pos client, erc721, withdrawExitFaster, polygon, sdk'
description: 'Exit the withdraw process using txHash from `withdrawStart`'
---

`withdrawExitFaster` method can be used to exit the withdraw process by using the txHash from `withdrawStart` method.


It is fast because it generates proof in backend. You need to configure [setProofAPI](/docs/tools/matic-js/set-proof-api).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```
const erc721RootToken = posClient.erc721(<root token address>, true);

const result = await erc721RootToken.withdrawExitFaster(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
