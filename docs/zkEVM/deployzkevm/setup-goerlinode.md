This is a step-by-step guide to setting up a full node on the Goërli Testnet to act as the Layer 1 (L1).

Follow the steps below to get started.

## Requirements

Before starting the setup, you will need **at least 500 GB of free disk space** to allocate a full Goerli node.

Next, make sure you have the following commands installed:

- wget
- jq
- docker

```bash
sudo apt update -y
sudo apt install -y wget jq docker.io

sudo usermod -aG docker $USER
newgrp docker && newgrp $USER
```

Additionally, you will need **an L1 Goerli address** to proceed with the setup that will act as the suggested fee recipient. Make sure you have this address provisioned.

## Preparation

1. Create a directory for your Goerli node:

```bash
mkdir -p ~/goerli-node/docker-volumes/{geth,prysm}
```

2. Create a `docker-compose.yml` file and open it for editing:

```bash
  cd ~/goerli-node/
  vim docker-compose.yml
```

3. Copy and paste the following content into the `docker-compose.yml` file:

```yaml
 services:
   geth:
     image: "ethereum/client-go:stable"
     container_name: goerli-execution
     command: |
       --goerli
       --http
       --http.vhosts=*
       --http.rpcprefix=/
       --http.corsdomain=*
       --http.addr 0.0.0.0
       --http.api eth,net,engine,admin
       --config=/app/config.toml
     volumes:
       - "./docker-volumes/geth:/root/.ethereum"
       - "./config.toml:/app/config.toml"
     ports:
       - "0.0.0.0:${L1_RPC_PORT}:8545"
       - "0.0.0.0:30303:30303/udp"

 prysm:
   image: "gcr.io/prysmaticlabs/prysm/beacon-chain:stable"

   container_name: goerli-consensus
   command: |
     --prater
     --datadir=/data
     --jwt-secret=/geth/goerli/geth/jwtsecret
     --rpc-host=0.0.0.0
     --grpc-gateway-host=0.0.0.0
     --monitoring-host=0.0.0.0
     --execution-endpoint=/geth/goerli/geth.ipc
     --accept-terms-of-use
     --suggested-fee-recipient=${L1_SUGGESTED_FEE_RECIPIENT_ADDR}
     --checkpoint-sync-url=${L1_CHECKPOINT_URL}
   volumes:
     - "./docker-volumes/prysm:/data"
     - "./docker-volumes/geth:/geth"
   ports:
     - "0.0.0.0:3500:3500"
     - "0.0.0.0:4000:4000"
     - "0.0.0.0:12000:12000/udp"
     - "0.0.0.0:13000:13000"
   depends_on:
     - geth
```

4. Save and Close the `docker-compose.yml` file.

5. Create an `.env` file and open it for editing:

```bash
cd ~/goerli-node/
vim .env
```

6. Set the following environment variables in the `.env` file:

```bash
 L1_RPC_PORT=8845
 L1_SUGGESTED_FEE_RECIPIENT_ADDR=0x  # Put your Goerli account address
 L1_CHECKPOINT_URL=https://goerli.checkpoint-sync.ethpandaops.io
```

7. Save and Close the `.env` file.

8. Add geth config.toml file with following values to increase RPC timeouts

```bash
cd ~/goerli-node/
vim config.toml
```

```bash
[Node.HTTPTimeouts]
ReadTimeout = 600000000000
ReadHeaderTimeout = 600000000000
WriteTimeout = 600000000000
IdleTimeout = 1200000000000
```

## Deploy

1. Start the compose services:

```bash
cd ~/goerli-node/
docker compose --env-file /root/goerli-node/.env -f /root/goerli-node/docker-compose.yml up -d
```

2. Check the logs of the prysm service to monitor the synchronization progress:

```bash
docker compose --env-file /root/goerli-node/.env -f /root/goerli-node/docker-compose.yml logs -f prysm --tail 20
```

  Wait for the initial sync to complete. You will see log messages similar to the following indicating the progress:

  ```bash
    #goerli-consensus  | time="2023-06-19 09:39:44" level=info msg="Synced up to slot 5888296" prefix=initial-sync
  ```

3. Check the logs of the geth service to monitor the initial download and sync progress:

```bash
docker compose --env-file /root/goerli-node/.env -f /root/goerli-node/docker-compose.yml logs -f geth --tail 20
```

- This process may take a couple of hours. Look for log messages similar to the following indicating the progress:

```bash
#goerli-execution  | INFO [06-19|09:43:24.954] Syncing beacon headers                   downloaded=25600 left=9,177,918 eta=1h5m31.860s
#goerli-execution  | INFO [06-19|10:09:19.488] Syncing: state download in progress      synced=0.30% state=331.34MiB accounts=81053@20.52MiB slots=1,112,986@239.47MiB codes=11681@71.34MiB >
```

## Validation

Once both service logs show the sync completion and new blocks are being updated, you can verify the correctness of the RPC by making a call. For example, to get the current block number, use the following command:

```bash
printf "%d\n" $(curl -s -X POST --header "Content-Type: application/json"  --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}' http://localhost:8845 | jq -r .result)
```

If everything is correctly set up, you should see the current block number returned.

Congratulations! You have successfully set up your own full node on the Goerli Testnet. You can now use this node to perform transactions and interact with the Goerli network.
