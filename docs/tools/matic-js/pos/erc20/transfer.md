---
id: transfer
title: transfer
keywords: 
- 'POS client, erc20, transfer, polygon, sdk'
description: 'Transfer amount from one address to another address.'
---

`transfer` method can be used to transfer amount from one address to another address.

```
const erc20Token = posClient.erc20(<token address>);

const result = await erc20Token.transfer(<amount>,<to>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
