# Checkpoint

`checkpoint` module manages checkpoint related functionalities for Heimdall. It needs Bor chain when a new checkpoint is proposed on Heimdall to verify checkpoint root hash.

All related to checkpoint data is explained in details [here](/docs/pos/design/heimdall/checkpoint).

## Checkpoint life-cycle

Heimdall uses the same leader selection algorithm as Tendermint to select the next proposer. While submitting checkpoints on the Ethereum chain, it may fail due to multiple reasons like gas limit, traffic on Ethereum, high gas fees. That's why the multi-stage checkpoint process is required.

Each checkpoint has validator as proposer. If checkpoint on Ethereum chain fails or succeeds, `ack` and `no-ack` transaction would change the proposer on Heimdall for next checkpoint. The following flow chart represents the life cycle of the checkpoint:

<img src="/img/pos/checkpoint-flowchart.svg")} />

## Messages

<img src="/img/pos/checkpoint-module-flow.svg")} />

### MsgCheckpoint

`MsgCheckpoint` handles checkpoint verification on Heimdall. Only this message uses RLP encoding as it needs to be verified on Ethereum chain.

```go
// MsgCheckpoint represents checkpoint transaction
type MsgCheckpoint struct {
	Proposer        types.HeimdallAddress `json:"proposer"`
	StartBlock      uint64                `json:"startBlock"`
	EndBlock        uint64                `json:"endBlock"`
	RootHash        types.HeimdallHash    `json:"rootHash"`
	AccountRootHash types.HeimdallHash    `json:"accountRootHash"`
}
```

Once this transaction gets processed on Heimdall, the `proposer` takes `votes` and `sigs` from Tendermint for this transaction and sends checkpoint on the Ethereum chain.

Since block contains multiple transactions and verifies this particular transaction on the Ethereum chain, Merkle proof is required. To avoid extra Merkle proof verification on Ethereum, Heimdall only allows one transaction in the block if the transaction type is `MsgCheckpoint`

To allow this mechanism, Heimdall sets `MsgCheckpoint` transaction as high gas consumed transaction. Check [https://github.com/maticnetwork/heimdall/blob/develop/auth/ante.go#L104-L106](https://github.com/maticnetwork/heimdall/blob/develop/auth/ante.go#L104-L106)

```go
// fee wanted for checkpoint transaction
gasWantedPerCheckpoinTx sdk.Gas = 10000000

// checkpoint gas limit
if stdTx.Msg.Type() == "checkpoint" && stdTx.Msg.Route() == "checkpoint" {
	gasForTx = gasWantedPerCheckpoinTx
}
```

This transaction will store proposed checkpoint on `checkpointBuffer` state instead of actual checkpoint list state.

### MsgCheckpointAck

`MsgCheckpointAck` handles successful checkpoint submission. Here `HeaderBlock` is a checkpoint counter;

```go
// MsgCheckpointAck represents checkpoint ack transaction if checkpoint is successful
type MsgCheckpointAck struct {
	From        types.HeimdallAddress `json:"from"`
	HeaderBlock uint64                `json:"headerBlock"`
	TxHash      types.HeimdallHash    `json:"tx_hash"`
	LogIndex    uint64                `json:"log_index"`
}
```

For valid `TxHash` and `LogIndex` for the submitted checkpoint, this transaction verifies the following event and validates checkpoint in `checkpointBuffer` state: [https://github.com/maticnetwork/contracts/blob/develop/contracts/root/RootChainStorage.sol#L7-L14](https://github.com/maticnetwork/contracts/blob/develop/contracts/root/RootChainStorage.sol#L7-L14)

```jsx
event NewHeaderBlock(
    address indexed proposer,
    uint256 indexed headerBlockId,
    uint256 indexed reward,
    uint256 start,
    uint256 end,
    bytes32 root
);
```

On successful event verification, it updates the actual count of checkpoint, also known as `ackCount` and clears the `checkpointBuffer`.

### MsgCheckpointNoAck

`MsgCheckpointNoAck` handles un-successful checkpoints or offline proposers. This transaction is only valid after `CheckpointBufferTime` has passed from the following events:

- Last successful `ack` transaction
- Last successful `no-ack` transaction

```go
// MsgCheckpointNoAck represents checkpoint no-ack transaction
type MsgCheckpointNoAck struct {
	From types.HeimdallAddress `json:"from"`
}
```

This transaction gives the timeout period for the current proposer to send checkpoint/ack before Heimdall chooses a new `proposer` for the next checkpoint.

## Parameters

The checkpoint module contains the following parameters:

|Key                   |Type  |Default value     |
|----------------------|------|------------------|
|CheckpointBufferTime  |uint64|1000 * time.Second|


## CLI Commands

### Params

To print all params:

```go
heimdallcli query checkpoint params --trust-node
```

Expected Result:

```yaml
checkpoint_buffer_time: 16m40s
```

### Send Checkpoint

Following command sends checkpoint transaction on Heimdall:

```yaml
heimdallcli tx checkpoint send-checkpoint \
	--start-block=<start-block> \
	--end-block=<end-block> \
	--root-hash=<root-hash> \
	--account-root-hash=<account-root-hash> \
	--chain-id=<chain-id>
```

### Send `ack`

Following command sends ack transaction on Heimdall if checkpoint is successful on Ethereum:

```yaml
heimdallcli tx checkpoint send-ack \
	--tx-hash=<checkpoint-tx-hash>
	--log-index=<checkpoint-event-log-index>
	--header=<checkpoint-index> \
  --chain-id=<chain-id>
```

### Send `no-ack`

Following command send no-ack transaction on Heimdall:

```yaml
heimdallcli tx checkpoint send-noack --chain-id <chain-id>
```

## REST APIs

|Name                  |Method|Endpoint          |
|----------------------|------|------------------|
|It returns the prepared msg for ack checkpoint|POST   |/checkpoint/ack|
|It returns the prepared msg for new checkpoint|POST   |/checkpoint/new|
|It returns the prepared msg for no-ack checkpoint|POST   |/checkpoint/no-ack|
|Checkpoint by number  |GET   |/checkpoints/<checkpoint-number\>|
|Get current checkpoint buffer state|GET   |/checkpoints/buffer|
|Get checkpoint counts |GET   |/checkpoints/count |
|Get last no-ack details|GET   |/checkpoints/last-no-ack|
|Get latest checkpoint |GET   |/checkpoints/latest|
|All checkpoints       |GET   |/checkpoints/list  |
|It returns the checkpoint parameters|GET   |/checkpoints/parama|
|It returns the prepared checkpoint|GET   |/checkpoints/prepare|
|Get ack count, buffer, validator set, validator count and last-no-ack details|GET   |/overview         |

More details about the query and response of the above requests can be found [here](https://heimdall-api.polygon.technology/swagger-ui/#/checkpoint).

All query APIs will provide result in following format:

```json
{
	"height": "1",
	"result": {
		...	  
	}
}
```