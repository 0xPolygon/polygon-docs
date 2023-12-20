Find in here a record of the zkEVM’s historical data. This document records timelines, major milestones, forks, and updates to the zkEVM.

### 13th Dec, 2023
SCHEDULED zkEVM MAINNET UPDATE

Date: Wed, 13th Dec
Time: 09:00 UTC / 10:00 AM CET
Duration: ~15 mins

Please note an upcoming update of zkEVM Mainnet infrastructure happening on Dec 13 at 10:00 AM CET. The network will be available during the update duration, except for ~1 min for sequencer restart. This update includes reduced number of RPC logs and also aligns error messages to match geth error messages regarding estimate gas for unsigned tx.

Node version: v0.4.4 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.4.4)


Things to note:

   1. Be prepared for the scheduled update.
   2. Stay updated on the progress through official communication channels.
   3. For infrastructure partners, this is a recommended but optional version for partners. No config changes needed. Update to the new version and restart the node and RPC.


### 23rd Nov, 2023
SCHEDULED zkEVM MAINNET UPDATE

Date: Thursday, 23rd Nov
zkEVM Mainnet Update Changes
The mainnet update planned today will be done at 16:30 UTC/17:30 CET,  with node version v0.4.1 https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.4.1
(Additional CORS header fix + features in v0.4.0)

For infrastructure partners, 
AFTER the update, please use the instructions here (https://polygontechnology.notion.site/Instructions-zkEVM-Mainnet-Node-v0-4-1-Prover-v3-0-2-7a585f394cd24b90b90283086276533c?pvs=4)


### 21st Nov, 2023
SCHEDULED zkEVM TESTNET UPDATE

Date: Tue, 21st Nov
Time: 07:00 UTC / 08:00 CET
Duration: ~30 mins

Please note an upcoming important update of zkEVM Testnet infrastructure will happen on Nov 21 at 07:00 UTC. The network will be available during the update, except for ~2 mins for sequencer restart.

This update brings many significant changes to zkEVM node, bridge and prover infrastructure, including changes to RPC, sequencer, synchroniser, database. It also includes WS improvements, along with other fixes.

Please find the versions below:
Node version: v0.4.0 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.4.0)

Prover version: v3.0.2 (https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v3.0.2)

Bridge version: v0.3.0 (https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.3.0)


Things to note:
-Be prepared for the scheduled update.
-Stay updated on the progress through official communication channels.
-For infrastructure partners, detailed instructions will be shared on the day of update. Please wait for the official update on Tues before updating to v0.4.0.


### 9th Nov, 2023

Upcoming zkEVM mainnet UPGRADE: Incaberry hardfork

Date: Thurs, 9th Nov 2023
Time: 10:00 AM CET / 09:00 AM UTC
Duration: ~1 hour operation

Incaberry upgrade will bring cryptographic optimisations and bug fixes to Polygon zkEVM mainnet. After the upgrade, the node should be restarted to update to the new fork. 
The network will be available, except for ~2 min for sequencer restart. Communication will be done when the network resumes operations.

Things to note: 
⚠️ Note that the version v0.3.2 with Prover v3.0.0 are required to be able to upgrade the network to Incaberry.
Although, partners are recommended to update to v0.3.3. 
⚠️ Note that the version v0.3.1 with Prover v2.2.2 and earlier would be obsolete.

Before Incaberry is Live on mainnet, infrastructure partners will need to update to the latest versions of the node and prover. The GitHub repos and changelogs would be found here:
Node v0.3.3 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.3.3)

Prover v3.0.0 (https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v3.0.0)


What needs to be done:
-Standby for the upgrade instructions on Thursday
-Stay updated on the progress through official communication channels
-For infrastructure partners, before the Incaberry upgrade, please follow the instructions to update to node v0.3.3 here (https://www.notion.so/Instructions-zkEVM-Mainnet-Node-v0-3-3-Prover-v3-0-0-b14faaf6e2f146f0961e3b1556adec34?pvs=21)

-For infrastructure partners, AFTER the Incaberry hard fork, please restart the node, and start the RPC to update to the new fork


### 7th Nov, 2023
zkEVM Mainnet: Upcoming Incaberry hardfork preparation

Date: Tues, 7th Nov 2023
Time: 03:00 PM UTC / 04:00 PM CET
Duration: ~1 hour operation

As a preparation for the the Incaberry upgrade, the mainnet node will be updated to v0.3.3 and prover to v3.0.0. There are updates to the RPC, sequencer and synchroniser

The network will be available, except for ~2 min for sequencer restart. Communication will be done when the network resumes operations.

Things to note:

⚠️Note that the version v0.3.2 with Prover v3.0.0 are required to be able to upgrade the network to Incaberry. Although, partners are recommended to update to v0.3.3.

⚠️Note that the version v0.3.1 with Prover v2.2.2 and earlier would be obsolete.

Before Incaberry is Live on mainnet, infrastructure partners will need to update to the latest versions of the node and prover. The GitHub repos and changelogs would be found here:
Node v0.3.3 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.3.3)

Prover v3.0.0 (https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v3.0.0)


What needs to be done:
-Standby for the node updates/instructions on Tuesday
-Stay updated on the progress through official communication channels
-For infrastructure partners, after the Tuesday update, please follow the instructions to update to node v0.3.3 here (https://polygontechnology.notion.site/Instructions-zkEVM-Mainnet-Node-v0-3-3-Prover-v3-0-0-b14faaf6e2f146f0961e3b1556adec34?pvs=4)


### 24th Oct, 2023
This update includes a fix for situations when there is a 'stateRoot calculated is different from the stateRoot received during the trustedState synchronisation' error that resolves after a synchroniser restart. 

There is no expected network downtime, a micro outage at most.

This version is highly recommended for RPC providers and does not require any config changes.

Upcoming zkEVM testnet UPGRADE: Incaberry hardfork

Date: Tues, 24th Oct 2023
Time: 02:00 PM UTC / 04:00 PM CEST
Duration: ~1 hour operation

Incaberry upgrade will bring cryptographic optimisations and bug fixes to Polygon zkEVM testnet. Before the upgrade, the node should be updated to v0.3.2 and prover to v3.0.0. There are updates to the RPC, sequencer and synchroniser as well.

The network will be available, except for ~2 min for sequencer restart. Communication will be done when the network resumes operations.

Things to note:
 ⚠️: Note that the version v0.3.2 with Prover v3.0.0 are required to be able to upgrade the network to Incaberry
 ⚠️: Note that the version v0.3.1 with Prover v2.2.2 and earlier would be obsolete.

Before Incaberry is Live on testnet, infrastructure partners will need to update to the latest versions of the node and prover. The GitHub repos and changelogs would be found here:
Node v0.3.2(https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.3.2)

Prover v3.0.0(https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v3.0.0)


What needs to be done:
1. Be prepared for the Incaberry upgrade
2. Stay updated on the progress through official communication channels

For infrastructure partners, BEFORE the upgrade, please follow the instructions (https://www.notion.so/Instructions-zkEVM-Testnet-Node-v0-3-5-Prover-v2-2-6-18d0b34840874e7cb9ded72e8a9e4e08?pvs=21) to update to node v0.3.2 here


### 26th Sep, 2023

Upcoming Mainnet Beta Update
Date: TUE 26th Sept
Time: 4.30 AM UTC/ 6.30 AM CEST
Duration: 15 mins approximately

Node v0.3.1
 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.3.1)
Prover v2.2.2 
(https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v2.2.2)


### 20th Sep, 2023
Scheduled UPGRADE: zkEVM Mainnet Beta Dragonfruit (ForkID5) UPGRADE

Date: Wed, 20th Sept 2023
Time: 7:30 AM UTC / 09.30 AM CEST
Duration: ~2 hours

The Dragon Fruit upgrade covers a range of improvements to the network, including support for the latest Ethereum opcode, PUSH0. For more details, please refer to the blog post here (https://polygon.technology/blog/polygon-zkevm-dragon-fruit-upgrade-with-new-opcode-coming-to-mainnet-beta)


Things to note:
⚠️ Note that the version v0.3.0 with Prover v2.2.0 are required to be able to upgrade the network to Dragon Fruit [ForkID5] 
⚠️ Note that the version v0.1.2 with Prover v1.1.4 and earlier are now obsolete

During the upgrade, the network will be available. No disruptions will take place for the 2 hours of deployment, except for a small downtime of ~2 mins for sequencer restart. But the bridge will be unavailable for approx. 3.5 hours. Communication will be done when the bridge resumes operations.

Upgrade Time Lock compliance:
The 10-day timelock for upgrading Polygon zkEVM Mainnet Beta (https://x.com/0xPolygon/status/1697286124375277647?s=20) was initiated on Aug 31st, 2023 and completed on Sept 10, 2023.

The upgraded contract can be checked here (https://etherscan.io/address/0x301442aA888701c8B86727d42F3C55Fb0dd9eF7F#readContract)


The transaction hash containing the upgrade proposal and its signatures can be found here (https://etherscan.io/tx/0x94c0d1e336349013d0fe2072375d5b40c174fc26f7f1b06f23ddf4c6b1142519)


What needs to be done:
-Be prepared for the ForkID5 upgrade and bridge downtime
-Stay updated on the progress through official communication channels
-For infrastructure partners who have not updated to latest version please follow the instructions to update to node v0.3.0 here (https://www.notion.so/Mainnet-Beta-UPDATE-zkEVM-Node-version-0-3-0-Sep-6-e150867951cd46c088f6d6c03b2cb5db?pvs=21)


### 18th Sep, 2023
18th Sept
Upcoming Mainnet Beta event REMINDER!
Today, Mon 18th Sept, the scheduled mainnet beta rehashing + L2 bridge resync will be started in ~60 minutes.

Duration: 6 hours approximately
During the update, the network and bridge will be unavailable. Communication will be done when the network resumes operations.

What needs to be done:
1. Be prepared for the scheduled downtime.
2. Stay updated on our progress through our official communication channels.
3. After the event is complete, please wait for the updated snapshots communication
4. For infrastructure partners, after the updated snapshots are available, please follow the instructions here 
https://www.notion.so/polygontechnology/zkEVM-mainnet-beta-Instructions-for-permissionless-nodes-to-rehash-the-network-53b525498bc94c03ab02bba621f8d8e3


### 6th Sep, 2023
UPDATE: ZKEVM MAINNET BETA

Update Date and Time:
Date: Wednesday, September 6th
Time: 11:00 hrs UTC / 13:00 hrs CEST
Duration: Approximately 1 hour

Important Notice: During this update, the network will be temporarily unavailable.


We are excited to announce a crucial update to our ZKEVM Mainnet Beta. This update introduces the latest versions of both the Node and Prover components:

Node:v0.3.0: https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.3.0

This update includes Node:v0.3.0, which incorporates a critical fix implemented this week, ensuring enhanced stability and performance.

Prover:v2.2.0: https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v2.2.0

We have seamlessly integrated Prover:v2.2.0 into this release. We kindly request your assistance in verifying its inclusion and ensuring that no other release candidate has been introduced in its place.

To our valued Infra Providers, please follow the provided instructions to ensure a smooth transition
We appreciate your ongoing support as we continue to improve and optimize the Mainnet Beta. If you have any questions or require assistance, please feel free to reach out.


### 31st Aug, 2023
SCHEDULED ZKEVM MAINNET UPDATE

Date: Thursday, 31st Aug 2023
Time: 09:00 UTC / 11: 00 CEST
Duration: ~ 1hr

A Mainnet update has been scheduled to release versions Node v0.2.5 (https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.2.5) and Prover v2.1.2.
 (https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v2.1.2) 
 
We recommend to update to this version of the Node as it brings the fixes to issues that created a version rollback during the last mainnet update.


### 27th Jul, 2023
SCHEDULED zkEVM MAINNET BETA UPDATE

Date: Thursday, July 27th, 2023
Time: 7:00 UTC / 9:00 CEST / 3:00 (am) EST
Duration: 90 minutes (during the update window, the network will be unavailable)
Version Upgrade for Prover, Node and Bridge

Notes:
We are scheduling the next MAINNET BETA UPDATE this week on Thursday 27 July 2023 at early morning hours (7:00 UTC)
This is an important update, considered as essential since the build brings new features, important fixes and optimisations that are critical for an optimized performance of Mainnet Beta.
There are config changes that must considered as we are releasing new versions of the Node, Prover and Bridge. We have prepared documentation that contains the change logs and instructions related to service providers.
In this document you will find more details.


### 8th June, 2023
MAINNET BETA update complete. Full network service resumed.

Please ensure you are using the latest versions of the Node & Prover as they will be the recommended packages to run for zkEVM Mainnet Beta.
You can find the detailed change log for each component in the links below.

Prover: v1.1.4-fork.4
changelog: https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v1.1.4-fork.4

Node: v0.1.2
changelog: https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.1.2
The latest bridge service version remains: v0.1.0 


### 2nd May, 2023
https://github.com/0xPolygonHermez/zkevm-node/tree/v0.0.7


### 25th Apr, 2023
UPDATE MAINNET

We've updated mainnet! We encourage you to update your nodes as well, here's the release: https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.0.6. Both node and prover containers have new versions, and prover has some new config parameters that are reflected on the shared files in the release. Also, I'd like to let you know that we're working on a process to improve how we communicate this updates, changelogs, config changes... That we hope that it will be ready for next release

Telegram: https://t.me/polygonzkevm_technical_updates/31
