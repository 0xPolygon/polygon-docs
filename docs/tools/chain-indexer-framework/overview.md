---
comments: true
---

!!! info "Git repo and contact details"
    - For details about the technical architecture and if you want to contribute, head over to the repo https://github.com/0xPolygon/chain-indexer-framework
    - For any questions, reach out to us on the [Polygon R&D Discord](https://discord.com/invite/0xpolygonrnd).

## Overview & problem statement

The Chain Indexer Framework is a powerful blockchain data indexer framework designed for the development of flexible event-driven data pipelines on EVM blockchains. Built on the reliable foundation of Kafka, the Chain Indexer Framework empowers developers to build robust and scalable applications that seamlessly process blockchain events and enable real-time data integration.

The Chain Indexer Framework revolutionizes the way developers interact with blockchain data, offering a fast, secure, and efficient method for data retrieval. By choosing the Chain Indexer Framework you are not just selecting a tool, but opting for a more streamlined and efficient development process for your dApps. 

Before we get into the details, let us understand why we need it and the problem it solves.

### 1. What is an EVM blockchain data indexer?

An EVM [Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/) blockchain data indexer is a specialised search engine for EVM-based blockchains like Ethereum and Polygon protocols. It sorts and organises blockchain data, making it faster and easier for developers to query and retrieve specific information for their decentralised applications (dApps).

### 2. Why do dApps need a blockchain data indexer?

Without a data indexer like Chain Indexer Framework, querying blockchain data can be cumbersome and slow. Traditional methods require developers to sift through enormous volumes of transaction records, smart contracts, and other types of data. This is like trying to find a single paragraph in an entire library of uncategorized books. Chain Indexer Framework makes this process fast and efficient, acting as a digital librarian that quickly retrieves the specific data the user is looking for.

!!! info "An helpful analogy"
    
    Imagine that a blockchain is like a massive public library, and each book in the library represents a block of transactions. Now, think of an EVM-based dApp as a researcher who needs specific pieces of information from multiple books in this huge library for their project. Without a catalog or librarian, this researcher would spend an enormous amount of time locating what they need.
    
    A blockchain data indexer like Chain Indexer Framework acts as both the catalog system and the super-efficient librarian for this library. It knows exactly where each "book" is located and can instantly pinpoint the specific "page" you need. The indexer saves the researchers (dApps) valuable time and resources, allowing them to focus on their main project instead of getting bogged down with the cumbersome task of data retrieval.

### 3. Why is it hard to build a blockchain data indexer?

The development complexity in building a blockchain data indexer arises from the need to integrate a diverse software stack that often includes databases, queueing systems, and caching layers. Ensuring real-time performance, handling data consistency during blockchain forks, and adapting to protocol changes add to the complexity. Rigorous testing is essential to validate the indexer under various scenarios, making it a challenging endeavour that requires expertise in multiple domains. Things get more complicated in the multi-chain world.

## The solution: Chain Indexer Framework

The Chain Indexer Framework is a powerful developer framework designed to index raw blockchain data, which can later be utilized by developers to build the backend layers of their decentralized applications (dApps) based on their specific dApp logic. Think of the Chain Indexer Framework as a tool that helps you construct the "Search Engine" for blockchain data; it indexes, categorizes, and makes data to be quickly and cost-effectively accessible to developers. Chainflow brings the power of advanced data indexing to dApps, simplifying and accelerating the process of fetching the data developers need.

!!! note
    The Chain Indexer Framework is a tool that gathers information from a blockchain and channels it into a data stream known as Kafka. However, such data is raw, and not yet ready for use. It must therefore be transformed and stored in a database like Postgres or MongoDB. Only then can a decentralized application (dApp) utilize it. Chainflow provides the framework/tools that enable developers to transform the raw data based on their individual dApp requirements.

In short, the Chain Indexer Framework handles the tedious task of collecting and preparing blockchain data for developers. Afterward, developers will need to build specific features for their app, such as how to use the data. Chain Indexer Framework offers foundational logic and helper functions that make the task much easier.

### How does Chain Indexer Framework work?

Chain Indexer Framework employs a combination of caching, distributed architecture, and advanced algorithms to quickly retrieve the data a dApp might require. It takes raw blockchain data, indexes it, and helps to convert it into easily accessible formats that developers can query using simple APIs.

Initially, Chain Indexer Framework obtains the raw blockchain data via blockchain RPC and stores it in a Kafka stream. It provides the core logic and helper functions needed to transform this raw data. Additionally, it allows you to consume the data from the Kafka stream and stores it in a separate database. Developers can then host the APIs for their dApp on top of this database.

## Features & benefits

### Why choose Chain Indexer Framework?

1. **Open source:** Anyone can fork, modify, and host the software on their own infrastructure. Unlike common third-party indexers, Chain Indexer Framework offers complete control to developers, enabling them to monitor the service closely in order to identify and resolve issues.
2. **Cost savings:** developers can save money otherwise spent on third-party data indexers. There will be no restrictions on usage or API rate limits, as developers will host the service themselves.
3. **Built using TypeScript:** This developer-friendly programming language makes it easy to understand the code and implement changes. Chain Indexer Framework can be easily installed by downloading the NPM package and integrating it into your project.
4. **One-time effort for indexing historical blocks:** Once the raw blockchain data is indexed, developers can build an unlimited number of application layers on top of it. There will be no need to make RPC calls to re-index historical blocks, as they will already be available in the Kafka Data Warehouse.
5. **Modular architecture:** Chain Indexer Framework features a modular architecture, simplifying debugging and bug-fixing processes for developers.
6. **Instant query:** Imagine a customer walking into your retail store and asking for a specific product. If your inventory is well-organized, you can instantly determine whether the item is in stock and where it is located. Chain Indexer Framework enables similar real-time data queries, making it easier for dApps to access and utilize blockchain data.
7. **Event-triggered actions:** Consider how online stores send customers notifications when an item is back in stock. Chain Indexer Framework can establish event triggers for specific blockchain activities, allowing dApps to automatically execute actions such as sending notifications or updating the user-interface.
8. **Customization:** Just as some stores need to track perishable items differently from non-perishable ones, dApps often have unique data requirements. Chain Indexer Framework’s flexible architecture allows developers to customize data pipelines to meet their specific needs.
9. **Scalability:** A small retail store might initially work with manual sorting, but as the business expands, automation becomes essential. Chain Indexer Framework can scale alongside your dApp's growth, handling increased data loads without sacrificing performance.
10. **Improved User Experience:** Nothing frustrates a customer more than slow or unresponsive service. By providing faster and more reliable access to blockchain data, Chain Indexer Framework helps dApps offer a smoother, more responsive user experience.

### Popular use cases

1. **Wallet services**: Blockchain indexers can help wallet providers offer more features like transaction history, balance history, and real-time updates.
2. **dApp backend**: dApps often require real-time access to contract events, token transactions, and other on-chain activities. A data indexer can speed up this process considerably.
3. **Analytics and monitoring**: Firms specializing in blockchain analytics use indexers to monitor activities like fraudulent transactions, smart contract interactions, and trends in token transfers.
4. **Cross-chain services**: For cross-chain swaps or interactions, indexers can offer data that facilitates more seamless integrations.
5. **Oracles**: Data indexers can support oracles by providing them with a more efficient way to access specific data points on the blockchain.
6. **NFT marketplaces**: To track ownership changes, price histories, and various attributes of NFTs, data indexers are often used in the backend.