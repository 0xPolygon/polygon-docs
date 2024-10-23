Abstract contract required to preserve the storage slots from previous versions. Inherits from `IPolygonZkEVMGlobalExitRootV2.sol`

## Functions

None.

## Variables

### `lastRollupExitRoot`

Rollup root, contains all exit roots of all rollups.

Returns `bytes32` object.

### `lastMainnetExitRoot`

Mainnet exit root; updated every time a deposit is made in mainnet.

Returns `bytes32` object.

### `globalExitRootMap`

Stores every global exit root: where root == `blockhash`.

Note that global exit roots in previous versions recorded `timestamp` instead of `blockhash`.

Returns `mapping(bytes32 => uint256)` object.
