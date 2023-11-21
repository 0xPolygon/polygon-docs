---
id: how-state-sync-works
title: How does State Sync work?
description: "Sending the state from the Ethereum chain to the Bor chain."
keywords:
  - docs
  - matic
  - state sync
  - working
image: https://matic.network/banners/matic-network-16x9.png 
---

# How does State Sync work?

State management sends the state from the Ethereum chain to the Bor chain. It is called **state-sync**.

State transfer from Ethereum to Bor happens through system call. Suppose, a user deposits USDC to the deposit manager on Ethereum. Validators listen to those events, validate, and store them in Heimdall state. Bor gets the latest state-sync records and updates the Bor state (mints equal amount of USDC on Bor) using a system call. 

## State sender

Source: [https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol)

To sync state, the contract calls following method **state sender contract** on Ethereum chain. 

```jsx
contract StateSender {
	/**
	 * Emits `stateSynced` events to start sync process on Ethereum chain
	 * @param receiver    Target contract on Bor chain
	 * @param data        Data to send
	 */
	function syncState (
		address receiver, 
		bytes calldata data
	) external;
}
```

`receiver` contract must be present on the child chain, which receives state `data` once the process is complete. `syncState` emits `StateSynced` event on Ethereum, which is the following:

```jsx
/**
 * Emits `stateSynced` events to start sync process on Ethereum chain
 * @param id                  State id
 * @param contractAddress     Target contract address on Bor
 * @param data                Data to send to Bor chain for Target contract address
 */
event StateSynced (
	uint256 indexed id, 
	address indexed contractAddress, 
	bytes data
);
```

Once the `StateSynced` event emitted on the `stateSender` contract on the Ethereum chain, Heimdall listens to those events and adds to the Heimdall state after 2/3+ validators agree on the.

After every sprint (currently 64 blocks on Bor), Bor fetches new state-sync record and updates the state using a `system` call. Here is the code for the same: [https://github.com/maticnetwork/bor/blob/6f0f08daecaebbff44cf18bee558fc3796d41832/consensus/bor/genesis_contracts_client.go#L51](https://github.com/maticnetwork/bor/blob/6f0f08daecaebbff44cf18bee558fc3796d41832/consensus/bor/genesis_contracts_client.go#L51)

During `commitState`, Bor executes `onStateReceive`, with `stateId` and `data` as args, on target contract.

## State receiver interface on Bor

`receiver` contract on Bor chain must implement following interface.

```jsx
// IStateReceiver represents interface to receive state
interface IStateReceiver {
  function onStateReceive(uint256 stateId, bytes calldata data) external;
}
```

Only `0x0000000000000000000000000000000000001001` — `StateReceiver.sol`, must be allowed to call `onStateReceive` function on target contract.

## System Call

Only system address, `2^160-2`, allows making a system call. Bor calls it internally with the system address as `msg.sender`. It changes the contract state and updates the state root for a particular block. Inspired from [https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md) and [https://wiki.parity.io/Validator-Set#contracts](https://wiki.parity.io/Validator-Set#contracts)

System call is helpful to change state to contract without making any transaction.

## State-sync logs and Bor Block Receipt

Events emitted by system calls are handled in a different way than normal logs. Here is the code: [https://github.com/maticnetwork/bor/pull/90](https://github.com/maticnetwork/bor/pull/90).

Bor produces a new tx / receipt just for the client which includes all the logs for state-sync. Tx hash is derived from block number and block hash (last block at that sprint):

```jsx
keccak256("matic-bor-receipt-" + block number + block hash)
```

This doesn't change any consensus logic, only client changes. `eth_getBlockByNumber`, `eth_getTransactionReceipt`,  and `eth_getLogs` include state-sync logs with derived. Note that the bloom filter on the block doesn't include inclusion for state-sync logs. It also doesn't include derived tx in `transactionRoot` or `receiptRoot`.