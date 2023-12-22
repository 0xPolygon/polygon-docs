!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

Developers building on Polygon can now leverage Band Protocol's decentralized oracle infrastructure. With Band Protocol's oracle, they now have access to various cryptocurrency price data to integrate into their applications.

## Supported tokens

Currently, the list of supported symbols can be found at [https://data.bandprotocol.com/](https://data.bandprotocol.com/). Going forward, this list will continue to expand based on developer needs and community feedback.

## Price pairs

The following methods can work with any combination of base/quote token pair, as long as the base and quote symbols are supported by the dataset.

### Querying prices

Currently, there are two methods for developers to query prices from Band Protocol's oracle: through Band's `StdReference` smart contract on Polygon and through their [`bandchain.js`](https://www.npmjs.com/package/%40bandprotocol%2Fbandchain.js) JavaScript helper library.

### Solidity smart contract

To query prices from Band Protocol's oracle, a smart contract should reference Band's `StdReference` contract, specifically the `getReferenceData` and `getReferenceDatabulk` methods.

`getReferenceData` takes two strings as the inputs, the `base` and `quote` symbol, respectively. It then queries the `StdReference` contract for the latest rates for those two tokens, and returns a `ReferenceData` struct, shown below.

```c++
struct ReferenceData {
    uint256 rate; // base/quote exchange rate, multiplied by 1e18.
    uint256 lastUpdatedBase; // UNIX epoch of the last time when base price gets updated.
    uint256 lastUpdatedQuote; // UNIX epoch of the last time when quote price gets updated.
}
```

`getReferenceDataBulk` instead takes two lists, one of the `base` tokens, and one of the `quotes`. It then proceeds to similarly query the price for each base/quote pair at each index, and returns an array of `ReferenceData` structs.

For example, if we call `getReferenceDataBulk` with `['BTC','BTC','ETH']` and `['USD','ETH','BNB']`, the returned `ReferenceData` array will contain information regarding the pairs:

- `BTC/USD`
- `BTC/ETH`
- `ETH/BNB`

## Contract addresses

| Blockchain           |               Contract Address               |
| -------------------- | :------------------------------------------: |
| Polygon (Test) | `0x56e2898e0ceff0d1222827759b56b28ad812f92f` |

## BandChain.JS

Band's node helper library [`bandchain.js`](https://www.npmjs.com/package/@bandprotocol/bandchain.js) also supports a similar `getReferenceData` function. This function takes one argument, a list of token pairs to query the result. It then returns a list of corresponding rate values.

### Example usage

The code below shows an example usage of the function:

```javascript
const { Client } = require('@bandprotocol/bandchain.js');

// BandChain's REST Endpoint
const endpoint = 'https://rpc.bandchain.org';
const client = new Client(endpoint);

// This example demonstrates how to query price data from
// Band's standard dataset
async function exampleGetReferenceData() {
  const rate = await client.getReferenceData(['BTC/ETH','BAND/EUR']);
  return rate;
}

(async () => {
  console.log(await exampleGetReferenceData());
})();

```

The corresponding result will then be similar to:

```bash
$ node index.js
[
    {
        pair: 'BTC/ETH',
        rate: 30.998744363906173,
        updatedAt: { base: 1615866954, quote: 1615866954 },
        requestID: { base: 2206590, quote: 2206590 }
    },
    {
        pair: 'BAND/EUR',
        rate: 10.566138918332376,
        updatedAt: { base: 1615866845, quote: 1615866911 },
        requestID: { base: 2206539, quote: 2206572 }
    }
]
```

For each pair, the following information will be returned:

- `pair`: The base/quote symbol pair string.
- `rate`: The resulting rate of the given pair.
- `updated`: The timestamp at which the base and quote symbols was last updated on BandChain. For `USD`, this will be the current timestamp.
- `rawRate`: This object consists of two parts.
  - `value` is the `BigInt` value of the actual rate, multiplied by `10^decimals`.
  - `decimals` is then the exponent by which `rate` was multiplied by to get `rawRate`.

## Example usage

This [contract](https://gist.github.com/tansawit/a66d460d4e896aa94a0790df299251db) demonstrates an example of using Band's `StdReference` contract and the `getReferenceData` function.
