## Exit trees

Due to the presence of multiple rollup stacks in the unified bridge functionality, it becomes necessary to adjust the global exit tree so as to accommodate exits across all the stacks.

- Mainnet has a local exit tree built as an append-only tree of 32 levels.
- Each rollup has a local exit tree which is also built as an append-only tree of 32 levels.
- All the rollups are grouped together in a tree of rollups called the rollup exit tree, which is again built as an append-only tree of 32 levels.

![Unified bridge mainnet and rollup exit trees](../../../../img/zkEVM/ulxly-mainnet-and-rollup-exit-trees.png)

## Global index

When creating and verifying proofs, an index called $\texttt{globalIndex}$ is used to uniquely locate a leaf in the new global exit tree.

A $\texttt{globalIndex}$​​​ is a 256-bit string composed of unused bits, mainnet flag, rollup index bits, and local root index bits.

$$
\texttt{globalIndex} = \texttt{(unused bits)_} \texttt{(mainnet flag)_} \texttt{(rollupIndex)_} \texttt{(local root index)}
$$

Starting from the most significant bit, a $\texttt{globalIndex}$ consists of the following bits:

- $191$ bits of unused bits: These bits are unused, and can be filled with any value. The best option is to fill them with zeros because zeros are cheaper.
- $1$ bit of mainnet flag: This single bit serves as a flag indicating whether an exit pertains to a rollup (represented by $0$) or the mainnet (indicated by $1$).
- $32$ bit of the rollup Index: These bits indicate the specific rollup being pointed at, within the rollup exit tree. These bits are therefore only used whenever mainnet flag is $0$.
- $32$ bits of the local root index: These bits indicate the specific index being pointed at, within each rollup's local exit tree.

The figure below depicts how the $\texttt{globalIndex}$ is interpreted:

- The mainnet exit tree has the $\texttt{globalIndex = X_1_X_3}$, where 
  - the $\texttt{mainnet flag}$ equals $\texttt{1}$ to indicates that it's the mainnet, and 
  - the $\texttt{local root index}$ being $\texttt{3}$ points at the fourth leaf in the mainnet exit tree.
- The rollup 9002's exit tree has the $\texttt{globalIndex = X_0_1_2}$, where 
  - the $\texttt{mainnet flag}$ is $\texttt{0}$ indicating that it's a rollup, 
  - the $\texttt{rollupIndex = 1}$ means the rollup is the second in the rollup exit tree, and 
  - the $\texttt{local root index = 3}$, pointing at the fourth leaf in the rollup 9002's exit tree.

![ulxly-mainnet-and-rollups-exit-trees-2](../../../../img/zkEVM/ulxly-mainnet-and-rollups-exit-trees-2.png)

## Exit root contracts

The class diagram below describes how the exit root contracts communicate with the bridge and the rollup manager.

![Polygon Solidity smart contract bridging architecture](../../../../img/cdk/high-level-architecture/exit-root-class-diagram.png)

An exit tree is a binary, append-only, sparse Merkle tree (SMT) whose leaf nodes store bridging data. The exit trees have a depth of 32.

The Merkle root of an exit tree is known as the exit tree root, and it is the fingerprint of all the information recorded in the exit tree's leaf nodes. 

The global exit tree root of the L1 info tree is, therefore, the source of truth for the whole network. 

## Rollup local exit trees

The L2 bridge contract manages a special Merkle tree called a local exit tree for each network that participates in bridging and claiming which is updated by the [PolygonZkEVMGlobalExitRootL2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/feature/etrog/contracts/PolygonZkEVMGlobalExitRootL2.sol) contract.

<center>

![Local exit tree for network participant](../../../../img/cdk/high-level-architecture/local-exit-tree.png)

</center>

Data from `bridgeAsset()` and `bridgeMessage()` calls on the bridge is stored in leaf nodes on the local exit trees. 

!!! important
    The following exit tree structures are managed by:

    - The [PolygonRollupManager.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonRollupManager.sol). 
    - The L1 [PolygonZkEVMBridgeV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) contract. 
    - The[PolygonZkEVMGlobalExitRootV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol).

## Exit tree for rollups

The roots of the L2 local exit trees feed into a single exit tree that manages state from all participating L2 rollups. The state lives in the L1 realm and is accessed at sequencing time.

<center>

![Exit tree for rollups](../../../../img/cdk/high-level-architecture/exit-tree-for-rollups.png)

</center>

The L2 local exit root is accessible on the rollup manager by calling the [`getRollupExitRoot()`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/b2a62e6af5738366e7494e8312184b1d6fdf287c/contracts/v2/PolygonRollupManager.sol#L1620) method.

## L1 local exit tree

Every time there is a call to `bridgeAsset()` and `bridgeMessage()` on the bridge at the L1 Ethereum level, the data is stored in a leaf node on the L1 local exit tree.

<center>

![L1 local exit tree](../../../../img/cdk/high-level-architecture/l1-ethereum-exit-tree.png)

</center>

## L1 info tree

The L1 info tree is stored in the [PolygonZkEVMGlobalExitRootV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol) contract also known as the global exit root manager.

All subtrees exit roots feed into the leaves of the L1 info tree, which contains the global exit root (GER). 

The GER is the fingerprint of the information stored in all trees, and thus represents the global state of the system.

<center>

![Exit tree for rollups](../../../../img/cdk/high-level-architecture/l1-info-tree.png)

</center>

## Exit leaves

Two constants define transaction leaf types in the bridge contract.

```solidity
// Leaf type asset
uint8 private constant _LEAF_TYPE_ASSET = 0;

// Leaf type message
uint8 private constant _LEAF_TYPE_MESSAGE = 1;
```

Data in a leaf contains a Keccak256 hash of the metadata (ABI encoded metadata if any) and the following parameters (matched by publicly available transaction data as seen in the [bridge L1 to L2](bridging.md#l1-to-l2) documentation):

```solidity
_addLeaf(
    getLeafValue(
        _LEAF_TYPE_ASSET, // or _LEAF_TYPE_MESSAGE_
        originNetwork,
        originTokenAddress,
        destinationNetwork,
        destinationAddress,
        leafAmount,
        keccak256(metadata)
    )
);
```

!!! info "Leaf parameters"
    - `int32 originNetwork`: Origin network ID, where the original asset belongs.
    - `address originTokenAddress`: If `leafType = 0`, Origin network token address (`0x0000...0000`) is reserved for ether. If `leafType = 1`, `msg.sender` of the message.
    - `uint32 destinationNetwor`k: Bridging destination network ID.
    - `address destinationAddress`: Address that receives the bridged asset in the destination network.
    - `uint256 leafAmount`: Amount of tokens/ether to bridge.
    - `bytes32 keccak256(metadata)`: Hash of the metadata. This metadata contains information about assets transferred or the message payload.

## Updating system state

The system uses a set of [exit tree roots](exit-roots.md) to manage system state. Leaves of the trees point to transaction data such as detailed above.

Adding a new leaf to the tree triggers an update to the exit tree root which then propagates to an update on the global exit tree root.

Using Merkle tree exit roots in this way, referenced by the bridge contracts and accessible to the `PolygonRollupManager` contract with getters, the bridge contract triggers data synchronization across L1 and L2, including at the sequencer and state db level.

The use of two distinct global exit root manager contracts for L1 and L2, as well as separate logic for the sequencing flow and the bridge contract, allows for extensive network interoperability. Meanwhile, all asset transfers can be validated by any L1 and L2 node due to the accessibility of state data.

The exit roots are modified in two key flows; sequencing and bridging.

### Sequencing flow

The `PolygonZkEVMGlobalExitRootV2` contract manages updates to the exit roots on sequencing. The contract calls `updateExitRoot(...)` on the `GlobalExitRootManager` during the sequencing flow to add an exit leaf to the relevant exit tree. 

![Update exit roots via sequencing flow](../../../../img/cdk/high-level-architecture/update-exit-roots-via-sequencing.png)

1. Initiate update: `PolygonZkEVMEtrog` initiates the update process by calling `updateExitRoots` on `PolygonRollupBaseEtrog`.
2. Retrieve current roots: `PolygonRollupBaseEtrog` retrieves the current local and global exit roots from `PolygonZkEVMGlobalExitRootL2` and `PolygonZkEVMGlobalExitRootV2` respectively.
3. Compute new exit root: `PolygonRollupBaseEtrog` computes the new exit root based on the retrieved local and global exit roots.
4. Update local exit root: `PolygonRollupBaseEtrog` updates the local exit root in `PolygonZkEVMGlobalExitRootL2`.
5. Update global exit root: `PolygonRollupBaseEtrog` updates the global exit root in `PolygonZkEVMGlobalExitRootV2`.
6. Verify updated exit root: `PolygonRollupBaseEtrog` calls `getRollupExitRoot` on `PolygonRollupManager` to verify the updated exit root.

!!! tip "L1 or L2 update"
    - If `msg.sender` is the bridge contract, the L1 local exit root is updated.
    - If `msg.sender` is the rollup manager, the L2 local exit root is updated.

### Bridging flow

When bridging, the global exit root is updated if the [`forceUpdateGlobalExitRoot`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L312) variable is set to `true`.

![Update exit roots via bridging flow](../../../../img/cdk/high-level-architecture/update-exit-roots-via-bridging.png)

1. The user interacts with the `PolygonZkEVMBridgeV2` contract by calling the `bridge()` function.
2. `PolygonZkEVMBridgeV2` calls `updateLocalExitRoot()` on `PolygonZkEVMGlobalExitRootL2`, which updates the local exit root.
3. If `forceUpdateGlobalExitRoot` is set to true, `PolygonZkEVMBridgeV2` calls `updateGlobalExitRoot()` on `PolygonZkEVMGlobalExitRootV2`, which updates the global exit root.