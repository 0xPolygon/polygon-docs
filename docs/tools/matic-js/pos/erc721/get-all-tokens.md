---
id: get-all-tokens 
title: getAllTokens
keywords: 
- 'pos client, erc721, getAllTokens, polygon, sdk'
description: 'Retrieve all tokens owened by specified user.'
---

`getAllTokens` method returns all tokens owned by specified user.

```
const erc721Token = posClient.erc721(<token address>);

const result = await erc721Token.getAllTokens(<user address>, <limit>);

```

you can also limit the tokens by specifying limit value in second parmater.
