Topups are amounts used to pay fees on the Heimdall chain.

There are two ways to topup your account:

1. When new validator joins, they can mention a `topup` amount as top-up in addition to the staked amount, which will be moved as balance on Heimdall chain to pays fees on Heimdall.
2. A user can directly call the top-up function on the staking smart contract on Ethereum to increase top-up balance on Heimdall.

## Messages

### MsgTopup

`MsgTopup` transaction is responsible for minting balance to an address on Heimdall based on Ethereum chain's `TopUpEvent` on staking manager contract.

Handler for this transaction processes top-up and increases the balance only once for any given `msg.TxHash` and `msg.LogIndex`. It throws `Older invalid tx found` error, if trying to process the top-up more than once.

Here is the structure for the top-up transaction message:

```go
type MsgTopup struct {
 FromAddress types.HeimdallAddress `json:"from_address"`
 ID          types.ValidatorID     `json:"id"`
 TxHash      types.HeimdallHash    `json:"tx_hash"`
 LogIndex    uint64                `json:"log_index"`
}
```

### MsgWithdrawFee

`MsgWithdrawFee` transaction is responsible for withdrawing balance from Heimdall to Ethereum chain. A Validator can withdraw any amount from Heimdall.

Handler processes the withdraw by deducting the balance from the given validator and prepares the state to send the next checkpoint. The next possible checkpoint will contain the withdraw related state for the specific validator.

Handler gets validator information based on `ValidatorAddress` and processes the withdraw.

```go
// MsgWithdrawFee - high-level transaction of the fee coin withdrawal module
type MsgWithdrawFee struct {
 ValidatorAddress types.HeimdallAddress `json:"from_address"`
 Amount           types.Int             `json:"amount"`
}
```

## CLI Commands

### Topup fee

```bash
heimdallcli tx topup fee
 --log-index <log-index> 
 --tx-hash <transaction-hash> 
 --validator-id <validator ID here>
 --chain-id <heimdall-chain-id>
```

### Withdraw fee

```bash
heimdallcli tx topup withdraw --chain-id <heimdall-chain-id>
```

To check reflected topup on account run following command

```bash
heimdallcli query auth account <validator-address> --trust-node
```

## REST APIs

|Name                  |Method|URL               |Body Params                                                                                                                                      |
|----------------------|------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|Topup Fee             |POST  |/topup/fee        |`id` Validator id, `tx_hash` Transaction hash of successful topup event on Ethereum chain, `log_index` Log index of topup event emitted on Ethereum chain|
|Withdraw Fee          |POST  |/topup/withdraw   |`amount` Withdraw amount|
