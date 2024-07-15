---
comments: true
---

## Polygon PoS 

Polygon PoS is a widely-adopted EVM-compatible sidechain designed for low transaction costs and fast transaction times.

### Where Polygon PoS is heading

Here is how the proposed development, with consensus of the Polygon community, will be achieved:

- Changes to network architecture. Becoming a zero-knowledge validium instead of a zk-rollup.
- Changes to network token.
- Introduction of a Staking Layer, which will eventually serve all L2 chains in the Polygon network.

[PIP-18](https://forum.polygon.technology/t/pip-18-polygon-2-0-phase-0-frontier/12913) has suggested a phased approach for upgrading Polygon PoS to a zkEVM validium. This community discussion is guiding the technical specification of the potential upgrade. If this PIP is accepted, Polygon PoS will eventually plug into the Agglayer that will connect the entire Polygon network.

!!! info "What's Agglayer?"
    AggLayer is the interoperability layer that EVM-compatible chains connect to, enabling features such as seamless and efficient cross-chain communication, unified liquidity, and more. Read more on the AggLayer in the [Polygon blog](https://polygon.technology/blog/wtf-is-polygon?utm_source=twitter&utm_medium=social&utm_content=wtf-is-polygon).

Phase 0 of PIP-18 includes:

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

- [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Expected in the Cancun hard fork, proto-Danksharding creates a low-cost alternative to CALLDATA, expected to greatly reduce transaction fees on rollups.
- [EIP-7212](https://eips.ethereum.org/EIPS/eip-7212): A new precompiled contract will support signature verifications in the secp256r1 elliptic curve.

Polygon zkEVM will continue to offer the strongest open source software security guarantees by making transaction data available (DA) on Ethereum. Eventually, Polygon zkEVM will plug into the Agglayer that will help connect the entire Polygon ecosystem.

## Polygon CDK

Polygon CDK is a collection of open source software components for launching ZK-powered L2 chains on Ethereum. Currently, it supports two primary configurations, rollup mode and validium mode, with an additional customizable data availability committee (DAC) for validium chains. 

### Where Polygon CDK is heading

The next release of Polygon CDK, expected in Q1 2024, will support a wider set of features and configurations. These include:

- The unified LxLy bridge: As the first phase of the Agglayer development, projects building with CDK will have the option to plug into the unified LxLy bridge that will, eventually, help connect the entire Polygon ecosystem.
- Custom native (gas) tokens.
- Custom allow-lists for smart contracts and transactions.
- Support for modular, third-party data availability solutions.

## Polygon Miden

Polygon Miden is a novel ZK rollup currently in development, designed as a zkVM. Powered by the Miden VM, Polygon Miden extends Ethereum’s capabilities, offering enhanced throughput and privacy features beyond those of the EVM.

### Where Polygon Miden is heading

The new version (v2) of Polygon Miden Alpha testnet was [launched in Q2 2024](https://polygon.technology/blog/polygon-miden-alpha-testnet-v-2-live), and the mainnet is expected to go live later in the year.

Once Polygon Miden is on mainnet, it will plug into the Agglayer that will help connect the entire Polygon ecosystem.
