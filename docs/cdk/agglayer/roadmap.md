---
hide:
- toc
---


| AggLayer version       | AggLayer: Unified bridge zkEVM | AggLayer: Unified bridge CDK* | AggLayer: Go implementation | AggLayer: Rust implementation | AggLayer: Rust with pessimistic proof | AggLayer: Multi-chain |
|------------------------|--------------------------------|-------------------------------|-----------------------------|-------------------------------|---------------------------------------|-----------------------|
| Finality L1 to L2      | 12 mins (2 epochs)             |                               |                             |                               |                                       |                       |
| Finality L2 to L1      | 1 hour                         |                               |                             |                               |                                       |                       |
| Finality L2 to L2      | 1 hour                         |                               |                             |                               |                                       |                       |
| Gas fee proof onchain  | ~350K                          |                               |                             |                               |                                       |                       |
| Transaction per second | Less than 1                    |                               |                             |                               |                                       |                       |
| Prover type            | PIL + zkAssembly               |                               |                             |                               |                                       |                       |
| Initial sync time      | N/A                            | N/A                           | N/A                         | N/A                           | In design                             | In design             |
| Snapshots available    | N/A                            | N/A                           | N/A                         | N/A                           | In design                             | In design             |

!!! info 
    * Parameters are configurable.