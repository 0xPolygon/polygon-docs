## Functions

### `constructor`

```solidity
  function constructor(
    contract IPolygonZkEVMGlobalExitRoot _globalExitRootManager,
    contract IERC20Upgradeable _pol,
    contract IPolygonZkEVMBridge _bridgeAddress,
    contract PolygonRollupManager _rollupManager
  ) public
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRoot | Global exit root manager address
|`_pol` | contract IERC20Upgradeable | POL token address
|`_bridgeAddress` | contract IPolygonZkEVMBridge | Bridge address
|`_rollupManager` | contract PolygonRollupManager | Global exit root manager address

### `sequenceBatches`

```solidity
  function sequenceBatches(
  ) public
```

### `sequenceBatchesDataCommittee`

Allows a sequencer to send multiple batches.

```solidity
  function sequenceBatchesDataCommittee(
    struct PolygonDataComittee.ValidiumBatchData[] batches,
    address l2Coinbase,
    bytes dataAvailabilityMessage
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct PolygonDataComittee.ValidiumBatchData[] | Struct array which holds the necessary data to append new batches to the sequence
|`l2Coinbase` | address | Address that will receive the fees from L2
|`dataAvailabilityMessage` | bytes | Byte array containing the signatures and all the addresses of the committee in ascending order
[signature 0, ..., signature requiredAmountOfSignatures -1, address 0, ... address N]
note that each ECDSA signatures are used, therefore each one must be 65 bytes

### `switchSequenceWithDataAvailability`

Allows the admin to turn on the force batches.

This action is not reversible.

```solidity
  function switchSequenceWithDataAvailability(
  ) external
```

## Events

### SwitchSequenceWithDataAvailability

```solidity
  event SwitchSequenceWithDataAvailability(
  )
```

Emitted when switching the ability to sequence with data availability.
