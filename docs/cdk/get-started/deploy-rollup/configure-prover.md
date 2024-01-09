
Continue with this deployment guide's **fifth step** where you configure the Prover and Services.

## Edit DBs

Edit `~/zkevm/mainnet/db/scripts/init_prover_db.sql` to match this:

```bash
vim ~/zkevm/mainnet/db/scripts/init_prover_db.sql
```

```sql
CREATE DATABASE prover_db;
\connect prover_db;

CREATE SCHEMA state;

CREATE TABLE state.nodes (hash BYTEA PRIMARY KEY, data BYTEA NOT NULL);
CREATE TABLE state.program (hash BYTEA PRIMARY KEY, data BYTEA NOT NULL);

CREATE USER prover_user with password 'prover_pass';
GRANT CONNECT ON DATABASE prover_db TO prover_user;
ALTER USER prover_user SET SEARCH_PATH=state;
GRANT ALL PRIVILEGES ON SCHEMA state TO prover_user;
GRANT ALL PRIVILEGES ON TABLE state.nodes TO prover_user;
GRANT ALL PRIVILEGES ON TABLE state.program TO prover_user;
```

Save and exit the file once the changes have been made. The above SQL script will set up your databases for the zkEVM Node.

## Configure the Prover

Create the `~/zkevm/config.json` and paste the configs below. Replace the `aggregatorClientHost` parameter with your **PUBLIC IP**:

```bash
vim ~/zkevm/config.json
```

??? "Click to expand the <code>config.json</code> file"
    ```json
    {
      "runExecutorServer": false,
      "runExecutorClient": false,
      "runExecutorClientMultithread": false,

      "runStateDBServer": false,
      "runStateDBTest": false,
      
      "runAggregatorServer": false,
      "runAggregatorClient": true,
      "proverName": "static_prover",
      
      "runFileGenBatchProof": false,
      "runFileGenAggregatedProof": false,
      "runFileGenFinalProof": false,
      "runFileProcessBatch": false,
      "runFileProcessBatchMultithread": false,
      "runFileExecutor": false,
      
      "runKeccakScriptGenerator": false,
      "runKeccakTest": false,
      "runStorageSMTest": false,
      "runBinarySMTest": false,
      "runMemAlignSMTest": false,
      "runSHA256Test": false,
      "runBlakeTest": false,
      
      "executeInParallel": true,
      "useMainExecGenerated": true,
      "useProcessBatchCache": true,
      "saveRequestToFile": false,
      "saveInputToFile": true,
      "saveDbReadsToFile": true,
      "saveDbReadsToFileOnChange": false,
      "saveOutputToFile": true,
      "saveFilesInSubfolders": false,
      "saveProofToFile": true,
      "saveResponseToFile": false,
      "loadDBToMemCache": true,
      "loadDBToMemCacheInParallel": false,
      "dbMTCacheSize": 16384,
      "dbProgramCacheSize": 16384,
      "dbMultiWrite": true,
      "dbFlushInParallel": true,
      
      "opcodeTracer": false,
      "logRemoteDbReads": false,
      "logExecutorServerResponses": false,
      
      "executorServerPort": 50071,
      "executorROMLineTraces": false,
      "executorClientPort": 50071,
      "executorClientHost": "127.0.0.1",
      
      "stateDBServerPort": 5432,
      "stateDBURL": "local",
      
      "aggregatorServerPort": 50081,
      "aggregatorClientPort": 50081,
      "aggregatorClientHost": "", // YOUR PUBLIC IP ADDRESS
      "aggregatorClientMockTimeout": 10000000,
      
      "mapConstPolsFile": false,
      "mapConstantsTreeFile": false,
      
      "inputFile": "testvectors/aggregatedProof/recursive1.zkin.proof_0.json",
      "inputFile2": "testvectors/aggregatedProof/recursive1.zkin.proof_1.json",
      
      "outputPath": "/output/",
      "configPath": "/mnt/prover/config/",
      "zkevmCmPols_disabled": "/mnt/prover/runtime/zkevm.commit",
      "c12aCmPols": "runtime/c12a.commit",
      "recursive1CmPols_disabled": "runtime/recursive1.commit",
      "recursive2CmPols_disabled": "runtime/recursive2.commit",
      "recursivefCmPols_disabled": "runtime/recursivef.commit",
      "finalCmPols_disabled": "runtime/final.commit",
      
      "publicsOutput": "public.json",
      "proofFile": "proof.json",
      
      "databaseURL": "postgresql://prover_user:prover_pass@zkevm-state-db:5432/prover_db",
      "databaseURL_disabled": "local",
      "dbNodesTableName": "state.nodes",
      "dbProgramTableName": "state.program",
      "dbConnectionsPool": true,
      "cleanerPollingPeriod": 600,
      "requestsPersistence": 3600,
      "maxExecutorThreads": 20,
      "maxProverThreads": 8,
      "maxStateDBThreads": 8
    }
    ```

### Configure services

Edit the `~/zkevm/mainnet/docker-compose.yml` file with the following content:

```bash
vim ~/zkevm/mainnet/docker-compose.yml
```

??? "Click to expand the <code>~/zkevm/mainnet/docker-compose.yml</code> file"
    ```yml
    version: "3.5"
    networks:
      default:
      name: zkevm

    services:
      zkevm-sequencer:
        container_name: zkevm-sequencer
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 9092:9091 # needed if metrics enabled
          - 6060:6060
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
        extra_hosts:
          - "localhost:host-gateway"
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json--cfg /app/config.toml --components sequencer"
      
      zkevm-sequence-sender:
        container_name: zkevm-sequence-sender
        image: hermeznetwork/zkevm-node:v0.2.1
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
          - ZKEVM_NODE_SEQUENCER_SENDER_ADDRESS=XXXXXXXXXXXX # trustedSequencer from deploy_output.json
        volumes:
          - ./sequencer.keystore:/pk/sequencer.keystore
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components sequence-sender"
        
      zkevm-json-rpc:
        container_name: zkevm-json-rpc
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 8123:8545
          - 8133:8546 # needed if WebSockets enabled
          - 9091:9091 # needed if metrics enabled
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
        extra_hosts:
          - "localhost:host-gateway"
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
            - "-c"
            - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components rpc"
      
      zkevm-aggregator:
        container_name: zkevm-aggregator
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 50081:50081
          - 9093:9091 # needed if metrics enabled
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_AGGREGATOR_SENDER_ADDRESS=XXXXXXXXXXXX # trustedAggregator from deploy_output.json
        extra_hosts:
          - "localhost:host-gateway"
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components aggregator"
      
      zkevm-sync:
        container_name: zkevm-sync
        restart: unless-stopped
        depends_on:
          zkevm-state-db:
            condition: service_healthy
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 9095:9091 # needed if metrics enabled
        extra_hosts:
          - "localhost:host-gateway"
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_ETHERMAN_URL=${ZKEVM_NODE_ETHERMAN_URL}
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components synchronizer"
      
      zkevm-eth-tx-manager:
        container_name: zkevm-eth-tx-manager
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 9094:9091 # needed if metrics enabled
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
        extra_hosts:
          - "localhost:host-gateway"
        volumes:
          - ./sequencer.keystore:/pk/sequencer.keystore
          - ./aggregator.keystore:/pk/aggregator.keystore
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components eth-tx-manager"
      
      zkevm-l2gaspricer:
        container_name: zkevm-l2gaspricer
        image: hermeznetwork/zkevm-node:v0.2.1
        environment:
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
        extra_hosts:
          - "localhost:host-gateway"
        volumes:
          - ./sequencer.keystore:/pk/keystore
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components l2gaspricer"
      
      zkevm-state-db:
        container_name: zkevm-state-db
        image: postgres
        deploy:
          resources:
            limits:
              memory: 2G
            reservations:
              memory: 1G
        healthcheck:
          test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
          interval: 10s
          timeout: 5s
          retries: 5
        ports:
          - 5432:5432
        volumes:
          - ./db/scripts/init_prover_db.sql:/docker-entrypoint-initdb.d/init.sql
          - ${ZKEVM_NODE_STATEDB_DATA_DIR}:/var/lib/postgresql/data
          - ${ZKEVM_ADVANCED_CONFIG_DIR:-./config/environments/testnet}/postgresql.conf:/etc/postgresql.conf
        environment:
          - POSTGRES_USER=state_user
          - POSTGRES_PASSWORD=state_password
          - POSTGRES_DB=state_db
        command:
          - "postgres"
          - "-N"
          - "500"
          - "-c"
          - "config_file=/etc/postgresql.conf"
      
      zkevm-pool-db:
        container_name: zkevm-pool-db
        image: postgres
        deploy:
          resources:
            limits:
              memory: 2G
            reservations:
              memory: 1G
        healthcheck:
          test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
          interval: 10s
          timeout: 5s
          retries: 5
        ports:
          - 5433:5432
        volumes:
          - ${ZKEVM_NODE_POOLDB_DATA_DIR}:/var/lib/postgresql/data
        environment:
          - POSTGRES_USER=pool_user
          - POSTGRES_PASSWORD=pool_password
          - POSTGRES_DB=pool_db
        command:
          - "postgres"
          - "-N"
          - "500"
      
      zkevm-event-db:
        container_name: zkevm-event-db
        image: postgres
        deploy:
          resources:
            limits:
              memory: 2G
            reservations:
              memory: 1G
        ports:
          - 5435:5432
        volumes:
          - ./db/scripts/init_event_db.sql:/docker-entrypoint-initdb.d/init.sql
        environment:
          - POSTGRES_USER=event_user
          - POSTGRES_PASSWORD=event_password
          - POSTGRES_DB=event_db
        command:
          - "postgres"
          - "-N"
          - "500"
      
      zkevm-explorer-l1:
        container_name: zkevm-explorer-l1
        image: hermeznetwork/zkevm-explorer:latest
        ports:
          - 4000:4000
        environment:
          - NETWORK=ETH
          - SUBNETWORK=Local Ethereum
          - COIN=ETH
          - ETHEREUM_JSONRPC_VARIANT=geth
          - ETHEREUM_JSONRPC_HTTP_URL=http://zkevm-mock-l1-network:8545
          - DATABASE_URL=postgres://l1_explorer_user:l1_explorer_password@zkevm-explorer-l1-db:5432/l1_explorer_db
          - ECTO_USE_SSL=false
          - MIX_ENV=prod
        command:
          - "/bin/sh"
          - "-c"
          - "mix do ecto.create, ecto.migrate; mix phx.server"
      
      zkevm-explorer-l1-db:
        container_name: zkevm-explorer-l1-db
        image: postgres
        ports:
          - 5436:5432
        environment:
          - POSTGRES_USER=l1_explorer_user
          - POSTGRES_PASSWORD=l1_explorer_password
          - POSTGRES_DB=l1_explorer_db
        command:
          - "postgres"
          - "-N"
          - "500"
      
      zkevm-explorer-l2:
        container_name: zkevm-explorer-l2
        image: hermeznetwork/zkevm-explorer:latest
        ports:
          - 4001:4000
        extra_hosts:
          - "localhost:host-gateway"
        environment:
          - NETWORK=POE
          - SUBNETWORK=Polygon Hermez
          - COIN=ETH
          - ETHEREUM_JSONRPC_VARIANT=geth
          - ETHEREUM_JSONRPC_HTTP_URL=http://localhost:8123
          - DATABASE_URL=postgres://l2_explorer_user:l2_explorer_password@zkevm-explorer-l2-db:5432/l2_explorer_db
          - ECTO_USE_SSL=false
          - MIX_ENV=prod
          - LOGO=/images/blockscout_logo.svg
          - LOGO_FOOTER=/images/blockscout_logo.svg
        command:
          - "/bin/sh"
          - "-c"
          - "mix do ecto.create, ecto.migrate; mix phx.server"
      
      zkevm-explorer-json-rpc:
        container_name: zkevm-explorer-json-rpc
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 8124:8124
          - 8134:8134 # needed if WebSockets enabled
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
          - ZKEVM_NODE_RPC_PORT=8124
          - ZKEVM_NODE_RPC_WEBSOCKETS_PORT=8134
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components rpc --http.api eth,net,debug,zkevm,txpool,web3"
        
      zkevm-explorer-l2-db:
        container_name: zkevm-explorer-l2-db
        image: postgres
        ports:
          - 5437:5432
        extra_hosts:
          - "localhost:host-gateway"
        environment:
          - POSTGRES_USER=l2_explorer_user
          - POSTGRES_PASSWORD=l2_explorer_password
          - POSTGRES_DB=l2_explorer_db
        command: ["postgres", "-N", "500"]
        
      zkevm-mock-l1-network:
        container_name: zkevm-mock-l1-network
        image: hermeznetwork/geth-zkevm-contracts:v2.0.0-RC1-fork.5-geth1.12.0
        ports:
          - 8545:8545
          - 8546:8546
        command:
          - "--http"
          - "--http.api"
          - "admin,eth,debug,miner,net,txpool,personal,web3"
          - "--http.addr"
          - "0.0.0.0"
          - "--http.corsdomain"
          - "*"
          - "--http.vhosts"
          - "*"
          - "--ws"
          - "--ws.origins"
          - "*"
          - "--ws.addr"
          - "0.0.0.0"
          - "--dev"
          - "--datadir"
          - "/geth_data"
          - "--syncmode"
          - "full"
          - "--rpc.allow-unprotected-txs"
      
      zkevm-prover:
        container_name: zkevm-prover
        image: hermeznetwork/zkevm-prover:v2.1.0-RC2
        ports:
          - 50051:50051 # Prover
          - 50052:50052 # Mock prover
          - 50061:50061 # MT
          - 50071:50071 # Executor
        volumes:
          - ./config/environments/testnet/public.prover.config.json:/usr/src/app/config.json
        command: >
          zkProver -c /usr/src/app/config.json
        
      zkevm-approve:
        container_name: zkevm-approve
        image: hermeznetwork/zkevm-node:v0.2.1
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
        volumes:
          - ./sequencer.keystore:/pk/keystore
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-node approve --network custom --custom-network-file /app/genesis.json --key-store-path /pk/keystore --pw testonly --am 115792089237316195423570985008687907853269984665640564039457584007913129639935 -y --cfg /app/config.toml"
      
      zkevm-permissionless-db:
        container_name: zkevm-permissionless-db
        image: postgres
        deploy:
          resources:
            limits:
              memory: 2G
            reservations:
              memory: 1G
        ports:
          - 5434:5432
        volumes:
          - ./db/scripts/single_db_server.sql:/docker-entrypoint-initdb.d/init.sql
        environment:
          - POSTGRES_USER=test_user
          - POSTGRES_PASSWORD=test_password
          - POSTGRES_DB=test_db
        command:
          - "postgres"
          - "-N"
          - "500"
      
      zkevm-permissionless-node:
        container_name: zkevm-permissionless-node
        image: hermeznetwork/zkevm-node:v0.2.1
        ports:
          - 8125:8125
        environment:
          - ZKEVM_NODE_ISTRUSTEDSEQUENCER=false
          - ZKEVM_NODE_STATEDB_USER=test_user
          - ZKEVM_NODE_STATEDB_PASSWORD=test_password
          - ZKEVM_NODE_STATEDB_NAME=state_db
          - ZKEVM_NODE_STATEDB_HOST=zkevm-permissionless-db
          - ZKEVM_NODE_POOL_DB_USER=test_user
          - ZKEVM_NODE_POOL_DB_PASSWORD=test_password
          - ZKEVM_NODE_POOL_DB_NAME=pool_db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-permissionless-db
          - ZKEVM_NODE_RPC_PORT=8125
          - ZKEVM_NODE_RPC_SEQUENCERNODEURI=http://zkevm-json-rpc:8123
          - ZKEVM_NODE_MTCLIENT_URI=zkevm-permissionless-prover:50061
          - ZKEVM_NODE_EXECUTOR_URI=zkevm-permissionless-prover:50071
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
          - "-c"
          - '/app/zkevm-node run --network custom --custom-network-file /app/genesis.json --cfg /app/config.toml --components "rpc,synchronizer"'
      
      zkevm-permissionless-prover:
        container_name: zkevm-permissionless-prover
        image: hermeznetwork/zkevm-prover:v2.1.0-RC2
        ports:
          # - 50058:50058 # Prover
          - 50059:50052 # Mock prover
          - 50068:50061 # MT
          - 50078:50071 # Executor
        volumes:
          - ./config/environments/testnet/public.permissionless.prover.config.json:/usr/src/app/config.json
        command: >
          zkProver -c /usr/src/app/config.json
      
      zkevm-metrics:
        image: prom/prometheus:v2.39.1
        container_name: zkevm-metrics
        restart: unless-stopped
        ports:
          - 9090:9090
        command:
          - --config.file=/etc/prometheus/prometheus.yml
          - --web.enable-lifecycle
        volumes:
          - ./config/metrics/prometheus:/etc/prometheus
      
      zkevm-sh:
        container_name: zkevm-sh
        image: hermeznetwork/zkevm-node:v0.2.1
        stdin_open: true
        tty: true
        environment:
          - ZKEVM_NODE_STATEDB_HOST=zkevm-state-db
          - ZKEVM_NODE_POOL_DB_HOST=zkevm-pool-db
        volumes:
          - ./config/environments/testnet/public.node.config.toml:/app/config.toml
          - ./config/environments/testnet/public.genesis.config.json:/app/genesis.json
        command:
          - "/bin/sh"
      
      zkevm-bridge-db:
        container_name: zkevm-bridge-db
        image: postgres
        deploy:
          resources:
            limits:
              memory: 8G
            reservations:
              memory: 4G
          expose:
            - 5435
          ports:
            - 5435:5432
          extra_hosts:
            - "localhost:host-gateway"
          environment:
            - POSTGRES_USER=bridge_user
            - POSTGRES_PASSWORD=bridge_password
            - POSTGRES_DB=bridge_db
          command:
            - "postgres"
            - "-N"
            - "500"
      zkevm-bridge-service:
        container_name: zkevm-bridge-service
        image: hermeznetwork/zkevm-bridge-service:2.0
        ports:
          - 8080:8080
          - 9090:9090
        extra_hosts:
          - "localhost:host-gateway"
        environment:
          - ZKEVM_BRIDGE_DATABASE_USER=bridge_user
          - ZKEVM_BRIDGE_DATABASE_PASSWORD=bridge_password
          - ZKEVM_BRIDGE_DATABASE_NAME=bridge_db
          - ZKEVM_BRIDGE_DATABASE_HOST=localhost
          - ZKEVM_BRIDGE_DATABASE_PORT=5435
        volumes:
          - ./sequencer.keystore:/pk/keystore.claimtxmanager
          - ./config/environments/testnet/public.bridge.config.toml:/app/config.toml
        command:
          - "/bin/sh"
          - "-c"
          - "/app/zkevm-bridge run --cfg /app/config.toml"
    ```
  
## Start services

Continue with starting all the services as indicated below.

### Start the databases

```bash
export ZKEVM_NET="mainnet"
export ZKEVM_DIR="/root/zkevm"
export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-pool-db zkevm-state-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-pool-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-state-db
```

### Start the Prover (contains executor)

```bash
export ZKEVM_NET="mainnet"
export ZKEVM_DIR="/root/zkevm"
export ZKEVM_CONFIG_DIR="/root/zkevm/zkevm-config"
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-prover
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-prover --tail 20
```

### Start synchronizer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-sync
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-sync --tail 20
```

### Start L2 gas pricer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-l2gaspricer
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-l2gaspricer --tail 20
```

### Start transaction manager

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-eth-tx-manager
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-eth-tx-manager --tail 20
```

### Start the RPC

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-json-rpc
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-json-rpc --tail 20
```

### Start the sequencer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-sequencer
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-sequencer --tail 20
```

### Start the aggregator

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-aggregator
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-aggregator --tail 20
```

### Start the block explorer

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-explorer-l2 zkevm-explorer-l2-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-explorer-l2-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-explorer-l2 --tail 20
```

### Start the bridge

```bash
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml up -d zkevm-bridge-service zkevm-bridge-db
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-bridge-db --tail 20
docker compose --env-file $ZKEVM_CONFIG_DIR/.env -f $ZKEVM_DIR/$ZKEVM_NET/docker-compose.yml logs -f zkevm-bridge-service --tail 20
```
