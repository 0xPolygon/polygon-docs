---
comments: true
---

Polygon zkEVM deploys smart contracts to manage transaction processing and related data transfers between itself and other networks, such as the Ethereum L1 or other L2s connected to the AggLayer. 

There are four key contract types built into the system design: 

- [Consensus contracts](#consensus). 
- [Rollup manager](#rollup-manager). 
- [Bridge contract](#bridge). 
- [Exit root management](#global-exit-roots).

### Consensus

Consensus contracts live in the L1 and expose specific functions for controlling the sequencing and verification mechanisms triggered by the sequencer and aggregator.

Polygon zkEVM can be implemented as,

- Either a zk-rollup, deploying the [`PolygonZkEVMEtrog.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/a5eacc6e51d7456c12efcabdfc1c37457f2219b2/contracts/v2/consensus/zkEVM/PolygonZkEVMEtrog.sol) consensus contract, where all transaction data is posted to Ethereum. 

- Or, a validium using a data-availability committee (DAC) for managing availability of transaction data, and deploying the [`PolygonValidiumEtrog.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/a5eacc6e51d7456c12efcabdfc1c37457f2219b2/contracts/v2/consensus/validium/PolygonValidiumEtrog.sol) consensus contract. 

These contracts therefore define the type of a CDK chain, either a validium or zk-rollup.

### Rollup manager

The [PolygonRollupManager.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonRollupManager.sol) contract is useful for managing CDK chains. 
It is responsible for creating, updating, and verifying CDK rollup and validium chains.

### Bridge 

The unified bridge contract [PolygonZkEVMBridgeV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) is responsible for bridging and claiming assets or messages across L1 and L2 chains.

### Global exit roots

Each bridging of an asset or a message from the zkEVM is recorded on a leaf of the zkEVM's _local exit tree_.

Every update of the local exit tree at the leaf-level triggers an update of the local exit root, which in turn is appended to a leaf of the global exit tree.

Similarly, each bridging of an asset or a message from the L1 to the zkEVM is recorded on a leaf of the _L1 Info tree_.

The [PolygonZkEVMGlobalExitRootV2.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol) contract manages the exit roots across multiple networks at the Ethereum L1 level.

The [PolygonZkEVMGlobalExitRootL2.sol](https://github.com/0xPolygon/cdk-validium-contracts/blob/main/contracts/PolygonZkEVMGlobalExitRootL2.sol) contract manages the zkEVM state by keeping track of the current local exit root.

### Validium stacks

CDK validium stacks use the [cdk-validium-contracts](https://github.com/0xPolygon/cdk-validium-contracts/tree/main) which has slightly adjusted behavior to take account of data-availability components and custom CDK requirements. 

The CDK repo is a fork of the zkEVM main contracts repo and all contracts, therefore, extend from common interfaces.

!!! important
    - A CDK validium stack starts off as a rollup stack. 
    - It may interchangeably be referred to as such when discussing aspects shared by the two options.
