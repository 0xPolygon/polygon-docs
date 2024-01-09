
Continue with the **third step** of this deployment-guide where you create wallets and deploy contracts.

## Deploying contracts

Clone the contracts from our [github repository](https://github.com/0xPolygonHermez/zkevm-contracts):

```bash
cd ~
git clone https://github.com/0xPolygonHermez/zkevm-contracts.git
cd ~/zkevm-contracts
npm i
```

### Create wallets

Next, create a `wallets.js` file with the following content:

```bash
cd ~/zkevm-contracts
vim wallets.js
```

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

Generate the wallets using below command:

```bash
node wallets.js | tee wallets.txt
```

### Prepare deploy configuration

Edit the environment variables:

```bash
cp .env.example .env        # copies .env.example file into .env
nano .env                   # opens .env file for editing
```

Set these variables:

```bash
cd ~/zkevm-contracts
cp .env.example .env
vim .env
```

Set these variables within your .env file:

```bash
MNEMONIC="..."              # from wallets.txt Deployment Address mnemonic
INFURA_PROJECT_ID="..."     # your API Key from Infura account
ETHERSCAN_API_KEY="..."     # your Etherscan API key
```

Next, open the `deploy_parameters.json` file in vim editor:

```bash
cd ~/zkevm-contracts/deployment
cp deploy_parameters.json.example deploy_parameters.json
vim deploy_parameters.json
```

Only fill in the commented fields in your `deploy_parameters.json` file:

```json
{
  "realVerifier": true,
  "trustedSequencerURL": "<http://X.X.X.X:8545>", // your public IP
  "networkName": "zkevm",
  "version": "0.0.1",
  "trustedSequencer": "", // from wallets.txt Trusted Sequencer address
  "chainID": 42069, // put any id you prefer
  "trustedAggregator": "", // from wallets.txt Trusted Aggregator address
  "trustedAggregatorTimeout": 604799,
  "pendingStateTimeout": 604799,
  "forkID": 4,
  "admin": "", // from wallets.txt Deployment Address  address
  "zkEVMOwner": "", // from wallets.txt Deployment Address address
  "timelockAddress": "", // from wallets.txt Deployment Address address
  "minDelayTimelock": 1,
  "salt": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "initialZkEVMDeployerOwner": "", // from wallets.txt Deployment Address address
  "maticTokenAddress": "", // put existing contract address or leave empty to auto-deploy a new contract
  "zkEVMDeployerAddress": "", // put existing contract address or leave empty to auto-deploy a new contract
  "deployerPvtKey": "",
  "maxFeePerGas": "",
  "maxPriorityFeePerGas": "",
  "multiplierGas": ""
}
```

!!!caution
    Get some GöETH

    You will need to send 0.5 GöETH to the Deployment Address wallet listed in `wallets.txt`.

Adjust the `gasPrice` according to the network status. For Goerli, you can check it with the following command, where you insert your Etherscan API key, note this can sometimes be 0 for testnet:

```bash
ETHERSCAN_API_KEY="YOUR_ETHERSCAN_API_KEY" echo "$(($(printf "%d\\n" $(curl -s "https://api-goerli.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=$ETHERSCAN_API_KEY" | jq -r .result))/1000000000)) Gwei"
```

Edit `~/zkevm/zkevm-contracts/deployment/helpers/deployment-helpers.js` to adjust the `gasPrice` according to network status. It is recommended to add 50 Gwei to the current `gasPrice` to ensure transactions are processed quickly.

```js
vim ~/zkevm-contracts/deployment/helpers/deployment-helpers.js
const gasPriceKeylessDeployment = "50"; // 50 gwei
```

### Deploy contracts

```bash
cd ~/zkevm-contracts/
npm i @openzeppelin/hardhat-upgrades
npm run deploy:deployer:ZkEVM:goerli
npm run verify:deployer:ZkEVM:goerli
npm run deploy:testnet:ZkEVM:goerli
npm run verify:ZkEVM:goerli
```

The previous scripts will auto-deploy the MATIC token contract and the `zkEVMDeployer` contract if required.

You will see in the logs the verification of each smart contract deployed, but you can check it on etherscan too.

```html
https://goerli.etherscan.io/address/0x -> Put the Deployment Address wallet from
wallets.txt
```
