Heimdall's `bank` module handles balance transfers between accounts. This module corresponds to the `bank` module from the Cosmos SDK.

## Messages

### `MsgSend`

`MsgSend` handles transfer between accounts in Heimdall. Here is a structure for transaction message:

```go
// MsgSend - high-level transaction of the coin module
type MsgSend struct {
 FromAddress types.HeimdallAddress `json:"from_address"`
 ToAddress   types.HeimdallAddress `json:"to_address"`
 Amount      types.Coins           `json:"amount"`
}
```

### `MsgMultiSend`

`MsgMultiSend` handles multi transfer between account for Heimdall.

```go
// MsgMultiSend - high-level transaction of the coin module
type MsgMultiSend struct {
 Inputs  []Input  `json:"inputs"`
 Outputs []Output `json:"outputs"`
}
```

## Parameters

The bank module contains the following parameters:

| Key           | Type | Default value |
| ------------- | ---- | ------------- |
| `sendenabled` | bool | true          |

## CLI Commands

### Send balance

The following command sends 1000 POL tokens to the specified `address`:

```bash
heimdallcli tx bank send <address> 1000pol --chain-id <chain-id>
```
