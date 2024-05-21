<!-- https://excalidraw.com/#json=JKZp9QEihifF_B7Z41Dfv,FVNhqQKi9PA1jM0kzUoCsQ" -->

## Polygon smart contract architecture

The diagram below shows the Polygon smart contract architecture and how the consensus mechanism works through sequencing and verification activity.

The stacks direct transaction data into the L2 and L1 realms via Solidity smart contract calls, which then record the system state in binary tree structures that store local and global exit roots of the system.

### Smart contracts topology

![Polygon Solidity smart contract architecture](../../../../img/cdk/high-level-architecture/smart-contracts-full-view.png)

### Rollup contracts

The main contracts for the zkEVM rollup stack are [PolygonRollupManager.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonRollupManager.sol) which is responsible for managing rollup and validium batches; the bridge contract [PolygonZkEVMBridgeV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) which is responsible for bridging and claiming activity across L1 and L2 chains; and the [PolygonZkEVMGlobalExitRootV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol) contract which manages the exit roots across multiple networks at the Ethereum L1 level.

### Valdium contracts 

The CDK validium stacks use the [cdk-validium-contracts](https://github.com/0xPolygon/cdk-validium-contracts/tree/main) which has slightly adjusted behavior to take account of validium components, such as in the [PolygonZkEVMGlobalExitRootL2.sol](https://github.com/0xPolygon/cdk-validium-contracts/blob/main/contracts/PolygonZkEVMGlobalExitRootL2.sol) contract for example. 

The CDK repo is a fork of the zkEVM main contracts repo and all contracts, therefore, extend from common interfaces.
