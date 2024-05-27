Bridge functionality allows token and message passing between L1 and L2. 

The smart contract that manages bridging across L1 and L2 is the [PolygonZkEVMBridgeV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) contract.

Using the exit roots of the Merkle tree, referenced by the bridge contract and accessible to the `PolygonRollupManager` contract, the bridge contract synchronizes data across the L1 and L2 chains, the sequencer component, and the state db.

!!! tip
    - Read more about the bridge in our [bridging documentation](../../protocol/zkevm-bridge/index.md)
    