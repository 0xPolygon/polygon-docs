An exit tree is a binary, append-only, sparse Merkle tree (SMT) whose leaf nodes store bridging data. The exit trees have a depth of 32.

The Merkle root of an exit tree is known as the exit tree root, and it is the fingerprint of all the information recorded in the exit tree's leaf nodes. 

The global exit tree root of the L1 info tree is, therefore, the source of truth for the whole network. 

## Updating system state

The system uses a set of [exit tree roots](exit-roots.md) to manage system state. Leaves of the trees point to transaction data such as detailed above.

The `PolygonRollupManager.sol` contract calls `updateExitRoot(...)` on the `GlobalExitRootManager` during the sequencing flow to add an exit leaf to the relevant exit tree. 

When bridging, the global exit root is updated if the [`forceUpdateGlobalExitRoot`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L312) variable is set to `true`.

- If `msg.sender` is the bridge contract, the L1 local exit root is updated.
- If `msg.sender` is the rollup manager, the L2 local exit root is updated.

Adding a new leaf to the tree triggers an update to the exit tree root which then propagates to an update on the global exit tree root.

Using Merkle tree exit roots in this way, referenced by the bridge contracts and accessible to the `PolygonRollupManager` contract with getters, the bridge contract triggers data synchronization across L1 and L2, including at the sequencer and state db level.

The use of two distinct global exit root manager contracts for L1 and L2, as well as separate logic for the bridge contract and each of these global exit root managers, allows for extensive network interoperability.

Meanwhile, all asset transfers can be validated by any L1 and L2 node due to the accessibility of state data.

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

The roots of the L2 local exit trees feed into a single exit tree that manages state from all participating L2 rollups.

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

The GER is the fingerprint of the information stored in all trees, and thus represents the true state of the system.

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
