## Configure the prover

Copy and modify the contents of `test.prover.config.json` in `~/cdk-validium/cdk-validium-node/test/config/` to the `/tmp/cdk/` directory using the following jq command:

```bash
cd ~/cdk-validium/cdk-validium-node 
jq '.aggregatorClientHost = "127.0.0.1" | .databaseURL = "postgresql://cdk_user:cdk_password@localhost:5432/postgres"' ./test/config/test.prover.config.json > /tmp/cdk/test.prover.config.json
```

## Configure the node

1. Create the configuration files for the node by first building the `cdk-validium-node`.

	```bash
	cd ~/cdk-validium/cdk-validium-node
	make build
	```

2. Create a keystore for reference in the `config.toml` configuration file. Use the private key we generated previously and stored in the `/tmp/cdk/.env` file and encrypt it with a basic password. For example:

	```bash
	source /tmp/cdk/.env
	./dist/zkevm-node encryptKey --pk=$TEST_PRIVATE_KEY --pw="testonly" --output=/tmp/cdk/account.keystore
	find /tmp/cdk/account.keystore -type f -name 'UTC--*' | head -n 1 | xargs -I xxx mv xxx /tmp/cdk/account.key
	```

	!!!	important
		Make sure you source your environment: `source /tmp/cdk/.env`.

	The output keystore is now stored in `/tmp/cdk/account.keystore`

3. Create a file `node-config.toml` inside `/tmp/cdk/` and paste in the following content.

	???     "`node-config.toml`"		
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

4. Run the following script to modify the `URL` parameter in`[Etherman]` to the URL of the RPC Provider, along with the parameters `L2Coinbase` in `[SequenceSender]` and `SenderAddress` in `[Aggregator]` to the address we generated earlier.

	```bash
	source /tmp/cdk/.env
	tomlq -i -t --arg L1_URL "$L1_URL" '.Etherman.URL = $L1_URL' /tmp/cdk/node-config.toml
	tomlq -i -t --arg TEST_ADDRESS "$TEST_ADDRESS" '.SequenceSender.L2Coinbase = $TEST_ADDRESS' /tmp/cdk/node-config.toml
	tomlq -i -t --arg TEST_ADDRESS "$TEST_ADDRESS" '.Aggregator.SenderAddress = $TEST_ADDRESS' /tmp/cdk/node-config.toml
	```

5. Now we will modify the `genesis.json` from the earlier contract deployment to include information about the newly configured chain.

	!!!	info
		`genesis.json` is in the `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/` directory

	The values to append to `genesis.json` are something like:

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

6. Run the following script that automates the process of appending those values:

	```bash
	jq --argjson data "$(jq '{maticTokenAddress, cdkValidiumAddress, cdkDataCommitteeContract, polygonZkEVMGlobalExitRootAddress, deploymentBlockNumber}' ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/deploy_output.json)" \
	'.L1Config.chainId = 11155111 | 
	.L1Config.maticTokenAddress = $data.maticTokenAddress | 
	.L1Config.polygonZkEVMAddress = $data.cdkValidiumAddress | 
	.L1Config.cdkDataCommitteeContract = $data.cdkDataCommitteeContract | 
	.L1Config.polygonZkEVMGlobalExitRootAddress = $data.polygonZkEVMGlobalExitRootAddress | 
	.genesisBlockNumber = $data.deploymentBlockNumber' ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment/genesis.json > /tmp/cdk/genesis.json
	```

## Configure the DAC

At this point we should have setup and provisioned the psql database and configured the zk prover and node. 

Now let’s configure the Data Availability Committee.

1. Navigate to `~/cdk-validium/cdk-data-availability-0.0.3`.

2. Build the DAC

	```bash
	make build
	```

3. Create a `dac-config.toml` file inside `/tmp/cdk/`. 

4. Copy and paste the following example config below into `dac-config.toml`.

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

5. Run the `tomlq` script to replace the necessary parameters.

	```bash
	source /tmp/cdk/.env
	tomlq -i -t --arg L1_URL "$L1_URL" '.L1.RpcURL = $L1_URL' /tmp/cdk/dac-config.toml
	tomlq -i -t --arg L1_WS_URL "$L1_WS_URL" '.L1.WsURL = $L1_WS_URL' /tmp/cdk/dac-config.toml
	tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.L1.CDKValidiumAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/dac-config.toml
	tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.L1.DataCommitteeAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/dac-config.toml
	```

6. Update the contracts on Sepolia with information about our DAC.

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

	!!!	note
		This can take a few minutes.
	
	You should see something like this:

	![DAC configuration output](../../../../img/cdk/dac-output.png)

## Configure bridge service

1. Navigate into the `zkevm-bridge-service-0.3.1` directory and build the files.

	```bash
	cd ~/cdk-validium/zkevm-bridge-service-0.3.1/
	make build
	```

2. Create a starter bridge config `bridge-config.toml` inside `/tmp/cdk` using the following config file:

	```bash
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

3. Replace the values using the `tomlq` script below.

	```bash
	tomlq -i -t --arg L1_URL "$L1_URL" '.Etherman.L1URL = $L1_URL' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg GEN_BLOCK_NUMBER "$GEN_BLOCK_NUMBER" '.NetworkConfig.GenBlockNumber = $GEN_BLOCK_NUMBER' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg CDK_VALIDIUM_ADDRESS "$CDK_VALIDIUM_ADDRESS" '.NetworkConfig.PolygonZkEVMAddress = $CDK_VALIDIUM_ADDRESS' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg POLYGON_ZKEVM_BRIDGE_ADDRESS "$POLYGON_ZKEVM_BRIDGE_ADDRESS" '.NetworkConfig.PolygonBridgeAddress = $POLYGON_ZKEVM_BRIDGE_ADDRESS' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS "$POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS" '.NetworkConfig.PolygonZkEVMGlobalExitRootAddress = $POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg MATIC_TOKEN_ADDRESS "$MATIC_TOKEN_ADDRESS" '.NetworkConfig.MaticTokenAddress = $MATIC_TOKEN_ADDRESS' /tmp/cdk/bridge-config.toml
	tomlq -i -t --arg CDK_DATA_COMMITTEE_CONTRACT_ADDRESS "$CDK_DATA_COMMITTEE_CONTRACT_ADDRESS" '.NetworkConfig.L2PolygonBridgeAddresses = [$CDK_DATA_COMMITTEE_CONTRACT_ADDRESS]' /tmp/cdk/bridge-config.toml
	```

