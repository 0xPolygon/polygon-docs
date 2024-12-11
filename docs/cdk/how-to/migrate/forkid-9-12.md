> 💡 For CDK fork ID9 chains **NOT attached to the AggLayer** (Isolated), they can ignore section 4.

> 💡 For CDK fork ID9 chains **attached to the AggLayer**, follow steps in sections 1 to 5. This is a coordinated effort between Polygon and the Implementation Provider.

## 1. Summary of the Procedure

To initiate a CDK chain upgrade, the Implementation Provider can request support from Polygon by submitting the "*Request Help for an Issue with an Existing CDK Chain*" through the [service desk](https://cdk.polygon.technology/).

| ![CDK Service Desk](https://raw.githubusercontent.com/0xPolygon/polygon-docs/a8eee02f74ed28011ccaec99ae73b5b95d768b87/docs/img/cdk/Service-desk-screenshot.png) | ![Example Request](https://raw.githubusercontent.com/0xPolygon/polygon-docs/a8eee02f74ed28011ccaec99ae73b5b95d768b87/docs/img/cdk/Example-request-screenshot.png) |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **CDK Service Desk**| **Example Request**|

Polygon will then collaborate with the Implementation Provider to **schedule** the UTC timing and dates for the upgrade.

This planning enables the Implementation Provider to schedule testnet and mainnet maintenance windows for the respective networks, ensuring proper communication and coordination with their communities.

See [Example Maintenance Communication to Network Partners](#example-maintenance-communication-to-network-partners) Implementation Providers can prepare for the customer network chains.

The high-level steps in the collaborative process are:

1. Implementation Provider halting the sequencer,
2. Polygon executes the upgrade transaction,
3. Implementation Provider upgrades components to Fork 12 stack,
4. Implementation Provider restarts the components.

## 2. CDK Components Versions

Please read carefully to fully understand the new architecture before starting the process: [https://docs.polygon.technology/cdk/getting-started/cdk-erigon/](https://docs.polygon.technology/cdk/getting-started/cdk-erigon/)

The table below lists the CDK Fork ID 9 components and the new CDK FEP Fork ID 12 components.

> 💡 **Please note:** Latest CDK FEP Fork ID 12 components are listed in the [Polygon Knowledge Layer](https://docs.polygon.technology/cdk/releases/stack-components/#cdk-fep-components)

| **CDK Components**                         | **Fork ID 9**                                                                                                                                            | **CDK Components**                         | **Fork ID 12**                                                                                                            |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| CDK Validium node<br>Sequence sender<br>Aggregator | [0.6.7+cdk.1](https://hub.docker.com/layers/0xpolygon/cdk-validium-node/0.6.7-cdk.1/images/sha256-dafb15f9355331b4b7174f47ac416b275915ff24a9ed89c211c7c15c8adfc6b8?context=explore) | CDK Erigon RPC & CDK node                 | [cdk-erigon:v2.1.x](https://github.com/0xPolygonHermez/cdk-erigon/releases) |
|                                            |                                                                                                                   | CDK node<br>Sequence sender<br>Aggregator | [cdk:v0.3.x](https://github.com/0xPolygonHermez/cdk-erigon/releases)                                                                                                                 |
| Tx pool manager                            | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager)                                                                                    | Tx pool manager                            | [zkevm-pool-manager](https://github.com/0xPolygon/zkevm-pool-manager) use latest tag                                                   |
| Prover                                     | [v6.0.0](https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v6.0.0)                                                                            | Prover                                     | [zkevm-prover v8.0.0-RC14](https://hub.docker.com/r/hermeznetwork/zkevm-prover/tags)                                                                            |
| CDK data availability                      | [v0.0.7](https://hub.docker.com/layers/0xpolygon/cdk-data-availability/0.0.7/images/sha256-17590789a831259d7a07d8a042ea87e381c5708dec3a7daef6f3f782f50b2c00?context=explore) | CDK data availability                      | [cdk-data-availability](https://github.com/0xPolygon/cdk-data-availability) use latest tag                                       |
| zkEVM rollup node                          | [v6.0.0](https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v6.0.0)                                                                            | zkEVM rollup node                          | N/A                                                                                                                       |
| Contracts                                  | [v6.0.0](https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v6.0.0-rc.1-fork.9)                                                             | Contracts                                  | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v8.0.0-fork.12)                                                   |
| Bridge service                             | [v0.4.2-cdk.1](https://hub.docker.com/layers/hermeznetwork/zkevm-bridge-service/v0.4.2-cdk.1/images/sha256-f22ad8c9ad058c7a97a3d38f53cac5b1053858916523b96211d33ae40a9b45f8?context=explore) | Bridge service                             | [zkevm-bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service)                                           |
| Bridge UI                                  | [Polygon Portal](https://portal.polygon.technology/)                                                                                                     | Bridge UI                                  | [Polygon Portal](https://portal.polygon.technology/)                                                                      |

## 3. Implementation Provider Preparation Steps

The Implementation Provider must prepare in advance for the upgrade to ensure a smooth transition from fork ID 9 to fork ID 12. Failure to complete these steps ahead of time could result in delays or even cancellation of the scheduled upgrade.

1. The Implementation Provider downloads [CDK Fork 12 components](https://docs.polygon.technology/cdk/releases/stack-components/#cdk-fep-components) in advance so they are ready to deploy.
2. Map to the latest prover files which can be found here: [https://storage.googleapis.com/zkevm/zkproverc/v8.0.0-rc.9-fork.12.tgz](https://storage.googleapis.com/zkevm/zkproverc/v8.0.0-rc.9-fork.12.tgz)
3. Scale up the number of provers in advance. It is recommended that you at least double the number of provers up and running for the scheduled upgrade maintenance window.
    - Ensure all (majority) of the network batches are verified before starting the upgrade process, otherwise there will be additional downtime as we wait for the network to be ready.
4. Setting up your CDK Erigon node.
    - Please see the [cdk-erigon readme](https://github.com/0xPolygonHermez/cdk-erigon/blob/v1.0.3/README.md) for information on prereqs, configuration files and running cdk-erigon.
5. Required CDK-Node pre syncing.
   - Run CDK-Node aggregator component in sync only mode in advance to populate its database.
   - Run CDK-Node l1infotreesync component in advance to populate the sequence sender database.
7. Required Erigon pre-syncing:
    - Generate data stream files from the current `cdk-validium-node` database.
        - Tool and instructions can be found here:  
            - [https://github.com/0xPolygonHermez/zkevm-node/tree/develop/tools/datastreamer](https://github.com/0xPolygonHermez/zkevm-node/tree/develop/tools/datastreamer)
    - Use the Erigon tool (from `cdk-erigon` repo) to serve the DS:
        - `go run ./zk/debug_tools/datastream-host --file /path/to/directory`
        - Start CDK-Erigon, which reads from this datastream (provide `zkevm.l2-datastreamer-url: 127.0.0.1:6900` in the config).
    - Wait for it to sync to the tip.
    - CDK-Erigon can be stopped. The generated files will be used later during the upgrade process.

The whole process should look more or less like this:
```bash
# PREREQUISITES: Install GO 1.23
WORK_DIR=/tmp

cd $WORK_DIR
git clone https://github.com/0xPolygonHermez/zkevm-node.git
cd $WORK_DIR/zkevm-node/tools/datastreamer
vim config/tool.config.toml
# Edit [StateDB] section with your StateDB credentials
make generate-file

cd $WORK_DIR
git clone https://github.com/0xPolygonHermez/cdk-erigon.git
cd $WORK_DIR/cdk-erigon
go run ./zk/debug_tools/datastream-host \
    --file $WORK_DIR/zkevm-node/tools/datastreamer/datastream

# Bring up Erigon pointing to that DS (localhost:6900 if running locally)
# and let it fully sync to the end of the DS.
```

## 4. Polygon Preparation Steps

1. Polygon will collaborate with the Implementation Provider to **schedule** the UTC timing and dates for the upgrade, incorporating required timelocks.
2. Polygon will set up Google Meet calls between Polygon and the Implementation Provider's engineers to conduct planned upgrades for both testnet and mainnet on agreed dates.
3. Polygon will prepare in advance and with agreed timelock:
    - Rolluptype for fork 12
    - Upgrade transaction to fork 12
4. For chains attached to the Polygon Agglayer, Polygon will handle steps to upgrade the permissionless node.
5. [See example communication](#example-maintenance-communication-to-network-partners) that Implementation Providers can use to prepare their customer network partners and communities.

## 5. Operational Steps

**Please Note:** To avoid creating reorgs or other unwanted situations, it's important that all L2 transactions are verified before performing a fork upgrade. This means all batches should be closed, sequenced, and verified on L1.

### Steps to Halt the Sequencer
> 💡 Please note: For an isolated chain not attached to the Agglayer the chain admin can  perform operational step 4 on their chain’s rollupmanagercontract. 
Polygon are not involved. Please check the [upgrade procedure for isolated networks](#contract-upgrade-procedure-for-isolated-networks).

 
1. Stop the sequencer.
2. Reconfigure the node to enforce sequencer stops at a specific `batch_num`:
    - Get the current batch number from StateDB:
    
    ```sql
    -- Note resulting value as X:
    SELECT batch_num, wip FROM state.batch WHERE wip IS true;
    ```
    
    - Edit node configuration:
    
    ```yaml
    # SEQUENCER CONFIG
    # Where X is the batch number obtained from the SQL query:
    Sequencer.Finalizer.HaltOnBatchNumber = X+1
    # Optional: Reduce batch time to avoid excessive downtime
    Sequencer.Finalizer.BatchMaxDeltaTimestamp = "120s" # 1800s
    ```
    
    ```yaml
    # SEQUENCE SENDER CONFIG
    # Optional: Reduce sending time to avoid excessive downtime
    SequenceSender.WaitPeriodSendSequence = "10s" # 60s
    SequenceSender.LastBatchVirtualizationTimeMaxWaitPeriod = "30s" # 600s
    ```
    
    ```yaml
    # AGGREGATOR CONFIG
    # Recommended: Reduce verify interval to avoid excessive downtime
    Aggregator.VerifyProofInterval = "5m"
    ```
    
    - Restart the sequencer, sequence sender, and aggregator to apply these configs.
    - Check that the sequencer halts when reaching batch X+1.
    - Wait until all pending batches are virtualized and verified (X):
    
    ```sql
    -- Both queries should return X
    SELECT max(batch_num) FROM state.virtual_batch;
    SELECT max(batch_num) FROM state.verified_batch;
    ```
    
3. Stop all services (node, prover/executor, bridge).

4. **Polygon:** Upgrade the Smart Contract (multisig):
    - Upgrade rollup to fork 12.
    - Wait for the Tx to be finalized.

**Please Note:** Wait for Polygon to send the L1 transaction (tx) and confirm it.

### Steps to Deploy CDK FEP Fork 12 Components
1. It is recommended to back up your DAC node by taking a snapshot of the DAC database.
     -  **Locate Your PostgreSQL Instance**:
         - Identify the PostgreSQL host, port, database name (`dac_db`), and the username (`master_user`) configured for your DAC node. These values can typically be found in your environment's configuration or `.env` files.
        -  **Run the `pg_dump` Command**:
           -  Use the `pg_dump` command to create a backup of your DAC database. Replace the placeholders with your specific values:
           -  pg_dump -U master_user -d dac_db -h 127.0.0.1 -p 5432 > dac.db.sql
        -  **Verify the Backup**:
           -  After running the command, ensure that the `dac.db.sql` file has been created and contains the database snapshot.

2. [With the network stopped, repeat Erigon sync to get it fully synced to the current state.](#5-operational-steps)
    - This instance is ready to act as Sequencer and/or RPC. Clone the whole Erigon config/datadir as many times as instances are needed. Pick one to be the new Sequencer (by setting the environment variable **`CDK_ERIGON_SEQUENCER=1`**), and configure all other instances (permissionless RPCs) to point to the Sequencer:
    
    ```yaml
    zkevm.l2-sequencer-rpc-url: "http://sequencer-fqdn-or-ip:8123"
    zkevm.l2-datastreamer-url: "sequencer-fqdn-or-ip:6900"
    ```
    
3. Start the stateless Executor.
4. Start CDK-Erigon Sequencer
    - On a fork upgrade, once the upgrade Tx is finalized you can start the sequencer. Once started, check logs and ensure new blocks are generated with new forkid.
        - You would expect to see starting block #5796790 as forkid 12. If you see the starting block 5796790 as fork id 9 there is a problem.
        If the new block is on the old fork id 9, you need to resync sequencer from scratch or get one of the rpc datadirs (that were synced till the halt and are currenctly stopped) and replace it to become the new sequencer.
6. Verify in the sequencer’s logs that new blocks are being generated with fork ID 12.
7. Start the Pool Manager (if used/needed).
8. Start CDK-Erigon RPCs (if used/needed).
9. Start the Bridge.
10. Start the CDK aggregator and Sequence Sender components.
11. Start the stateless Prover.

### Polygon Steps for CDK Chains Attached to the Agglayer

Polygon's DevOps team will be accountable for upgrading the Agglayer permissionless nodes during the upgrade process.

### Post-Upgrade Validations

1. Test batch lifecycle.
2. Test the bridge.



# Example Maintenance Communication to Network Partners

There is a planned maintenance window upgrade of the xxxx network on the following dates. This is to upgrade the xxx network from Fork ID9 to Fork ID12.

**Maintenance Event:**  xxx Network Upgrade from Fork ID9 to Fork ID12

**Date:** TBD by Implementation Provider

**Time:** 00:00 PM EDT / 00:00 PM UTC

**Duration:** 2 Hours

**Things to Note:**

- This upgrade is from Fork ID9 to Fork ID12. The change log can be viewed [here](https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v8.0.0-rc.1-fork.12).
- Partners should **not update their nodes until after** the xxx network upgrade is confirmed as complete.
- New Node Version: [cdk-erigon:v2.1.x](https://github.com/0xPolygonHermez/cdk-erigon/releases)

### Upgrade Instructions for Community Partners (Testnet/Mainnet)

Update FROM node version [0.6.7+cdk.1](https://hub.docker.com/layers/0xpolygon/cdk-validium-node/0.6.7-cdk.1/images/sha256-dafb15f9355331b4b7174f47ac416b275915ff24a9ed89c211c7c15c8adfc6b8?context=explore) up to [cdk-erigon:v2.1.x](https://github.com/0xPolygonHermez/cdk-erigon/releases).

#### Instructions to Update Nodes

1. Stop the RPC, Synchronizer, and Executor components.
2. Update the node (RPC and Synchronizer) to [cdk-erigon:v2.1.x](https://github.com/0xPolygonHermez/cdk-erigon/releases).
3. Update the Prover/Executor to [v8.0.0-RC12-fork.12](https://hub.docker.com/layers/hermeznetwork/zkevm-prover/v8.0.0-RC12-fork.12/images/sha256-7657c7ac473acd4f67ab6de81bb61595a1d52c97287bb2d043bff235a4803a66?context=explore).
4. Start the components in this order:
    1. Prover/Executor
    2. Synchronizer
    3. RPC




# Contract Upgrade procedure for isolated networks
## Resources

- [rollup-manager-cli](https://github.com/0xPolygonHermez/rollup-manager-cli)
    - get L1 information easily
- [tool deploy verifiers](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/tools/deployVerifier)
- [tool add new rollup type](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/tools/addRollupType)

> For fork.12 upgrades, it is need to upgrade PolygonZkEVMGlobalExitRootV2 and the PolygonRollupManager. Please refer to [the Upgrade Banana SC section](https://www.notion.so/CDK-chain-upgrade-procedure-from-Fork-ID9-to-Fork-ID12-11980500116a802ab22cec6f7eea6080?pvs=21) in order to do the SCs upgrade
> 

## Verifier

- Go to the correct branch(or tag) in [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts)
    - [main](https://github.com/0xPolygonHermez/zkevm-contracts) for fork.10 & fork.11
    - [develop](https://github.com/0xPolygonHermez/zkevm-contracts/tree/develop) for fork.12 (AKA Banana)
- Check out previous verifiers deployed in [contracts-info repository](https://github.com/0xPolygonHermez/contracts-info/tree/master/verifiers)
- If verifiers are not deployed:
    - use the [following tool](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/tools/deployVerifier) to deploy them

## Add rollup type

- check-out which address has the ability to add new rollup types
    - role is `_ADD_ROLLUP_TYPE_ROLE`
    - [this tool](https://github.com/0xPolygonHermez/rollup-manager-cli) could be used to check which addresses has this role
- Two types of addresses could do the SC call: EOA or timelock (multisig)
    - Next tooling takes that into account
    - Timelock usually have an associated delay. In order to check it, you can check it directly on etherscan as it is a SC variable.
    - Example:
        - Timelock delay Cardona: https://sepolia.etherscan.io/address/0xfd8ace213595fac05d45714e8e2a63df267e3545#readContract#F6
        - Timelock delay Mainnet: https://etherscan.io/address/0xef1462451c30ea7ad8555386226059fe837ca4ef#readContract#F6
- Use [tool to add new rollup type](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/tools/addRollupType) to do the transaction properly
    - if the receiver is the timelock:
        - transaction needs to be schedules first and then executed
        - tool output needs to be forwarded to the admin address of the timelock to schedule/execute the transaction

## Upgrade rollup

- check-out which address has the ability to add new rollup types
    - role is `_UPDATE_ROLLUP_ROLE`
    - rollup admin
    - [this tool](https://github.com/0xPolygonHermez/rollup-manager-cli) could be used to check which addresses has this role and the rollup admin
- this step is straughforward and it can be done is several ways:
    - directly call etherscan function if the role is managed by an EOA
        - example Bali
            - https://sepolia.etherscan.io/address/0xE2EF6215aDc132Df6913C8DD16487aBF118d1764#writeProxyContract#F20
            - https://sepolia.etherscan.io/address/0xE2EF6215aDc132Df6913C8DD16487aBF118d1764#writeProxyContract#F21
    - use [this tool](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/tools/updateRollup) to call the SC function

# Upgrade Smart Contracts to Banana

- [script to upgrade from old version (fork.11) to Banana SC](https://github.com/0xPolygonHermez/zkevm-contracts/tree/v8.0.0-fork.12/upgrade/upgradeBanana)
    - it upgrades the [PolygonZkEVMGlobalExitRootV2](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v8.0.0-fork.12/upgrade/upgradeBanana/upgradeBanana.ts#L104)
    - and [PolygonRollupManager](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v8.0.0-fork.12/upgrade/upgradeBanana/upgradeBanana.ts#L140)

## Params

- [example parameters](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v8.0.0-fork.12/upgrade/upgradeBanana/upgrade_parameters.json.example)
    - the script deploys the new implementation and any EOA can do that
- On top of those parameters, it is needed a file from previous deployment
    - this file is generated automatically by hardhat when you deploy a network
    - placed in `$root-sc_repo/.oppenzeppelin/${network-name}.json`
    - remember to copy this file into thew folder mentioned above and then run the [upgradeBanana](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v8.0.0-fork.12/upgrade/upgradeBanana/upgradeBanana.ts) script

## Output script

- [Similar to this one](https://github.com/0xPolygonHermez/contracts-info/blob/master/mainnet/upgrade-banana/upgrade_output.json)
    - Take the `scheduleData`, send a tx to `timelockAddress` with the proper EOA that has `proxyAdmin` rights
    - wait `timelockDelay`
    - Take the `executeData`, send a tx to `timelockAddress` with the proper EOA that has `proxyAdmin` rights

## Apply upgrade

- `cast send $TIMELOCK_ADDR $SCHEDULE_DATA --private-key $ADMIN_KEY --rpc-url $L1_URL`
- Wait timelock delay
- `cast send $TIMELOCK_ADDR $EXECUTE_DATA --private-key $ADMIN_KEY --rpc-url $L1_URL`
