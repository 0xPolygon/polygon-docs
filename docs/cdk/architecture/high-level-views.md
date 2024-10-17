## CDK full execution proof (FEP)

The diagram below depicts a simplified architectural layout of the CDK FEP stack and indicates at a high level how components communicate.

![High level view of CDK stack](../../img/cdk/cdk-stack.svg)

### Component interactions

- Engineers use a CLI to manage the backend components, installing and initializing various modes of operation, such as validium versus rollup for example.
- External applications send transactions to the CDK Erigon RPC node which forwards the transaction data to the sequencer via the transaction pool manager.
- The sequencer sequences transactions batches and synchronizes data with the RPC node.
- The sequencer sender reads batch data from the RPC node.
- The aggregator reads batch data from the sequencer data stream.
- The sequencer sender persists data into the L1 smart contract domain for rollup mode and into DAC nodes for validium mode operations.
- The aggregator sends batches to the prover and receives proofs in return. Together with the prover, it aggregates the proofs into batches before submitting the final proofs to the AggLayer or L1, depending on the chosen settlement layer.
- Users interact with the bridge service via the bridge UI or API.
- The AggLayer verifies proofs and interacts with the L1 smart contracts.

### User data flow

The following diagram is a sequential depiction of the user data flow for the CDK FEP stack in validium mode using a mock prover and having an AggLayer connection.

![High level view of CDK user data flow](../../img/cdk/cdk-user-data-flow.svg)

#### Sequential interactions

1. User sends a transaction to the CDK Erigon RPC node.
2. The CDK Erigon RPC node proxies the data to the CDK Erigon sequencer node and syncs the batch data between the sequencer and the RPC nodes.
3. The sequencer sequences the transaction batches.
4. The sequencer sender reads batches from the RPC node.
5. In validium mode only, the sequencer sender persists transaction data into the DAC nodes.
6. The sequencer sender sequences the batches into the L1 smart contracts.
7. The aggregator reads batches from the sequencer data stream.
8. The aggregator sends batches to the provers.
9. The aggregator submits the final proof to the AggLayer.
10. The AggLayer submits the final proof to the L1 smart contract domain.

```mermaid
sequenceDiagram
    participant User
    participant ErigonRPC as CDK Erigon RPC Node
    participant Sequencer as CDK Erigon Sequencer Node
    participant SeqSender as Sequence Sender
    participant Aggregator
    participant AggLayer
    participant DACNodes as DAC Nodes
    participant Prover
    participant L1 as L1 Smart Contracts

    User->>ErigonRPC: Send transaction
    ErigonRPC->>Sequencer: Proxy and sync transaction data
    Sequencer->>Sequencer: Sequence transaction batches
    SeqSender->>ErigonRPC: Reads batches
    SeqSender->>DACNodes: Persist transaction data (validium mode only)
    SeqSender->>L1: Sequence batches into L1 Smart Contracts 
    Aggregator->>Prover: Send batches to Prover 
    Prover->>Aggregator: Return proofs 
    Aggregator->>Aggregator: Aggregate the proofs
    Aggregator->>AggLayer: Submit final proof
    AggLayer->>L1: Submit final proof to L1 Smart Contract Domain
```

!!! tip
    Detailed AggLayer flows will be published soon.
