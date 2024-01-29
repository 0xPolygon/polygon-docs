
Welcome to the Polygon PoS how-to section! 

## Common tasks

There are a number of guides here to help you get started with technical tasks like bridging assets from Ethereum to the Polygon PoS chain and vice-versa, smart contract development basics covering deployment and verification, messaging between Layer-1 (L1) and Layer-2 (L2) networks, etc. Check out the links listed below:

* [Bridge tokens from Ethereum to PoS](bridging/ethereum-polygon/ethereum-to-matic.md)
* [Bridge tokens from PoS to Ethereum](bridging/ethereum-polygon/matic-to-ethereum.md)
* [L1 - L2 communication](bridging/l1-l2-communication/state-transfer.md)
* [Work with smart contracts on PoS](smart-contracts/index.md)

## Deploy, operate, and maintain nodes

This section also contains guides that describe the system requirements and configurations necessary to spin up different kinds of Polygon nodes, and then take you step by step through the process of setting them up on the PoS network. 

Depending on the extent to which you're looking to participate in different network processes, and the kind of computational and network capabilities you can offer, you can choose to deploy any of the following nodes:

!!! tip

    It's always a good idea to first read and understand the **minimum** and **recommended** system requirements for any node that you choose to deploy to the PoS network.

|                       Validator node                       |                          Full node                          |        Access node         | Archive node |
| :--------------------------------------------------------: | :---------------------------------------------------------: | :------------------------: | :----------: |
| [Prerequisites](validator/prerequisites.md) **(Read me!)** | [Requirements](/full-node/full-node-system-requirements.md) | [Full guide](access-node.md) |   [Full guide](erigon-archive-node.md)   |
|        [Binaries](validator/validator-binaries.md)         |        [Binaries](/full-node/full-node-binaries.md)         |             -              |      -       |
|         [Ansible](validator/validator-ansible.md)          |         [Ansible](/full-node/full-node-ansible.md)          |             -              |      -       |
|        [Packages](validator/validator-packages.md)         |        [Packages](/full-node/full-node-packages.md)         |             -              |      -       |
|                             -                              |          [Docker](/full-node/full-node-docker.md)           |             -              |      -       |
|                             -                              |             [GCP](/full-node/full-node-gcp.md)              |             -              |      -       |

## Polygon DID

Included in the section is an elaborate startup guide for users who wish to implement the Polygon DID, which is a three-part package consisting of an identity-registrar, identity-resolver, and identity-registry-contract.

* [Polygon DID integration guide](./polygon-did.md)