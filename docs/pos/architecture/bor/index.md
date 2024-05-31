Bor is an integral component of the Polygon network that operates based on principles derived from the *Clique consensus protocol*, detailed in [EIP-225](https://eips.ethereum.org/EIPS/eip-225). This consensus model is characterized by predefined block producers who collectively participate in a voting process to appoint new producers, taking turns in block generation.

## Proposers and producers selection

Block producers for the Bor layer are a committee selected from the validator pool on the basis of their stake, which happens at regular intervals and is shuffled periodically. These intervals are decided by the validator's governance with regard to dynasty and network.

The ratio of stake/staking power specifies the probability to be selected as a member of the block producer committee.

#### Selection process

1. Validators are given slots proportionally according to their stake.
2. Using historical Ethereum block data as seed, we shuffle this array.
3. Now depending on Producer count*(maintained by validator's governance)*, validators are taken from the top.
4. Using this validator set and Tendermint's proposer selection algorithm, we choose a producer for every sprint on Bor.

## Detailed mechanics of Bor consensus

### Validators in Polygon's Proof-of-Stake system

In Polygon's Proof-of-Stake (PoS) framework, participants can stake MATIC tokens on a designated Ethereum smart contract, known as the "staking contract," to become validators. Active validators on Heimdall are eligible for selection as block producers through the Bor module.

### Span: Defining validator sets and voting power

A span is a defined set of blocks, during which a specific subset of validators is selected from the broader validator pool. Heimdall provides intricate details of each span through its span-details APIs. Within a span, each validator is assigned a certain voting power. The probability of a validator being chosen as a block producer is directly proportional to their voting power. The selection algorithm for block producers is borrowed from Tendermint's consensus protocol.

### Sprint: Single block producer selection within a span

Within a span, a sprint is a smaller subset of blocks. For each sprint, only one block producer is selected to generate blocks. The size of a sprint is a fraction of the overall span size. Bor also designates backup producers, ready to step in if the primary producer is unable to fulfill its role.

### Block authorization by producers

Block producers in Bor are also referred to as signers. To authorize a block, a producer signs the block's hash, encompassing all components of the block header except the signature itself. This signature is generated using the `secp256k1` elliptic curve algorithm and is appended to the `extraData` field of the block header.

Each block is assigned a difficulty level. Blocks signed in-turn (by the designated producer) are given a higher difficulty (`DIFF_INTURN`) compared to out-of-turn signatures (`DIFF_NOTURN`).

#### Handling out-of-turn signing

Bor selects multiple backup producers to address situations where the designated producer fails to generate a block. This failure could be due to various reasons, including technical issues, intentional withholding, or other disruptions. The backup mechanism is activated based on a sequential order of validators and a predefined delay known as the "wiggle" time.

#### Wiggle time: Delay before backup production

Wiggle time is the predefined delay a backup producer waits before starting to generate a block. This delay is calculated based on the last block's production time and a variable parameter known as `Period`. The wiggle time is dynamically adjusted based on the position of the backup producer in the validator sequence relative to the designated producer's position.

#### Resolving forks with difficulty metrics

The potential for forks arises when backup producers generate blocks due to delays in block propagation. Bor addresses this by selecting the fork with the highest cumulative difficulty, reflecting the sequence of in-turn block production. The difficulty of a block is determined based on the validator's turn to produce the block, with in-turn production assigned the highest difficulty.

### View change and span commitment

At the end of each span, Bor undergoes a view change, fetching new producers for the subsequent span. This involves an HTTP call to the Heimdall node to retrieve new span data and a `commitSpan` call to the `BorValidatorSet` genesis contract. Block headers in Bor are also structured to include producer bytes, aiding in the fast-syncing process.

### State synchronization with the Ethereum chain

Bor features a mechanism to relay specific events from the Ethereum chain to Bor. This involves:

1. Contracts on Ethereum triggering the `StateSynced` event via `StateSender.sol`.
2. Heimdall monitoring these events and proposing state changes through `StateReceiver.sol`.
3. Bor committing these state changes at the start of every sprint, ensuring synchronization with the Ethereum chain's state.

This state sync process is a crucial aspect of maintaining consistency between the Ethereum and Bor chains, ensuring that relevant state changes on Ethereum are reflected in Bor's state.
