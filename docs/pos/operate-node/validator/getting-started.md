Validators are the key actor in maintaining the Polygon network. Validators run a full node, secure the network by staking MATIC to produce blocks, validate and participate in PoS consensus.

!!!info
    
    There is limited space for accepting new validators. New validators can only join the active set when a currently active validator unbonds.

    A new auction process for validator replacement will be rolled out.


## Overview

Polygon consists of the three following layers:

* Ethereum layer — a set of contracts on the Ethereum mainnet.
* Heimdall layer — a set of proof-of-stake Heimdall nodes running in parallel to the Ethereum mainnet, monitoring the set of staking contracts deployed on the Ethereum mainnet, and committing the Polygon Network checkpoints to the Ethereum mainnet. Heimdall is based on Tendermint.
* Bor layer — a set of block-producing Bor nodes shuffled by Heimdall nodes. Bor is based on Go Ethereum.

To be a validator on the Polygon Network, you must run:

* Sentry node — a separate machine running a Heimdall node and a Bor node. A sentry node is open to all nodes on the Polygon Network.
* Validator node — a separate machine running a Heimdall node and a Bor node. A validator node is only open to its sentry node and closed to the rest of the network.
* Stake the MATIC tokens in the staking contracts deployed on the Ethereum mainnet.

## Components

### Heimdall

Heimdall does the following:

* Monitors the staking contracts on the Ethereum mainnet.
* Verifies all state transitions on the Bor chain.
* Commits the Bor chain state checkpoints to the Ethereum mainnet.

Heimdall is based on Tendermint.

!!!info
    See Also

    * GitHub repository: [Heimdall](https://github.com/maticnetwork/heimdall)
    * GitHub repository: [Staking contracts](https://github.com/maticnetwork/contracts/tree/master/contracts/staking)
    * Blog post: [Heimdall and Bor](https://blog.polygon.technology/heimdall-and-bor/)


### Bor

Bor does the following:

* Produces blocks on the Polygon Network.

Bor is the Block producer node and layer for the Polygon Network. It is based on Go Ethereum. Blocks produced on Bor are validated by Heimdall nodes.

!!!info
    See Also

    * GitHub repository: [Bor](https://github.com/maticnetwork/bor)
    * Blog post: [Heimdall and Bor](https://blog.polygon.technology/heimdall-and-bor/)


This section guides you through the following topics:

* [Validator responsibilities](/pos/design/validator/responsibilities.md)
* Joining the network as a validator:
  * [Start and run the nodes with Ansible](/pos/validator/run-validator/ansible.md)
  * [Start and run the nodes with binaries](/pos/validator/run-validator/binaries.md)
  * [Stake as a validator](/pos/validator/validator-staking-operations.md)
* Maintaining your validator nodes:
  * [Change the signer address](/pos/validator/change-signer-address.md)
  * [Change the commission](/pos/validator/validator-commission-operations.md)

Community assistance:

* [Discord](https://discord.com/invite/0xPolygon)
* [Forum](https://forum.polygon.technology/)
