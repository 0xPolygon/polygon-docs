---
id: commit-chain-multisigs
title: PoS Mainnet Multi-Signatures
sidebar_label: Multisigs
description: "A comprehensive guide on active multi-signature wallets in the Polygon PoS Mainnet."
keywords:
  - docs
  - polygon
  - matic
  - multisignature
  - multisig
  - address
image: https://wiki.polygon.technology/img/polygon-logo.png
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Purpose & Capabilities

The primary role of multi-signature wallets (multisigs) is to facilitate contract upgrades during the early stages of development. As these contracts become more robust, Polygon plans to:

- Transition from multisigs to governance-controlled proxies.
- Implement timelocks for added security.
- Phase out multisigs entirely in the long term.

**It's important to note that the existing multisigs do not have the capability to censor transactions, including bridge transactions.**

## Active Multi-Signature Wallets

### Ethereum Chain Multisigs

| Multisig Address  | **5/9 Multisig**<br/>`0xFa7D2a996aC6350f4b56C043112Da0366a59b74c` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To upgrade PoS and staking contracts on Ethereum.                    |
| Chain            | Ethereum                                                            |
| Rights           | - Update staking contracts for optimizations and upgrades.<br/>- Address unexpected bugs in PoS contracts. |
| Signatories      | Quickswap, Curve, Polygon, Horizon Games, Cometh                     |

### Polygon Commitchain Multisigs

| Multisig Address  | **5/8 Multisig**<br/>`0x355b8E02e7F5301E6fac9b7cAc1D6D9c86C0343f` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To update custom ChildERC20s on Polygon Commitchain.                 |
| Chain            | Polygon Commitchain                                                  |
| Rights           | Ability to upgrade custom child contracts.                           |
| Signatories      | Quickswap, Curve, Polygon, Horizon Games, Cometh                     |

### Custom Child ERC20s Mapping

| Multisig Address  | **4/8 Multisig**<br/>`0x424bDE99FCfB68c5a1218fd3215caFfD031f19C4` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To enable the mapping of custom ChildERC20s with Mainnet contracts.  |
| Chain            | Ethereum                                                            |
| Rights           | Limited to mapping; no access to Child tokens or deposit/withdrawal rights. |
| Signatories      | Polygon                                                             |

### Permissionless Mapping

| Multisig Address  | **Permissionless Mapping of Standard ChildERC20 Tokens (No Multisig Required)** |
|:----------------:|--------------------------------------------------------------------------------|
| Purpose          | FxPortal supports permissionless token mapping of standard ChildERC20 for any ERC20 token on Ethereum. |
| Chain            | Permissionless                                                                 |
| Rights           | Permissionless                                                                 |
| Signatories      | Permissionless                                                                 |

<sub>*Plans are underway to transition these functions to governance. We are currently exploring options such as Aave's governance contracts and Compound’s timelock contracts.</sub>
