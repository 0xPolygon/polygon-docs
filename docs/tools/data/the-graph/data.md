!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

# Polygon root subgraph introduction

Polygon has a GraphQL API Endpoint hosted by [The Graph](https://thegraph.com/docs/about/introduction#what-the-graph-is) called a subgraph for indexing and organizing data from the Polygon smart contracts.

This subgraph can be used to query on-chain Polygon data. The subgraph data is serviced by a decentralized group of server operators called [Indexers](https://thegraph.com/docs/en/network/indexing/).

The PolygonRoot subgraph works by listening for events emitted by one or more data sources (Smart Contracts) on the various chains. It handles the indexing and caching of data which can later be queried using the GraphQL API Endpoint, providing an excellent developer experience.

## Helpful resources

- [Video tutorial on creating an API Key](https://www.youtube.com/watch?v=UrfIpm-Vlgs).
- [Managing your API Key & setting your indexer preferences](https://thegraph.com/docs/en/studio/managing-api-keys/).
- [Querying from an application](https://thegraph.com/docs/en/developer/querying-from-your-app/).
- [How to use the explorer and playground to query on-chain data](https://medium.com/@chidubem_/how-to-query-on-chain-data-with-the-graph-f8507488215).
- [Explorer page](https://thegraph.com/explorer/).
- GraphQL Endpoint: <https://gateway.thegraph.com/api/[api-key]/subgraphs/id/FDrqtqbp8LhG1hSnwtWB2hE6C97FWA54irrozjb2TtMH>.
- [Code repo](https://github.com/maticnetwork/subgraphs).
