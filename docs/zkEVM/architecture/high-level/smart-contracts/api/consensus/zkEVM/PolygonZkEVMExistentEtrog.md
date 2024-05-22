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

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRootV2 | Global exit root manager address
|`_pol` | contract IERC20Upgradeable | POL token address
|`_bridgeAddress` | contract IPolygonZkEVMBridgeV2 | Bridge address
|`_rollupManager` | contract PolygonRollupManager | Global exit root manager address

### `initializeUpgrade`

```solidity
  function initializeUpgrade(
    address _admin,
    address _trustedSequencer,
    string _trustedSequencerURL,
    string _networkName,
    bytes32 _lastAccInputHash
  ) external
```

!!! note
    - This initializer is called instead of the `PolygonRollupBase`.
    - This is a especial initializer since the zkEVM network has already been created.

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_admin` | address | Admin address
|`_trustedSequencer` | address | Trusted sequencer address
|`_trustedSequencerURL` | string | Trusted sequencer URL
|`_networkName` | string | L2 network name
|`_lastAccInputHash` | bytes32 | Acc input hash

## Events

### `UpdateEtrogSequence`

Emitted when the system is updated to a etrog using this contract, and contains the set up etrog transaction.

```solidity
  event UpdateEtrogSequence(
  )
```
