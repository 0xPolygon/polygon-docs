---
id: is-withdraw-exited
title: isWithdrawExited
keywords: 
- 'pos client, erc1155, isWithdrawExited, polygon, sdk'
description: 'Checks if a withdraw has been exited.'
---

`isWithdrawExited` method check if a withdraw has been exited. It returns boolean value.

```
const erc1155Token = posClient.erc1155(<token address>);

const result = await erc1155Token.isWithdrawExited(<exit tx hash>);

```
