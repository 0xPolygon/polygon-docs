---
id: state-sync
title: State Sync Mechanism
description: Mechanism to read Ethereum data from Matic EVM chain
keywords:
  - docs
  - matic
  - state sync
  - mechanism
  - read ethereum data
image: https://matic.network/banners/matic-network-16x9.png 
---

# State Sync Mechanism

`State Sync` is the native mechanism to read Ethereum data from Matic EVM chain. 

Validators on the Heimdall layer pickup the [StateSynced](https://github.com/maticnetwork/contracts/blob/a4c26d59ca6e842af2b8d2265be1da15189e29a4/contracts/root/stateSyncer/StateSender.sol#L24) event and pass it on to the Bor layer (read more about the architecture [here](/docs/pos/design/bor/overview). 

The receiver contract inherits [IStateReceiver](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol), and custom logic sits inside [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/05556cfd91a6879a8190a6828428f50e4912ee1a/contracts/IStateReceiver.sol#L5) function.


This is the flow required from dapps / users to work with state-sync:

1. Call the smart contract function present here: [https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33](https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33)
2. Which emits an event called `StateSynced(uint256 indexed id, address indexed contractAddress, bytes data);`
3. All the validators on the Heimdall chain receive this event and one of them, whoever wishes to get the tx fees for state sync sends this transaction to Heimdall.
4. Once `state-sync` transaction on Heimdall has been included in a block, it is added to pending state-sync list.
5. After every sprint on `bor`, the Bor node fetches the pending state-sync events from Heimdall via an API call.
6. The receiver contract inherits `IStateReceiver` interface, and custom logic of decoding the data bytes and performing any action sits inside `onStateReceive` function: [https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol)
