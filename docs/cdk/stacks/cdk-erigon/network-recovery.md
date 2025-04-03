CDK-erigon supports two simple methods for network recovery:

- Partial L1 recovery; from a partially synced datadir.
- Full L1 recovery; from a completely empty datadir.

## Partial recovery

### Sync limit step

First, find out the following:

- What batch to set as the first batch to start recovering from.
- What is the last block of the batch prior to this. It can be found by querying the RPC or checking the L1 data from the sequencer contract.

Once we know the last block number, we can begin a fresh sync to get to that block height. To do this use the same configuration that you would normally use for the network but add an additional flag in `--zkevm.sync-limit=[block you need + 1]`. 

!!! info "Example"
    In order to sync to block 100, enter `101` for the flag value. 

Let the node run and it eventually sits in a loop at this block height. Once the node reaches the required height, you can stop the node as normal. 

### L1 recovery step

First determine the earliest L1 block height suitable for recovery. 

You can do this by looking for the L1 block number for the earliest transaction against the sequencer contract (found in the cdk-erigon config). 

Once you have the info you need, start the node up with a new flag: `zkevm.l1-sync-start-block=[l1block height]`.

!!! important
    Remove the `zkevm.sync-limit` flag from the previous step at this point if you are running a partial recovery. 
    
It is important to pick the earliest block on the network so that the L1 info tree update events are gathered correctly. If not, you run the risk of the indexes
not lining up.

## Full recovery

Follow the L1 recovery step as above, and use a completely fresh datadir.
