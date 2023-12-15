This guide provides a curated list of common commands and Polygon-specific operations essential for node operators. Whether you're setting up a full node, validator node or troubleshooting, these commands will assist you in managing your Polygon PoS environment effectively.

## Frequently used commands for Bor & Heimdall
### Bor

To execute Bor IPC commands, use the following syntax:

```bash
bor attach .bor/data/bor.ipc <command>
```

| IPC Command | RPC Command | Description |
| ----------- | ----------- | ----------- |
| `admin.peers.length` | `curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "net_peerCount", "params": [], "id": 74}' localhost:8545` | Retrieves the number of peers connected to the node. |
| `admin.nodeInfo` |  | Provides detailed information about the node. |
| `eth.syncing` | `curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "eth_syncing","params": []}' localhost:8545` | Indicates whether the node is syncing (`true`) or not (`false`). |
| `eth.syncing.highestBlock - eth.syncing.currentBlock` |  | Compares the current block of your node to the highest block. |
| `eth.blockNumber` | `curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "eth_blockNumber","params": []}' localhost:8545` | Returns the latest block number processed by the node. |
| `debug.setHead("0x"+((eth.getBlock('latest').number) - 1000).toString(16))` |  | Rewinds the blockchain to 1000 blocks prior. |
| `admin.nodeInfo.enode` |  | Retrieves the public enode URL of the node. |
| `eth.syncing.currentBlock * 100 / eth.syncing.highestBlock` |  | Calculates the remaining percentage for block synchronization. |
| `eth.getBlock("latest").number` | `curl http://YourIP:8545 -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0", "id":1, "method":"bor_getSigners", "params":["0x98b3ea"]}'` | Queries the height of the latest Bor block. |
|  | `curl http://YourIP:8545 -X POST -H "Content-Type: application/json" --data '{"method":"eth_chainId","params":[],"id":1,"jsonrpc":"2.0"}'` | Retrieves the `chainID`. |

### Heimdall

| Command | Description |
| ------- | ----------- |
| `curl localhost:26657/net_info?` | Returns the number of connected peers using `jq .result.n_peers`. |
| `curl -s localhost:26657/status` | Retrieves Heimdall's current block height using `jq .result.sync_info.latest_block_height`. |
| `curl localhost:26657/net_info` | Queries the node using its moniker with `grep moniker`. |
| `curl -s localhost:26657/status` | Checks if Heimdall is in sync using `jq .result.sync_info.catching_up`. |
| `curl -s localhost:26657/status` | Verifies Heimdall's sync status using `jq .result \| jq .sync_info`. |
| `heimdalld unsafe-reset-all` | Resets the database in case of issues. |
| `curl localhost:26657/status` | Provides comprehensive information about Heimdall. |


## Node management commands

| Description                           | Command                                        |
| ------------------------------------- | ---------------------------------------------- |
| **Locate Heimdall genesis file**      | `$CONFIGPATH/heimdall/config/genesis.json`     |
| **Locate heimdall-config.toml**       | `/etc/heimdall/config/heimdall-config.toml`    |
| **Locate config.toml**                | `/etc/heimdall/config/config.toml`             |
| **Locate heimdall-seeds.txt**         | `$CONFIGPATH/heimdall/heimdall-seeds.txt`      |
| **Start Heimdall**                    | `$ sudo service heimdalld start`               |
| **Start Heimdall rest-server**        | `$ sudo service heimdalld-rest-server start`   |
| **Start Heimdall bridge-server**      | `$ sudo service heimdalld-bridge start`        |
| **Locate Bor genesis file**           | `$CONFIGPATH/bor/genesis.json`                 |
| **Start Bor**                         | `sudo service bor start`                       |
| **Retrieve Heimdall logs**            | `/var/log/matic-logs/`                         |
| **Check Heimdall logs**               | `tail -f heimdalld.log`                        |
| **Check Heimdall rest-server logs**   | `tail -f heimdalld-rest-server.log`            |
| **Check Heimdall bridge logs**        | `tail -f heimdalld-bridge.log`                 |
| **Check Bor logs**                    | `tail -f bor.log`                              |

## Useful configuration commands

### Sync status of Heimdall

To check if Heimdall is synced, run:

```bash
curl http://localhost:26657/status
```

### Latest block height on Heimdall

To check the latest block height on Heimdall, run:

```bash
curl localhost:26657/status
```

### Latest block height on Bor

To check the latest block height on Bor, use:

```bash
curl http://<your ip>:8545 -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0", "id":1, "method":"bor_getSigners", "params":["0x98b3ea"]}'
```

### Cleanup: deleting remnants of Heimdall and Bor

**For Linux package:**

```bash
sudo dpkg -i matic-bor
sudo rm -rf /etc/bor
```

**For Binaries:**

```bash
sudo rm -rf /etc/bor
sudo rm /etc/heimdall
```

### Terminate Bor process

**For Linux:**

```bash
ps -aux | grep bor
sudo kill -9 <PID>
```

**For Binaries:**

```bash
cd CS-2003/bor
bash stop.sh
```

### Retrieve latest peer details

To retrieve the latest peer details, run:

```bash
bor attach bor.ipc
admin.peers.forEach(function(value){
    console.log(value.enode+',')
})
exit
```

### Stop Heimdall and Bor services

**For Linux packages:**

```bash
sudo service heimdalld stop
sudo service bor stop
```

**For binaries:**

```bash
pkill heimdalld
pkill heimdalld-bridge
cd CS-2001/bor
bash stop.sh
```

### Remove Heimdall and Bor directories

**For Linux packages:**

```bash
sudo rm -rf /etc/heimdall/*
sudo rm -rf /etc/bor/*
```

**For binaries:**

```bash
sudo rm -rf /var/lib/heimdalld/
sudo rm -rf /var/lib/bor
```
