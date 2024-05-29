The unified bridge transfers assets and messages between L1 and L2 networks by calling bridge and claim functions on the unified bridge smart contract. 

![Polygon zkEVM bridge schema](../../../../img/zkEVM/01pzb-polygon-zkevm-schema.png)

## Smart contract definition

The smart contract that manages bridging and claiming across networks is the [PolygonZkEVMBridgeV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) contract. It is deployed on both L1 and L2 networks.

### Bridge and claim assets

Bridging and claiming assets is managed by the `bridgeAsset` and the `claimAsset` functions.

These functions allow data payloads to be sent across networks.

#### `bridgeAsset`

To send an asset from L1 to L2, the sender first transfers the token from the user into the bridge by locking the asset on the origin network (L1). 

```solidity
IERC20Upgradeable(token).safeTransferFrom(
    msg.sender,
    address(this),
    amount
);
```

From L2 to L1, the wrapped token is burnt on the L2 network:

```solidity
TokenWrapped(token).burn(msg.sender, amount);
``` 

#### `claimAsset`

From L1 to L2, the bridge smart contract mints an equivalent asset, called a wrapped token, on the destination network (L2). 

```solidity
bytes32 tokenInfoHash = keccak256(
    abi.encodePacked(originNetwork, originTokenAddress)
);
```

Once minted, the recipient can claim the token on the destination network (L2).

In reverse, the bridge smart contract unlocks the original asset on the origin network (L1).

## Updating system state

The Polygon bridge smart contract uses exit trees to manage state.

On a successful transfer, the bridge contract adds an exit leaf to the relevant exit tree. 

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

This triggers an update to the exit tree root which then propagates to an update on the global exit tree root.

Using these Merkle tree exit roots, referenced by the bridge contract and accessible to the `PolygonRollupManager` contract with getters, the bridge contract synchronizes data across L1 and L2, the sequencer component, and the state db.

The use of two distinct global exit root manager contracts for L1 and L2, as well as separate logic for the bridge contract and each of these global exit root managers, allows for extensive network interoperability.

Meanwhile, all asset transfers can be validated by any L1 and L2 node due to the accessibility of state data.

## Transaction flows

### L1 to L2

1. If a call to the `bridgeAsset` or `bridgeMessage` passes validation, the bridge contract appends an exit leaf to the L1 exit tree and computes the new L1 exit tree root.

2. The global exit root manager appends the new L1 exit tree root to the global exit tree and computes the global exit root.

3. The sequencer fetches the latest global exit root from the global exit root manager.

4. At the start of the transaction batch, the sequencer stores the global exit root in special storage slots of the L2 global exit root manager smart contract, allowing L2 users to access it.

5. A call to `claimAsset` or `claimMessage` provides a Merkle proof that validates the correct exit leaf in the global exit root.

6. The bridge contract validates the caller's Merkle proof against the global exit root. If the proof is valid, the bridging process succeeds; otherwise, the transaction fails.

### L2 to L1

1. If a `bridgeAsset` or `bridgeMessage` call on the L2 bridge contract validates, the bridge contract appends an exit leaf to the L2 exit tree and computes the new L2 exit tree root.

2. The L2 global exit root manager appends the new L2 exit tree toot to the global exit tree and computes the global exit root. At that point, the caller's bridge transaction is included in one of batches selected and sequenced by the sequencer.

3. The aggregator generates a zk-proof attesting to the computational integrity in the execution of sequenced batches which include the transaction.

4. For verification purposes, the aggregator sends the zk-proof together with all relevant batch information that led to the new L2 exit tree root (computed in step 2), to the consensus contract.

5. The consensus contract utilizes the `verifyBatches` function to verify validity of the received zk-proof. If valid, the contract sends the new L2 exit tree root to the global exit root manager in order to update the global exit tree.

6. `claimMessage` or `claimAsset` is then called on the bridge contract with Merkle proofs for correct validation of exit leaves.

7. The bridge contract retrieves the global exit root from the L1 global exit root manager and verifies validity of the Merkle proof. If the Merkle proof is valid, the bridge completes. Otherwise, the transaction is reverted.

### L2 to L2

1. When a batch of transactions is processed, the bridge contracts appends the L2 exit tree with a new leaf containing the batch information. This updates the L2 exit tree root.

2. The bridge contracts communicates the L2 exit tree root to the L2 global exit root manager. The L2 global exit root manager, however, does not update the global exit tree at this stage.

3. For proving and verification, the zk-proof-generating circuit obtains the L2 exit tree root from the L2 global exit root manager.

4. Only after the batch has been successfully proved and verified does the L2 global exit root manager append the L2 exit tree root to the global exit tree. As a result, the global exit root is updated.

The zk-proof-generating circuit also writes the L2 exit tree root to the mainnet. The L1 bridge contract can then finalize the transfer by using the `claim` function.