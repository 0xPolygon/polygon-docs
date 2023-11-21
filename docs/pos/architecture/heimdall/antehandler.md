---
id: antehandler
title: Ante Handler
description: Ante Handler checks and validates the transaction
keywords:
  - docs
  - matic
  - polygon
  - Ante Handler
  - validate transactions
image: https://matic.network/banners/matic-network-16x9.png 
---

# Ante Handler

Ante handler checks and validates the transaction. After the verification, it checks the balance of the sender for enough fees and deduct fees in case of successful transaction inclusion.

## Gas Limit

Each block and transaction have a limit for gas usage. A block can contain multiple transactions, but gas used by all transactions in a block must be less than block gas limit to avoid larger blocks. 

```go
block.GasLimit >= sum(tx1.GasUsed + tx2.GasUsed + ..... + txN.GasUsed)
```

Note that each state manipulation on transaction costs gas, including signature verification for the transaction.

### Block Gas Limit

Max block gas limit and bytes per block is passed while setting up app's consensus params: [https://github.com/maticnetwork/heimdall/blob/develop/app/app.go#L464-L471](https://github.com/maticnetwork/heimdall/blob/develop/app/app.go#L464-L471)

```go
maxGasPerBlock   int64 = 10000000 // 10 Million
maxBytesPerBlock int64 = 22020096 // 21 MB

// pass consensus params
ConsensusParams: &abci.ConsensusParams{
	Block: &abci.BlockParams{
		MaxBytes: maxBytesPerBlock,
		MaxGas:   maxGasPerBlock,
	},
	...
},
```

### Transaction Gas Limit

The transaction gas limit is defined in params in `auth` module. It can be changed through the Heimdall `gov` module.

### Checkpoint Transaction Gas Limit

Since block contains multiple transactions and verifies this particular transaction on the Ethereum chain, Merkle proof is required. To avoid extra Merkle proof verification for checkpoint transaction, Heimdall only allows one transaction in the block if the transaction type is `MsgCheckpoint`

```go
// fee wanted for checkpoint transaction
gasWantedPerCheckpoinTx sdk.Gas = 10000000 // 10 Million

// checkpoint gas limit
if stdTx.Msg.Type() == "checkpoint" && stdTx.Msg.Route() == "checkpoint" {
	gasForTx = gasWantedPerCheckpoinTx
}
```

## Transaction Verification and Replay Protection

Ante Handler handles and verifies signature in incoming transaction: [https://github.com/maticnetwork/heimdall/blob/develop/auth/ante.go#L230-L266](https://github.com/maticnetwork/heimdall/blob/develop/auth/ante.go#L230-L266)

Each transaction must include `sequenceNumber` to avoid replay attacks. After each successful transaction inclusion, Ante handler increases the sequence number for the TX sender account to avoid duplication (replay) of the previous transactions.