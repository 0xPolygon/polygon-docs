!!! info "Disclaimer"
    - Some of the content in this section discusses technology in development and not ready for release.
    - Please check against the main documentation site for any live releases.
    - Feel free to experiment with any code in public repos.

## Welcome to AggLayer documentation

The AggLayer is an in-development interoperability protocol that allows for trustless, cross-chain token transfers and message-passing, as well as more complex operations. The safety of the AggLayer is provided by zero-knowledge proofs. 

The AggLayer currently connects chains built with Polygon CDK, a developer toolkit for designing ZK-powered Layer 2s. The long term goal for the protocol is to be flexible enough to provide interoperability among a growing range of blockchain architectures, including L2s, appchains, and non-EVM chains. 
 
## AggLayer components

### Polygon CDK

The AggLayer connects chains built with Polygon CDK, which use ZK proofs to generate state transitions that are cryptographically secure. 

### Unified bridge

The unified bridge is a single bridge contract for all AggLayer-connected chains, allowing for the cross-chain transfer of fungible (non-wrapped) tokens. In the abstract, it is the source of unified liquidity for the AggLayer. 

!!! tip "More information"
    See the [unified bridge documentation](unified-bridge.md) for details. 

### AggLayer service

The AggLayer service is a service designed to receive zero-knowledge proofs from various CDK chains and verify their validity before sending them to the L1 for final settlement. Currently, the AggLayer service has two implementations: [agglayer-go](agglayer-go.md) and [agglayer-rs](agglayer-rs.md).