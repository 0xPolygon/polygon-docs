## Functions

### `constructor`

```solidity
  function constructor(
    contract IPolygonZkEVMGlobalExitRoot _globalExitRootManager,
    contract IERC20Upgradeable _matic,
    contract IVerifierRollup _rollupVerifier,
    contract IPolygonZkEVMBridge _bridgeAddress,
    contract ICDKDataCommittee _dataCommitteeAddress,
    uint64 _chainID,
    uint64 _forkID
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRoot | Global exit root manager address
|`_matic` | contract IERC20Upgradeable | MATIC token address
|`_rollupVerifier` | contract IVerifierRollup | Rollup verifier address
|`_bridgeAddress` | contract IPolygonZkEVMBridge | Bridge address
|`_dataCommitteeAddress` | contract ICDKDataCommittee | Data committee address
|`_chainID` | uint64 | L2 chainID
|`_forkID` | uint64 | Fork Id

### `initialize`

```solidity
  function initialize(
    struct CDKValidium.InitializePackedParameters initializePackedParameters,
    bytes32 genesisRoot,
    string _trustedSequencerURL,
    string _networkName
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`initializePackedParameters` | struct CDKValidium.InitializePackedParameters | Struct to save gas and avoid stack too deep errors
|`genesisRoot` | bytes32 | Rollup genesis root
|`_trustedSequencerURL` | string | Trusted sequencer URL
|`_networkName` | string | L2 network name

### `sequenceBatches`

Allows a sequencer to send multiple batches.

```solidity
  function sequenceBatches(
    struct CDKValidium.BatchData[] batches,
    address l2Coinbase,
    bytes signaturesAndAddrs
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct CDKValidium.BatchData[] | Struct array which holds the necessary data to append new batches to the sequence
|`l2Coinbase` | address | Address that will receive the fees from L2
|`signaturesAndAddrs` | bytes | Byte array containing the signatures and all the addresses of the committee in ascending order
[signature 0, ..., signature requiredAmountOfSignatures -1, address 0, ... address N]
note that each ECDSA signatures are used, therefore each one must be 65 bytes

### `verifyBatches`

Allows an aggregator to verify multiple batches.

```solidity
  function verifyBatches(
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `verifyBatchesTrustedAggregator`

Allows an aggregator to verify multiple batches.

```solidity
  function verifyBatchesTrustedAggregator(
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `_verifyAndRewardBatches`

Verify and reward batches internal function.

```solidity
  function _verifyAndRewardBatches(
    uint64 pendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`pendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `_tryConsolidatePendingState`

Internal function to consolidate the state automatically once sequence or verify batches are called. It tries to consolidate the first and the middle pending state in the queue.

```solidity
  function _tryConsolidatePendingState(
  ) internal
```

### `consolidatePendingState`

Consolidates any pending state that has already exceed the `pendingStateTimeout`.
Can be called by the trusted aggregator, which can consolidate any state without the timeout restrictions.

```solidity
  function consolidatePendingState(
    uint64 pendingStateNum
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`pendingStateNum` | uint64 | Pending state to consolidate

### `_consolidatePendingState`

Internal function to consolidate any pending state that has already exceed the `pendingStateTimeout`.

```solidity
  function _consolidatePendingState(
    uint64 pendingStateNum
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`pendingStateNum` | uint64 | Pending state to consolidate

### `_updateBatchFee`

Function to update the batch fee based on the new verified batches. The batch fee will not be updated when the trusted aggregator verifies batches.

```solidity
  function _updateBatchFee(
    uint64 newLastVerifiedBatch
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newLastVerifiedBatch` | uint64 | New last verified batch

### `forceBatch`

Allows a sequencer/user to force a batch of L2 transactions. This should be used only in extreme cases where the trusted sequencer does not work as expected.

```solidity
  function forceBatch(
    bytes transactions,
    uint256 maticAmount
  ) public
```

!!! note
    - The sequencer has a certain degree of control on how non-forced and forced batches are ordered.
    - In order to assure that users force transactions are processed properly, user must not sign any other transaction with the same nonce.

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`transactions` | bytes | L2 ethereum transactions EIP-155 or pre-EIP-155 with signature:
|`maticAmount` | uint256 | Max amount of MATIC tokens that the sender is willing to pay

### `sequenceForceBatches`

Allows anyone to sequence forced batches if the trusted sequencer has not done so within the timeout period.

```solidity
  function sequenceForceBatches(
    struct CDKValidium.ForcedBatchData[] batches
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct CDKValidium.ForcedBatchData[] | Struct array which holds the necessary data to append force batches

### `setTrustedSequencer`

Allow the admin to set a new trusted sequencer.

```solidity
  function setTrustedSequencer(
    address newTrustedSequencer
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedSequencer` | address | Address of the new trusted sequencer

### `setTrustedSequencerURL`

Allow the admin to set the trusted sequencer URL.

```solidity
  function setTrustedSequencerURL(
    string newTrustedSequencerURL
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedSequencerURL` | string | URL of trusted sequencer

### `setTrustedAggregator`

Allow the admin to set a new trusted aggregator address.

```solidity
  function setTrustedAggregator(
    address newTrustedAggregator
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedAggregator` | address | Address of the new trusted aggregator

### `setTrustedAggregatorTimeout`

Allow the admin to set a new pending state timeout. The timeout can only be lowered, except if emergency state is active.

```solidity
  function setTrustedAggregatorTimeout(
    uint64 newTrustedAggregatorTimeout
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedAggregatorTimeout` | uint64 | Trusted aggregator timeout

### `setPendingStateTimeout`

Allow the admin to set a new trusted aggregator timeout. The timeout can only be lowered, except if emergency state is active.

```solidity
  function setPendingStateTimeout(
    uint64 newPendingStateTimeout
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newPendingStateTimeout` | uint64 | Trusted aggregator timeout

### `setMultiplierBatchFee`

Allow the admin to set a new multiplier batch fee.

```solidity
  function setMultiplierBatchFee(
    uint16 newMultiplierBatchFee
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newMultiplierBatchFee` | uint16 | multiplier batch fee

### `setVerifyBatchTimeTarget`

Allow the admin to set a new verify batch time target. This value is only relevant when aggregation is decentralized, so the trustedAggregatorTimeout should be zero or very close to zero.

```solidity
  function setVerifyBatchTimeTarget(
    uint64 newVerifyBatchTimeTarget
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newVerifyBatchTimeTarget` | uint64 | Verify batch time target

### `setForceBatchTimeout`

Allow the admin to set the `forcedBatchTimeout`. The new value can only be lower, except if emergency state is active.

```solidity
  function setForceBatchTimeout(
    uint64 newforceBatchTimeout
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newforceBatchTimeout` | uint64 | New force batch timeout

### `activateForceBatches`

Allow the admin to turn on the force batches. This action is not reversible.

```solidity
  function activateForceBatches(
  ) external
```

### `transferAdminRole`

Starts the admin role transfer. This is a two step process, the pending admin must accepted to finalize the process.

```solidity
  function transferAdminRole(
    address newPendingAdmin
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newPendingAdmin` | address | Address of the new pending admin

### `acceptAdminRole`

Allows the current pending admin to accept the admin role.

```solidity
  function acceptAdminRole(
  ) external
```

### `overridePendingState`

Allows the trusted aggregator to override the pending state if it's possible to prove a different state root given the same batches.

```solidity
  function overridePendingState(
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `proveNonDeterministicPendingState`

Allows to halt the CDKValidium if its possible to prove a different state root given the same batches.

```solidity
  function proveNonDeterministicPendingState(
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `_proveDistinctPendingState`

Internal function that proves a different state root given the same batches to verify.

```solidity
  function _proveDistinctPendingState(
    uint64 initPendingStateNum,
    uint64 finalPendingStateNum,
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 newStateRoot,
    bytes32[24] proof
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`initPendingStateNum` | uint64 | Init pending state, 0 if consolidated state is used
|`finalPendingStateNum` | uint64 | Final pending state, that will be used to compare with the newStateRoot
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 |  New local exit root once the batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed
|`proof` | bytes32[24] | fflonk proof

### `activateEmergencyState`

Function to activate emergency state, which also enables the emergency mode on both `CDKValidium` and `PolygonZkEVMBridge` contracts. If not called by the owner must be provided a `batchNum` that does not have been aggregated within the  `_HALT_AGGREGATION_TIMEOUT` period.

```solidity
  function activateEmergencyState(
    uint64 sequencedBatchNum
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`sequencedBatchNum` | uint64 | Sequenced batch number that has not been aggregated in _HALT_AGGREGATION_TIMEOUT

### `deactivateEmergencyState`

Function to deactivate emergency state on both CDKValidium and PolygonZkEVMBridge contracts.

```solidity
  function deactivateEmergencyState(
  ) external
```

### `_activateEmergencyState`

Internal function to activate emergency state on both CDKValidium and PolygonZkEVMBridge contracts.

```solidity
  function _activateEmergencyState(
  ) internal
```

### `getForcedBatchFee`

```solidity
  function getForcedBatchFee(
  ) public returns (uint256)
```

### `getLastVerifiedBatch`

```solidity
  function getLastVerifiedBatch(
  ) public returns (uint64)
```

### `isPendingStateConsolidable`

Returns a boolean that indicates if the `pendingStateNum` is consolidate-able.

```solidity
  function isPendingStateConsolidable(
  ) public returns (bool)
```

!!! note
    - This function does not check if the pending state currently exists, or if it's consolidated already.

### `calculateRewardPerBatch`

Function to calculate the reward to verify a single batch. 

```solidity
  function calculateRewardPerBatch(
  ) public returns (uint256)
```

### `getInputSnarkBytes`

Function to calculate the input snark bytes.

```solidity
  function getInputSnarkBytes(
    uint64 initNumBatch,
    uint64 finalNewBatch,
    bytes32 newLocalExitRoot,
    bytes32 oldStateRoot,
    bytes32 newStateRoot
  ) public returns (bytes)
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`initNumBatch` | uint64 | Batch which the aggregator starts the verification
|`finalNewBatch` | uint64 | Last batch aggregator intends to verify
|`newLocalExitRoot` | bytes32 | New local exit root once the batch is processed
|`oldStateRoot` | bytes32 | State root before batch is processed
|`newStateRoot` | bytes32 | New State root once the batch is processed

### `checkStateRootInsidePrime`

```solidity
  function checkStateRootInsidePrime(
  ) public returns (bool)
```

## Events

### `SequenceBatches`

Emitted when the trusted sequencer sends a new batch of transactions.

```solidity
  event SequenceBatches(
  )
```

### `ForceBatch`

Emitted when a batch is forced.

```solidity
  event ForceBatch(
  )
```

### `SequenceForceBatches`

Emitted when forced batches are sequenced by not the trusted sequencer.

```solidity
  event SequenceForceBatches(
  )
```

### `VerifyBatches`

Emitted when a aggregator verifies batches.

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

### `SetTrustedSequencer`

Emitted when the admin updates the trusted sequencer address.

```solidity
  event SetTrustedSequencer(
  )
```

### `SetTrustedSequencerURL`

Emitted when the admin updates the sequencer URL.

```solidity
  event SetTrustedSequencerURL(
  )
```

### `SetTrustedAggregatorTimeout`

Emitted when the admin updates the trusted aggregator timeout.

```solidity
  event SetTrustedAggregatorTimeout(
  )
```

### `SetPendingStateTimeout`

Emitted when the admin updates the pending state timeout.

```solidity
  event SetPendingStateTimeout(
  )
```

### `SetTrustedAggregator`

Emitted when the admin updates the trusted aggregator address.

```solidity
  event SetTrustedAggregator(
  )
```

### `SetMultiplierBatchFee`

Emitted when the admin updates the multiplier batch fee.

```solidity
  event SetMultiplierBatchFee(
  )
```

### `SetVerifyBatchTimeTarget`

Emitted when the admin updates the verify batch timeout.

```solidity
  event SetVerifyBatchTimeTarget(
  )
```

### `SetForceBatchTimeout`

Emitted when the admin update the force batch timeout.

```solidity
  event SetForceBatchTimeout(
  )
```

### `ActivateForceBatches`

Emitted when activate force batches.

```solidity
  event ActivateForceBatches(
  )
```

### `TransferAdminRole`

Emitted when the admin starts the two-step transfer role setting a new pending admin.

```solidity
  event TransferAdminRole(
  )
```

### `AcceptAdminRole`

Emitted when the pending admin accepts the admin role.

```solidity
  event AcceptAdminRole(
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

### `UpdateZkEVMVersion`

Emitted every time the forkID is updated; this includes the first initialization of the contract. This event should be emitted on every upgrade of the contract with relevant changes for the nodes.

```solidity
  event UpdateZkEVMVersion(
  )
```
