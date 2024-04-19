---
comments: true
---

## Run the prover

1. Open a new terminal window.

2. Since the prover is large and compute-expensive to build, we will use a docker container.

	```bash
	docker run -v "/tmp/cdk/test.prover.config.json:/usr/src/app/config.json" -p 50061:50061 -p 50071:50071 --network host hermeznetwork/zkevm-prover:v3.0.2 zkProver -c /usr/src/app/config.json
	```

	!!! note "Run containers in background"
        Add the `-d` flag to the command to run the container in the background.
        
        ```bash
        docker run -d -v "/tmp/cdk/test.prover.config.json:/usr/src/app/config.json" -p 50061:50061 -p 50071:50071 --network host hermeznetwork/zkevm-prover:v3.0.2 zkProver -c /usr/src/app/config.json
        ```

	!!! important
		The database logs may output an error while they wait for a node. For example:

		```txt
		2024-01-31 12:18:30.329 UTC [675] ERROR:  relation "state.nodes" does not exist at character 15
		2024-01-31 12:18:30.329 UTC [675] STATEMENT:  SELECT * FROM state.nodes WHERE hash = E'\\xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff';
		```

		The node log may also output an error while they wait for services to come online. For example:

		```txt
		aggregatorClientMockThread() channel broken; will retry in 5 seconds
		aggregatorClientMockThread() failed calling readerWriter->Read(&aggregatorMessage)
		```

## Run the node

1. Open a new terminal window.

2. Run the following commands.

	```bash
	cd ~/cdk-validium/cdk-validium-node 
	./dist/zkevm-node run --network custom --custom-network-file /tmp/cdk/genesis.json --cfg /tmp/cdk/node-config.toml \
		--components sequencer \
		--components sequence-sender \
		--components aggregator \
		--components rpc --http.api eth,net,debug,zkevm,txpool,web3 \
		--components synchronizer \
		--components eth-tx-manager \
		--components l2gaspricer
	```

### Run the additional approval scripts for the node

1. Open a new terminal window at the same directory as the previous step.

2. Run the following commands.

	```bash
	cd ~/cdk-validium/cdk-validium-node 
	./dist/zkevm-node approve --network custom \
		--custom-network-file /tmp/cdk/genesis.json \
		--cfg /tmp/cdk/node-config.toml \
		--amount 1000000000000000000000000000 \
		--password "testonly" --yes --key-store-path /tmp/cdk/account.key
	```

## Run the DAC

Navigate to the `cdk-data-availability` directory and run the following command.

```bash
cd ~/cdk-validium/cdk-data-availability
./dist/cdk-data-availability run --cfg /tmp/cdk/dac-config.toml
```

## Run the bridge service

Open a new terminal window and run the following command.

```bash
cd ~/cdk-validium/zkevm-bridge-service-0.3.1/
./dist/zkevm-bridge run --cfg /tmp/cdk/bridge-config.toml
```

## Congratulations

You have now set up and deployed a full CDK validium network.

Check the next section to find out how to send a test transaction.