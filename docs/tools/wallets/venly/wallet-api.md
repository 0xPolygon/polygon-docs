!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

# Wallet API

The Wallet API allows developers to interact with blockchain networks and offer wallet functionality to their users without having to build everything from scratch. This can include features like account creation, transaction management, balance inquiries, and more.

- Welcome your users with custom wallet branding. You can customize the user interface to your taste.
- You are completely in charge of the wallet user experience to optimize user conversion. Get total freedom with regard to UX and asset management with our Wallet API.
- You and your users have complete control over digital assets without any third-party interference. Securely manage wallets with complete autonomy and privacy.
- In the event of loss of login credentials, you and your users can recover access to wallets with a security code or biometric verification.

![Wallet-API to create Polygon wallets](../../../img/tools/wallet/venly/07.png)

## Key features

| Features | Description |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wallet management           | Developers can use the API to create, manage, and secure wallets for their users.                                                                                           |
| Transaction services        | The API can enable the initiation and monitoring of blockchain transactions.                                                                                                |
| Token support               | It may allow the handling of various tokens and assets on supported blockchain networks.                                                                                    |
| Blockchain interactions     | Developers can integrate functionalities like reading data from the blockchain or writing data to it, along with creating and interacting with smart contracts. |
| Security features           | The API might offer features to enhance the security of user funds and transactions.                                                                                        |
| User experience enhancement | It can contribute to a smoother and more user-friendly interaction with blockchain applications.                                                                            |
| Multi-blockchain support    | Venly supports multiple blockchain networks, allowing developers to offer wallets for different cryptocurrencies. |

## Prerequisites

1. You need a Venly business account. If you don't have one, click to register in our [Developer Portal](https://portal.venly.io), or follow our [Getting Started with Venly](https://venly.readme.io/docs/getting-started) guide.
2. You need an active trial or paid subscription of the Wallet-API. You can start a 30-day free trial for the Wallet-API.
3. You need your client ID and client secret which can be obtained from the [Portal](https://portal.venly.io/).

## Creating a Polygon wallet

### Request Endpoint: [reference](https://docs.venly.io/reference/createwallet)

```https
POST /api/wallets
```
#### Header params

| Parameter | Param type | Value | Description |
| :--------------- | :--------- | :--------- | :--------------------------------------- |
| `Signing-Method` | Header     | `id:value` | `id`: This is the ID of the signing method. `value`: This is the value of the signing method. |

#### Body params

| Parameter                | Param type | Description                                            | Data type | Mandatory |
| :----------------------- | :--------- | :----------------------------------------------------- | :-------- | :-------- |
| `secretType`             | Body       | The blockchain on which to create the wallet           | String    | ✅         |
| `userId`                 | Body       | The ID of the user who you want to link this wallet to | String    | ❌         |
| `pincode` (_Deprecated_) | Body       | The pin that will encrypt and decrypt the wallet       | String    | ❌         |

### Request body

```json
{
  "secretType": "MATIC",
  "userId": "6a5a9020-e969-4d9a-ae4b-fcd91a75769d"
}
```

### Response body

!!! success "Wallet created"
    The wallet has been created and linked to the specified user (`userId`).

```json
{
    "success": true,
    "result": {
        "id": "10f26e75-1f01-4c46-a2c1-551f886c6db6",
        "address": "0x1bC722F33E62019F1d9CBcc43531c81731023483",
        "walletType": "API_WALLET",
        "secretType": "MATIC",
        "createdAt": "2023-12-06T12:17:36.420854289",
        "archived": false,
        "description": "Self-driven Zebra",
        "primary": false,
        "hasCustomPin": false,
        "userId": "6a5a9020-e969-4d9a-ae4b-fcd91a75769d",
        "custodial": false,
        "balance": {
            "available": true,
            "secretType": "MATIC",
            "balance": 0,
            "gasBalance": 0,
            "symbol": "MATIC",
            "gasSymbol": "MATIC",
            "rawBalance": "0",
            "rawGasBalance": "0",
            "decimals": 18
        }
    }
}
```

!!! success "Ready to try it out?"
    Click to read the [getting started guide for Wallet API.](https://docs.venly.io/docs/wallet-api-getting-started)
