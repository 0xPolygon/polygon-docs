!!! info "Content disclaimer"  

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

# Supra Oracle Integration

**Supra** is a MultiVM Layer 1 network designed for high performance, interoperability, and security. It has achieved over **500,000 transactions per second (TPS)** across **300 nodes** with **sub-second consensus latency**, marking it as one of the fastest and most scalable Layer 1 solutions available. Supra is also the first blockchain to provide full vertical integration of **native oracles, DVRF, bridging, and automation**, enabling developers to build powerful **Super dApps** within a unified ecosystem.

---

## Key Features

### Lightning Fast Speeds
Supra provides near-instant data refresh rates with full on-chain finality, reaching consensus in **600–900 milliseconds**. This makes it one of the **fastest-to-finality oracle networks** available.

### Truly Decentralized
Supra’s oracles are decentralized at every level—from **multi-source data collection** to a **globally distributed node network**—ensuring reliability and trustless data delivery.

### Toughened Security
A randomized node network and built-in fail-safes help **maximize security** and prevent manipulation or downtime.

### Natively Interoperable
Supra is **blockchain agnostic**, offering compatibility with **58+ networks** including **Polygon, Ethereum, Arbitrum, Optimism, Avalanche, and Aptos**, among others.

### Massive Scalability
Supra’s novel consensus mechanism enables **hundreds of thousands of transactions per second** without sacrificing security or decentralization.

---

## Supra Oracle Resources

Explore Supra’s documentation for more information on:

- [**Data Feeds**](#)  
- [**APIs for Real-Time and Historical Data**](#)  
- [**Indices**](#)  

---

# Pull Oracle Integration

Supra’s **Pull Oracle** allows developers to retrieve proof data directly from a gRPC server and interact with smart contracts programmatically.

## Installation

Clone the repository or download the source code, then install the required dependencies:

```bash
npm install
```

## Configuration

Before using the library, configure the parameters in your `main.js` file.

### gRPC Server Address

**Mainnet:**
```
mainnet-dora-2.supra.com:443
```

**Testnet:**
```
testnet-dora-2.supra.com:443
```

### REST Server Address

**Mainnet:**
```
https://rpc-mainnet-dora-2.supra.com
```

**Testnet:**
```
https://rpc-testnet-dora-2.supra.com
```

### Pair Indexes

Set the desired pair indexes as an array (example):

```javascript
const pairIndexes = [0, 21, 61, 49];
```

### Chain Type

Specify the chain type as EVM:

```javascript
const chainType = 'evm';
```

### RPC Configuration

Set the RPC URL for your target blockchain network:

```javascript
const web3 = new Web3(new Web3.providers.HttpProvider('<RPC URL>'));
```

---

## Customization

You can modify the smart contract interaction logic within the `callContract` function.

### Smart Contract ABI

Update the path to your ABI JSON file:

```javascript
const contractAbi = require("../resources/abi.json");
```

### Smart Contract Address

Specify your contract address:

```javascript
const contractAddress = '<CONTRACT ADDRESS>';
```

### Function Call

Modify the function call as per your contract. Example:

```javascript
const txData = contract.methods.GetPairPrice(hex, 0).encodeABI();
```

### Gas Estimation

Estimate gas for your function call:

```bash
const gasEstimate = await contract.methods.GetPairPrice(hex, 0).estimateGas({ from: "<WALLET ADDRESS>" });
```

### Transaction Object

Customize the transaction parameters:

```bash
const transactionObject = {
  from: "<WALLET ADDRESS>",
  to: contractAddress,
  data: txData,
  gas: gasEstimate,
  gasPrice: await web3.eth.getGasPrice()
};
```

### Private Key Signing

Sign the transaction using your private key:

```bash
const signedTransaction = await web3.eth.accounts.signTransaction(transactionObject, "<PRIVATE KEY>");
```

---

## Running the Application

To start the application and initiate proof data fetching, run:

```bash
node main.js
```

This will retrieve data from Supra’s servers and interact with your smart contract using the defined configurations.

---

# Push Oracle Integration

Supra’s **Push Oracle** enables on-chain access to real-time data feeds (S-Values) through Solidity interfaces.

## Step 1: Create the S-Value Interface

Add the following code to your contract to define the data structures and functions needed to retrieve S-Values:

```solidity
pragma solidity 0.8.19;

interface ISupraSValueFeed {
    struct priceFeed {
        uint256 round;
        uint256 decimals;
        uint256 time;
        uint256 price;
    }

    struct derivedData {
        int256 roundDifference;
        uint256 derivedPrice;
        uint256 decimals;
    }

    function getSvalue(uint256 _pairIndex) external view returns (priceFeed memory);

    function getSvalues(uint256[] memory _pairIndexes) external view returns (priceFeed[] memory);

    function getDerivedSvalue(uint256 pair_id_1, uint256 pair_id_2, uint256 operation)
        external
        view
        returns (derivedData memory);

    function getTimestamp(uint256 _tradingPair) external view returns (uint256);
}
```

---

## Step 2: Configure the S-Value Feed Address

Initialize the S-Value feed contract in your smart contract constructor:

```solidity
contract ISupraSValueFeedExample {
    ISupraSValueFeed internal sValueFeed;

    constructor() {
        sValueFeed = ISupraSValueFeed(0xE92D276bBE234869Ecc9b85101F423c6bD26654A);
    }
}
```

*Note: Replace the above address with the correct network-specific Supra contract address.*

---

## Step 3: Retrieve the S-Value Data

Use the following functions to fetch single or multiple S-Values and to derive new data pairs.

```solidity
function getPrice(uint256 _priceIndex)
    external
    view 
    returns (ISupraSValueFeed.priceFeed memory)
{
    return sValueFeed.getSvalue(_priceIndex);
}

function getPriceForMultiplePair(uint256[] memory _pairIndexes)
    external
    view
    returns (ISupraSValueFeed.priceFeed[] memory)
{
    return sValueFeed.getSvalues(_pairIndexes);
}

function getDerivedValueOfPair(uint256 pair_id_1, uint256 pair_id_2, uint256 operation)
    external
    view
    returns (ISupraSValueFeed.derivedData memory)
{
    return sValueFeed.getDerivedSvalue(pair_id_1, pair_id_2, operation);
}
```

---

## Recommended Best Practices

Implement an **access-controlled function** to update the Supra feed contract address for future upgrades:

```solidity
function updateSupraSvalueFeed(ISupraSValueFeed _newSValueFeed)
    external
    onlyOwner
{
    sValueFeed = _newSValueFeed;
}
```

This approach ensures your contract remains upgradeable while maintaining secure access control over Oracle configurations.

---

By integrating **Supra Oracles**, developers gain access to a high-speed, decentralized, and secure data layer—purpose-built for real-world use cases across DeFi, gaming, and Web3 applications.
