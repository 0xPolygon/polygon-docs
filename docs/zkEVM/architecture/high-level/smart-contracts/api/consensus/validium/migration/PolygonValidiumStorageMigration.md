## Functions

### `constructor`

```solidity
  function constructor(
    contract IPolygonZkEVMGlobalExitRootV2 _globalExitRootManager,
    contract IERC20Upgradeable _pol,
    contract IPolygonZkEVMBridgeV2 _bridgeAddress,
    contract PolygonRollupManager _rollupManager
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRootV2 | Global exit root manager address
|`_pol` | contract IERC20Upgradeable | POL token address
|`_bridgeAddress` | contract IPolygonZkEVMBridgeV2 | Bridge address
|`_rollupManager` | contract PolygonRollupManager | Global exit root manager address

### `initializeMigration`

```solidity
  function initializeMigration(
  ) external
```

### `sequenceBatchesValidium`

Allows a sequencer to send multiple batches.

```solidity
  function sequenceBatchesValidium(
    struct PolygonValidiumStorageMigration.ValidiumBatchData[] batches,
    uint64 maxSequenceTimestamp,
    uint64 initSequencedBatch,
    address l2Coinbase,
    bytes dataAvailabilityMessage
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct PolygonValidiumStorageMigration.ValidiumBatchData[] | Struct array which holds the necessary data to append new batches to the sequence
|`maxSequenceTimestamp` | uint64 | Max timestamp of the sequence. This timestamp must be inside a safety range (actual + 36 seconds).
This timestamp should be equal or higher of the last block inside the sequence, otherwise this batch will be invalidated by circuit.
|`initSequencedBatch` | uint64 | This parameter must match the current last batch sequenced.
This will be a protection for the sequencer to avoid sending undesired data
|`l2Coinbase` | address | Address that will receive the fees from L2
|`dataAvailabilityMessage` | bytes | Byte array containing the signatures and all the addresses of the committee in ascending order
[signature 0, ..., signature requiredAmountOfSignatures -1, address 0, ... address N]
note that each ECDSA signatures are used, therefore each one must be 65 bytes
note Pol is not a reentrant token

### `sequenceBatches`

Allows a sequencer to send multiple batches.

```solidity
  function sequenceBatches(
    struct PolygonRollupBaseEtrogNoGap.BatchData[] batches,
    uint64 maxSequenceTimestamp,
    uint64 initSequencedBatch,
    address l2Coinbase
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct PolygonRollupBaseEtrogNoGap.BatchData[] | Struct array which holds the necessary data to append new batches to the sequence
|`maxSequenceTimestamp` | uint64 | Max timestamp of the sequence. This timestamp must be inside a safety range (actual + 36 seconds).
This timestamp should be equal or higher of the last block inside the sequence, otherwise this batch will be invalidated by circuit.
|`initSequencedBatch` | uint64 | This parameter must match the current last batch sequenced.
This will be a protection for the sequencer to avoid sending undesired data
|`l2Coinbase` | address | Address that will receive the fees from L2
note Pol is not a reentrant token

### `setDataAvailabilityProtocol`

Allow the admin to set a new data availability protocol.

```solidity
  function setDataAvailabilityProtocol(
    contract IDataAvailabilityProtocol newDataAvailabilityProtocol
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newDataAvailabilityProtocol` | contract IDataAvailabilityProtocol | Address of the new data availability protocol

### `switchSequenceWithDataAvailability`

Allow the admin to switch the sequence with data availability.

```solidity
  function switchSequenceWithDataAvailability(
    bool newIsSequenceWithDataAvailabilityAllowed
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newIsSequenceWithDataAvailabilityAllowed` | bool | Boolean to switch

## Events

### `SetDataAvailabilityProtocol`

Emitted when the admin updates the data availability protocol.

```solidity
  event SetDataAvailabilityProtocol(
  )
```

### `SwitchSequenceWithDataAvailability`

Emitted when switch the ability to sequence with data availability.

```solidity
  event SwitchSequenceWithDataAvailability(
  )
```
