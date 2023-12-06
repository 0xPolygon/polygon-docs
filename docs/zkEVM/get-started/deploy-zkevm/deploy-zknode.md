
Continue with the **fourth step** of this deployment-guide where you deploy the zkNode.

## zkNode deployment

First, create the following directories:

```bash
mkdir -p ~/zkevm/data/{statedb,pooldb} ~/zkevm/zkevm-config ~/zkevm/zkevm-node
```

Next, populate the directories by fetching data from latest node releases, for example with mainnet:

```bash
export ZKEVM_NET="mainnet"
export ZKEVM_DIR="zkevm"
curl -L https://github.com/0xPolygonHermez/zkevm-node/releases/latest/download/$ZKEVM_NET.zip > $ZKEVM_NET.zip && unzip -o $ZKEVM_NET.zip -d $ZKEVM_DIR && rm $ZKEVM_NET.zip
```

Copy the `example.env` file into `.env` file and open in editor:

```bash
export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
cp ~/$ZKEVM_DIR/$ZKEVM_NET/example.env $ZKEVM_CONFIG_DIR/.env
vim $ZKEVM_CONFIG_DIR/.env
```

In the `.env` file, set:

```bash
ZKEVM_NODE_ETHERMAN_URL = "http://localhost:8845"  # set valid Geth Goerli RPC endpoint
ZKEVM_NODE_STATEDB_DATA_DIR = "~/zkevm/data/statedb"
ZKEVM_NODE_POOLDB_DATA_DIR = "~/zkevm/data/pooldb"
```

### Approve MATIC token for sequencer

Run the below command to launch a Hardhat console connected to the Goerli network.

```bash
cd ~/zkevm-contracts
npx hardhat console --network goerli
```

Here, you can utilize the JavaScript environment to interact with the Goerli network. In the console, run the following (you can copy all the code in one go):

```js
const provider = ethers.getDefaultProvider("http://localhost:8845"); // set Geth Goerli RPC node
const privateKey = ""; // From wallet.txt Trusted Sequencer prvkey
const wallet = new ethers.Wallet(privateKey, provider);

const maticTokenFactory = await ethers.getContractFactory(
  "ERC20PermitMock",
  provider
);
maticTokenContract = maticTokenFactory.attach(""); // From ~/zkevm-contracts/deployments/goerli_*/deploy_output.json maticTokenAddress
maticTokenContractWallet = maticTokenContract.connect(wallet);
await maticTokenContractWallet.approve("", ethers.utils.parseEther("100.0")); // From ~/zkevm-contracts/deployments/goerli_*/deploy_output.json polygonZkEVMAddress
```

### Configure genesis

Run the below commands to copy `genesis.json` file into appropriate location and open for editing:

```bash
cp ~/zkevm-contracts/deployments/goerli_*/genesis.json ~/zkevm/mainnet/config/environments/testnet/public.genesis.config.json
vim ~/zkevm/mainnet/config/environments/testnet/public.genesis.config.json
```

Edit the file changing the following parameters from `~/zkevm/zkevm-contracts/deployments/goerli_***/deploy_output.json`. **Keep in mind that `genesisBlockNumber` is called `deploymentBlockNumber` in `deploy_output.json`**.

```json
"l1Config" : {
    "chainId": 5,
    "polygonZkEVMAddress": "", // From ~/zkevm-contracts/deployments/goerli_*/deploy_output.json polygonZkEVMAddress
    "maticTokenAddress": "", // From ~/zkevm-contracts/deployments/goerli_*/deploy_output.json maticTokenAddress
    "polygonZkEVMGlobalExitRootAddress": ""  // polygonZkEVMGlobalExitRootAddress from ~/zkevm/zkevm-contracts/deployments/goerli_*/deploy_output.json
  },
 "genesisBlockNumber": 9500870,  // deploymentBlockNumber from ~/zkevm/zkevm-contracts
# add above to head of file, leave all remaining fields intact
```

### Update node config file

Edit `~/zkevm/mainnet/config/environments/testnet/public.node.config.toml` with the following values. The config file is large and we'll update the documentation in the future to list only the updated parameters.

??? "Click to expand the <code>node.config.toml</code> file"
    ```bash
    vim ~/zkevm/mainnet/config/environments/testnet/public.node.config.toml

```

    ```bash
    IsTrustedSequencer = true
    [Log]
    Environment = "development"
    Level = "debug"
    Outputs = ["stderr","stdout"]

    [StateDB]
    User = "state_user"
    Password = "state_password"
    Name = "state_db"
    Host = "zkevm-state-db"
    Port = "5432"
    EnableLog = false
    MaxConns = 200

    [Pool]
    FreeClaimGasLimit = 1500000
    MaxTxBytesSize=30132
    MaxTxDataBytesSize=30000
    DefaultMinGasPriceAllowed = 1000000000
    MinAllowedGasPriceInterval = "5m"
    PollMinAllowedGasPriceInterval = "15s"
        [Pool.DB]
        User = "pool_user"
        Password = "pool_password"
        Name = "pool_db"
        Host = "zkevm-pool-db"
        Port = "5432"
        EnableLog = false
        MaxConns = 200
    [Etherman]
    URL = "http://localhost:8845"    # put a valid Goerli node
    MultiGasProvider = false
    L1URL = "http://localhost:8845"  # put a valid Goerli node
    L2URLs = ["http://X.X.X.X:8545"]  # your public IP
        [Etherman.Etherscan]
        ApiKey = ""     # Etherscan API key
    
    [RPC]
    Host = "0.0.0.0"
    Port = 8545
    ReadTimeoutInSec = 60
    WriteTimeoutInSec = 60
    MaxRequestsPerIPAndSecond = 5000
    SequencerNodeURI = ""
    BroadcastURI = "http://3.144.195.147:61090"
    DefaultSenderAddress = "0x1111111111111111111111111111111111111111"
    EnableL2SuggestedGasPricePolling = true
        [RPC.WebSockets]
                Enabled = true
                Port = 8546
    [Synchronizer]
    SyncInterval = "5s"
    SyncChunkSize = 500
    trustedSequencerURL = "http://X.X.X.X:8545"  # your public IP
    
    [MTClient]
    URI = "zkevm-prover:50061"

    [Executor]
    URI = "zkevm-prover:50071"
    
    [Metrics]
    Host = "0.0.0.0"
    Port = 9091
    Enabled = true
    ProfilingHost = "0.0.0.0"
    ProfilingPort = 6060
    ProfilingEnabled = false
    
    [Sequencer]
    WaitPeriodPoolIsEmpty = "1s"
    WaitPeriodSendSequence = "15s"
    LastBatchVirtualizationTimeMaxWaitPeriod = "10s"
    BlocksAmountForTxsToBeDeleted = 100
    FrequencyToCheckTxsForDelete = "12h"
    MaxTxsPerBatch = 150
    MaxBatchBytesSize = 129848
    MaxCumulativeGasUsed = 30000000
    MaxKeccakHashes = 468
    MaxPoseidonHashes = 279620
    MaxPoseidonPaddings = 149796
    MaxMemAligns = 262144
    MaxArithmetics = 262144
    MaxBinaries = 262144
    MaxSteps = 8388608
    WeightBatchBytesSize = 1
    WeightCumulativeGasUsed = 1
    WeightKeccakHashes = 1
    WeightPoseidonHashes = 1
    WeightPoseidonPaddings = 1
    WeightMemAligns = 1
    WeightArithmetics = 1
    WeightBinaries = 1
    WeightSteps = 1
    TxLifetimeCheckTimeout = "10m"
    MaxTxLifetime = "3h"
    MaxTxSizeForL1 = 131072
        [Sequencer.Finalizer]
                GERDeadlineTimeoutInSec = "2s"
                ForcedBatchDeadlineTimeoutInSec = "60s"
                SendingToL1DeadlineTimeoutInSec = "20s"
                SleepDurationInMs = "100ms"
                ResourcePercentageToCloseBatch = 10
                GERFinalityNumberOfBlocks = 0
                ClosingSignalsManagerWaitForCheckingL1Timeout = "10s"
                ClosingSignalsManagerWaitForCheckingGER = "10s"
                ClosingSignalsManagerWaitForCheckingForcedBatches = "10s"
                ForcedBatchesFinalityNumberOfBlocks = 0
                TimestampResolution = "15s"
        [Sequencer.DBManager]
                PoolRetrievalInterval = "500ms"
        [Sequencer.Worker]
                ResourceCostMultiplier = 1000
    [SequenceSender]
    WaitPeriodSendSequence = "5s"
    LastBatchVirtualizationTimeMaxWaitPeriod = "5s"
    MaxTxSizeForL1 = 131072
    SenderAddress = ""  # trustedSequencer address from deploy_output.json
    PrivateKeys = [{Path = "/pk/sequencer.keystore", Password = "password"}]
    
    [Aggregator]
    Host = "0.0.0.0"
    Port = 50081
    ForkId = 4
    RetryTime = "5s"
    VerifyProofInterval = "30s"
    TxProfitabilityCheckerType = "acceptall"
    TxProfitabilityMinReward = "1.1"
    ProofStatePollingInterval = "5s"
    SenderAddress = ""  # trustedAggregator address from deploy_output.json
    CleanupLockedProofsInterval = "2m"
    GeneratingProofCleanupThreshold = "10m"
    
    [EthTxManager]
    ForcedGas = 0
    PrivateKeys = [
        {Path = "/pk/sequencer.keystore", Password = "password"},
        {Path = "/pk/aggregator.keystore", Password = "password"}
        ]
    [Database]
    Database = "postgres"
    User = "test_user"
    Password = "test_password"
    Name = "test_db"
    Host = "zkevm-bridge-db"
    Port = "5435"
    MaxConns = 20
    
    [BridgeController]
    Store = "postgres"
    Height = 32
    
    [BridgeServer]
    GRPCPort = "9090"
    HTTPPort = "8080"
    
    [NetworkConfig]
    GenBlockNumber = 9500870     # deploymentBlockNumber from deploy_output.json
    PolygonZkEVMAddress = ""  # polygonZkEVMAddress from deploy_output.json
    PolygonBridgeAddress = ""  # PolygonZkEVMBridge from genesis.json
    PolygonZkEVMGlobalExitRootAddress = ""  # polygonZkEVMGlobalExitRootAddress from deploy_output.json
    MaticTokenAddress = ""  # maticTokenAddress from deploy_output.json
    L2PolygonBridgeAddresses = [""]  # PolygonZkEVMBridge from genesis.json
    L1ChainID = 5  # Goerli chainID
    
    [L2GasPriceSuggester]
    Type = "default"
    DefaultGasPriceWei = 100000000
    
    [ClaimTxManager]
    FrequencyToMonitorTxs = "1s"
    PrivateKey = {Path = "/pk/sequencer.keystore", Password = "password"}
    Enabled = true
    ```

### Add wallets

Copy/paste keystore value from wallets.txt for sequencer/aggregator respectively:

```bash
# paste only the keystore value from wallets.txt in each respective file
vim ~/zkevm/zkevm-config/sequencer.keystore
vim ~/zkevm/zkevm-config/aggregator.keystore
```
