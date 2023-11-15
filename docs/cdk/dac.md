---
id: dac-overview
title: Data Availability
sidebar_label: Data Availability
description: "Learn about the DAC in Polygon CDK."
keywords:
  - docs
  - polygon
  - layer 2
  - validium
  - dac
  - data availability
  - sdk
  - cdk
  - chain development kit
---

Data Availability Committees (“DACs”) have one core responsibility: to verify that the data necessary to reconstruct the L2 state from on-chain events is accessible to everyone. This availability means that, even if L2 operators go offline, users can still access their assets and data.

## The Key to CDK-developed Chains: The DAC

In CDK-developed chains, the DAC, functioning as a secure consortium of nodes, ensures off-chain data access. This consortium is pivotal for the operation of CDK-developed chains, maintaining data availability even if chain operators go offline.

### Polygon zkEVM: Powering Computation

CDK-developed chains are powered by Polygon zkEVM, offering a specialized environment for runtime and execution. This zkEVM-based engine is an exact implementation of the existing zkEVM. Operating as a zero-knowledge rollup (zk-rollup), it efficiently condenses numerous transactions into one batch, which is then submitted to Ethereum for validation.

Learn more about the roles and operation of zkEVM in the official documentation, available [<ins>here</ins>]().

### Data Availability Layer: Ensuring Data Robustness

The DAC-managed Data Availability Layer, combined with the computational efficiency of Polygon zkEVM, ensures high-performance L2 blockchains within chains built with the CDK.

## Advantages of the DAC Provided by Polygon CDK

The DAC primarily provides:

- **Lower Transaction Fees**: Reduced computational requirements lead to lower fees.
- **State Privacy**: Holding a secure copy of state transitions, ensuring data integrity.

## zkEVM vs. Validium

The table below illustrates the key differences between Polygon's zkEVM and the Validium used in Polygon CDK.

| Feature | zkEVM | Validium |
|---------|-------|------------|
| **Transaction Data Storage** | Stores all transaction data on L1 (Ethereum). | Only the hash of the transaction data is stored on Ethereum. |
| **Data Availability** | All data is available on-chain, providing high data availability. | Off-chain data availability is managed by the DAC, which authenticates the hashes of transaction data. |
| **Security** | Offers high security due to on-chain data availability and the use of Zero-Knowledge Proofs (ZKPs). | The off-chain data availability can potentially reduce security if DAC members collude to withhold state data. However, security is still maintained through the use of ZKPs. |
| **Gas Fees** | Higher, because all transaction data is stored on Ethereum. | Lower, because only the hash of the transaction data is stored on Ethereum. |
| **Proof Generation** | Uses Prover to generate ZKPs of batched transactions for validation. | Uses Prover to generate ZKPs of batched transactions for validation. |
| **Transaction Validation** | Validation is achieved through smart contracts on Ethereum. | Validation involves an additional layer where DAC members sign the hash of the transaction data. |
| **Final Settlement** | The transaction batches and their corresponding ZKPs are added to the Ethereum state. | The hash of transaction data and its ZKP are added to the Ethereum state, referred to as the Consolidated State. |

## Data Flow in Polygon CDK

The DAC works closely with the Sequencer to ensure secure and efficient data handling. The process can be broken down as follows:

1. **Batch Formation**: The Sequencer collects user transactions and organizes them into batches.

2. **Batch Authentication**: Once the batches are assembled, they are authenticated. The Sequencer forwards the batch data and its corresponding hash to the DAC.

3. **Data Validation and Storage**:  The DAC nodes each independently validate the batch data. Once validated, the hash is stored in each node's local database for future reference.

4. **Signature Generation**: Each DAC node generates a signature for the batch hash. This serves as an endorsement of the batch's integrity and authenticity.

5. **Communication with Ethereum**: The Sequencer collects the DAC members' signatures and the original batch hash and submits them to the Ethereum network for verification.

6. **Verification on Ethereum**: A designated smart contract on Ethereum verifies the submitted signatures against a list of valid DAC members and confirms that sufficient approval has been provided for the batch hash.

7. **Final Settlement with ZKP**: The Aggregator prepares a ZKP for the batch and submits it to Ethereum. This proof confirms the validity of the batch's transactions without revealing their details, thereby updating the CDK-developed chain state on Ethereum.

This process ensures a secure, efficient, and auditable flow of data through the system, supporting the implementation and operation of a CDK-developed chain in a broad range of contexts.

The following diagram illustrates the entire data flow process within Polygon CDK.

<div align="center">
  <img src="/img/cdk/zksupernets-data-flow.excalidraw.png" alt="bridge" width="100%" height="30%" />
</div>
