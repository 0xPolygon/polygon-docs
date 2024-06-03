# Transaction Finality

Through the [transaction lifecycle](./transaction-lifecycle.md), transactions progress through three states of finality:

1. **Trusted**: The transaction has been **submitted** and **executed** on the L2. The user receives the result of the transaction and can continue to interact with the L2 chain.

2. **Virtual**: The transaction has been **batched** and **sequenced**, meaning the batch containing the transaction has been sent to Ethereum. However, the ZK-proof to verify the validity of the transaction has not yet been posted and verified on Ethereum.

3. **Consolidated**: A ZK-proof has been generated, posted, and verified on Ethereum. The transaction is now considered final at the L1 level. This means the user is free to withdraw their funds from the L2 chain back to Ethereum.

![Transaction Finality](../../img/cdk/transaction-finality.png)
