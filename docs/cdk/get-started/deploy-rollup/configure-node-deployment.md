## Set up

1. Create some working directories.

    !!! info
        The following commands takes care of directory placements where non-obvious.

    ```sh
    mkdir -p ~/zkevm/data/{statedb,pooldb} ~/zkevm/zkevm-config ~/zkevm/zkevm-node
    ```

2. Populate the directories by fetching data from latest mainnet node release.

    ```sh
    export ZKEVM_NET="mainnet"
    export ZKEVM_DIR="zkevm"
    curl -L https://github.com/0xPolygonHermez/zkevm-node/releases/latest/download/$ZKEVM_NET.zip > $ZKEVM_NET.zip && unzip -o $ZKEVM_NET.zip -d $ZKEVM_DIR && rm $ZKEVM_NET.zip
    ```

3. Copy the `example.env` file into `.env` file and open it for editing.

    ```sh
    export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
    cd ~/zkevm/mainnet
    cp example.env .env
    nano .env
    ```

4. In the `.env` file, set the following:

    ```sh
    ZKEVM_NODE_ETHERMAN_URL = ""  # set valid Goerli RPC endpoint
    ZKEVM_NODE_STATEDB_DATA_DIR = "~/zkevm/data/statedb"
    ZKEVM_NODE_POOLDB_DATA_DIR = "~/zkevm/data/pooldb"
    ```

## Approve MATIC token for sequencer

1. Launch a Hardhat console connected to the Goerli network.

    ```sh
    cd ~/zkevm-contracts
    npx hardhat console --network goerli
    ```

2. Add the extra data and copy/paste the following code into the open console.

    ```js
    const provider = ethers.getDefaultProvider("<GOERLI_RPC_NODE>"); // set Goerli RPC node
    const privateKey = "<TRUSTED_SEQUENCER_PK>"; // from wallet.txt 
    const wallet = new ethers.Wallet(privateKey, provider);

    const maticTokenFactory = await ethers.getContractFactory(
    "ERC20PermitMock",
    provider
    );
    maticTokenContract = maticTokenFactory.attach("<maticTokenAddress>"); // from ~/zkevm-contracts/deployments/goerli_*/deploy_output.json 
    maticTokenContractWallet = maticTokenContract.connect(wallet);
    await maticTokenContractWallet.approve("<polygonZkEVMAddress>", ethers.utils.parseEther("100.0")); // from ~/zkevm-contracts/deployments/goerli_*/deploy_output.json 
    ```

## Configure genesis

1. Copy the `genesis.json` file into the appropriate location.

    ```sh
    cp ~/zkevm-contracts/deployment/genesis.json ~/zkevm/mainnet/config/environments/mainnet/public.genesis.config.json
    ```

2. Copy/paste the json below to the head of the file inputting the data from `~/zkevm/zkevm-contracts/deployments/deploy_output.json`. 

    !!! important
        The `genesisBlockNumber` is called `deploymentBlockNumber` in `deploy_output.json`.

    ```json
    "l1Config" : {
        "chainId": 5,
        "polygonZkEVMAddress": "", 
        "maticTokenAddress": "", 
        "polygonZkEVMGlobalExitRootAddress": ""  
    },
    "genesisBlockNumber": <number-here>,  
    ```

## Update node config

Add the missing parameters in `~/zkevm/mainnet/config/environments/mainnet/public.node.config.toml`.

- `ApiKey` // for Etherscan
- `URL` // for Goerli node

## Add wallet keystores

Copy/paste the keystore value from `wallets.txt` for the sequencer and aggregator respectively into the following files.

```sh
# paste only the keystore value from wallets.txt in each respective file
nano ~/zkevm/zkevm-config/sequencer.keystore
nano ~/zkevm/zkevm-config/aggregator.keystore
```
