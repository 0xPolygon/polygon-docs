---
id: is-withdraw-exited-many
title: isWithdrawExitedMany
keywords: 
- 'pos client, erc1155, isWithdrawExitedMany, polygon, sdk'
description: 'Checks if withdraw has been exited for multiple tokens.'
---

`isWithdrawExitedMany` method check if withdraw has been exited for multiple tokens. It returns boolean value.

```
const erc1155Token = posClient.erc1155(<token address>);

const result = await erc1155Token.isWithdrawExitedMany(<exit tx hash>);

```
