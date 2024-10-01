# Architecture

This section provides architectural details of Polygon PoS from a node perspective. 

Due to the proof-of-stake consensus, Polygon PoS consists of a consensus layer called Heimdall and execution layer called Bor.

Nodes on Polygon are therefore designed with a two-layer implementation represented by Bor (the block producer layer) and Heimdall (the validator layer).

In particular, and on the execution client side, it delineates on snapshots and state syncing, network configurations, and frequently used commands when running PoS nodes.

On the consensus client side, one finds descriptions on how Heimdall handles; authentication of account addresses, management of validators' keys, management of gas limits, enhancement of transaction verifications, balance transfers, staking and general chain management.

## Architectural overview

The Polygon Network is broadly divided into three layers:

* Ethereum layer — a set of contracts on the Ethereum mainnet.
* Heimdall layer — a set of proof-of-stake Heimdall nodes running in parallel to the Ethereum mainnet, monitoring the set of staking contracts deployed on the Ethereum mainnet, and committing the Polygon Network checkpoints to the Ethereum mainnet. Heimdall is based on Tendermint.
* Bor layer — a set of block-producing Bor nodes shuffled by Heimdall nodes. Bor is based on Go Ethereum.

![Figure: Ethereum, Bor and Heimdall architecture](../../img/pos/architecture.png)

## Staking smart contracts on Ethereum

To enable the Proof of Stake (PoS) mechanism on Polygon, the system employs a set of staking management contracts on the Ethereum mainnet.

The staking contracts implement the following features:

* The ability for anyone to stake MATIC tokens on the staking contracts on the Ethereum mainnet and join the system as a validator.
* Earn staking rewards for validating state transitions on the Polygon Network.
* Save checkpoints on the Ethereum mainnet.

The PoS mechanism also acts as a mitigation to the data unavailability problem for the Polygon sidechains.

## Heimdall: Validation layer

Heimdall layer handles the aggregation of blocks produced by Bor into a Merkle tree and publishes the Merkle root periodically to the root chain. The periodic publishing of snapshots of Bor are called checkpoints.

For every few blocks on Bor, a validator on the Heimdall layer:

1. Validates all the blocks since the last checkpoint.
2. Creates a Merkle tree of the block hashes.
3. Publishes the Merkle root hash to the Ethereum mainnet.

Checkpoints are important for two reasons:

1. Providing finality on the root chain.
2. Providing proof of burn in withdrawal of assets.

An overview of the process:

* A subset of active validators from the pool is selected to act as block producers for a span. These block producers are responsible for creating blocks and broadcasting the created blocks on the network.
* A checkpoint includes the Merkle root hash of all blocks created during any given interval. All nodes validate the Merkle root hash and attach their signature to it.
* A selected proposer from the validator set is responsible for collecting all signatures for a particular checkpoint and committing the checkpoint on the Ethereum mainnet.
* The responsibility of creating blocks and proposing checkpoints is variably dependent on a validator’s stake ratio in the overall pool.

See also [Heimdall architecture](../architecture/heimdall/introduction.md).
<!-- (/docs/pos/design/heimdall/overview). -->

## Bor: Block production layer

Bor is Polygon PoS's block producer — the entity responsible for aggregating transactions into blocks.

Bor block producers are a subset of the validators and are shuffled periodically by the Heimdall validators.

See also [Bor architecture](../architecture/bor/introduction.md).
<!-- (/docs/pos/design/bor/overview). -->
