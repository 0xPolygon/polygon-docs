Heimdall's *ante handler* plays a crucial role in the integrity and efficiency of transaction processing. It is primarily responsible for the preliminary verification and validation of all transactions, ensuring that they meet the necessary criteria before being included in a block. This includes checking the sender's balance to ensure there are sufficient funds to cover transaction fees and subsequently deducting these fees for successful transactions.

## Advanced gas management in Heimdall

### Block and transaction gas limits

Heimdall employs a gas limit system to regulate the computational and storage resources consumed by transactions and blocks. This system is designed to prevent excessive block sizes and ensure network stability.

#### Block gas limit

Each block in Heimdall has a maximum gas limit, constraining the total gas used by all transactions within the block. The sum of the gas used by each transaction in a block must not exceed this limit:

```go
block.GasLimit >= sum(tx1.GasUsed + tx2.GasUsed + ..... + txN.GasUsed)
```

The maximum block gas limit and block size are specified as part of the consensus parameters during the application setup, as seen in the Heimdall source code at [app.go#L464-L471](https://github.com/maticnetwork/heimdall/blob/develop/app/app.go#L464-L471):

```go
maxGasPerBlock   int64 = 10000000 // 10 Million
maxBytesPerBlock int64 = 22020096 // 21 MB

// Setting consensus parameters
ConsensusParams: &abci.ConsensusParams{
 Block: &abci.BlockParams{
  MaxBytes: maxBytesPerBlock,
  MaxGas:   maxGasPerBlock,
 },
 ...
},
```

#### Transaction gas limit

For individual transactions, the gas limit is determined by parameters in the `auth` module and can be modified through Heimdall's governance (`gov`) module.

#### Special handling of checkpoint transactions

Checkpoint transactions, which require Merkle proof verification on the Ethereum chain, are treated distinctly. To streamline processing and avoid the overhead of additional Merkle proof verification, Heimdall restricts blocks containing a `MsgCheckpoint` transaction to just that one transaction:

```go
// Gas requirement for checkpoint transaction
gasWantedPerCheckpoinTx sdk.Gas = 10000000 // 10 Million

// Special gas limit handling for checkpoint transactions
if stdTx.Msg.Type() == "checkpoint" && stdTx.Msg.Route() == "checkpoint" {
 gasForTx = gasWantedPerCheckpoinTx
}
```

## Enhanced transaction verification and replay protection

The ante handler in Heimdall is instrumental in ensuring the legitimacy and uniqueness of transactions. It performs a thorough verification of incoming transactions, including signature validation, as delineated in the source code at [ante.go#L230-L266](https://github.com/maticnetwork/heimdall/blob/develop/auth/ante.go#L230-L266).

### Sequence number for replay protection

A critical aspect of transaction security in Heimdall is the use of a `sequenceNumber` in each transaction. This feature is a safeguard against replay attacks, where a transaction might be fraudulently or mistakenly repeated. To prevent such scenarios, the ante handler increments the sequence number for the sender's account after each successful transaction. This incrementation ensures that each transaction is unique and that previous transactions cannot be replayed.

In summary, Heimdall's ante handler, along with its sophisticated gas management and transaction verification systems, provides a robust framework for secure and efficient transaction processing. The careful balance of block and transaction gas limits, coupled with advanced replay protection mechanisms, ensures the smooth operation of the Heimdall chain within the Polygon PoS network.
