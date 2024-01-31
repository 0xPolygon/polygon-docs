## Run the prover

Since the prover is large and compute-expensive to build, we will use a docker container.

```bash
docker run -v "/tmp/cdk/test.prover.config.json:/usr/src/app/config.json" -p 50061:50061 -p 50071:50071 --network host hermeznetwork/zkevm-prover:v3.0.2 zkProver -c /usr/src/app/config.json
```

## Run the node

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

### Run the additional approval scripts for the node

```bash
~/cdk-validium/cdk-validium-node % ./dist/zkevm-node approve --network custom \
	--custom-network-file /tmp/cdk/genesis.json \
	--cfg /tmp/cdk/node-config.toml \
	--amount 1000000000000000000000000000 \
	--password "testonly" --yes --key-store-path /tmp/cdk/account.key
```

## Run the DAC

```bash
~/cdk-validium/cdk-data-availability-0.0.3 % ./dist/cdk-data-availability run --cfg /tmp/cdk/dac-config.toml
```

## Run the bridge service

```bash
~/cdk-validium/cdk-bridge-service % ./dist/zkevm-bridge run --cfg /tmp/cdk/bridge-config.toml
```