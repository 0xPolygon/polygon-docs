# Accounts
Miden aims to support expressive smart contracts via a Turing-complete language. For smart contracts the go-to solution is account-based state. In Miden, an account is an entity which holds assets and defines rules of how these assets can be transferred. They are basic building blocks representing a user or an autonomous smart contract.

## Account Design
The diagram below illustrates basic components of an account. In Miden every account is a smart contract.

<center>
![Architecture core concepts](../img/architecture/account/account-definition.png){ width="25%" }
</center>

In the above picture, you can see:

* **Account ID &rarr;** a unique identifier of an account which does not change throughout its lifetime
* **Storage &rarr;** user-defined data which can be stored in an account
* **Nonce &rarr;** a counter which must be incremented whenever the account state changes
* **Vault &rarr;** a collection of assets stored in an account
* **Code &rarr;** a collection of functions which define the external interface for an account

### Account ID
~63 bits (1 field element) long identifier for the account. The four most significant bits specify its [account type](https://0xpolygonmiden.github.io/miden-base/architecture/accounts.html#account-types) - regular, immutable, faucet - and the [storage mode](https://0xpolygonmiden.github.io/miden-base/architecture/accounts.html#account-storage-modes) - public or private.

### Account Storage
Storage for user-defined data. `AccountStorage` is composed of two components.

The first component is a simple Sparse Merkle Tree of depth `8` which is index addressable. This provides the user with `256` `Word` slots.

Users requiring additional storage can use the second component a `MerkleStore`. It allows users to store any Merkle structures they need. The root of the Merkle structure can be stored as a leaf in a simple Sparse Merkle Tree. When `AccountStorage` is serialized it will check if any of the leafs in the simple Sparse Merkle Tree are Merkle roots of other Merkle structures. If any Merkle roots are found then the Merkle structures will be persisted in the `AccountStorage` `MerkleStore`.

### Nonce
Counter which must be incremented whenever the account state changes. Nonce values must be strictly monotonically increasing and can be incremented by any value smaller than 2^{32} for every account update.

### Vault
Asset container for an account.

An account vault can contain an unlimited number of [assets](https://0xpolygonmiden.github.io/miden-base/architecture/assets.html). The assets are stored in a sparse
Merkle tree as follows:

* For fungible assets, the index of a node is defined by the issuing faucet ID, and the value
  of the node is the asset itself. Thus, for any fungible asset there will be only one node
  in the tree.
* For non-fungible assets, the index is defined by the asset itself, and the asset is also
  the value of the node.

An account vault can be reduced to a single hash which is the root of the Sparse Merkle Tree.

### Code
Interface for accounts. In Miden every account is a smart contract. It has an interface that exposes functions that can be called by [note scripts](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-scripts) and [transaction scripts](https://0xpolygonmiden.github.io/miden-base/transactions/transaction-kernel.html#the-transaction-script-processing). Users cannot call those functions directly.

Functions exposed by the account have the following properties:

* Functions are actually roots of [Miden program MASTs](https://0xpolygonmiden.github.io/miden-vm/user_docs/assembly/main.html) (i.e., a 32-byte hash). Thus, function identifier is a commitment to the code which is executed when a function is invoked.
* Only account functions have mutable access to an account's storage and vault. Therefore, the only way to modify an account's internal state is through one of the account's functions.
* Account functions can take parameters and can create new notes.

*Note: Since code in Miden is expressed as MAST, every function is a commitment to the underlying code. The code cannot change unnoticed to the user because its hash would change. Behind any MAST root there can only be `256` functions*

#### Example Account Code
Currently, Miden provides two standard implementations for account code.

##### Basic user account (Regular updatable account)
There is a standard for a basic user account. It exposes three functions via its interface.
<details>
  <summary>Want to see the code?</summary>

  ```
    use.miden::contracts::wallets::basic->basic_wallet
    use.miden::contracts::auth::basic

    export.basic_wallet::receive_asset
    export.basic_wallet::send_asset
    export.basic::auth_tx_rpo_falcon512
  ```
</details>

[Note scripts](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-scripts) or [transaction scripts](https://0xpolygonmiden.github.io/miden-base/transactions/transaction-kernel.html#the-transaction-script-processing) can call `receive_asset` and `send_asset` and in doing so, the account can receive and send assets. Transaction scripts can also call `auth_tx_rpo_falcon512` and authenticate the transaction. It is important to know, that without correct authentication, i.e. knowing the correct private key, a note cannot successfully invoke receive and send asset.

##### Basic fungible faucet (Faucet for fungible assets)
There is also a standard for a [basic fungible faucet](https://github.com/0xPolygonMiden/miden-base/blob/main/miden-lib/asm/miden/contracts/faucets/basic_fungible.masm).

<details>
  <summary>Want to see the code?</summary>

  ```
  #! Distributes freshly minted fungible assets to the provided recipient.
  #!
  #! ...
  export.distribute
      # get max supply of this faucet. We assume it is stored at pos 3 of slot 1
      push.METADATA_SLOT exec.account::get_item drop drop drop
      # => [max_supply, amount, tag, RECIPIENT, ...]

      # get total issuance of this faucet so far and add amount to be minted
      exec.faucet::get_total_issuance
      # => [total_issuance, max_supply, amount, tag, RECIPIENT, ...]

      # compute maximum amount that can be minted, max_mint_amount = max_supply - total_issuance
      sub
      # => [max_supply - total_issuance, amount, tag, RECIPIENT, ...]

      # check that amount =< max_supply - total_issuance, fails if otherwise
      dup.1 gte assert
      # => [asset, tag, RECIPIENT, ...]

      # creating the asset
      exec.asset::create_fungible_asset
      # => [ASSET, tag, RECIPIENT, ...]

      # mint the asset; this is needed to satisfy asset preservation logic.
      exec.faucet::mint
      # => [ASSET, tag, RECIPIENT, ...]

      # create a note containing the asset
      exec.tx::create_note
      # => [note_ptr, ZERO, ZERO, ...]
  end

  #! Burns fungible assets.
  #!
  #! ...
  export.burn
      # burning the asset
      exec.faucet::burn
      # => [ASSET]

      # increments the nonce (anyone should be able to call that function)
      push.1 exec.account::incr_nonce

      # clear the stack
      padw swapw dropw
      # => [...]
  end
  ```
</details>

The contract exposes two functions `distribute` and `burn`. The first function `distribute` can only be called by the faucet owner, otherwise it fails. As inputs, the function expects everything that is needed to create a note containing the freshly minted asset, i.e., amount, [tag](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-metadata), [RECIPIENT](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-recipient).

The second function `burn` can be called by anyone to burn the tokens that are contained in a note.

*Info: The difference is that the `burn` procedure exposes `exec.account::incr_nonce`, so by calling `burn` the nonce of the executing account gets increased by 1 and the transaction will pass the epilogue check. The `distribute` procedure does not expose that. That means the executing user needs to call `basic::auth_tx_rpo_falcon512` which requires the private key.*

## Account creation
For an account to exist it must be present in the [Account DB](https://0xpolygonmiden.github.io/miden-base/architecture/state.html#account-database) kept by the Miden node(s). However, new accounts can be created locally by users using a wallet.

The process is as follows:

* Alice grinds a new Account ID (according to the account types) using a wallet
* Alice's Miden client requests the Miden node to check if new Account ID already exists
* Alice shares the new Account ID to Bob (eg. when Alice wants to receive funds)
* Bob executes a transaction and creates a note that contains an asset for Alice
* Alice consumes Bob's note to receive the asset in a transaction
* Depending on the account storage mode (private vs. public) and transaction type (local vs. network) the Operator receives the new Account ID eventually and - if the transaction is correct - adds the ID to the Account DB

For a user to create an account we have 2 solutions at the moment:

1. Use the [Miden client](https://github.com/0xPolygonMiden/miden-client/tree/main) as a wallet
2. Use the Miden Base builtin functions for wallet creation: [Basic wallet](https://github.com/0xPolygonMiden/miden-base/blob/4e6909bbaf65e77d7fa0333e4664be81a2f65eda/miden-lib/src/accounts/wallets/mod.rs#L15), [Fungible faucet](https://github.com/0xPolygonMiden/miden-base/blob/4e6909bbaf65e77d7fa0333e4664be81a2f65eda/miden-lib/src/accounts/faucets/mod.rs#L11)

## Account types
There are four types of accounts in Miden:

| | Regular updatable account | Regular immutable account | Faucet for fungible assets | Faucet for non-fungible assets |
|---|---|---|---|---|
| **Description** | For most users, e.g. a wallet. Code changes allowed, including public API. | For most smart contracts. Once deployed code is immutable. | Users can issue fungible assets and customize them. | Users can issue non-fungible assets and customize them. |
| **Code updatability** | yes | no | no | no |
| **Most significant bits** | `00` | `01` | `10` | `11` |

## Account storage modes
Account data - stored by the Miden node - can be public, private, or encrypted. The third and fourth most significant bits of the account ID specifies whether the account data is public `00`, encrypted `01`, or private `11`.

* Accounts with **public state**, where the actual state is stored onchain. These would be similar to how accounts work in public blockchains. Smart contracts that depend on public shared state should be stored public on Miden, e.g., DEX contract.
* Accounts with **private state**, where only the hash of the account is stored onchain. Users who want stay private and take care of their own data should choose this mode. The hash is defined as: `hash([account ID, 0, 0, nonce], [vault root], [storage root], [code root])`.

In the future we will also support **encrypted state** which will be onchain but encrypted. * Depending on the account storage mode (private vs. encrypted vs. public) and transaction type (local vs. network) the operator receives the new Account ID eventually and - if the transaction is correct - adds the ID to the Account DB
