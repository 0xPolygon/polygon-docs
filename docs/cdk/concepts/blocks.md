# Batches, Blocks, and Transactions

To understand how transactions are handled on L2s built with the CDK, there are four key concepts to understand:

- **Transaction**: Signed instruction to perform an action on the blockchain.
- **Block**: A group of transactions and a hash of the previous block in the chain.
- **Batch**: A group of many transactions from multiple blocks.

To best understand how these concepts relate to each other, on this page, we will follow a real transaction from the Polygon zkEVM to see how it first gets included in a block on the L2, then in a batch, and finally, a sequence that is sent to Ethereum.

![Batches, blocks, transactions](../../img/cdk/sequence-batch-block-transaction.png)

## Transaction

A transaction is a cryptographically signed instruction from an account to update the state of the blockchain. Users can send transactions to L2 chains built with the CDK using the same tools and libraries they use to interact with Ethereum such as MetaMask.

Transactions are included in both blocks and batches. An example Polygon zkEVM transaction [`0xdd`](https://zkevm.polygonscan.com/tx/0xdd3f79c24886310ddf868ad1d36aadc6a3b6495048f68aad765c658c42426ef8) performs a `Simple Swap` function call, and part of block [`12952601`](https://zkevm.polygonscan.com/block/12952601) on the L2.

![Transaction with Block Number](../../img/cdk/transaction-block.png)

## Block

Blocks contain multiple transactions and the hash of the previous block in the chain to link blocks together. Following our example transaction from above, the `0xdd` transaction is included in block [`12952601`](https://zkevm.polygonscan.com/block/12952601), which contains [2 total transactions](https://zkevm.polygonscan.com/txs?block=12952601).

![Block and Batch](../../img/cdk/block-batch.png)

## Batch

Batches contain multiple transactions from multiple blocks. The two total transactions from our example block `12952601` are included in batch [`2041736`](https://zkevm.polygonscan.com/batch/2041736), which contains [10 total transactions](https://zkevm.polygonscan.com/txs?batch=2041736).

As there is also a `Sequence Tx Hash` field associated with this batch, we can infer that this batch is part of a sequence of batches that have already been sent to Ethereum.

![Batch of transactions](../../img/cdk/batch-overview.png)

By inspecting the transactions in the batch, we can see:

- Our original example transaction is included in this batch.
- The batch contains many transactions from many different blocks.

![Transaction found inside batch](../../img/cdk/transaction-in-batch.png)

If the L2 is a [rollup](./layer2s.md) (meaning it uses Ethereum for it&rsquo;s [data availability](https://docs.polygon.technology/cdk/glossary/#data-availability)), it sends an array of batches to Ethereum, by providing the array as an argument to the `sequenceBatches` function of a smart contract on Ethereum.

![Sequence Transaction](../../img/cdk/sequence-transaction.png)

By inspecting the `Sequence Tx Hash` transaction, we can see the `sequenceBatches` function is called with the array of batches as an argument. One of these batches is the batch we have been following, `2041736`, which contains our original example transaction:

![Last Batch Sequenced](../../img/cdk/last-batch-sequenced.png)
