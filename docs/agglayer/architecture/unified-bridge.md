# Unified Bridge

## Overview

The unified bridge (prev. LxLy bridge) is the common access point for chains connected to the Agglayer. Along with the pessimistic proof, it is one of two core components of the Agglayer.

The unified bridge consists of two main components:
- **On-Chain Smart Contracts**: Maintain the data structures related to chain states, cross-chain transactions, and the Agglayer’s Global Exit Root.
- **Off-Chain Services & Tooling**: APIs and indexing frameworks for interacting with the bridge.

## Bridge Smart Contracts

The unified bridge is responsible for maintaining the data structures related to chain states, cross-chain transactions, and the Agglayer’s Global Exit Root, ensuring cross-chain transactions are indeed finalized on the L1 before they can be claimed. The smart contracts are as follows:

| Contract | Functions | Deployed on |
|----------|------------|--------------|
| `PolygonRollupManager.sol` | Responsible for creating, updating, and verifying rollups, validiums, and sovereign chains built with Polygon CDK | L1 |
| `PolygonZkEVMBridgeV2.sol` | Responsible for bridging and claiming assets or messages across L1 and L2 chains | L1 & L2 |
| `PolygonZkEVMGlobalExitRootV2.sol` | Maintains the Global Exit Root, which represents the complete state of all exit data from chains connected through the Agglayer | L1 & L2 |

## Unified Bridge: Data Structures

### Local Exit Root & Local Index
- All cross-chain transactions using the unified bridge are recorded in a **Sparse Merkle Tree** called the **Local Exit Tree**.
- Each Agglayer-connected chain updates its own **Local Exit Tree**, maintained in `PolygonZkEVMBridgeV2.sol` on the L2.
- The **Local Exit Root** is the root of the Local Exit Tree, a binary tree with a height of 32, updated each time a new cross-chain transaction is initiated.
- The **Local Root Index** is the index of the leaf node, which is a hash of cross-chain transactions such as `bridgeAsset` / `bridgeMessage`.

### Rollup Exit Root
- Once a chain updates its **Local Exit Tree** in `PolygonRollupManager.sol`, the contract updates the chain’s **Local Exit Root**.
- Each time a chain’s Local Exit Root is updated, the **Rollup Exit Root** is also updated.
- The **Rollup Exit Root** is the Merkle root of all Local Exit Roots.
- Any update to the Rollup Exit Root triggers an update of the **Global Exit Root**, which is maintained in `PolygonZkEVMGlobalExitRootV2.sol` on the L1.

### Mainnet Exit Root
- Functionally similar to the **Local Exit Root**, but it tracks the bridging activities of L1 to all chains connected through the Agglayer.
- When the **Mainnet Exit Root** is updated in `PolygonZkEVMBridgeV2.sol`, the contract then updates `mainnetExitRoot` in `PolygonZkEVMGlobalExitRootV2.sol`.

### Global Exit Root, L1 Info Tree, Global Index
- **Global Exit Root** is the hash of the **Rollup Exit Root** and **Mainnet Exit Root**.
- When a new **Rollup Exit Root** or **Mainnet Exit Root** is submitted, the contract appends the new **Global Exit Root** to the **L1 Info Tree**.
- **L1 Info Tree** is a **Sparse Merkle Tree** that maintains Global Exit Roots. It is a binary tree with a height of 32, updated every time a new Global Exit Root is submitted.
- **Global Index** is a **256-bit string** used to locate the unique leaf in the latest **Global Exit Tree** when creating and verifying SMT proofs.

## Bridge Service

### Chain Indexer Framework
- An EVM blockchain data indexer that parses, sorts, and organizes blockchain data for the **Bridge Service API**.
- Each Agglayer-connected chain has its own indexer instance.

### Transaction API
- Provides details of a bridge transaction initiated by or incoming to a user’s wallet address.

**API Endpoints:**
- **Testnet:**  
  `https://api-gateway.polygon.technology/api/v3/transactions/testnet?userAddress={userAddress}`
- **Mainnet:**  
  `https://api-gateway.polygon.technology/api/v3/transactions/mainnet?userAddress={userAddress}`

### Proof Generation API
- Generates the **Merkle proof payload** needed to process claims on the destination chain.

**API Endpoints:**
- **Testnet:**  
  `https://api-gateway.polygon.technology/api/v3/proof/testnet/merkle-proof?networkId={sourceNetworkId}&depositCount={depositCount}`
- **Mainnet:**  
  `https://api-gateway.polygon.technology/api/v3/proof/mainnet/merkle-proof?networkId={sourceNetworkId}&depositCount={depositCount}`

## Tools

### Claimer
- Any network participant may complete the bridging process by becoming a **claimer**.
- The **claim service** can be deployed by dApps, chains, or any individual end-user.
- An **auto-claiming script** automates the claim process on the destination chain.

### Lxly.js
- A JavaScript library with prebuilt functions for interacting with the **Unified Bridge contracts**.

## Security of the Unified Bridge

### Secured by Ethereum
- All cross-chain transactions are **settled on Ethereum** before they can be claimed on the destination chain.

### Secured by Mathematics
- Once the source chain bridging transaction is finalized on Ethereum, the destination chain verifies the proof to confirm validity.

### Immutable Data Packaging
- The **source chain specifies** the destination network, address, and transfer amount.
- The transaction is bundled into an immutable cross-chain package, ensuring:
  - Assets cannot be claimed on an incorrect network.
  - Assets cannot be claimed to an incorrect address.
  - Assets cannot be claimed in excess of the transferred amount.

### Secured by Access Control
- The bridge contract can only mint, burn, or transfer assets through **user-initiated transactions**.
- There is **no administrative control** over assets locked in the bridge contract.
- The actual movement of tokens is strictly controlled by **cryptographic proofs** and **mathematical constraints**.
