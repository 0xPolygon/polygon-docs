
The Polygon PoS chain is a decentralized network of validator nodes that participate in block generation and consensus, and non-validator nodes that perform functions such as maintaining the complete block history of the network, providing dApps with an interface to communicate with the chain, and so on. No single node controls the network, meaning consensus is required for upgrades. 

Changes to the network require a high level of coordination and ecosystem consensus to execute successfully; if the ecosystem disagrees over a change, it can result in the network splitting, a protocol-level change generally referred to as *forking*.

!!! info "Hard forks vs. soft forks"
    A *hard fork* happens when the node software changes in such a way that the new version is no longer backward-compatible with earlier blocks. This is usually the result of a change in the consensus logic, meaning that blocks validated using the latest software will produce a different hash.

    A block number is selected, before which all nodes in the network should have upgraded to the new version; nodes running the old version will be disconnected from the canonical chain after the hard fork block.

    Should there be ${1/3}+1$ staked POL in disagreement with the fork, two canonical chains will temporarily form until the end of the current span. Afterwards, Bor will stop producing blocks, and the chain will halt until consensus is reached.

    In contrast, a *soft fork* is backward-compatible with the pre-fork blocks. This type of protocol change does not require nodes to upgrade before a deadline, therefore, multiple versions of the node software can be running at once and be able to validate transactions. 

The key ecosystem stakeholders involved in implementing a change are:

- Users
- Token holders
- Validators
- Infrastructure providers
- Full nodes
- Core developers

The PoS chain uses an improvement proposal-based framework to meet these coordination requirements. This framework acts as a signaling mechanism for stakeholders, and is not binding.

## Ecosystem consensus

The preliminary ecosystem consensus takes place through an off-chain process involving key stakeholders, including users and core developers. The framework set in place accommodates different perspectives put forward by the stakeholders, and provides a platform for constructive discussions and community cohesion.

The framework is composed of three key components:

1. [Polygon Improvement Proposals (“PIPs”)](https://github.com/maticnetwork/Polygon-Improvement-Proposals): Outlined in [PIP-1](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-01.md), PIPs are essentially instruments that enable the community to put forward protocol upgrades in the form of formal proposals that aim to improve the network. The framework borrows heavily from [Ethereum](https://hackmd.io/@timbeiko/eth-governance) and [EIP-1](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1.md), with many guiding principles originating within the [IETF](https://www.ietf.org/about/introduction/) and the broader open-source community.

2. [Polygon Protocol Governance Call (“PPGC”)](https://github.com/maticnetwork/Polygon-Improvement-Proposals/tree/main/Project%20Management): Synchronous discussions where "[rough consensus](https://datatracker.ietf.org/doc/html/rfc1603#:~:text=decisions%20through%20a%20%22-,rough%20consensus,-%22%20process.%0A%20%20%20IETF%20consensus)" is established, and the technical community makes protocol decisions. These calls generally decide which [PIPs](https://github.com/maticnetwork/Polygon-Improvement-Proposals/tree/main/PIPs) will be included in a particular upgrade, along with the roll-out schedule.

3. [Polygon Community Forum](https://forum.polygon.technology/): A space for long-form discussions ranging from high-level meta discussions to low-level technical details. 

## Implementation

The PoS network currently uses two clients simultaneously:

- Heimdall: The [consensus layer](https://docs.polygon.technology/pos/architecture/heimdall/) client - [See GitHub](https://github.com/maticnetwork/heimdall)
- Bor: The [execution layer](https://docs.polygon.technology/pos/architecture/bor/) client - [See GitHub](https://github.com/maticnetwork/bor)

Currently, Bor and Heimdall are the majority clients for the PoS network. These clients serve as ecosystem focal points rather than control switches operated by core developers that can dictate decisions.

Assuming that the change or upgrade agreed upon via community consensus requires a hard fork, the process that ensues generally looks like this:

1. The protocol decision is made on a PPGC, and implementation begins in the form of modifications to the relevant GitHub repositories.
2. Core developers create pull requests containing the changes, which can then be merged into the respective code base, and a new [tag](https://github.com/maticnetwork/bor/tags) is created.
3. Core developers test new releases by deploying them on local devnets. If everything continues to function normally, the tag is marked as *beta*, which is essentially the *pre-release* state.
4. The modifications and upgrades are rolled out to the Amoy testnet, and left out to soak for at least one week. Currently, the Amoy Testing Committee reports on the stability of the release in the PPGC.
5. Finally, once confirmed that the upgrade doesn't break anything, it is scheduled to be released to mainnet on a PPGC. At this point, the tag version is marked as *final*.
6. Validators upgrade their nodes to the latest version after considering the changes. The upgrade is now made canonical via on-chain consensus of the validating stake, including that delegated by token holders. 

## On-chain consensus

The parameters that define on-chain consensus are inherited from [Tendermint BFT](https://cosmos-network.gitbooks.io/cosmos-academy/content/introduction-to-the-cosmos-ecosystem/tendermint-bft-consensus-algorithm.html#:~:text=BFT%20Consensus%20Algorithm-,Tendermint%20BFT%20Consensus%20Algorithm,-Tendermint%20is%20consistent), which requires *at least ${2/3}rd$* of the total validating stake to be in favour of the upgrade.

For the chain to remain stable once the change is made canonical by validators, non-validating full nodes must also be upgraded to the latest version.

Key ecosystem stakeholders such as dApps, exchanges, and RPCs run full nodes, and are crucial in network operations as they propagate transactions and blocks. These nodes can either accept or reject blocks. This makes them *enforcers of the network consensus rules* and vital to the on-chain governance process. Should these nodes be incompatible with the changes, users and dApps would find that their transactions are invalid and not accepted by the network.

## On-chain governance module

The Heimdall client also has an [in-built governance module](https://github.com/maticnetwork/heimdall/tree/develop/gov#governance-module) that can synchronously carry out consensus parameter changes across the network.

1. Proposals can be submitted to the on-chain module along with a deposit containing the proposed changes.
2. Each validator then tallies votes cast by validators.
3. When the defined voting parameters are met, each validator makes the upgrade with the proposal data.

The current voting parameters (denominated in staked POL):

- Quorum: 33.4%		
- Threshold: 50% 
- Veto: 33.4%	

A list of the changeable parameters is available [here](https://github.com/maticnetwork/heimdall/blob/develop/auth/types/params.go).