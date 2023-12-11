
!!!info
    This document is a continuation in the series of articles explaining the [transaction life cycle](submit-transaction.md) inside Polygon zkEVM.

The trusted sequencer reads transactions from the pool** and decides whether to discard them or order and execute them. Transactions that have been executed are added to a transaction batch, and the sequencer's local L2 State is updated.

Once a transaction is added to the L2 state, it is broadcast to all other zkEVM nodes via a broadcast service. It is worth noting that by relying on the trusted sequencer, we can achieve fast transaction finality (faster than in L1). However, the resulting L2 state will be in a trusted state until the batch is committed in the consensus contract.

## Verification on layer 1

Users will typically interact with trusted L2 state. However, due to certain protocol characteristics, the verification process for L2 transactions (on layer 1 to enable withdrawals) can take a long time, typically around 30 minutes but up to a week in rare cases.

!!!note

     - What is the rare case scenario?
        Verification of transactions on L1 will take 1 week only in the case when an emergency state is activated or the aggregator does not batch any proofs at all.

     - Additionally, the emergency mode is activated if a sequenced batch is not aggregated in 7 days. Please refer to [this guide](../malfunction-resistance/emergency-state.md) to understand more about the emergency state.

As a result, users should be mindful of the potential risks associated with high-value transactions, particularly those that cannot be reversed, such as off-ramps, over-the-counter transactions, and alternative bridges.
