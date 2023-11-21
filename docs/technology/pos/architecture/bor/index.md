# Bor

Polygon PoS uses dual-consensus architecture on the Polygon Network to optimise for speed and decentralisation.

## Architecture

<img src={useBaseUrl("img/Bor/matic_structure.png")}/>

A blockchain is a set of network clients interacting and working together. The client is a piece of software capable of establishing a p2p communication channel with other clients, signing and broadcasting transactions, deploying and interacting with smart contracts, etc. The client is often referred to as a node.

For Polygon, the node is designed with a two layer implementation Heimdall (Validator Layer) and Bor(Block Producer Layer).

1. Heimdall
    - Proof-of-Stake verification
    - Checkpointing blocks on Ethereum main chain
    - Validator and Rewards Management
    - Ensuring Sync with Ethereum main chain
    - Decentralised Bridge
2. Bor
    - Polygon Chain
    - EVM Compatible VM
    - Proposers and Producer set selection
    - SystemCall
    - Fee Model

## Heimdall (Validator layer)

Heimdall (the All-Protector) is the purveyor of all that happens in the Polygon Proof-of-Stake system – good or bad.

Heimdall is our Proof-of-Stake Verifier layer, which is responsible for checkpointing a representation of the blocks to the main chain in our architecture. We have implemented this by building on top of the Tendermint consensus engine with changes to the signature scheme and various data structures.

For more information, please read [https://blog.matic.network/heimdall-and-bor-matic-validator-and-block-production-layers/](https://blog.matic.network/heimdall-and-bor-matic-validator-and-block-production-layers/).

## Bor (Block Producer layer)

The Bor node implementation is basically the EVM-compatible blockchain operator. Currently, it is a basic Geth implementation with custom changes done to the consensus algorithm. However, this will be built from the ground up to make it lightweight and focused.

Bor is our Block producer layer, which in sync with Heimdall selects the producers and verifiers for each span and sprint.

### Polygon Chain

This chain is a separate blockchain that is attached to Ethereum using a two-way peg. The two-way peg enables interchangeability of assets between the Ethereum and Polygon.

### EVM Compatible VM

The Ethereum Virtual Machine (EVM) is a powerful, sandboxed virtual stack embedded within each full Polygon node, responsible for executing contract bytecode. Contracts are typically written in higher level languages, like Solidity, then compiled to EVM bytecode.

### Proposers and Producers Selection

Block Producers for the Bor layer are a committee selected from the Validator pool on the basis of their stake, which happens at regular intervals and is shuffled periodically. These intervals are decided by the Validator's governance with regards to dynasty and network.

Ratio of Stake/Staking power specifies the probability to be selected as a member of the block producer committee.

<img src={useBaseUrl("img/Bor/bor-span.png")} />

#### Selection Process

- Let's suppose we have 3 validators in pool, and they are Alice, Bill and Clara.
- Alice staked 100 Matic tokens whereas Bill and Clara staked 40 Matic tokens.
- Validators are given slots according to the stake, as Alice has 100 Matic tokens staked, she will get slots proportionally. Alice will get 5 slots in total. Similarly, Bill and Clara get 2 slots in total.
- All the validators are given these slots [ A, A, A, A, A, B, B, C, C ]
- Using historical Ethereum block data as seed, we shuffle this array.
- After shuffling the slots using the seed, say we get this array [ A, B, A, A, C, B, A, A, C]
- Now depending on Producer count*(maintained by validator's governance)*, we pop validators from the top. For e.g. if we want to select 5 producers we get the producer set as [ A, B, A, A, C]
- Hence the producer set for the next span is defined as [ A: 3, B:1, C:1 ].
- Using this validator set and tendermint's proposer selection algorithm we choose a producer for every sprint on BOR.

### SystemCall Interface

System call is an internal operator address which is under EVM. This helps to maintain the state for Block Producers for every sprint. A System Call is triggered towards the end of a sprint and a request is made for the new list of Block Producers. Once the state is updated, changes are received after block generation on Bor to all the Validators.

### Functions

#### proposeState

- Call is only allowed to validators.
- Inspect `stateId` if it is already proposed or committed.
- Propose the `stateId` and update the flag to `true`.

#### commitState

- Call is only allowed to System.
- Inspect `stateId` if it is already proposed or committed.
- Notify `StateReceiver` Contract with new `stateId`.
- Update the `state` flag to `true`, And `remove` the `proposedState`.

#### proposeSpan

- Call is only allowed to validators.
- Check if the Span proposal is `pending`.
- Update the Span Proposal to `true`

#### proposeCommit

- Call is only allowed to System.
- Set `initial validators` if current span is zero.
- Check Conditions for `spanId` and `time_period` of Sprint and Span.
- Update the new `span` and `time_period`.
- Set `validators` and `blockProducers` for the `sprint`.
- Update the flag for `spanProposal` to `true`.

### Bor Fee Model

For normal transaction, fees in Matic token gets collected and distributed to block producers, similar to Ethereum transactions.

Like other blockchains, Polygon has a native token called Matic(MATIC). MATIC is an ERC20 token used primarily for paying gas(transaction fees) on Polygon and staking.

:::info

An important thing to note is that on the Polygon chain, the MATIC tokens works as an ERC20 token, but also as the native token - both at the same time. Therefore, this means that a user can pay gas with MATIC as well as send MATIC to other accounts.

:::

For genesis-contracts, `gasPrice` and `gasLimit` works same as Ethereum, but during the execution it won't deduct the fees from sender's account.

Genesis transactions from current validators are executed with `gasPrice = 0`.

Also, validators have to send following types of transaction like State proposals like deposits & Span proposals on Bor.

## Technical Insight

### Genesis Contracts

[BorValidatorSet(0x1000)](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/BorValidatorSet.template) ⇒ This contract manages validator set for each span and sprint.

[BorStateReceiver(0x1001)](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/StateReceiver.sol) ⇒ This Contract manages the transfer of arbitrary contract data from Ethereum contracts to Polygon contracts

MaticChildERC20(0x1010) ⇒ Child Contract for Main Chain tokens which allows to move assets from Ethereum to Polygon.

### [Bor.go](https://github.com/maticnetwork/bor/blob/master/consensus/bor/bor.go)

Bor Protocol

## Glossary

- StartEpoch - Checkpoint number post which a validator is activated and will participate in the consensus.
- EndEpoch - Checkpoint number post which a validator is considered deactivated and won't participate in the consensus.
- Sprint - Sprint is a continuous set of blocks created by a single validator.
- Span -  Span is a big set of blocks with a fixed validator set but consisting of various sprints. For eg for a span of length 1600 blocks it will consist of 100 sprints of 16 blocks.
- Dynasty: Time between the end of last auction and start time of next auction.

## Resources

- [Bor](https://github.com/maticnetwork/bor)
- [EVM](https://www.bitrates.com/guides/ethereum/what-is-the-unstoppable-world-computer)
- [How EVM Works?](https://medium.com/mycrypto/the-ethereum-virtual-machine-how-does-it-work-9abac2b7c9e)
- [Tendermint Proposer Selection](https://docs.tendermint.com/master/spec/reactors/consensus/proposer-selection.html)
