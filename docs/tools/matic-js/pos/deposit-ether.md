---
id: deposit-ether
title: deposit ether
keywords: 
- 'pos client, depositEther, polygon, sdk'
description: 'Deposit a required amount of ether from ethereum to polygon.'
---

`depositEther` method can be used to deposit required amount of **ether** from ethereum to polygon.

```
const result = await posClient.depositEther(<amount>, <userAddress>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
