---
id: core_concepts
title: Core Concepts
description: Bor is state chain in Polygon architecture
keywords:
  - docs
  - matic
  - Core Concepts
  - polygon
  - state chain
  - architecture
image: https://matic.network/banners/matic-network-16x9.png
---
import useBaseUrl from '@docusaurus/useBaseUrl';

# Core Concepts

Bor is state chain in Polygon architecture. It is a fork of Geth [https://github.com/ethereum/go-ethereum](https://github.com/ethereum/go-ethereum) with new consensus called Bor.

Source: [https://github.com/maticnetwork/bor](https://github.com/maticnetwork/bor)

## Consensus

Bor uses new improved consensus, inspired by [Clique consensus](https://eips.ethereum.org/EIPS/eip-225)

More details on consensus and specifications: [Bor Consensus](https://www.notion.so/Bor-Consensus-5e52461f01ef4291bc1caad9ab8419c5)

## Genesis

The genesis block contains all the essential information to configure the network. It's basically the config file for Bor chain. To boot up Bor chain, the user needs to pass in the location of the file as a param.

Bor uses `genesis.json` as Genesis block and params.  Here is an example for Bor genesis `config`:

```json
"config": {
    "chainId": 15001,
    "homesteadBlock": 1,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "bor": {
      "period": 1,
      "producerDelay": 4,
      "sprint": 64,
      "validatorContract": "0x0000000000000000000000000000000000001000",
      "stateReceiverContract": "0x0000000000000000000000000000000000001001"
    }
  }
```

[Config](https://www.notion.so/15ab7eb6e8124142a3641939762d6d67)

[Consensus specific config](https://www.notion.so/17a8a10c3bd44b8caf34432c057e401c)

## EVM/Solidity as VM

Bor uses un-modified EVM as a VM for a transaction. Developers can deploy any contract they wish using the same Ethereum tools and compiler like `solc` without any changes.

## MATIC as Native token (Gas token)

Bor has a MATIC token as a native token similar to ETH in Ethereum. It is often called the gas token. This token works correctly as to how ETH works currently on the Ethereum chain.

In addition to that, Bor provides an in-built wrapped ERC20 token for the native token (similar to WETH token), which means applications can use wrapped MATIC ERC20 token in their applications without creating their own wrapped ERC20 version of the Matic native token.

Wrapped ERC20 token is deployed at `0000000000000000000000000000000000001010` as `[MRC20.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/child/MRC20.sol)` on Bor as one of the genesis contracts.

### Fees

Native token is used as fees while sending transaction on Bor. This prevents spam on Bor and provides incentives to Block Producers to run the chain for longer period and discourages bad behaviour.

A transaction sender defines `GasLimit` and `GasPrice` for each transaction and broadcasts it on Bor. Each producer can define how much minimum gas price they can accept using `--gas-price` while starting Bor node. If user-defined `GasPrice` on the transaction is the same or greater than producer defined gas price, the producer will accept the transaction and includes it in the next available block. This enables each producer to allow its own minimum gas price requirement.

Transaction fees will be deducted from sender's account in terms of Native token.

Here is the formula for transaction fees:

```go
Tx.Fee = Tx.GasUsed * Tx.GasPrice
```

Collected fees for all transactions in a block are transferred to the producer's account using coinbase transfer. Since having more staking power increases your probability to become a producer, it will allow a validator with high staking power to collect more rewards (in terms of fees) accordingly.

### Transfer receipt logs

The Matic token is no exception to that.

`LogTransfer` is a special log that is added to all compatible ERC20/721 tokens.  Consider it as one 2-inputs-2-outputs UTXO for transfer.  Here, `output1 = input1 - amount` and `output2 = input2 + amount`  This allows fraud-proof contracts to verify a transfer of Matic ERC20 tokens (here, Native token) on the Ethereum chain.

```jsx
/**
 * @param token    ERC20 token address
 * @param from     Sender address
 * @param to       Recipient address
 * @param amount   Transferred amount
 * @param input1   Sender's amount before the transfer is executed
 * @param input2   Recipient's amount before the transfer is executed
 * @param output1  Sender's amount after the transfer is executed
 * @param output2  Recipient's amount after the transfer is executed
 */
event LogTransfer(
    address indexed token,
    address indexed from,
    address indexed to,
    uint256 amount,
    uint256 input1,
    uint256 input2,
    uint256 output1,
    uint256 output2
);
```

Since, MATIC token is the native token and doesn't have Native ERC20 token, Bor adds receipt log for each transfer made for Native token using following Golang code. Source: [https://github.com/maticnetwork/bor/blob/develop/core/state_transition.go#L241-L252](https://github.com/maticnetwork/bor/blob/develop/core/state_transition.go#L241-L252)

```go
// addTransferLog adds transfer log into state
func addTransferLog(
	state vm.StateDB,
	eventSig common.Hash,

	sender,
	recipient common.Address,

	amount,
	input1,
	input2,
	output1,
	output2 *big.Int,
) {
	// ignore if amount is 0
	if amount.Cmp(bigZero) <= 0 {
		return
	}

	dataInputs := []*big.Int{
		amount,
		input1,
		input2,
		output1,
		output2,
	}

	var data []byte
	for _, v := range dataInputs {
		data = append(data, common.LeftPadBytes(v.Bytes(), 32)...)
	}

	// add transfer log
	state.AddLog(&types.Log{
		Address: feeAddress,
		Topics: []common.Hash{
			eventSig,
			feeAddress.Hash(),
			sender.Hash(),
			recipient.Hash(),
		},
		Data: data,
	})
}
```

### Deposit native token

A user can receive native token by depositing MATIC tokens on Ethereum main-chain to `DepositManager` contract (deployed on Ethereum chain). Source: [https://github.com/maticnetwork/contracts/blob/develop/contracts/root/depositManager/DepositManager.sol#L68](https://github.com/maticnetwork/contracts/blob/develop/contracts/root/depositManager/DepositManager.sol#L68)

```jsx
/**
 * Moves ERC20 tokens from Ethereum chain to Bor.
 * Allowance for the `_amount` tokens to DepositManager is needed before calling this function.
 * @param _token   Ethereum ERC20 token address which needs to be deposited
 * @param _amount  Transferred amount
 */
function depositERC20(address _token, uint256 _amount) external;
```

Using `depositERC20` tokens, users can move Matic ERC20 token (Native token) or any other ERC20 tokens from the Ethereum chain to Bor chain.

### Withdraw native token

Withdraw from Bor chain to Ethereum chain works exactly like any other ERC20 tokens. A user can call `withdraw` function on ERC20 contract, deployed on Bor, at `0000000000000000000000000000000000001010`  to initiate withdraw process for the same.  Source: [https://github.com/maticnetwork/contracts/blob/develop/contracts/child/MaticChildERC20.sol#L47-L61](https://github.com/maticnetwork/contracts/blob/develop/contracts/child/MaticChildERC20.sol#L47-L61)

```jsx
/**
 * Withdraw tokens from Bor chain to Ethereum chain
 * @param amount     Withdraw amount
 */
function withdraw(uint256 amount) public payable;
```

## In-built contracts (Genesis contracts)

Bor starts with three in-built contracts, often called genesis contracts. These contracts are available at block 0. Source: [https://github.com/maticnetwork/genesis-contracts](https://github.com/maticnetwork/genesis-contracts)

These contracts are compiled using `solc --bin-runtime`. Example, following command emits compiled code for `contract.sol`

```bash
solc --bin-runtime contract.sol
```

Genesis contract is defined in `genesis.json`. When bor starts at block 0, it loads all contracts with the mentioned code and balance.

```json
"0x0000000000000000000000000000000000001010": {
	"balance": "0x0",
	"code" : "0x..."
}
```

Below are the details for each genesis contract.

### Bor validator set

Source: [https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/BorValidatorSet.sol](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/BorValidatorSet.sol)

Deployed at: `0x0000000000000000000000000000000000001000`

`BorValidatorSet.sol` contract manages validator set for spans. Having a current validator set and span information into a contract allows other contracts to use that information. Since Bor uses producers from Heimdall (external source), it uses system call to change the contract state.

For first sprint all producers are defined in `BorValidatorSet.sol` directly.

`setInitialValidators` is called when the second span is being set. Since Bor doesn't support constructor for genesis contract, the first validator set needs to be set to `spans` map.

First span details are following:

```jsx
firstSpan = {
  number: 0,
	startBlock: 0,
	endBlock: 255
}
```

Solidity contract definition:

```jsx
contract BorValidatorSet {
  // Current sprint value
  uint256 public sprint = 64;

  // Validator details
  struct Validator {
    uint256 id;
    uint256 power;
    address signer;
  }

  // Span details
  struct Span {
    uint256 number;
    uint256 startBlock;
    uint256 endBlock;
  }

  // set of all validators
  mapping(uint256 => Validator[]) public validators;

  // set of all producers
  mapping(uint256 => Validator[]) public producers;

  mapping (uint256 => Span) public spans; // span number => span
  uint256[] public spanNumbers; // recent span numbers

	/// Initializes initial validators to spans mapping since there is no way to initialize through constructor for genesis contract
	function setInitialValidators() internal

	/// Get current validator set (last enacted or initial if no changes ever made) with a current stake.
	function getInitialValidators() public view returns (address[] memory, uint256[] memory;

  /// Returns bor validator set at given block number
  function getBorValidators(uint256 number) public view returns (address[] memory, uint256[] memory);

  /// Proposes new span in case of force-ful span change
  function proposeSpan() external;

  /// Commits span (called through system call)
  function commitSpan(
    uint256 newSpan,
    uint256 startBlock,
    uint256 endBlock,
    bytes calldata validatorBytes,
    bytes calldata producerBytes
  ) external onlySystem;

  /// Returns current span number based on current block number
  function currentSpanNumber() public view returns (uint256);
}
```

`proposeSpan` can be called by any valid validator with zero fees. Bor allows `proposeSpan` transaction to be free transaction since it is part of the system.

`commitSpan` is being called through the [system call](https://www.notion.so/maticnetwork/Overview-c8bdb110cd4d4090a7e1589ac1006bab#bba582b9e9c441d983aeec851b9421f9).

### State receiver

Source: [https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/StateReceiver.sol](https://github.com/maticnetwork/genesis-contracts/blob/master/contracts/StateReceiver.sol)

Deployed at: `0x0000000000000000000000000000000000001001`

The `StateReceiver` contract provides a mechanism for receiving and storing state data from other contracts and notifying interested parties (i.e., contracts) of state changes.
The state-sync mechanism allows for the transfer of state data from the Ethereum chain to Bor.

```jsx
contract StateReceiver is System {
  using RLPReader for bytes;
  using RLPReader for RLPReader.RLPItem;

  uint256 public lastStateId;

  function commitState(uint256 syncTime, bytes calldata recordBytes) onlySystem external returns(bool success) {
    // parse state data
    RLPReader.RLPItem[] memory dataList = recordBytes.toRlpItem().toList();
    uint256 stateId = dataList[0].toUint();
    require(
      lastStateId + 1 == stateId,
      "StateIds are not sequential"
    );
    lastStateId++;

    address receiver = dataList[1].toAddress();
    bytes memory stateData = dataList[2].toBytes();
    // notify state receiver contract, in a non-revert manner
    if (isContract(receiver)) {
      uint256 txGas = 5000000;
      bytes memory data = abi.encodeWithSignature("onStateReceive(uint256,bytes)", stateId, stateData);
      // solium-disable-next-line security/no-inline-assembly
      assembly {
        success := call(txGas, receiver, 0, add(data, 0x20), mload(data), 0, 0)
      }
    }
  }

  // check if address is contract
  function isContract(address _addr) private view returns (bool){
    uint32 size;
    assembly {
      size := extcodesize(_addr)
    }
    return (size > 0);
  }
}
```

- `commitState`: Called by authorized contracts, this function updates the contract's state by parsing state data and checking its sequential order. If the data is from a contract, it calls the `onStateReceive` function on that contract.
- `isContract`: This function checks whether a given address belongs to a contract or not by checking its bytecode size, used in `commitState`.

### MATIC ERC20 token

Source: [https://github.com/maticnetwork/contracts/blob/develop/contracts/child/MaticChildERC20.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/child/MaticChildERC20.sol)

Deployed at: `0x0000000000000000000000000000000000001010`

This is special contract that wraps native coin (like $ETH in Ethereum) and provides an ERC20 token interface. Example: `transfer` on this contract transfers native tokens. `withdraw` method in ERC20 token allows users to move their tokens from Bor to Ethereum chain.

Note: This contract doesn't support `allowance`. This is same for every compatible ERC20 token contract.

```jsx
contract MaticChildERC20 is BaseERC20 {
  event Transfer(address indexed from, address indexed to, uint256 value);

  uint256 public currentSupply;
  uint8 private constant DECIMALS = 18;

  constructor() public {}

  // Initializes state since genesis contract doesn't support constructor
  function initialize(address _childChain, address _token) public;

  /**
   * Deposit tokens to the user account
   * This deposit is only made through state receiver address
   * @param user   Deposit address
   * @param amount Withdraw amount
   */
  function deposit(address user, uint256 amount) public onlyOwner;

  /**
   * Withdraw amount to Ethereum chain
   * @param amount Withdraw amount
   */
  function withdraw(uint256 amount) public payable;

  function name() public pure returns (string memory) {
      return "Matic Token";
  }

  function symbol() public pure returns (string memory) {
      return "MATIC";
  }

  function decimals() public pure returns (uint8) {
      return DECIMALS;
  }

  /**
   * Total supply for the token.
   * This is 10b tokens, same as total Matic supply on Ethereum chain
   */
  function totalSupply() public view returns (uint256) {
      return 10000000000 * 10**uint256(DECIMALS);
  }

  /**
   * Balance of particular account
   * @param account Target address
   */
  function balanceOf(address account) public view returns (uint256) {
      return account.balance;
  }

  /**
   *  Function that is called when a user or another contract wants to transfer funds
   *  @param to Address of token receiver
   *  @param value Number of tokens to transfer
   *  @return Returns success of function call
   */
  function transfer(address to, uint256 value) public payable returns (bool) {
    if (msg.value != value) {
		  return false;
    }
    return _transferFrom(msg.sender, to, value);
  }

  /**
   * This enables to transfer native token between users
   * while keeping the interface the same as that of an ERC20 Token
   * @param _transfer is invoked by _transferFrom method that is inherited from BaseERC20
   */
  function _transfer(address sender, address recipient, uint256 amount) internal {
    address(uint160(recipient)).transfer(amount);
    emit Transfer(sender, recipient, amount);
  }
}
```

## System Call

Only system address, `2^160-2`, allows making a system call. Bor calls it internally with the system address as `msg.sender`. It changes the contract state and updates the state root for a particular block. Inspired from [https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-210.md) and [https://wiki.parity.io/Validator-Set#contracts](https://wiki.parity.io/Validator-Set#contracts)

System call is helpful to change state to contract without making any transaction.

Limitation: Currently events emitted by system call are not observable and not-included in any transaction or block.

## Span Management

Span is a logically defined set of blocks for which a set of validators is chosen from among all the available validators. Heimdall will select the committee of producers out of all validators. The producers will include a subset of validators depending upon the number of validators in the system.

<img src={useBaseUrl("img/Bor/span-management.svg")} />

### Propose Span Transaction

Type: **Heimdall transaction**

Source: [https://github.com/maticnetwork/heimdall/blob/develop/bor/handler.go#L27](https://github.com/maticnetwork/heimdall/blob/develop/bor/handler.go#L27)

`spanProposeTx` sets validators’ committee for a given `span` in case of successful transaction inclusion. One transaction for each span must be included in Heimdall. It is called `spanProposeTx` on Heimdall. `spanProposeTx` must revert if being sent frequently or there is no less than 33% stake change occurred within the current committee (for, given `span`).

`bor` module on Heimdall handles span management. Here is how Bor chooses producers out of all validators:

1. Bor creates multiple slots based on validators' power. Example: A with power 10 will have 10 slots, B with power 20 with have 20 slots.
2. With all slots, `shuffle` function shuffles them using `seed` and selects first `producerCount` producers.  `bor` module on Heimdall uses ETH 2.0 shuffle algorithm to choose producers out of all validators. Each span `n` uses block hash of Ethereum (ETH 1.0) block `n`  as `seed`. Note that slots based selection allows validators to get selected based on their power. The higher power validator will have a higher probability to get selected. Source: [https://github.com/maticnetwork/heimdall/blob/develop/bor/selection.go](https://github.com/maticnetwork/heimdall/blob/develop/bor/selection.go)

```go
// SelectNextProducers selects producers for the next span by converting power to slots
// spanEligibleVals - all validators eligible for next span
func SelectNextProducers(blkHash common.Hash, spanEligibleVals []hmTypes.Validator, producerCount uint64) (selectedIDs []uint64, err error) {
	if len(spanEligibleVals) <= int(producerCount) {
		for _, val := range spanEligibleVals {
			selectedIDs = append(selectedIDs, uint64(val.ID))
		}
		return
	}

	// extract seed from hash
	seed := helper.ToBytes32(blkHash.Bytes()[:32])
	validatorIndices := convertToSlots(spanEligibleVals)
	selectedIDs, err = ShuffleList(validatorIndices, seed)
	if err != nil {
		return
	}
	return selectedIDs[:producerCount], nil
}

// converts validator power to slots
func convertToSlots(vals []hmTypes.Validator) (validatorIndices []uint64) {
	for _, val := range vals {
		for val.VotingPower >= types.SlotCost {
			validatorIndices = append(validatorIndices, uint64(val.ID))
			val.VotingPower = val.VotingPower - types.SlotCost
		}
	}
	return validatorIndices
}
```

### Commit span Tx

Type: **Bor transaction**

There are two way to commit span in Bor.

1. **Automatic span change**

    At the end of the current span, at last block of the last sprint, Bor queries the next span from Heimdall and set validators and producers for the next span using a system call.

    ```jsx
    function commitSpan(
        bytes newSpan,
        address proposer,
        uint256 startBlock,
        uint256 endBlock,
        bytes validatorBytes,
        bytes producerBytes
     ) public onlySystem;
    ```

    Bor uses new producers as block producers for their next blocks.

2. **Force commit**

    Once the `span` proposed on Heimdall, the validator can force push span if span needs to be changed before the current span ends. A transaction to propose a `span` must be committed to Bor by any validator. Bor then updates and commits the proposed span at end of the current sprint using a system call.


## State Management (State-sync)

State management sends the state from the Ethereum chain to Bor chain. It is called `state-sync`. This is a way to move data from the Ethereum chain to Bor chain.

<img src={useBaseUrl("img/Bor/state-managment.svg")} />

### State sender

Source: [https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/root/stateSyncer/StateSender.sol)

To sync state sync, call following method **state sender contract** on Ethereum chain. The `state-sync` mechanism is basically a way to move state data from the Ethereum chain to Bor.

A user, who wants to move `data` from contract on Ethereum chain to Bor chain, calls `syncSate` method on `StateSender.sol`

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

Once `StateSynced` event emitted on `stateSender` contract on the Ethereum chain, any validator sends `MsgEventRecord` transaction on Heimdall.

After confirmation of a tx on Heimdall, a validator proposes `proposeState` on Bor with the simple transaction and at end of the sprint, Bor commits and finalizes `state-sync` by calling `commitState` using a `system` call.

During `commitState`, Bor executes `onStateReceive`, with `stateId` and `data` as args, on target contract.

### State Receiver Interface

`receiver` contract on Bor chain must implement following interface.

```jsx
// IStateReceiver represents interface to receive state
interface IStateReceiver {
  function onStateReceive(uint256 stateId, bytes calldata data) external;
}
```

Only `0x0000000000000000000000000000000000001001` — `StateReceiver.sol`, must be allowed to call `onStateReceive` function on target contract.

## Transaction Speed

Bor currently works as expected with ~2 to 4 seconds' block time with 100 validators and 4 block producers. After multiple stress testing with huge number of transactions, exact block time will be decided.

Using sprint-based architecture helps Bor to create faster bulk blocks without changing the producer during the current sprint. Having delay between two sprints gives other producers to receive a broadcasted block, often called as `producerDelay`

Note that time between two sprints is higher than normal blocks to buffer to reduce the latency issues between multiple producers.

## Attacks

### Censorship

Bor uses a very small set of producers to create faster blocks. It means it is prone to more censorship attacks than Heimdall. In order to deal with that, multiple testing will be done to find out the max number of producers for acceptable block time in the system.

Apart from that there are few attacks possible:

1. One producer is censoring the transaction

    In that case, the transaction sender can wait for the next producer's sprint and try to send the transaction again.

2. All validators are colluding with each-other and censoring particular transaction

    In this case, Polygon system will provide a way to submit a transaction on Ethereum chain and ask validators to include the transaction in next `x` checkpoints. If validators fail to include it during that time window, the user can slash the validators. Note that this is not currently implemented.

### Fraud

Producers can include invalid transaction during their turn. It can be possible at multiple levels:

1. One producer is fraudulent

    If a producer includes invalid transaction at any height, other producers can create a fork and exclude that transaction since their valid node ignores invalid blocks

2. Span producers are fraudulent

    If other producers don't create a fork, other validators who are validating the block can forcefully change the span by creating their own fork. This is not currently implemented since it requires how Geth works internally. However, this is in our future roadmap.

3. All validators are fraudulent

    Assumption is that ⅔+1 validators must be honest to work this system correctly.
