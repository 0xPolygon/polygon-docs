## Set up wallet contracts

Clone the wallet contracts from the [`zkevm-contracts` repository](https://github.com/0xPolygonHermez/zkevm-contracts) and install the `npm` libraries.

```sh
git clone https://github.com/0xPolygonHermez/zkevm-contracts.git
cd ~/zkevm-contracts
npm i
```

## Create wallets

Next, create a `wallets.js` file.

```sh
cd ~/zkevm-contracts
nano wallets.js
```

Copy/paste the JavaScript code below.

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

```sh
node wallets.js | tee wallets.txt
```

## Prepare deployment configuration

1. Edit the environment variables file.

```bash
cp .env.example .env        # copies .env.example file into .env
nano .env                   # opens .env file for editing
```

2. Set the following variables.

```sh
`MNEMONIC`="..."              # from wallets.txt Deployment Address mnemonic
`INFURA_API_KEY`="..."     # your API Key from Infura account
`ETHERSCAN_API_KEY`="..."     # your Etherscan API key
```

3. Send 0.5 GöETH to the deployment address wallet listed in `wallets.txt`.

## Deploy contracts

```sh
cd ~/zkevm-contracts/
npm i @openzeppelin/hardhat-upgrades
npm run deploy:deployer:ZkEVM:goerli
npm run verify:deployer:ZkEVM:goerli
npm run deploy:testnet:ZkEVM:goerli
npm run verify:ZkEVM:goerli
```

The scripts  auto-deploy the MATIC token contract and the `zkEVMDeployer` contract if required.

4. Check the deployment was successful on Etherscan.

```html
https://goerli.etherscan.io/address/0x -> Put the Deployment Address wallet from
wallets.txt
```