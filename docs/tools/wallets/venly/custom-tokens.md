!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

## Fungible tokens

A developer can easily add support for their custom ERC20 token by creating a small pull request containing the token details toward the [Arkane Git repository](https://github.com/ArkaneNetwork/content-management/tree/master/tokens). Here is an example snippet of the information you must provide:

```json
{"name":"SAND","symbol":"SAND","address":"0x3845badade8e6dff049820680d1f14bd3903a5d0","decimals":18,"type":"ERC20"}
```

You can always contact the Venly team via their in-app chat and ask them to add your custom fungible token.

## Non-fungible tokens (NFTs)

Venly has developed its service in such a way that it will automatically pick up custom created Non-Fungible Tokens (NFTs) if they follow the ERC721 and ERC1155 standard.

![The Hulk ERC1155 NFT on Polygon](../../../img/tools/wallet/venly/06.png)
