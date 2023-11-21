---
id: dapp-fauna-polygon-react
sidebar_label: dApps Data Tutorial
title: Data Tutorial for Decentralized Applications
description: Build dapps using Fauna, Polygon, and React
keywords:
  - docs
  - matic
  - dapp
  - fauna
  - polygon
  - data
  - security
  - react
image: https://wiki.polygon.technology/img/polygon-logo.png
slug: dapp-fauna-polygon-react
---

In this tutorial, we’ll be building a simple allowlisting app that utilizes **React** for the UI and functionality, **Polygon PoS** for transactions, and **Fauna** for storing private data from transactions that we may not necessarily want to surface publicly in the blockchain. **Allowlisting**, also known as **whitelisting**, is a concept that is very common in the decentralized world - when signing up for a allowlist, you typically gain access to special privileges, such as being able to be the first to purchase digital assets.

![img](/img/dapp-fauna-polygon-react/polygon-fauna-app.gif)

GIF of app workflow - user fills out form, MetaMask window pops up, and then once the transaction is submitted and confirmed, it surfaces a success message.

The application will take in a first name, last name, and a wallet address. Typically, a lot of allowlists take in a wallet address only, but we’ll be using the first and last name as a way to pass in some additional private information within the transaction. The flow of data will be as illustrated in the diagram:

![img](/img/dapp-fauna-polygon-react/flow.png)
User submits their first name, last name, and wallet address successfully through a form. The new database entry is submitted to Fauna that has a randomly generated UUID, first name, last name, and wallet address. Net transaction is submitted to Polygon that passes in first name, last name, and wallet address as part of the transaction details, but each property equals the UUID generated for the Fauna database.

### What is Fauna?

[Fauna](https://fauna.com/) is a data API that offers a serverless database experience. With in-depth [documentation](https://docs.fauna.com/) and a web-native GraphQL interface, it allows developers to quickly get started with storing their application data without needing to sacrifice things such as flexibility, scale, and performance.

In this tutorial, we’ll be using Fauna as a method of storing private transaction data we may not want to surface on the blockchain explicitly. We’ll use UUIDs populated in the private transaction data to map information from a blockchain transaction to a specific entry with the actual private transaction details in the Fauna database.

## Getting started

In order to get started with building, follow these steps:

- Create a Fauna Account — you can sign up [here](https://dashboard.fauna.com/accounts/register?utm_source=polygon.technology&utm_medium=referral&utm_campaign=docs-tutorial).
- Create a MetaMask Wallet with Polygon’s Test Network (Mumbai-Testnet) configured.
    - First, get set up with MetaMask [here](/docs/tools/wallets/metamask/tutorial-metamask.md). Make sure you save your Secret Recovery Phrase.
    - Then, configure the Mumbai-Testnet on your MetaMask by following the instructions [here](/docs/tools/wallets/metamask/config-polygon-on-metamask.md).
- Once you have MetaMask set up and configured for the Mumbai-Testnet, you’ll need some MATIC to add to your wallet
    - MATIC is the native cryptocurrency of the Polygon network and it’s used to pay network fees, for staking, and also for governance to the Polygon blockchain (MATIC holders can vote on Polygon changes). In the context of this project, you will need MATIC to pay gas fees that are charged for each transaction. You can learn more about MATIC [here](https://www.kraken.com/en-us/learn/what-is-polygon-matic).
    - To get started, use the [MATIC faucet](https://faucet.polygon.technology/) to get free MATIC sent to your wallet (note: this MATIC will only be available on the Mumbai-Testnet and is only for development purposes). Once on the webpage, make sure the following options are selected:

    ![img](/img/dapp-fauna-polygon-react/faucet.png)

    Network: Mumbai, Select Token: MATIC Token, Wallet Address: Put your wallet address here
    - To find out what your wallet address is, you can pull it from Metamask:

    ![img](/img/dapp-fauna-polygon-react/metamask_wallet_address.png)

    Go into MetaMask from your browser. At the top under your Account Name, you’ll see a long string. That’s your account ID. Copy that ID by clicking on it.

    :::info

    This can take a while and you may have to try a few times before the first transaction comes through your wallet. Each successful transaction from the MATIC faucet will give you 0.5 MATIC.

    Since testing the application requires spending MATIC as gas fees (a fluctuating fee that you must pay to perform transactions), we recommend doing this transaction ~12 times so you have about 6 MATIC in your wallet, which should be enough for testing the app in development.

    To track your wallet’s transactions, you can visit [https://mumbai.polygonscan.com/address/](https://mumbai.polygonscan.com/address/)[wallet address].

    :::
- Now, install [Truffle](https://trufflesuite.com/) — this is a suite of tools designed for developing Ethereum applications.
  - To see if you already have Truffle installed, you can run `truffle version` - if you get back a response that looks like this, you already have it installed:
    ``` js
    $ truffle version
    Truffle v5.4.29 (core: 5.4.29)
    Solidity v0.5.16 (solc-js)
    Node v13.8.0
    Web3.js v1.5.3
    ```
  - To install Truffle, run `npm -g truffle`.
- Also, if you don’t already have it, install the tool to spin up a sample React app with `npm i create-react-app`. Learn more about React [here](https://reactjs.org/).

## Start building

If you’re someone that prefers walking through code independently, the GitHub repo is available [here](https://github.com/hello-ashleyintech/polygon-fauna-app). To get started with the GitHub repo, download or clone it and reference the [README](https://github.com/hello-ashleyintech/polygon-fauna-app#readme) to get set up.

### Setup

1. Create a new directory for your project in your location of choice - we called ours `polygon-fauna-app`.
2. Once the directory is created, in your command line, `cd` into the folder (ex: `cd polygon-fauna-app`).
3. Once inside the directory, it’s time to set up the app. Truffle makes it easier for us to build a decentralized application with a React front-end. To set up your initial project, run `truffle unbox react`.
    1. Once the command has run, if you were to run `ls` in your current directory, you’d notice a variety of different subdirectories that weren’t there before. The most important ones we’ll be focusing on are:
        1. `client` - this is where your application, its primary functionality, and its front-end will live. Within client, the structure looks exactly like a regular React project.
        2. `contracts` - this directory is where your smart contracts will live. Smart contracts are programs that will execute specified functionality within an account on the blockchain when the functionality is called. You might notice that the files in this directory end in `.sol` - this is because they are built with [Solidity](https://docs.soliditylang.org/), which is an object-oriented, high-level language for implementing smart contracts.
        3. `migrations` - within this directory, there are preconfigured scripts that will allow you to deploy the smart contracts in `contracts` on the specified network, which will end up being the Mumbai-Testnet network.

  :::note

    If you use an IDE to code, now would be the perfect time to open your project in the IDE! We’re going to start editing some files pretty soon.

  :::

### Smart contract configuration and functionality

1. Currently, the project is pointed towards deploying on the Ethereum blockchain directory. We’re going to need to update this to point to the Mumbai-Testnet that we want to work off of.
    - To do this, first we’ll need to run these commands in your command line to install some necessary packages:

        `npm install @truffle/hdwallet-provider`

        and

        `npm install dotenv`

    - Then, create a file called `.env` in the directory you’re currently in. Within `.env`, do the following:
        - Create an environment variable called `MNEMONIC` and make it equal to the Secret Recovery Phrase for your MetaMask wallet - if you didn’t write it down, you can follow [this guide](https://metamask.zendesk.com/hc/en-us/articles/360015290032-How-to-reveal-your-Secret-Recovery-Phrase) to reveal it once again.
        - Create an environment variable called `RPC_APP_ID` and

        Your `.env` should look something like this:
        ```js
          MNEMONIC=your secret phrase should go here
        ```
    - Finally, replace the truffle-config.js file that was generated through Truffle with the following (note: it should be in the same directory as the client, contracts, and migrations folders):
    ```js
    const HDWalletProvider = require("@truffle/hdwallet-provider");
    const path = require("path");
    require("dotenv").config(); // Load .env file

    module.exports = {
      // See <http://truffleframework.com/docs/advanced/configuration>
      // to customize your Truffle configuration!
      contracts_build_directory: path.join(__dirname, "client/src/contracts"),
      networks: {
        develop: {
          port: 8545,
        },
        matic: {
          provider: () =>
            new HDWalletProvider(
              process.env.MNEMONIC,
              `https://matic-mumbai.chainstacklabs.com`
            ),
          network_id: 80001,
          confirmations: 2,
          timeoutBlocks: 200,
          skipDryRun: true,
          gas: 6000000,
          gasPrice: 10000000000,
        },
      },
    };
    ```
2. Once you’ve set up your configuration, test it and make sure it points to your account.
  - To test this, migrate your current smart contracts (Truffle has auto-populated some for you) by running `truffle migrate --network matic`. If it’s not your first time running this `deploy` command for this project, you’ll want to run `truffle migrate --network matic --reset` so it runs a fresh copy of migrations and pulls the most recent code updates.

  :::info Facing Errors?

  If you run into any issues, try the following things:

  * Make sure your `MNEMONIC` environment variable is defined in a `.env` file in your root directory.

  * If you are running into continuous errors and you’ve checked the above, try other RPC URLs in place of the [matic-mubai.chainstacklabs.com](http://matic-mubai.chainstacklabs.com) URL in `truffle-config.js`. A list of additional URLs for the Mumbai-Testnet can be found on [this page](https://docs.polygon.technology/docs/operate/network/) under the **Mumbai-Testnet** section.

  :::

- Then, test being able to connect to your new application by running the front-end. Truffle added some pre-configured logic that will allow you to test this connection. You can test it by running the following from your main directory:

  ```bash
  `cd client`
  `npm run start`
  ```

:::note

  You will only be able to start your application inside the `client` folder.

:::

  - Your browser will launch a development instance on [http://localhost:3000](http://localhost:3000) that will then prompt Metamask. It may ask you to re-auth your password. Finally, MetaMask will attempt to connect your account on the testnet to your application instance, which will cost you some MATIC in gas fees. You’ll see a window like this:

  ![img](/img/dapp-fauna-polygon-react/metamask_notification.png)

  - To go through with the transaction, click “Confirm”. The MetaMask window will disappear and you should get a small “Transaction Confirmed” notification in your browser. To verify that your wallet has been connected successfully, you should see this page:

  ![img](/img/dapp-fauna-polygon-react/truffe_box_installed.png)

  Note that the stored value at the bottom of the page in this screenshot is the value 5. The original value is set to 0 when the page is initially loaded prior to authenticating your wallet. It will update to 5 once it is successfully connected.

3. Now, we can get to work on updating your smart contract functionality.
  - To do this, we’re going to clean up the `contracts` directory in the root project directory. You can access it in your command line by running `cd ../contracts` from the `client` directory.
  - We’ll first delete the default `SimpleStorage.sol` file in the `contracts` directory.
  - Then, we’ll add a new smart contract for the specific allowlisting functionality. Within `contracts`, create a new file called `Allowlist.sol` and paste in the following:

``` solidity

  pragma solidity ^0.5.0;

  contract Allowlist {
      // all are going to be set to uuid value in smart contract, so declare as same type
    struct allowlister {
      string f_name;
      string l_name;
      string wallet_address;
    }

    allowlister[] allowlisters; // array of all allowlisters

    function _createAllowlister (string memory _uuid) public {
      allowlisters.push(allowlister({
        f_name: _uuid,
        l_name: _uuid,
        wallet_address: _uuid
      })) -1;
    }
  }

```

Let’s break this code down a bit:

  - The smart contract, `Allowlist`, contained an outline of what an allowlister (someone who submits an entry to the Allowlist) will look like. We know that we’ll be taking in a first name, last name, and wallet address in the form, so we created a `struct` representing an allowlister with those properties. When we store the items in the contract, they’ll each map to that submission’s UUID, meaning that each variable type should align with whatever variable type that UUID will be.
      - Since the UUID will be a string that exceeds the length of other kinds of variable types in Solidity, we’ll be assigning each property the type `string`, which accepts longer lengths.
  - We’ve also initialized an array of `allowlisters` that we can add to as users submit information in the form.
  - Finally, we’ve created a function, `_createAllowlister`, that will be what we call when users submit the form. The function takes in the generated `_uuid` string for that entry (the underscore in the variable name is to differentiate the variable as a function parameter). Within the function, we will push a new `allowlister` instance to the `allowlisters` array - each property in the instance will equal the `_uuid` that is passed in.

- Then, go into the migrations folder in the root directory. We’re going to hop into the  2_deploy_contracts.js file and update the functionality so it deploys the new contract

  ```js
  var Allowlist = artifacts.require("./Allowlist.sol");

  module.exports = function(deployer) {
    deployer.deploy(Allowlist);
  };
  ```

- Finally, you will migrate your new contract by running `truffle migrate --network matic --reset`.

### App and functionality development

Once you’ve deployed your new smart contract, let’s get started on building out the application.

1. We’ll be using the `react-hook-form` library to build a simple form experience. You’ll need to install it by running `npm install react-hook-form`.
2. Next, create a new directory in `client/src` titled `components`.
3. Within `components`, create a file called `AllowlistForm.js` and paste in the following:

  ```js
  import React, { useEffect } from "react";
  import { useForm } from "react-hook-form";

  export default function AllowlistForm(props) {
    const {
      register,
      handleSubmit,
      setValue,
      formState: { errors },
    } = useForm();

    useEffect(() => {
      register("firstName", { required: true });
      register("lastName", { required: true });
      register("walletAddress", { required: true });
    }, [register]);

    async function submitForm(data) {
      console.log(data);
    }

    return (
      <div className="wrapper">
        <form onSubmit={handleSubmit((data) => submitForm(data))}>
          <div className="header">
            <h1>Allowlist Form</h1>
            <p>
              Please fill out this form to get allowlisted for this exclusive
              project.
            </p>
          </div>
          <label htmlFor="firstName">First Name</label>
          <input
            id="firstName"
            onChange={(e) => setValue("firstName", e.target.value)}
          />
          {errors.firstName && (
            <span role="alert" className="errorField">
              First name is required.
            </span>
          )}
          <label htmlFor="lastName">Last Name</label>
          <input
            id="lastName"
            onChange={(e) => setValue("lastName", e.target.value)}
          />
          {errors.lastName && (
            <span role="alert" className="errorField">
              Last name is required.
            </span>
          )}
          <label htmlFor="walletAddress">Wallet Address</label>
          <input
            id="walletAddress"
            onChange={(e) => setValue("walletAddress", e.target.value)}
          />
          {errors.walletAddress && (
            <span role="alert" className="errorField">
              Wallet address is required.
            </span>
          )}
          <input type="submit" className="submitButton" />
        </form>
      </div>
    );
  }
  ```

  The above code creates a component called `AllowlistForm`  using the `react-hook-form` library installed earlier. The form allows a `firstName`, `lastName`, and `walletAddress` field, and also explicitly specifies what fields are required or not for error validation. The component also contains some error-handling logic for leaving required inputs blank and attempting to submit.

4. Next, to make the form look better, create a file called `AllowlistForm.css` and add in the following CSS code:

  ```css

  h1 {
    border-bottom: 1px solid white;
    color: #3d3d3d;
    font-family: sans-serif;
    font-size: 20px;
    font-weight: 600;
    line-height: 24px;
    text-align: center;
  }

  .header {
    margin-bottom: 10px;
  }

  form {
    background: white;
    border: 1px solid #dedede;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin: 0 auto;
    margin-top: 10px;
    max-width: 500px;
    padding: 30px 50px 0px;
  }

  input {
    border: 1px solid #d9d9d9;
    border-radius: 4px;
    box-sizing: border-box;
    padding: 10px;
    width: 100%;
    margin-bottom: 10px;
  }

  label {
    color: #3d3d3d;
    display: block;
    font-family: sans-serif;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 5px;
    text-align: left;
  }

  .errorField {
    color: red;
    font-family: sans-serif;
    font-size: 12px;
    margin-bottom: 10px;
    text-align: left;
  }

  .submitButton {
    background-color: #6976d9;
    color: white;
    font-family: sans-serif;
    font-size: 14px;
    margin: 20px 0px;
  }
  ```

  :::tip

  To implement the form field, button, and input styling and color scheme, as well as to help outline form functionality, you can use [Retool tutorial](https://retool.com/blog/how-to-build-a-react-form-component/) on `react-hook-form` as a reference.

  :::

  :::note

  If you receive a warning about old stylesheets, this is probably due to a legacy version of `create-react-app` that Truffle is using to set up the React project. To mitigate this, you can update your `package.json`'s `browserlist` property so it looks like this:

  ```js
  "browserslist": {
      "production": [
        ">0.3%",
        "not ie 11",
        "not dead",
        "not op_mini all"
      ],
      "development": [
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version",
        ">0.3%",
        "not ie 11",
        "not dead",
        "not op_mini all"
      ]
    }
  ```
  :::

5. To wire up the styling with the component, add the following import statement at the top of your `AllowlistForm.js` component:

  `import "./AllowlistForm.css";`

6. Finally, we need to actually surface the form in our demo app. We’ll do this by updating the `App.js` file in the `client` directory. Replace the current contents of `App.js` with the following:

  ```js
  import React, { Component } from "react";
  import AllowlistContract from "./contracts/Allowlist.json";
  import getWeb3 from "./getWeb3";
  import AllowlistForm from "./components/AllowlistForm";

  import "./App.css";

  class App extends Component {
    state = { storageValue: 0, web3: null, accounts: null, contract: null };

    componentDidMount = async () => {
      try {
        // Get network provider and web3 instance.
        const web3 = await getWeb3();

        // Use web3 to get the user's accounts.
        const accounts = await web3.eth.getAccounts();

        // Get the contract instance.
        const networkId = await web3.eth.net.getId();
        const deployedNetwork = AllowlistContract.networks[networkId];
        const instance = new web3.eth.Contract(
          AllowlistContract.abi,
          deployedNetwork && deployedNetwork.address
        );

        // Set web3, accounts, and contract to the state, and then proceed with an
        // example of interacting with the contract's methods.
        this.setState({ web3, accounts, contract: instance });
      } catch (error) {
        // Catch any errors for any of the above operations.
        alert(
          `Failed to load web3, accounts, or contract. Check console for details.`
        );
        console.error(error);
      }
    };

    render() {
      if (!this.state.web3) {
        return <div>Loading Web3, accounts, and contract...</div>;
      }
      return (
        <div className="App">
          <AllowlistForm
            contract={this.state.contract}
            accounts={this.state.accounts}
          />
        </div>
      );
    }
  }

  export default App;
  ```
You might notice that some of this `App.js` logic is similar to what was originally set up by Truffle! Our new-and-improved `App.js` will do the following:

- On page load, initialize a web3 instance, any related accounts, and an instance of our `Allowlist` smart contract (pulled from `Allowlist.json`, an instance of our contract that is generated from the previously run `truffle migrate` command). Within these initializations, we set corresponding state variables for the contract, account list, and web3 instances.
- When the page renders, if we’re still fetching all of the web3 information, it’ll show a `Loading message` rather than the form - this is determined by checking whether the web3 state variable has been set. Once that web3 state variable has been set, we return the `AllowlistForm` component and pass in our `contract` and `accounts` state variables - we’ll need them within our component to write to the blockchain when we submit the form.
- To get a beautiful full-page lavender background like in the demo GIF, add the following at the bottom of your `App.css` file:

  ```css
  html,
  body {
    width: 100%;
    height: 100%;
    background: lavender;
  }
  ```

When navigating to http://localhost:3000 now, your application will look like this:

![img](/img/dapp-fauna-polygon-react/allowlist.png)

At this point, you can test the functionality of your form - try to submit empty responses to see if the error messages pop up. You can also fill out each field with random strings to test successfully submitting - to determine if it was successful, check your console, and you should see your submitted form responses as they come through.

### Fauna setup and wiring

Now that the application is set up, hop into Fauna and connect it to our application.

1. Log into your Fauna account. You’ll be taken to the main dashboard, where you’ll create a database by clicking the “Create Database” button. Create a database with a name of your choice and make sure to select the “Classic” Region Group:

![img](/img/dapp-fauna-polygon-react/create_database.png)

Once you create your database, you will be taken to the overview page.

2. Within your newly created database, you’re going to create a [Collection](https://docs.fauna.com/fauna/current/learn/understanding/collections). Collections in Fauna are equivalent to the concept of a “table” in a traditional database - a dedicated place to store entries that all have the same information and fields as one another. You’ll click the “New Collection” button and create a Collection with a name of your choosing:

![img](/img/dapp-fauna-polygon-react/new_collection.png)

:::tip

  Something super interesting about Fauna is that you don’t actually create `columns`, which, in a traditional database, are a way to structure entries that you insert in the table. The data you insert into Fauna determines the collection structure rather than the other way around.

:::

3. Once a database and a collection within it has been made, we need to generate a secret key to be able to access it in-app. To do so, go to the **Security** option in your database and click **New Key**. Create a new key with the following settings and give it a name of your choosing:

![img](/img/dapp-fauna-polygon-react/new_key.png)

Click **Save** and copy the Secret that appears above the list of keys. Then, create a `.env` file in your project within client - this is a React-specific environment file that the frontend will read from. Add a `REACT_APP_FAUNADB_SECRET` environment variable and set it equal to the Secret that you copied when generating the API key. Your `.env` should look like this:

  ```js
  REACT_APP_FAUNADB_SECRET=your secret from fauna goes here
  ```

:::note

  For React `.env` files, all custom environment variables MUST start with `REACT_APP_` in order for React to recognize them.

:::

4. Now that we have a collection ready in Fauna and an API key generated from the database it lives in, we can start writing to Fauna.
  - In your project directory, run `npm install --save faunadb` to install `faunadb` locally.
  - Next, in `client/src`, create an `api` folder.
  - Within the `api` folder, create a file called `fauna.js`, which is going to be how we talk within our application to the Fauna API. Your `fauna.js` file should look like this:

    ```js
    require("dotenv").config(); // Load .env file
    export async function addDocument(uuid, firstName, lastName, walletAddress) {
      const faunadb = require("faunadb");
      const q = faunadb.query;
      const client = new faunadb.Client({
        secret: process.env.REACT_APP_FAUNADB_SECRET,
        domain: "db.fauna.com",
        scheme: "https",
      });
      var response = client.query(
        q.Create(q.Collection("allowlist_members"), {
          data: {
            uuid: uuid,
            f_name: firstName,
            l_name: lastName,
            wallet_address: walletAddress,
          },
        })
      );

      return response;
    }

    ```

The `fauna.js` starts by pulling the environment variable set in the `client/.env`. Then, it declares an `addDocument` function that takes in a `uuid` (which we will generate programmatically in a section below), and the form-inputted `firstName`, `lastName`, and `walletAddress`. Within the function, it initializes an instance of a Fauna API client utilizing the secret stores in the `.env`, which specifically will point Fauna to the database you created.

Finally, the function actually queries the API client to add a new item, called a Document, to the collection you created (in this code example it is pulling from a collection called `allowlist_members`- you’ll need to change this to the name you chose for your own collection).

Finally, the API response is returned once the query is executed.

:::tip

The `faunadb` [package website](https://www.npmjs.com/package/faunadb) is a great resource for insight into configuring and connecting Fauna to the app!

:::

### Submit form responses to Fauna

With the Fauna API client added in and a way to add new items to our collection, let’s wire it up to our form!

If you recall from the user flow, we want the following things to happen when someone submits the form:

1. All the information is sent to the blockchain, but the private values are replaced with generated UUIDs.
2. Those private values (first name, last name, and wallet address) are instead sent to Fauna and stored next to that UUID.

Now that we have the functionality in place to send information to Fauna, let’s use it to accomplish goal #2.

1. Add the following import at the top of your `AllowlistForm.js` file:

    ```js
    `import { *addDocument* } from "../api/fauna";`
    ```

2. Then, inside the `submitForm` function in `AllowlistForm.js`, replace the `console.log` statement with the following:

    ``` js
    // add data to Fauna
    const uuid = crypto.randomUUID();
    await addDocument(uuid, data.firstName, data.lastName, data.walletAddress)
      .then((res) => {
        console.log(res);
      }
    )
    ```

In this snippet, we are programmatically generating a UUID using the built-in `crypto.randomUUID()` [function](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID), which will generate a 36-character-long v4 UUID. Once the UUID has been generated, we call the `addDocument` function we just added. Within `addDocument`, we’re passing information from the form submission (captured in `data`, which is being initially passed into `submitForm` - `data.firstName`, `data.lastName`, and `data.walletAddress`) as well as the generated UUID. Finally, the API response is logged to the console, which will help us determine if the API call successfully went through.

3. At this point, your form is now configured to send information to Fauna when submitting a fully filled out form. You can test this by filling out each field in the form and submitting it. It should log an object in the console with a `data` property inside it that shows all the information submitted to Fauna. To confirm that it successfully submitted, you can pull up your collection in Fauna and see if the entry is there. It should look something like this:

![img](/img/dapp-fauna-polygon-react/allowlist_members.png)

### Handling UUID collisions

Our application is now sending responses to Fauna. However, since we’re using a randomly generated UUID, there is a chance that we could have duplicated UUID entries in our database. We want to make sure that before we store any information in Fauna that there are no other UUIDs that match the one we’ve generated, and if there are, we’ll need to generate a new one.

1. In order to search the data we’ve been populating into our Fauna collection, we can use an [Index](https://docs.fauna.com/fauna/current/api/fql/indexes?lang=javascript). Indexes in Fauna allow you to browse and easily search the data stored in your collections. To do this, you can go to your collection in Fauna and click the “New Index” button.

2. You will be taken to a page to create a new index - make sure the Source Collection field has correctly populated the collection you’re trying to add to. Indexes are used for querying, so try to name the index something that specifically captures what it’s going to do - since the index will be used to query entries by UUID, we chose `allowlist_members_by_uuid`. To specify what properties you’ll be querying by, add `data.uuid` into the Terms field - this lets Fauna know to pull items based on the UUID. Lastly, since you do want the UUID to be unique, check the “Unique” option and also make sure the “Serialized” option also stays checked:

![img](/img/dapp-fauna-polygon-react/new_index.png)

3. Once the index has been created, we can now query it from Fauna. To do this, we’ll need to hop into our client/src/api/fauna.js file and add a new function, findUUID, to search by index when given a UUID passed in as a parameter:

    ```js

    export async function findUUID(uuid) {
      const faunadb = require("faunadb");
      const q = faunadb.query;
      const client = new faunadb.Client({
        secret: process.env.REACT_APP_FAUNADB_SECRET,
        domain: "db.fauna.com",
        scheme: "https",
      });
      client
        .query(q.Paginate(q.Match(q.Index("allowlist_members_by_uuid"), uuid)))
        .then((res) => {
          if (res.data.length === 0) {
            return false;
          } else {
            return true;
          }
        });
    }

    ```

Very similarly to the `addDocuments` function, we need to do some initial setup and configurations with the Fauna client in this function. Then, we’re calling a query that looks into a specific index (in this case `allowlist_members_by_uuid` ) and sees if there are any matching items that have the `uuid` passed in as a function argument. In the event that there are no matches, an empty array is returned, so the function then checks for an empty array and returns `false` (indicating the UUID has not been found and is therefore not taken) - otherwise, it’ll return `true` (indicating the UUID has a match).

4. Now that we have a way to check for existing UUIDs, we can add this in to our `submitForm` function in our `AllowlistForm.js` component.
    - To do this, we’ll add the `findUUID` function in to the `../api/fauna` import statement at the top of the file like so:

      ``` js
      import { addDocument, findUUID } from "../api/fauna";
      ```

    - Replace the const uuid = crypto.randomUUID(); line with the following logic:

      ```js
      // generate uuid
      let uuid = "";
      // check for duplicate uuids in db
      while (true) {
        const generatedUUID = crypto.randomUUID();
        const didFindUUID = await findUUID(generatedUUID);
        if (!didFindUUID) {
          uuid = generatedUUID;
          break;
        }
      }
      ```
    With the above code, we’re initializing a UUID variable. Then, we’re diving into an infinite loop that will run until it is manually broken out of - within the loop, a UUID is generated using `crypto.randomUUID()`. The generated UUID is then passed into a call to the `findUUID` function, which will return either true or false to the variable `didFindUUID` once the function call is complete. If `didFindUUID` returns false, meaning there are no matches in the database for this generated UUID, then the UUID variable is set to the generated UUID and the loop is broken out of. Otherwise, the entire process is repeated until a non-duplicate UUID is identified.

### Submit form responses to the blockchain

The final step in our application is to write to  the blockchain using our smart contract. As we mentioned above, we want the generated UUID that we store in Fauna to replace all of the actual private data (in this case, the first name, last name, and wallet address submitted). This adds a layer of security to the private data - it’s not publicly available on the blockchain, only the UUID is, and you’d need access to the Fauna database to be able to see the information behind that UUID.

1. Since we want the form to submit to the blockchain only if the Fauna API call is successful (and only once it happens), we can nest the API call to add a new allowlister within the Fauna API call where we add a new document. We’ll do this in the `submitForm` function by replacing the `console.log(res)` line so that it calls our `_createAllowlister` method from our smart contract:

    ```js
    async function submitForm(data) {
      // generate uuid
        let uuid = "";
      // check for duplicate uuids in db
      while (true) {
        const generatedUUID = crypto.randomUUID();
        const didFindUUID = await findUUID(generatedUUID);
        if (!didFindUUID) {
          uuid = generatedUUID;
          break;
        }
      }
      // add data to Fauna
      await addDocument(uuid, data.firstName, data.lastName, data.walletAddress)
        .then((res) => {
          // add data to contract
          props.contract.methods
            ._createAllowlister(uuid)
            .send({ from: props.accounts[0] })
        }
      )
    }
    ```

 Since we passed the `Allowlist` smart contract and all available accounts into our `AllowlistForm` component, we’re able to access them to pull information from our smart contract. Since they’re passed in as props, we’re referencing them as `props.contract` and `props.accounts` rather than `contract` and `accounts`.

2. Once that has been added in, you can see if your application is successfully submitting to Fauna and the blockchain by filling out the form in your application. A MetaMask window should pop up, and if you click “Accept”, you’ll receive a notification after a few seconds that the transaction was successfully submitted. You can also check for the newly added document in your Fauna collection to make sure it’s writing to both Fauna and the blockchain.

### Read transaction data from the blockchain and lookup in Fauna

Now that we’re able to write transactions to Fauna and then the blockchain, how can we actually find the data we need from a transaction we’ve submitted?

Luckily, the public nature of the blockchain makes it easy to track down transactions and also find the metadata associated with a given transaction.

1. We’ll be using the Mumbai Polygonscan tool to find all the transactions associated with the wallet we’ve used to develop the application. This tool allows you to look up any wallet on the Mumbai-Testnet by its address and see a history of all of its transactions as well as the amount of MATIC inside the wallet.
    - To find your wallet, you can go to this url: [https://mumbai.polygonscan.com/address/](https://mumbai.polygonscan.com/address/)[put your wallet address here]
2. Once you navigate to this page, you’ll see a list of all of the transactions associated with your wallet. The transactions display from most to least recent.

Click on a transaction to see more information by clicking on the transaction hash - this hash is uniquely generated and is what identifies your transaction.

![img](/img/dapp-fauna-polygon-react/transaction_hash.png)

3. When you click on the transaction hash, you’ll go to a page that lists the transaction’s specific details. To grab the information you’ll need, click the “Click to see more” option near the bottom of the displayed transaction information.
4. Within the “Click to see more” option, you’ll see a lot more information. We’re going to scroll to the “Input Data” section, where there will be a long hash.

![img](/img/dapp-fauna-polygon-react/input_data.png)

We can write a script to parse the transaction hash for the Input Data, so that we can turn that hash into actual data that we can pull our `uuid` from to be able to query in Fauna.

5. To decode this, we can use the [abi-decoder library](https://github.com/ConsenSys/abi-decoder). In the `client` directory of your project, run the following to install the library:

    ```jsx
    npm install abi-decoder
    ```

6. Then, create a folder named `scripts` in the `client` directory.
7. Within the `scripts` folder, create a file called `decode-transaction.js` and paste the following information in:

    ```jsx
    const abiDecoder = require('abi-decoder');

    // pulled from Allowlist.json "abi" field
    const testABI = [
        {
          "constant": false,
          "inputs": [
            {
              "internalType": "string",
              "name": "_uuid",
              "type": "string"
            }
          ],
          "name": "_createAllowlister",
          "outputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        }
    ];
    abiDecoder.addABI(testABI);

    // add in your input data hash as a string here
    const testData = "";
    const decodedData = abiDecoder.decodeMethod(testData);
    console.log(decodedData);
    ```

The above code will create an instance of the abi-decoder library so it can be used, storing it in the variable `abiDecoder`. In order to read the Input Data hash, the library requires an ABI, or Application Binary Interface, to tell the decoder what information, such as functions and arguments, is in the smart contract being used for the transaction. The ABI will help inform the decoder what information can be parsed from the hash.

If you used the same smart contract from this tutorial in your application, then the ABI has already been populated for you in the `testABI` variable. This ABI was taken from the smart contract metadata for `Allowlist.sol` that was generated upon migration. The metadata can be found in `client/contracts/Allowlist.json`. Within this file, there is an `abi` property, representing the `Allowlist` contract ABI, which is where the `testABI` value was pulled from.

The final touch for this program to run will be to add in the input data hash for the transaction you want to decode. Copy the Input Data you found from the Mumbai Polygonscan website and set it as a string equal to `testData`.

8. Once all information has been added in to the script, we can run it in the command line to see the output. Run the script from the `client` folder using this command:

    ```jsx
        node scripts/decode-transaction.js
    ```

You’ll receive a response back that looks like this:

```js
{
  name: '_createAllowlister',
  params: [
    {
      name: '_uuid',
      value: '2bb542ef-39b7-4991-bfa8-aac848fdce39',
      type: 'string'
    }
  ]
}
```

This response indicates that the transaction was initialized by the `_createAllowlister` function from the smart contract and that the `_uuid` value was passed in as a parameter (as well as what that value was).

Our `uuid` has been successfully identified from the transaction - in this particular response, it’s `2bb542ef-39b7-4991-bfa8-aac848fdce39`.

9. Now that we have the `uuid`, we can search in Fauna using it to find the data behind the transaction. To do so, navigate to your [Fauna Dashboard](https://dashboard.fauna.com/), click on the Database you used for your application, and then click on “Indexes” in the sidebar for that database. Make sure that the index you used for the app is displaying at the top of the page - if not, then select it from the list of indexes below to ensure you’re querying from the right one.

Once you have the right index pulled up, paste your UUID into the field under “data.uuid” and make sure the dropdown above the field says “String”.

When you click the search button, an entry should appear below the search field:

![img](/img/dapp-fauna-polygon-react/search_index.png)

Once you expand the entry, you’ll see all of the original data passed in to the form for that specific transaction, such as the first name, last name, and wallet address.

### Error and success messaging

We’ve written a React form application that stores its data directly in Fauna and then submits it as a transaction to the blockchain where its private details are stored as a UUID, which can be used to reference the record in Fauna. We also showed how to take a transaction from the blockchain, parse its input data, and use it to search up the records in Fauna.

However, while working through form submission and testing everything in the application, you might’ve noticed it was sometimes difficult to tell when a record was successfully submitted or not. To mitigate this, we can add in some error and success messaging that will surface to indicate an errored form submission (either from a Fauna or Polygon issue) or a successful form submission. This part of the tutorial will focus on changing some API call logic in `AllowlistForm.js`.

**Error Messaging**

Ideally, we’d want to catch when the Fauna API throws an error, and we’d also want to catch when interacting with the blockchain throws an error - either of these scenarios indicates that the transaction won’t go all the way through. We also want to make sure that if Fauna fails, it doesn’t still try to interact with the blockchain - this could create inconsistency in the entries.

1. To do this, let’s add a state variable to track whether or not the form submission has failed at any point. To initialize new state variables, we’ll need to start by importing the `useState` hook, which can be added in where we’re importing `React` and `useEffect`:
``` jsx
import React, { useEffect, useState } from "react";
```

2. Once imported, we can initialize our variable. We’ll call it `formField` - this will be added in after the `useForm()` usage at the top of the component:

    ```jsx
    const {
        register,
        handleSubmit,
        setValue,
        formState: { errors },
    } = useForm(); // this is already in the code, add the line below
    const [formFail, setFormFail] = useState(false);
    ```

To initialize a new state variable, we need to declare a name (`formFail`) and also a function to set it (`setFormFail`). We also need to set it to a default value (since `formFail` will be a boolean indicating whether or not the form has failed, we can set the default value to `false`).

3. Now, we need to make sure that we add in error messaging that uses this state variable. If `formFail` becomes `true`, we’d want to surface the error messaging. We can add in this snippet of `jsx` within the `wrapper` div class in the `return()` function at the bottom of the file:

    ```jsx
    {formFail && (
      <div className="errorMessage">
        <p>Failed to submit allowlist entry. Please try again.</p>
      </div>
    )}
    ```

4. In addition to adding the error message block, we need to add some styling for the error message in `AllowlistForm.css`:

    ```jsx
      .errorMessage {
        background-color: #fe6f5e;
        border: solid 1px;
        border-color: #000000;
        margin-bottom: 10px;
        margin: 10px;
      }
    ```

5. Finally, we need to actually set `formFail` to `true` in areas where the form fails. To do this, we’ll hop back into `AllowlistForm.js` and update our `submitForm` function’s API calls to Fauna and the blockchain so that they have `.catch()` statements:

    ```jsx
    async function submitForm(data) {
    	... // some logic exists here
    	// update this snippet that is already within submitForm()
    	await addDocument(uuid, data.firstName, data.lastName, data.walletAddress)
    	  .then((res) => {
    	    if (!res.ok && res.status >= 400) {
    	      setFormFail(true);
    	      return;
    	    } else {
    	      // add data to contract
    	      props.contract.methods
    	        ._createAllowlister(uuid)
    	        .send({ from: props.accounts[0] })
    	        .catch(() => {
    	          setFormFail(true);
    	          return;
    	        });
    	    }
    	  })
    	  .catch(() => {
    	    setFormFail(true);
    	    return;
    	  });
    	}
    }
    ```

In addition to adding `.catch` statements to each API call (`addDocument` and `_createAllowlister`), the code above also adds a block that checks for a scenario where Fauna may not throw an error, but does return an error response (meaning that the API does not return a `res.ok` and that the `res.status` is greater than or equal to a `400` response code, which indicates an error).

Your error messaging will look like this:

![img](/img/dapp-fauna-polygon-react/error_msg.png)

**Success Messaging**
1. Let’s say we want a success message that surfaces what we submitted in the form within the message - to do so, we’ll need to store what we submitted in the form (first name, last name, and wallet address, which are all strings) as state variables, as well as one to track a successful form submission. To do so, add the following state variable initializations into your code:

    ```jsx
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [walletAddress, setWalletAddress] = useState("");
    const [formSuccess, setFormSuccess] = useState(false);
    ```

2. Within the `wrapper` div in the `return()` in `AllowlistForm.js`, just as you added a `jsx` block for the error message, add one for the success message above or below it. The message will surface the form input-related state variables:

    ```jsx
    {formSuccess && (
      <div className="successMessage">
        <p>
          Successfully submitted allowlist entry for{" "}
          {firstName + " " + lastName} with wallet address {walletAddress}!
        </p>
      </div>
    )}
    ```

3. Add some styling for the success message in `AllowlistForm.css`:

    ```jsx
    .successMessage {
      background-color: #e2fee2;
      border: solid 1px;
      border-color: #000000;
      margin-bottom: 10px;
      margin: 10px;
    }
    ```
4. Finally, update all of your newly added state variables in a place where, after the API calls are executed, the form is considered fully submitted:

    ```jsx
    async function submitForm(data) {
    	... // some logic exists here
      await addDocument(uuid, data.firstName, data.lastName, data.walletAddress)
        .then((res) => {
          if (!res.ok && res.status >= 400) {
            setFormFail(true);
            return;
          } else {
            // add data to contract
            props.contract.methods
              ._createAllowlister(uuid)
              .send({ from: props.accounts[0] })
              .then(() => {
    						// update this snippet that is already within submitForm()
                setFirstName(data.firstName);
                setLastName(data.lastName);
                setWalletAddress(data.walletAddress);
                setFormSuccess(true);
              })
              .catch(() => {
                setFormFail(true);
                return;
              });
          }
        })
        .catch(() => {
          setFormFail(true);
          return;
        });
    }
    ```

The form submission would be considered successful once both the Fauna and Polygon API calls went through. Because of this, we’ve added the logic to set the `firstName`, `lastName`, `walletAddress`, and `formSuccess` variables as a `.then()` block attached to `_createAllowlister` - this is the last API call that happens before the `submitForm` function ends, and adding in a `.then()` ensures that the states are only updated once the last API call has been completed.

Your success messaging will look like this:

![img](/img/dapp-fauna-polygon-react/success_msg.png)

## Conclusion

We’ve built an allowlisting application in React that takes in private information, securely stores it in a Fauna database, and then submits a public UUID for each property corresponding to the transaction’s database record to the Polygon blockchain. The full GitHub repository for this tutorial can be found [here](https://github.com/hello-ashleyintech/polygon-fauna-app).

If you’re looking to build off of this tutorial or expand the app from here, some great next steps would be to:

- Write some tests for the Solidity smart contracts
- Write some tests for the React functionality and components
- Try adding some additional features, such as:
    - Surfacing every submitted allowlister and the corresponding UUID info as an easily referenceable guide to find them in Fauna
    - Adding in logic so that if the Polygon API call fails for any reason, then it’ll remove the entry from the Fauna database
    - Adding in logic so that if someone gets a failed submission, and then resubmits and gets a successful submission, the error message goes away and only shows the success message and vice versa
