Users must rely on a trusted sequencer for their transactions to be executed in the L2. However, users can include their transactions in a forced batch if they are unable to execute them through the trusted sequencer.

A forced batch is a collection of L2 transactions that users can commit to L1 to publicly declare their intent to execute those transactions.

![Forced batch sequencing flow](../../../img/zkEVM/09l2-forced-batch-seq-flow.png)

The `PolygonZkEVM.sol` contract has a `forcedBatches` mapping, as shown in the above figure, in which users can submit transaction batches to be forced. The `forcedBatches` mapping serves as an immutable notice board where forced batches are timestamped and published before being included in a sequence.

```
// ForceBatchNum --> hashedForcedBatchData

mapping(uint64 => bytes32) public forcedBatches;
```

!!!caution
    The trusted sequencer include these forced batches in future sequences to maintain its status as a trusted entity. Otherwise, users can demonstrate that they are being censored, and the trusted sequencer's trusted status is revoked.

Although the trusted sequencer is incentivized to sequence the forced batches published in the `forcedBatches` mapping, this does not guarantee finality of the transactions' execution in those batches.

In order to ensure finality in the case of trusted sequencer's malfunction, the L1 `PolygonZkEVM.sol` contract has an alternative batch sequencing function called `sequenceForceBatches`. This function allows anyone to sequence forced batches that have been published for a time period, specified by the public constant `forceBatchTimeout`, yet they have not been sequenced. The timeout is set to 5 days.

Any user can publish a batch to be forced by directly calling `forceBatch` function:

```bash
function sequenceForceBatches(
    ForcedBatchData[] memory batches
) public ifNotEmergencyState isForceBatchAllowed
```
in Etrog it is:

```bash
function sequenceForceBatches(
    BatchData[] calldata batches
) external virtual isSenderAllowedToForceBatches
```

In order to successfully publish a forced batch to the `forcedBatches` mapping, the following conditions must be met, otherwise the transaction reverts;

- The contract must not be in emergency state,
- The force batches must be allowed,
- The `maticAmount` argument must be higher than the MATIC fee per batch. It is the maximum amount of MATIC tokens the user is willing to pay as a forced batch publication fee. The fee for publishing a forced batch is the same as the fee for sequencing, and it is therefore set in the `batchFee` storage variable. Since the fee is paid when a forced batch is published, it is not be paid again when the batch is sequenced.
- The length of the transactions byte array must be less than the value of `MAX_TRANSACTIONS_BYTE_LENGTH` constant (which is set at 120000).

The forced batch is entered in `forcedBatches` mapping keyed by its force batch index.

```
struct ForcedBatchData {
    bytes transactions;
    bytes32 globalExitRoot;
    uint64 minForcedTimestamp;
}
```

The `lastForceBatch` storage variable, which is incremented for each forced batch published, serves as a forced batch counter and thus provides a specific index number. The value entered is a hash digest of the ABI-encoded packed struct fields from the `lastForceBatch`.

```
keccak256(
 abi.encodePacked(
  keccak256(bytes transactions),
  bytes32 globalExitRoot,
  unint64 minTimestamp
 )
);
```

Storage slots (mapping entries) are only used to store a commitment of the forced batch for storage usage optimization reasons. Data availability is ensured because it can be recovered from transaction calldata.

The contract sets the `minTimestamp` to the L1 block timestamp, at which point the forced batch is published.

In the extremely unlikely event that the trusted sequencer fails, any user can use the `sequenceForceBatches` function to sequence forced batches:

```
function sequenceForceBatches(
 ForcedBatchData[] memory batches
) public ifNotEmergencyState isForceBatchAllowed
```

The `sequenceForceBatches` function is similar to the `sequenceBatches` function, but it can be called by anyone if batch forcing is enabled.

The `sequenceForceBatches` function determines whether each batch in the submitted sequence has been published to the `forcedBatches` mapping for a period of time greater than the `forceBatchTimeout`.

Because the MATIC batch fee was paid at the time of publication, it is not required to be paid again.

If the sequence of forced batches meets all of the sequence conditions, it is added to the `sequencedBatches` mapping as a regular one. As a result, a `sequenceForceBatches` event is generated.

```
event SequenceForceBatches(uint64 indexed numBatch);
```

Note that since the sequences of forced batches, sequenced using the `sequenceForceBatches` function, never reaches a trusted state, a divergence occurs between the node’s local trusted L2 state and the virtual L2 state committed in the L1 `PolygonZkEVM.sol` contract.

This situation has been detected and handled by the node software. It reorganises its local L2 state instance based on the L2 state retrieved from L1. 

The below diagram depicts the distinction between trusted and virtual L2 states that occur when a forced batch sequence is executed.

![Differences between trusted and virtual L2 state](../../../img/zkEVM/10l2-diff-trustd-virtual-state.png)