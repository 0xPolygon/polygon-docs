---
comments: true
---

This glossary provides definitions for technical terminology and concepts that commonly occur throughout the CDK docs space.

### AggLayer v1 (AL1)
The AggLayer is the interoperability layer that CDK chains connect to, enabling features such as seamless and efficient cross-chain communication, unified liquidity, and more. AggLayer v1 (AL1), is the first version of many planned iterations that relies on ZK checks to ensure operational soundness, and a unified bridge infrastructure.
Read more on the AggLayer in the Polygon blog [here](https://polygon.technology/blog/wtf-is-polygon?utm_source=twitter&utm_medium=social&utm_content=wtf-is-polygon).

### Chain operator
The IP, or individual(s), who own a chain and are responsible for chain operation and maintenance. This includes tasks such as transaction validation, block production, and ensuring the security and integrity of the chain, etc., any combination of which a chain operator may perform personally in varying degrees.

### Data availability
Data availability in the context of modular rollups refers to the idea that transaction callback data needs to be available to L1 network actors where transactions are settled and finalized, so it can be used to verify transaction execution if necessary. 

### Data Availability Committee (DAC)
Polygon CDK validiums connect to a DAC to guarantee data availability. The DAC nodes fetch tx data from the sequencer, validate it independently, and then sign it guaranteeing its validity before storing it in the local database. The data remains available to be fetched by other networks actors across all DAC nodes.

### LxLy bridge
The native bridge infrastructure of CDK chains that allows transfer of assets and messages between L2 and L1 (typically Ethereum).

### LxLy messenger
A contract on the LxLy bridge utilizes its message passing capabilities to pass arbitrary messages between L1 and L2.  This is not a separate component, but part of the LxLy bridge's architecture.

### POL (Token)
The POL token powers the Polygon ecosystem through a native re-staking protocol that allows token holders to validate multiple chains, and perform multiple roles on each of those chains (sequencing, ZK proof generation, participation in data availability committees, etc.) 

### Rollups
Rollups refer to blockchain scaling solutions (in the context of Ethereum) that carry out transaction execution on L2, and then post updated state data to a contract on L1. There are different types rollups, two of the most popular being optimistic, and zero-knowledge (ZK) rollups. Follow the links below to learn more:

- [Optimistic rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/)
- [ZK rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/)

### Stake the Bridge (STB)
A feature of the [unified bridge](#unified-bridge) that lets CDK chain operators maintain control over the assets that are deposited to their respective networks, enabling them to implement staking mechanisms, investment strategies, and other custom features on L2.

### Unified bridge
A specific instance of an LxLy bridge that allows several chains to connect to it.  This instance is specific to the [AggLayer v1](#agglayer-v1-al1).

### Unified escrow (Master Escrow)
The unified bridge's escrow contract that holds all the tokens that bridged (locked on L1), and natively minted on L2.

### Validiums
Validiums are a special kind of ZK rollup protocol that handles data availability off-chain instead of posting callback data to base layer Ethereum. CDK chains support deploying and running validium using a Data Availability Committee (DAC) as the DA solution.
Learn more about validiums [here](https://ethereum.org/en/developers/docs/scaling/validium/).