!!! info "Disclaimer"
    - Some of the content in this section discusses technology in development and not ready for release.
    - Please check against the main documentation site for any live releases.
    - Feel free to experiment with any code in public repos.

The AggLayer is an in-development interoperability protocol that allows for trustless, cross-chain token transfers and message-passing, as well as more complex operations. The safety of the AggLayer is provided by ZK proofs. 

The AggLayer currently connects chains built with Polygon CDK, a developer toolkit for designing ZK-powered Layer 2s. The long term goal for the protocol is to be flexible enough to provide interoperability among a growing range of blockchain architectures, including L2s, appchains, and non-EVM chains.

## Chains connected to AggLayer

Here's a list of chains connected to the alpha version of the AggLayer:


| Implementation Provider | Chain Name | L2 Chain ID |Network Name           |
| ------------------ | ------------- | ----------- | ----------------------- |
| Startale Labs      | Astar         | 6038361     | zKyoto                  |
| Startale Labs      | Astar         | 3776        | Astar zkEVM             |
| Gateway FM         | GPT Protocol  | 1511670449  | gpt-mainnet             |
| Gateway FM         | Haust         | 1570754601  | haust-testnet           |
| Gateway FM         | Haust         | 938        | haust-network           |
| Gateway FM         | Lumia         | 1952959480  | Lumia Testnet           |
| Gateway FM         | Lumia         | 994873017   | prism                   |
| Gateway FM         | Moonveil      | 1297206718  | moonveil-testnet        |
| OKX                | OKX           | 196         | X Layer                 |
| Gateway FM         | Silicon       | 1722641160  | silicon-sepolia-testnet |
| Gateway FM         | Silicon       | 2355        | silicon-zk              |
| Gateway FM         | WilderWorld   | 1668201165  | zchain-testnet          |  
| Gateway FM         | Wirex         | 31415       | pay-chain               |

## AggLayer components

### Polygon CDK

The AggLayer connects chains built with Polygon CDK, which use ZK proofs to generate state transitions that are cryptographically secure. 

### Unified bridge

The unified bridge is a single bridge contract for all AggLayer-connected chains, allowing for the cross-chain transfer of fungible (non-wrapped) tokens. It is the source of unified liquidity for the AggLayer. 

!!! tip "More information"
    See the [unified bridge documentation](unified-bridge.md) for details. 

### AggLayer service

The AggLayer service is designed to receive ZK proofs from various CDK and non-CDK chains, and verify their validity before sending them to the L1 Ethereum for final settlement. Currently, the AggLayer service has two implementations: [agglayer-go](agglayer-go.md) and [agglayer-rs](agglayer-rs.md).
