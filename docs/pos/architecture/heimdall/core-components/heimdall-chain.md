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
