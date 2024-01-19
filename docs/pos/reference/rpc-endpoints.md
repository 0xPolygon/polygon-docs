This guide provides an index of network details for the Polygon Mumbai Testnet and Polygon PoS Mainnet, including their associated RPC and node endpoints.

## Network details

### Mumbai

The Mumbai testnet serves as a replica of the Polygon mainnet and is primarily used for testing. Obtain testnet tokens from the [faucet](https://faucet.polygon.technology/). Note that these tokens hold no value and differ from MATIC.

| Properties       | Network details                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network name     | **Mumbai**                                                                                          |
| Parent chain     | **[Goërli](https://goerli.net/)**                                                                   |
| Chain ID         | `80001`                                                                                            |
| Gas token        | MATIC                                                                                  |
| Gas station      | [Mumbai gas station](https://gasstation-testnet.polygon.technology/v2)                                       |
| RPC endpoint     | [https://rpc-mumbai.matic.today](https://rpc-mumbai.matic.today)                                     |
| Node endpoint    | [wss://rpc-mumbai.matic.today](wss://rpc-mumbai.matic.today)                                        |
| Heimdall API     | [https://heimdall-api-testnet.polygon.technology](https://heimdall-api-testnet.polygon.technology)   |
| Block Explorer   | [https://mumbai.polygonscan.com/](https://mumbai.polygonscan.com/)                                   |

!!!note
    Additional information

    For more details, refer to this [**JSON data**](https://static.polygon.technology/network/testnet/mumbai/index.json).


### Mainnet

The native token for the Polygon PoS mainnet is MATIC, which is used for transaction fees.

| Properties       | Network details                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network name     | **Polygon**                                                                                         |
| Parent chain     | **Ethereum**                                                                                        |
| Chain ID         | `137`                                                                                               |
| Gas token        | MATIC                                                                                               |
| Gas station      | [PolygonScan Gas Tracker](https://polygonscan.com/gastracker)                                        |
| RPC endpoint     | [https://polygon-rpc.com/](https://polygon-rpc.com/)                                                |
| Node endpoint    | [wss://rpc-mainnet.matic.network](wss://rpc-mainnet.matic.network)                                  |
| Heimdall API     | [https://heimdall-api.polygon.technology](https://heimdall-api.polygon.technology)                   |
| Block explorer   | [https://polygonscan.com/](https://polygonscan.com/)                                                 |

!!!note
    Additional information

    For more details, refer to this [**JSON data**](https://github.com/maticnetwork/static/blob/master/network/mainnet/v1/index.json).


</TabItem>
</Tabs>

## RPC API methods

Developers can interact with on-chain data and execute various types of transactions using network endpoints. These APIs adhere to the JSON-RPC standard, a stateless, lightweight remote procedure call (RPC) protocol.

!!!info
    Getting started with RPC calls

    For a comprehensive list of API documentation, visit [**Polygon JSON-RPC calls**](https://github.com/0xPolygon/polygon-edge/tree/develop/docs/docs/api).

    To explore API requests without any setup, fix failing requests, or discover new methods on the Polygon network, try the [**Composer App**](https://composer.alchemyapi.io).


### Infrastructure providers

Public RPCs may have rate limits or traffic restrictions. For dedicated free RPC URLs, consider the following providers:

- [Alchemy](https://www.alchemy.com/)
- [Allnodes](https://polygon.publicnode.com)
- [Ankr](https://www.ankr.com/)
- [Blast (Bware Labs)](https://blastapi.io/)
- [BlockPI](https://blockpi.io/)
- [Chainnodes](https://www.chainnodes.org/)
- [Chainstack](https://chainstack.com/build-better-with-polygon/)
- [DataHub (Figment)](https://datahub.figment.io)
- [GetBlock](https://getblock.io/en/)
- [Infura](https://infura.io)
- [Moralis](https://moralis.io)
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

For a complete list of public endpoints, visit [Alchemy's Chain Connect](https://www.alchemy.com/chain-connect/chain/polygon-pos) and [Chainlist](https://chainlist.org/?search=Polygon+Mainnet).
