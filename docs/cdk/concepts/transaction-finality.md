# Transaction finality

Throughout the [transaction lifecycle](./transaction-lifecycle.md), transactions progress through three states of finality:

1. Trusted: The transaction has been [submitted](./transaction-lifecycle.md#submitted) and [executed](./transaction-lifecycle.md#executed) on the L2. The user receives the result of the transaction and can continue to interact with the L2 chain.

2. Virtual: The transaction has been [batched](./transaction-lifecycle.md#batched) and [sequenced](./transaction-lifecycle.md#sequenced), meaning the batch containing the transaction has been sent to Ethereum. However, the ZK-proof to verify the validity of the transaction has not yet been posted and verified on Ethereum.

3. Consolidated: The transaction has been [aggregated](./transaction-lifecycle.md#aggregated), meaning a ZK-proof has been generated, posted, and verified on Ethereum to prove the validity of the transaction. The transaction is now considered final at the L1 level, enabling the user to withdraw their funds from the L2 chain back to Ethereum.

![Transaction finality](../../img/cdk/transaction-finality.png)

## Further reading

- [zkEVM state management](../../zkEVM/architecture/protocol/state-management.md).
- [zkEVM transaction lifecycle](../../zkEVM/architecture/protocol/transaction-life-cycle/submit-transaction.md).