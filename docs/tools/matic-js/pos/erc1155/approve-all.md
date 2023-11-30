---
id: approve-all
title: approveAll
keywords: 
- 'pos client, erc1155, approve, polygon, sdk'
description: 'Approve ERC1155 tokens.'
---

# approveAll

`approveAll` method can be used to approve all tokens on root token.

```
const erc1155RootToken = posClient.erc1155(<root token address>,true);

const approveResult = await erc1155RootToken.approveAll();

const txHash = await approveResult.getTransactionHash();

const txReceipt = await approveResult.getReceipt();

```
