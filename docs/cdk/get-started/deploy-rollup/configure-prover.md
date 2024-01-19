## Configure prover DB

Edit `~/zkevm/mainnet/db/scripts/init_prover_db.sql` to set up the node databases.

```sql
CREATE DATABASE prover_db;
\connect prover_db;

CREATE SCHEMA state;

CREATE TABLE state.nodes (hash BYTEA PRIMARY KEY, data BYTEA NOT NULL);
CREATE TABLE state.program (hash BYTEA PRIMARY KEY, data BYTEA NOT NULL);

CREATE USER prover_user with password 'prover_pass';
GRANT CONNECT ON DATABASE prover_db TO prover_user;
ALTER USER prover_user SET SEARCH_PATH=state;
GRANT ALL PRIVILEGES ON SCHEMA state TO prover_user;
GRANT ALL PRIVILEGES ON TABLE state.nodes TO prover_user;
GRANT ALL PRIVILEGES ON TABLE state.program TO prover_user;
```

Save and exit the file. 

## Configure the prover

Create the `~/zkevm/config.json` and paste the configs below. 

!!! info
    `aggregatorClientHost` only required when running the full prover.

??? "Click to expand the <code>config.json</code> file"
    ```json
    {
      "runExecutorServer": false,
      "runExecutorClient": false,
      "runExecutorClientMultithread": false,

      "runStateDBServer": false,
      "runStateDBTest": false,
      
      "runAggregatorServer": false,
      "runAggregatorClient": true,
      "proverName": "static_prover",
      
      "runFileGenBatchProof": false,
      "runFileGenAggregatedProof": false,
      "runFileGenFinalProof": false,
      "runFileProcessBatch": false,
      "runFileProcessBatchMultithread": false,
      "runFileExecutor": false,
      
      "runKeccakScriptGenerator": false,
      "runKeccakTest": false,
      "runStorageSMTest": false,
      "runBinarySMTest": false,
      "runMemAlignSMTest": false,
      "runSHA256Test": false,
      "runBlakeTest": false,
      
      "executeInParallel": true,
      "useMainExecGenerated": true,
      "useProcessBatchCache": true,
      "saveRequestToFile": false,
      "saveInputToFile": true,
      "saveDbReadsToFile": true,
      "saveDbReadsToFileOnChange": false,
      "saveOutputToFile": true,
      "saveFilesInSubfolders": false,
      "saveProofToFile": true,
      "saveResponseToFile": false,
      "loadDBToMemCache": true,
      "loadDBToMemCacheInParallel": false,
      "dbMTCacheSize": 16384,
      "dbProgramCacheSize": 16384,
      "dbMultiWrite": true,
      "dbFlushInParallel": true,
      
      "opcodeTracer": false,
      "logRemoteDbReads": false,
      "logExecutorServerResponses": false,
      
      "executorServerPort": 50071,
      "executorROMLineTraces": false,
      "executorClientPort": 50071,
      "executorClientHost": "127.0.0.1",
      
      "stateDBServerPort": 5432,
      "stateDBURL": "local",
      
      "aggregatorServerPort": 50081,
      "aggregatorClientPort": 50081,
      "aggregatorClientHost": "", // YOUR PUBLIC IP ADDRESS
      "aggregatorClientMockTimeout": 10000000,
      
      "mapConstPolsFile": false,
      "mapConstantsTreeFile": false,
      
      "inputFile": "testvectors/aggregatedProof/recursive1.zkin.proof_0.json",
      "inputFile2": "testvectors/aggregatedProof/recursive1.zkin.proof_1.json",
      
      "outputPath": "/output/",
      "configPath": "/mnt/prover/config/",
      "zkevmCmPols_disabled": "/mnt/prover/runtime/zkevm.commit",
      "c12aCmPols": "runtime/c12a.commit",
      "recursive1CmPols_disabled": "runtime/recursive1.commit",
      "recursive2CmPols_disabled": "runtime/recursive2.commit",
      "recursivefCmPols_disabled": "runtime/recursivef.commit",
      "finalCmPols_disabled": "runtime/final.commit",
      
      "publicsOutput": "public.json",
      "proofFile": "proof.json",
      
      "databaseURL": "postgresql://prover_user:prover_pass@zkevm-state-db:5432/prover_db",
      "databaseURL_disabled": "local",
      "dbNodesTableName": "state.nodes",
      "dbProgramTableName": "state.program",
      "dbConnectionsPool": true,
      "cleanerPollingPeriod": 600,
      "requestsPersistence": 3600,
      "maxExecutorThreads": 20,
      "maxProverThreads": 8,
      "maxStateDBThreads": 8
    }
    ```