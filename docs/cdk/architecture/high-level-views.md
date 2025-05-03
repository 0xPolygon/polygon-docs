## 💻 Sovereign Mode (Live)

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| CDK Stack    | CDK-Erigon           | Combined EL + CL client                  | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon) |
| Aggkit       | AggOracle            | GER update component                     | [aggkit](https://github.com/agglayer/aggkit) |
|              | AggSender            | Sends certificates to Agglayer           | — |
|              | Bridge API           | Cross-chain messaging                    | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | Agglayer             | Native Agglayer connectivity             | [agglayer](https://github.com/agglayer/agglayer) |
| Contracts    | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |

## 🧪 Validium Mode

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| CDK Stack    | CDK-Erigon           | EL + CL client                           | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon) |
| CDK          | Aggregator           | Handles sequencing                       | — |
|              | Sequence Sender      | Submits blocks to DA                     | — |
|              | Bridge API           | Messaging layer                          | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | Custom DAC           | Off-chain DA                             | [cdk-data-availability](https://github.com/0xPolygon/cdk-data-availability) |
|              | Agglayer             | Messaging/bridge layer                   | [agglayer](https://github.com/agglayer/agglayer) |
| Prover       | Hermez Prover        | zk-SNARK based prover                    | [zkevm-prover](https://github.com/0xPolygonHermez/zkevm-prover) |
| Contracts    | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |

## 🔒 zkRollup Mode

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| CDK Stack    | CDK-Erigon           | EL + CL client                           | [cdk-erigon](https://github.com/0xPolygonHermez/cdk-erigon) |
| CDK          | Aggregator           | Handles sequencing                       | — |
|              | Sequence Sender      | Submits blocks to L1                     | — |
|              | Bridge API           | Messaging layer                          | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | Ethereum DA          | On-chain data storage                    | — (uses Ethereum L1) |
|              | Agglayer             | Messaging/bridge layer                   | [agglayer](https://github.com/agglayer/agglayer) |
| Prover       | Hermez Prover        | zk-SNARK based prover                    | [zkevm-prover](https://github.com/0xPolygonHermez/zkevm-prover) |
| Contracts    | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |


### User Data Flow

The following diagram sequentially depicts the user data flow for the CDK FEP config in validium mode using a mock prover and an Agglayer connection.

![High level view of CDK user data flow](../../img/cdk/cdk-user-data-flow.svg)

---

### Sequential Interactions

1. The user sends a transaction to the **CDK Erigon RPC node**.
2. The **CDK Erigon RPC node** proxies the data to the **CDK Erigon sequencer node** and syncs the batch data between the sequencer and the RPC nodes.
3. The sequencer sequences the transaction batches.
4. The **sequencer sender** reads batches from the RPC node.
5. In validium mode only, the sequencer sender persists transaction data into the **DAC nodes**.
6. The sequencer sender sequences the batches into the **L1 smart contracts**.
7. The **aggregator** reads batches from the sequencer data stream.
8. The aggregator sends batches to the **provers**.
9. The aggregator submits the final proof to the **Agglayer**.
10. The Agglayer submits the final proof to the **L1 smart contract domain**.

---

### Mermaid Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant ErigonRPC as CDK Erigon RPC Node
    participant Sequencer as CDK Erigon Sequencer Node
    participant SeqSender as Sequencer Sender
    participant Aggregator
    participant Agglayer
    participant DACNodes as DAC Nodes
    participant Prover
    participant L1 as L1 Smart Contracts

    User->>ErigonRPC: Send transaction
    ErigonRPC->>Sequencer: Proxy and sync transaction data
    Sequencer->>Sequencer: Sequence transaction batches
    SeqSender->>ErigonRPC: Read batches
    SeqSender->>DACNodes: Persist transaction data (validium mode only)
    SeqSender->>L1: Sequence batches into L1 Smart Contracts
    Aggregator->>Prover: Send batches to Prover
    Prover->>Aggregator: Return proofs
    Aggregator->>Aggregator: Aggregate proofs
    Aggregator->>Agglayer: Submit final proof
    Agglayer->>L1: Submit final proof to L1 Smart Contract Domain
```