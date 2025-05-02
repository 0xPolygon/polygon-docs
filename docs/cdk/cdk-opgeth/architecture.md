# 🖥️ cdk-opgeth Architecture

This section outlines the architecture of the `cdk-opgeth` stack across its three configurations: **Sovereign**, **Validium**, and **zkRollup**. All configurations use the OP Stack, AggKit, and Agglayer components to deliver performant, Ethereum-compatible L2s with ZK-backed infrastructure.

---

## 📘 cdk-opgeth-sovereign

Chains using the sovereign configuration benefit from fast deployment, OP compatibility, and Agglayer's pessimistic security model. No execution proofs are used.

![cdk-opgeth-sovereign architecture](../CDK-opgeth-sovereign.png)

### 🔧 OP Stack
- **[OP Geth Client (EL)](https://github.com/ethereum-optimism/op-geth)**  
- **[OP Node (CL)](https://github.com/ethereum-optimism/optimism)**

### 🧩 AggKit
- **[AggOracle](https://github.com/agglayer/aggkit):** Updates the Global Exit Root (GER)
- **AggSender:** Sends Certificates to Agglayer
- **[Bridge API](https://github.com/0xPolygonHermez/zkevm-bridge-service):** Handles chain messaging

### 🗂️ Data Availability
- **[OP Batcher](https://github.com/ethereum-optimism/optimism):** Sends data to Ethereum L1
- **[Agglayer](https://github.com/agglayer/agglayer)**  
- Agglayer Node  
- Agglayer Prover  

### 📜 Contracts
- **[OP-Contracts-L1](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[OP-Contracts-L2](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[Ethereum Bridge Contracts](https://github.com/0xPolygonHermez/zkevm-contracts):** Ethereum L1 settlement

---

## 📘 cdk-opgeth-validium *(In Development)*

A configuration designed for off-chain data availability using alternative DA layers and ZK proofs via the SP1 prover.

![cdk-opgeth-validium architecture](../CDK-opgeth-zkrollup.png)

### 🔧 OP Stack
- **[OP Geth Client (EL)](https://github.com/ethereum-optimism/op-geth)**  
- **[OP Node (CL)](https://github.com/ethereum-optimism/optimism)**  
- **[OP Proposer](https://github.com/ethereum-optimism/optimism)**

### 🧩 AggKit
- **[AggOracle](https://github.com/agglayer/aggkit)**  
- AggSender  
- **[Bridge API](https://github.com/0xPolygonHermez/zkevm-bridge-service)**

### 🗂️ Data Availability
- **[Alt-DA TBD](https://docs.optimism.io/stack/beta-features/alt-da-mode)**  
- **[Agglayer](https://github.com/agglayer/agglayer)**  
- Agglayer Node  
- Agglayer Prover  

### 📜 Contracts
- **[OP-Contracts-L1](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[OP-Contracts-L2](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[Ethereum Bridge Contracts](https://github.com/0xPolygonHermez/zkevm-contracts)**

### 🔐 Prover Network
- **[SP1 Prover](https://github.com/succinctlabs/sp1):** Generates zkVM proofs

---

## 📘 cdk-opgeth-zkrollup *(In Development)*

A full ZK Rollup configuration that uses on-chain DA and the SP1 prover for trustless finality.

![cdk-opgeth-zkrollup architecture](../CDK-opgeth-zkrollup.png)

### 🔧 OP Stack
- **[OP Geth Client (EL)](https://github.com/ethereum-optimism/op-geth)**  
- **[OP Node (CL)](https://github.com/ethereum-optimism/optimism)**  
- **[OP Proposer](https://github.com/ethereum-optimism/optimism)**

### 🧩 AggKit
- **[AggOracle](https://github.com/agglayer/aggkit)**  
- AggSender  
- **[Bridge API](https://github.com/0xPolygonHermez/zkevm-bridge-service)**

### 🗂️ Data Availability
- **Ethereum DA:** Native Ethereum protocol  
- **[Agglayer](https://github.com/agglayer/agglayer)**  
- Agglayer Node  
- Agglayer Prover  

### 📜 Contracts
- **[OP-Contracts-L1](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[OP-Contracts-L2](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11)**  
- **[Ethereum Bridge Contracts](https://github.com/0xPolygonHermez/zkevm-contracts)**

### 🔐 Prover Network
- **[SP1 Prover](https://github.com/succinctlabs/sp1)**