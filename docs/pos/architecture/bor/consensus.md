# Consensus in Bor

Bor consensus is inspired by Clique consensus: [https://eips.ethereum.org/EIPS/eip-225](https://eips.ethereum.org/EIPS/eip-225). Clique works with multiple pre-defined producers. All producers vote on new producers using Clique APIs. They take turns creating blocks.

Bor fetches new producers through span and a sprint management mechanism.

## Validators

Polygon is a Proof-of-stake system. Anyone can stake their Matic token on Ethereum smart-contract, "staking contract", and become a validator for the system.

Once validators are active on Heimdall they get selected as producers through `bor` module.

## Span

A logically defined set of blocks for which a set of validators is chosen from among all the available validators. Heimdall provides span details through span-details APIs.

Each validator in span contains voting power. Based on their power, they get selected as block producers. Higher power, a higher probability of becoming block producers. Bor uses Tendermint's algorithm for the same. 

## Sprint

A set of blocks within a span for which only a single block producer is chosen to produce blocks. The sprint size is a factor of span size. 

Apart from the current proposer, Bor also selects back-up producers.

## Authorizing a block

The producers in Bor are also called signers, since to authorize a block for the network, the producer needs to sign the block's hash containing **everything except the signature itself**. This means that the hash contains every field of the header, and also the `extraData` with the exception of the 65-byte signature suffix.

This hash is signed using the standard `secp256k1` curve, and the resulting 65-byte signature is embedded into the `extraData` as the trailing 65-byte suffix.

Each signed block is assigned to a difficulty that puts weight on the Block. In-turn signing weighs more (`DIFF_INTURN) than out-of-turn one (`DIFF_NOTURN`).

### Out-of-turn signing

Bor chooses multiple block producers as a backup when an in-turn producer doesn't produce a block. This could happen for a variety of reasons:

- The block producer node is down
- The block producer is trying to withhold the block
- The block producer is not producing a block intentionally.

When the above happens, Bor's backup mechanism is used.

At any point in time, the validators set is stored as an array sorted based on their signer address. Assume, that the validator set is ordered as A, B, C, D and that it is C's turn to produce a block. If C doesn't produce a block within a sufficient amount of time, it becomes D's turn to produce one. If D doesn't, then A and then B.

However, since there will be some time before C produces and propagates a block, the backup validators will wait a certain amount of time before starting to produce a block. This time delay is called wiggle.

### Wiggle

Wiggle is the time that a producer should wait before starting to produce a block.

- Say the last block (n-1) was produced at time `t`.
- We enforce a minimum time delay between the current and next block by a variable parameter `Period`.
- In ideal conditions, C will wait for `Period` and then produce and propagate the block. Since block times in Polygon are being designed to be quite low (2-4s), the propagation delay is also assumed to be the same value as `Period`.
- So if D doesn't see a new block in time `2 * Period`, D immediately starts producing a block. Specifically, D's wiggle time is defined as `2 * Period * (pos(d) - pos(c))` where `pos(d) = 3` and `pos(c) = 2` in the validator set. Assuming, `Period = 1`, wiggle for D is 2s.
- Now if D also doesn't produce a block, A will start producing one when the wiggle time of `2 * Period * (pos(a) + len(validatorSet) - pos(c)) = 4s` has elapsed.
- Simmilary, wiggle for C is `6s`

### Resolving forks

While the above mechanism adds to the robustness of the chain to a certain extent, it introduces the possibility of forks. It could actually be possible that C produced a block, but there was a larger than expected delay in propagation and hence D also produced a block, so that leads to at least 2 forks.

The resolution is simple - choose the chain with higher difficulty. But then the question is how do we define difficulty of a block in our setup?

### Difficulty

- The difficulty for a block that is produced by an in-turn signer (say c) is defined to be the highest = `len(validatorSet)`.
- Since D is the producer who is next in line; if and when the situation arises that D is producing the block; the difficulty for the block will be defined just like in wiggle as `len(validatorSet) - (pos(d) - pos(c))` which is `len(validatorSet) - 1`
- Difficulty for block being produced by A while acting as a backup becomes `len(validatorSet) - (pos(a) + len(validatorSet) - pos(c))` which is `2`

Now having defined the difficulty of each block, the difficulty of a fork is simply the sum of the difficulties of the blocks in that fork. In the case when a fork has to be chosen, the one with higher difficulty is chosen, since that is a reflection of the fact that blocks were produced by in-turn block producers. This is simply to provide some sense of finality to the user on Bor.

## View Change

After each span, Bor changes view. It means that it fetches new producers for the next span.

### Commit span

When the current span is about to end (specifically at the end of the second-last sprint in the span), Bor pulls a new span from Heimdall. This is a simple HTTP call to the Heimdall node. Once this data is fetched, a `commitSpan` call is made to the BorValidatorSet genesis contract through System call.

Bor also sets producers bytes into the header of the block. This is necessary while fast-syncing Bor. During fast-sync, Bor syncs headers in bulk and validates if blocks are created by authorized producers.

At the start of each Sprint, Bor fetches header bytes from the previous header for next producers and starts creating blocks based on `ValidatorSet` algorithm.

Here is how header looks like for a block:

```js
header.Extra = header.Vanity + header.ProducerBytes /* optional */ + header.Seal
```

## State sync from Ethereum Chain

Bor provides a mechanism where some specific events on the main Ethereum chain are relayed to Bor.

1. Any contract on Ethereum may call [syncState](https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol#L33) in `StateSender.sol`. This call emits `StateSynced` event: https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol#L38

  ```js
  event StateSynced(uint256 indexed id, address indexed contractAddress, bytes data)
  ```

2. Heimdall listens to these events and calls `function proposeState(uint256 stateId)` in `StateReceiver.sol`  - thus acting as a store for the pending state change ids. Note that the `proposeState` transaction will be processed even with a 0 gas fee as long as it is made by one of the validators in the current validator set: https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/StateReceiver.sol#L24

3. At the start of every sprint, Bor pulls the details about the pending state changes using the states from Heimdall and commits them to the Bor state using a system call. See `commitState` here: https://github.com/maticnetwork/genesis-contracts/blob/f85d0409d2a99dff53617ad5429101d9937e3fc3/contracts/StateReceiver.sol#L41