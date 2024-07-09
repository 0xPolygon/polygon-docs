---
comments: true
---

!!! warning
    
    **Apologies to zkEVM users**

    We don't have snapshots from the time we moved from AWS to GCP. That’s since February, 2024.

    As we are moving towards an Erigon-based CDK, which has no PostgreSQL, the task to prepare snapshots is on-hold.

    Also, it is expected to take only hours, instead of days, for Erigon to sync from scratch.

    So, there will be no need for snapshots.

    As a result, this document will soon be deprecated … or maybe be moved to the legacy section of the zkEVM docs (if the team so decides).

    
Follow the instructions below to run a fast state sync on a node database using the relevant snapshot. Snapshot URLs are available in the [snapshots subsection](#snapshots) below.

## Sync a database

1. Run the following command to download the snapshot with the correct `snapshot-url` and `db-name`:

    ```sh
    curl <snapshot-url> -o <db-name>.sql.gz
    ```

    For example: 

    ```sh
    curl https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-statedb.sql.gz -o statedb.sql.gz
    ```

2. Stop/start the database:
    
    ```sh
    docker compose stop
    docker compose start zkevm-state-db
    ```

3. Remove data from the database, keeping the schema and a raw backup copy:

    ```sh
    docker compose exec -it zkevm-state-db pg_dump -U state_user -v -Fc -s -f /tmp/statedb.schema state_db
    docker compose exec -it zkevm-state-db dropdb -U state_user state_db
    docker compose exec -it zkevm-state-db createdb -U state_user state_db
    docker compose exec -it zkevm-state-db pg_restore -U state_user -v -d state_db /tmp/statedb.schema
    ```

4. Import the backup file into the database:

    ```sh
    gunzip -c statedb.sql.gz | docker compose exec -T zkevm-state-db psql -U state_user -d state_db
    ```

5. Clean up:

    ```sh
    docker compose exec zkevm-state-db rm /tmp/statedb.schema
    rm statedb.sql.gz
    ```
    
6. Start everything again:

    ```sh
    docker compose up -d
    ```

## Snapshots

The snapshot for the bridge, state, and hash databases are given below for mainnet and testnet.

### Mainnet

```bash
https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-bridgedb.sql.gz (315MB)
https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-statedb.sql.gz (6GB)
https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-hashdb.sql.gz (160GB)
```

### Testnet

```bash
https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-bridgedb.sql.gz (312MB)
https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-statedb.sql.gz (1.9GB)
https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-hashdb.sql.gz (49GB)
```
