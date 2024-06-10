
!!!info
    This document is a continuation in the series of articles explaining the [transaction life cycle](submit-transaction.md) inside Polygon zkEVM.

The trusted sequencer reads transactions from the pool and decides which transactions to order and execute. Once executed, transactions are added to blocks, then the blocks fill batches, and the sequencer's local L2 state is updated.

Once a transaction is added to the L2 state, it is broadcast to all other zkEVM nodes via a broadcast service. It is worth noting that by relying on the trusted sequencer, we can achieve fast transaction finality (faster than in L1). However, the resulting L2 state remains a trusted state until the batch is committed in the consensus contract.

## Verification on layer 1

Users typically interact with trusted L2 state. However, because of specific protocol characteristics, the verification process for L2 transactions on L1 (to enable withdrawals) can be lengthy, usually taking about 30 minutes, and in rare instances, up to a week.

!!!note

     - What is the rare case scenario?
        Verification of transactions on L1 can take 1 week in the case when an emergency state is activated or the aggregator does not batch any proofs at all.

     - Additionally, the emergency mode is activated if a sequenced batch is not aggregated in 7 days. Please refer to [this guide](../malfunction-resistance/emergency-state.md) to understand more about the emergency state.

As a result, users should be mindful of the potential risks associated with high-value transactions, particularly those that cannot be reversed, such as off-ramps, over-the-counter transactions, and alternative bridges.
