## Network upgrade overview

This page provides hardfork activation timestamps along with links to detailed specifications. It also outlines the hardfork release process, versions, network and node i.,e bor/heimdall. The network upgrade naming scheme follows the order in which the release happened on the Polygon network.

## Activations

On the Polygon Network, upgrades are activated based on timestamps. If you fail to update your Polygon client software before the specified timestamp, it may result in chain divergence, requiring a full resynchronization.


|          Upgrade          |                               Forum                                                                |                                             PIP                                                                |                              Activation                           |
| ------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
|        Delhi Hardfork     |        [Link](https://forum.polygon.technology/t/pip-7-delhi-hardfork/10904/2)                     |     [PIP-7](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-07.md)            |           Block >= `38,189,056` on Polygon Mainnet (Bor)          |
|        Indore Hard Fork   |        [Link](https://forum.polygon.technology/t/pip-13-indore-hard-fork12272)                     |     [PIP-13](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-13md)            |           Block >= `44,934,656` on Polygon Mainnet(Bor)           |
|       Aalborg Hard Fork   |        [Link](https://forum.polygon.technology/t/aalborg-upgrade-mainnet-timeline-update/12960)    |     [PIP-21](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-21.md)           |           Block >= `15,950,759` on Polygon Mainnet (Heimdall)     |
|        Agra Hard Fork     |        [Link](https://forum.polygon.technology/t/pip-28-agra-hardfork/13067)                       |     [PIP-28](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-28.md)           |           Block >= `50,523,000` on Polygon Mainnet (Bor)          |
|                           |                                                                                                    |                                                                                                                |           Block >= `41,874,000` on Polygon Mumbai (Bor)           |
|        Napoli Hardfork    |        [Link](https://forum.polygon.technology/t/pip-33-napoli-upgrade/13405)                      |     [PIP-33](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-33.md)           |           Block >= `54,876,000` on Polygon Mainnet (Bor)          |
|                           |                                                                                                    |                                                                                                                |           Block >= `5,423,600`  on Polygon Amoy (Bor)             |
|      Ahmedabad Hardfork   |        [Link](https://forum.polygon.technology/t/pip-37-ahmedabad-hardfork/13885)                  |     [PIP-37](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-37.md)           |           Block >= `62,278,656` on Polygon Mainnet (Bor)          |
|                           |                                                                                                    |                                                                                                                |           Block >= `11,865,856` on Polygon Amoy (Bor)             |
|      Jorvik Hardfork      |        [Link](https://forum.polygon.technology/t/pip-53-jorvik-hardfork/20357)                     |     [PIP-53](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-53.md)           |           Block >= `22,393,043` on Polygon Mainnet (Heimdall)     |
|                           |                                                                                                    |                                                                                                                |           Block >= `5,768,528` on Polygon Amoy (Heimdall)         |
|       Danelaw Hardfork    |        [Link](https://forum.polygon.technology/t/pip-56-danelaw-hardfork/20511)                    |     [PIP-56](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-56.md)           |           Block >= `22,393,043` on Polygon Mainnet (Heimdall)     |
|                           |                                                                                                    |                                                                                                                |           Block >= `6,490,424` on Polygon Amoy (Heimdall)         |    
|       Bhilai Hardfork     |        [Link](https://forum.polygon.technology/t/bor-v2-1-0-beta4-release-bhilai-hf-on-amoy/21010) |     [PIP-63](https://github.com/maticnetwork/Polygon-Improvement-Proposals/blob/main/PIPs/PIP-63.md)           |           Block >= `22,765,056` on Polygon Amoy (Bor)             |




## Upgrade process

Network upgrades follow this general process in which the features included in the upgrade are put into a release version cut from the develop branch and then the software is deployed on production networks.


![network-upgrade](<../../img/pos/Pos Phases.png>)


### 1. Proposal & Governance Approval
Polygon is governed by the polygon governance, where any significant protocol changes, including hardforks, must be proposed and approved through a governance and community discussion on forum. The process includes:

 - Submitting an Polygon Improvement Proposal (PIP).
 - Community discussion and feedback.
 - On-chain voting to pass the proposal.

### 2. Development & Testing
 Once a proposal is approved, developers implement and test the changes:

- Code is developed and reviewed.
- Extensive testing is conducted on Devnets and testnets to ensure security and stability.
- Smart contracts and Layer 2 infrastructure are upgraded.

### 3. Node & Software Upgrades
Once the development is done, announcement is done for validators and node operators.

- Node operators and validators must update their software before the hardfork activation timestamp.
- Failure to upgrade could result in a chain split or desynchronization.

### 4. Hardfork Activation

- The upgrade is scheduled at a specific block height or timestamp.
- If all nodes update in time, the upgrade is seamless.
- If some nodes fail to update, they risk being left on an outdated chain.

### 5. Post-Hardfork Monitoring

- After activation, the network is monitored for stability.
- Any bugs or issues are addressed quickly through patches if needed.
