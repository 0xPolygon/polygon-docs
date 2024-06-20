---
comments: true
---

## Set up wallet contracts

Clone the wallet contracts from the [`zkevm-contracts` repository](https://github.com/0xPolygonHermez/zkevm-contracts) and install the `npm` libraries.

```sh
git clone https://github.com/0xPolygonHermez/zkevm-contracts.git
cd zkevm-contracts
npm i
```

## Create wallets

1. Create a `wallets.js` file.

    ```sh
    cd zkevm-contracts
    nano wallets.js
    ```

2. Copy/paste the JavaScript code below.

    ```js
    const ethers = require("ethers");

    async function main() {
      const arrayNames = [
        "## Deployment Address",
        "\\n\\n## Trusted sequencer",
        "\\n\\n## Trusted aggregator",
      ];
      for (let i = 0; i < arrayNames.length; i++) {
        const wallet = ethers.Wallet.createRandom();
        console.log(arrayNames[i]);
        console.log(`Address: ${wallet.address}`);
        console.log(`PrvKey: ${wallet.privateKey}`);
        console.log(`mnemonic: "${wallet.mnemonic.phrase}"`);

        const keystoreJson = await wallet.encrypt("password");
        console.log(`keystore: ${keystoreJson}`);
      }
    }

    main().catch((e) => {
      console.error(e);
      process.exit(1);
    });
    ```

3. Generate the wallets.

    ```sh
    node wallets.js | tee wallets.txt
    ```

## Prepare environment variables

1. Edit the environment variables file.

    ```bash
    cp .env.example .env        # copies .env.example file into .env
    nano .env                   # opens .env file for editing
    ```

2. Set the following variables.

    ```sh
    MNEMONIC="..."            # from wallets.txt Deployment Address mnemonic
    INFURA_API_KEY="..."      # your API Key from Infura account
    ETHERSCAN_API_KEY="..."   # your Etherscan API key
    ```

3. Send 1 Sepolia ETH to the deployment address wallet listed in `wallets.txt`.

## Edit deployment configuration

1. Open the `deploy-parameters.json` file.

    ```sh
    cd zkevm-contracts/deployment/v2
    cp deploy_parameters.json.example deploy_parameters.json
    nano deploy_parameters.json
    ```

2. Edit the following parameters to match the generated wallet parameters.

    - `trustedAggregator`: trusted aggregated address in `wallets.txt`.
    - `admin`: deployment address in `wallets.txt`.
    - `zkEVMOwner`: deployment address in `wallets.txt`.
    - `timelockAddress`: deployment address in `wallets.txt`.
    - `initialZkEVMDeployerAddress`: deployment address in `wallets.txt`.  
    - `zkEVMDeployerAddress`: deployment address in `wallets.txt`.  
    - `emergencyCouncilAddress`: deployment address in `wallets.txt`.
    - `deployerPvtKey`: deployment private key in `wallets.txt`.

3. Open the `create_rollup_parameters.json` file.

    ```bash
    cd zkevm-contracts/deployment/v2
    cp create_rollup_parameters.json.example create_rollup_parameters.json
    vim create_rollup_parameters.json
    ```

4. Edit the following parameters to match the rollup parameters
    - `trustedSequencer`:  trusted sequencer address in `wallets.txt`.
    - `adminZkEVM`: deployment address in `wallets.txt`.
    - `deployerPvtKey`: private key in `wallets.txt`.
## Deploy & verify contracts

`cd` back to `zkevm-contract` root directory and run the deployment scripts.

1. Install Hardhat:

   ```
   cd ..
   npm i @openzeppelin/hardhat-upgrades
   ```

2. Deploy Polygon zkEVM deployer

   ```bash
   npx hardhat run deployment/v2/2_deployPolygonZKEVMDeployer.ts --network sepolia
   ```

   You should see output that looks like this:

   ```bash
   #######################
   
   polygonZkEVMDeployer deployed on:  0xB1A5BA61fBAD71Ba52d70B769d6A994c01b40983
   ```

3. Verify deployer

   ```bash
   npx hardhat run deployment/v2/verifyzkEVMDeployer.js --network sepolia
   ```

   You should see ouput that looks like this:

   ```bash
   The contract 0xB1A5BA61fBAD71Ba52d70B769d6A994c01b40983 has already been verified.
   https://sepolia.etherscan.io/address/0xB1A5BA61fBAD71Ba52d70B769d6A994c01b40983#code
   ```

4. Prepare testnet

   ```bash
   npx hardhat run deployment/testnet/prepareTestnet.ts --network sepolia
   ```

   You should see output that looks like this:

   ```bash
   #######################
   
   pol deployed to: 0x2B2Ef864542EA38657221393B0A18215e5c3fc7e
   ```

   And now if you go to sepolia scan, you should also see that under your account, there's a new `Pol` Erc-20 token created with the balance of `19,900,000` tokens.
