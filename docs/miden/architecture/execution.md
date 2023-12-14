Polygon Miden is an Ethereum rollup. It batches transactions - or more precisely, proofs thereof - that happen together in the same time period into a block. The execution model describes how the state progresses on an individual level via transactions and at the global level expressed as aggregated state updates in blocks.

<center>
![Execution](../../img/miden/architecture/execution/execution.png){ width="80%" }
</center>

## Transaction execution

Every transaction will result in a zkProof that attests to its correctness.

As mentioned in [transactions](transactions.md), there are two types of transactions: local and network. For every transaction there is a proof which is either created by the user in the Miden Client or by the Operator using the Miden Node.

## Transaction batching

To reduce the required space on the Ethereum blockchain, transaction proofs are aggregated into batches. This can happen in parallel by different machines that need to verify several proofs using the Miden VM and thus creating a proof. Verifying a STARK proof within the VM is relatively efficient but it is still a pretty costly operation (we aim for 2<sup>16</sup> cycles).

## Block production

Several batch proofs are being aggregated together into one block. This can not happen in parallel and must be done by the Miden Operator running the Miden Node. The idea is the same, using recursive verification.

## State progress

At the beginning, Miden will have a centralized operator running a Miden node.

Users will send either transaction proofs (using local execution) or transaction data (for network execution) to the Miden Node. Later on, the Miden Node will use recursive verification to aggregate transaction proofs into batches.

Batch proofs are aggregated into blocks by the Miden Node. The blocks are then sent to Ethereum, and once a block is added to the L1 chain, the rollup chain is believed to have progressed to the next state.

A block produced by the Miden Node looks somewhat like this:

<center>
![Block](../../img/miden/architecture/execution/block.png)
</center>

* State updates contain only the hashes of changes. For example, for each account which was updated, we record a tuple `([account id], [new account hash])`.
* The included zkProof attests that given a state commitment from the previous block, there was a sequence of valid transactions executed that resulted in the new state commitment, and also output included state updates.
* The block also contains full account and note data for public accounts and notes. For example, if account `123` is a public account which was updated, in the state updates section we'd have a records for it as `(123, 0x456..)`. The full new state of this account (which should hash to `0x456..`) would be included in a separate section.

To verify that a block describes a valid state transition, we do the following:

1. Compute hashes of public account and note states.
2. Make sure these hashes match records in the *state updates* section.
3. Verify the included ZKP against the following public inputs:
   - State commitment from the previous block.
   - State commitment from the current block.
   - State updates from the current block.

The above can be performed by a verifier contract on Ethereum L1.

This structure has another nice property. It is very easy for a new node to sync up to the current state from genesis. The new node would need to do the following:

1. Download only the first part of the blocks (i.e., without full account/note states) starting at the genesis up until the latest block.
2. Verify all zkProofs in the downloaded blocks. This will be super quick (exponentially faster than re-executing original transactions) and can also be done in parallel.
3. Download the current states of account, note, and nullifier databases.
4. Verify that the downloaded current state matches the state commitment in the latest block.

Overall, state sync is dominated by the time needed to download the data.
