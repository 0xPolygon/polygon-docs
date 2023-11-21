---
id: account-abstraction
title: Account Abstraction
sidebar_label: Overview
description: "Learn about how account abstraction can improve transaction experience"
keywords:
  - docs
  - polygon
  - matic
  - transaction
  - account abstraction
  - meta transaction
  - eip4337
  - EIP-4337
  - ERC-4337
image: https://wiki.polygon.technology/img/polygon-logo.png
slug: account-abstraction
---

Account Abstraction is a blockchain technology that enables users to utilize smart contracts as their accounts. While the default account for most users is an Externally Owned Account (EOA), which is controlled by an external private key, it requires users to have a considerable understanding of blockchain technology to use them securely. Fortunately, smart contract accounts can create superior user experiences.

## Benefits

Contract accounts offer numerous benefits, including:

- **Arbitrary verification logic:** Rather than use an external private key, contract accounts can use any arbitrary signature type. This feature supports single and multi-signature verification and any signature scheme.
- **Sponsored transactions:** Users can pay transaction fees in ERC-20 tokens or create their fee logic, including sponsoring transaction fees on their app.
- **Account security:** Contract accounts enable social recovery and security features such as time-locks and withdraw limits.
- **Atomic multi-operations:** Users can perform multiple operations simultaneously, such as trading in a single click instead of approving and swapping separately.

## Using Account Abstraction on Polygon

There are two primary ways users can use account abstraction on Polygon: by sending ERC-4337 transactions or with third party meta transaction services.

### ERC-4337

ERC-4337, also known is EIP-4337, brings account abstraction to the Polygon ecosystem and all EVM-compatible chains.

### Meta Transactions

Meta transactions are bespoke third party services for achieving account abstraction.
