# Operating a Validator

A blockchain validator is someone who is responsible for validating transactions within a blockchain. On the Polygon Network, any participant can be qualified to become a Polygon's validator by running a **Validator Node (Sentry + Validator)** to earn rewards and collect transaction fees. To ensure the good participation by validators, they lock up at least 1 MATIC token as a stake in the ecosystem.

Any validator on the Polygon Network has the following responsibilities:

* Technical node operations (done automatically by the nodes)
* Operations
  * Maintain high uptime
  * Check node-related services and processes daily
  * Run node monitoring
  * Keep ETH balance (between 0.5 to 1) on the signer address
* Delegation
  * Be open to delegation
  * Communicate commission rates
* Communication
  * Communicate issues
  * Provide feedback and suggestions
* Earn staking rewards for validate blocks on the blockchain

## Technical node operations

The following technical node operations are **done automatically by the nodes:**

* Block producer selection:
  * Select a subset of validators for the block producer set for each span.
  * For each span, select the block producer set again on Heimdall and transmit the selection information to Bor periodically.
* Validating blocks on Bor:
  * For a set of Bor blocks, each validator independently reads block data for these blocks and validates the data on Heimdall.
* Checkpoint submission:
  * A proposer is chosen among the validators for each Heimdall block. The checkpoint proposer creates the checkpoint of Bor block data, validates, and broadcasts the signed transaction for other validators to consent to.
  * If more than 2/3 of the active validators reach consensus on the checkpoint, the checkpoint is submitted to the Ethereum mainnet.
* Sync changes to Polygon staking contracts on Ethereum:
  * Continuing from the checkpoint submission step, since this is an external network call, the checkpoint transaction on Ethereum may or may not be confirmed, or may be pending due to Ethereum congestion issues.
  * In this case, there is an `ack/no-ack` process that is followed to ensure that the next checkpoint contains a snapshot of the previous Bor blocks as well. For example, if checkpoint 1 is for Bor blocks 1-256, and it failed for some reason, the next checkpoint 2 will be for Bor blocks 1-512. See also [Heimdall architecture: Checkpoint](/pos/design/heimdall/checkpoint.md).
* State sync from the Ethereum mainnet to Bor:
  * Contract state can be moved between Ethereum and Polygon, specifically through Bor:
  * A DApp contract on Ethereum calls a function on a special Polygon contract on Ethereum.
  * The corresponding event is relayed to Heimdall and then Bor.
  * A state-sync transaction gets called on a Polygon smart contract and the DApp can get the value on Bor via a function call on Bor itself.
  * A similar mechanism is in place for sending state from Polygon to Ethereum. See also [State Sync Mechanism](/docs/pos/state-sync/state-sync).

## Operations

### Maintain high uptime

The node uptime on the Polygon Network is based on the number of checkpoint transactions that the validator node has signed.

Approximately every 34 minutes a proposer submits a checkpoint transaction to the Ethereum mainnet. The checkpoint transaction must be signed by every validator on the Polygon Network. **Failure to sign a checkpoint transaction results in the decrease of your validator node performance**.

The process of signing the checkpoint transactions is automated. To ensure your validator node is signing all valid checkpoint transactions, you must maintain and monitor your node health.

### Check node services and processes daily

You must check daily the services and processes associated with Heimdall and Bor. Also, pruning of the nodes should be done regularly to reduce disk usage.

### Run node monitoring

You must run either:

* Grafana Dashboards provided by Polygon. See GitHub repository: [Matic-Jagar setup](https://github.com/vitwit/matic-jagar)
* Or, use your own monitoring tools for the validator and sentry nodes
* Ethereum endpoint used on nodes should be monitored to ensure the node is within the request limits

### Keep an ETH balance

You must maintain an adequate amount of ETH (should be always around the threshold value i.e., 0.5 to 1) on your validator signer address on the Ethereum Mainnet.

You need ETH to:

* Sign the proposed checkpoint transactions on the Ethereum Mainnet.
* Propose and send checkpoint transactions on the Ethereum Mainnet.

Not maintaining an adequate amount of ETH on the signer address will result in:

* Delays in the checkpoint submission. Note that transaction gas prices on the Ethereum network may fluctuate and spike.
* Delays in the finality of transactions included in the checkpoints.
* Delays in subsequent checkpoint transactions.

## Rewards

In Polygon, validators stake their MATIC tokens as collateral to work for the security of the network, and in exchange for their service, earn rewards.

To leverage Polygon's economics, you should either become a validator or a delegator.

To be a validator, you need to **run a full validator** node and stake MATIC.

Also check the [Validator Responsibilities](/pos/design/validator/responsibilities) page.

To be a delegator, you only need to **delegate MATIC to a validator**

### What is the incentive?

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

### Who gets the incentives?

Stakers running validator nodes and stakers delegating their tokens toward a validator that they prefer.

Validators have the option to charge a commission on the reward earned by delegators.

The funds belonging to all stakers are locked in a contract deployed on the Ethereum mainnet.

No validator holds custody over delegator tokens.

### Staking rewards

The yearly incentive is absolute — irrespective of the overall stake or the target bonding rate in the network, the incentive amount is given out as a reward to all signers periodically.

In Polygon, there is an additional element of committing periodic checkpoints to the Ethereum mainnet. This is a major part of the validator responsibilities and they are incentivized to perform this activity. This constitutes a cost to the validator which is unique to a Layer 2 solution such as Polygon. We strive to accommodate this cost in the validator staking reward payout mechanism as a bonus to be paid to the proposer, who is responsible for committing the checkpoint. Rewards minus the bonus is to be shared among all stakers, proposer and signers, proportionally.

### Encouraging the proposer to include all signatures

To avail the bonus completely, the proposer must include all signatures in the checkpoint. Because the protocol desires ⅔ +1 weight of the total stake, the checkpoint is accepted even with 80% votes. However, in this case, the proposer gets only 80% of the calculated bonus.

### Transaction fees

Each block producer at Bor is given a certain percentage of the transaction fees collected in each block. The selection of producers for any given span is also dependent on the validator’s ratio in the overall stake. The remaining transaction fees flow through the same funnel as the rewards which get shared among all validators working at the Heimdall layer.

## Delegation

### Be open for delegation

All validators must be open for delegation from the community. Each validator has the choice of setting their own commission rate. There is no upper limit to the commission rate.

### Communicate commission rates

It is the moral duty of the validators to communicate the commission rates and the commission rate changes to the community. The preferred platforms to communicate the commission rates are:

* [Discord](https://discord.com/invite/0xPolygon)
* [Forum](https://forum.polygon.technology/)

## Communication

### Communicate issues

Communicating issues as early as possible ensures that the community and the Polygon team can rectify the problems as soon as possible. The preferred platforms to communicate the commission rates are:

* [Discord](https://discord.com/invite/0xPolygon)
* [Forum](https://forum.polygon.technology/)
* [GitHub](https://github.com/maticnetwork)

### Provide feedback and suggestions

At Polygon, we value your feedback and suggestions on any aspect of the validator ecosystem. [Forum](https://forum.polygon.technology/) is the preferred platform to provide feedback and suggestions.


## System Requirements

The system requirements listed in this section are both for the Sentry node and the Validator node.

The **minimum** system requirements mean you can run the nodes but the setup is not future-proof.

The **recommended** system requirements mean the nodes are future-proof. There is, however, no upper limit to future-proofing your nodes.

You must always run the sentry node and the validator node on separate machines.

### Minimum system requirements

* RAM: 32 GB
* CPU: 8-core
* Storage: 2.5 TB SSD

:::info

For Amazon Web Services (AWS), the equivalent of the minimum requirements instances are, **with unlimited credits selected**:

- For Sentry: **c5.2xlarge**
- For Validator node: **c5.4xlarge**

:::

### Recommended system requirements

* RAM: 64 GB
* CPU: 16-core
* Storage: 5 TB SSD
* Bandwidth: 1 Gbit/s
