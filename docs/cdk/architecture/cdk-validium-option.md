The Polygon CDK validium is one of two configuration options of the Polygon CDK, the other being the Polygon zkEVM rollup.

As per [the definition](https://ethereum.org/developers/docs/scaling/validium), the Polygon CDK validium uses validity proofs to enforce integrity of state transitions, but it does not store transaction data on the Ethereum network.

The Polygon CDK validium is in fact a _zero-knowledge validium_ (zkValidium) because it utilises the Polygon zkEVM's off-chain prover to produce zero-knowledge proofs, which are published as _validity proofs_.

The use of the above-mentioned prover, to a certain extent, adds trustlessness to the Polygon CDK validium.

The validium mode inherits, not just the prover, but all the Polygon zkEVM's components and their functionalities, except that it does not publish transaction data on L1.

The validium configuration has one major advantage over the zkEVM rollup option: And that is, reduced gas fees due to the off-chain storage of transaction data, where only a hash of the transaction data gets stored on the Ethereum network.

## Data availability committee (DAC)

In relation to storing transaction data off-chain, the CDK validium comes with the requirement to manage the data.

- First of all, the transaction data is not published to the L1 but only the hash of the data.
- Secondly, a trusted-sequencer collects transactions from the pool DB, puts them into batches and computes the hash of the transaction data. 

It is due to the above two points that the Polygon CDK validium has to have a set of _trusted actors_, who can monitor and even authenticate the hash values that the sequencer proposes to be published on the L1. 

The hash values need to be verified as true _footprints_ of the transaction data corresponding to all transactions in the sequenced batches.

These _trusted actors_ are collectively called the Data Availability Committee (DAC). 

After verifying the proposed hash values individually, each DAC member signs them and sends the signature to the sequencer.

The sequencer uses a _multi-sig_, which is a custom-specified _m-out-of-n multi-party protocol_, to attach the required _m_ signatures to the hash of the transaction data. The _multi-sig_ contract lives on the L1 network. 

Architecturally speaking, the Polygon CDK validium is therefore nothing but a zkEVM with a DAC. That is, **Polygon CDK validium =  Polygon zkEVM + DAC**.

## Validium data flow

The DAC works together with the sequencer to control the flow of data and state changes. 

The below diagram depicts a simplified outline of the Polygon CDK Validium architecture. It particularly shows how the DAC and the sequencer relate in the overall data flow.

![CDK validium data availability dataflow](../../img/cdk/cdk-val-dac-02.png)

The entire process can be broken down as follows:

1. **Batch formation**: The sequencer collects user transactions, adds them to blocks, and puts the blocks in batches while recursively computing their hash values.
2. **Batch authentication**: Once the batches are assembled, and their hash values computed, they need to be authenticated by the DAC. The sequencer therefore forwards the batch data, and their corresponding hash values to the DAC, as a way to request for signatures.
3. **Data validation and storage**: The DAC nodes independently validate the batch data against the hash values received from the sequencer. Once validated, each hash value is stored in each DAC node's local database for future reference.
4. **Signature generation**: Each DAC node generates a signature for each batch hash. This serves as an endorsement of the batch's integrity and authenticity.
5. **Communication with Ethereum**: The sequencer collects the DAC members' signatures and the original batch hash, and submits them to the Ethereum network for verification.
6. **Verification on Ethereum**: A designated _multi-sig_ smart contract on Ethereum verifies the submitted signatures against each DAC member's known signatures, and confirms that sufficient approval has been provided for the batch hash.
7. **Final settlement with zero-knowledge proof**: The aggregator prepares a proof for the batch via the Prover and submits it to the Ethereum network. This proof confirms the validity of the transactions in the batch without revealing transaction details. The chain's state gets updated on Ethereum.
