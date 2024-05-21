Transactions flowing through the system reach the smart contract environment after one of two contract call use cases; sequencing or verifying batches.

This section of the docs takes a closer look at the sequencing workflow.

## `sequenceBatches(...)`

The rollup sequencer component calls the [`sequenceBatches`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/1ad7089d04910c319a257ff4f3674ffd6fc6e64e/contracts/v2/lib/PolygonRollupBaseEtrog.sol#L425) function on the [`PolygonZkEVMEtrog.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/1ad7089d04910c319a257ff4f3674ffd6fc6e64e/contracts/v2/consensus/zkEVM/PolygonZkEVMEtrog.sol) contract which inherits the function from [PolygonRollupBaseEtrog](https://github.com/0xPolygonHermez/zkevm-contracts/blob/1ad7089d04910c319a257ff4f3674ffd6fc6e64e/contracts/v2/lib/PolygonRollupBaseEtrog.sol).

The function takes an array of `BatchData` structs containing transactions. 

```solidity
struct BatchData {
    bytes transactions;
    bytes32 forcedGlobalExitRoot;
    uint64 forcedTimestamp;
    bytes32 forcedBlockHashL1;
}
```

The function checks them, organizes them, and appends them to the sequence correctly, eventually emitting a `SequenceBatch` event which sends a newly sequenced batch of transactions to the `PolygonRollupManager.sol` contract via the `onSequenceBatches(...)` function.

### `onSequenceBatches(...)`

This function takes the sequenced batches and adds them to the correct stack and updates the batch count.

## `sequenceBatchesValidium(...)`