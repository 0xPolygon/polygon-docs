This document shows Polygon partners how to migrate an isolated CDK stack.

## Process to upgrade forks for isolated CDK chains

In order to avoid reorgs and other undesirable scenarios, all L2 transactions must be verified before upgrading a fork. Verification means that all batches are closed, sequenced, and verified on L1.

Follow the steps to verify all batches for upgrading.

1. Stop the sequencer.
2. Enforce the sequencer to stop at a specific `batch_num`.

    1. In the statedb, get WIP batch number: 
        
        `SELECT batch_num, wip FROM state.batch WHERE wip IS true;` 
        
        Result = X (write down X for later)

    2. Edit node config:

        1. `Sequencer.Finalizer.HaltOnBatchNumber = X+1`
        2. `Sequencer.BatchMaxDeltaTimestamp = “120s” # 1800s`
        3. `SequenceSender.WaitPeriodSendSequence = "10s" # 60s`
        4. `SequenceSender.LastBatchVirtualizationTimeMaxWaitPeriod = “30s” # 600s`

    3. Restart sequencer, sequence-sender.

    4. Check sequencer halted when reaching batch `X+1` (this is obvious in the logs).

    5. Wait until all pending batches are virtualized (X): 

        `SELECT batch_num FROM state.virtual_batch ORDER BY batch_num DESC LIMIT 1;` → X

    6. Wait until the aggregator has aggregated proofs for all the batches:

        1. `SELECT batch_num FROM state.verified_batch ORDER BY batch_num DESC LIMIT 1;` → Y (if Y == X) you can skip next steps until `3. Prepare (**do not apply**) new versions according to the version matrix`

        2. `SELECT batch_num, batch_num_final FROM state.proof WHERE NOT generating AND batch_num = Y AND batch_num_final = X` wait until this query returns a row, remove `WHERE` conditions to get a sense of progress.

    7. Edit node config to force the aggregator into sending the already aggregated proof ASAP: 

        `Aggregator.VerifyProofInterval = "5m”`. Then restart aggregator.

    8. Wait until the proof is settled on-chain: 

        `SELECT batch_num FROM state.verified_batch ORDER BY batch_num DESC LIMIT 1;` → X

3. Prepare (**do not apply**) new versions according to the version matrix.

4. Stop all services (node, prover/executor, bridge).

## Update software

1. Start synchronizer's new version.

2. Wait until synchornizer receives a fork id event (check table `state.fork_id`).

3. Edit node config file (node v0.6.2 version):

    1. `Sequencer.Finalizer.HaltOnBatchNumber = 0`

4. Start all node components, executors, provers, and bridge with new versions.

5. Check batches ≥ X are virtualized and verified.

6. Edit new node config (restore previous values):

    1. `Aggregator.VerifyProofInterval = "25m”` # restore previous value
    2. `Sequencer.BatchMaxDeltaTimestamp = “1800s”`
    3. `SequenceSender.WaitPeriodSendSequence = "60s”` # restore previous value
    4. `SequenceSender.LastBatchVirtualizationTimeMaxWaitPeriod = “600s”` # restore previous value
    
7. Restart sequencer, sequence-sender, and aggregator.
