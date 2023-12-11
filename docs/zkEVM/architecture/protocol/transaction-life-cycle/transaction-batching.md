
!!!info
    This document is a continuation in the series of articles explaining the [transaction life cycle](submit-transaction.md) inside Polygon zkEVM.

The trusted sequencer must batch the transactions using the following `BatchData` struct specified in the `PolygonZkEVM.sol` contract:

```
struct BatchData {
  bytes transactions;
  bytes32 globalExitRoot;
  uint64 timestamp;
  uint64 minForcedTimestamp;
}
```

### Transactions

​These are byte arrays containing the concatenated batch transactions.

​Each transaction is encoded according to the Ethereum pre-EIP-155 or EIP-155 formats using RLP (recursive-length prefix) standard**, but the signature values, `v`, `r` and `s`, are concatenated as shown below;

1. `EIP-155`: $\mathtt{\ rlp(nonce, gasprice, gasLimit, to, value, data, chainid, 0, 0,) \#v\#r\#s\#effectivePercentage}$

2. `pre-EIP-155`: $\mathtt{\ rlp(nonce, gasprice, gasLimit, to, value, data) \#v\#r\#s\# effectivePercentage}$.

### GlobalExitRoot

This is the root of the bridge's global exit Merkle tree**, which will be synchronized in the L2 state at the start of batch execution.

The bridge transports assets between L1 and L2, and a claiming transaction unlocks the asset in the destination network.

### Timestamp

​In as much as Ethereum blocks have timestamps, each batch has a timestamp.

​There are two constraints each timestamp must satisfy in order to ensure that batches are ordered in time and synchronized with L1 blocks:

1. The timestamp of a given batch must be greater or equal to the timestamp of the last sequenced batch.

2. The maximum batch timestamp a trusted sequencer can set to a batch is the timestamp of the block where the sequencing L1 transaction is executed.

### MinForcedTimestamp

If a batch is a so-called forced batch, this parameter must be greater than zero. Censorship is countered by using forced batches. More on this in the following sections.
