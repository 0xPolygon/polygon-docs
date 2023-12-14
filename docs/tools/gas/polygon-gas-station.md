Polygon gas station aims to help dApp developers with gas price recommendations, so that they can use it before sending transaction off to the Polygon network.

We received a lot of requests from dApp developers for building a gas price recommendation service. So we took some inspiration from Eth Gas Station and built one.

Polygon gas station has been deployed both on the Polygon mainnet & Mumbai testnet. It queries the RPC for `eth_feeHistory` and fetches the 10th, 25th, and 50th percentiles of priority fees for transactions in each of the last 15 blocks. The average value of the 10th, 25th, and 50th percentiles become the `safeLow`, `standard`, and fast fee predictions.

!!! important
    On Polygon PoS mainnet, it is mandatory to pass a minimum priority fees of 30 gwei.

## Usage

### Mumbai

For getting gas price recommendation from this oracle (Polygon Mumbai), send a `GET` request to [https://gasstation-testnet.polygon.technology/v2](https://gasstation-testnet.polygon.technology/v2).

#### cURL

```bash
curl https://gasstation-testnet.polygon.technology/v2
```

#### JavaScript

```javascript
fetch('https://gasstation-testnet.polygon.technology/v2')
  .then(response => response.json())
  .then(json => console.log(json))
```

#### Python

```python
import requests
requests.get('https://gasstation-testnet.polygon.technology/v2').json()
```

### Mainnet

For getting a gas price recommendation from this oracle (Polygon Mainnet), send a **GET** request to the Polygon Gas Station V2 to get the gas fee estimates. Polygon Gas Station V2 Endpoint: [https://gasstation.polygon.technology/v2](https://gasstation.polygon.technology/v2).

#### cURL

```bash
curl https://gasstation.polygon.technology/v2
```

#### JavaScript

```javascript
fetch('https://gasstation.polygon.technology/v2')
  .then(response => response.json())
  .then(json => console.log(json))
```

#### Python

```python
import requests
requests.get('https://gasstation.polygon.technology/v2').json()
```

</TabItem>
</Tabs>

## Interpretation

An example JSON response will look like this:

```json
{
  "safeLow": {
    "maxPriorityFee":30.7611840636,
    "maxFee":30.7611840796
    },
  "standard": {
    "maxPriorityFee":32.146027800733336,
    "maxFee":32.14602781673334
    },
  "fast": {
    "maxPriorityFee":33.284344224133335,
    "maxFee":33.284344240133336
    },
  "estimatedBaseFee":1.6e-8,
  "blockTime":6,
  "blockNumber":24962816
}
```

- `safelow`, `standard`, `fast`, `estimatedBaseFee` are gas prices in GWei. You can use these prices before sending transaction off to Polygon, depending upon your needs.
- `blockNumber` tells what was latest block mined when recommendation was made.
- `blockTime`, in second, gives average block time of the network.
- On Polygon PoS mainnet, it is mandatory to pass a minimum priority fees of 30 gwei.
