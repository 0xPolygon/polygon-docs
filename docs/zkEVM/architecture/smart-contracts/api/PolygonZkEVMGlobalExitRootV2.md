Contract responsible for managing the exit roots across multiple networks.

## Functions

### `constructor`

```solidity
  function constructor(
    address _rollupManager,
    address _bridgeAddress
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_rollupManager` | address | Rollup manager contract address
|`_bridgeAddress` | address | PolygonZkEVMBridge contract address

### `updateExitRoot`

Updates the exit root of any of the networks and the global exit root.

```solidity
  function updateExitRoot(
    bytes32 newRoot
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newRoot` | bytes32 | new exit tree root

### `getLastGlobalExitRoot`

Returns last global exit root.

```solidity
  function getLastGlobalExitRoot(
  ) public returns (bytes32)
```

### `getRoot`

Computes and returns the Merkle root of the `L1InfoTree`.

```solidity
  function getRoot(
  ) public returns (bytes32)
```

### `getLeafValue`

Given leaf data, it returns the leaf hash.

```solidity
  function getLeafValue(
    bytes32 newGlobalExitRoot,
    uint256 lastBlockHash,
    uint64 timestamp
  ) public returns (bytes32)
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newGlobalExitRoot` | bytes32 | Last global exit root
|`lastBlockHash` | uint256 | Last accesible block hash
|`timestamp` | uint64 | Ethereum timestamp in seconds

## Events

### `UpdateL1InfoTree`

Emitted when the global exit root is updated.

```solidity
  event UpdateL1InfoTree(
  )
```
