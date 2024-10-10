## Introduction

In this document, we provide an overview of the backend architecture and functionalities of the Bridge API service that supports the Polygon Unified Bridge UI, also known as [Polygon Portal](https://portal.polygon.technology/).

The Unified Bridge API offers a unified interface for tracking and managing bridge transactions across the various chains in Polygon network and Ethereum, indexing data from Polygon PoS, Polygon zkEVM, and other CDK chains, including testnets and mainnets, into a cohesive user experience.

This document details the architecture, endpoints, and components of the Bridge API service, and provides guidelines for running the auto-claim script, which automates the process of claiming assets on destination chains, thereby simplifying user interactions and reducing transaction costs.

## Bridge API architecture

Bridge API is the backend service that powers the [Portal UI](https://portal.polygon.technology/). The API helps track user bridge transaction status in real time and provides details such as transaction ID, status, and time.

The Bridge API indexes data from Polygon PoS, Polygon zkEVM, Polygon CDK chains, and Ethereum, along with their corresponding testnets, and presents it to the UI in a unified manner. This makes Bridge API a comprehensive service for all Polygon chains, just like the current Bridge UI.

![Bridge API architecture](../../img/cdk/bridge-api-service.png)

The Unified Bridge API is powered by the [chain indexer framework](../../tools/chain-indexer-framework/overview.md). The chain indexer's data pipeline consists of three main components:

### Producer

To index data, the producer reads raw blockchain data from a specific chain and writes it to an [Apache Kafka](https://kafka.apache.org/documentation/) queue, indexing all data in a specific block.  

The indexed data can be used for various purposes, including bridge transactions.

!!! info "Reorg handling"

    Chain reorgs are handled at the producer level if the reorg height is less than 256 blocks. For reorgs exceeding 256 blocks, a manual resync is required.

### Transformer

The transformer actively monitors specific topics on the Kafka queue and transforms the incoming data into a different format. 

For the bridge service use case, the transformer filters bridge and claim events from the producer, transforms the information into a more readable format, and sends it back to the relevant Kafka topic.

### Consumer

This component consumes the transformed data from the queue and writes it into a database, making it accessible to users via API endpoints.

### Deploying the components

The infrastructure for all three components needs to be deployed for each chain. This means that every new CDK chain must have a new producer, transformer, and consumer. Once these components are deployed, the API endpoints can start exposing data for the respective chain. 

## Endpoints

The endpoints are common for all CDK chains. 

### Network IDs

Transaction data belonging to a specific chain is identified using either the `destinationNetwork` and `sourceNetwork` parameters which are included in every endpoint response. 

- ETH = 0
- zkEVM = 1
- CDK chains = >1 (including testnets) 

### Transactions API

This API manages the details of a bridge transactions initiated from, or incoming to, a user’s `walletAddress`. Details include the real-time status, the bridged token, transaction amount, source chain, and destination chain, etc. For example:

- Testnet: [https://api-gateway.polygon.technology/api/v3/transactions/testnet?userAddress=](https://api-gateway.polygon.technology/api/v3/transactions/testnet?userAddress=)`walletAddress`
- Mainnet: [https://api-gateway.polygon.technology/api/v3/transactions/mainnet?userAddress=](https://api-gateway.polygon.technology/api/v3/transactions/mainnet?userAddress=)`walletAddress`
    
!!! tip
    - Additional filtering can be performed on the transactions API by including the `sourceNetworkIds` and `destinationNetworkIds` query parameters.
    
### Merkle proof API

This API manages the payload needed to process claims on the destination chain. For example:

- Testnet: [https://api-gateway.polygon.technology/api/v3/merkle-proof/testnet?networkId=](https://api-gateway.polygon.technology/api/v3/merkle-proof/testnet?networkId=sourceNetworkId&depositCount=depositCount)`[sourceNetworkId](https://bridge-api-mainnet-dev.polygon.technology/merkle-proof?networkId=1&depositCount=1)`[&depositCount=](https://api-gateway.polygon.technology/api/v3/merkle-proof/testnet?networkId=sourceNetworkId&depositCount=depositCount)`[depositCount](https://bridge-api-mainnet-dev.polygon.technology/merkle-proof?networkId=1&depositCount=1)`
- Mainnet: [https://api-gateway.polygon.technology/api/v3/merkle-proof/mainnet?networkId](https://api-gateway.polygon.technology/api/v3/merkle-proof/mainnet?networkId)[=`sourceNetworkId`&depositCount=`depositCount`](https://bridge-api-mainnet-dev.polygon.technology/merkle-proof?networkId=1&depositCount=1)
    
!!! tip
    - Use the Transactions API to get `sourceNetworkId` and `depositCount` data for a given bridge transaction. 
    
## Onboarding a new CDK

New CDK implementation providers must supply the following mandatory parameters:

- Public RPC
- Chain ID
- Chain name
- Chain logo
- Dedicated RPC: This is _really important_ as the indexer requires it to index all data coming from the CDK chain.
- Block explorer URL
- Bridging contracts address

!!! important
    - The above are mandatory expectations from any CDK implementation provider. 
    - At the time of writing, the Polygon Labs team coordinates additional steps for full implementation.

## Deeper dive into the bridging workflow

To understand why the API requires the mandatory onboarding parameters, let's examine the workflow of the Unified Bridge API and some of the components it interacts with.

### `lxly.js` client library 

The [LxLy SDK](https://www.npmjs.com/package/@maticnetwork/lxlyjs) is a JavaScript library that provides pre-built functions required for interacting with the bridge contracts on Polygon network.

To initialize the SDK, you'll need the bridge contract address, RPC, and network ID. The library provides methods to perform most operations, such as type conversion, formatting, and error handling, making it easy for developers to invoke bridge, claim, and other functions. The LxLy SDK is compatible with any LxLy-enabled chain, requiring no additional modifications.

The SDK can be used for any compatible chain with no additional changes. 

#### Common use cases

Cross-chain token bridging and message passing from:

- L1 to L2 (e.g. Ethereum to CDK L2 chain).
- L2 to L2 (e.g. zkEVM to CDK L2 chain).
- L2 to L1 (e.g. CDK L2 chain to Ethereum).

### Unified Bridge API

The backend service, [as discussed earlier](#bridge-api-architecture), indexes data from different chains and powers the Portal UI.

The repository to spin up this service is not yet open source and is currently managed by the Polygon Labs team. The code is expected to be open source soon, at which time all participants will manage their own deployments.

### Gas station 

In order to estimate the gas price before submitting the transactions, we use the [Polygon gas station](../../tools/gas/polygon-gas-station.md), a lightweight service which gets gas price estimates for a specific chain.

The gas station is currently maintained by the Polygon Labs team, but can be hosted by anyone as the [code is open source](https://github.com/maticnetwork/maticgasstation).

### Token list

This is a [JSON-formatted list](https://api-polygon-tokens.polygon.technology/tokenlists/polygon.tokenlist.json) containing metadata for all supported tokens. 

It automatically updates with new token details whenever one is bridged for the first time. However, logos or other metadata types need to be added or updated via a PR to the [token list repo](https://github.com/maticnetwork/polygon-token-list). 

### Balance API

This service relies on a [balance scanner contract](https://github.com/MyCryptoHQ/eth-scan) deployed on each chain. 

The contract fetches the balance from multiple ERC20 tokens in one single batch call and returns them. Token balance is processed with a price-feed service which attaches the USD value of the tokens before sending to the UI. 

### Merkle proof generation API

This is used to process claims on L1 and L2. 

The service can be accessed via the Unified Bridge API endpoint. It relies on the indexed bridge events and Merkle tree data to generate the Merkle proof required to process claims on L1/L2. 

### The auto-claim script

This automated script monitors the Bridge API for unprocessed claims on a specific chain and automatically submits `claimAsset` transactions to ensure tokens are claimed on the destination chain without requiring user intervention. Thus, users don’t need to perform any extra steps or pay additional transaction gas fees to receive their tokens. 

While not mandatory, this service is crucial for a seamless bridging experience. The script will be open-sourced, and CDK chains will be deploying and running their own instances of the service.

!!! tip "CDK chain onboarding"

    Initially, CDK chains only need to deploy the auto-claim script. The instructions for this are available in the next section. The Polygon team will deploy all other services, including the Bridge API.

## How to run the auto-claim script

The auto-claim script is a Cron job service that automates the second step of LxLy bridge transactions. It checks the Bridge API for unclaimed transactions, retrieves Merkle proof payloads, and submits `claimAsset` transactions on the destination chain, including retries and error handling to ensure reliability.

After cloning the [auto-claim service repo](https://github.com/0xPolygon/auto-claim-service), install dependencies and simply configure the endpoint URLs in the script's settings. Detailed deployment instructions for each CDK chain are available in the [README.md file of the auto-claim repo](https://github.com/0xPolygon/auto-claim-service/blob/main/README.md).