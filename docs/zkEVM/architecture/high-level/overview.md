<!-- https://excalidraw.com/#json=JKZp9QEihifF_B7Z41Dfv,FVNhqQKi9PA1jM0kzUoCsQ" -->

This section of the docs provides a detailed analysis of the full topology of the Polygon zero-knowledge system architecture. 

Tailored for CDK stacks and using zkEVM technology, these documents explore the contents, layout, and interactions among component systems and functions. They offer in-depth descriptions of the components that constitute the larger system, with references to relevant code bases.

The diagram below is a full and detailed topological overview of the entire Polygon zero-knowledge system architecture.

## Architectural topology

![Polygon systems topology](../../../img/cdk/high-level-architecture/full-topology.png)

## Components 

- Smart contracts: L1 and L2 Solidity smart contracts used for interacting with the whole stack.
- Exit root trees: Append-only sparse Merkle trees which record the current and historical state of the network. 
- CDK and zkEVM nodes containing:
    - JSON RPC client: Exposes the read/write interfaces for interacting with a node/chain.
    - Pool database: Records transactions coming in from the JSON RPC client.
    - State database: Permanently stores state data.
    - Sequencer: A node responsible for fetching transactions from the pool database, executes and puts them into batches. See the discussion on [sequencers](../../architecture/index.md#sequencer) for more information.
    - Aggregator: A node tasked with aggregating batches and using the prover to produce proofs of computational integrity. See the discussion on [aggregators](../../architecture/index.md#aggregator) for more information.
    - Synchronizer: Updates the state database by fetching data from Ethereum through the Etherman.
    - Etherman: Implements methods for interacting with the L1 network and smart contracts.
- Bridge service: Provides an API to perform bridge claims, i.e. asset and message transfers between L1/L2 and L2/L2.
- Prover: System for generating proofs attesting to computational integrity.

## What to expect

When complete, this section will include information on: 

- The structure of a CDK node and how it interacts with L2 and L1 smart contracts.
- The structure of a zkEVM node and how it interacts with L2 and L1 smart contracts.
- The key components included in the nodes, how they function, and their interactions with other components, external dApps, and the L1/L2 environment.
- Key similarities and differences between a CDK and zkEVM node.
- CDK validium components, including the DAC and DAC sequencer.
- Detailed description of the Polygon smart contract sets for L1 and L2.
- The zkProver and how it interacts with a zkEVM node aggregator.

### Currently out of scope

- The in-development bridge service.
- AggLayer.
