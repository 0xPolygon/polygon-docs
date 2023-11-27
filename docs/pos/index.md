Polygon PoS, initially unveiled as the Matic Network, has undergone substantial evolution, reflecting the dynamic landscape of blockchain scalability and security. Beginning as a hybrid Plasma sidechain designed to enhance Ethereum's scalability, Polygon is now transitioning towards a ZK-based validium solution on Ethereum. This shift is driven by the goal of achieving superior scalability and fortified security.

Polygon PoS is integrating the Polygon zkEVM execution environment, coupled with a specialized data availability layer. Its architecture is modular and composable, allowing fluid integration with a variety of layer-two scaling solutions. In this diverse and expanding ecosystem, Polygon PoS maintains its pivotal role as a primary "mainnet," underpinning numerous decentralized applications and services.

## Understanding the current PoS mechanism

### Transaction lifecycle overview
Polygon PoS's transaction lifecycle is characterized by a systematic workflow:

1. **Initiating Transactions**: Users initiate transactions on the Polygon PoS chain, often through smart contract interactions.
2. **Validation by Plasma Checkpoint Nodes**: Public nodes validate these transactions in accordance with the Polygon chain’s prevailing state.
3. **Checkpoint Creation and Ethereum Submission**: Post-validation, checkpoints encapsulating transaction data are crafted and forwarded to Ethereum's core contracts.
4. **Ethereum Mainnet Verification**: Leveraging Fraud Proofs, Ethereum’s core contracts scrutinize the checkpoints for authenticity.
5. **Executing Transactions**: Verified transactions are executed, culminating in state updates on the Matic Sidechain.
6. **Asset Transfer (Optional)**: Assets can be relocated back to Ethereum, utilizing the Plasma Exit Queue within the core contracts.
7. **Process Recurrence**: Users can initiate new transactions, re-engaging the cycle from the first step.

### Core contracts on Ethereum mainnet
At the heart of Polygon PoS's architecture is Ethereum mainnet, which anchors the system. A suite of core contracts on Ethereum provides essential functionalities, bridging the PoS chain with Ethereum. These include ensuring transaction and state change integrity via Fraud Proofs and managing asset transfers through the Plasma Exit Queue. These features collectively uphold security and operational fluidity between Polygon PoS and Ethereum.

### Checkpoint nodes
Public Plasma Checkpoint Nodes, functioning as validators, are integral to the Polygon PoS framework. Their responsibilities span validating transactions and submitting checkpoints to Ethereum's core contracts. By producing cryptographic proofs and submitting them to Ethereum, these nodes reinforce the symbiotic relationship between the two chains, ensuring transactional integrity and security.

### The Polygon sidechain
The Polygon Sidechain is the hub of transaction processing, offering a more scalable and cost-effective alternative to Ethereum's mainnet. Here, transactions validated by the Public Plasma Checkpoint Nodes are executed, with the Sidechain’s design optimized for high throughput and reduced latency. This makes the Polygon Sidechain a pivotal component in the network's ecosystem, efficiently handling transaction processing and maintaining the overall system's performance and reliability.