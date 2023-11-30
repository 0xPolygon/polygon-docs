---
id: get-token-id-at-index-for-user
title: getTokenIdAtIndexForUser
keywords: 
- 'pos client, erc721, getTokenIdAtIndexForUser, polygon, sdk'
description: 'Retrieve token id on supplied index for user.'
---

`getTokenIdAtIndexForUser` method returns token id on supplied index for user.

```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.getTokenIdAtIndexForUser(<index>,<user address>);

```
