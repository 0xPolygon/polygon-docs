---
comments: true
---

If you're a new Web3 developer, it's unlikely that you'll need to run your own full node on Polygon.

The majority of developers use a node provider, or a third-party external service that receives node requests and returns responses for you automatically. That's because the fastest way to get developing on Polygon is using a node provider rather than managing your own node.

This guide demonstrates how to connect to a RPC provider, using Alchemy as an example.

## Send your first blockchain request

This guide assumes you already have an [Alchemy account](https://alchemy.com/?r=e68b2f77-7fc7-4ef7-8e9c-cdfea869b9b5) and access to the [Alchemy Dashboard](https://dashboard.alchemyapi.io).

### Create an Alchemy key

First, you'll need an Alchemy API key to authenticate your requests. You can [create API keys from the dashboard](http://dashboard.alchemyapi.io). Check out [this YouTube video](https://www.youtube.com/watch?v=tfggWxfG9o0) on how to create an app. Or you can follow the steps written below:

1. Navigate to the **Create App** button in the **Apps** tab.
  ![img](https://files.readme.io/693457a-Getting_Started.png)

2. Fill in the details under **Create App** to get your new key. You can also see the applications you previously made by you and your team on this page. Pull existing keys by clicking on **View Key** for any app.
  ![img](https://files.readme.io/d6172a5-Create_App_Details.png)

!!! tip "Optional"
    You can also pull existing API keys by hovering over **Apps** and selecting one. You can **View Key** here, as well as **Edit App** to whitelist specific domains, see several developer tools, and view analytics.

  <center>
  ![img](https://files.readme.io/f0dbb19-ezgif.com-gif-maker_1.gif)
  </center>

### Making a cURL request

You can interact with Alchemy's Polygon infrastructure provider using JSON-RPC and your [command line interface](https://www.computerhope.com/jargon/c/commandi.htm).

For manual requests, use `POST` requests to interact with the JSON-RPC. Simply pass in the `Content-Type: application/json` header and your query as the `POST` body with the following fields:

* `jsonrpc`: The JSON-RPC version—currently, only `2.0` is supported.
* `method`: The MATIC API method. [See API reference](https://alchemyenterprisegroup.readme.io/reference/polygon-api-quickstart).
* `params`: A list of parameters to pass to the method.
* `id`: The ID of your request. Will be returned by the response so you can keep track of which request a response belongs to.

Here is an example you can run from the Terminal/Windows/LINUX command line to retrieve the current gas price:

```bash
curl https://matic-mainnet.alchemyapi.io/v2/demo \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":73}'
```

!!! info

    In case you want to send requests to your own app instead of our public demo, replace `https://eth-mainnet.alchemyapi.io/jsonrpc/demo` with your own API key `https://eth-mainnet.alchemyapi.io/v2/your-api-key`.

Results:

```json
{ "id": 73,
  "jsonrpc": "2.0",
  "result": "0x09184e72a000" // 10000000000000 }
```

## Alchemy SDK setup

To make blockchain requests directly from your Javascript / Node.js dApp, you'll need to integrate the *Alchemy SDK*, the easiest and most powerful way to access the blockchain and Alchemy's suite of enhanced APIs.

*If you have an existing client such as Web3.js or Ethers.js,* you can just change your current node provider URL to an Alchemy URL with your API key: <https://eth-mainnet.alchemyapi.io/v2/your-api-key>

!!! note

    The scripts below need to be run in a **node context** or **saved in a file**, not run from the command line.

### Install the Alchemy SDK

To install the Alchemy SDK, you want to create a project, and then navigate to your project directory to run the installation. Let's go ahead and do that! Once we're in our home directory, let's execute the following:

With Yarn:

```bash
mkdir your-project-name
cd your-project-name
yarn init # (or yarn init --yes)
yarn add alchemy-sdk
```

With NPM:

```bash
mkdir your-project-name
cd your-project-name
npm init   # (or npm init --yes)
npm install alchemy-sdk
```

### Create `index.js`

Make sure to replace `demo` with your Alchemy HTTP API key!

```js title="index.js"
// Setup: npm install alchemy-sdk
const { Network, Alchemy } = require("alchemy-sdk");

// Optional Config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.MATIC_MAINNET, // Replace with your network.
};

const alchemy = new Alchemy(settings);

async function main() {
  const latestBlock = await alchemy.core.getBlockNumber();
  console.log("The latest block number is", latestBlock);
}

main();
```

If you are unfamiliar with the async stuff, check out this [Medium post](https://betterprogramming.pub/understanding-async-await-in-javascript-1d81bb079b2c).

### Run `index.js` using node.js

```bash
node index.js
```

### Console output

You should now see the latest block number output in your console.

```bash
The latest block number is 11043912
```

Excellent! You just wrote a working Web3 script and sent your first request to your Alchemy API endpoint.

The project associated with your API key should now look like this on the dashboard:

![img](https://files.readme.io/e3d2ffd-Alchemy_Tutorial_Result1.png)

![img](https://files.readme.io/bcfc9ff-Alchemy_Tutorial_Result2.png)

## Start building

Don't know where to start? Check out these tutorials to get more familiar with Alchemy and blockchain development:

1. [Examples of Common Queries Using the Alchemy SDK](https://docs.alchemy.com/reference/using-the-alchemy-sdk).
3. Learn [How to Send Transactions on Ethereum](https://docs.alchemy.com/docs/how-to-send-transactions-on-ethereum).
4. Try deploying your first [Hello World Smart Contract](https://docs.alchemy.com/docs/hello-world-smart-contract) and get your hands dirty with some solidity programming!

### Other Web3 libraries

There are a number of alternative Web3 libraries other than the Alchemy SDK you may already be using. See the documentation for these libraries below:

* [Web3.py](https://web3py.readthedocs.io/en/stable/)
* [Web3j](https://docs.web3j.io)
* [Ethers.js](https://docs.ethers.io/v5/)
* [Web3.js](https://web3js.readthedocs.io/en/v1.2.9/)

Using the below code snippets, you can install and use Alchemy as a provider via any of the following libraries.

```python
# Setup: pip install web3
from web3 import Web3
alchemy = Web3(Web3.HTTPProvider("https://eth-mainnet.alchemyapi.io/v2/your-api-key"));
```

```js
// Setup: curl -L get.web3j.io | sh
Web3j web3 = Web3j.build(new HttpService("https://eth-mainnet.alchemyapi.io/v2/your-api-key"));
```

```js
// Setup: npm install ethers
const ethers = require("ethers");
const url = "https://eth-mainnet.alchemyapi.io/v2/your-api-key";
const customHttpProvider = new ethers.providers.JsonRpcProvider(url);
```

```js
// Setup: npm install web3
const Web3 = require('web3');
const web3 = new Web3("https://eth-mainnet.alchemyapi.io/v2/your-api-key");
```
