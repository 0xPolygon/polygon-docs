Polygon supports delegation via validator shares. By using this design, it is easier to distribute rewards and slash with scale (thousands of delegators) on Ethereum contracts without much computation.

Delegators delegate by purchasing shares of a finite pool from validators. Each validator will have their own validator share token. Let's call these fungible tokens `VATIC` for a validator `A`. As soon as a user delegates to a validator `A`, they will be issued `VATIC` based on an exchange rate of `MATIC/VATIC` pair. As users accrue value the exchange rate indicates that they can now withdraw more `MATIC` for each `VATIC` and when users get slashed, users withdraw less `MATIC` for their `VATIC`.

Note that `MATIC` is a staking token. A delegator needs to have `MATIC` tokens to participate in the delegation.

Initially, a delegator `D` buys tokens from validator `A` specific pool when `1 MATIC per 1 VATIC`.

When a validator gets rewarded with more `MATIC` tokens, new tokens are added to the pool. Let's say with the current pool of `100 MATIC` tokens, `10 MATIC` rewards are added to the pool. But since the total supply of `VATIC` tokens didn't change due to rewards, the exchange rate becomes `1 MATIC per 0.9 VATIC`. Now, delegator `D` gets more `MATIC` for the same shares.

`VATIC`: Validator specific minted validator share tokens (ERC20 tokens)

## Technical specification

```solidity
uint256 public validatorId; // Delegation contract for validator
uint256 public validatorRewards; // accumulated rewards for validator
uint256 public commissionRate; // validator's cut %
uint256 public validatorDelegatorRatio = 10; // to be implemented/used

uint256 public totalStake;
uint256 public rewards; // rewards for pool of delegation stake
uint256 public activeAmount; // # of tokens delegated which are part of active stake
```

Exchange rate is calculated as below:

```js
ExchangeRate = (totalDelegatedPower + delegatorRewardPool) / totalDelegatorShares
```

## Methods and variables

### buyVoucher

```js
function buyVoucher(uint256 _amount) public;
```

- Transfer the `_amount` to stakeManager and update the timeline data structure for active stake.
- `updateValidatorState` is used to update timeline DS.
- `Mint` delegation shares using current `exchangeRate` for `_amount`.
- `amountStaked` is used to keep track of active stake of each delegator in order to calculate liquid rewards.

### sellVoucher

```js
function sellVoucher() public;
```

- Using current `exchangeRate` and number of shares to calculate total amount (active stake + rewards).
- `unBond` active stake from validator and transfer rewards to delegator, if any.
- Must remove active stake from timeline using `updateValidatorState` in stakeManger.
- `delegators` mapping is used to keep track of stake in withdrawal period.

### withdrawRewards

```js
function withdrawRewards() public;
```

- For a delegator, calculate the rewards and transfer, and depending upon `exchangeRate` burn count of shares.
- Example: if a delegator owns 100 shares and exchange rate is 200 so rewards are 100 tokens, transfer 100 tokens to delegator. Remaining stake is 100 so using exchange rate 200, now it is worth 50 shares. So burn 50 shares. Delegator now has 50 shares worth 100 tokens (which he initially staked / delegated).

### reStake

Restake can work in two ways: delegator can buy more shares using `buyVoucher` or reStake rewards.

```js
function reStake() public;
```

Above function is used to reStake rewards. The number of shares aren’t affected because `exchangeRate` is the same; so just the rewards are moved into active stake for both validator share contract and stakeManager timeline.

`getLiquidRewards` is used for calculating accumulated rewards i.e., delegator owns 100 share and exchange rate is 200, so rewards are 100 tokens. Move 100 tokens into active stake, since exchange rate is still same number of share will also remain same. Only difference is that now 200 tokens are considered into active stake and can't be withdrawn immediately (not a part of liquid rewards).

Purpose of reStaking is that since delegator's validator has now more active stake and they will earn more rewards for that so will the delegator.

### unStakeClaimTokens

```js
function unStakeClaimTokens()
```

Once withdrawal period is over, delegators who've sold their shares can claim their MATIC tokens. Must transfer tokens to user.

### updateCommissionRate

```js
function updateCommissionRate(uint256 newCommissionRate)
        external
        onlyValidator
```

- Updates commission % for the validator.

### updateRewards

```js
function updateRewards(uint256 reward, uint256 checkpointStakePower, uint256 validatorStake)
        external
        onlyOwner
        returns (uint256)
```

When a validator gets rewards for submitting checkpoint, this function is called for disbursements of rewards between validator and delegators.
