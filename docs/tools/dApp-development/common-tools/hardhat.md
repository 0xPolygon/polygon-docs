---
comments: true
---

## Overview

Hardhat is an Ethereum development environment for deploying smart contracts, running tests, and debugging Solidity code locally.

In this tutorial, you will learn how to set up Hardhat and use it to build, test, and deploy a simple smart contract.

## Set up

1. Ensure you have installed the following:

- [Node.js v10+ LTS and npm](https://nodejs.org/en/).
- [Git](https://git-scm.com/).

2. Create an npm project

```sh
mkdir hardhat-test
cd hardhat-test/
npm init
```

3. Now install Hardhat.

```sh
npm install --save-dev hardhat
```

!!! note
    The sample project used here comes from the [Hardhat Quickstart guide](https://hardhat.org/getting-started/#quick-start), as well as its instructions.

## Creating a project

To create a sample project, run `npx hardhat` in your project folder. You should see the following prompt:

![img](../../../img/tools/hardhat/quickstart.png)

Choose the JavaScript project and go through these steps to compile, test and deploy the sample contract.

### Checking the contract

The `contracts` folder contains `Lock.sol`, which is a sample contract which consists of a simple digital lock, where users could only withdraw funds after a given period of time.

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// Import this file to use console.log
import "hardhat/console.sol";

contract Lock {
    uint public unlockTime;
    address payable public owner;

    event Withdrawal(uint amount, uint when);

    constructor(uint _unlockTime) payable {
        require(
            block.timestamp < _unlockTime,
            "Unlock time should be in the future"
        );

        unlockTime = _unlockTime;
        owner = payable(msg.sender);
    }

    function withdraw() public {
        // Uncomment this line to print a log in your terminal
        // console.log("Unlock time is %o and block timestamp is %o", unlockTime, block.timestamp);

        require(block.timestamp >= unlockTime, "You can't withdraw yet");
        require(msg.sender == owner, "You aren't the owner");

        emit Withdrawal(address(this).balance, block.timestamp);

        owner.transfer(address(this).balance);
    }
}
```

### Setting up the contract

- Go to `hardhat.config.js`
- Update the `hardhat-config` with matic-network-credentials
- Create `.env` file in the root to store your private key
- Add Polygonscan API key to `.env` file to verify the contract on Polygonscan. You can generate an API key by [creating an account](https://polygonscan.com/register)

```js
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");

module.exports = {
  defaultNetwork: "polygon_amoy",
  networks: {
    hardhat: {
    },
    polygon_amoy: {
      url: "https://rpc-amoy.polygon.technology",
      accounts: [process.env.PRIVATE_KEY]
    }
  },
  etherscan: {
    apiKey: process.env.POLYGONSCAN_API_KEY
  },
  solidity: {
    version: "0.8.9",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
}
```

!!! note
    Note that the file above requires DOTENV, for managing environment variables and also ethers and etherscan. Make sure to install all those packages.

    Find more instructions on how to use DOTENV on [this page](https://www.npmjs.com/package/dotenv).

### Compiling the contract

To compile the contract, you first need to install Hardhat:

```bash
npm install --save-dev @nomicfoundation/hardhat-toolbox
```

Then, simply run to compile:

```bash
npx hardhat compile
```

### Testing the contract

To run tests with Hardhat, you just need to type the following:

```bash
npx hardhat test
```

And this is an expected output:

![img](../../../img/tools/hardhat/test.png)

### Deploying on Polygon network

Run this command in root of the project directory:

```bash
npx hardhat run scripts/deploy.js --network polygon_amoy
```

The contract will be deployed on Polygon Amoy testnet, and you can check the deployment status here: <https://amoy.polygonscan.com/>

**Congratulations! You have successfully deployed Greeter Smart Contract. Now you can interact with the Smart Contract.**

!!! tip "Quickly verify contracts on Polygonscan"

    Run the following commands to quickly verify your contract on Polygonscan. This makes it easy for anyone to see the source code of your deployed contract. For contracts that have a constructor with a complex argument list, see [here](https://hardhat.org/plugins/nomiclabs-hardhat-etherscan.html).

    ```bash
    npm install --save-dev @nomiclabs/hardhat-etherscan
    npx hardhat verify --network polygon_amoy 0x4b75233D4FacbAa94264930aC26f9983e50C11AF
    ```
