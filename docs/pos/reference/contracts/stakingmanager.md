For the Polygon PoS Proof of Security based consensus, all the $2/3+1$ proof verification and handling of staking, rewards are executed on the Ethereum smart contract. The whole design follows this philosophy of doing less on the Mainnet contract. It does information verification and pushes all the computation-heavy operations to L2 (read about [Heimdall](https://docs.polygon.technology/pos/architecture/heimdall/)).

*Stakers* are divided into *validators*, *delegators*, and *watchers* (for fraud reporting).

[`StakeManager`](https://github.com/maticnetwork/contracts/blob/develop/contracts/staking/stakeManager/StakeManager.sol) is the main contract for handling validator related activities like `checkPoint` signature verification, reward distribution, and stake management. Since the contract is using *NFT ID* as a source of ownership, change of ownership and signer won't affect anything in the system.

!!! info
    
    From a single Ethereum address, *a staker can only function as either a validator or a delegator* (this is a design choice without any underlying technical constraints).


## Validator admissions/replacement

### Admissions

Currently, the system allows for a maximum of 105 active validators at any given time on Polygon PoS. There is also a waitlist to become a validator. New validators can join the active set only when a currently active validator unbonds or is removed due to low performance. You can apply to become a validator via the [Polygon validators hub](https://polygoncommunity.typeform.com/validatorshub).

Please note that submitting an application does not guarantee a validator slot. More relevant information is available on the [becoming a validator](../../get-started/becoming-a-validator.md) page.


### Replacement

[PIP4](https://forum.polygon.technology/t/pip-4-validator-performance-management/9956) introduced the concept of showcasing validator performance for community visibility. If a validator is in an unhealthy state for an extended period of time as outlined in PIP4, they are off-boarded from the network. The validator slot is then made available to those coming off of the waitlist.

Learn more about these requirements on the [validator performance requirements page](../../how-to/operate-validator-node/validator-performance.md).


## Methods and variables

### `validatorThreshold`

It stores the maximum number of validators accepted by the system, also called slots.

### `AccountStateRoot`

- For various accounting done on Heimdall for validators and delegator, account root is submitted while submitting the `checkpoint`.
- `accRoot` is used while `claimRewards` and `unStakeClaim`.

### `stake` / `stakeFor`

```solidity title="StakeManager.sol"
function stake(
    uint256 amount,
    uint256 heimdallFee,
    bool acceptDelegation,
    bytes calldata signerPubkey
) public;

function stakeFor(
    address user,
    uint256 amount,
    uint256 heimdallFee,
    bool acceptDelegation,
    bytes memory signerPubkey
) public;
```

- Allows anyone with amount (in MATIC tokens) greater than `minDeposit`, if `currentValidatorSetSize` is less then `validatorThreshold`.
- Must transfer `amount+heimdallFee`.
- `updateTimeLine` updates special timeline data structure, which keeps track of active validators and active stake for given epoch / checkpoint count.
- One unique `NFT` is minted on each new `stake` or `stakeFor` call, which can be transferred to anyone but can be owned 1:1 Ethereum address.
- `acceptDelegation` set to true if validators want to accept delegation, `ValidatorShare` contract is deployed for the validator.

### `unstake`

- Remove validator from validator set in next epoch (only valid for current checkpoint once called `unstake`)
- Remove validator's stake from timeline data structure, update count for validator's exit epoch.
- If validator had delegation on, collect all rewards and lock delegation contract for new delegations.

### `unstakeClaim`

```solidity
function unstakeClaim(uint256 validatorId) public;
```
Once `WITHDRAWAL_DELAY` period is served, validators can call this function and do settlement with `stakeManager` (get rewards if any, get staked tokens back, burn NFT, etc).

### `restake`

```solidity
function restake(uint256 validatorId, uint256 amount, bool stakeRewards) public;
```

- Allows validators to increase their stake by putting new amount or rewards or both.
- Must update timeline (amount) for active stake.

### `withdrawRewards`

```solidity
function withdrawRewards(uint256 validatorId) public;
```

This method allows validators to withdraw accumulated rewards, must consider getting rewards from delegation contract if validator accepts delegation.

### `updateSigner`

```solidity
function updateSigner(uint256 validatorId, bytes memory signerPubkey) public
```

This method allows validators to update signer address (which is used to validate blocks on Polygon blockchain and checkpoint signatures on `stakeManager`).

### `topUpForFee`

```solidity
function topUpForFee(uint256 validatorId, uint256 heimdallFee) public;
```

Validators can top-up their balance for Heimdall fee by invoking this method.

### `claimFee`

```solidity
function claimFee(
        uint256 validatorId,
        uint256 accumSlashedAmount,
        uint256 accumFeeAmount,
        uint256 index,
        bytes memory proof
    ) public;
```

This method is used to withdraw fees from Heimdall. `accountStateRoot` is updated on each checkpoint, so that validators can provide proof of inclusion in this root for account on Heimdall and withdraw fee.

Note that `accountStateRoot` is re-written to prevent exits on multiple checkpoints (for old root and save accounting on `stakeManager`).

### Staking NFT

Standard ERC721 contract with few restrictions like one token per user and minted in sequential manner.

### `checkSignatures`

```solidity
function checkSignatures(
        uint256 blockInterval,
        bytes32 voteHash,
        bytes32 stateRoot,
        bytes memory sigs
    ) public;
```

- Writes are meant only for RootChain contract when submitting checkpoints
- `voteHash` on which all validators sign (BFT $2/3+1$ agreement)
- This function validates only unique sigs and checks for $2/3+1$ power has signed on checkpoint root (inclusion in `voteHash` verification in `RootChain` contract for all data) `currentValidatorSetTotalStake` provides current active stake.
- Rewards are distributed proportionally to validator's stake. More on rewards on the [rewards distribution](https://docs.polygon.technology/pos/how-to/operating/validator-node/#reward-distribution) page.
<!-- (https://www.notion.so/Rewards-Distribution-127d586c14544beb9ea326fd3bb5d3a2). -->

### `isValidator`

Checks if a given validator is active validator for the current epoch.

## Timeline data structure

```solidity
struct State {
    int256 amount;
    int256 stakerCount;
}

mapping(uint256 => State) public validatorState;
```

![Figure: Knowledge base - node setup 1](../../../img/pos/staking_manager.png)


## `StakingInfo`

Centralized logging contract for both validator and delegation events, includes few read only functions. You can check out the source code of the [`StakingInfo.sol`](https://github.com/maticnetwork/contracts/blob/develop/contracts/staking/StakingInfo.sol) contract on GitHub.

## `ValidatorShareFactory`

A factory contract to deploy `ValidatorShare` contract for each validator who opt-in for delegation. You can check out the source code of the [ValidatorShareFactory.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/staking/validatorShare/ValidatorShareFactory.sol) contract on GitHub.
