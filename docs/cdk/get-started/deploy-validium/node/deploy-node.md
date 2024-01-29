| Repo | Version |
| --- | --- |
| https://github.com/0xPolygon/cdk-validium-contracts/releases/tag/v0.0.2 | v0.0.2 |
| https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.0.3 | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-prover | v3.0.2 |
| https://github.com/0xPolygon/cdk-data-availability.git | v0.0.3 |
| https://github.com/0xPolygonHermez/zkevm-bridge-service | v0.3.1 |

The listed version may not be the most recent, but this will give a general idea of how the deployment process works.

# Prerequisites

### Minimum Requirements:

| Minimum Disk Size | vCPUs | Memory (GB) | CPU Type | Architecture | OS |
| --- | --- | --- | --- | --- | --- |
| 32GB | 2 | 8 | Intel or AMD | x86/64 | Ubuntu 22.04 |

Your operating system should be Linux-based (preferably Ubuntu 22.04), and it must have an AMD or Intel chip.

Lastly, make sure you have at least `~0.3 Sepolia ETH` ready for deploying contracts and various contract calls.

## Dependency Checking

| Dependency | Version | Installation links |
| --- | --- | --- |
| git | 2.18.0 | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git |
| node | 16.0.0 | https://nodejs.org/en/download |
| npm | 6.0.0 | https://docs.npmjs.com/downloading-and-installing-node-js-and-npm |
| golang | 1.18.0 | https://go.dev/doc/install |
| cast | 0.2.0 | https://book.getfoundry.sh/getting-started/installation |
| jq | 1.0 | https://jqlang.github.io/jq/download/ |
| tomlq | 3.0.0 | https://kislyuk.github.io/yq/#installation |
| postgres | 15 | https://www.postgresql.org/download/ |
| psql | 15.0 | https://www.postgresql.org/download/ |
| make | 3.80.0 | https://www.gnu.org/software/make/ |
| docker | 24.0.0 | https://docs.docker.com/engine/install/ |
| pip3 | 20.0.0 | https://pip.pypa.io/en/stable/installation/ |
| [For Testing] python3 | 3.8.0 | https://www.python.org/downloads/ |
| [For Testing] polycli | 0.1.39 | https://github.com/maticnetwork/polygon-cli/tree/main |
- You can run the following script to validate that dependency requirements are met:
    
    ```bash
    #!/bin/bash
    
    declare -A commands
    commands["git"]="2.18.0"
    commands["node"]="16.0.0"
    commands["npm"]="6.0.0"
    commands["go"]="1.18.0"
    commands["cast"]="0.2.0"
    commands["jq"]="1.0"
    commands["tomlq"]="3.0.0"
    commands["psql"]="15.0"
    commands["make"]="3.80.0"
    commands["docker"]="24.0.0"
    commands["pip3"]="20.0.2"
    commands["python3"]="3.8.0"
    commands["polycli"]="0.1.39"
    
    # Function to check command version
    check_version() {
        local command=$1
        local min_version=$2
        local version
        local status
    
        if ! command -v "$command" &> /dev/null; then
            printf "| %-15s | %-20s | %-20s |\n" "$command" "Not Found" "$min_version"
            return
        fi
    
        case "$command" in
            git) version=$(git --version | awk '{print $3}') ;;
            node) version=$(node --version | cut -d v -f 2) ;;
            npm) version=$(npm --version) ;;
            go) version=$(go version | awk '{print $3}' | cut -d 'o' -f 2) ;;
            cast) version=$(cast --version | awk '{print $2}') ;;
            jq) version=$(jq --version | cut -d '-' -f 2) ;;
            tomlq) version=$(tomlq --version | awk '{print $2}') ;;
            psql) version=$(psql --version | awk '{print $3}') ;;
            make) version=$(make --version | head -n 1 | awk '{print $3}') ;;
            docker) version=$(docker --version | awk '{print $3}' | cut -d ',' -f 1) ;;
            pip3) version=$(pip3 --version | awk '{print $2}') ;;
            python3) version=$(python3 --version | awk '{print $2}') ;;
            polycli) version=$(polycli version | awk '{print $4}' | cut -d '-' -f 1 | sed 's/v//') ;;
            *) version="Found" ;;
        esac
    
        printf "| %-15s | %-20s | %-20s |\n" "$command" "$version" "$min_version"
    }
    
    echo "+-----------------+----------------------+----------------------+"
    printf "| %-15s | %-20s | %-20s |\n" "CLI Command" "Found Version" "Minimum Version"
    echo "+-----------------+----------------------+----------------------+"
    
    for cmd in "${!commands[@]}"; do
        check_version "$cmd" "${commands[$cmd]}"
        echo "+-----------------+----------------------+----------------------+"
    done
    ```
    
    You can create a `version-check.sh` file, then copy and paste the script into that file. Then run the following to execute the script:
    
    ```bash
    chmod +x version-check.sh
    ./version-check.sh
    ```
    

# Setup & Deployment

First, lets navigate back to the working directory we created earlier, `~/cdk-validium`

```bash
cd ~/cdk-validium
```

For this setup, we will also need our information from `deploy_output.json` inside `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment`. Navigate back to `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment` and run the following script to fill the required parameters into the `/tmp/cdk/.env` we created in the previous steps:

```bash
cd ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment
echo "GEN_BLOCK_NUMBER=$(jq -r '.deploymentBlockNumber' deploy_output.json)" >> /tmp/cdk/.env
echo "CDK_VALIDIUM_ADDRESS=$(jq -r '.cdkValidiumAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "POLYGON_ZKEVM_BRIDGE_ADDRESS=$(jq -r '.polygonZkEVMBridgeAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS=$(jq -r '.polygonZkEVMGlobalExitRootAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "CDK_DATA_COMMITTEE_CONTRACT_ADDRESS=$(jq -r '.cdkDataCommitteeContract' deploy_output.json)" >> /tmp/cdk/.env
echo "MATIC_TOKEN_ADDRESS=$(jq -r '.maticTokenAddress' deploy_output.json)" >> /tmp/cdk/.env
```

Source our new environment and navigate back to `~/cdk-validium`:

```bash
source /tmp/cdk/.env
cd ~/cdk-validium
```

## 1. Downloading cdk-validium-node, cdk-data-availability, and cdk-bridge-service

Now clone the `0.0.3` release of `cdk-validium-node`. 

```bash
git clone --depth 1 --branch v0.0.3 https://github.com/0xPolygon/cdk-validium-node.git
```

We also must download and extract version `0.0.3` of `cdk-data-availability.` The release file is available here:

[Untitled Database](https://www.notion.so/b329e3b1511943ae979cc2b4c73a35e8?pvs=21)

Downloading `cdk-validium-contracts` as a ***`tar.gz`*** and extracting

```bash
~/cdk-validium % curl -L -o cdk-data-availability.tar.gz https://github.com/0xPolygon/cdk-data-availability/archive/refs/tags/v0.0.3.tar.gz
\tar -xzf cdk-data-availability.tar.gz
```

Finally, the `cdk-bridge-service` release `0.3.1`. The release file can be found here:

```bash
curl -L -o cdk-bridge-service.tar.gz https://github.com/0xPolygonHermez/zkevm-bridge-service/archive/refs/tags/v0.3.1.tar.gz
\tar -xzf cdk-bridge-service.tar.gz

```
Now we have three new directories in *`cdk-validium/`* named ***`cdk-data-availability-0.0.3`, `cdk-validium-node` and `zkevm-bridge-service-0.3.1`***

## 2. Preparing the environment

We will begin our setup in the node directory.

Navigate into the node directory we cloned from the previous step***`cdk-validium-node/`***

```bash
~/cdk-validium % cd cdk-validium-node/
```

### Setup the database

Run the docker command to start an instance of the `psql` database. The database is used for many of the services, such as the node, prover, DAC, and bridge service.

```bash
docker run -e POSTGRES_USER=cdk_user -e POSTGRES_PASSWORD=cdk_password -e POSTGRES_DB=postgres -p 5432:5432 postgres:15
```

*note: if you are unable to start the process because port is in use, check the processes occupying the port then kill the processes*

```bash
sudo lsof -t -i:5432
kill -9 <PID>
```

Once you have postgres running, validate you have the following setup correctly:

- an admin account called: `cdk_user` with a password of `cdk_password`
- postgres server running on `localhost:5432`

You can use the following command to validate the steps, `\q` to exit:

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432
#=> \q
```

### Provision the database

The `cdk-validium-node` directory contains a script called `single_db_server.sql` that provisions all the databases required for the prover, state, and pool to operate. Run the script to provision all the necessary databases and schemas that will be used for both the prover and node:

```bash
~/cdk-validium/cdk-validium-node % PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -a -q -f ./db/scripts/single_db_server.sql
```

In addition to the provisions required for the prover and node, another provision is needed for the Data Availability Committee (DAC). We can set this up now for use later.

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE committee_db;"
```

Finally, we will provision a database for our bridge service, which we will setup last in this guide.

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE bridge_db;"
```

### Configure the prover

To configure our prover, lets copy and modify the contents of `test.prover.config.json` inside `~/cdk-validium/cdk-validium-node/test/config/` to our `/tmp/cdk/` directory we created earlier using the following jq command:

```bash
~/cdk-validium/cdk-validium-node % jq '.aggregatorClientHost = "127.0.0.1" | .databaseURL = "postgresql://cdk_user:cdk_password@localhost:5432/postgres"' ./test/config/test.prover.config.json > /tmp/cdk/test.prover.config.json
```

### Configure the node

To create the configuration files for our node, we first must build the `cdk-validium-node` itself.

```bash
~/cdk-validium/cdk-validium-node % make build
```

Now we can create a keystore. This will be referenced in all of our`config.toml` we create in the next steps. Take the private key we generated and stored in our `.env` earlier and encrypt it with a basic password.

For example:

```bash

$ source /tmp/cdk/.env
$ ./dist/zkevm-node encryptKey --pk=$TEST_PRIVATE_KEY --pw="testonly" --output=/tmp/cdk/account.keystore
$ find /tmp/cdk/account.keystore -type f -name 'UTC--*' | head -n 1 | xargs -I xxx mv xxx /tmp/cdk/account.key
```

*note: make sure your environment is sourced ie: `source /tmp/cdk/.env`*

The output keystore is now stored in `/tmp/cdk/account.keystore`

Create a new file `node-config.toml` inside `/tmp/cdk/` and paste the following content:

Example `node-config.toml`:

```bash
#/tmp/cdk/node-config.toml
IsTrustedSequencer = true

[Log]
Environment = "development" # "production" or "development"
Level = "debug"
Outputs = ["stderr"]

[State]
	[State.DB]
	User = "cdk_user"
	Password = "cdk_password"
	Name = "state_db"
	Host = "localhost"
	Port = "5432"
	EnableLog = false	
	MaxConns = 200
	[State.Batch]
		[State.Batch.Constraints]
		MaxTxsPerBatch = 300
		MaxBatchBytesSize = 120000
		MaxCumulativeGasUsed = 30000000
		MaxKeccakHashes = 2145
		MaxPoseidonHashes = 252357
		MaxPoseidonPaddings = 135191
		MaxMemAligns = 236585
		MaxArithmetics = 236585
		MaxBinaries = 473170
		MaxSteps = 7570538

[Pool]
FreeClaimGasLimit = 1500000
IntervalToRefreshBlockedAddresses = "5m"
IntervalToRefreshGasPrices = "5s"
MaxTxBytesSize=100132
MaxTxDataBytesSize=100000
DefaultMinGasPriceAllowed = 0
MinAllowedGasPriceInterval = "5m"
PollMinAllowedGasPriceInterval = "15s"
AccountQueue = 64
GlobalQueue = 1024
	[Pool.EffectiveGasPrice]
		Enabled = false
		L1GasPriceFactor = 0.25
		ByteGasCost = 16
		ZeroByteGasCost = 4
		NetProfit = 1
	    BreakEvenFactor = 1.1			
		FinalDeviationPct = 10
		L2GasPriceSuggesterFactor = 0.5
	[Pool.DB]
	User = "cdk_user"
	Password = "cdk_password"
	Name = "pool_db"
	Host = "localhost"
	Port = "5432"
	EnableLog = false
	MaxConns = 200

[Etherman]
URL = "https://sepolia.infura.io/v3/bd6164d34c324fa08ca5b6dc1d3ed3a2"
ForkIDChunkSize = 20000
MultiGasProvider = false
	[Etherscan]
		ApiKey = ""

[RPC]
Host = "0.0.0.0"
Port = 8123
ReadTimeout = "60s"
WriteTimeout = "60s"
MaxRequestsPerIPAndSecond = 5000
SequencerNodeURI = ""
BatchRequestsEnabled = true
EnableL2SuggestedGasPricePolling = true
	[RPC.WebSockets]
		Enabled = true
		Port = 8133

[Synchronizer]
SyncInterval = "1s"
SyncChunkSize = 100
TrustedSequencerURL = "" # If it is empty or not specified, then the value is read from the smc.
L1SynchronizationMode = "sequential" # "sequential" or "parallel"
	[Synchronizer.L1ParallelSynchronization]
		MaxClients = 10
		MaxPendingNoProcessedBlocks = 25
		RequestLastBlockPeriod = "5s"
		RequestLastBlockTimeout = "5s"
		RequestLastBlockMaxRetries = 3
		StatisticsPeriod = "5m"
		TimeoutMainLoop = "5m"
		RollupInfoRetriesSpacing= "5s"
		FallbackToSequentialModeOnSynchronized = false
		[Synchronizer.L1ParallelSynchronization.PerformanceWarning]
			AceptableInacctivityTime = "5s"
			ApplyAfterNumRollupReceived = 10

[Sequencer]
WaitPeriodPoolIsEmpty = "1s"
LastBatchVirtualizationTimeMaxWaitPeriod = "10s"
BlocksAmountForTxsToBeDeleted = 100
FrequencyToCheckTxsForDelete = "12h"
TxLifetimeCheckTimeout = "10m"
MaxTxLifetime = "3h"
	[Sequencer.Finalizer]
		GERDeadlineTimeout = "2s"
		ForcedBatchDeadlineTimeout = "5s"
		SleepDuration = "100ms"
		ResourcePercentageToCloseBatch = 10
		GERFinalityNumberOfBlocks = 0
		ClosingSignalsManagerWaitForCheckingL1Timeout = "10s"
		ClosingSignalsManagerWaitForCheckingGER = "10s"
		ClosingSignalsManagerWaitForCheckingForcedBatches = "10s"
		ForcedBatchesFinalityNumberOfBlocks = 0
		TimestampResolution = "10s"
		StopSequencerOnBatchNum = 0
	[Sequencer.DBManager]
		PoolRetrievalInterval = "500ms"
		L2ReorgRetrievalInterval = "5s"

[SequenceSender]
WaitPeriodSendSequence = "15s"
LastBatchVirtualizationTimeMaxWaitPeriod = "10s"
MaxTxSizeForL1 = 131072
L2Coinbase = "0xf100D00c376D62682Faf28FeE5cF603AAED75e13"
PrivateKey = {Path = "/tmp/cdk/account.key", Password = "testonly"}

[Aggregator]
Host = "0.0.0.0"
Port = 50081
RetryTime = "5s"
VerifyProofInterval = "10s"
TxProfitabilityCheckerType = "acceptall"
TxProfitabilityMinReward = "1.1"
ProofStatePollingInterval = "5s"
SenderAddress = "0xf100D00c376D62682Faf28FeE5cF603AAED75e13"
CleanupLockedProofsInterval = "2m"
GeneratingProofCleanupThreshold = "10m"

[EthTxManager]
ForcedGas = 0
PrivateKeys = [
	{Path = "/tmp/cdk/account.key", Password = "testonly"}
]

[L2GasPriceSuggester]
Type = "default"
UpdatePeriod = "10s"
Factor = 0.5
DefaultGasPriceWei = 0
MaxGasPriceWei = 0

[MTClient]
URI  = "localhost:50061"

[Executor]
URI = "localhost:50071"
MaxGRPCMessageSize = 100000000

[Metrics]
Host = "0.0.0.0"
Port = 9091
Enabled = true
ProfilingHost = "0.0.0.0"
ProfilingPort = 6060
ProfilingEnabled = true

[HashDB]
User = "cdk_user"
Password = "cdk_password"
Name = "prover_db"
Host = "localhost"
Port = "5432"
EnableLog = false
MaxConns = 200
```

We will modify the `URL` parameter in`[Etherman]` to the URL of our RPC Provider, along with the parameters `L2Coinbase` in `[SequenceSender]` and `SenderAddress` in `[Aggregator]` to the address we generated earlier. Here’s a script to replace those values automatically using your environment sourced from `/tmp/cdk/`

```bash
source /tmp/cdk/.env
tomlq -i -t --arg L1_URL "$L1_URL" '.Etherman.URL = $L1_URL' /tmp/cdk/node-config.toml
tomlq -i -t --arg TEST_ADDRESS "$TEST_ADDRESS" '.SequenceSender.L2Coinbase = $TEST_ADDRESS' /tmp/cdk/node-config.toml
tomlq -i -t --arg TEST_ADDRESS "$TEST_ADDRESS" '.Aggregator.SenderAddress = $TEST_ADDRESS' /tmp/cdk/node-config.toml
```

Now we have to copy and modify the `genesis.json` from our earlier deployment of contracts to include information about our newly configured chain

You can find `genesis.json` inside `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/`

The values we are going to append to the `genesis.json` would be something like:

```bash
#~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/genesis.json
"L1Config": {
  "chainId": 11155111,
  "maticTokenAddress": "0xd76B50509c1693C7BA35514103a0A156Ca57980c",
  "polygonZkEVMAddress": "0x52C8f9808246eF2ce992c0e1f04fa54ec3378dD1",
  "cdkDataCommitteeContract": "0x8346026951978bd806912d0c93FB0979D8E3436a",
  "polygonZkEVMGlobalExitRootAddress": "0xE3A721c20B30213FEC306dd60f6c7F2fCB8b46D2"
},
"genesisBlockNumber": 5098088
```

Run the following script to automate the process of appending those JSON values:

```bash
jq --argjson data "$(jq '{maticTokenAddress, cdkValidiumAddress, cdkDataCommitteeContract, polygonZkEVMGlobalExitRootAddress, deploymentBlockNumber}' ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/deploy_output.json)" \
'.L1Config.chainId = 11155111 | 
.L1Config.maticTokenAddress = $data.maticTokenAddress | 
.L1Config.polygonZkEVMAddress = $data.cdkValidiumAddress | 
.L1Config.cdkDataCommitteeContract = $data.cdkDataCommitteeContract | 
.L1Config.polygonZkEVMGlobalExitRootAddress = $data.polygonZkEVMGlobalExitRootAddress | 
.genesisBlockNumber = $data.deploymentBlockNumber' ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/genesis.json > /tmp/cdk/genesis.json
```

### Configure the DAC

At this point we have setup and provisioned the psql database and configured the zk prover and node. Now let’s configure our Data Availability Comittee

Navigate into `~/cdk-validium/cdk-data-availability-0.0.3` we downloaded in step 1.

Build the DAC

```bash
~/cdk-validium/cdk-data-availability-0.0.3 % make build
```

Now we can create a `dac-config.toml` file inside `/tmp/cdk/` . Copy and paste the following example config from below, then run the sequential `tomlq` script to replace the necessary parameters.

```bash
#~/tmp/cdk/dac-config.toml
PrivateKey = {Path = "/tmp/cdk/account.key", Password = "testonly"}

[L1]
WsURL = "wss://sepolia.infura.io/ws/v3/bd6164d34c324fa08ca5b6dc1d3ed3a2"
RpcURL = "https://sepolia.infura.io/v3/bd6164d34c324fa08ca5b6dc1d3ed3a2"
CDKValidiumAddress = "0x52C8f9808246eF2ce992c0e1f04fa54ec3378dD1"
DataCommitteeAddress = "0x8346026951978bd806912d0c93FB0979D8E3436a"
Timeout = "3m" # Make sure this value is less than the rootchain-int-ws loadbalancer timeout
RetryPeriod = "5s"

[Log]
Environment = "development" # "production" or "development"
Level = "debug"
Outputs = ["stderr"]

[DB]
User = "cdk_user"
Password = "cdk_password"
Name = "committee_db"
Host = "127.0.0.1"
Port = "5432"
EnableLog = false
MaxConns = 10

[RPC]
Host = "0.0.0.0"
Port = 8444
ReadTimeout = "60s"
WriteTimeout = "60s"
MaxRequestsPerIPAndSecond = 500
SequencerNodeURI = ""
EnableL2SuggestedGasPricePolling = false
	[RPC.WebSockets]
		Enabled = false
```

You can replace the values automatically:

```bash
source /tmp/cdk/.env
tomlq -i -t --arg L1_URL "$L1_URL" '.L1.RpcURL = $L1_URL' /tmp/cdk/dac-config.toml
tomlq -i -t --arg L1_WS_URL "$L1_WS_URL" '.L1.WsURL = $L1_WS_URL' /tmp/cdk/dac-config.toml
tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.L1.CDKValidiumAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/dac-config.toml
tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.L1.DataCommitteeAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/dac-config.toml
```

Now we can update the contracts on Sepolia with information about our DAC

```bash
cast send \
        --legacy \
        --from $TEST_ADDRESS \
        --private-key $TEST_PRIVATE_KEY \
        --rpc-url $L1_URL \
        $CDK_DATA_COMMITTEE_CONTRACT_ADDRESS \
        'function setupCommittee(uint256 _requiredAmountOfSignatures, string[] urls, bytes addrsBytes) returns()' \
        1 \
        '["http://localhost:8444"]' \
        $TEST_ADDRESS
```

*note: this can take a few minutes as this transactions has to be mined on Sepolia*

### Configure Bridge Service

Navigate into the `cdk-bridge-service-0.3.1` directory and build the files:
```bash
cd ~/cdk-validium/cdk-bridge-service-0.3.1/
make build
```
Create a starter bridge config `bridge-config.toml` inside `/tmp/cdk`: using the following config file:

```bash
nano /tmp/cdk/bridge-config.toml
#/tmp/cdk/bridge-config.toml
[Log]
Level = "info"
Outputs = ["stderr"]

[SyncDB]
Database = "postgres"
User = "cdk_user"
Name = "bridge_db"
Password = "cdk_password"
Host = "localhost"
Port = "5432"
MaxConns = 20

[Etherman]
L1URL = "https://sepolia.infura.io/v3/b27a8be73bcb4bc7a83aada13c65e135"
L2URLs = ["http://localhost:8123"]

[Synchronizer]
SyncInterval = "1s"
SyncChunkSize = 100

[BridgeController]
Store = "postgres"
Height = 32

[BridgeServer]
GRPCPort = "9090"
HTTPPort = "8080"
DefaultPageLimit = 25
MaxPageLimit = 100
BridgeVersion = "v1"
    # Read only
    [BridgeServer.DB]
    Database = "postgres"
    User = "cdk_user"
    Name = "bridge_db"
    Password = "cdk_password"
    Host = "localhost"
    Port = "5432"
    MaxConns = 20

[NetworkConfig]
GenBlockNumber = "5098088"
PolygonZkEVMAddress = "0x52C8f9808246eF2ce992c0e1f04fa54ec3378dD1"
PolygonBridgeAddress = "0x24F2aF81Ae588690C9752A342d7549f58133CE4e"
PolygonZkEVMGlobalExitRootAddress = "0xE3A721c20B30213FEC306dd60f6c7F2fCB8b46D2"
MaticTokenAddress = "0xd76B50509c1693C7BA35514103a0A156Ca57980c"
L2PolygonBridgeAddresses = ["0x24F2aF81Ae588690C9752A342d7549f58133CE4e"]
L1ChainID = 11155111

[ClaimTxManager]
FrequencyToMonitorTxs = "1s"
PrivateKey = {Path = "/tmp/cdk/account.key", Password = "testonly"}
Enabled = true
RetryInterval = "1s"
RetryNumber = 10
```

And replace the values using the `tomlq` script:

```bash
tomlq -i -t --arg L1_URL "$L1_URL" '.Etherman.L1URL = $L1_URL' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg GEN_BLOCK_NUMBER "$GEN_BLOCK_NUMBER" '.NetworkConfig.GenBlockNumber = $GEN_BLOCK_NUMBER' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.NetworkConfig.PolygonZkEVMAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg POLYGON_ZKEVM_BRIDGE_ADDRESS "$POLYGON_ZKEVM_BRIDGE_ADDRESS" '.NetworkConfig.PolygonBridgeAddress = $POLYGON_ZKEVM_BRIDGE_ADDRESS' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS "$POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS" '.NetworkConfig.PolygonZkEVMGlobalExitRootAddress = $POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg MATIC_TOKEN_ADDRESS "$MATIC_TOKEN_ADDRESS" '.NetworkConfig.MaticTokenAddress = $MATIC_TOKEN_ADDRESS' /tmp/cdk/bridge-config.toml
tomlq -i -t --arg CDK_DATA_COMMITTEE_CONTRACT_ADDRESS "$CDK_DATA_COMMITTEE_CONTRACT_ADDRESS" '.NetworkConfig.L2PolygonBridgeAddresses = [$CDK_DATA_COMMITTEE_CONTRACT_ADDRESS]' /tmp/cdk/bridge-config.toml
```

## 3. Running the components

### Run the prover

Since the prover is large and rather compute expensive to build, we will use a docker container

```bash
docker run -v "/tmp/cdk/test.prover.config.json:/usr/src/app/config.json" -p 50061:50061 -p 50071:50071 --network host hermeznetwork/zkevm-prover:v3.0.2 zkProver -c /usr/src/app/config.json
```

### Run the node

```bash
~/cdk-validium/cdk-validium-node % ./dist/zkevm-node run --network custom --custom-network-file /tmp/cdk/genesis.json --cfg /tmp/cdk/node-config.toml \
	--components sequencer \
	--components sequence-sender \
	--components aggregator \
	--components rpc --http.api eth,net,debug,zkevm,txpool,web3 \
	--components synchronizer \
	--components eth-tx-manager \
	--components l2gaspricer
```

Run the additional approval scripts for node:

```bash
~/cdk-validium/cdk-validium-node % ./dist/zkevm-node approve --network custom \
	--custom-network-file /tmp/cdk/genesis.json \
	--cfg /tmp/cdk/node-config.toml \
	--amount 1000000000000000000000000000 \
	--password "testonly" --yes --key-store-path /tmp/cdk/account.key
```

### Run the DAC

```bash
~/cdk-validium/cdk-data-availability-0.0.3 % ./dist/cdk-data-availability run --cfg /tmp/cdk/dac-config.toml
```

### Run the Bridge Service

```bash
~/cdk-validium/cdk-bridge-service % ./dist/zkevm-bridge run --cfg /tmp/cdk/bridge-config.toml
```