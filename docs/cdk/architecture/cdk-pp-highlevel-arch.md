The figure below depicts a simplified, high level view of the CDK PP chain architecture, as well as the flow of transactions through the system.

![Figure: CDK PP Architecture](../../img/cdk/CDK-pessimistic-proof-chain.jpg)

## Transaction flow

Here is a step by step flow of transactions starting from when users submit transactions up to when the transactions are settled in L1.

1. A user connects to the chain via a CDK Erigon RPC node and submits a transaction.
2. CDK Erigon RPC node sends the transaction data to the transaction-pool manager.
3. The transaction-pool manager proxies all transaction data to the CDK Erigon sequencer.
4. CDK Erigon sequencer executes transactions, puts the transactions in blocks, and the blocks fill up batches. 
5. CDK Erigon sequencer syncs all transaction data with any CDK Erigon RPC node.
6. AggSender gets batch data from the CDK Erigon sequencer, uses the data to generate certificates, and submits the certificates to the JSON-RPC API.
7. The JSON-RPC API checks validity of the certificates against the transaction data in the CDK Erigon RPC node.
8. After validating the certificates, the JSON-RPC API sends a request to generate a proof, together with the necessary data (including the certificates), to the SP1 prover. 
9. Once the proof is received from the SP1 prover, the JSON-RPC API sends it to L1.