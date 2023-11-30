---
id: get-tokens-count
title: getTokensCount
keywords: 
- 'pos client, erc721, getTokensCount, polygon, sdk'
description: 'Get  tokens count for specified user.'
---

`getTokensCount` method returns tokens count for specified user.

```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.getTokensCount(<user address>);

```
