This guide provides a curated list of common commands and Polygon PoS-specific operations essential for node operators. Whether you're setting up a full node, validator node or troubleshooting, these commands will assist you in managing your Polygon PoS environment effectively.

## Frequently used commands for Bor & Heimdall

### Bor

To execute Bor IPC commands, use the following syntax:

```bash
bor attach .bor/data/bor.ipc <command>
```

| IPC Command                                                                 | RPC Command                                                                                                                                            | Description                                                      |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `admin.peers.length`                                                        | `curl -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "net_peerCount", "params": [], "id": 74}' localhost:8545`               | Retrieves the number of peers connected to the node.             |
| `admin.nodeInfo`                                                            |                                                                                                                                                        | Provides detailed information about the node.                    |
| `eth.syncing`                                                               | `curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "eth_syncing","params": []}' localhost:8545`                         | Indicates whether the node is syncing (`true`) or not (`false`). |
| `eth.syncing.highestBlock - eth.syncing.currentBlock`                       |                                                                                                                                                        | Compares the current block of your node to the highest block.    |
| `eth.blockNumber`                                                           | `curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "eth_blockNumber","params": []}' localhost:8545`                     | Returns the latest block number processed by the node.           |
| `debug.setHead("0x"+((eth.getBlock('latest').number) - 1000).toString(16))` |                                                                                                                                                        | Rewinds the blockchain to 1000 blocks prior.                     |
| `admin.nodeInfo.enode`                                                      |                                                                                                                                                        | Retrieves the public enode URL of the node.                      |
| `eth.syncing.currentBlock * 100 / eth.syncing.highestBlock`                 |                                                                                                                                                        | Calculates the remaining percentage for block synchronization.   |
| `eth.getBlock("latest").number`                                             | `curl http://YourIP:8545 -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0", "id":1, "method":"bor_getSigners", "params":["0x98b3ea"]}'` | Queries the height of the latest Bor block.                      |
|                                                                             | `curl http://YourIP:8545 -X POST -H "Content-Type: application/json" --data '{"method":"eth_chainId","params":[],"id":1,"jsonrpc":"2.0"}'`             | Retrieves the `chainID`.                                         |

### Heimdall

| Command                                                                      | Description                                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------- |
| `curl localhost:26657/net_info?jq .result.n_peers`                           | Returns the number of connected peers.             |
| `curl -s localhost:26657/status | jq .result.sync_info.latest_block_height` | Retrieves Heimdall's current block height.         |
| `curl localhost:26657/net_info | grep moniker`                              | Queries the node using its moniker.                |
| `curl -s localhost:26657/status | jq .result.sync_info.catching_up`        | Checks if Heimdall is in sync.                     |
| `curl -s localhost:26657/status | jq .result | jq .sync_info`              | Verifies Heimdall's sync status.                   |
| `heimdalld unsafe-reset-all`                                                 | Resets the database in case of issues.             |
| `curl localhost:26657/status`                                                | Provides comprehensive information about Heimdall. |

## Node management commands

| Description                  | Command                                     |
| ---------------------------- | ------------------------------------------- |
| Locate Heimdall genesis file | `$CONFIGPATH/heimdall/config/genesis.json`  |
| Locate heimdall-config.toml  | `/etc/heimdall/config/heimdall-config.toml` |
| Locate config.toml           | `/etc/heimdall/config/config.toml`          |
| Start Heimdall               | `$ sudo service heimdalld start`            |
| Locate Bor genesis file      | `$CONFIGPATH/bor/genesis.json`              |
| Start Bor                    | `sudo service bor start`                    |
| Retrieve Heimdall logs       | `/var/log/matic-logs/`                      |
| Check Heimdall logs          | `journalctl -fu heimdalld.service`          |
| Check Bor logs               | `journalctl -fu bor.service`                |

## Remove Heimdall directories

```bash
sudo rm -rf /var/lib/heimdalld/
```

## Remove Bor directories

```bash
sudo rm -rf /var/lib/bor
```
