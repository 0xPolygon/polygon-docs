---
comments: true
---

## Configure deployment parameters

1. Navigate to the contracts deployment directory.

    ```sh
    cd ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment
    ```

2. Run the following `jq` script to streamline the process of replacing the fields with the `/tmp/cdk/.env` data:

    ```bash
    source /tmp/cdk/.env
    jq --arg TEST_ADDRESS "$TEST_ADDRESS" '.trustedSequencerURL = "http://127.0.0.1:8123" | .trustedSequencer = $TEST_ADDRESS | .trustedAggregator = $TEST_ADDRESS | .admin = $TEST_ADDRESS | .cdkValidiumOwner = $TEST_ADDRESS | .initialCDKValidiumDeployerOwner = $TEST_ADDRESS | .timelockAddress = $TEST_ADDRESS | .forkID = 6' ./deploy_parameters.json.example > ./deploy_parameters.json
    ```

3. The complete `deploy_parameters.json` should look something like this, where all the addresses are equal to the generated address except for `maticTokenAddress`:

    ```bash
    nano ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/deploy_parameters.json
    # ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/deploy_parameters.json
    {
        "realVerifier": false,
        "trustedSequencerURL": "http://127.0.0.1:8123,
        "networkName": "cdk-validium",
        "version":"0.0.1",
        "trustedSequencer":"0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "chainID": 1001,
        "trustedAggregator":"0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "trustedAggregatorTimeout": 604799,
        "pendingStateTimeout": 604799,
        "forkID": 6,
        "admin":"0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "cdkValidiumOwner": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "timelockAddress": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "minDelayTimelock": 3600,
        "salt": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "initialCDKValidiumDeployerOwner" :"0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
        "maticTokenAddress":"0x617b3a3528F9cDd6630fd3301B9c8911F7Bf063D",
        "cdkValidiumDeployerAddress":"",
        "deployerPvtKey": "",
        "maxFeePerGas":"",
        "maxPriorityFeePerGas":"",
        "multiplierGas": "",
        "setupEmptyCommittee": true,
        "committeeTimelock": false
    }
    ```

## Deploy contracts

### `CDKValidiumDeployer`

This is a factory contract that deploys the deterministic contracts required by the system and must be deployed first. 

The address of the contracts it creates depends on the salt and the `initialCDKValidiumDeployerOwner` inside `deploy_parameters.json`.

1. From the same `deployment` directory you were already in, run the deploy script.

    ```bash 
    npm run deploy:deployer:CDKValidium:sepolia
    ```

    You should see something similar to this:

    ```bash
    cdkValidiumDeployer deployed on:  0x87572242776ccb6c98F4Cf1ff20f7e5a4e4142fF
    ```

2. Now we can deploy the rest of the contract suite.

    ```bash
    npm run deploy:testnet:CDKValidium:sepolia
    ```

    !!! info
        This may take several minutes depending on network conditions.

    !!! warning
        If you see this message, you can safely ignore it:
        
        ```sh
        cp: cannot stat '.openzeppelin/sepolia.json': No such file or directory
        ```

3. On successful deployment, you should see a new directory named `deployments` containing a directory storing the information about your deployment. For example:

    ```bash
    # ~/cdk-validium/cdk-validium-contracts-0.0.2/deployments/sepolia_1705429054/deploy_output.json
    {
    "cdkValidiumAddress": "0x37eEBCa90363b0952e03a64979B64AAE3b8C9631",
    "polygonZkEVMBridgeAddress": "0x3485bfA6F27e54a8FF9782032fdbC7C555c178E4",
    "polygonZkEVMGlobalExitRootAddress": "0x8330E90c82F4BDDfa038041B898DE2d900e6246C",
    "cdkDataCommitteeContract": "0xb49d901748c3E278a634c05E0c500b23db992fb0",
    "maticTokenAddress": "0x20db28Bb7C779a06E4081e55808cc5DE35cca303",
    "verifierAddress": "0xb01Be1534d1eF82Ba98DCd5B33A3A331B6d119D0",
    "cdkValidiumDeployerContract": "0x87572242776ccb6c98F4Cf1ff20f7e5a4e4142fF",
    "deployerAddress": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
    "timelockContractAddress": "0xDa476BD0B6A660cd08239dEb620F701877688c6F",
    "deploymentBlockNumber": 5097689,
    "genesisRoot": "0xf07cd7c4f7df7092241ccb2072d9ac9e800a87513df628245657950b3af78f94",
    "trustedSequencer": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
    "trustedSequencerURL": "http://127.0.0.1:8123",
    "chainID": 1001,
    "networkName": "cdk-validium",
    "admin": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
    "trustedAggregator": "0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE",
    "proxyAdminAddress": "0x828E55268524c13dB25FD33f2Be45D2771f1EeA4",
    "forkID": 6,
    "salt": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "version": "0.0.1"
    }
    ```

4. In the  `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/` folder, you should also see a `genesis.json` file. 

    !!! info
        We use the info in `genesis.json` and `deploy_output.json` to configure the `cdk-validium-node` node.

    !!! warning "Deployment failure"
        - Since there are deterministic addresses, you cannot deploy twice on the same network using the same `salt` and `initialCDKValidiumDeployerOwner` inside `deploy_parameters.json`. Changing one of them is enough to make a new deployment.
        - It's mandatory to delete the `~/cdk-validium/cdk-validium-contracts-0.0.2/.openzeppelin` upgradability information in order to make a new deployment.

## Verify contracts

When deploying to Sepolia, the contracts should automatically verify based on other live deployments on the network with similar bytecode. If the contracts have not been verified on Etherscan, run the following commands from the `/cdk-validium/cdk-validium-contracts-0.0.2/deployment` directory.

1. To verify the contract factory:

    ```bash
    npm run verify:deployer:CDKValidium:sepolia
    ```

2. To verify the rest of the contract suite:

    ```bash
    npm run verify:CDKValidium:sepolia
    ```

## Use a different node provider

If you would rather use a different node provider than Infura, modify the contents of `~/cdk-validium/cdk-validium-contracts-0.0.2/hardhat.config.js` and `cdk-validium-contracts-0.0.2/.env` .

For example, using Alchemy:

```bash
MNEMONIC="test test test test test test test test test test test junk"
INFURA_PROJECT_ID="" # leave blank when not using Infura
ETHERSCAN_API_KEY="" # or blank if not verifying contracts
ALCHEMY_PROJECT_ID="" # add the Alchemy data here
```

```bash
sepolia: {
      url: `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_PROJECT_ID}`, # rpc value changed here
      accounts: {
        mnemonic: process.env.MNEMONIC || DEFAULT_MNEMONIC,
        path: "m/44'/60'/0'/0",
        initialIndex: 0,
        count: 20,
      },
    },
```

## Steps to run the node and services

You are now ready to begin the [CDK validum node and services deployment steps](../node/prerequisites.md).