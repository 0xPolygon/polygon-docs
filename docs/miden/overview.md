Polygon Miden is a zero-knowledge rollup for private, high-throughput applications.

It is a modular execution layer that extends Ethereum's capabilities using powerful features such as parallel transaction execution and client-side proving. 

Miden allows users to prove state changes locally while the network only tracks a commitment, leading to privacy and high-throughput. Users can also let the operator prove public state changes like other rollups.

With Miden, developers can create novel, high-throughput, privacy-preserving dApps for DeFi, RWA, and on-chain games with languages such as Rust and TypeScript.

If you want to join the technical discussion, please check out the following:

* [Discord](https://discord.gg/0xpolygondevs)
* [Miden repo](https://github.com/0xPolygonMiden)
* [Roadmap](introduction/roadmap.md)

!!! info
    - These docs are still work-in-progress. 
    - Some topics have been discussed in greater depth, while others require additional clarification. 

## Status and features

Polygon Miden is currently on release v0.2. This is an early version of the protocol and its components. 

!!! important
    We expect breaking changes on all components.

At the time of writing, Polygon Miden doesn't offer all the features you may expect from a zkRollup. During 2024, we expect to gradually implement more features. 

### Feature highlights

#### Private accounts

The Miden operator only tracks a commitment to account data in the public database. Users can only execute smart contracts when they know the interface.

#### Private notes

Like private accounts, the Miden operator only tracks a commitment to notes in the public database. Users need to communicate note details to each other off-chain (via a side channel) in order to consume private notes in transactions.

#### Public accounts

Polygon Miden supports public smart contracts like Ethereum. The code and state of those accounts is visible to the network and anyone can execute transactions against them.

#### Public notes

As with public accounts, public notes are also supported. That means, the Miden operator publicly stores note data. Note consumption is not private.

#### Local transaction execution 

The Miden client allows for local transaction execution and proving. The Miden operator verifies the proof and, if valid, updates the state DBs with the new data.

#### Simple smart contracts

Currently, there are three different smart contracts available. A basic wallet smart contract that sends and receives assets, and fungible and non-fungible faucets to mint and burn assets. 

All accounts are written in [MASM](https://0xpolygonmiden.github.io/miden-vm/user_docs/assembly/main.html).

#### P2ID, P2IDR, and SWAP note scripts

Currently, there are three different note scripts available. Two different versions of pay-to-id scripts of which P2IDR is reclaimable, and a swap script that allows for simple token swaps.

#### Simple block building

The Miden operator running the Miden node builds the blocks containing transactions. 

#### Maintaining state

The Miden node stores all necessary information in its state DBs and provides this information via its RPC endpoints.

### Planned features

!!! warning
    The following features are at a planning stage only.

#### Customized smart contracts

Accounts can expose any interface in the future. This is the Miden version of a smart contract. Account code can be arbitrarily complex due to the underlying Turing-complete [Miden VM](https://0xpolygonmiden.github.io/miden-vm/intro/main.html).

#### Customized note scripts

Users will be able to write their own note scripts using the Miden client. Note scripts are executed during note consumption and they can be arbitrarily complex due to the underlying Turing-complete Miden VM.

#### Network transactions

Transaction execution and proving can be outsourced to the network and to the Miden operator. Those transactions will be necessary when it comes to public shared state, and they can be useful if the user's device is not powerful enough to prove transactions efficiently.

#### Rust compiler

In order to write account code, note or transaction scripts, in Rust, there will be a Rust -> Miden Assembly compiler.

#### Block and epoch proofs

The Miden node will recursively verify transactions and in doing so build batches of transactions, blocks, and epochs.

## Benefits of Polygon Miden

* Ethereum security.
* Developers can build applications that are infeasible on other systems. For example:
    * **on-chain order book exchange** due to parallel transaction execution and updatable transactions.
    * **complex, incomplete information games** due to client-side proving and cheap complex computations.
    * **safe wallets** due to hidden account state.
* Better privacy properties than on Ethereum - first web2 privacy, later even stronger privacy guarantees.
* Transactions can be recalled and updated.
* Lower fees due to client-side proving.
* dApps on Miden are safe to use due to account abstraction and compile-time safe Rust smart contracts.

## License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).
