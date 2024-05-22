The ability of a blockchain to exchange data with other blockchains is crucial for its participation in a broader ecosystem, a concept known as Interoperability. Various solutions have been developed to enable interoperability, each offering unique advantages and disadvantages.

The Polygon team has developed an interoperability solution in the form of a bridge for the Polygon zkEVM network. This zkEVM bridge facilitates communication and asset migration between the Polygon zkEVM network and other networks, such as the L1 (Ethereum Mainnet) or any L2 built on Ethereum.

The ability to transfer an asset from one network to another without altering its value or functionality is crucial for users. Additionally, cross-chain messaging is supported, enabling the exchange of payloads between networks.

In zk-rollups like the Polygon zkEVM, L1 smart contracts manage L2 state transitions and data availability. Consequently, with a well-designed L2 architecture, both ends of the bridge smart contract (SC) can be fully synchronized through the logic of the smart contract.

## zkEVM bridge schema

To better understand the zkEVM bridge protocol design, let's use an analogy. Refer to the illustration below for a clearer explanation of the protocol.

![Polygon zkEVM bridge Schema](../../../../img/zkEVM/01pzb-polygon-zkevm-schema.png)

Consider two networks, L1 and L2. To bridge an asset between L1 and L2, a user must lock the asset on the origin network (L1). The bridge smart contract then mints an equivalent representative asset on the destination network (L2). This minted asset is called a Wrapped Token.

Once minting is complete, the asset can be claimed by the user or recipient in the destination network (L2).

The operation can also be performed in reverse. After burning the Wrapped Token, the bridge smart contract unlocks the original asset on the origin network.

As mentioned earlier, there is also a third option where the bridge smart contract facilitates cross-chain messaging. This allows data payloads to be sent from one network to another using the bridge smart contract's Bridge and Claim operations.

## Comparing with Ethereum 2.0 deposit contract

The zkEVM bridge smart contract is built upon the Ethereum 2.0 deposit contract with some modifications.

For instance, it employs custom append-only Merkle trees but follows the same logic as the Ethereum 2.0 deposit contract.

Other differences are related to the base hash and the leaf nodes.

First, the deposit contract uses SHA256, whereas the zkEVM employs the Keccak hash function. And it's all because, in addition to being EVM-compatible, the Keccak hash function is less expensive in terms of Ethereum gas fees.

Second, the bridge SC generates wrapped tokens the first time a new token is added to the zkEVM network. In addition, the metadata of the ERC20 token, such as the name, decimal, or symbol, is added to the information contained in the leaf.

As a result, as stated in this document, every transfer is protected by smart contracts.

## Features

The Polygon zkEVM bridge smart contract's main feature is the use of Exit Trees and the Global Exit Tree, with the Global Exit Tree Root serving as the primary source of state truth.

The use of two distinct Global Exit Root managers for L1 and L2, as well as separate logic for the bridge SC and each of these Global Exit Root managers, allows for extensive network interoperability.

Meanwhile, all asset transfers can be validated by any L1 and L2 nodes due to data availability.

The sections that follow explain how the Polygon zkEVM bridge-related smart contracts ensure the security of assets transferred between the zkEVM and any network.