## Introduction

Polygon CDK running in validium mode inherits the core functionalities of zkEVM rollup mode and adds a [data availability layer](dac.md).

## Key differences

|        | zkEVM                                                       | Validium                                                                           |
| ------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Node type**            | [zkEVM node](https://github.com/0xPolygonHermez/zkevm-node) | [Validium node](https://github.com/0xPolygon/cdk-validium-node): zkEVM node with validium extensions                  |
| **Data availability**    | On-chain                                                    | Off-chain via DACs + [DA node](https://github.com/0xPolygon/cdk-data-availability) |
| **Components**           | zkEVM components\*\*                                        | zkEVM components\*\* + PostgreSQL database + on-chain committees                   |
| **Contracts** | [zkEVM smart contracts](https://github.com/0xPolygonHermez/zkevm-contracts)  <ul><li>`PolygonZkEVM` (main rollup contract)</li> <li> `PolygonZkEVMBridge`</li> <li>`PolygonZkEVMGlobalExitRoot`</li></ul>  | [Validium-specific DAC contract](https://github.com/0xPolygon/cdk-validium-contracts) <ul><li>`CDKDataCommittee.sol`</li><li> `CDKValidium.sol` </li></ul> |
| **Infrastructure** | Standard infrastructure                                     | Dedicated infrastructure for data availability layer and DACs                      |

<sub><sup>**</sup>JSON RPC, Pool DB, Sequencer, Etherman, Synchronizer, State DB, Aggregator, Prover</sub>