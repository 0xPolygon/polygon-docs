---
comments: true
---

!!! info "Transitioning to POL"

    Polygon network is transitioning from MATIC to POL, which will serve as the gas and staking token on Polygon PoS. Use the links below to learn more:

    - [Migrate from MATIC to POL](../get-started/matic-to-pol.md)
    - [POL token specs](../concepts/tokens/pol.md)

Validators are the key actor in maintaining the Polygon PoS network. Validators run a full node, secure the network by staking POL to produce blocks, validate and participate in PoS consensus.

Validators play a crucial role in maintaining the integrity and security of the Polygon PoS network. By running a full node, validators contribute to the network's infrastructure and help facilitate transactions. They secure the network by staking POL tokens, which enables them to produce blocks and participate in network consensus (PoS). This contributes to greater network security and enhances network decentralization making it more resilient against potential attacks.

In return for their efforts, validators are rewarded with incentives, encouraging active participation and commitment to the network's stability and growth.

!!! info "Active validator limit"
    
    There is limited space for accepting new validators. Currently, the system allows for a maximum of 105 active validators at any given time. New validators can join the active set only when a currently active validator unbonds or is removed due to low performance.
    
    If you are interested in becoming a validator on the PoS network, you can submit an application over at the [Polygon validators hub](https://polygoncommunity.typeform.com/validatorshub).

    \* *Submitting an application does not guarantee a validator slot.*


## Overview

Polygon consists of the three following layers:

* Ethereum layer: A set of contracts on the Ethereum mainnet.
* Heimdall layer: A set of proof-of-stake Heimdall nodes running in parallel to the Ethereum mainnet, monitoring the set of staking contracts deployed on the Ethereum mainnet, and committing the Polygon PoS network checkpoints to the Ethereum mainnet. Heimdall is based on Tendermint.
* Bor layer: A set of block-producing Bor nodes shuffled by Heimdall nodes. Bor is based on Go Ethereum.

To be a validator on the Polygon PoS network, you must do the following:

* Run a sentry node: A separate machine running a Heimdall node and a Bor node. A sentry node is open to all nodes on the Polygon PoS network.
* Run a validator node: A separate machine running a Heimdall node and a Bor node. A validator node is only open to its sentry node and closed to the rest of the network.
* Stake the POL tokens in the staking contracts deployed on the Ethereum mainnet.

## Components

### Heimdall

Heimdall does the following:

* Monitors the staking contracts on the Ethereum mainnet.
* Verifies all state transitions on the Bor chain.
* Commits the Bor chain state checkpoints to the Ethereum mainnet.

Heimdall is based on Tendermint.

!!! info "See also"

    * GitHub repository: [Heimdall](https://github.com/maticnetwork/heimdall)
    * GitHub repository: [Staking contracts](https://github.com/maticnetwork/contracts/tree/master/contracts/staking)
    * Blog post: [Heimdall](https://polygon.technology/blog/heimdall-vaibhav-chellani-the-all-seeing-all-hearing-protector-of-matic)

### Bor

Bor does the following:

* Produces blocks on Polygon PoS.

Bor is the block producing node and layer for the Polygon PoS network. It is based on Go Ethereum. Blocks produced on Bor are validated by Heimdall nodes.

!!! info "See also"

    * GitHub repository: [Bor](https://github.com/maticnetwork/bor)
    * Blog post: [Heimdall and Bor](https://blog.polygon.technology/heimdall-and-bor/)

## Validator responsibilities

!!! tip "Stay in the know"

    Keep up with the latest node and validator updates from the Polygon team and the community by keeping an eye on the [announcements posed to Polygon forums](https://forum.polygon.technology/c/announcement/6).

A blockchain validator is someone who is responsible for validating transactions within a blockchain. On the Polygon PoS network, any participant can be qualified to become a Polygon's validator by running a validator node (sentry + validator) to earn rewards and collect transaction fees. To ensure the good participation by validators, they lock up at least 1 POL token as a stake in the ecosystem.

!!! info "PIP4 raised the minimum staking amount"

    After the implementation of the [PIP4 governance proposal](https://forum.polygon.technology/t/pip-4-validator-performance-management/9956) at the contract level, the minimum staking amount was increased to *10,000 POL*.

Any validator on the Polygon PoS network has the following responsibilities:

- Technical node operations (done automatically by the nodes).
- Operations
    - Maintain high uptime.
    - Check node-related services and processes daily.
    - Run node monitoring.
    - Keep ETH balance (between 0.5 to 1) on the signer address.
- Delegation
    - Be open to delegation.
    - Communicate commission rates.
- Communication
    - Communicate issues.
    - Provide feedback and suggestions.
- Earn staking rewards for validate blocks on the blockchain.

### Technical node operations

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
    * In this case, there is an `ack/no-ack` process that is followed to ensure that the next checkpoint contains a snapshot of the previous Bor blocks as well. For example, if checkpoint 1 is for Bor blocks 1-256, and it failed for some reason, the next checkpoint 2 will be for Bor blocks 1-512. See also [Heimdall architecture: Checkpoint](../architecture/heimdall/checkpoints.md).
* State sync from the Ethereum mainnet to Bor:
    * Contract state can be moved between Ethereum and Polygon, specifically through Bor.
    * A dApp contract on Ethereum calls a function on a special Polygon contract on Ethereum.
    * The corresponding event is relayed to Heimdall and then Bor.
    * A state-sync transaction gets called on a Polygon smart contract and the dApp can get the value on Bor via a function call on Bor itself.
    * A similar mechanism is in place for sending state from Polygon to Ethereum. See also [State Sync Mechanism](../how-to/bridging/l1-l2-communication/state-transfer.md).

### Operations

#### Maintain high uptime

The node uptime on the Polygon PoS network is based on the number of checkpoint transactions that the validator node has signed.

Approximately every 34 minutes a proposer submits a checkpoint transaction to the Ethereum mainnet. The checkpoint transaction must be signed by every validator on the Polygon PoS network. Failure to sign a checkpoint transaction results in the decrease of your validator node performance.

The process of signing the checkpoint transactions is automated. To ensure your validator node is signing all valid checkpoint transactions, you must maintain and monitor your node health.

#### Check node services and processes daily

You must check daily the services and processes associated with Heimdall and Bor. Also, pruning of the nodes should be done regularly to reduce disk usage.

#### Run node monitoring

You must run either:

* Grafana Dashboards provided by Polygon. See GitHub repository: [Matic-Jagar setup](https://github.com/vitwit/matic-jagar)
* Or, use your own monitoring tools for the validator and sentry nodes.
* Ethereum endpoint used on nodes should be monitored to ensure the node is within the request limits.

#### Maintain ETH balance

You must maintain an adequate amount of ETH (should be always around the threshold value i.e., 0.5 to 1) on your validator signer address on the Ethereum Mainnet.

You need ETH to:

* Sign the proposed checkpoint transactions on the Ethereum Mainnet.
* Propose and send checkpoint transactions on the Ethereum Mainnet.

Not maintaining an adequate amount of ETH on the signer address will result in:

* Delays in the checkpoint submission. Note that transaction gas prices on the Ethereum network may fluctuate and spike.
* Delays in the finality of transactions included in the checkpoints.
* Delays in subsequent checkpoint transactions.

### Delegation

#### Be open for delegation

All validators must be open for delegation from the community. Each validator has the choice of setting their own commission rate. There is no upper limit to the commission rate.

#### Communicate commission rates

It is the moral duty of the validators to communicate the commission rates and the commission rate changes to the community. The preferred platforms to communicate the commission rates are:

* [Discord](https://discord.com/invite/0xPolygonCommunity)
* [Forum](https://forum.polygon.technology/)

### Communication

#### Communicate issues

Communicating issues as early as possible ensures that the community and the Polygon team can rectify the problems as soon as possible. The preferred platforms to communicate the commission rates are:

* [Discord](https://discord.com/invite/0xPolygonCommunity)
* [Forum](https://forum.polygon.technology/)
* [GitHub](https://github.com/maticnetwork)

#### Provide feedback and suggestions

At Polygon, we value your feedback and suggestions on any aspect of the validator ecosystem. [Forum](https://forum.polygon.technology/) is the preferred platform to provide feedback and suggestions.

## Run and maintain a node

The following step-by-step guides will take you through the process of running a new validator node, or performing necessary maintenance actions for an existing node you've deployed.

### Join the network as a validator

* [Start and run the nodes with Ansible](../how-to/validator/validator-ansible.md).
* [Start and run the nodes with binaries](../how-to/validator/validator-binaries.md).
* [Stake as a validator](../how-to/operate-validator-node/next-steps.md#stake-tokens).

### Maintain your validator nodes

* [Change the signer address](../how-to/operate-validator-node/change-signer-address.md).
* [Change the commission](../how-to/operate-validator-node/next-steps.md#changing-your-commission-rate).

### Community assistance

* [Discord](https://discord.com/invite/0xPolygonCommunity)
* [Forum](https://forum.polygon.technology/)
