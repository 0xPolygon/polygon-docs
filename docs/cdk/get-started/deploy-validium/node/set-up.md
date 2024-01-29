1. Navigate back to the working directory we created earlier, `~/cdk-validium`

```bash
cd ~/cdk-validium
```

For this setup, we will also need our information from `deploy_output.json` inside `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment`. Navigate back to `~/cdk-validium/cdk-validium-contracts-0.0.2/deployment` and run the following script to fill the required parameters into the `/tmp/cdk/.env` we created in the previous steps:

```bash
cd ~/cdk-validium/cdk-validium-contracts-0.0.2/deployment
echo "GEN_BLOCK_NUMBER=$(jq -r '.deploymentBlockNumber' deploy_output.json)" >> /tmp/cdk/.env
echo "CDK_VALIDIUM_ADDRESS=$(jq -r '.cdkValidiumAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "POLYGON_ZKEVM_BRIDGE_ADDRESS=$(jq -r '.polygonZkEVMBridgeAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "POLYGON_ZKEVM_GLOBAL_EXIT_ROOT_ADDRESS=$(jq -r '.polygonZkEVMGlobalExitRootAddress' deploy_output.json)" >> /tmp/cdk/.env
echo "CDK_DATA_COMMITTEE_CONTRACT_ADDRESS=$(jq -r '.cdkDataCommitteeContract' deploy_output.json)" >> /tmp/cdk/.env
echo "MATIC_TOKEN_ADDRESS=$(jq -r '.maticTokenAddress' deploy_output.json)" >> /tmp/cdk/.env
```

Source our new environment and navigate back to `~/cdk-validium`:

```bash
source /tmp/cdk/.env
cd ~/cdk-validium
```

## 1. Downloading cdk-validium-node, cdk-data-availability, and cdk-bridge-service

Now clone the `0.0.3` release of `cdk-validium-node`. 

```bash
git clone --depth 1 --branch v0.0.3 https://github.com/0xPolygon/cdk-validium-node.git
```

We also must download and extract version `0.0.3` of `cdk-data-availability.` The release file is available here:

[Untitled Database](https://www.notion.so/b329e3b1511943ae979cc2b4c73a35e8?pvs=21)

Downloading `cdk-validium-contracts` as a ***`tar.gz`*** and extracting

```bash
~/cdk-validium % curl -L -o cdk-data-availability.tar.gz https://github.com/0xPolygon/cdk-data-availability/archive/refs/tags/v0.0.3.tar.gz
\tar -xzf cdk-data-availability.tar.gz
```

Finally, the `cdk-bridge-service` release `0.3.1`. The release file can be found here:

```bash
curl -L -o cdk-bridge-service.tar.gz https://github.com/0xPolygonHermez/zkevm-bridge-service/archive/refs/tags/v0.3.1.tar.gz
\tar -xzf cdk-bridge-service.tar.gz

```
Now we have three new directories in *`cdk-validium/`* named ***`cdk-data-availability-0.0.3`, `cdk-validium-node` and `zkevm-bridge-service-0.3.1`***

## 2. Preparing the environment

We will begin our setup in the node directory.

Navigate into the node directory we cloned from the previous step***`cdk-validium-node/`***

```bash
~/cdk-validium % cd cdk-validium-node/
```

### Setup the database

Run the docker command to start an instance of the `psql` database. The database is used for many of the services, such as the node, prover, DAC, and bridge service.

```bash
docker run -e POSTGRES_USER=cdk_user -e POSTGRES_PASSWORD=cdk_password -e POSTGRES_DB=postgres -p 5432:5432 postgres:15
```

*note: if you are unable to start the process because port is in use, check the processes occupying the port then kill the processes*

```bash
sudo lsof -t -i:5432
kill -9 <PID>
```

Once you have postgres running, validate you have the following setup correctly:

- an admin account called: `cdk_user` with a password of `cdk_password`
- postgres server running on `localhost:5432`

You can use the following command to validate the steps, `\q` to exit:

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432
#=> \q
```

### Provision the database

The `cdk-validium-node` directory contains a script called `single_db_server.sql` that provisions all the databases required for the prover, state, and pool to operate. Run the script to provision all the necessary databases and schemas that will be used for both the prover and node:

```bash
~/cdk-validium/cdk-validium-node % PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -a -q -f ./db/scripts/single_db_server.sql
```

In addition to the provisions required for the prover and node, another provision is needed for the Data Availability Committee (DAC). We can set this up now for use later.

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE committee_db;"
```

Finally, we will provision a database for our bridge service, which we will setup last in this guide.

```bash
PGPASSWORD=cdk_password psql -h localhost -U cdk_user -d postgres -p 5432 -c "CREATE DATABASE bridge_db;"
```
