---
comments: true
---

## Set up

1. Create some working directories.

    !!! info
        The following commands take care of directory placements where non-obvious.

    ```sh
    mkdir -p ~/zkevm/data/{statedb,pooldb} ~/zkevm/zkevm-config ~/zkevm/zkevm-node
    ```

2. Populate the directories by fetching data from latest mainnet node release.

    ```sh
    export ZKEVM_NET="mainnet"
    export ZKEVM_DIR="zkevm"
    curl -L https://github.com/0xPolygonHermez/zkevm-node/releases/latest/download/$ZKEVM_NET.zip > $ZKEVM_NET.zip && unzip -o $ZKEVM_NET.zip -d $ZKEVM_DIR && rm $ZKEVM_NET.zip
    ```

3. Go to the `zkevm/zkevm-config` directory and create an `.env` file and open it for editing.

    ```sh
    cd ~/zkevm/zkevm-config/
    nano .env
    ```

4. In the `.env` file, set the following:

    ```sh
    ZKEVM_NODE_ETHERMAN_URL = ""  # set valid Sepolia RPC endpoint
    ZKEVM_NODE_STATEDB_DATA_DIR = "~/zkevm/data/statedb"
    ZKEVM_NODE_POOLDB_DATA_DIR = "~/zkevm/data/pooldb"
    ```

    !!! warning "Workaround if you have configuration issues"
        - You may have to hardcode these variables into the `mainnet/docker-compose.yaml` file.
            - Also, the `ZKEVM_NETWORK` variable which you can set to `mainnet`.
            - Note, there is more than one reference to hardcode in.

## Approve POL token for sequencer

1. Launch a Hardhat console connected to the Sepolia network.

    ```sh
    cd ~/zkevm-contracts
    npx hardhat console --network sepolia
    ```

2. Add the missing data as directed and copy/paste the following code into the open console.

    ```js
    const provider = ethers.getDefaultProvider("<SEPOLIA_RPC_NODE>"); // set Sepolia RPC node
    const privateKey = "<TRUSTED_SEQUENCER_PK>"; // from wallets.txt 
    const wallet = new ethers.Wallet(privateKey, provider);
    
    const polTokenFactory = await ethers.getContractFactory(
    "ERC20PermitMock",
    provider
    );
    polTokenContract = polTokenFactory.attach("<polTokenAddress>"); // from ~/zkevm-contracts/deployments/deploy_output.json 
    polTokenContractWallet = polTokenContract.connect(wallet);
    await polTokenContractWallet.approve("<polygonZkEVMAddress>", ethers.parseEther("100.0")); // from ~/zkevm-contracts/deployments/deploy_output.json 
    ```

## Configure genesis

1. Copy the `genesis.json` file into the appropriate location.

    ```sh
    cp ~/zkevm-contracts/deployment/v2/genesis.json ~/zkevm/mainnet/config/environments/mainnet/public.genesis.config.json
    ```

2. Copy/paste the json below to the head of the `public.genesis.config.json` file inputting the data from `~/zkevm-contracts/deployments/v2/deploy_output.json`. 

    !!! important
        The `genesisBlockNumber` is called `deploymentBlockNumber` in `deploy_output.json`.

    ```json
    "l1Config" : {
        "chainId": 11155111,
        "polygonZkEVMAddress": "", 
        "polTokenAddress": "", 
        "polygonZkEVMGlobalExitRootAddress": ""  
    },
    "genesisBlockNumber": <number-here>,  
    ```

## Update node config

Add the following missing parameters to the `~/zkevm/mainnet/config/environments/mainnet/public.node.config.toml` file.

!!! warning
    If you're having trouble locating the configuration file, try looking for `node.config.toml`, since it may exist under that name in some cases. Once you've added the missing parameters, rename the file to `public.node.config.toml`.

- `ApiKey`  # for Etherscan
- `URL`     # for Sepolia node, under [ETHERMAN]

## Add wallet keystores

Copy/paste the keystore value from `wallets.txt` for the sequencer and aggregator respectively into the following files.

```sh
# paste only the keystore value from wallets.txt in each respective file
nano ~/zkevm/zkevm-config/sequencer.keystore
nano ~/zkevm/zkevm-config/aggregator.keystore
```
