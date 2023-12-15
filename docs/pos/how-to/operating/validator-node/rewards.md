In Polygon, validators stake their MATIC tokens as collateral to work for the security of the network, and in exchange for their service, earn rewards.

To leverage Polygon's economics, you should either become a validator or a delegator.

To be a validator, you need to **run a full validator** node and stake MATIC.

Also check the [Validator Responsibilities](/pos/design/validator/responsibilities) page.

To be a delegator, you only need to **delegate MATIC to a validator**

## What is the incentive?

Polygon allocates 12% of its total supply of 10 billion tokens to fund the staking rewards. This is to ensure that the network is seeded well enough until transaction fees gain traction. These rewards are primarily meant to jump-start the network, while the protocol in the long run is intended to sustain itself on the basis of transaction fees.

**Validator Rewards = Staking Rewards + Transaction Fees**

This is allocated in a way to ensure gradual decoupling of staking rewards from being the dominant component of the validator rewards.

|Year|Target Stake (30% of circulating supply)|Reward Rate for 30% Bonding|Reward Pool|
|---|---|---|---|
|First|1,977,909,431|20%|312,917,369|
|Second|2,556,580,023|12%|275,625,675|
|Third|2,890,642,855|9%|246,933,140|
|Fourth|2,951,934,048|7%|204,303,976|
|Fifth|2,996,518,749|5%|148,615,670 + **11,604,170**|

Below is a sample snapshot of the expected annual rewards for the first 5 years considering staked supply ranging from 5% to 40% at 5% interval

|% of circulating supply staked|5%|10%|15%|20%|25%|30%|35%|40%|
|---|---|---|---|---|---|---|---|---|
|Annual reward for year|
|First|120%|60%|40%|30%|24%|20%|17.14%|15%|
|Second|72%|36%|24%|18%|14.4%|12%|10.29%|9%|
|Third|54%|27%|18%|13.5%|10.8%|9%|7.71%|6.75%|
|Fourth|42%|21%|14%|10.5%|8.4%|7%|6%|5.25%|
|Fifth|30%|15%|10%|7.5%|6%|5%|4.29%|3.75%|

## Who gets the incentives?

Stakers running validator nodes and stakers delegating their tokens toward a validator that they prefer.

Validators have the option to charge a commission on the reward earned by delegators.

The funds belonging to all stakers are locked in a contract deployed on the Ethereum mainnet.

No validator holds custody over delegator tokens.

## Staking rewards

The yearly incentive is absolute — irrespective of the overall stake or the target bonding rate in the network, the incentive amount is given out as a reward to all signers periodically.

In Polygon, there is an additional element of committing periodic checkpoints to the Ethereum mainnet. This is a major part of the validator responsibilities and they are incentivized to perform this activity. This constitutes a cost to the validator which is unique to a Layer 2 solution such as Polygon. We strive to accommodate this cost in the validator staking reward payout mechanism as a bonus to be paid to the proposer, who is responsible for committing the checkpoint. Rewards minus the bonus is to be shared among all stakers, proposer and signers, proportionally.

## Encouraging the proposer to include all signatures

To avail the bonus completely, the proposer must include all signatures in the checkpoint. Because the protocol desires ⅔ +1 weight of the total stake, the checkpoint is accepted even with 80% votes. However, in this case, the proposer gets only 80% of the calculated bonus.

## Transaction fees

Each block producer at Bor is given a certain percentage of the transaction fees collected in each block. The selection of producers for any given span is also dependent on the validator’s ratio in the overall stake. The remaining transaction fees flow through the same funnel as the rewards which get shared among all validators working at the Heimdall layer.
