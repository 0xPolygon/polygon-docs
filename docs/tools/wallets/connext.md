---
id: connext
title: Crosschain transfers using Connext
description: Build your next blockchain app on Polygon.
keywords:
  - docs
  - matic
  - connext
  - polygon
image: https://wiki.polygon.technology/img/polygon-logo.png
---

import useBaseUrl from '@docusaurus/useBaseUrl';

:::caution Content disclaimer

Please view the third-party content disclaimer [<ins>here</ins>](https://github.com/0xPolygon/wiki/blob/master/CONTENT_DISCLAIMER.md).

:::

---

Connext is a crosschain liquidity network that powers fast, fully noncustodial swaps between evm-compatible chains and Ethereum L2 systems.

Ethereum is going multichain. With the growing adoption of evm-compatible chains and L2s, a new challenge has emerged around liquidity fragmentation within the ecosystem. Connext solves this problem by connecting discrete liquidity pools on each chain into a global network, without introducing new, significant trust considerations for users. Developers can leverage this liquidity to build a new class of natively chain-agnostic dApps on Connext.

At a high level, Connext lets users swap assetA on chainA for assetB on chainB using conditional transfers. This happens in a few simple steps:

Alice, a user of Connext, sends a conditional transfer of assetA to Bob.
Bob, a liquidity provider (aka a router), sends an equivalent amount of assetB to Alice.
Alice unlocks her conditional transfer to receive assetB, which in turn allows Bob to do the same.
Routers form the backbone of our network, providing liquidity on different chains and earning fees for doing so. You can learn more about how this works trustlessly in our Protocol Primer.

To setup  crosschain transfers from the Ethereum Goerli Testnet to the Polygon Mumbai Testnet in a browser dApp please go through this [guide](https://docs.connext.network/quickstart-polygon-matic-integration).
