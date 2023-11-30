---
id: is-withdraw-exited-many
title: isWithdrawExitedMany
keywords: 
- 'pos client, erc721, isWithdrawExitedMany, polygon, sdk'
description: 'Check if withdraw has been exited for multiple tokens.'
---

`isWithdrawExitedMany` method check if withdraw has been exited for multiple tokens. It returns boolean value.

```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.isWithdrawExitedMany(<exit tx hash>);

```
