## Introduction

Polygon CDK running in validium mode inherits the core functionalities of zkEVM rollup mode and adds a [data availability layer](dac.md).

!!! danger
    How can we say that validium inherits from zkEVM rollup when zkEVM rollup is unavailable? Do we mean non-CDK zkEVM rollup? We need to say so.

## Key differences

|        | zkEVM                                                       | Validium                                                                           |
| ------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Node type**            | [zkEVM node](https://github.com/0xPolygonHermez/zkevm-node) | [Validium node](https://github.com/0xPolygon/cdk-validium-node): zkEVM node with validium extensions                  |
| **Data availability**    | On-chain                                                    | Off-chain via DACs + [DA node](https://github.com/0xPolygon/cdk-data-availability) |
| **Components**           | zkEVM components\*\*                                        | zkEVM components\*\* + PostgreSQL database + on-chain committees                   |
| **Contracts** | [zkEVM smart contracts](https://github.com/0xPolygonHermez/zkevm-contracts)  <ul><li>`PolygonZkEVM` (main rollup contract)</li> <li> `PolygonZkEVMBridge`</li> <li>`PolygonZkEVMGlobalExitRoot`</li></ul>  | [Validium-specific DAC contract](https://github.com/0xPolygon/cdk-validium-contracts) <ul><li>`CDKDataCommittee.sol`</li><li> `CDKValidium.sol` </li></ul> |
| **Infrastructure** | Standard infrastructure                                     | Dedicated infrastructure for data availability layer and DACs                      |
| **Tx flow** | All transaction data is published on L1 | Validium only publishes the hash of the transaction data. This `Accumulated Input Hash` must be approved by a majority of DAC members. <br/><br/>The sequencer sends both the hash and the transaction data to the DAC for verification. Once approved, the hash plus signatures, is sent to the Consensus L1 contract of the validium protocol. <br/><br/> After verification, the hash and the zk-proof are added to the L1 state.

<sub><sup>**</sup>JSON RPC, Pool DB, Sequencer, Etherman, Synchronizer, State DB, Aggregator, Prover</sub>