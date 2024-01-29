## Configure prover DB

1. Copy/paste the following script into `~/zkevm/mainnet/db/scripts/init_prover_db.sql` to replace what's there.

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

2. Save and exit the file. 

## Configure the prover

1. Create a file called `config.json` and copy/paste the mock prover configuration from here: https://github.com/0xPolygonHermez/zkevm-node/blob/develop/test/config/test.prover.config.json.

2. Save it to the `~/zkevm/` directory.