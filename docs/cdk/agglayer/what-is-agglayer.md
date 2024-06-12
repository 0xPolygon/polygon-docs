### What is AggLayer

The Aggregation Layer (AggLayer) is a decentralized protocol designed to unify disparate Layer 1 (L1) and Layer 2 (L2) blockchains into a cohesive network with zero-knowledge (ZK) security. Much like how TCP/IP unified the Internet, the AggLayer aims to transform the fragmented blockchain landscape by ensuring near-instant atomic cross-chain transactions and aggregating ZK proofs from interconnected chains. This protocol enhances interoperability and security beyond traditional monolithic and modular blockchain designs.

The AggLayer leverages ZK proofs to create a seamlessly integrated environment that preserves the sovereignty of each chain within the ecosystem. This framework facilitates near-instant atomic transactions, unifies liquidity across the network, enhances capital efficiency, and significantly improves the user experience. By interfacing with the AggLayer, L1s and L2s maintain their sovereignty while accessing a vast pool of consolidated liquidity, simplifying liquidity bootstrapping. DApp developers benefit from collective user access without the need for complex bridging interfaces, fostering organic growth and broadening user access within the network. Users experience a seamless UX similar to navigating the Internet, with eventual capabilities of executing cross-chain atomic transactions in under one second.

### System scope and context

Current blockchain issues include low throughput, scalability, and fragmented liquidity. The following claims reflect the status quo:

- No single chain, L1 or L2, can support the throughput needed for Internet scale.
- Scaling blockchains requires scaling access to liquidity and shared state. Adding blockspace through multiple chains fragments liquidity.

These challenges affect both modular and monolithic scalability views:
- Monolithic view: A single high-throughput chain is seen as the best way to scale.
- Modular view: Promotes a multi-chain or multi-rollup ecosystem.

Neither view scales sufficiently, failing to increase access to shared state and liquidity.

Polygon offers the AggLayer to provide safety for near-instant cross-chain transactions and address the lack of access to shared state and liquidity.

### Principles

#### Simplicity in design 

- Lower development costs.
- Reduce unexpected security vulnerabilities.
- Simplify explaining design choices to users.
- Complex functionalities should prioritize client implementations over protocol specifications.

#### Future-proofness

- Design protocol's low levels to remain unchanged for a long time.
- Select components secure against quantum adversaries or replaceable with quantum-secure alternatives.

#### Comprehensive applicability

- Enable a wide range of applications and use cases.

#### Security

- Maintain operational integrity under various security conditions, considering network latency, fault tolerance, user intents, and POL price fluctuations.

### Goals and non-goals

#### Goals

- High throughput: Scalable to enable 1M chains by 2030.
- Decentralization: Operate with a target of 100 nodes.
- Lower-than-Ethereum latency: Provide safe cross-chain interoperability with lower latency.
- Efficient storage: Ensure the AggLayer state grows slowly.
- Quarantine faults: Prevent systemic issues from faulty chains affecting the ecosystem.
- Censorship resistance: Prevent chains from being censored.
- Economic model: Participants capture value from participation, not just inflation.
- Composability: Preserve DApp interactions across chains.
- Upgradeability: Accept and aggregate proofs from different proving systems.
- Backward compatibility: Allow chains to join without a hard fork.
- Chain registration: Balanced cost for joining the AggLayer.
- Minimize load on chains: Handle less resource-intensive functions to reduce chain burden.
- No client modification: Existing chains should join without updating their software.

#### Non-goals

- Network size: No need to scale to millions of validators.
- Chain internal safety/liveness**: Prevent malicious chains from harming other chains.
- Execution: The AggLayer should remain execution-free.
- Data Availability (DA): Remain agnostic to the DA of chains.
