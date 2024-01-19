`State Sync` is the native mechanism for a user in the Polygon PoS chain to read the latest Ethereum data.

Validators on the Heimdall layer pickup the [StateSynced](https://github.com/maticnetwork/contracts/blob/a4c26d59ca6e842af2b8d2265be1da15189e29a4/contracts/root/stateSyncer/StateSender.sol#L24) event and pass it on to the Bor layer.

The receiver contract inherits [IStateReceiver](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol), and custom logic sits inside [onStateReceive](https://github.com/maticnetwork/genesis-contracts/blob/05556cfd91a6879a8190a6828428f50e4912ee1a/contracts/IStateReceiver.sol#L5) function.

This is the flow required from dapps / users to work with state-sync:

1. Call the smart contract function present here: [https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33](https://github.com/maticnetwork/contracts/blob/19163ddecf91db17333859ae72dd73c91bee6191/contracts/root/stateSyncer/StateSender.sol#L33)
2. Which emits an event called `StateSynced(uint256 indexed id, address indexed contractAddress, bytes data);`
3. All the validators on the Heimdall chain receive this event and one of them, whoever wishes to get the tx fees for state sync sends this transaction to Heimdall.
4. Once `state-sync` transaction on Heimdall has been included in a block, it is added to pending state-sync list.
5. After every sprint on `bor`, the Bor node fetches the pending state-sync events from Heimdall via an API call.
6. The receiver contract inherits `IStateReceiver` interface, and custom logic of decoding the data bytes and performing any action sits inside `onStateReceive` function: [https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/IStateReceiver.sol)

## How does State Sync work?

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

## System call

Only system address, `2^160-2`, allows making a system call. Bor calls it internally with the system address as `msg.sender`. It changes the contract state and updates the state root for a particular block. Inspired by [https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md). 
<!-- and [https://wiki.parity.io/Validator-Set#contracts](https://wiki.parity.io/Validator-Set#contracts) -->

System call is helpful to change state to contract without making any transaction.

## State-sync logs and Bor block receipts

Events emitted by system calls are handled in a different way than normal logs. Here is the code: [https://github.com/maticnetwork/bor/pull/90](https://github.com/maticnetwork/bor/pull/90).

Bor produces a new tx / receipt just for the client which includes all the logs for state-sync. Tx hash is derived from block number and block hash (last block at that sprint):

```jsx
keccak256("matic-bor-receipt-" + block number + block hash)
```

This doesn't change any consensus logic, only client changes. `eth_getBlockByNumber`, `eth_getTransactionReceipt`,  and `eth_getLogs` include state-sync logs with derived. Note that the bloom filter on the block doesn't include inclusion for state-sync logs. It also doesn't include derived tx in `transactionRoot` or `receiptRoot`.
