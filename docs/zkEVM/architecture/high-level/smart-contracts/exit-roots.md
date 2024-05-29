An exit tree is a binary append-only sparse Merkle tree (SMT) whose leaf nodes store bridging data. The exit trees have a depth of 32.

Whenever a token or message is bridged, the bridge contract appends an exit leaf to the tree related to the specific network.

## Local exit trees

The L2 bridge has a special Merkle tree called a local exit tree for each network that participates in bridging and claiming. 

<center>
![Local exit tree for network participant](../../../../img/cdk/high-level-architecture/local-exit-tree.png)
</center>

Data from `bridgeAsset()` and `bridgeMessage()` calls on the bridge is stored in leaf nodes on the local exit trees. 

## Exit tree for rollups

The roots of the local exit trees feed into a single exit tree that manages state from all participating L2 rollups.

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

## Exit leaves

Two constants define leaf types in the bridge contract.

```solidity
// Leaf type asset
uint8 private constant _LEAF_TYPE_ASSET = 0;

// Leaf type message
uint8 private constant _LEAF_TYPE_MESSAGE = 1;
```

An exit leaf, in particular, is a Keccak256 hash of the ABI encoded packed structure with the following parameters:

- uint8 leafType: [0] asset, [1] message.
- int32 originNetwork: Origin network ID, where the original asset belongs.
- address originAddress: If `leafType = 0`, Origin network token address (`0x0000...0000`) is reserved for ether. If `leafType = 1`, `msg.sender` of the message.
- uint32 destinationNetwork: Bridging destination network ID.
- address destinationAddress: Address that receives the bridged asset in the destination network.
- uint256 amount: Amount of tokens/ether to bridge.
- bytes32 metadataHash: Hash of the metadata. This metadata contains information about asset transferred or the message payload.

When a user commits to transferring assets from one network to another, the bridge contract adds an exit leaf to that network's exit tree.

The Merkle root of an exit tree is known as the exit tree root, and it is the fingerprint of all the information recorded in the exit tree's leaf nodes.

As a result, given any network exit tree, whether L1 or L2, its exit tree root is the source of state truth for that network.

## Global exit tree

Consider a scenario of bridging assets between the L1 Mainnet and L2 network. The global exit tree is a binary Merkle tree whose leaf nodes are the L1 exit tree's Merkle root and the L2 exit tree's Merkle root. A global exit tree is depicted in the figure below.

![The L1-L2 global exit tree](../../../../img/zkEVM/02pzb-global-exit-tree.png)

The Merkle root of the global exit tree is called the global exit root.

Whenever a new exit leaf is added to an exit tree, a new root for that exit tree is calculated. Consequently, the global exit tree is updated with this new root. As a result, the global exit root always reflects the current state of both networks.

Since the Merkle root of each exit tree represents the true state of its respective network, the most recent global exit root consequently represents the true state of all networks, that is, both the L1 and L2 networks.

Once the global exit root is synchronized between the L1 and L2 networks, users can use a Merkle proof to verify the inclusion of the correct exit leaf, allowing them to claim their transferred assets.

This is how a complete asset transfer or cross-chain messaging is achieved: it starts with the bridge function in the origin network and concludes with the claim function in the destination network, with exit tree roots conveying the true state at both ends.

## Asset transfer scenarios

In this subsection, we present two scenarios to illustrate the role of exit trees and the global exit tree in the asset transfer process.

### Transfer from L1 to rollup L2

Consider a scenario where a user wants to transfer assets from the L1 Mainnet to the L2 Rollup.

Once the user commits to a transfer, a new exit leaf with the information of the assets being bridged is appended to the L1 exit tree. The transfer data typically looks like this:

```
Origin network: 0 (L1)
Origin address: 0x56566... 
Dest Network: 1 (L2)
Dest Address: 0x12345...
Amount: 145
Metadata: 0x0...
```

With the newly added exit leaf, the L1 exit tree now has a new root. Updating the global exit tree with this new L1 exit tree root means changing the root of the global exit tree.

To claim the bridged assets on the destination L2 network, the global exit root is verified using a Merkle proof. This proof allows one to confirm whether an exit leaf, containing information about assets being bridged to L2, is represented in the global exit tree by the corresponding L1 exit tree root.

![Updating L1 exit tree and the global exit root](../../../../img/zkEVM/03pzb-exit-leaf-add-L1-L2.png)

### Transfer from rollup L2 to L1

Transfers can also occur from an L2 Rollup to the L1 mainnet. In this scenario, the same procedure outlined in the previous example is followed, but in the reverse direction.

That is, once a user commits to a transfer, an exit leaf is added to the L2 exit tree with corresponding transfer information. The transfer data in this case looks as follows:

```
Origin network: 3 (L2)
Origin address: 0x34655... 
Dest Network: 0 (L1)
Dest Address: 0x27564...
Amount: 92
Metadata: 0x116...
```

The newly added L2 exit leaf means the L2 exit tree has a new root. The new L2 exit tree Root is then appended to the global exit tree, and thus the root of the global exit tree is updated.



## Global Exit Root manager contract

The Global Exit Root Manager SC (PolygonZkEVMGlobalExitRoot.sol) manages the Global Exit Tree Root. It is in charge of updating the Global Exit Tree Root and acts as a repository for the Global Exit Tree's history.

The logic of the zkEVM Bridge SC has been separated from that of the Global Exit Root Manager SC in order to achieve improved interoperability.

This means that the zkEVM Bridge SC, in conjunction with the Global Exit Root Manager SC, can be installed in any network to achieve the same results.

!!!info
    There are two Global Exit Root manager SCs: one deployed in L1, while the other is deployed in L2.

    Their Solidity code files are; [PolygonZkEVMGlobalExitRoot.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMGlobalExitRoot.sol), and [PolygonZkEVMGlobalExitRootL2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMGlobalExitRootL2.sol), respectively.

But the L2 Global Exit Root Manager SC is different, and it appears in code as `PolygonZkEVMGlobalExitRootL2.sol`. This is a special contract that allows synchronization of L2 Exit Tree Root and the Global Exit Root.