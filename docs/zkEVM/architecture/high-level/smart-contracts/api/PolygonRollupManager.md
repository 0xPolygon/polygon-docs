## Functions

### `constructor`

```solidity
  function constructor(
    contract IPolygonZkEVMGlobalExitRootV2 _globalExitRootManager,
    contract IERC20Upgradeable _pol,
    contract IPolygonZkEVMBridge _bridgeAddress
  ) public
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRootV2 | Global exit root manager address
|`_pol` | contract IERC20Upgradeable | POL token address
|`_bridgeAddress` | contract IPolygonZkEVMBridge | Bridge address

### `initialize`

```solidity
  function initialize(
    address trustedAggregator,
    uint64 _pendingStateTimeout,
    uint64 _trustedAggregatorTimeout,
    address admin,
    address timelock,
    address emergencyCouncil,
    contract PolygonZkEVMExistentEtrog polygonZkEVM,
    contract IVerifierRollup zkEVMVerifier,
    uint64 zkEVMForkID,
    uint64 zkEVMChainID
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`trustedAggregator` | address | Trusted aggregator address
|`_pendingStateTimeout` | uint64 | Pending state timeout
|`_trustedAggregatorTimeout` | uint64 | Trusted aggregator timeout
|`admin` | address | Admin of the rollup manager
|`timelock` | address | Timelock address
|`emergencyCouncil` | address | Emergency council address
|`polygonZkEVM` | contract PolygonZkEVMExistentEtrog | New deployed Polygon zkEVM which will be initialized wiht previous values
|`zkEVMVerifier` | contract IVerifierRollup | Verifier of the new zkEVM deployed
|`zkEVMForkID` | uint64 | Fork id of the new zkEVM deployed
|`zkEVMChainID` | uint64 | Chain id of the new zkEVM deployed

### `addNewRollupType`

```solidity
  function addNewRollupType(
    address consensusImplementation,
    contract IVerifierRollup verifier,
    uint64 forkID,
    uint8 genesis,
    bytes32 description
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`consensusImplementation` | address | Consensus implementation
|`verifier` | contract IVerifierRollup | Verifier address
|`forkID` | uint64 | ForkID of the verifier
|`genesis` | uint8 | Genesis block of the rollup
|`description` | bytes32 | Description of the rollup type

### `obsoleteRollupType`

```solidity
  function obsoleteRollupType(
    uint32 rollupTypeID
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupTypeID` | uint32 | Rollup type to obsolete

### `createNewRollup`

```solidity
  function createNewRollup(
    uint32 rollupTypeID,
    uint64 chainID,
    address admin,
    address sequencer,
    address gasTokenAddress,
    string sequencerURL,
    string networkName
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupTypeID` | uint32 | Rollup type to deploy
|`chainID` | uint64 | ChainID of the rollup, must be a new one
|`admin` | address | Admin of the new created rollup
|`sequencer` | address | Sequencer of the new created rollup
|`gasTokenAddress` | address | Indicates the token address that will be used to pay gas fees in the new rollup
Note if a wrapped token of the bridge is used, the original network and address of this wrapped will be used instead
|`sequencerURL` | string | Sequencer URL of the new created rollup
|`networkName` | string | Network name of the new created rollup

### `addExistingRollup`

Add an already deployed rollup.

```solidity
  function addExistingRollup(
    contract IPolygonRollupBase rollupAddress,
    contract IVerifierRollup verifier,
    uint64 forkID,
    uint64 chainID,
    bytes32 genesis,
    uint8 rollupCompatibilityID
  ) external
```

!!! note
    - This rollup does not follow any `rollupType`.

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupAddress` | contract IPolygonRollupBase | Rollup address
|`verifier` | contract IVerifierRollup | Verifier address, must be added before
|`forkID` | uint64 | Fork id of the added rollup
|`chainID` | uint64 | Chain id of the added rollup
|`genesis` | bytes32 | Genesis block for this rollup
|`rollupCompatibilityID` | uint8 | Compatibility ID for the added rollup

### `_addExistingRollup`

Add an already deployed rollup.

```solidity
  function _addExistingRollup(
    contract IPolygonRollupBase rollupAddress,
    contract IVerifierRollup verifier,
    uint64 forkID,
    uint64 chainID,
    uint8 rollupCompatibilityID,
    uint64 lastVerifiedBatch
  ) internal returns (struct PolygonRollupManager.RollupData rollup)
```

!!! note
    - This rollup does not follow any `rollupType`.

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupAddress` | contract IPolygonRollupBase | Rollup address
|`verifier` | contract IVerifierRollup | Verifier address, must be added before
|`forkID` | uint64 | Fork id of the added rollup
|`chainID` | uint64 | Chain id of the added rollup
|`rollupCompatibilityID` | uint8 | Compatibility ID for the added rollup
|`lastVerifiedBatch` | uint64 | Last verified batch before adding the rollup

### `updateRollup`

Upgrade an existing rollup.

```solidity
  function updateRollup(
    contract ITransparentUpgradeableProxy rollupContract,
    uint32 newRollupTypeID,
    bytes upgradeData
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupContract` | contract ITransparentUpgradeableProxy | Rollup consensus proxy address
|`newRollupTypeID` | uint32 | New rolluptypeID to upgrade to
|`upgradeData` | bytes | Upgrade data

### `onSequenceBatches`

Sequence batches, callback called by one of the consensus rollups managed by this contract.

```solidity
  function onSequenceBatches(
    uint64 newSequencedBatches,
    bytes32 newAccInputHash
  ) external returns (uint64)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newSequencedBatches` | uint64 | Number of batches sequenced
|`newAccInputHash` | bytes32 | New accumulate input hash

### `verifyBatches`

Allows an aggregator to verify multiple batches.

```solidity
  function verifyBatches(
    uint32 rollupID,
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    address beneficiary,
    bytes32[24] proof
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`beneficiary` | address | Address that will receive the verification reward
|`proof` | bytes32[24] | Fflonk proof

### `verifyBatchesTrustedAggregator`

Allows a trusted aggregator to verify multiple batches.

```solidity
  function verifyBatchesTrustedAggregator(
    uint32 rollupID,
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    address beneficiary,
    bytes32[24] proof
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`beneficiary` | address | Address that will receive the verification reward
|`proof` | bytes32[24] | Fflonk proof

### `_verifyAndRewardBatches`

Verify and reward batches internal function.

```solidity
  function _verifyAndRewardBatches(
    struct PolygonRollupManager.RollupData rollup,
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    address beneficiary,
    bytes32[24] proof
  ) internal
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollup` | struct PolygonRollupManager.RollupData | Rollup Data storage pointer that will be used to the verification
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`beneficiary` | address | Address that will receive the verification reward
|`proof` | bytes32[24] | Fflonk proof

### `_tryConsolidatePendingState`

Internal function to consolidate the state automatically once sequence or verify batches are called. It tries to consolidate the first and the middle pending state in the queue.

```solidity
  function _tryConsolidatePendingState(
  ) internal
```

### `consolidatePendingState`

Consolidates any pending state that has already exceed the `pendingStateTimeout`. Can be called by the trusted aggregator, which can consolidate any state without the timeout restrictions.

```solidity
  function consolidatePendingState(
    uint32 rollupID,
    uint64 pendingStateNum
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`pendingStateNum` | uint64 | Pending state to consolidate

### `_consolidatePendingState`

Internal function to consolidate any pending state that has already exceed the `pendingStateTimeout`.

```solidity
  function _consolidatePendingState(
    struct PolygonRollupManager.RollupData rollup,
    uint64 pendingStateNum
  ) internal
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollup` | struct PolygonRollupManager.RollupData | Rollup data storage pointer
|`pendingStateNum` | uint64 | Pending state to consolidate

### `overridePendingState`

Allows the trusted aggregator to override the pending state if it is possible to prove a different state root given the same batches.

```solidity
  function overridePendingState(
    uint32 rollupID,
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | Fflonk proof

### `proveNonDeterministicPendingState`

Activates the emergency state if its possible to prove a different state root given the same batches.

```solidity
  function proveNonDeterministicPendingState(
    uint32 rollupID,
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | Fflonk proof

### `_proveDistinctPendingState`

Internal function that proves a different state root given the same batches to verify.

```solidity
  function _proveDistinctPendingState(
    struct PolygonRollupManager.RollupData rollup,
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) internal
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollup` | struct PolygonRollupManager.RollupData | Rollup Data struct that will be checked
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | Fflonk proof

### `_updateBatchFee`

Function to update the batch fee based on the new verified batches. The batch fee is not updated when the trusted aggregator verifies batches.

```solidity
  function _updateBatchFee(
    struct PolygonRollupManager.RollupData newLastVerifiedBatch
  ) internal
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newLastVerifiedBatch` | struct PolygonRollupManager.RollupData | New last verified batch

### `activateEmergencyState`

Function to activate emergency state, which also enables the emergency mode on both `PolygonRollupManager` and `PolygonZkEVMBridge` contracts. If not called by the owner, it must not have been aggregated within a `_HALT_AGGREGATION_TIMEOUT` period and an emergency state should not have happened in the same period.

```solidity
  function activateEmergencyState(
  ) external
```

### `deactivateEmergencyState`

Function to deactivate emergency state on both `PolygonRollupManager` and `PolygonZkEVMBridge` contracts.

```solidity
  function deactivateEmergencyState(
  ) external
```

### `_activateEmergencyState`

Internal function to activate emergency state on both `PolygonRollupManager` and `PolygonZkEVMBridge` contracts.

```solidity
  function _activateEmergencyState(
  ) internal
```

### `setTrustedAggregatorTimeout`

Set a new pending state timeout. The timeout can only be lowered, except if emergency state is active.

```solidity
  function setTrustedAggregatorTimeout(
    uint64 newTrustedAggregatorTimeout
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedAggregatorTimeout` | uint64 | Trusted aggregator timeout

### `setPendingStateTimeout`

Set a new trusted aggregator timeout. The timeout can only be lowered, except if emergency state is active.

```solidity
  function setPendingStateTimeout(
    uint64 newPendingStateTimeout
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newPendingStateTimeout` | uint64 | Trusted aggregator timeout

### `setMultiplierBatchFee`

Set a new multiplier batch fee.

```solidity
  function setMultiplierBatchFee(
    uint16 newMultiplierBatchFee
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newMultiplierBatchFee` | uint16 | multiplier batch fee

### `setVerifyBatchTimeTarget`

Set a new verify batch time target. This value will only be relevant once the aggregation is decentralized, so the `trustedAggregatorTimeout` should be zero or very close to zero.

```solidity
  function setVerifyBatchTimeTarget(
    uint64 newVerifyBatchTimeTarget
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newVerifyBatchTimeTarget` | uint64 | Verify batch time target

### `setBatchFee`

```solidity
  function setBatchFee(
    uint256 newBatchFee
  ) external
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newBatchFee` | uint256 | new batch fee

### `getRollupExitRoot`

Get the current rollup exit root: Compute the rollup exit root by using all the local exit roots of all rollups. 

```solidity
  function getRollupExitRoot(
  ) public returns (bytes32)
```

### `getLastVerifiedBatch`

```solidity
  function getLastVerifiedBatch(
  ) public returns (uint64)
```

### `_getLastVerifiedBatch`

```solidity
  function _getLastVerifiedBatch(
  ) internal returns (uint64)
```

### `isPendingStateConsolidable`

Returns a boolean that indicates if the `pendingStateNum` is consolidate-able.

```solidity
  function isPendingStateConsolidable(
    uint32 rollupID,
    uint64 pendingStateNum
  ) public returns (bool)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup id
|`pendingStateNum` | uint64 | Pending state number to check

!!! note
    - This function does not check if the pending state currently exists, or if it's consolidated already.

### `_isPendingStateConsolidable`

Returns a boolean that indicates if the `pendingStateNum` is consolidate-able.

```solidity
  function _isPendingStateConsolidable(
    struct PolygonRollupManager.RollupData rollup,
    uint64 pendingStateNum
  ) internal returns (bool)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollup` | struct PolygonRollupManager.RollupData | Rollup data storage pointer
|`pendingStateNum` | uint64 | Pending state number to check

!!! note
    - This function does not check if the pending state currently exists, or if it's consolidated already.

### `calculateRewardPerBatch`

Function to calculate the reward to verify a single batch.

```solidity
  function calculateRewardPerBatch(
  ) public returns (uint256)
```

### `getBatchFee`

This function is used instead of the automatic public view one.

```solidity
  function getBatchFee(
  ) public returns (uint256)
```

### `getForcedBatchFee`

```solidity
  function getForcedBatchFee(
  ) public returns (uint256)
```

### `getInputSnarkBytes`

Function to calculate the input snark bytes.

```solidity
  function getInputSnarkBytes(
    uint32 rollupID,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 oldStateRoot,
    bytes32 newStateRoot
  ) public returns (bytes)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup id used to calculate the input snark bytes
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`oldStateRoot` | bytes32 | State root before batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed

### `_getInputSnarkBytes`

Function to calculate the input snark bytes.

```solidity
  function _getInputSnarkBytes(
    struct PolygonRollupManager.RollupData rollup,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 oldStateRoot,
    bytes32 newStateRoot
  ) internal returns (bytes)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollup` | struct PolygonRollupManager.RollupData | Rollup data storage pointer
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`oldStateRoot` | bytes32 | State root before batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed

### `_checkStateRootInsidePrime`

Function to check if the state root is inside of the prime field.

```solidity
  function _checkStateRootInsidePrime(
    uint256 newStateRoot
  ) internal returns (bool)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newStateRoot` | uint256 | New State root once the batch is processed

### `getRollupBatchNumToStateRoot`

Get rollup state root given a batch number.

```solidity
  function getRollupBatchNumToStateRoot(
    uint32 rollupID,
    uint64 batchNum
  ) public returns (bytes32)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`batchNum` | uint64 | Batch number

### `getRollupSequencedBatches`

Get rollup sequence batches struct given a batch number.

```solidity
  function getRollupSequencedBatches(
    uint32 rollupID,
    uint64 batchNum
  ) public returns (struct LegacyZKEVMStateVariables.SequencedBatchData)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`batchNum` | uint64 | Batch number

### `getRollupPendingStateTransitions`

Get rollup sequence pending state struct given a batch number.

```solidity
  function getRollupPendingStateTransitions(
    uint32 rollupID,
    uint64 batchNum
  ) public returns (struct LegacyZKEVMStateVariables.PendingState)
```

#### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`rollupID` | uint32 | Rollup identifier
|`batchNum` | uint64 | Batch number

## Events

### `AddNewRollupType`

Emitted when a new rollup type is added.

```solidity
  event AddNewRollupType(
  )
```

### `ObsoleteRollupType`

Emitted when a a rollup type is obsoleted.

```solidity
  event ObsoleteRollupType(
  )
```

### `CreateNewRollup`

Emitted when a new rollup is created based on a `rollupType`.

```solidity
  event CreateNewRollup(
  )
```

### `AddExistingRollup`

Emitted when an existing rollup is added.

```solidity
  event AddExistingRollup(
  )
```

### `UpdateRollup`

Emitted when a rollup is updated.

```solidity
  event UpdateRollup(
  )
```

### `OnSequenceBatches`

Emitted when a new verifier is added.

```solidity
  event OnSequenceBatches(
  )
```

### `VerifyBatches`

Emitted when an aggregator verifies batches.

```solidity
  event VerifyBatches(
  )
```

### `VerifyBatchesTrustedAggregator`

Emitted when the trusted aggregator verifies batches.

```solidity
  event VerifyBatchesTrustedAggregator(
  )
```

### `ConsolidatePendingState`

Emitted when pending state is consolidated.

```solidity
  event ConsolidatePendingState(
  )
```

### `ProveNonDeterministicPendingState`

Emitted when is proved a different state given the same batches.

```solidity
  event ProveNonDeterministicPendingState(
  )
```

### `OverridePendingState`

Emitted when the trusted aggregator overrides pending state.

```solidity
  event OverridePendingState(
  )
```

### `SetTrustedAggregatorTimeout`

Emitted when is updated the trusted aggregator timeout.

```solidity
  event SetTrustedAggregatorTimeout(
  )
```

### `SetPendingStateTimeout`

Emitted when is updated the pending state timeout.

```solidity
  event SetPendingStateTimeout(
  )
```

### `SetMultiplierBatchFee`

Emitted when is updated the multiplier batch fee.

```solidity
  event SetMultiplierBatchFee(
  )
```

### `SetVerifyBatchTimeTarget`

Emitted when is updated the verify batch timeout

```solidity
  event SetVerifyBatchTimeTarget(
  )
```

### `SetTrustedAggregator`

Emitted when is updated the trusted aggregator address.

```solidity
  event SetTrustedAggregator(
  )
```

### `SetBatchFee`

Emitted when is updated the batch fee.

```solidity
  event SetBatchFee(
  )
```
