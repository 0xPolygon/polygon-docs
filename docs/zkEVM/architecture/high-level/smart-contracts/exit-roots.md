An exit tree is a binary append-only sparse Merkle tree (SMT) whose leaf nodes store bridging data. The exit trees have a depth of 32.

Whenever a token or message is bridged, the bridge contract appends an exit leaf to the tree related to the specific network.

## Local exit trees

The bridge uses a special Merkle tree called a local exit tree for each network that participates in bridging and claiming. 

<center>
![Local exit tree for network participant](../../../../img/cdk/high-level-architecture/local-exit-tree.png)
</center>

Data from `bridgeAsset()` and `bridgeMessage()` calls on the bridge is stored in leaf nodes on the local exit trees. 

## Exit tree for rollups

The roots of the local exit trees feed into an exit tree for all participating L2 rollups.

<center>
![Exit tree for rollups](../../../../img/cdk/high-level-architecture/exit-tree-for-rollups.png)
</center>

The L2 local exit root is accessible on the rollup manager by calling the `getRollupExitRoot()` method.

## L1 local exit tree

Data from `bridgeAsset()` and `bridgeMessage()` calls on the bridge at the L1 Ethereum level is stored in leaf nodes on the L1 local exit tree.

<center>
![Exit tree for rollups](../../../../img/cdk/high-level-architecture/l1-ethereum-exit-tree.png)
</center>

## L1 info tree

All subtrees feed into the L1 info tree, which contains the global exit root (GER). 

The GER is the fingerprint of the information stored in all trees, and thus represents the true state of the system.

<center>
![Exit tree for rollups](../../../../img/cdk/high-level-architecture/l1-info-tree.png)
</center>

!!! tip
    - Read more about exit trees in our [exit tree documentation](../../protocol/zkevm-bridge/exit-tree.md).
    