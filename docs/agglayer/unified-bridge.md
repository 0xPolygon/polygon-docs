The unified bridge is a single bridge contract on Ethereum, providing a safe, common access point for the transfer of all native, never-wrapped tokens. Each chain has a local copy of the unified bridge root, enabling cross-chain interoperability that doesn’t require the security risks of third-party bridges.

!!! important "AggLayer smart contracts"
    - The current version of the unified bridge uses the contracts in the [PolygonzkEVM smart contract repo](https://github.com/0xPolygonHermez/zkevm-contracts).

## Bridging mechanism

The bridging mechanism enables token transfers and message-passing between Ethereum (L1) and CDK chains via smart contracts. Detailed in the [zkEVM bridging documentation](../zkEVM/architecture/unified-LxLy/bridging.md), core components include the bridge and exit root Solidity smart contracts.

## Data structures 

Each chain holds a single data structure which stores a record of all token withdrawals and messages that originated from that chain. This “exit tree” is an append-only Merkle trie, similar in structure to the Ethereum deposit trie. The latest state of each chain and the unified bridge is represented by the root of this Merkle tree, referred to as the “exit root.”

As cryptographic commitments, exit roots ensure the integrity of the network as a whole.  Refer to the [exit root documentation](../zkEVM/architecture/high-level/smart-contracts/exit-roots.md) for greater detail about the role of exit roots in the system.
