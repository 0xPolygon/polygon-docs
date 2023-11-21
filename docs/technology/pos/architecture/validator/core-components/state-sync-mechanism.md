---
id: state-sync-mechanism
title: State Sync Mechanism
description: State sync mechanism to natively read Ethereum data
keywords:
  - docs
  - matic
  - polygon
  - state sync
  - mechanism
slug: state-sync-mechanism
image: https://wiki.polygon.technology/img/polygon-logo.png
---

Validators on the Heimdall layer pick up the [StateSynced](https://github.com/maticnetwork/contracts/blob/a4c26d59ca6e842af2b8d2265be1da15189e29a4/contracts/root/stateSyncer/StateSender.sol#L24) event and pass the event on to the Bor layer. See also [Polygon Architecture](/docs/pos/polygon-architecture).

The **receiver contract** inherits [IStateReceiver](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol), and custom logic sits inside the [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/05556cfd91a6879a8190a6828428f50e4912ee1a/contracts/IStateReceiver.sol#L5) function.

The latest version, [Heimdall v0.3.4](https://github.com/maticnetwork/heimdall/releases/tag/v0.3.4), contains a few enhancements such as:
1. Restricting data size in state sync txs to:
    * **30Kb** when represented in **bytes**
    * **60Kb** when represented as **string**.
2. Increasing the **delay time** between the contract events of different validators to ensure that the mempool doesn't get filled very quickly in case of a burst of events which can hamper the progress of the chain.

The following example shows how the data size is restricted:

```
Data - "abcd1234"
Length in string format - 8
Hex Byte representation - [171 205 18 52]
Length in byte format - 4
```

## Requirements for the users

Things required from dapps/users to work with state-sync are:

1. Call the [syncState](https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33) function.
2. The `syncState` function emits an event called `StateSynced(uint256 indexed id, address indexed contractAddress, bytes data);`
3. All the validators on the Heimdall chain receive the `StateSynced` event. Any validator that wishes to get the transaction fee for the state sync sends the transaction to Heimdall.
4. Once the `state-sync` transaction on Heimdall is included in a block, it is added to the pending state-sync list.
5. After every sprint on Bor, the Bor node fetches the pending state-sync events from Heimdall via an API call.
6. The receiver contract inherits the `IStateReceiver` interface, and custom logic of decoding the data bytes and performing any action sits inside the [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol) function.
