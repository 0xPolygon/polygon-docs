---
comments: true
---

This guide provides an index of network details for the Polygon Amoy testnet and Polygon PoS mainnet, including their associated RPC and node endpoints.

## Network details

### Amoy

The Amoy testnet serves as a replica of the Polygon mainnet and is primarily used for testing. Obtain testnet tokens from the [faucet](https://faucet.polygon.technology/). Note that these test tokens hold no real-world value.

| Properties       | Network details                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network name     | **Amoy**                                                                                           |
| Parent chain     | **Sepolia**                                                                                        |
| Chain ID         | `80002`                                                                                            |
| Gas token        | POL                                                                                              |
| Gas station      | [AMOY gas station](https://gasstation-testnet.polygon.technology/amoy)                             |
| RPC endpoint     | [https://rpc-amoy.polygon.technology/](https://rpc-amoy.polygon.technology/)                       |
| Node endpoint    | [wss://rpc-amoy.polygon.technology/](wss://rpc-amoy.polygon.technology/)                           |
| Heimdall API     | [https://heimdall-api-amoy.polygon.technology](https://heimdall-api-amoy.polygon.technology)       |
| Block Explorer   | [https://amoy.polygonscan.com/](https://amoy.polygonscan.com/)                                     |

!!! info "Additional information"

    For more details, refer to this [**JSON data**](https://static.polygon.technology/network/testnet/amoy/index.json).


### Mainnet

The native token for the Polygon PoS mainnet is MATIC, which is used for transaction fees.

| Properties       | Network details                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network name     | **Polygon**                                                                                        |
| Parent chain     | **Ethereum**                                                                                       |
| Chain ID         | `137`                                                                                              |
| Gas token        | POL                                                                                              |
| Gas station      | [PolygonScan Gas Tracker](https://polygonscan.com/gastracker)                                      |
| RPC endpoint     | [https://polygon-rpc.com/](https://polygon-rpc.com/)                                               |
| Node endpoint    | [wss://rpc-mainnet.matic.network](wss://rpc-mainnet.matic.network)                                 |
| Heimdall API     | [https://heimdall-api.polygon.technology](https://heimdall-api.polygon.technology)                 |
| Block explorer   | [https://polygonscan.com/](https://polygonscan.com/)                                               |


!!! info "Additional information"
    
    For more details, refer to the [JSON data](https://github.com/maticnetwork/static/blob/master/network/mainnet/v1/index.json).

## RPC API methods

Developers can interact with on-chain data and execute various types of transactions using network endpoints. These APIs adhere to the JSON-RPC standard, a stateless, lightweight remote procedure call (RPC) protocol.

!!! info "Getting started with RPC calls"

    For a comprehensive list of API documentation, visit [**Polygon JSON-RPC calls**](https://github.com/0xPolygon/polygon-edge/tree/develop/docs/docs/api).

    To explore API requests without any setup, fix failing requests, or discover new methods on the Polygon network, try the [**Composer App**](https://composer.alchemyapi.io).


## Infrastructure providers

Public RPCs may have rate limits or traffic restrictions. For dedicated free RPC URLs, consider the following providers:

- [Alchemy](https://www.alchemy.com/)
- [Allnodes](https://polygon.publicnode.com)
- [All That Node](https://www.allthatnode.com/polygon.dsrv)
- [Amazon Managed Blockchain](https://aws.amazon.com/managed-blockchain/)
- [Ankr](https://www.ankr.com/)
- [Blast (Bware Labs)](https://blastapi.io/)
- [BlockPI](https://blockpi.io/)
- [Chainnodes](https://www.chainnodes.org/)
- [Chainstack](https://chainstack.com/build-better-with-polygon/)
- [DataHub (Figment)](https://datahub.figment.io)
- [Dwellir](https://www.dwellir.com/networks/polygon)
- [GetBlock](https://getblock.io/en/)
- [Infura](https://infura.io)
- [Moralis](https://moralis.io/nodes/?utm_source=polygon-docs&utm_medium=partner-docs)
- [NodeReal](https://nodereal.io)
- [OnFinality](https://onfinality.io/)
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
- [4EVERLAND](https://docs.4everland.org/rpc-beta/polygon)
- [SubQuery](https://subquery.network/rpc)
- [Validation Cloud](https://app.validationcloud.io)
- [dRPC](https://drpc.org/chainlist/polygon)

For a complete list of public endpoints, visit [Alchemy's Chain Connect](https://www.alchemy.com/chain-connect/chain/polygon-pos) and [Chainlist](https://chainlist.org/?search=Polygon+Mainnet).
