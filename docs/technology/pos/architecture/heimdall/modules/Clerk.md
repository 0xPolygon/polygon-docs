---
id: clerk
title: Clerk
description: Module that manages generic state-sync from Ethereum to Bor
keywords:
  - docs
  - matic
  - module
  - state sync
  - clerk
  - heimdall
image: https://matic.network/banners/matic-network-16x9.png 
---

# Clerk

Clerk manages generic state-sync from Ethereum chain to Bor chain. Heimdall agrees on state sync, which is initiated on the Ethereum chain using the Clerk module.

More details are available in [state sync mechanism](/docs/pos/design/bor/core_concepts.md#state-management-state-sync)

## Messages

### MsgEventRecord

`MsgEventRecord` transaction is responsible for validating events from `StateSender.sol`  and storing the state on Heimdall for Bor to use.

Handler for this transaction validates for any given `msg.TxHash` and `msg.LogIndex`. It throws `Older invalid tx found` error if trying to process the transaction more than once.

Here is the structure for the transaction message:

```go
// MsgEventRecord - state msg
type MsgEventRecord struct {
	From     types.HeimdallAddress `json:"from"`
	TxHash   types.HeimdallHash    `json:"tx_hash"`
	LogIndex uint64                `json:"log_index"`
	ID       uint64                `json:"id"`
	ChainID  string                `json:"bor_chain_id"`
}
```

## CLI Commands

### Send state record transaction

```bash
heimdallcli tx clerk record
	--log-index <log-index> 
	--tx-hash <transaction-hash> 
	--bor-chain-id <bor-chain-id>
	--chain-id <heimdall-chain-id>
```

### To query already validated state event record

```go
heimdallcli query clerk record --id <state-record-id>
```

## REST APIs

|Name                  |Method|Endpoint          |
|----------------------|------|------------------|
|Event record details  |GET   |/clerk/event-record/<record-id\>|
|All event records     |GET   |/clerk/event-record/list|
