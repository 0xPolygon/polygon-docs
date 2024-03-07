In order to use the Miden client library in a Rust project, you need to include it as a dependency. In your project's `cargo.toml`, add:

```toml
miden_client = { package = "miden-client", git = "https://github.com/0xPolygonMiden/miden-client", branch = "main" }
```

## Client instantiation

Currently, the client is generic over the `NodeRpcClient` and the `DataStore`. The current supported store is the `SqliteStore`, which is a SQLite implementation of the incoming `Store` trait.

```rust
        let client: Client<TonicRpcClient, SqliteDataStore> = {
            let store = Store::new((&client_config).into()).map_err(ClientError::StoreError)?;

            Client::new(
                client_config,
                TonicRpcClient::new(&rpc_endpoint),
                SqliteDataStore::new(store),
            )?
        };
```

## Local account creation

With the Miden client, you can create and track local (not on-chain) accounts. What this means is that all state is tracked locally, and the rollup only keeps commitments to the data, which in turn guarantees privacy:

```Rust
    let account_template = AccountTemplate::BasicWallet {
        mutable_code: false,
        storage_mode: accounts::AccountStorageMode::Local,
    };
    
    let (new_account, account_seed) = client.new_account(client_template)?;
```

The `AccountTemplate` enum defines which type of account will be created. Note that once an account is created, it will be kept locally and its state will automatically be tracked by the client. Any number of accounts can be created and stored by the client.

## Execute a transaction

In order to execute a transaction, you first need to define which type of transaction is to be executed. This may be done with the `TransactionTemplate` enum. Here is an example for a pay-to-id type transaction:

```rust
    // Define asset
    let faucet_id = AccountId::from_hex(faucet_id)?;
    let fungible_asset = FungibleAsset::new(faucet_id, *amount)?.into();

    let sender_account_id = AccountId::from_hex(bob_account_id)?;
    let target_account_id = AccountId::from_hex(alice_account_id)?;
    let payment_transaction = PaymentTransactionData::new(
        fungible_asset,
        sender_account_id,
        target_account_id,
    );

    let transaction_template: TransactionTemplate = TransactionTemplate::P2ID(payment_transaction);

    // Execute transaction. No information is tracked after this.
    let transaction_execution_result =
        client.new_transaction(transaction_template.clone())?;

    // Prove and submit the transaction, which is stored alongside created notes (if any)
    client
        .send_transaction(transaction_execution_result)
        .await?
```
