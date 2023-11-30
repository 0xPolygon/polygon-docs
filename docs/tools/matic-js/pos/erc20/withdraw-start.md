---
id: withdraw-start
title: withdraw start
keywords: 
- 'pos client, erc20, withdrawStart, polygon, sdk'
description: 'Initiate the withdraw process.'
---

`withdrawStart` method can be used to initiate the withdraw process which will burn the specified amount on polygon chain.

```
const erc20Token = posClient.erc20(<child token address>);

// start withdraw process for 100 amount
const result = await erc20Token.withdrawStart(100);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

The received transaction hash will be used to exit the withdraw process. So we recommend to store it.

