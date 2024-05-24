This document explains how the Polygon zkEVM protocol manages the L2 rollup state while providing verifiability of each state transition.

## Trustless L2 state management

The trusted sequencer generates batches and broadcasts the batches to all L2 nodes. Each L2 node can then run the batches to compute the resulting L2 state locally, and thus achieve faster finality of L2 transactions.

But the trusted sequencer also commits the batches to L1, allowing L2 nodes who rely on the Ethereum security to fetch the batches from there, execute them, and thus compute the L2 state.

Nodes requiring stringent security can wait for correct transactional computations to be proved and verified, before syncing state. Zero-knowledge proofs are computed off-chain as required by the L1 smart contract and proofs are verified by another verifier smart contract.

This way both data availability and verification of transaction execution rely only on L1 security assumptions.

![figure 1](../../../img/zkEVM/01L2-overview-l2-state-management.png)

As shown in the above figure, L2 nodes can receive batch data in three different ways:

1. Directly from the trusted sequencer before the batches are committed to L1.
2. Straight from L1 after the batches have been sequenced.
3. Only after correctness of execution has been proved by the aggregator and verified by the `PolygonZkEVM.sol` contract.

It is worth noting that the three batch data formats are received by L2 nodes in the chronological order listed above.

## Three L2 states

There are three stages of the L2 state, each corresponding to the three different ways in which L2 nodes can update their state. All three cases depend on the format of batch data used to update the L2 state.

In the first instance, the update is informed solely by the information (i.e., Batches consisting of ordered transactions) coming directly from the trusted sequencer, before any data availability on L1. The resulting L2 state is called the trusted state.

In the second case, the update is based on information retrieved from the L1 network by L2 nodes. That is, after the batches have been sequenced and data has been made available on L1. The L2 state is referred to as the virtual state at this point.

The information used to update the L2 state in the last case includes verified zero-knowledge proofs of computational integrity. That is, after the zero-knowledge proof has been successfully verified in L1, L2 nodes synchronize their local L2 state root with the one committed in L1 by the trusted aggregator. As a result, such an L2 state is known as the consolidated state.

The figure below depicts the timeline of L2 State stages from a batch perspective, as well as the actions that trigger progression from one stage to the next.

![L2 State stages timeline](../../../img/zkEVM/02l2-l2-state-timeline.png)
