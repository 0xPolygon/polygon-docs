---
id: overview
title: Overview
description: The Bor node is basically the blockchain operator
keywords:
  - docs
  - matic
  - polygon
  - bor
  - geth
image: https://matic.network/banners/matic-network-16x9.png
---

# Bor

The Bor node or the Block Producer implementation is basically the EVM-compatible blockchain operator. Currently, it is a basic Geth implementation with custom changes done to the consensus algorithm. However, this will be built from the ground up to make it lightweight and focused.

Block producers are chosen from the Validator set and are shuffled using historical Ethereum block hashes for the same purpose. However, we are exploring sources of randomness for this selection.