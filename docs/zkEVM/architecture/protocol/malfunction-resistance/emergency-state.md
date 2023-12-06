The emergency state is a Consensus Contract state (of 'PolygonZkEVM.sol' and 'PolygonZkEVMBridge.sol') that, when activated, terminates batch sequencing and bridge operations. The goal of enabling the emergency state is to allow the Polygon team to solve cases of soundness vulnerabilities or exploitation of any smart contract bugs. It is a security measure used to protect users' assets in zkEVM.

The following functions will be disabled while in the emergency state:

- `sequenceBatches`
- `verifyBatches`
- `forceBatch`
- `sequenceForceBatches`
- `proveNonDeterministicPendingState`

As a result, while the contract is in the emergency state, the Sequencer cannot sequence batches. Meanwhile, the trusted Aggregator will be able to consolidate additional state transitions or override a pending state transition that can be proven to be non-deterministic.

When the same sequence of batches is successfully verified with two different resulting L2 State root values, a non-deterministic state transition occurs. This situation could arise if a soundness vulnerability in the verification of the Zero-Knowledge proof of computational integrity is exploited.

## When is the emergency state activated?

The emergency state can only be triggered by two contract functions:

1. It can be directly activated by calling the `activateEmergencyState` function by contract owner.

2. It can also be called by anyone after a `HALT AGGREGATION TIMEOUT` constant delay (of one week) has passed. The timeout begins when the batch corresponding to the `sequencedBatchNum` argument has been sequenced but not yet verified.

This situation directly implies that no one can aggregate batch sequences. The objective is to temporarily stop the protocol until aggregation activity resumes.

```
function activateEmergencyState(uint64 sequencedBatchNum) external
```

Additionally, anyone can use the `proveNonDeterministicPendingState` function to trigger the emergency state, but only if they can prove that some pending state is non-deterministic.

```
function proveNonDeterministicPendingState( 
   uint64 initPendingStateNum , 
   uint64 finalPendingStateNum ,
   uint64 initNumBatch ,
   uint64 finalNewBatch , 
   bytes32 newLocalExitRoot , 
   bytes32 newStateRoot ,
   uint256 [2] calldata proofA , 
   uint256 [2][2] calldata proofB , 
   uint256 [2] calldata proofC 
) public ifNotEmergencyState
```

## Overriding a pending state

If a soundness vulnerability is exploited, the Trusted Aggregator has the ability to override a non-deterministic pending state.

To initiate the override, use the `overridePendingState` function. Because the Trusted Aggregator is a trusted entity in the system, only the L2 state root provided by the Trusted Aggregator is considered valid for consolidation in the event of a non-deterministic state transition.

```
function overridePendingState( 
   uint64 initPendingStateNum , 
   uint64 finalPendingStateNum , 
   uint64 initNumBatch ,
   uint64 finalNewBatch ,
   bytes32 newLocalExitRoot ,
   bytes32 newStateRoot ,
   uint256 [2] calldata proofA , 
   uint256 [2][2] calldata proofB , 
   uint256 [2] calldata proofC 
)  public onlyTrustedAggregator
```

To successfully override a pending state, the Trusted Aggregator must submit a proof that will be verified in the same way, as in the `proveNonDeterministicPendingState` function. If the proof is successfully verified, the pending state transition is wiped and a new one is directly consolidated.

To summarize, the emergency state can only be activated:

- when the contract owner deems it appropriate, or
- when aggregation activity is halted due to a `HALT_AGGREGATION_TIMEOUT`, or
- when anyone can demonstrate that a pending state is non-deterministic.
