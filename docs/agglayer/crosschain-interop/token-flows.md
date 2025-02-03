The following workflows describe how token transfers and message passing are implemented by the unified bridge across various L1 and L2 permutations. While the descriptions refer only to token transfers in the current AggLayer implementation, the sequence of events is exactly the same for arbitrary messages. 

## L1 to L2

1. If a call to `bridgeAsset` or `bridgeMessage` on L1 passes validation, the unified bridge contract appends an exit leaf to the L1 exit tree and computes the new L1 exit tree root.

2. The global exit root manager appends the new L1 exit tree root to the global exit tree and computes the global exit root.

3. The sequencer fetches the latest global exit root from the global exit root manager.

4. At the start of the transaction batch, the sequencer stores the global exit root in special storage slots of the L2 global exit root manager smart contract, allowing L2 users to access it.

5. A call to `claimAsset` or `claimMessage` provides a Merkle proof that validates the correct exit leaf in the global exit root.

6. The unified bridge contract validates the caller's Merkle proof against the global exit root. If the proof is valid, the bridging process succeeds; otherwise, the transaction fails.

## L2 to L1

1. If a call to `bridgeAsset` or `bridgeMessage` on L2 passes validation, the unified bridge contract appends an exit leaf to the L2 exit tree and computes the new L2 exit tree root.

2. The L2 global exit root manager appends the new L2 exit tree root to the global exit tree and computes the global exit root. At that point, the caller's bridge transaction is included in one of the batches selected and sequenced by the sequencer.

3. The aggregator generates a zk-proof attesting to the computational integrity in the execution of sequenced batches which include the transaction.

4. For verification purposes, the aggregator sends the zk-proof together with all relevant batch information that led to the new L2 exit tree root (computed in step 2), to the verifier contract.

5. The verifier contract utilizes the `verifyBatches` function to verify validity of the received zk-proof. If valid, the contract sends the new L2 exit tree root to the global exit root manager in order to update the global exit tree.

6. `claimMessage` or `claimAsset` is then called on the unified bridge contract with Merkle proofs for correct validation of exit leaves.

7. The unified bridge contract retrieves the global exit root from the L1 global exit root manager and verifies validity of the Merkle proof. If the Merkle proof is valid, the settlement completes, otherwise, the transaction is reverted.

## L2 to L2

1. When a batch of transactions is processed, the bridge contract appends the L2 exit tree with a new leaf containing the batch information. This updates the L2 exit tree root.

2. The bridge contract communicates the L2 exit tree root to the L2 global exit root manager. The L2 global exit root manager, however, does not update the global exit tree at this stage.

3. For proving and verification, the zk-proof-generating circuit obtains the L2 exit tree root from the L2 global exit root manager.

4. Only after the batch has been successfully proved and verified does the L2 global exit root manager append the L2 exit tree root to the global exit tree. As a result, the global exit root is updated.

5. The zk-proof-generating circuit also writes the L2 exit tree root to the mainnet. The L1 bridge contract can then finalize the transfer by using the `claim` function.