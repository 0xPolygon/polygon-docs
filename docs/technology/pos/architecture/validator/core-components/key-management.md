---
id: key-management
title: Key Management
description: Signer and owner keys management
keywords:
  - docs
  - polygon
  - matic
  - key
  - key management
  - signer
  - owner
slug: key-management
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Each validator uses two keys to manage validator related activities on Polygon:

* Signer key
* Owner key

## Signer Key

The signer key is the address used to sign Heimdall blocks, checkpoints, and other signing related activities.

The signer address's private key must be located on the machine running the validator node for signing purposes.

The signer key cannot manage staking, rewards, or delegations.

The validator must keep ETH on the signer address on the Ethereum mainnet to send checkpoints.

## Owner Key

The owner key is the address used to stake, restake, change the signer key, withdraw rewards and manage delegation related parameters on the Ethereum mainnet. The private key for the owner key must be secure at all costs.

All transactions through the owner key are performed on the Ethereum mainnet.

The signer key is kept on the node and is generally considered a **hot** wallet, whereas the owner key is supposed to kept very secure, is used infrequently, and is generally considered a **cold** wallet. The staked funds are controlled by the owner key.

This separation of responsibilities between the signer and the owner keys is done to ensure an efficient tradeoff between security and ease of use.

Both keys are Ethereum compatible addresses and work in the exactl the same manner.

## Signer Change

See [Change Your Signer Address](/docs/pos/validator/change-signer-address).
