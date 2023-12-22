!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

**Chainlink** enables your contracts to **access any external data source**, through a decentralized oracle network. Whether your contract requires sports results, the latest weather, or any other publicly available data, Chainlink provides the tools required for your contract to consume it.

## Decentralized data

One of Chainlink's most powerful features is already decentralized, aggregated, and ready to be digested on-chain data on most of the popular cryptocurrencies. These are known as [**Chainlink Data Feeds**](https://docs.chain.link/docs/using-chainlink-reference-contracts).

Here is a working example of a contract that pulls the latest price of MATIC in USD on the Mumbai Testnet.

All you need to do is swap out the address [with any address of a data feed](https://docs.chain.link/docs/matic-addresses#config) that you wish, and you can start digesting price information.

```solidity
pragma solidity ^0.6.7;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract PriceConsumerV3 {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Mumbai Testnet
     * Aggregator: MATIC/USD
     * Address: 0xd0D5e3DB44DE05E9F294BB0a3bEEaF030DE24Ada
     */
    constructor() public {
        priceFeed = AggregatorV3Interface(0xd0D5e3DB44DE05E9F294BB0a3bEEaF030DE24Ada);
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

## Request and receive cycle

Chainlink's Request and Receive cycle enables your smart contracts to make a request to any external API and consume the response. To implement it, your contract needs to define two functions:

1. One to **request the data**, and
2. Another to **receive the response**.

To request data, your contract builds a `request` object which it provides to an oracle. Once the oracle has reached out to the API and parsed the response, it will attempt to send the data back to your contract using the callback function defined in your smart contract.

## Uses

1. **Chainlink Data Feeds**

    These are decentralized data reference points already aggregated on-chain, and the quickest, easiest, and cheapest way to get data from the real world. Currently supports some of the most popular cryptocurrency and fiat pairs.

    For working with Data Feeds, use the [**Polygon Data Feeds**](https://docs.chain.link/data-feeds/price-feeds/addresses/?network=polygon) from the Chainlink documentation.

2. **Chainlink Verifiable Randomness Function**

   Get provably random numbers, where the random number is cryptographically guaranteed to be random.

   For working with Chainlink VRF, use the [**Polygon VRF**](https://docs.chain.link/vrf/v2/subscription/supported-networks) addresses from the [Chainlink documentation](https://docs.chain.link/vrf/v2/subscription/examples/get-a-random-number).

3. **Chainlink API Calls**

   How to configure your smart contract to work with traditional APIs, and customize to get any data, send any requests over the internet, and more.

## Code example

To interact with external APIs, your smart contract should inherit from [`ChainlinkClient.sol`](https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.6/ChainlinkClient.sol), which is a contract designed to make processing requests easy. It exposes a struct called `Chainlink.Request`, which your contract should use to build the API request.

The request should define the oracle address, job id, fee, adapter parameters, and the callback function signature. In this example, the request is built in the `requestEthereumPrice` function.

`fulfill` is defined as the callback function.

```solidity
pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.6/ChainlinkClient.sol";

contract APIConsumer is ChainlinkClient {

    uint256 public price;

    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    /**
     * Network: Polygon Mumbai Testnet
     * Oracle: 0x58bbdbfb6fca3129b91f0dbe372098123b38b5e9
     * Job ID: da20aae0e4c843f6949e5cb3f7cfe8c4
     * LINK address: 0x326C977E6efc84E512bB9C30f76E30c160eD06FB
     * Fee: 0.01 LINK
     */
    constructor() public {
        setChainlinkToken(0x326C977E6efc84E512bB9C30f76E30c160eD06FB);
        oracle = 0x58bbdbfb6fca3129b91f0dbe372098123b38b5e9;
        jobId = "da20aae0e4c843f6949e5cb3f7cfe8c4";
        fee = 10 ** 16; // 0.01 LINK
    }

    /**
     * Create a Chainlink request to retrieve API response, find the target price
     * data, then multiply by 100 (to remove decimal places from price).
     */
    function requestBTCCNYPrice() public returns (bytes32 requestId)
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);

        // Set the URL to perform the GET request on
        // NOTE: If this oracle gets more than 5 requests from this job at a time, it will not return.
        request.add("get", "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo");

       // Set the path to find the desired data in the API response, where the response format is:
       // {
       //     "Realtime Currency Exchange Rate": {
       //       "1. From_Currency Code": "BTC",
       //       "2. From_Currency Name": "Bitcoin",
       //       "3. To_Currency Code": "CNY",
       //       "4. To_Currency Name": "Chinese Yuan",
       //       "5. Exchange Rate": "207838.88814500",
       //       "6. Last Refreshed": "2021-01-26 11:11:07",
       //       "7. Time Zone": "UTC",
       //      "8. Bid Price": "207838.82343000",
       //       "9. Ask Price": "207838.88814500"
       //     }
       //     }
        string[] memory path = new string[](2);
        path[0] = "Realtime Currency Exchange Rate";
        path[1] = "5. Exchange Rate";
        request.addStringArray("path", path);

        // Multiply the result by 10000000000 to remove decimals
        request.addInt("times", 10000000000);

        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * Receive the response in the form of uint256
     */
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId)
    {
        price = _price;
    }
}
```

## Mainnet Polygon LINK token

To get mainnet Polygon LINK token from the Ethereum Mainnet, you must follow a 2-step process.

1. Bridge your LINK using the [PoS bridge](https://wallet.polygon.technology/bridge).
2. Swap the LINK for the ERC677 version via the [Pegswap, deployed by the Chainlink](https://pegswap.chain.link/).

The Polygon bridge brings over an ERC20 version of LINK, and LINK is an ERC677, so we just have to update it with this swap.

## Addresses

There are currently only a few operational Chainlink oracles on the Polygon Mumbai Testnet. You can always run one yourself too, and list it on the Chainlink Marketplace.

* Oracle: [`0xb33D8A4e62236eA91F3a8fD7ab15A95B9B7eEc7D`](https://mumbai.polygonscan.com/address/0x58bbdbfb6fca3129b91f0dbe372098123b38b5e9/transactions)
* LINK: [`0x326C977E6efc84E512bB9C30f76E30c160eD06FB`](https://mumbai.polygonscan.com/address/0x70d1F773A9f81C852087B77F6Ae6d3032B02D2AB/transactions)

To obtain LINK on Mumbai Testnet, head to the [Polygon faucet here](https://faucet.polygon.technology/).

## Supported APIs

Chainlink's Request and Receive cycle is flexible enough to call any public API, so long as the request parameters are correct and the response format is known. For example, if the response object from a URL we want to fetch from is formatted like this: `{"USD":243.33}`, the path is simple: `"USD"`.

If an API responds with a complex JSON object, the **path** parameter would need to specify where to retrieve the desired data, using a dot delimited string for nested objects. For example, consider the following response:

```json
{
   "Prices":{
        "USD":243.33
    }
}
```

This would require the following path: `"Prices.USD"`. If there are spaces in the strings, or the strings are quite long, we can use the syntax shown in the example above, where we pass them all as a string array.

```json
string[] memory path = new string[](2);
path[0] = "Prices";
path[1] = "USD";
request.addStringArray("path", path);
```

## What are job IDs for?

You may have noticed that our [example](#code-example) uses a `jobId` parameter when building the request. Jobs are comprised of a sequence of instructions that an oracle is configured to run. In the [code example](#code-example) above, the contract makes a request to the oracle with the job ID: `da20aae0e4c843f6949e5cb3f7cfe8c4`. This particular job is configured to do the following:

* Make a GET request
* Parse the JSON response
* Multiply the value by *x*
* Convert the value to `uint`
* Submit to the chain

This is why our contract adds in the URL, the path of where to find the desired data in the JSON response, and the times amount to the request; using the `request.add` statements. These instructions are facilitated by what's known as Adapters, in the oracle.

**Every request to an oracle must include a specific job ID.**

Here is the list of jobs that the Polygon oracle is configured to run.

| Name |  Return Type  | ID | Adapters |
|-----|--------|------|-------|
| HTTP GET | `uint256` | `da20aae0e4c843f6949e5cb3f7cfe8c4` |  `httpget`<br/>`jsonparse`<br/>`multiply`<br/>`ethuint256`<br/>`ethtx`  |
| HTTP GET | `int256` | `e0c76e45462f4e429ba32c114bfbf5ac` |  `httpget`<br/>`jsonparse`<br/>`multiply`<br/>`ethint256`<br/>`ethtx`  |
| HTTP GET | `bool` | `999539ec63414233bdc989d8a8ff10aa` |  `httpget`<br/>`jsonparse`<br/>`ethbool`<br/>`ethtx`  |
| HTTP GET | `bytes32` | `a82495a8fd5b4cb492b17dc0cc31a4fe` | `httpget`<br/>`jsonparse`<br/>`ethbytes32`<br/>`ethtx`  |
| HTTP GET | `string` | `7d80a6386ef543a3abb52817f6707e3b` | `httpget`<br/>`jsonparse`<br/>`ethstring`<br/>`ethtx`  |
| HTTP POST | `bytes32` | `a82495a8fd5b4cb492b17dc0cc31a4fe` | `httppost`<br/>`jsonparse`<br/>`ethbytes32`<br/>`ethtx`  |

The complete Chainlink API reference can be found [here](https://docs.chain.link/any-api/api-reference).
