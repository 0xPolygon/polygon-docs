## Summary

!!! warning
    This local migration test doc is work-in-progress and unpublished currently.

These instructions show you how to fully test locally the migration steps from fork 7 to 8.

## Build Docker dev geth with fork 7

1. Clone `zkevm-contracts`, checkout branch `v4.0.0-fork.7`, and install.

    ```sh
    git clone https://github.com/0xPolygonHermez/zkevm-contracts
    cd zkevm-contracts/
    git checkout v4.0.0-fork.7
    npm install
    ```

2. Edit the `docker/scripts/v2/deploy_parameters_docker.json` file to change the following:

    ```json
    "minDelayTimelock": 3600, -> "minDelayTimelock": 1,
    ```

3. Edit the `docker/scripts/v2/create_rollup_parameters_docker.json` file and change `"consensusContract": "PolygonZkEVMEtrog",` to the following:

    ```json
    "consensusContract": "PolygonValidiumEtrog",
    ```

    And add the following parameter:

    ```json
    "dataAvailabilityProtocol": "PolygonDataCommittee",
    ```

4. Run the following command:

    ```sh
    cp docker/scripts/v2/hardhat.example.paris hardhat.config.ts
    ```

5. Edit the `docker/scripts/v2/deploy-docker.sh` file to add the following line:

    ```sh
    sudo chmod -R go+rxw docker/gethData before docker build -t hermeznetwork/geth-zkevm-contracts -f docker/Dockerfile . 
    ```

6. Uncomment the following lines from `deployment/v2/4_createRollup.ts`:

    ```sh
    // Setup data commitee to 0
    await (await polygonDataCommittee?.setupCommittee(0, [], "0x")).wait();
    ```

7. Build the image:

    ```sh
    npm run docker:contracts
    ```

8. Tag the image:

    ```sh
    docker image tag hermeznetwork/geth-zkevm-contracts hermeznetwork/geth-zkevm-contracts:test-upgrade-7
    ```

## Build the genesis file for the node

1. Clone the `cdk-validium-node` repo, `cd` into it, and checkout the `v0.5.13+cdk.6` branch.

    ```sh
    git clone https://github.com/0xPolygon/cdk-validium-node
    cd cdk-validium-node
    git checkout v0.5.13+cdk.6
    ```

2. Edit the `test/config/test.genesis.config.json` file with values in the output files in the `zkevm-contracts/docker/deploymentOutput` directory.
    
    - `l1Config.polygonZkEVMAddress` ==> `rollupAddress` @ create_rollup_output.json
    - `l1Config.polygonRollupManagerAddress` ==> `polygonRollupManager` @ deploy_output.json
    - `l1Config.polTokenAddress` ==> `polTokenAddress` @ deploy_output.json
    - `l1Config.polygonZkEVMGlobalExitRootAddress` ==> `polygonZkEVMGlobalExitRootAddress` @ deploy_output.json
    - `rollupCreationBlockNumber` ==> `createRollupBlock` @ create_rollup_output.json
    - `rollupManagerCreationBlockNumber` ==> `deploymentBlockNumber` @ deploy_output.json
    - `root` ==> `root` @ genesis.json
    - `genesis` ==> `genesis` @ genesis.json

## Run the network using fork 7

1. Build the docker: `make build-docker`.

2. Edit `test/docker-compose.yml` to use the geth image from the first step, replace:   

    - `hermeznetwork/geth-cdk-validium-contracts:v0.0.4` => `hermeznetwork/geth-zkevm-contracts:test-upgrade-7`

3. Run all the stack: `cd test` then `make run`.

4. Send a bunch of txs using metamask:

    - Import private key `0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80` which has funds on L2 since genesis.
    - chainID is 1001
    - port is 8123

## Stop the sequencer in a clean state (no WIP batch) to avoid reorgs

This explained in more detail and orientated to a prod env [here](?)

1. Make sure you are on the test directory

2. Stop sequencer 
        
    ```sh
    docker compose stop zkevm-sequencer && docker compose rm -f zkevm-sequencer`
    ```

3. Connect to StateDB using: 

    ```psql
    psql -h localhost -p 5432 -U state_user state_db
    ```
    then introduce password `state_password`

4. Get WIP batch number: 

    ```sql
    SELECT batch_num, wip FROM state.batch WHERE wip IS true;` 
    ```

!!! danger
    → X. Write down somewhere the value of X, as it's gonna be used ina. bunch of places

5. Edit node config (`test/config/test.node.config.toml`):

6. Change: `Sequencer.Finalizer.HaltOnBatchNumber = X+1 # wip batch_num+1`
    
    For a prod env you may want to tweak other values, see the linked doc above, for the local dev env defaults are ok -> waiting for link

7. Restart sequencer: 
    
    ```sh
    docker compose up -d zkevm-sequencer`
    ```

8. Check sequencer halted when reaching batch X+1 

    ```sh
    docker logs -f zkevm-sequencer`
    ```

9. Wait until all pending batches are virtualized and verified (X). Note that this could be checked on etherscan or using custom RPC endpoint

    ```sql
    SELECT batch_num FROM state.virtual_batch ORDER BY batch_num DESC LIMIT 1; → X
    SELECT batch_num FROM state.verified_batch ORDER BY batch_num DESC LIMIT 1; → X
    ```

10. Stop all the node components: 

    ```sh
    make stop-node && make stop-zkprover`
    ```

## L1 interactions to upgrade CDK to fork 8

On zkevm-contracts, checkout develop: 

    ```sh
    git stash && git checkout develop && npm i`
    ```

### Deploy verifier

1. Run

    ```sh
    cp tools/deployVerifier/deploy_verifier_parameters.example tools/deployVerifier/deploy_verifier_parameters.json`
    ```

2. Edit `tools/deployVerifier/deploy_verifier_parameters.json`:
    
    - `realVerifier` ==> `false`

3. Run 

    ```sh
    cp docker/scripts/v2/hardhat.example.paris hardhat.config.ts`
    ```

4. Deploy verifier: 

    ```sh
    npx hardhat run tools/deployVerifier/deployVerifier.ts --network localhost`
    ```

5. Write the deployed address somewhere (you will only get that on the logs, something similar to `verifierContract deployed to: 0xa85233C63b9Ee964Add6F2cffe00Fd84eb32338f`) 

!!! warning
    On production this step should be skipped, as the fork 8 verifier should already be deployed (since it's already being used by Hermez)

### Add rollup type

1. Edit `tools/addRollupType/add_rollup_type.json` using values from the output files @ `docker/deploymentOutputs`

    - `consensusContract` ==> `PolygonValidiumEtrog`
    - `polygonRollupManagerAddress` ==> `polygonRollupManager` @ deploy_output.json
    - `polygonZkEVMBridgeAddress` ==> `polygonZkEVMBridgeAddress` @ deploy_output.json
    - `polygonZkEVMGlobalExitRootAddress` ==> `polygonZkEVMGlobalExitRootAddress` @ deploy_output.json
    - `polTokenAddress` ==> `polTokenAddress` @ deploy_output.json
    - `verifierAddress` ==> value outputed on the logs of previous step
    - `timelockDelay` ==> `0`

2. Run 

    ```sh
    npx hardhat run tools/addRollupType/addRollupType.ts --network localhost
    ``` 
    
    should output: Added new Rollup Type deployed

3. Write the type ID (you will only get that on the logs, something similar to `type: 2`,)  THIS IS INCORRECT, LoL. Need a better way to detect the correct typeID

!!! warning
    The procedure is not the same when using timelocks!

### Update rollup

1. Run

    ```sh
    cp tools/updateRollup/updateRollup.json.example tools/updateRollup/updateRollup.json`
    ```

2. Edit `tools/updateRollup/updateRollup.json` using values from the output files @ docker/deploymentOutputs:

    - `rollupAddress` ==> `rollupAddress` @ create_rollup_output.json
    - `newRollupTypeID` ==> value outputed on the logs of previous step (put 2 if running with docker as per the instructions)
    - `polygonRollupManagerAddress` ==> `polygonRollupManager` @ deploy_output.json
    - `timelockDelay` ==> `minDelayTimelock` @ docker/scripts/v2/deploy_parameters_docker.json
    - (ADD) `timelockAddress` ==> `timelockContractAddress` @ deploy_output.json
    
#### With timelock (NOT TESTED)

1. Run 

    ```sh
    npx hardhat run tools/updateRollup/updateRollup.ts --network localhost`
    ```

2. Create `tools/updateRollup/executeUpdate.ts` and `tools/updateRollup/scheduleUpdate.ts`

3. Run 

    ```sh
    npx hardhat run tools/updateRollup/scheduleUpdate.ts --network localhost`
    ```

4. Wait for the timelock delay to be elapsed (just one second )

5. Run 

    ```sh
    npx hardhat run tools/updateRollup/executeUpdate.ts --network localhost`
    ```

#### Without timelock

1. Create `tools/updateRollup/noTimelock.ts`

2. Run 

    ```sh
    npx hardhat run tools/updateRollup/noTimelock.ts --network localhost` 
    ```

3. Missing to implement something to verify that the tx went through…??

!!! warning
    After upgrade, the dataAvailabilityProtocol of the Validium contract is lost (set to 0x000…0), needed to set it up again using the script at the bottom of the doc

## Upgrade node to fork 8

!!! tip
    It is recommended to have log level set to debug until the upgrade is confirmed to be succesful

1. Make sure you are on the root directory of `cdk-validium-node`

2. Backup the genesis file so no need to re-write it: 

    ```sh
    cp test/config/test.genesis.config.json /tmp`
    ```

3. Update node version: 

    ```sh
    git stash && git checkout v0.6.2+cdk`
    ```

4. Build docker (on root directory): 

    ```sh
    make build-docker`
    ```

5. Backup genesis file: 

    ```sh
    mv /tmp/test.genesis.config.json test/config`
    ```

6. Run the synchronizer: 

    ```sh
    cd test && make run-zkprover && docker compose up -d zkevm-sync`
    ```

7. Connect to StateDB using: 

    ```sql
    psql -h localhost -p 5432 -U state_user state_db,
    ```
     then introduce password `state_password`

8. Query the registered fork IDs: 

    ```sql
    SELECT * FROM state.fork_id;
    ``` 
    You should get two rows, one with 7 and the other with 8 (it may take a bit)

9. Start the rest of the node components: 

    ```sh
    make run-node
    ```
    
10. Send a bunch of transactions using metamask

11. Wait until new batches are virtualized and verified (> X). Note that this could be checked on etherscan or using custom RPC endpoint

    ```sql
    SELECT batch_num FROM state.batch ORDER BY batch_num DESC LIMIT 1; → > X
    SELECT batch_num FROM state.virtual_batch ORDER BY batch_num DESC LIMIT 1; → > X
    SELECT batch_num FROM state.verified_batch ORDER BY batch_num DESC LIMIT 1; → > X
    ```