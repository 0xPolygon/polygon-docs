Heimdall's `bor` module is responsible for managing span intervals and coordinating interactions with the Bor chain. Specifically, it determines when a new span can be proposed on Heimdall based on the current block number `n` and the current span `span`. A new span proposal is permissible when the current Bor chain block number `n` falls within the range of `span.StartBlock` and `span.EndBlock` (inclusive of `StartBlock` and exclusive of `EndBlock`). Validators on the Heimdall chain can propose a new span when these conditions are met.

## Messages

### MsgProposeSpan

The `MsgProposeSpan` message plays a crucial role in setting up the validator committee for a specific span and records a new span in the Heimdall state. This message is detailed in the Heimdall source code at [bor/handler.go#L27](https://github.com/maticnetwork/heimdall/blob/develop/bor/handler.go#L27).

```go
// MsgProposeSpan creates msg propose span
type MsgProposeSpan struct {
 ID         uint64                  `json:"span_id"`
 Proposer   hmTypes.HeimdallAddress `json:"proposer"`
 StartBlock uint64                  `json:"start_block"`
 EndBlock   uint64                  `json:"end_block"`
 ChainID    string                  `json:"bor_chain_id"`
}
```

#### Selection of Producers

The process for choosing producers from among all validators involves a two-step mechanism:

1. **Slot Allocation Based on Validator Power:** Each validator is assigned a number of slots proportional to their power. For instance, a validator with a power rating of 10 will receive 10 slots, while one with a power rating of 20 will receive 20 slots. This method ensures that validators with higher power have a correspondingly higher chance of being selected.

2. **Shuffling and Selection:** All allocated slots are then shuffled using a `seed` derived from the Ethereum (ETH 1.0) block hash corresponding to each span `n`. The first `producerCount` producers are selected from this shuffled list. The `bor` module on Heimdall employs the Ethereum 2.0 shuffle algorithm for this selection process. The algorithm's implementation can be viewed at [bor/selection.go](https://github.com/maticnetwork/heimdall/blob/develop/bor/selection.go).

This method of selection ensures that the process is both fair and weighted according to the validators' power, thereby maintaining a balanced and proportional representation in the span committee.

```go
// SelectNextProducers selects producers for the next span by converting power to slots
// spanEligibleVals - all validators eligible for next span
func SelectNextProducers(blkHash common.Hash, spanEligibleVals []hmTypes.Validator, producerCount uint64) (selectedIDs []uint64, err error) {
 if len(spanEligibleVals) <= int(producerCount) {
  for _, val := range spanEligibleVals {
   selectedIDs = append(selectedIDs, uint64(val.ID))
  }
  return
 }

 // extract seed from hash
 seed := helper.ToBytes32(blkHash.Bytes()[:32])
 validatorIndices := convertToSlots(spanEligibleVals)
 selectedIDs, err = ShuffleList(validatorIndices, seed)
 if err != nil {
  return
 }
 return selectedIDs[:producerCount], nil
}

// converts validator power to slots
func convertToSlots(vals []hmTypes.Validator) (validatorIndices []uint64) {
 for _, val := range vals {
  for val.VotingPower >= types.SlotCost {
   validatorIndices = append(validatorIndices, uint64(val.ID))
   val.VotingPower = val.VotingPower - types.SlotCost
  }
 }
 return validatorIndices
}
```

## Types

Here are the span details that Heimdall uses:

```go
// Span structure
type Span struct {
 ID                uint64       `json:"span_id" yaml:"span_id"`
 StartBlock        uint64       `json:"start_block" yaml:"start_block"`
 EndBlock          uint64       `json:"end_block" yaml:"end_block"`
 ValidatorSet      ValidatorSet `json:"validator_set" yaml:"validator_set"`
 SelectedProducers []Validator  `json:"selected_producers" yaml:"selected_producers"`
 ChainID           string       `json:"bor_chain_id" yaml:"bor_chain_id"`
}
```

## Parameters

The Bor module contains the following parameters:

|Key                   |Type  |Default value                      | Duration (*)                 |
|----------------------|------|-----------------------------------|------------------------------|
|SprintDuration.       |uint64|16 blocks                          |32 seconds                    |
|SpanDuration          |uint64|100 * SprintDuration = 1,600 blocks|3,200 seconds (53min and 20s)|
|ProducerCount         |uint64|4 blocks                           |8 seconds                     |

(*): Given that blocks are produced every [2 seconds](https://github.com/maticnetwork/bor/blob/4d23e6de3387e18c5f9f55b40ed37189ce82a7aa/params/config.go#L416) on Bor.

Previously, a sprint would last [64 blocks](https://github.com/maticnetwork/bor/blob/4d23e6de3387e18c5f9f55b40ed37189ce82a7aa/params/config.go#L423) but it was agreed to decrease this number to [16 blocks](https://github.com/maticnetwork/bor/blob/4d23e6de3387e18c5f9f55b40ed37189ce82a7aa/params/config.go#L424) on the [Delhi hard fork](https://polygon.technology/blog/hardfork-incoming-upgrading-polygon-pos-chain-to-boost-performance) of January 17th, 2023, precisely starting at block number [38,189,056](https://polygonscan.com/block/38189056).

## CLI Commands

### Span propose tx

```bash
heimdallcli tx bor propose-span \
 --start-block <start-block> \
 --chain-id <heimdall-chain-id>
```

### Query current span

```bash
heimdallcli query bor span latest-span --chain-id <heimdall-chain-id>
```

Expected output:

```go
{
  "span_id":2,
  "start_block":6656,
  "end_block":13055,
  "validator_set":{
    "validators":[
      {
        "ID":1,
        "startEpoch":0,
        "endEpoch":0,
        "power":1,
        "pubKey":"0x04b12d8b2f6e3d45a7ace12c4b2158f79b95e4c28ebe5ad54c439be9431d7fc9dc1164210bf6a5c3b8523528b931e772c86a307e8cff4b725e6b4a77d21417bf19",
        "signer":"0x6c468cf8c9879006e22ec4029696e005c2319c9d",
        "last_updated":"",
        "accum":0
      }
    ],
    "proposer":{
      "ID":1,
      "startEpoch":0,
      "endEpoch":0,
      "power":1,
      "pubKey":"0x04b12d8b2f6e3d45a7ace12c4b2158f79b95e4c28ebe5ad54c439be9431d7fc9dc1164210bf6a5c3b8523528b931e772c86a307e8cff4b725e6b4a77d21417bf19",
      "signer":"0x6c468cf8c9879006e22ec4029696e005c2319c9d",
      "last_updated":"",
      "accum":0
    }
  },
  "selected_producers":[
    {
      "ID":1,
      "startEpoch":0,
      "endEpoch":0,
      "power":1,
      "pubKey":"0x04b12d8b2f6e3d45a7ace12c4b2158f79b95e4c28ebe5ad54c439be9431d7fc9dc1164210bf6a5c3b8523528b931e772c86a307e8cff4b725e6b4a77d21417bf19",
      "signer":"0x6c468cf8c9879006e22ec4029696e005c2319c9d",
      "last_updated":"",
      "accum":0
    }
  ],
  "bor_chain_id":"15001"
}
```

### Query span by id

```bash
heimdallcli query bor span --span-id <span-id> --chain-id <heimdall-chain-id>
```

It prints the result in same format as above.

### Parameters

To print all params;

```go
heimdalldcli query bor params
```

Expected Result:

```go
sprint_duration: 16
span_duration: 1600
producer_count: 4
```

## REST APIs

|Name                  |Method|Endpoint          |
|----------------------|------|------------------|
|Span details          |GET   |/bor/span/span-id |
|Get latest span       |GET   |/bor/latest-span  |
|Get params            |GET   |/bor/params       |
