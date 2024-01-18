## Start the databases

```bash
export ZKEVM_NET="mainnet"
export ZKEVM_DIR="/root/zkevm"
export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-pool-db zkevm-state-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-pool-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-state-db
```

## Start the prover (contains executor)

```bash
export ZKEVM_NET="mainnet"
export ZKEVM_DIR="/root/zkevm"
export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-prover
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-prover --tail 20
```

## Start synchronizer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-sync
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-sync --tail 20
```

## Start L2 gas pricer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-l2gaspricer
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-l2gaspricer --tail 20
```

## Start transaction manager

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-eth-tx-manager
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-eth-tx-manager --tail 20
```

## Start the RPC

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-json-rpc
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-json-rpc --tail 20
```

## Start the sequencer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-sequencer
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-sequencer --tail 20
```

## Start the aggregator

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-aggregator
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-aggregator --tail 20
```

## Start the block explorer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-explorer-l2 zkevm-explorer-l2-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-explorer-l2-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-explorer-l2 --tail 20
```

## Start the bridge

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-bridge-service zkevm-bridge-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-bridge-db --tail 20
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-bridge-service --tail 20
```
