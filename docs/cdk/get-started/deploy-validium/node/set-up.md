## Set up the environment variables

1. Navigate to `cdk-validium-contracts-0.0.2/deployment` and run the following script that inputs the required parameters from `deploy_output.json` into `/tmp/cdk/.env`.

    ```bash
    cd ~/cdk-validium-contracts-0.0.2/deployment
    echo "GEN_BLOCK_NUMBER=$(jq -r '.deploymentBlockNumber' deploy_output.json)" >> /tmp/cdk/.env
    echo "CDK_VALIDIUM_ADDRESS=$(jq -r '.cdkValidiumAddress' deploy_output.json)" >> /tmp/cdk/.env
    echo "POLYGON_ZKEVM_BRIDGE_ADDRESS=$(jq -r '.polygonZkEVMBridgeAddress' deploy_output.json)" >> /tmp/cdk/.env
    echo "POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS=$(jq -r '.polygonZkEVMGlobalExitRootAddress' deploy_output.json)" >> /tmp/cdk/.env
    echo "CDK_DATA_COMMITTEE_CONTRACT_ADDRESS=$(jq -r '.cdkDataCommitteeContract' deploy_output.json)" >> /tmp/cdk/.env
    echo "MATIC_TOKEN_ADDRESS=$(jq -r '.maticTokenAddress' deploy_output.json)" >> /tmp/cdk/.env
    ```

2. Save the new environment and navigate back to `~/cdk-validium`.

    ```bash
    source /tmp/cdk/.env
    cd ~/cdk-validium
    ```

## Download `cdk-validium-node`, `cdk-data-availability`, and `cdk-bridge-service`

1. Clone the `0.0.3` release of `cdk-validium-node`. 

    ```bash
    git clone --depth 1 --branch v0.0.3 https://github.com/0xPolygon/cdk-validium-node.git
    ```

2. Clone the `0.0.3` release of `cdk-data-availability`. 

    ```bash
    git clone --depth 1 --branch v0.0.3 https://github.com/0xPolygon/cdk-data-availability.git
    ```

3. Finally, download the `cdk-bridge-service` release `0.3.1`. 

    ```bash
    curl -L -o cdk-bridge-service.tar.gz https://github.com/0xPolygonHermez/zkevm-bridge-service/archive/refs/tags/v0.3.1.tar.gz
    \tar -xzf cdk-bridge-service.tar.gz
    ```

    You should see three new directories in `cdk-validium/`: 

    - `cdk-data-availability-0.0.3`
    - `cdk-validium-node`
    - `zkevm-bridge-service-0.3.1`

## Set up the database

1. Navigate to the node directory we cloned at the previous step: `cdk-validium-node/`.

    ```bash
    cd cdk-validium-node/
    ```

2. Run the docker command below to start an instance of the `psql` database. The database is used for many of the services, such as the node, prover, DAC, and bridge service.

    ```bash
    docker run -e POSTGRES_USER=cdk_user -e POSTGRES_PASSWORD=cdk_password -e POSTGRES_DB=postgres -p 5432:5432 postgres:15
    ```

    !!! note "Port is in use"
        If you are unable to start the process because a port is in use, check the processes occupying the port then kill those processes.

        ```bash
        sudo lsof -t -i:5432
        kill -9 <PID>
        ```

3.  Use the following command to validate the setup (`\q` to exit).

    ```bash
    PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432
    ```

    You should have: 

    - An admin account called: `cdk_user` with a password of `cdk_password`.
    - A postgres server running on `localhost:5432`.

## Provision the database

The `cdk-validium-node` directory contains a script called `single_db_server.sql` that provisions all the databases required for the prover, state, and pool to operate. 

1. In a new terminal window, run the script to provision all the necessary databases and schemas used for the prover and node:

    ```bash
    cd cdk-validium/cdk-validium-node
    PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -a -q -f ./db/scripts/single_db_server.sql
    ```

2. Set up the database for the Data Availability Committee (DAC).

    ```bash
    PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE committee_db;"
    ```

3. Finally, provision a database for the bridge service.

    ```bash
    PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE bridge_db;"
    ```
