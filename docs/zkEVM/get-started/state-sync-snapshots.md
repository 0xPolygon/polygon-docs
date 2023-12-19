Use snapshots for quick state syncing. 

Find the zkEVM mainnet snapshots at the below urls.
    ```bash
    https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-pooldb.sql.gz (65MB)
    https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-bridgedb.sql.gz (315MB)
    https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-statedb.sql.gz (6GB)
    https://zkevm-mai.s3.eu-west-1.amazonaws.com/mainnet-hashdb.sql.gz (160GB)
    ```

Find the testnet snapshots at the below urls.
    ```bash
    https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-pooldb.sql.gz (65MB)
    https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-bridgedb.sql.gz (312MB)
    https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-statedb.sql.gz (1.9GB)
    https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-hashdb.sql.gz (49GB)
    ```

Follow the next instructions to sync state. Be sure to 'curl' snapshots for the correct network, that is, mainnet or testnet.

```bash
    # Retrieve backup file
    curl https://zkevm-pub.s3.eu-west-1.amazonaws.com/testnet-statedb.sql.gz -o statedb.sql.gz

    # Let only datatabase running
    docker compose stop
    docker compose start zkevm-state-db

    # Remove data from database, keeping schema (the backup is raw COPY)
    docker compose exec -it zkevm-state-db pg_dump -U state_user -v -Fc -s -f /tmp/statedb.schema state_db
    docker compose exec -it zkevm-state-db dropdb -U state_user state_db
    docker compose exec -it zkevm-state-db createdb -U state_user state_db
    docker compose exec -it zkevm-state-db pg_restore -U state_user -v -d state_db /tmp/statedb.schema

    # Import the backup file into database
    gunzip -c statedb.sql.gz | docker compose exec -T zkevm-state-db psql -U state_user -d state_db

    # Cleanup
    docker compose exec zkevm-state-db rm /tmp/statedb.schema
    rm statedb.sql.gz

    # Start everything
    docker compose up -d
```
