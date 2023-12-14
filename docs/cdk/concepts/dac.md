Data availability in blockchain technology refers to whether or not transaction data is available on-chain or off-chain.

If data is available on-chain, then each node has to store every piece of data related to every transaction. This can be costly for node operators as hardware and storage requirements are high. Moving data off-chain streamlines node architecture and operations.

!!! info "Recommended resource"
    See [Ethereum.org's discussion on data availability](https://ethereum.org/en/developers/docs/data-availability/).

## Data availability committee (DAC)

Polygon's CDK validium has an optional DAC.

A DAC is an off-chain network of nodes that implements a data storage layer in a modular chain architecture like CDK. Some advantages are:

- **Lower transaction fees**: Reduced computational requirements lead to lower fees and faster finality on the main network.
- **Privacy and security**: The DAC stores secure and private transaction data.
- **Trustless**: Data owners do not have to trust the blockchain operator.
- **Scalable**: Decoupling data storage from the main chain supports more scalable networks.

DACs store the data required to reconstruct the state of the blockchain and make that data accessible so that, if the main blockchain network goes down, users can still access their assets and data.

Setting up a DAC can be costly and therefore DACs mostly support Enterprise use cases which require cheap and fast transactions with a private and secure data layer.

The CDK validium DAC is a secure consortium of nodes that ensures off-chain data access.

## DAC data flow

![CDK validium data availability dataflow](../../img/cdk/cdk-val-dac-02.png)

The DAC works together with the sequencer to control the flow of data. The process can be broken down as follows:

1. **Batch formation**: The sequencer collects user transactions and organizes them into batches.

2. **Batch authentication**: Once the batches are assembled, they are authenticated. The sequencer forwards the batch data and its corresponding hash to the DAC.

3. **Data validation and storage**: The DAC nodes independently validate the batch data. Once validated, the hash is stored in each node's local database for future reference.

4. **Signature generation**: Each DAC node generates a signature for the batch hash. This serves as an endorsement of the batch's integrity and authenticity.

5. **Communication with Ethereum**: The sequencer collects the DAC members' signatures and the original batch hash and submits them to the Ethereum network for verification.

6. **Verification on Ethereum**: A designated smart contract on Ethereum verifies the submitted signatures against a list of valid DAC members and confirms that sufficient approval has been provided for the batch hash.

7. **Final settlement with zero-knowledge proof**: The aggregator prepares a proof for the batch via the prover and submits it to Ethereum. This proof confirms the validity of the batch's transactions without revealing their details. The chain state updates on Ethereum.
