---
id: transfer
title: transfer
keywords: 
- 'pos client, erc1155, transfer, polygon, sdk'
description: 'Transfer tokens from one user to another user.'
---

`transfer` method can be used to transfer tokens from one user to another user.

```
const erc1155Token = posClient.erc1155(<token address>);

const result = await erc1155Token.transfer({
    tokenId: <tokenId>,
    amount: <amount>,
    from : <from address>,
    to : <to address>,
    data : <data to sent>, // data is optional
});

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```
