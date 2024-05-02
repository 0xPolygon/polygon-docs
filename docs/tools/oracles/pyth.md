## Overview

The [Pyth network](https://pyth.network/) is the largest first-party financial oracle network, delivering real-time market data to over 40 blockchains securely and transparently.

The network comprises some of the world’s largest exchanges, market makers, and financial services providers publishing their proprietary price-data on-chain for aggregation and distribution to smart contract applications.

## Using Pyth network
                                                                                       
The Pyth Network introduced an innovative low-latency [pull oracle design](https://docs.pyth.network/documentation/pythnet-price-feeds/on-demand), where users are empowered to “pull” price updates on-chain when needed, enabling everyone in that blockchain environment to access that data point. 

Developers on Polygon have permissionless access to any of Pyth’s 350+ price feeds for equities, ETFs, commodities, foreign exchange pairs, and cryptocurrencies.

Here is a working example of a contract that fetches the latest price of MATIC/USD on the Polygon mainnet. 
You have to pass [Pyth's contract address](https://docs.pyth.network/price-feeds/contract-addresses/evm) of Polygon mainnet/mumbai and the desired [price feed](https://pyth.network/developers/price-feed-ids) id](https://pyth.network/developers/price-feed-ids) to fetch the latest price

```solidity 
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract MyFirstPythContract {
    IPyth pyth;

    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    function fetchPrice(
        bytes[] calldata pythPriceUpdate,
        bytes32 priceFeed
    ) public payable returns (int64) {
        uint updateFee = pyth.getUpdateFee(pythPriceUpdate);
        pyth.updatePriceFeeds{value: updateFee}(pythPriceUpdate);

        // Fetch the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeed);
        return price.price;
    }
}

```

Here you can fetch the `updateData` from our [`Hermes`](https://docs.pyth.network/price-feeds/pythnet-price-feeds/hermes), which listens to Pythnet and Wormhole for price updates or you can use [`pyth-evm-js`](https://github.com/pyth-network/pyth-crosschain/blob/main/target_chains/ethereum/sdk/js/src/EvmPriceServiceConnection.ts#L15) sdk. 


This [package](https://github.com/pyth-network/pyth-crosschain/tree/main/target_chains/ethereum/sdk/solidity) provides utilities for consuming prices from the Pyth Network Oracle using Solidity. Also, it contains the [Pyth Interface ABI](https://github.com/pyth-network/pyth-crosschain/blob/main/target_chains/ethereum/sdk/solidity/abis/IPyth.json) that you can use in your libraries to communicate with the Pyth contract.

It is strongly recommended to follow the consumer's [best practices](https://docs.pyth.network/documentation/pythnet-price-feeds/best-practices) when consuming Pyth data. 

For more information and details, please refer to the official documentation [here](https://docs.pyth.network/price-feeds).

You can find more details on the various functions available to you when interacting with the Pyth smart contract in the [API Reference section](https://docs.pyth.network/price-feeds/api-reference/evm).

## Pyth on Polygon

The Pyth Network smart contract is available at the following address: 

- Mainnet: [0xff1a0f4744e8582DF1aE09D5611b887B6a12925C](https://polygonscan.com/address/0xff1a0f4744e8582df1ae09d5611b887b6a12925c).
- Mumbai: [0xFC6bd9F9f0c6481c6Af3A7Eb46b296A5B85ed379](https://mumbai.polygonscan.com/address/0xFC6bd9F9f0c6481c6Af3A7Eb46b296A5B85ed379)

Additionally, you'll be able to find all the Pyth Price Feed IDs [here](https://pyth.network/developers/price-feed-ids). Be sure to select the correct environment as mainnet and testnet price feed IDs differ.

## Other

The Pyth Network provides additional tools to developers like this [TradingView Integration](https://docs.pyth.network/guides/how-to-create-tradingview-charts) or the [Gelato Web3 Functions](https://docs.pyth.network/guides/how-to-schedule-price-updates-with-gelato).  

If you have any questions or issues, you can contact us on the following platforms: [Telegram](https://t.me/Pyth_Network), [Discord](https://discord.gg/invite/PythNetwork), [Website](https://pyth.network/contact).