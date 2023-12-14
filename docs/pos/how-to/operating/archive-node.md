## Get access to an archive node with NodeReal

If you're new to Web3 development, [NodeReal](https://nodereal.io/) simplifies the process of setting up a full node on Polygon.

!!! tip Simplify Polygon node usage with NodeReal and its quality assurance capabilities

    Many developers prefer to use a node provider when getting started on Polygon, or any chain for that matter, as it offers a quick and easy way to handle requests and responses.
    
    NodeReal offers a range of features for developers looking for a node provider on the Polygon network. These features include a Standard Interface that simplifies node usage, as well as reliability and scalability for optimal performance. 
    
    Additionally, NodeReal offers Archive Data for secure data storage, and an API Marketplace that provides additional resources for developers looking to build on Polygon.

## Send your first blockchain API request

If you haven't signed up for a MegaNode account yet, you can find a step-by-step guide to getting started [here](https://docs.nodereal.io/docs/getting-started). Once you have a MegaNode account and access to the NodeReal Dashboard, you're ready to proceed.

### Create Your First API Key

![MegaNode User's Dashboard without API key created](https://files.readme.io/9352cd2-Screen_Shot_2023-01-10_at_19.26.00.png)

To start sending RPC requests on MegaNode, you'll need to create an API Key. This project-based unit is used to manage your API requests, and requires you to input a name for the key and leave any notes you prefer for future reference. Here's how to get started:

!!! tip One API key for all chains

    With only one API Key, you can request all the chains and networks we support on NodeReal.

**Get started &rarr;** Input an API **Key name** and leave any **notes** you prefer:

![Create An API Key](https://files.readme.io/bd84a9f-Screen_Shot_2023-01-10_at_19.29.31.png)

After you have created an API Key, you can find a dashboard on the main screen.

![MegaNode User's Dashboard](https://files.readme.io/b715e5a-Screen_Shot_2023-01-10_at_19.31.18.png)

!!! question "How many API Keys can I create?"

    The number of available API Keys is subjected to the pricing plan.

### Find your API key

After you have successfully created an API Key, you can find the API endpoints on the API Key detail page. Please note that this API key is used to identify a particular user and should **NOT** be shared with anyone.

![Created Your First API key](https://files.readme.io/ce6a39d-Screen_Shot_2023-01-10_at_19.34.38.png)

## Make your first RPC request

After you find the API Key, you can now start to send RPC requests on MegaNode. Please note that all usage will be calculated on an account basis. You can find our API docs [here](https://docs.nodereal.io/reference). Furthermore, you can find more information about the Compute Unit (CU) usage [here](https://docs.nodereal.io/docs/compute-units-cus) and the account Compute Unit Per Second (CUPS) rate limits [here](https://docs.nodereal.io/docs/cups-rate-limit).

!!! info "Any concern about your Privacy?"

    Check out NodeReal [Privacy Policy](https://nodereal.io/privacy-policy).

We’ll be using [Web3.js](https://web3js.readthedocs.io/en/v1.8.2/) libraries to make our first RPC request.

## Install the Web3.js SDK​

If you want to create a project, install Web3.js SDK, and then navigate to your project directory to run the installation. Once we're in our home directory, let's execute the following:

With Yarn:

```bash
mkdir your-project-name
cd your-project-name
yarn init # (or yarn init --yes)
yarn add web3
```

With npm:

```bash
mkdir your-project-name
cd your-project-name
npm init   # (or npm init --yes)
npm install web3
```

### Create `index.js`

Create a JavaScript file named `index.js` and paste the following code:

```js title="index.js"
const Web3 = require('web3');

// Set up a new web3 instance
const web3 = new Web3('https://polygon-mainnet.nodereal.io/v1/<API~KEY> ');


// Get the latest block number
web3.eth.getBlockNumber()
  .then((latestBlockNumber) => {
    console.log(`Latest block number: ${latestBlockNumber}`);


    // Get the latest block details
    return web3.eth.getBlock(latestBlockNumber);
  })
  .then((latestBlock) => {
    console.log('Latest block details:', latestBlock);
  })
  .catch((err) => {
    console.error('Error:', err);
  });

```

Make sure to replace `<API KEY>` with your NodeReal Https API key.

You can retrieve the Polygon **HTTPS URL** from your dashboard.

![Click on Polygon Standard API](https://files.readme.io/94f4b79-Screen_Shot_2023-01-16_at_20.24.34.png)

If you encounter any issues, do reach out to us at [Discord](https://discord.com/invite/nodereal).

### Install dependency for `index.js`

npm

```bash
npm install web3
```

yarn

```bash
yarn add web3
```

### Run `index.js` Using node

```bash
node index.js
```

### Response in Your terminal

You should be able to see the latest block number and block details on your terminal.

```bash
Latest block number: 40302452
Latest block details: {.............}
```

### Self-service troubleshooting for MegaNode users

Please refer to [MegaNode Errors](https://docs.nodereal.io/docs/support) for more information.

**Great work! You managed to write a working Web3 script and sent your first request via NodeReal API endpoint.**
