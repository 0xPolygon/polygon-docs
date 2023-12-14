Polygon CDK running in validium mode inherits the core functionalities of a zkEVM rollup node and adds a [data availability layer](../concepts/dac.md).

## Key differences

|        | Rollup                                                    | Validium                                                                           |
| ------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Node type**            | [zkEVM node](https://github.com/0xPolygonHermez/zkevm-node) | [Validium node](https://github.com/0xPolygon/cdk-validium-node): zkEVM node with validium extensions                  |
| **Data availability**    | On-chain via L1                                            | Off-chain via a local option, or a [DAC](../concepts/dac.md) + [DA node](https://github.com/0xPolygon/cdk-data-availability) |
| **Components**           | zkEVM components\*                                        | zkEVM components\* + PostgreSQL database + on-chain committees                   |
| **Contracts** | [zkEVM smart contracts](https://github.com/0xPolygonHermez/zkevm-contracts)  <ul><li>`PolygonZkEVM` (main rollup contract)</li> <li> `PolygonZkEVMBridge`</li> <li>`PolygonZkEVMGlobalExitRoot`</li></ul>  | [Validium-specific DAC contract](https://github.com/0xPolygon/cdk-validium-contracts) <ul><li>`CDKDataCommittee.sol`</li><li> `CDKValidium.sol` </li></ul> |
| **Infrastructure** | Standard infrastructure                                     | Dedicated infrastructure for data availability layer and DACs                      |
| **Tx flow** | All transaction data is published on L1 | Validium only publishes the hash of the transaction data to L1. The sequencer sends both the hash and the transaction data to the DAC for verification. Once approved, the hash+signatures are sent to the Consensus L1 contract of the validium protocol.
| **Security** | High security due to on-chain data availability and zero-knowledge proofs. |Off-chain data availability can affect security if the sequencer goes offline or if DAC members collude to withhold state data. |
| **Gas fees** | High, because all transaction data is stored on Ethereum. | Low, because only the hash of the transaction data is stored on Ethereum. |
| **Proof generation** | Uses Prover to generate proofs of batched transactions for validation. | Uses Prover to generate proofs of batched transactions for validation. |
| **Final settlement** | Transaction batches and their corresponding proofs are added to the Ethereum state. | The hash of transaction data and its proof are added to the Ethereum state, referred to as the consolidated state. |

<sub><sup>*</sup>JSON RPC, Pool DB, Sequencer, Etherman, Synchronizer, State DB, Aggregator, Prover</sub>
