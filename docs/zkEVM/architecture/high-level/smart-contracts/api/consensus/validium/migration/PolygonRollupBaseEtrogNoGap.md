## Functions

### `constructor`

```solidity
  function constructor(
    contract IPolygonZkEVMGlobalExitRootV2 _globalExitRootManager,
    contract IERC20Upgradeable _pol,
    contract IPolygonZkEVMBridgeV2 _bridgeAddress,
    contract PolygonRollupManager _rollupManager
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_globalExitRootManager` | contract IPolygonZkEVMGlobalExitRootV2 | Global exit root manager address. | 
|`_pol` | contract IERC20Upgradeable | POL token address. |
|`_bridgeAddress` | contract IPolygonZkEVMBridgeV2 | Bridge address. |
|`_rollupManager` | contract PolygonRollupManager | Global exit root manager address. |

### `initialize`

```solidity
  function initialize(
    address _admin,
    address sequencer,
    uint32 networkID,
    address _gasTokenAddress,
    string sequencerURL,
    string _networkName
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_admin` | address | Admin address. | 
|`sequencer` | address | Trusted sequencer address. |
|`networkID` | uint32 | Indicates the network identifier used in the bridge. |
|`sequencerURL` | string | Trusted sequencer URL. |
|`_networkName` | string | L2 network name. |

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
|`batches` | struct PolygonRollupBaseEtrogNoGap.BatchData[] | Struct array which holds the data necessary for appending new batches to the sequence. |
|`maxSequenceTimestamp` | uint64 | Max timestamp of the sequence. This timestamp must be inside a safety range (actual + 36 seconds). </br> This timestamp should be equal or greater than the last block inside the sequence. Otherwise the batch is invalidated by circuit. | 
|`initSequencedBatch` | uint64 | This parameter must match the current last batch sequenced. </br> This a protection mechanism against the sequencer sending undesired data. | 
|`l2Coinbase` | address | Address that will receive the fees from L2. </br> 
Note that POL is not a reentrant token. | 

### `onVerifyBatches`

Callback on verify batches. Can only be called by the rollup manager.

```solidity
  function onVerifyBatches(
    uint64 lastVerifiedBatch,
    bytes32 newStateRoot,
    address aggregator
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`lastVerifiedBatch` | uint64 | Last verified batch. |
|`newStateRoot` | bytes32 | New state root. |
|`aggregator` | address | Aggregator address. |

### `forceBatch`

Allows a user to force a batch of L2 transactions. This should be used only in extreme cases where the trusted sequencer does not work as expected.

!!! note
    - The sequencer has a certain degree of control over how non-forced and forced batches are ordered.
    - In order to assure that users' force transactions are processed properly, users must sign each transaction with a unique nonce.

```solidity
  function forceBatch(
    bytes transactions,
    uint256 polAmount
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`transactions` | bytes | L2 ethereum transactions. EIP-155 or pre-EIP-155 with signature. |
|`polAmount` | uint256 | Maximum amount of POL tokens the sender is willing to pay. |

### `sequenceForceBatches`

Allows anyone to sequence forced batches if the trusted sequencer has not done so within the timeout period.

```solidity
  function sequenceForceBatches(
    struct PolygonRollupBaseEtrogNoGap.BatchData[] batches
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`batches` | struct PolygonRollupBaseEtrogNoGap.BatchData[] | Struct array which holds the necessary data to append force batches

### `setTrustedSequencer`

Allows the admin to set a new trusted sequencer.

```solidity
  function setTrustedSequencer(
    address newTrustedSequencer
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedSequencer` | address | Address of the new trusted sequencer. |

### `setTrustedSequencerURL`

Allows the admin to set the trusted sequencer URL.

```solidity
  function setTrustedSequencerURL(
    string newTrustedSequencerURL
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newTrustedSequencerURL` | string | URL of trusted sequencer

### `setForceBatchAddress`

Allows the admin to change the address allowed to force batches. If address 0 is set, then anyone is able to force batches.

This action is irreversible.

```solidity
  function setForceBatchAddress(
    address newForceBatchAddress
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newForceBatchAddress` | address | New force batch address. |

### `setForceBatchTimeout`

Allow the admin to set the `forcedBatchTimeout`. The new value can only be lower, except for when the emergency state is active.

```solidity
  function setForceBatchTimeout(
    uint64 newforceBatchTimeout
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newforceBatchTimeout` | uint64 | New force batch timeout. |

### `transferAdminRole`

```solidity
  function transferAdminRole(
    address newPendingAdmin
  ) external
```

Starts the admin role transfer. This is a two step process. The pending admin must be accepted in order to finalize the process.

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`newPendingAdmin` | address | Address of the new pending admin. |

### `acceptAdminRole`

Allow the current pending admin to accept the admin role.

```solidity
  function acceptAdminRole(
  ) external
```

### `calculatePolPerForceBatch`

```solidity
  function calculatePolPerForceBatch(
  ) public returns (uint256)
```

A function that calculates the reward for a forced batch.

### `generateInitializeTransaction`

Generates the initialize transaction for the bridge on L2.

```solidity
  function generateInitializeTransaction(
    uint32 networkID,
    address _gasTokenAddress,
    uint32 _gasTokenNetwork,
    bytes _gasTokenMetadata
  ) public returns (bytes)
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`networkID` | uint32 | Indicates the network identifier used in the bridge. |
|`_gasTokenAddress` | address | Indicates the token address used to pay gas fees in the new rollup. |
|`_gasTokenNetwork` | uint32 | Indicates the native network of the token address. |
|`_gasTokenMetadata` | bytes | Abi encoded gas token metadata. |

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

Emitted when forced batches are sequenced by an entity other than the trusted sequencer.

```solidity
  event SequenceForceBatches(
  )
```

### `InitialSequenceBatches`

Emitted when a contract containing the first sequenced transaction is initialized.

```solidity
  event InitialSequenceBatches(
  )
```

### `VerifyBatches`

Emitted when a aggregator verifies batches.

```solidity
  event VerifyBatches(
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

### `SetForceBatchTimeout`

Emitted when the admin updates the force batch timeout.

```solidity
  event SetForceBatchTimeout(
  )
```

### `SetForceBatchAddress`

Emitted when the admin updates the force batch address.

```solidity
  event SetForceBatchAddress(
  )
```

### `TransferAdminRole`

Emitted when the admin starts the two-step transfer role of setting a new pending admin.

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
