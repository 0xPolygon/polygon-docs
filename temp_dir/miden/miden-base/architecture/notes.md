# Notes

Miden aims to achieve parallel transaction execution and privacy. The UTXO-model combined with client-side proofs provide those features. That means, in Miden exist notes as a way of transferring assets between and to interact with accounts. Notes can be consumed and produced asynchronously and privately. The concept of notes is a key difference between Ethereum’s Account-based model and Polygon Miden, which uses a hybrid UTXO- and Account-based [state-model](state.md).

## Note design

In Polygon Miden, accounts communicate with one another by producing and consuming notes. A note stores assets and a script that defines how this note can be consumed.

The diagram below illustrates the contents of a note:

<center>
![Architecture core concepts](../img/architecture/note/note.png){ width="25%" }
</center>

As shown in the above picture:
* **Assets &rarr;** serves as [asset](assets.md) container for a note. It can contain up to `256` assets stored in an array which can be reduced to a single hash.
* **Script &rarr;** will be executed in the [transaction](https://0xpolygonmiden.github.io/miden-base/architecture/transactions.html) in which the note is consumed. The script defines the conditions for the consumption, if the script fails, the note cannot be consumed.
* **Inputs &rarr;** used for the note script execution. They can be accessed by the note script via [transaction kernel procedures](https://0xpolygonmiden.github.io/miden-base/transactions/transaction-procedures.html#note). The number is limited to 16 and they must be defined at note creation.
* **Serial number &rarr;** a note's unique identifier to break linkability between [note hash](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-hash) and [nullifier](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-nullifier). Should be a random `Word` chosen by the user - if revealed, the nullifier might be computed easily.

In addition, a note has **metadata** including the sender and the note tag. Those values are always public regardless of the [note storage mode](https://0xpolygonmiden.github.io/miden-base/architecture/notes.html#note-storage-mode).

## Note's lifecycle
New notes are created by executing transactions. After verifying the transaction proof the operator adds either only the note hash (private notes) or the full note data (public notes) to the [Note DB](https://0xpolygonmiden.github.io/miden-base/architecture/state.html#notes-database). Notes can be produced and consumed locally by users in local transactions or by the operator in a network transaction. Note consumption requires the transacting party to know the note data to compute the nullifier. After successful verification, the operator sets the corresponding entry in the Nullifier DB to "consumed".

<center>
![Architecture core concepts](../img/architecture/note/note-life-cycle.png)
</center>

The following sections will explain, how notes are created, stored, discovered and consumed.

## Note creation
Notes are created as outputs (`OutputNotes`) of Miden transactions. Operators record those notes to the [Note DB](https://0xpolygonmiden.github.io/miden-base/architecture/state.html#note-database), after successful verification of the underlying transactions those notes can be consumed.

## The note script
Every note has a script which gets executed at note consumption. It is always executed in the context of a single account, and thus, may invoke zero or more of the [account's functions](https://0xpolygonmiden.github.io/miden-base/architecture/accounts.html#code). The script allows for more than just the transferring of assets, they could be of arbitrary complexity thanks to the Turing completeness of the Miden VM

By design, every note script can be defined as a unique hash or the root of a [Miden program MAST](https://0xpolygonmiden.github.io/miden-vm/user_docs/assembly/main.html). That also means every function is a commitment to the underlying code. That code cannot change unnoticed to the user because its hash would change. That way it is easy to recognize standardized notes and those which deviate.

Note scripts are created together with their inputs, i.e., the creator of the note defines which inputs are used at note execution by the executor. However, the executor or prover can pass optional note args. Note args are data put onto the the stack right before a note script is executed. These are different from note inputs, as the executing account can specify arbitrary note args.

There exist [standard note scripts](https://github.com/0xPolygonMiden/miden-base/tree/main/miden-lib/asm/note_scripts) (P2ID, P2IDR, SWAP) that users can create and add to their notes using the Miden client or by calling internal [Rust code](https://github.com/0xPolygonMiden/miden-base/blob/fa63b26d845f910d12bd5744f34a6e55c08d5cde/miden-lib/src/notes/mod.rs#L15-L66).

* P2ID and P2IDR scripts are used to send assets to a specific account ID. The scripts check at note consumption if the executing account ID equals the account ID that was set by the note creator as note inputs. The P2IDR script is reclaimable and thus after a certain block height can also be consumed by the sender itself.
* SWAP script is a simple way to swap assets. It adds an asset from the note into the consumer's vault and creates a new note consumable by the first note's issuer containing the requested asset.

### Example note script Pay to ID (P2ID)
<details>
  <summary>Want to know more how to ensure a note can only be consumed by a specified account?</summary>

  #### Goal of the P2ID script
  The P2ID script defines a specific target account ID as the only account that can consume the note. Such notes ensure a targeted asset transfer.

  #### Imports and context
  The P2ID script uses procedures from the account, note and wallet API.
  ```
  use.miden::account
  use.miden::note
  use.miden::contracts::wallets::basic->wallet
  ```
  As discussed in detail in [transaction kernel procedures](../transactions/transaction-procedures.md) certain procedures can only be invoked in certain contexts. The note script is being executed in the note context of the [transaction kernel](../transactions/transaction-kernel.md).

  #### Main script
  The main part of the P2ID script checks if the executing account is the same as the account defined in the `NoteInputs`. The creator of the note defines the note script and the note inputs separately to ensure usage of the same standardized P2ID script regardless of the target account ID. That way, it is enough to check the script root (see above).

  ```
  # Pay-to-ID script: adds all assets from the note to the account, assuming ID of the account
  # matches target account ID specified by the note inputs.
  #
  # Requires that the account exposes: miden::contracts::wallets::basic::receive_asset procedure.
  #
  # Inputs: [SCRIPT_ROOT]
  # Outputs: []
  #
  # Note inputs are assumed to be as follows:
  # - target_account_id is the ID of the account for which the note is intended.
  #
  # FAILS if:
  # - Account does not expose miden::contracts::wallets::basic::receive_asset procedure.
  # - Account ID of executing account is not equal to the Account ID specified via note inputs.
  # - The same non-fungible asset already exists in the account.
  # - Adding a fungible asset would result in amount overflow, i.e., the total amount would be
  #   greater than 2^63.
  begin
      # drop the transaction script root
      dropw
      # => []

      # load the note inputs to memory starting at address 0
      push.0 exec.note::get_inputs
        # => [inputs_ptr]

      # read the target account id from the note inputs
      mem_load
      # => [target_account_id]

      exec.account::get_id
      # => [account_id, target_account_id, ...]

      # ensure account_id = target_account_id, fails otherwise
      assert_eq
      # => [...]

      exec.add_note_assets_to_account
      # => [...]
  end
  ```

  Every note script starts with the note script root on top of the stack. After the `dropw`, the stack is cleared. Next, the script stored the note inputs at pos 0 in the [relative note context memory](https://0xpolygonmiden.github.io/miden-base/transactions/transaction-procedures.html#transaction-contexts) by  `push.0 exec.note::get_inputs`. Then, `mem_load` loads a `Felt` from the specified memory address and puts it on top of the stack, in that cases the   `target_account_id` defined by the creator of the note. Now, the note invokes `get_id` from the account API using `exec.account::get_id` - which is   possible even in the note context. Because, there are two account IDs on top of the stack now, `assert_eq` fails if the two account IDs (target_account_id and executing_account_id) are not the same. That means, the script cannot be successfully executed if executed by any other account than the account specified by the note creator using the note inputs.

  If execution hasn't failed, the script invokes a helper procedure `exec.add_note_assets_to_account` to add the note's assets into the executing account's vault.

  #### Add assets
  This procedure adds the assets held by the note into the account's vault.

  ```
  #! Helper procedure to add all assets of a note to an account.
  #!
  #! Inputs: []
  #! Outputs: []
  #!
  proc.add_note_assets_to_account
      push.0 exec.note::get_assets
      # => [num_of_assets, 0 = ptr, ...]

      # compute the pointer at which we should stop iterating
      dup.1 add
      # => [end_ptr, ptr, ...]

      # pad the stack and move the pointer to the top
      padw movup.5
      # => [ptr, 0, 0, 0, 0, end_ptr, ...]

      # compute the loop latch
      dup dup.6 neq
      # => [latch, ptr, 0, 0, 0, 0, end_ptr, ...]

      while.true
          # => [ptr, 0, 0, 0, 0, end_ptr, ...]

          # save the pointer so that we can use it later
          dup movdn.5
          # => [ptr, 0, 0, 0, 0, ptr, end_ptr, ...]

          # load the asset and add it to the account
          mem_loadw call.wallet::receive_asset
          # => [ASSET, ptr, end_ptr, ...]

          # increment the pointer and compare it to the end_ptr
          movup.4 add.1 dup dup.6 neq
          # => [latch, ptr+1, ASSET, end_ptr, ...]
      end

      # clear the stack
      drop dropw drop
  end
  ```

  The procedure starts by calling `exec.note::get_assets`. As with the note's inputs before, this writes the assets of the note into memory starting at the specified address. Assets are stored in consecutive memory slots, so `dup.1 add` provides the last memory slot.

  In Miden, [assets](assets.md) are represented by `Words`, so we need to pad the stack with four `0`s to make room for an asset. Now, if there is at least one asset (checked by `dup dup.6 neq`), the loop starts. It first saves the pointer for later use (`dup movdn.5`), then loads the first asset `mem_loadw` on top of the stack.

  Now, the procedure calls the a function of the account interface `call.wallet::receive_asset` to put the asset into the account's vault. Due to different [contexts](https://0xpolygonmiden.github.io/miden-base/transactions/transaction-procedures.html#transaction-contexts), a note script cannot directly call an account function to add the asset. The account must expose this function in its [interface](https://0xpolygonmiden.github.io/miden-base/architecture/accounts.html#example-account-code).

  Lastly, the pointer gets incremented, and if there is a second asset, the loop continues (`movup.4 add.1 dup dup.6 neq`). Finally, when all assets were put into the account's vault, the stack is cleared (`drop dropw drop`).

</details>

## Note storage mode
Similar to accounts, there are two storage modes for notes in Miden. Notes can be stored on-chain in the [Note DB](https://0xpolygonmiden.github.io/miden-base/architecture/state.html#notes-database) with all data publicly visible for everyone. Alternatively, notes can be stored off-chain by committing only the note hash to the Note DB.

Every note has a unique note hash. It is defined as follows:

```
hash(hash(hash(hash(serial_num, [0; 4]), script_hash), input_hash), vault_hash)
```

_Info: To compute a note's hash, we do not need to know the note's `serial_num`. Knowing the hash of the `serial_num` (as well as `script_hash`, `input_hash` and `note_vault`) is also sufficient. We compute the hash of `serial_num` as `hash(serial_num, [0; 4])` to simplify processing within the VM._

## Note discovery
Note discovery describes the process of Miden clients finding notes they want to consume. There are two ways to receive new relevant notes - getting notes via an off-chain channel or querying the Miden operator to request newly recorded relevant notes.
The latter is done via note tags. Tags are part of the note's metadata and are represented by a `Felt`. The `SyncState` API of the Miden node requires the Miden client to provide a `note_tag` value which is used as a filter in the operator's response. Tags are useful for note discovery enabling an easy collection of all notes matching a certain tag.

## Note consumption
As with creation, notes can only be consumed in Miden transactions. If a valid transaction consuming an `InputNote` gets verified by the Miden node, the note's unique nullifier gets added to the [Nullifier DB](https://0xpolygonmiden.github.io/miden-base/architecture/state.html#nullifier-database) and is therefore consumed.

Notes can only be consumed if the note data is known to the consumer. The note data must be provided as input to the [transaction kernel](transactions/kernel.md). That means, for privately stored notes, there must be some off-chain communication to transmit the note's data from the sender to the target.

### Note recipient to restrict note consumption
There are several ways to restrict the set of accounts that can consume a specific note. One way is to specifically define the target account ID as done in the P2ID and P2IDR note scripts. Another way is by using the concept of a `RECIPIENT`. Miden defines a `RECIPIENT` (represented as `Word`) as:

```
hash(hash(hash(serial_num, [0; 4]), script_hash), input_hash)
```

This concept restricts note consumption to those users who know the pre-image data of `RECIPIENT` - which might be a bigger set than a single account.

During the [transaction prologue](transactions/kernel.md) the users needs to provide all the data to compute the note hash. That means, one can create notes that can only be consumed if the `serial_num` and other data is known. This information can be passed on off-chain by the sender to the consumer. This is only useful with private notes.For public notes, all note data is known, and anyone can compute the `RECIPIENT`.

You can see in the standard [SWAP note script](https://github.com/0xPolygonMiden/miden-base/blob/main/miden-lib/asm/note_scripts/SWAP.masm) how `RECIPIENT` is used. Here, using a single hash, is sufficient to ensure that the swapped asset and its note can only be consumed by the defined target.

### Note nullifier to ensure private consumption
The note's nullifier is computed as:

```
hash(serial_num, script_hash, input_hash, vault_hash)
```

This achieves the following properties:
- Every note can be reduced to a single unique nullifier.
- One cannot derive a note's hash from its nullifier.
- To compute the nullifier, one must know all components of the note: `serial_num`, `script_hash`, `input_hash`, and `vault_hash`.

That means if a note is private and the operator stores only the note's hash, only those with the note details know if this note has been consumed already. Zcash first [introduced](https://zcash.github.io/orchard/design/nullifiers.html#nullifiers) this approach.

<center>
![Architecture core concepts](../img/architecture/note/nullifier.png)
</center>