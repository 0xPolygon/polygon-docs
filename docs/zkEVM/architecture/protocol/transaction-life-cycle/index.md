
!!! info 
    
    Users need funds on L2 to be able to send transactions to the L2 network.

    To do so, users need to deposit Ether to L2 through the [Polygon Portal](https://portal.polygon.technology/bridge).

Bridging:
    
- Deposit ETH.

- Wait until `globalExitRoot` is posted on L2.

- Perform claim on L2 and receive the funds.


Transaction process on L2 and the three (3) states:

- User initiates a transaction using their wallet (e.g. MetaMask) and sends it to a trusted sequencer.

- The transaction gets finalized on L2 once the trusted sequencer commits to adding the transaction to a batch. This is known as the _trusted state_.

- Sequencer sends the batch data to L1 smart contract, enabling any L2 node to synchronize from L1 in a trustless way. This is also known as the _virtual state_.

- Aggregator takes the pending transactions, and builds a proof.

- Once the proof is verified, the transactions attain L1 finality (important for withdrawal of funds from L2). This is called the _consolidated state_.

The above process is a summarized version of how transactions are processed in Polygon zkEVM. 

Take a look at the complete description in the [transaction life cycle](./submit-transaction.md)
