# Getting started

This tutorial will guide you through the process generating a new Miden account, requesting funds from a public faucet and interacting with the Miden rollup using the Miden client. 

The Miden node processes transactions and creates blocks for the Miden rollup. The Miden client provides a way to execute and prove transactions, facilitating the interaction with the Miden rollup. By the end of this tutorial, you will be able to configure the Miden client, connect to a Miden node, and perform basic operations like sending transactions, generating and consuming notes.

### Prerequisites

Before starting, ensure you have the following:

- **Rust Installed:** You must have the Rust programming language installed on your machine. If you haven't installed Rust, you can download it from [the Rust website](https://www.rust-lang.org/learn/get-started).

- **Node IP Address:** Obtain the IP address of the running Miden node. This information can be acquired by contacting one of the Miden engineers.

- **Miden client Installation:** You need to install the [Miden client](https://github.com/0xPolygonMiden/miden-client) and configure it to point to the remote node.

## Part 1: Creating a Miden account & using the faucet

In this first part of the tutorial we will teach you how to create a new Miden account locally and how to receive funds from the public Miden faucet website.

### Configuring the Miden client

1. **Download the Miden client:** First, download the Miden client from its repository. Use the following command:

      ```shell
      git clone https://github.com/0xPolygonMiden/miden-client
      ```

2. **Navigate & Configure the client:** Navigate to the client directory and modify the configuration file to point to the remote Miden node. You can find the configuration file at `./miden-client.toml`. In the `[RPC]` section replace the `endpoint = { host: }` field with the address provided by the Miden team.

      ```shell
      cd miden-client
      ```

      Configuration file example:

      ```toml
      [rpc]
      endpoint = { protocol = "http", host = "<NODE_IP_ADDRESS>", port = 57291 }

      [store]
      database_filepath = "store.sqlite3"
      ```

3. **Build & install the Client:** install the client using cargo:

      ```shell
      cargo install --features testing,concurrent --path .
      ```

      you should now be able to use the following command:

      ```shell
      miden-client --help
      ```
### Creating a new Miden account

1. **Creating a new account:** To be able to interact with the Miden rollup you will need to generate an account. For this first part of the example we will generate one `basic-immutable` account using the following command:

      ```shell
      miden-client account new basic-immutable
      ```

      Please refer to the documentation of the CLI

2. **Listing accounts:** To view the newly created account we can run the following command:

      ```shell
      miden-client account -l
      ```

      We should now see 1 available account listed:
      - `basic-immutable`

### Requesting tokens from the public faucet

1. **Navigating to the faucet website:** To request funds from the faucet navigate to the following website: [Miden faucet website](https://ethdenver.polygonmiden.io/)

2. **Requesting funds from the faucet:** Now that you have created your Miden account and navigated to the faucet website you should now be able to copy your `AccountId` that has been printed by the `miden-client account -l` command that you used in the previous steps. Paste this id into the field present on the faucet website and click `Send me tokens!`. After a few seconds your browser should download or prompt you to download a file called `note.mno` (mno = Miden Note), save this file on your computer, it will be needed for the next steps and contains the funds sent by the faucet destined to your address.

### Importing the note into the Miden client

1. **Importing & visualising notes:** From your terminal we will use the Miden client to import and visualise the note that you have received using the following commands: 

      ```shell
      miden-client input-notes -i <path-to-note>
      ```

      Now that the note has been successfully imported you should be able to visualise it's information using the following command: 

      ```shell
      miden-client input-notes -l
      ```

      As you can see the listed note is lacking a `commit-height` this is due to the fact that you have received a note off-chain but have not synced your view of the rollup to check that the note is valid and exists at the rollup level. This is essential to prevent double-spend and make sure that you consume notes that have not yet been nullified. Hence before consuming the note we will need to update or view of the rollup and sync.

2. **Syncing the client:** The client needs to periodically query the node to receive updates about entities that might be important in order to run transactions. The way to do so is by running the `sync` command:

      ```shell
      miden-client sync
      ```


### Consuming the note & receiving the funds

1. **Consuming the note:** Now that we have synced the client the input-note that we have imported from the faucet should have a `commit-height` confirming it's existence at the rollup level: 

      ```shell
      miden-client input-notes -l
      ```
      We can now consume the note and add the funds contained inside it's vault to our account using the following commands: 

      ```shell
      miden-client tx new consume-notes <Account-Id> <Note-Id>
      ```

      You should be able to find your account and note id by listing both `accounts` and `input-notes`:

      ```shell
      miden-client account -l
      miden-client input-notes -l
      ```
    
2. **Visualising account vault:** After successfully running the previous commands your account should now contained the tokens sent from the faucet. You can visualise your accounts vault by running the following command: 

      ```shell
      miden-client account show <Account-Id> -v
      ```
      You should now see your accounts vault containing the funds sent by the faucet. 

#### Congratulations! You finished the first part of the tutorial, continue to learn more about Miden and understand how to send Peer-to-Peer private off-chain transactions!

## Part 2: Peer-to-Peer private off-chain transactions

In this second part of the tutorial we will teach you how to make off-chain transactions and send funds to another account using the Miden client. 

> **Note**:
> We consider that you have done the first part of the turorial and that the state of your local client has not been reset. 


### Setting-up the Miden client

1. **Creating a second account:** To be able to send funds from one account to another we will need to generate one more account. For this example we will be generating 1 additional account: we generated `basic-immutable` account A in the first part of the tutorial. Here we will be creating `basic-immutable` account B using the following command:

      ```shell
      miden-client account new basic-immutable
      ```

      Please refer to the documentation of the CLI

2. **Listing accounts:** To view the newly created accounts we can run the following command:

      ```shell
      miden-client account -l
      ```

      We should now see 2 available accounts listed:
      - `basic-immutable` account A (created during the first part of this tutorial)
      - `basic-immutable` account B

### Transferring assets between accounts

Now that we have two accounts we are ready to transfer some of the tokens we received from the faucet into account A. We will now transfer some to our second regular account B. To do so, you can run:

```shell
miden-client tx new p2id <regular-account-id-A> <regular-account-id-B> <faucet-account-id> <Amount>
```

> **Note**
> The faucet account id can be found on the faucet website under the title "Miden faucet".

This will generate a Pay-to-ID (`P2ID`) note containing `<amount>` assets, transferred from one regular account to the other. If we sync, we can now make use of the note and consume it for the receiving account:

```shell
miden-client sync # Make sure we have an updated view of the state
miden-client input-notes list # Now use the second note id
miden-client tx new consume-notes <regular-account-ID-B> <input-note-id> # Consume the note
```

That's it! You should now be able to see both accounts containing assets coming from the faucet and then transferred from `Account A` to `Account B`.

```shell
miden-client account show <regular-account-ID-B> -v # Show account B's vault assets (50 fungible tokens)
miden-client account show <regular-account-ID-A> -v # Show account A's vault assets (950 fungible tokens)
```

### Clearing the state

All state is maintained in `store.sqlite3`, located in the directory defined in the `miden-client.toml` file. In case it needs to be cleared, the file can be deleted; it will later be created again when any command is executed.

## Conclusion

Congratulations! You have successfully configured and used the Miden client to interact with a Miden rollup and faucet. With these steps, you can perform basic Miden rollup operations like sending transactions, generating and consuming notes.

For more information on the Miden client, refer to the [Readme of the Miden Client](https://github.com/0xPolygonMiden/miden-client)

For more information on the Miden rollup, refer to the [Miden documentation](https://0xpolygonmiden.github.io/miden-base/introduction.html).
