---
id: checkpoint-mechanism
title: Checkpoint Mechanism
sidebar_label: Checkpoints
description: Checkpointing the system state to the Ethereum mainnet
keywords:
  - docs
  - matic
  - polygon
  - checkpoint
  - ethereum
  - mainnet
slug: checkpoint-mechanism
image: https://wiki.polygon.technology/img/polygon-logo.png
---

:::info Polygon is not a Layer 1 platform

Polygon depends on the Ethereum Mainnet as its Layer 1 Settlement Layer. All staking mechanics need to be in sync with the contracts on the Ethereum mainnet.

:::

Proposers for a checkpoint are initially selected via [Tendermint’s weighted round-robin algorithm](https://docs.tendermint.com/master/spec/consensus/proposer-selection.html). A further custom check is implemented based on the checkpoint submission success. This allows the Polygon system to decouple with Tendermint proposer selection and provides Polygon with abilities like selecting a proposer only when the checkpoint transaction on the Ethereum mainnet succeeds or submitting a checkpoint transaction for the blocks belonging to previous failed checkpoints.

Successfully submitting a checkpoint on Tendermint is a 2-phase commit process:

* A proposer, selected via the round-robin algorithm, sends a checkpoint with the proposer's address and the Merkle hash in the proposer field.
* All other proposers validate the data in the proposer field before adding the Merkle hash in their state.

The next proposer then sends an acknowledgment transaction to prove that the previous checkpoint transaction has succeeded on the Ethereum mainnet. Every validator set change is relayed by the validator nodes on Heimdall which is embedded onto the validator node. This allows Heimdall to remain in sync with the Polygon contract state on the Ethereum mainnet at all times.

The Polygon contract deployed on the Ethereum mainnet is considered to be the ultimate source of truth, and therefore all validation is done via querying the Ethereum mainnet contract.
