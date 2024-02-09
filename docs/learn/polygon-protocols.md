## Polygon PoS 

Polygon PoS is a widely-adopted EVM-compatible sidechain designed for low transaction costs and fast transaction times.

### Where Polygon PoS is heading

Here is how the proposed development, with consensus of the Polygon community, will be achieved:

- Changes to network architecture. Becoming a zero-knowledge validium instead of a zk-rollup.
- Changes to network token.
- Introduction of a Staking Layer, which will eventually serve all L2 chains in the Polygon network.

Polygon 2.0: A pre-PIP discussion for upgrading Polygon PoS to a zkEVM validium is underway. This community discussion is guiding the technical specification of the potential upgrade. If this PIP is accepted, Polygon PoS will eventually plug into the interop layer that will connect the entire Polygon network. 

Phase 0: PIP-18 has suggested a phased approach to implementation of Polygon 2.0. As it relates to Polygon PoS, Phase 0 includes:

- The initiation of the POL upgrade
- The upgrade from MATIC to POL as the native (gas) token for PoS
- The adoption of POL as the staking token for Polygon PoS
- The launch of the Staking Layer and migration of Polygon public chains to consequently leverage it.

## Polygon zkEVM

Polygon zkEVM is a Type-3, EVM-equivalent ZK rollup, which maximizes network security by posting both ZK proofs and transaction data to Ethereum.

### Where Polygon zkEVM is heading

Type 2: The primary goal for Polygon zkEVM is to become a full Type-2 ZK-EVM, supporting all nine precompiled smart contracts and all the opcodes. 

Security: The two near-term priorities for Polygon zkEVM are:
- Adding support for a forced-transaction mechanism that will make the network censorship-resistant.
- Lengthening the 10-day timelock for network upgrades.

EVM-equivalence: As EIPs change and shape Ethereum’s execution logic, Polygon zkEVM will evolve to maintain EVM-equivalence. The two most important forthcoming changes are:
- EIP-4844: Expected in the Cancun hard fork, proto-Danksharding creates a low-cost alternative to CALLDATA, expected to greatly reduce transaction fees on rollups.
- EIP-7212: A new precompiled contract will support signature verifications in the secp256r1 elliptic curve.

Polygon 2.0: Polygon zkEVM will continue to offer the strongest open source software security guarantees by making transaction data available (DA) on Ethereum. Eventually, Polygon zkEVM will plug into the unified interop layer that will help connect the entire Polygon ecosystem.

## Polygon CDK

Polygon CDK is a collection of open source software components for launching ZK-powered L2 chains on Ethereum. Currently, it supports two primary configurations, rollup mode and validium mode, with an additional customizable data availability committee (DAC) for validium chains. 

### Where Polygon CDK is heading

Upcoming release: The next release of Polygon CDK, expected in Q1 2024, will support a wider set of features and configurations. These include:

- The unified LxLy bridge: As the first phase of the interop layer, projects building with CDK will have the option to plug into the unified LxLy bridge that will, eventually, help connect the entire Polygon ecosystem.
- Custom native (gas) tokens.
- Custom allow-lists for smart contracts and transactions.
- Support for modular, third-party data availability solutions.

## Polygon Miden

Polygon Miden is an in-development, novel ZK rollup designed as a zkVM. Powered by the Miden VM, Polygon Miden extends Ethereum’s feature set, providing throughput and privacy features that are beyond the capabilities of the EVM. 

### Where Polygon Miden is heading

A testnet for Polygon Miden is expected to launch in Q1 2024, with mainnet following later in the year. 

Polygon 2.0: Once Polygon Miden is on mainnet, it will plug into the interop layer that will help connect the entire Polygon ecosystem.
