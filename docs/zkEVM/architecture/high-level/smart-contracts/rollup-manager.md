The [rollup manager contract](https://github.com/0xPolygonHermez/zkevm-contracts/blob/feature/etrog/contracts/v2/PolygonRollupManager.sol) creates, adds, removes, and manages rollups.

## Required structs

### `RollupType`

Each new rollup has a `RollupType` struct which defines the consensus implementation and some specifics.

```solidity
/**
* @notice Struct that stores the rollup type data.
* @param consensusImplementation Consensus implementation (contains the consensus logic for the transparent proxy).
* @param verifier verifier
* @param forkID fork ID
* @param rollupCompatibilityID Rollup compatibility ID, which checks for upgradability between rollup types.
* @param obsolete Indicates if the rollup type is obsolete.
* @param genesis Genesis block of the rollup, only used on creating new rollups.
*/
struct RollupType {
    address consensusImplementation;
    IVerifierRollup verifier;
    uint64 forkID;
    uint8 rollupCompatibilityID;
    bool obsolete;
    bytes32 genesis;
}
```

- The consensus implementation address is the address of the consensus contract responsible for sequencing batches.
- The `IVerifierRollup` parameter enables verification of each proof sent by the aggregator.
- The `forkID` tracks changes in rollup processing.
- The rollup compatibility identifier is used to prevent compatibility errors when the rollup needs an upgrade.
- The obsolete flag indicates whether the rollup is obsolete or not.
- The genesis block is the rollup's initial block and can include a small initial state.

!!! note
    - Several rollups can have the same `RollupType`​.
    - This means they share consensus and batch verification smart contracts.

### `RollupData`

Rollup state data is included in a struct called [`RollupData`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L68).

```solidity
/**
* @notice Struct which to store the rollup data of each chain
* @param rollupContract Rollup consensus contract, which manages everything
* related to sequencing transactions
* @param chainID Chain ID of the rollup
* @param verifier Verifier contract
* @param forkID ForkID of the rollup
* @param batchNumToStateRoot State root mapping
* @param sequencedBatches Queue of batches that defines the virtual state
* @param pendingStateTransitions Pending state mapping
* @param lastLocalExitRoot Last exit root verified, used for compute the rollupExitRoot
* @param lastBatchSequenced Last batch sent by the consensus contract
* @param lastVerifiedBatch Last batch verified
* @param lastPendingState Last pending state
* @param lastPendingStateConsolidated Last pending state consolidated
* @param lastVerifiedBatchBeforeUpgrade Last batch verified before the last upgrade
* @param rollupTypeID Rollup type ID, can be 0 if it was added as an existing rollup
* @param rollupCompatibilityID Rollup ID used for compatibility checks when upgrading
*/
struct RollupData {
    IPolygonRollupBase rollupContract;
    uint64 chainID;
    IVerifierRollup verifier;
    uint64 forkID;
    mapping(uint64 batchNum => bytes32) batchNumToStateRoot;
    mapping(uint64 batchNum => SequencedBatchData) sequencedBatches;
    mapping(uint256 pendingStateNum => PendingState) pendingStateTransitions;
    bytes32 lastLocalExitRoot;
    uint64 lastBatchSequenced;
    uint64 lastVerifiedBatch;
    uint64 lastPendingState;
    uint64 lastPendingStateConsolidated;
    uint64 lastVerifiedBatchBeforeUpgrade;
    uint64 rollupTypeID;
    uint8 rollupCompatibilityID;
}
```

The struct contains:

- Information about the current state of the rollup (e.g., the current batch being sequenced or verified, the states root for each batch, etc.)
- Information about the bridge within the rollup, such as the current local exit root.
- Data about [forced batches](../../protocol/malfunction-resistance/sequencer-resistance.md).

## Create new rollup

### `addNewRollupType(...)` 

The [`addNewRollupType(...)`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L493) function adds a new rollup type to the rollup manager.

### `createNewRollup(...)` 

The [`createNewRollup(...)`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L557) function creates a new rollup using [OpenZeppelin's transparent proxy pattern](https://blog.openzeppelin.com/the-transparent-proxy-pattern) which instantiates the `PolygonTransparentProxy` contract.

```solidity
/**
* @notice Create a new rollup
* @param rollupTypeID Rollup type to deploy
* @param chainID ChainID of the rollup, must be a new one
* @param admin Admin of the new created rollup
* @param sequencer Sequencer of the new created rollup
* @param gasTokenAddress Indicates the token address that will be used to pay gas fees in the new rollup
* Note if a wrapped token of the bridge is used, the original network and address of this wrapped will be used instead
* @param sequencerURL Sequencer URL of the new created rollup
* @param networkName Network name of the new created rollup
*/
function createNewRollup(
    uint32 rollupTypeID,
    uint64 chainID,
    address admin,
    address sequencer,
    address gasTokenAddress,
    string memory sequencerURL,
    string memory networkName
) external onlyRole(_CREATE_ROLLUP_ROLE)
```

The function specifies the following:

- The consensus contract specified by rollup type.
- The associated non-obsolete rollup type identifier, which should be existing.
- The `chainID` of the rollup, which should be new among the Polygon network's rollup chain IDs.
- The address of the rollup admin, who can update several parameters of the consensus contract. For instance, setting a trusted sequencer or a force batches address.
- The address of the trusted sequencer, which is the node responsible for sending the transaction for executing the `sequenceBatches` function.
- The address of the token address used to pay gas fees, in the newly created rollup.

`RollupData` is partially filled and stored in the `rollupIDToRollupData`​ mapping within the contract’s storage.

Once the function is finished building the new rollup, it initializes it using the `initialize(...)`​ function which sets all the roles and contracts addresses. 

The figure below depicts the process of creating and initializing a new rollup instance. Notice the empty state in the exit trees.

![ulxly-process-initializing-new-rollup](../../../../img/zkEVM/ulxly-process-initializing-new-rollup.png)

## Add existing rollup

Rollups that are already deployed and functional can be added to the rollup manager. They do not have a rollup type.

### `addExistingRollup(...)`

The [`addExistingRollup(...)`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L638) function adds an already existing rollup to the rollup manager by specifying its current address.

```solidity
/**
* @notice Add an already deployed rollup
* note that this rollup does not follow any rollupType
* @param rollupAddress Rollup address
* @param verifier Verifier address, must be added before
* @param forkID Fork id of the added rollup
* @param chainID Chain id of the added rollup
* @param genesis Genesis block for this rollup
* @param rollupCompatibilityID Compatibility ID for the added rollup
*/
function addExistingRollup(
    IPolygonRollupBase rollupAddress,
    IVerifierRollup verifier,
    uint64 forkID,
    uint64 chainID,
    bytes32 genesis,
    uint8 rollupCompatibilityID
) external onlyRole(_ADD_EXISTING_ROLLUP_ROLE) 
```

The `IVerifierRollup` interface requests the raw consensus contract address which will be accessed through a proxy to allow upgradeability options.

Since the rollup has previously been initialized, the following information needs to be provided:

- The consensus contract, implementing the [`IPolygonRollupBase`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/develop/contracts/v2/interfaces/IPolygonRollupBase.sol) interface.
- The verifier contract, implementing the [`IVerifierRollup`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/develop/contracts/interfaces/IVerifierRollup.sol) interface.
- The `forkID` of the existent rollup.
- The `chainID` of the existent rollup.
- The genesis block of the rollup.
- The `rollupCompatibilityID`.

!!! tip
    `RollupData` of already existing rollups is constructed by hand, since they do not have a rollup type.

The diagram below depicts the integration of an existing and operational rollup into the `RollupManager`. In this case, the state tree has information which is added to the manager.

![ulxly-existing-rollup-incorporate](../../../../img/zkEVM/ulxly-existing-rollup-incorporate.png)

## Update rollup

### `updateRollup(...)`

In order to change the consensus mechanism, a user with appropriate rights invokes the function [`updateRollup(...)`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L717).

```solidity
/**
* @notice Upgrade an existing rollup
* @param rollupContract Rollup consensus proxy address
* @param newRollupTypeID New rolluptypeID to upgrade to
* @param upgradeData Upgrade data
*/
function updateRollup(
    ITransparentUpgradeableProxy rollupContract,
    uint32 newRollupTypeID,
    bytes calldata upgradeData
) external onlyRole(_UPDATE_ROLLUP_ROLE)
```

Calling this function changes the transparent proxy implementation. Below is a schematic representation of the transparent proxy pattern within the rollup manager context.

![ulxly-transparent-proxy-pattern](../../../../img/zkEVM/ulxly-transparent-proxy-pattern.png)

!!! tip
    - Proxies are frequently utilized in Ethereum for upgradability.
    - Check the documentation for more information on [upgradability](../../protocol/upgradability.md).


In the upgrading procedure, the $\texttt{rollupCompatibilityID}$ comes into play:

- In order to avoid errors, we can only upgrade to a rollup type having the same compatibility identifier as the original one. 
- If this is not the case, the transaction is reverted, raising the $\texttt{UpdateNotCompatible}$ error.

## Remove rollup type

### `obsoleteRollupType(...)` 

The [`obsoleteRollupType(...)`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L527) obsoletes an existing rollup type.

!!! tip
    - It is not possible to create a new rollup of an obsolete rollup type.
