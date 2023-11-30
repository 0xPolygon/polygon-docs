---
id: withdraw-start-with-meta-data
title: withdrawStartWithMetaData
keywords: 
- 'pos client, erc721, withdrawStartWithMetaData, polygon, sdk'
description: 'Initiate the withdraw process with metadata.'
---

`withdrawStartWithMetaData` method can be used to initiate the withdraw process which will burn the specified token on polygon chain. Under the hood it calls `withdrawWithMetadata` method on token contract.


```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.withdrawStartWithMetaData(<token id>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
