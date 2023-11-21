---
id: bor-chain
title: Bor Chain
description: Polygon network block producer
keywords:
  - docs
  - polygon
  - matic
  - bor
  - bor chain
  - go ethereum
  - block producer
slug: bor-chain
image: https://wiki.polygon.technology/img/polygon-logo.png
---

The Bor node or the block producer implementation is the EVM-compatible blockchain operator.

Currently, Bor is a basic Geth implementation with custom changes done to the consensus algorithm.

Block producers are chosen from the validator set and are shuffled using historical Ethereum block hashes.

See also [Bor architecture](/docs/pos/design/bor/overview).



---
id: checkpoint-mechanism
title: Checkpoint Mechanism
sidebar_label: Checkpoints
description: Checkpointing the system state to the Ethereum mainnet
keywords:
  - docs
  - matic
  - polygon
  - checkpoint
  - ethereum
  - mainnet
slug: checkpoint-mechanism
image: https://wiki.polygon.technology/img/polygon-logo.png
---

:::info Polygon is not a Layer 1 platform

Polygon depends on the Ethereum Mainnet as its Layer 1 Settlement Layer. All staking mechanics need to be in sync with the contracts on the Ethereum mainnet.

:::

Proposers for a checkpoint are initially selected via [Tendermint’s weighted round-robin algorithm](https://docs.tendermint.com/master/spec/consensus/proposer-selection.html). A further custom check is implemented based on the checkpoint submission success. This allows the Polygon system to decouple with Tendermint proposer selection and provides Polygon with abilities like selecting a proposer only when the checkpoint transaction on the Ethereum mainnet succeeds or submitting a checkpoint transaction for the blocks belonging to previous failed checkpoints.

Successfully submitting a checkpoint on Tendermint is a 2-phase commit process:

* A proposer, selected via the round-robin algorithm, sends a checkpoint with the proposer's address and the Merkle hash in the proposer field.
* All other proposers validate the data in the proposer field before adding the Merkle hash in their state.

The next proposer then sends an acknowledgment transaction to prove that the previous checkpoint transaction has succeeded on the Ethereum mainnet. Every validator set change is relayed by the validator nodes on Heimdall which is embedded onto the validator node. This allows Heimdall to remain in sync with the Polygon contract state on the Ethereum mainnet at all times.

The Polygon contract deployed on the Ethereum mainnet is considered to be the ultimate source of truth, and therefore all validation is done via querying the Ethereum mainnet contract.




---
id: derivatives
title: Derivatives
description: Delegation through validator shares
keywords:
  - docs
  - polygon
  - matic
  - derivatives
  - delegation
  - shares
slug: derivatives
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Polygon supports delegation via validator shares. By using this design, it is easier to distribute rewards and slash with scale on the Ethereum mainnet contracts without much computation.

Delegators delegate by purchasing shares of a finite pool from validators. Each validator has their own validator share token.

Let's call the fungible validator share tokens VATIC for Validator A. When a user delegates to Validator A, the user is issued VATIC based on the exchange rate of the MATIC-VATIC pair. As users accrue value, the exchange rate indicates that the user can withdraw more MATIC for each VATIC. When validators get slashed, users withdraw less MATIC for their VATIC.

Note that MATIC is the staking token. A delegator needs to have MATIC tokens to participate in the delegation.

Initially, Delegator D buys tokens from the Validator A specific pool when the exchange rate is 1 MATIC per 1 VATIC.

When a validator gets rewarded with more MATIC tokens, the new tokens are added to the pool.

Let's say with the current pool of 100 MATIC tokens,  10 MATIC rewards are added to the pool. Since the total supply of VATIC tokens did not change due to the rewards, the exchange rate becomes 1 MATIC per 0.9 VATIC. Now, Delegator D gets more MATIC for the same amount if shares.

## The flow in the contract

`buyVoucher`: This function is attributed when performing a delegation process towards a validator. The delegation `_amount` is first transferred to `stakeManager`, which on confirmation mints delegation shares via `Mint` using the current `exchangeRate`.

The exchange rate is calculated as per the formula:

`ExchangeRate = (totalDelegatedPower + delegatorRewardPool) / totalDelegatorShares`

`sellVoucher`: This is function that is called when a delegator is unbonding from a validator. This function basically initiates the process of selling the vouchers bought during delegation. There is a withdrawal period that is taken into consideration before the delegators can `claim` their tokens.

`withdrawRewards`: As a delegator, you can claim your rewards by invoking the `withdrawRewards` function.

`reStake`: Restaking can work in two ways: a) delegator can buy more shares using `buyVoucher` or `reStake` rewards. You can restake by staking more tokens towarda a validator or you can restake your accumulated rewards as a delegator. Purpose of `reStaking` is that since delegator's validator has now more active stake, they will earn more rewards for that and so will the delegator.

`unStakeClaimTokens`: Once the withdrawal period is over, the delegators who sold their shares can claim their MATIC tokens.

`updateCommissionRate`: Updates the commission % for the validator. See also [Validator Commission Operations](/docs/pos/validator/validator-commission-operations).

`updateRewards`: When a validator gets rewards for submitting a checkpoint, this function is called for disbursements of rewards between the validator and delegators.



---
id: heimdall-chain
title: Heimdall Chain
description: Proof-of-stake verifier layer on the Polygon Network
keywords:
  - docs
  - polygon
  - matic
  - heimdall
  - chain
  - verifier
  - layer
  - proof of stake
slug: heimdall-chain
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Heimdall is the proof-of-stake verifier layer, which is responsible for checkpointing the representation of blocks to the Ethereum mainnet. Heimdall is based on [Tendermint](https://tendermint.com/).

The staking contract on the Ethereum mainnet works in conjunction with the Heimdall node to act as the trustless stake management mechanism for the PoS engine, including selecting the validator set, updating validators, etc. Since staking is done in the contract on the Ethereum mainnet, Polygon does not rely only on validator honesty and instead inherits the Ethereum mainnet security.

Heimdall layer handles the aggregation of blocks produced by Bor into a Merkle tree and publishes the Merkle root periodically to the Ethereum mainnet. This periodic publishing is called *checkpointing*.

For every few blocks on Bor, a validator (on the Heimdall layer):

1. Validates all the blocks since the last checkpoint.
2. Creates a Merkle tree of the block hashes.
3. Publishes the Merkle root to the Ethereum mainnet.

Checkpoints are important for two reasons:

1. Providing finality on the root chain.
2. Providing proof of burn in withdrawal of assets.

An overview of the process:

* A subset of active validators from the pool is selected to act as block producers for a span. These block producers are responsible for creating blocks and broadcasting the created blocks on the network.
* A checkpoint includes the Merkle root hash of all blocks created during any given interval. All nodes validate the Merkle root hash and attach their signature to it.
* A selected proposer from the validator set is responsible for collecting all signatures for a particular checkpoint and committing the checkpoint on the Ethereum mainnet.
* The responsibility of creating blocks and proposing checkpoints is variably dependent on a validator’s stake ratio in the overall pool.

See also [Heimdall architecture](/docs/pos/design/heimdall/overview).



---
id: key-management
title: Key Management
description: Signer and owner keys management
keywords:
  - docs
  - polygon
  - matic
  - key
  - key management
  - signer
  - owner
slug: key-management
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Each validator uses two keys to manage validator related activities on Polygon:

* Signer key
* Owner key

## Signer Key

The signer key is the address used to sign Heimdall blocks, checkpoints, and other signing related activities.

The signer address's private key must be located on the machine running the validator node for signing purposes.

The signer key cannot manage staking, rewards, or delegations.

The validator must keep ETH on the signer address on the Ethereum mainnet to send checkpoints.

## Owner Key

The owner key is the address used to stake, restake, change the signer key, withdraw rewards and manage delegation related parameters on the Ethereum mainnet. The private key for the owner key must be secure at all costs.

All transactions through the owner key are performed on the Ethereum mainnet.

The signer key is kept on the node and is generally considered a **hot** wallet, whereas the owner key is supposed to kept very secure, is used infrequently, and is generally considered a **cold** wallet. The staked funds are controlled by the owner key.

This separation of responsibilities between the signer and the owner keys is done to ensure an efficient tradeoff between security and ease of use.

Both keys are Ethereum compatible addresses and work in the exactl the same manner.

## Signer Change

See [Change Your Signer Address](/docs/pos/validator/change-signer-address).



---
id: proposer-bonus
title: Proposer Bonus
description: Additional incentive of being a validator
keywords:
  - docs
  - polygon
  - matic
  - validate
  - proposer
  - bonus
  - incentive
slug: proposer-bonus
image: https://wiki.polygon.technology/img/polygon-logo.png
---

# Proposer Bonus

In Polygon, there is an additional element of committing periodic checkpoints to the Ethereum mainnet. This is a major part of the validator responsibilities and they are incentivized to perform this activity. This constitutes a cost to the validator which is unique to a Layer 2 solution such as Polygon. We strive to accommodate this cost in the validator staking reward payout mechanism as a bonus to be paid to the proposer, who is responsible for committing the checkpoint. Rewards minus the bonus is to be shared among all stakers; proposer and signers, proportionally.

To avail the bonus completely, the proposer must include all signatures in the checkpoint. Because the protocol desires ⅔ +1 weight of the total stake, the checkpoint is accepted even with 80% votes. However, in this case, the proposer gets only 80% of the calculated bonus.



---
id: proposers-producers-selection
title: Proposers & Producers Selection
sidebar_label: Proposers & Producers
description: Proposer & block producer selection on Polygon
keywords:
  - docs
  - polygon
  - matic
  - proposers
  - block producers
  - selection
slug: proposers-producers-selection
image: https://wiki.polygon.technology/img/polygon-logo.png
---
import useBaseUrl from '@docusaurus/useBaseUrl';

Block Producers for the BOR layer, are a committee selected from the Validators pool on the basis of their stake which happens at regular intervals. These intervals are decided by the Validator's governance with regards to dynasty and network.

The ratio of stake specifies the probability to be selected as a member of block producers committee.

## Selection Process

Let's suppose we have 3 validators in pool — Alice, Bill, and Clara:

* Alice is staking 100 MATIC tokens.
* Bill is staking 40 MATIC tokens.
* Clara is staking 40 MATIC tokens.

Validators are given slots according to the stake.

Because Alice has 100 MATIC tokens staked, and the per slot cost is 10 MATIC tokens as maintained by validator's governance, Alice gets 5 slots in total. Similarly, Bill and Clara get 2 slots in total.

The Alice, Bill and Clara validators are given the following slots:

* [ A, A, A, A, A, B, B, C, C ]

Polygon then shuffles the array of the Alice, Bill and Clara slots by using the Ethereum block hashes as seed.

The result of the shuffle is the following array of slots:

* [ A, B, A, A, C, B, A, A, C]

Now depending on the total block producer count as maintained by validator's governance, Polygon uses the validators from the top — for example. for a set of 5 producers the array of slots is [ A, B, A, A, C].

The producer set for the next span is defined as [ A: 3, B:1, C:1 ].

Using the resulting validator set and Tendermint's [proposer selection algorithm](https://docs.tendermint.com/master/spec/consensus/proposer-selection.html), Polygon selects a producer for every sprint on Bor.

<img src={useBaseUrl("img/validators/producer-proposer.png")} />

**Legend:**

* Dynasty: Time between the end of the last auction and start time of the next auction.
* Sprint: Time interval for which the block producers committee is selected.
* Span: Number of blocks produced by a single producer.



---
id: staking
title: Staking
sidebar_label: Staking
description: Stake, unstake, and restake as a validator
keywords:
  - docs
  - matic
  - polygon
  - staking
  - unstake
  - restake
  - validator
slug: staking
image: https://wiki.polygon.technology/img/polygon-logo.png
---

For Polygon Network, any participant can be qualified to become a Polygon's validator by running a full node to earn rewards and collect transaction fees. To ensure the good participation by validators, they lock up some of their MATIC tokens as a stake in the ecosystem.

Validators in Polygon Network are selected via an on-chain auction process which happens at regular intervals.

A validator has two addresses an owner address and a signer address. The staking is done with the owner address.

See also [Key Management](key-management.md).

## Stake

:::note

Currently there is limited space to accept new validators.

To join the validator set, you must submit an application through our Validator Admissions process. See: https://polygoncommunity.typeform.com/validatorshub

An approved validator can only join the active set when a currently active validator unbonds.

For more information on the current admissions process, please see: https://discourse-forum.polygon.technology/t/update-pos-validator-admissions/12344

:::


## Unstake

Unstaking removes the validator from the active set of validators.

To ensure good participation, the validator stake is locked for 80 checkpoints.

## Restake

Validators can add more MATIC tokens to their stake:

* To earn more rewards.
* To maintain the position in the validator set.



---
id: state-sync-mechanism
title: State Sync Mechanism
description: State sync mechanism to natively read Ethereum data
keywords:
  - docs
  - matic
  - polygon
  - state sync
  - mechanism
slug: state-sync-mechanism
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Validators on the Heimdall layer pick up the [StateSynced](https://github.com/maticnetwork/contracts/blob/a4c26d59ca6e842af2b8d2265be1da15189e29a4/contracts/root/stateSyncer/StateSender.sol#L24) event and pass the event on to the Bor layer. See also [Polygon Architecture](/docs/pos/polygon-architecture).

The **receiver contract** inherits [IStateReceiver](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol), and custom logic sits inside the [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/05556cfd91a6879a8190a6828428f50e4912ee1a/contracts/IStateReceiver.sol#L5) function.

The latest version, [Heimdall v0.3.4](https://github.com/maticnetwork/heimdall/releases/tag/v0.3.4), contains a few enhancements such as:
1. Restricting data size in state sync txs to:
    * **30Kb** when represented in **bytes**
    * **60Kb** when represented as **string**.
2. Increasing the **delay time** between the contract events of different validators to ensure that the mempool doesn't get filled very quickly in case of a burst of events which can hamper the progress of the chain.

The following example shows how the data size is restricted:

```
Data - "abcd1234"
Length in string format - 8
Hex Byte representation - [171 205 18 52]
Length in byte format - 4
```

## Requirements for the users

Things required from dapps/users to work with state-sync are:

1. Call the [syncState](https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33) function.
2. The `syncState` function emits an event called `StateSynced(uint256 indexed id, address indexed contractAddress, bytes data);`
3. All the validators on the Heimdall chain receive the `StateSynced` event. Any validator that wishes to get the transaction fee for the state sync sends the transaction to Heimdall.
4. Once the `state-sync` transaction on Heimdall is included in a block, it is added to the pending state-sync list.
5. After every sprint on Bor, the Bor node fetches the pending state-sync events from Heimdall via an API call.
6. The receiver contract inherits the `IStateReceiver` interface, and custom logic of decoding the data bytes and performing any action sits inside the [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol) function.



---
id: transaction-fees
title: Transaction Fees
description: Distribution of fees among all validators on Heimdall
keywords:
  - docs
  - polygon
  - matic
  - validator
  - transaction
  - fees
slug: transaction-fees
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Each block producer on the Bor layer is given a certain percentage of the transaction fees collected in each block.

The selection of producers for any given span is dependent on the validator’s ratio in the overall stake. The remaining transaction fees flow through the same funnel as the rewards which get shared among all validators working at the Heimdall layer.
