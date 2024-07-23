---
comments: true
---

This document shows you how to migrate from fork 7 to fork 9 using the Kurtosis package.

!!! tip
    These steps are similar to a production build, except you have to use a [timelock](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v5.0.1-rc.2-fork.8/contracts/PolygonZkEVMTimelock.sol) contract to make the calls.

## Prerequisite steps and set up

1. Run a clean command to remove any lingering state:

    ```sh
    kurtosis clean --all
    ```

2. Downgrade all the necessary parameters to switch back to fork 7. Open the `params.yml` file and make the following changes:

    ```diff
    diff --git a/params.yml b/params.yml
    index 175619f..a72d452 100644
    --- a/params.yml
    +++ b/params.yml
    @@ -29,13 +29,13 @@ args:
    deployment_suffix: "-001"

    # Docker images and repositories used to spin up services.
    -  zkevm_prover_image: hermeznetwork/zkevm-prover:v6.0.0
    +  zkevm_prover_image: hermeznetwork/zkevm-prover:v4.0.19

    -  zkevm_node_image: 0xpolygon/cdk-validium-node:0.6.4-cdk.2
    +  zkevm_node_image: 0xpolygon/cdk-validium-node:0.5.13-cdk.3

    -  zkevm_da_image: 0xpolygon/cdk-data-availability:0.0.7
    +  zkevm_da_image: 0xpolygon/cdk-data-availability:0.0.6

    zkevm_contracts_image: leovct/zkevm-contracts # the tag is automatically replaced by the value of /zkevm_rollup_fork_id/
    @@ -160,7 +160,7 @@ args:
    zkevm_rollup_chain_id: 10101

    # The fork id of the new rollup. It indicates the prover (zkROM/executor) version.
    -  zkevm_rollup_fork_id: 9
    +  zkevm_rollup_fork_id: 7
    ```

3. Now kick-off a full redeploy:

    ```sh
    kurtosis run --enclave cdk-v1 --args-file params.yml --image-download always .
    ```

4. Confirm onchain that fork 7 is running:

    ```sh
    kurtosis files download cdk-v1 genesis /tmp/fork-7-test
    cast call \
        --rpc-url "$(kurtosis port print cdk-v1 el-1-geth-lighthouse rpc)" \
        "$(jq -r '.L1Config.polygonRollupManagerAddress' /tmp/fork-7-test/genesis.json)" \
        "rollupIDToRollupData(uint32)(address,uint64,address,uint64,bytes32,uint64,uint64,uint64,uint64,uint64,uint64,uint8)" 1
    ```

    Should you see `7` showing as the 4th parameter.

5. Send some test transactions to ensure batches are verified as expected.

    ```sh
    export ETH_RPC_URL="$(kurtosis port print cdk-v1 zkevm-node-rpc-001 http-rpc)"
    cast send --legacy --private-key "$(yq -r .args.zkevm_l2_admin_private_key params.yml)" --value 0.01ether 0x0000000000000000000000000000000000000000
    cast rpc zkevm_batchNumber
    cast rpc zkevm_virtualBatchNumber
    cast rpc zkevm_verifiedBatchNumber
    ```

After a few minutes, the number of verified batches should increase (the first batch checked does not count).

## Make a clean stop of the sequencer

1. Before attempting the upgrade, we need to make a clean stop of the sequencer. To do this, pick a halting batch number by updating the `node-config.toml` file like this. Make sure to pick a batch number higher than the current batch number!

    ```sh
    cast to-dec $(cast rpc zkevm_batchNumber | sed 's/"//g')
    ```

    ```diff
    diff --git a/templates/trusted-node/node-config.toml b/templates/trusted-node/node-config.toml
    index 6c9b9fa..372d904 100644
    --- a/templates/trusted-node/node-config.toml
    +++ b/templates/trusted-node/node-config.toml
    @@ -117,7 +117,7 @@ StateConsistencyCheckInterval = "5s"
                    BatchMaxDeltaTimestamp = "20s"
                    L2BlockMaxDeltaTimestamp = "4s"
                    ResourceExhaustedMarginPct = 10
    -                HaltOnBatchNumber = 0
    +                HaltOnBatchNumber = 64
                    SequentialBatchSanityCheck = false
                    SequentialProcessL2Block = true
            [Sequencer.StreamServer]
    ```

2. Re-run Kurtosis:

    ```sh
    kurtosis run --enclave cdk-v1 --args-file params.yml --image-download always .
    ```

3. Wait for the sequencer to halt and the verified batch to equal the latest batch and check the logs.

    ```sh
    kurtosis service logs cdk-v1 zkevm-node-sequencer-001 --follow
    ```

    You should see error logs that look like this:

    ```json
    {"level":"error","ts":1711481674.517157,"caller":"sequencer/finalizer.go:806","msg":"halting finalizer, error: finalizer reached stop sequencer on batch number: 64%!(EXTRA string=\n/home/runner/work/cdk-validium-node/cdk-validium-node/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()\n/home/runner/work/cdk-validium-node/cdk-validium-node/log/log.go:251 github.com/0xPolygonHermez/zkevm-node/log.Errorf()\n/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:806 github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).Halt()\n/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/batch.go:221 github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).closeAndOpenNewWIPBatch()\n/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/batch.go:163 github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).finalizeWIPBatch()\n/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:330 github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).finalizeBatches()\n/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:166 github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).Start()\n)","pid":7,"version":"v0.1.0","stacktrace":"github.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).Halt\n\t/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:806\ngithub.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).closeAndOpenNewWIPBatch\n\t/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/batch.go:221\ngithub.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).finalizeWIPBatch\n\t/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/batch.go:163\ngithub.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).finalizeBatches\n\t/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:330\ngithub.com/0xPolygonHermez/zkevm-node/sequencer.(*finalizer).Start\n\t/home/runner/work/cdk-validium-node/cdk-validium-node/sequencer/finalizer.go:166"}
    ```

4. Wait for the verified batch number to catch up to the trusted batch number:

    ```sh
    export ETH_RPC_URL="$(kurtosis port print cdk-v1 zkevm-node-rpc-001 http-rpc)"
    cast rpc zkevm_batchNumber
    cast rpc zkevm_verifiedBatchNumber
    ```

5. When those two numbers are the same, stop the services that are going to be upgraded:

    ```sh
    kurtosis service stop cdk-v1 zkevm-executor-pless-001
    kurtosis service stop cdk-v1 zkevm-node-aggregator-001
    kurtosis service stop cdk-v1 zkevm-node-eth-tx-manager-001
    kurtosis service stop cdk-v1 zkevm-node-l2-gas-pricer-001
    kurtosis service stop cdk-v1 zkevm-node-rpc-001
    kurtosis service stop cdk-v1 zkevm-node-rpc-pless-001
    kurtosis service stop cdk-v1 zkevm-node-sequence-sender-001
    kurtosis service stop cdk-v1 zkevm-node-sequencer-001
    kurtosis service stop cdk-v1 zkevm-node-synchronizer-001
    kurtosis service stop cdk-v1 zkevm-node-synchronizer-pless-001
    kurtosis service stop cdk-v1 zkevm-prover-001
    ```

## Smart contract calls

1. From another directory, make the required smart contract calls (this should not be done from the `kurtosis-cdk` directory):

    ```sh
    git clone git@github.com:0xPolygonHermez/zkevm-contracts.git
    pushd zkevm-contracts/
    git reset --hard a38e68b5466d1997cea8466dbd4fc8dacd4e11d8
    npm install
    printf "[profile.default]\nsrc = 'contracts'\nout = 'out'\nlibs = ['node_modules']\n" > foundry.toml
    forge build
    ```

2. Deploy a new verifier.

    !!! tip
        This step isn't strictly necessary but good to do because in some cases you need a new verifier contract.

    ```sh
    forge create \
        --json \
        --rpc-url "$(kurtosis port print cdk-v1 el-1-geth-lighthouse rpc)" \
        --private-key 0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625 \
        contracts/mocks/VerifierRollupHelperMock.sol:VerifierRollupHelperMock > verifier-out.json
    ```

3. Create the `PolygonValidiumStorageMigration` contract:

    ```sh
    export ETH_RPC_URL="$(kurtosis port print cdk-v1 el-1-geth-lighthouse rpc)"
    ger="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .polygonZkEVMGlobalExitRootAddress /opt/zkevm/combined.json" | tail -n +2)"
    pol="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .polTokenAddress /opt/zkevm/combined.json" | tail -n +2)"
    bridge="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .polygonZkEVMBridgeAddress /opt/zkevm/combined.json" | tail -n +2)"
    mngr="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .polygonRollupManager /opt/zkevm/combined.json" | tail -n +2)"
    forge create \
        --json \
        --private-key 0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625 \
        contracts/v2/consensus/validium/migration/PolygonValidiumStorageMigration.sol:PolygonValidiumStorageMigration \
        --constructor-args $ger $pol $bridge $mngr > new-consensus-out.json
    ```

4. Add a new rollup type to the rollup manager:

    ```sh
    genesis="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .genesis /opt/zkevm/combined.json" | tail -n +2)"
    cast send \
        --json \
        --private-key 0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625 \
        $mngr \
        'addNewRollupType(address,address,uint64,uint8,bytes32,string)' \
        "$(jq -r '.deployedTo' new-consensus-out.json)" \
        "$(jq -r '.deployedTo' verifier-out.json)" \
        9 0 "$genesis" 'test!!!' > add-rollup-type-out.json
    ```

5. Get your new rollup type id:

    ```sh
    jq -r '.logs[0].topics[1]' add-rollup-type-out.json
    ```

6. Update the rollup with the id:

    ```sh
    rollup="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .rollupAddress /opt/zkevm/combined.json" | tail -n +2)"
    cast send \
        --json \
        --private-key 0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625 \
        $mngr \
        'updateRollup(address,uint32,bytes)' \
        "$rollup" 2 0x > update-rollup-type-out.json
    ```

7. Verify the updated rollupid. Previously the 4th value was a `7` and now it should be a `9`.

    ```sh
    cast call \
        "$(jq -r '.L1Config.polygonRollupManagerAddress' /tmp/fork-7-test/genesis.json)" \
        "rollupIDToRollupData(uint32)(address,uint64,address,uint64,bytes32,uint64,uint64,uint64,uint64,uint64,uint64,uint8)" 1
    ```

8. Set up the data availability protocol again:

    ```sh
    dac="$(kurtosis service exec cdk-v1 contracts-001 "jq -r .polygonDataCommittee /opt/zkevm/combined.json" | tail -n +2)"
    cast send \
        --json \
        --private-key "0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625" \
        "$rollup" 'setDataAvailabilityProtocol(address)' $dac > set-dac-out.json
    ```

## Node upgrade

At this stage, the smart contracts are upgraded. However, we still need to start the nodes again.

!!! warning
    - This procedure is very sensitive.
    - Ensure the synchronizer starts first.

We're going to revert the parameters back to the versions of the node that worked with fork 9, and only redeploy the CDK central/trusted environment.

1. Update the `params.yml` file as follows:

    ```sh
    yq -Y --in-place 'with_entries(if .key == "deploy_cdk_central_environment" then .value = true elif .value | type == "boolean" then .value = false else . end)' params.yml
    ```

2. Remove the `HaltOnBatchNumber` setting that we added earlier.

3. Run Kurtosis to bring up the main node components.

    ```sh
    kurtosis run --enclave cdk-v1 --args-file params.yml --image-download always .
    ```

4. The core services are now running and we should be able to send a transaction and see the batch numbers moving through their normal progression.

    ```sh
    export ETH_RPC_URL="$(kurtosis port print cdk-v1 zkevm-node-rpc-001 http-rpc)"
    cast send --legacy --private-key "$(yq -r .args.zkevm_l2_admin_private_key params.yml)" --value 0.01ether 0x0000000000000000000000000000000000000000
    cast rpc zkevm_batchNumber
    cast rpc zkevm_virtualBatchNumber
    cast rpc zkevm_verifiedBatchNumber
    ```

## Troubleshooting

1. If you clone the `zkevm-contracts` repo in the same folder as `kurtosis-cdk`, you may see this error when you try to deploy the stack:

    ```sh
    Error:  An error occurred running command 'run'
    Caused by: An error occurred calling the run function for command 'run'
    Caused by: An error starting the Kurtosis code execution '.'
    Caused by: Error uploading package '.' prior to executing it
    Caused by: There was an error compressing module '.' before upload
    Caused by: An error occurred creating the archive from the files at '.'
    Caused by: The files you are trying to upload, which are now compressed, exceed or reach 100mb. Manipulation (i.e. uploads or downloads) of files larger than 100mb is currently disallowed in Kurtosis.
    ```

2. You may also see errors like these:

    ```json
    {"level":"warn","ts":1711502381.03938,"caller":"etherman/etherman.go:661","msg":"Event not registered: {Address:0x1Fe038B54aeBf558638CA51C91bC8cCa06609e91 Topics:[0xd331bd4c4cd1afecb94a225184bded161ff3213624ba4fb58c4f30c5a861144a] Data:[0 0 0 0 0 0 0 0 0 0 0 0 90 104 150 169 140 75 124 126 143 22 209 119 199 25 161 216 86 185 21 76] BlockNumber:108 TxHash:0x1bb5e714dd96434ded2d818458cc517cf7b30f5787dbb3aedb667e5e3e96808e TxIndex:0 BlockHash:0xdf5850cd5a8975859595649a05ce245f02953e84af627e9b22a1f8381077f057 Index:0 Removed:false}","pid":7,"version":"0.6.4+cdk"}
    ```

    You can check them directly from the rpc:

    ```sh
    cast logs \
        --rpc-url "$(kurtosis port print cdk-v1 el-1-geth-lighthouse rpc)" \
        --address 0x1Fe038B54aeBf558638CA51C91bC8cCa06609e91 \
        --from-block 108 \
        --to-block 108
    ```

     You can reverse an event with the following script:

    ```sh
    cat compiled-contracts/*.json | jq '.abi[] | select(.type == "event") | .type = "function"' | jq -s | polycli abi decode | grep d33
    cast sig-event 'SetDataAvailabilityProtocol(address)'
    ```

3. In the above example, it looks like the unregistered event is a call to `SetDataAvailabilityProtocol(address)`.
