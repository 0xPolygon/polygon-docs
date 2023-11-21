---
id: rpc-endpoints
title: RPC Endpoints
sidebar_label: RPC Endpoints
description: "Network endpoints for Polygon PoS Mainnet and Mumbai Testnet."
keywords:
  - docs
  - polygon
  - remote procedure call
  - network endpoints
  - rpcs
  - http
  - websocket
  - wss
image: https://wiki.polygon.technology/img/polygon-wiki.png
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

This guide provides an index of network details for the Polygon Mumbai Testnet and Polygon PoS Mainnet, including their associated RPC and node endpoints.

## Network Details

<Tabs
  defaultValue="mainnet"
  values={[
    { label: 'PoS Mainnet', value: 'mainnet' },
    { label: 'Mumbai Testnet', value: 'mumbai' },
  ]}
>

<TabItem value="mumbai">

The Mumbai Testnet serves as a replica of the Polygon Mainnet and is primarily used for testing. Obtain testnet tokens from the [faucet](https://faucet.polygon.technology/). Note that these tokens hold no value and differ from MATIC.

| Properties       | Network Details                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network Name     | **Mumbai**                                                                                          |
| Parent Chain     | **[Goërli](https://goerli.net/)**                                                                   |
| Chain ID         | `80001`                                                                                            |
| Gas Token        | [MATIC](gas-token)                                                                                  |
| Gas Station      | [Mumbai Gas Station](https://gasstation-mumbai.matic.today/v2)                                       |
| RPC Endpoint     | [https://rpc-mumbai.matic.today](https://rpc-mumbai.matic.today)                                     |
| Node Endpoint    | [wss://rpc-mumbai.matic.today](wss://rpc-mumbai.matic.today)                                        |
| Heimdall API     | [https://heimdall-api-testnet.polygon.technology](https://heimdall-api-testnet.polygon.technology)   |
| Block Explorer   | [https://mumbai.polygonscan.com/](https://mumbai.polygonscan.com/)                                   |

:::note Additional Information

For more details, refer to this [**JSON data**](https://static.polygon.technology/network/testnet/mumbai/index.json).

:::

</TabItem>

<TabItem value="mainnet">

The native token for the Polygon PoS Mainnet is MATIC, which is used for transaction fees.

| Properties       | Network Details                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network Name     | **Polygon**                                                                                         |
| Parent Chain     | **Ethereum**                                                                                        |
| Chain ID         | `137`                                                                                               |
| Gas Token        | MATIC                                                                                               |
| Gas Station      | [PolygonScan Gas Tracker](https://polygonscan.com/gastracker)                                        |
| RPC Endpoint     | [https://polygon-rpc.com/](https://polygon-rpc.com/)                                                |
| Node Endpoint    | [wss://rpc-mainnet.matic.network](wss://rpc-mainnet.matic.network)                                  |
| Heimdall API     | [https://heimdall-api.polygon.technology](https://heimdall-api.polygon.technology)                   |
| Block Explorer   | [https://polygonscan.com/](https://polygonscan.com/)                                                 |

:::note Additional Information

For more details, refer to this [**JSON data**](https://github.com/maticnetwork/static/blob/master/network/mainnet/v1/index.json).

:::

</TabItem>
</Tabs>

## RPC API Methods

Developers can interact with on-chain data and execute various types of transactions using network endpoints. These APIs adhere to the JSON-RPC standard, a stateless, lightweight remote procedure call (RPC) protocol.

:::info Getting Started with RPC Calls

For a comprehensive list of API documentation, visit [**Polygon JSON-RPC calls**](https://edge-docs.polygon.technology/docs/get-started/json-rpc-commands/).

To explore API requests without any setup, fix failing requests, or discover new methods on the Polygon network, try the [**Composer App**](https://composer.alchemyapi.io).

:::

### Infrastructure Providers

Public RPCs may have rate limits or traffic restrictions. For dedicated free RPC URLs, consider the following providers:

- [Alchemy](https://www.alchemy.com/)
- [Allnodes](https://polygon.publicnode.com)
- [Ankr](https://www.ankr.com/)
- [Blast (Bware Labs)](https://blastapi.io/)
- [BlockPI](https://blockpi.io/)
- [BlockSpaces](https://www.blockspaces.com/web3-infrastructure)
- [Chainnodes](https://www.chainnodes.org/)
- [Chainstack](https://chainstack.com/build-better-with-polygon/)
- [DataHub (Figment)](https://datahub.figment.io)
- [GetBlock](https://getblock.io/en/)
- [Infura](https://infura.io)
- [Moralis](https://moralis.io)
- [NodeReal](https://nodereal.io)
- [OnFinality](https://onfinality.io/)
- [Pocket Network](https://www.portal.pokt.network/)
- [QuickNode](https://www.quicknode.com/chains/matic)
- [SettleMint](https://docs.settlemint.com/docs/polygon-connect-to-a-node)
- [Tatum](https://tatum.io/)
- [WatchData](https://docs.watchdata.io/blockchain-apis/polygon-api)
- [NOWNodes](https://nownodes.io/nodes/polygon-matic)
- [Kriptonio](https://kriptonio.com/)
- [Chain49](https://chain49.com/)
- [Chainbase](https://chainbase.com/)
- [Stackup](https://www.stackup.sh/)
- [1RPC](https://1rpc.io/)

For a complete list of public endpoints, visit [Alchemy's Chain Connect](https://www.alchemy.com/chain-connect/chain/polygon-pos) and [Chainlist](https://chainlist.org/?search=Polygon+Mainnet).
