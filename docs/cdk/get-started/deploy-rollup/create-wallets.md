## Set up wallet contracts

Clone the wallet contracts from the [`zkevm-contracts` repository](https://github.com/0xPolygonHermez/zkevm-contracts) and install the `npm` libraries.

```sh
git clone https://github.com/0xPolygonHermez/zkevm-contracts.git
cd ~/zkevm-contracts
npm i
```

## Create wallets

1. Create a `wallets.js` file.

    ```sh
    cd ~/zkevm-contracts
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
        console.log(`PrvKey: ${wallet._signingKey().privateKey}`);
        console.log(`mnemonic: "${wallet._mnemonic().phrase}"`);

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
    `MNEMONIC`="..."            # from wallets.txt Deployment Address mnemonic
    `INFURA_API_KEY`="..."      # your API Key from Infura account
    `ETHERSCAN_API_KEY`="..."   # your Etherscan API key
    ```

3. Send 0.5 GöETH to the deployment address wallet listed in `wallets.txt`.

## Edit deployment configuration

1. Open the `deploy-parameters.json` file.

    ```sh
    cd ~/zkevm-contracts/deployment
    cp deploy_parameters.json.example deploy_parameters.json
    nano deploy_parameters.json
    ```

2. Edit the following parameters to match the generated wallet parameters.

    - `trustedSequencer`: trusted sequencer address in `wallets.txt`.
    - `trustedAggregator`: trusted aggregated address in `wallets.txt`.
    - `admin`: deployment address in `wallets.txt`.
    - `zkEVMOwner`: deployment address in `wallets.txt`.
    - `timelockAddress`: deployment address in `wallets.txt`.
    - `initialZkEVMDeployer`: deployment address in `wallets.txt`.  

## Deploy contracts

1. `cd` back to `zkevm-contract` root directory and run the deployment scripts.

    ```sh
    cd ..
    npm i @openzeppelin/hardhat-upgrades
    npm run deploy:deployer:ZkEVM:goerli
    npm run verify:deployer:ZkEVM:goerli
    npm run prepare:testnet:ZkEVM:goerli && npm run deploy:ZkEVM:test:goerli
    npm run verify:ZkEVM:goerli
    ```

    You should output that looks something like this at the start each time:

    ```sh
    > @0xpolygonhermez/zkevm-contracts@3.0.0 deploy:deployer:ZkEVM:goerli
    > npx hardhat run deployment/2_deployPolygonZKEVMDeployer.js --network goerli

    #######################

    polygonZkEVMDeployer deployed on:  0x8c4e69A65f84D5Ee0d83095916706Be74C133571
    ```

    !!! info
        The scripts auto-deploy the MATIC token contract and the `zkEVMDeployer` contract if required.

2. Check the deployment was successful on Etherscan.

    ```html
    https://goerli.etherscan.io/address/[deployment-address] <!-- from `wallets.txt` -->
    ```