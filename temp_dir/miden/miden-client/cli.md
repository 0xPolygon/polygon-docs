After installing the client, you can use it by running `miden-client`. In order to get more information about available CLI commands you can run `miden-client --help`.

## Configuration

The CLI can be configured through a TOML file ([`miden-client.toml`](https://github.com/0xPolygonMiden/miden-client/blob/main/miden-client.toml)). This file is expected to be located in the directory from where you are running the CLI. This is useful for connecting to a specific node when developing with the client, for example.

In the configuration file, you will find a section for defining the node's endpoint and the store's filename. By default, the node will run on `localhost:57291`, so the linked example file specifies it as the node's endpoint. 

Note that running the node locally for development is encouraged, but the endpoint can be set to point to any remote node's IP as well.

!!! example "Executing, proving, and submitting transactions to the Miden node"
    For a complete example on how to run the client and submit transactions to the Miden node, you can refer to the [`Getting started`](https://0xpolygonmiden.github.io/miden-base/introduction/getting-started.html).

## Reference

The following is a list of commands that the CLI currently supports. A small explanation follows for the commands that contain subcommands. Note that for any command you can get an explanation in the terminal by attaching `--help` to it.

| Command      | Description                                                  |
|--------------|--------------------------------------------------------------|
| `account`      | Create accounts and inspect account details                 |
| `input-notes`  | View and manage input notes                                             |
| `sync`         | Sync this client with the latest state of the Miden network |
| `info`         | View a summary of the current client state                  |
| `tags`         | View and add tags                                            |
| `tx` (or `transaction`)           | Execute and view transactions            

### `account` subcommands

| Command | Description                                         | Aliases |
|---------|-----------------------------------------------------|---------|
| `list`    | List all accounts monitored by this client         | -l      |
| `show`    | Show details of the account for the specified ID   | -s      |
| `new <ACCOUNT TYPE>`     | Create new account and store it locally            | -n      |
| `import`  | Import accounts from binary files | -i      |

Once an account gets created with the `new` command, it will be automatically stored and tracked by the client, which means the client can execute transactions that modify the state of accounts and track related changes by synchronizing with the Miden Node.

### `input-notes` subcommands

| Command | Description                                                 | Aliases |
|---------|-------------------------------------------------------------|---------|
| `list`    | List input notes                                            | -l      |
| `show`    | Show details of the input note for the specified note ID   | -s      |
| `export`  | Export input note data to a binary file                    | -e      |
| `import`  | Import input note data from a binary file                  | -i      |

### `tags` command

| Command | Description                                              | Aliases |
|---------|----------------------------------------------------------|---------|
| `list`    | List all tags monitored by this client                   | -l      |
| `add`     | Add a new tag to the list of tags monitored by this client | -a      |

### `tx` command

| Command | Description                                              | Aliases |
|---------|----------------------------------------------------------|---------|
| `list`    | List tracked transactions                                        | -l      |
| `new  <TX TYPE>` | Execute a transaction, prove and submit it to the node. Once submitted, it gets tracked by the client   | -n      |

After a transaction gets executed, two entities start being tracked:

- The transaction itself: It will follow a lifecycle of being `pending` (initial state) and `committed` (after the we know the node received it)
- Output Notes that might have been created as part of the transaction (for example, when executing a pay-to-id transaction)

You can list them with their respective commands.

## Types of transaction

| Command         | Explanation                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| `p2id <SENDER ACCOUNT ID> <TARGET ACCOUNT ID> <FAUCET ID> <AMOUNT>`            | Pay-to-id transaction. Sender Account creates a note that a target Account ID can consume. The asset is identifed by the tuple `(FAUCET ID, AMOUNT)`. |
| `mint <TARGET ACCOUNT ID> <FAUCET ID> <AMOUNT>`           | Creates a note that contains a specific amount tokens minted by a faucet, that the target Account ID can consume|
| `consume-notes  <ACCOUNT ID> [NOTES]`  | Account ID consumes a list of notes, specified by their Note ID |

