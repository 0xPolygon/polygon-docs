Polygon 2.0 envisions a network of ZK-powered L2s on Ethereum that unify liquidity across the ecosystem and can scale on demand. Here is how that vision comes into focus.

### Unified liquidity

In an interoperable Polygon ecosystem, access to cross-chain liquidity will be a solved problem. This is due to the in-development interop layer, which is what distinguishes the Polygon ecosystem from other multi-chain scaling architectures. 

The interop layer will be a service that aggregates proofs and coordinates cross-chain transactions between L2 chains built using Polygon technology, enabling unified liquidity. The interop layer expands on the design of the LxLy protocol, currently used by Polygon zkEVM. The core characteristics of the interop layer are:

- Proof aggregation: The aggregator accepts ZK proofs and Message Queues' representations (like Merkle roots) from chains, aggregates these ZK proofs into a single ZK proof, and submits the proof to Ethereum.
- Atomic cross-chain execution: Bundles of transactions are submitted to many chains in the Polygon network, with the guarantee that all transactions will be successfully executed, or none will be included.

With readily-available liquidity, developers can focus on use-case, rather than bootstrapping users. By abstracting the complexity of cross-chain communication, from the perspective of the end-user, the entire Polygon network will feel like using a single chain.

### Unlimited scale

Polygon CDK is an open source toolkit that allows developers to design and launch ZK-powered chains on demand–or migrate existing EVM-based L1 chains into L2s–backed by the security of Ethereum. In practice, it means unlimited scale in an environment unified through the interop layer.

Existing approaches to an ecosystem of L2s often provide new blockspace at the expense of a chain’s sovereignty. In contrast, Polygon CDK helps developers preserve a chain’s self-determination. The tools available in Polygon CDK are modular: Chains may use any parts of the stack they need, and none that they don’t. Configs will include, but are not limited to, customizable gas tokens, rollup and validium modes, support for different data availability solutions, and more.  

Even as the Polygon ecosystem feels like a single chain, each specific chain will be distinctive, with Polygon PoS, Polygon zkEVM, each Polygon CDK chain, and, eventually, Polygon Miden, providing differentiated feature-sets that will suit some projects more than others.
