---
id: is-approved-all
title: isApprovedAll
keywords: 
- 'pos client, erc721, isApprovedAll, polygon, sdk'
description: 'Checks if all token are approved.'
---

`isApprovedAll` method checks if all token is approved. It returns boolean value.

```
const erc721Token = posClient.erc721(<token address>, true);

const result = await erc721Token.isApprovedAll(<user Address>);

```
