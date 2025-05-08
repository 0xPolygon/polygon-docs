!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

**Chainlink** enables your contracts to **access any external data source**, through a decentralized oracle network. Whether your contract requires sports results, the latest weather, or any other publicly available data, Chainlink provides the tools required for your contract to consume it.

## Decentralized data

One of Chainlink's most powerful features is already decentralized, aggregated, and ready to be digested on-chain data on most of the popular cryptocurrencies. These are known as [**Chainlink Data Feeds**](https://docs.chain.link/docs/using-chainlink-reference-contracts).

Here is a working example of a contract that pulls the latest price of POL in USD on the Amoy Testnet.

All you need to do is swap out the address [with any address of a data feed](https://docs.chain.link/docs/matic-addresses#config) that you wish, and you can start digesting price information.

```solidity
pragma solidity ^0.8.26;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract PriceConsumerV3 {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Amoy Testnet
     * Aggregator: POL/USD
     * Address: 0x001382149eBa3441043c1c66972b4772963f5D43
     */
    constructor() public {
        priceFeed = AggregatorV3Interface(0x001382149eBa3441043c1c66972b4772963f5D43);
    }

    /**
     * Returns the latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            uint80 roundID,
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return price;
    }
}
```
