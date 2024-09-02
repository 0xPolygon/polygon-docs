---
comments: true
---

!!! warning "Work in progress!"

    This doc is currently undergoing revision, and the instructions provided may not be up to date. Stay tuned for updates!

Polygon validators continuously monitor a contract on Ethereum chain called `StateSender`. Each time a registered contract on Ethereum chain calls this contract, it emits an event. Using this event Polygon validators relay the data to another contract on Polygon chain. This *state sync* mechanism is used to send data from Ethereum to Polygon.

Additionally, Polygon validators send the transaction hash, namely *checkpoint*, of each transaction on the PoS chain to Ethereum on a regular basis. You can use this to validate any transaction that took place on Polygon. Once a transaction has been verified to have occurred on the PoS chain, the corresponding action can then be executed on Ethereum.

These two mechanisms can be used together to enable two-way data (state) transfer between Ethereum and Polygon. To abstract out all these interactions, you can directly inherit our `FxBaseRootTunnel` (on Ethereum) and `FxBaseChildTunnel` (on Polygon) contracts.

## Root tunnel contract

Use the `FxBaseRootTunnel` contract from [here](https://github.com/jdkanani/fx-portal/blob/main/contracts/tunnel/FxBaseRootTunnel.sol). This contract gives access to the following functions:

- `function _processMessageFromChild(bytes memory data)`: This is a virtual function that needs to be implemented in the contract which inherits it to handle data being sent from `ChildTunnel`.
- `_sendMessageToChild(bytes memory message)`: This function can be called internally with any bytes data as a message. This data will be sent as it is to the child tunnel.
- `receiveMessage(bytes memory inputData)`: This function needs to be called to receive the message emitted by `ChildTunnel`. The proof of transaction needs to be provided as calldata. An example script to generate proof using the *matic.js* SDK is included below.

## Child tunnel contract

Use the `FxBaseChildTunnel` contract from [here](https://github.com/jdkanani/fx-portal/blob/main/contracts/tunnel/FxBaseChildTunnel.sol). This contract gives access to following functions:

- `function _processMessageFromRoot(uint256 stateId, address sender, bytes memory data)`: This is a virtual function that needs to implement the logic to handle messages sent from the `RootTunnel`.
- `function _sendMessageToRoot(bytes memory message)`: This function can be called internally to send any bytes message to the root tunnel.

## Prerequisites

You need to inherit `FxBaseRootTunnel` contract in your root contract on Ethereum. As an example, you can follow this [contract](https://github.com/jdkanani/fx-portal/blob/main/contracts/examples/state-transfer/FxStateRootTunnel.sol) . Similarly, inherit `FxBaseChildTunnel` contract in your child on Polygon. Follow this [contract](https://github.com/jdkanani/fx-portal/blob/main/contracts/examples/state-transfer/FxStateChildTunnel.sol) as an example.

- While deploying your root contract on
    - *Sepolia testnet*, pass the address of `_checkpointManager` as `0xbd07D7E1E93c8d4b2a261327F3C28a8EA7167209` and `_fxRoot` as `0x0E13EBEdDb8cf9f5987512d5E081FdC2F5b0991e`.
    - *Ethereum mainnet*, `_checkpointManager` is `0x86e4dc95c7fbdbf52e33d563bbdb00823894c287` and `_fxRoot` is `0xfe5e5D361b2ad62c541bAb87C45a0B9B018389a2`.
- For deploying the child contract on 
    - *Amoy testnet*, pass `0xE5930336866d0388f0f745A2d9207C7781047C0f` as `_fxChild` in constructor.
    - *Polygon mainnet*, `_fxChild` will be `0x8397259c983751DAf40400790063935a11afa28a`.
- Call `setFxChildTunnel` on deployed root tunnel with the address of child tunnel. Example: [0x97482d379e397329ac1ee2a34eeb9aceb06bd4a91ec17c7d7d3da4a1e96c165c](https://sepolia.etherscan.io/tx/0x97482d379e397329ac1ee2a34eeb9aceb06bd4a91ec17c7d7d3da4a1e96c165c)
- Call `setFxRootTunnel` on deployed child tunnel with address of root tunnel. Example: [0xae30445301bd7c902bf373fb890faf5658bd3a9437131c9408d5ecbc41af3fc0](https://amoy.polygonscan.com/tx/0xae30445301bd7c902bf373fb890faf5658bd3a9437131c9408d5ecbc41af3fc0)

## State tunnel sample contracts

- Contracts: [Fx-Portal Github Repository](https://github.com/jdkanani/fx-portal/tree/main/contracts/tunnel)
- Sepolia: [0x1707157b9221204869ED67705e42fB65e026586c](https://sepolia.etherscan.io/address/0x1707157b9221204869ED67705e42fB65e026586c)
- Amoy: [0xf5D2463d0176462d797Afcd57eC477b7B0CcBE70](https://amoy.polygonscan.com/address/0xf5D2463d0176462d797Afcd57eC477b7B0CcBE70)

## State transfer from Ethereum to Polygon

- You need to call `_sendMessageToChild()` internally in your root contract and pass the data as an argument to be sent to Polygon. Example: [0x00a1aa71593fec825b4b1ce1081b5a9848612fb21f9e56def2914b483f5f34f5](https://sepolia.etherscan.io/tx/0x00a1aa71593fec825b4b1ce1081b5a9848612fb21f9e56def2914b483f5f34f5)
- In your child contract, implement `_processMessageFromRoot()` virtual function in `FxBaseChildTunnel` to retrieve data from Ethereum. The data will be received automatically from the state receiver when the state is synced.

## State transfer from Polygon to Ethereum

1. Call `_sendMessageToRoot()` internally in your child contract with data as a parameter to be sent to Ethereum. Note down the transaction hash as it will be used to generate the proof after the transaction has been included as a checkpoint.

2. Proof Generation to complete the exit on root chain: Generate the proof using the tx hash and `MESSAGE_SENT_EVENT_SIG`. To generate the proof, you can either use the proof generation API hosted by Polygon, or you can also spin up your own proof generation API by following the instructions [here](https://github.com/maticnetwork/proof-generation-api).

  The proof generation endpoint hosted by Polygon is available here:
  
  - [Mainnet](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/{burnTxHash}?eventSignature={eventSignature})
  - [Testnet](https://proof-generator.polygon.technology/api/v1/amoy/exit-payload/{burnTxHash}?eventSignature={eventSignature})

Here, 

- `burnTxHash` is the transaction hash of the `_sendMessageToRoot()` transaction you initiated on Polygon.
- `eventSignature` is the event signature of the event emitted by the `_sendMessageToRoot()` function. The event signature for the `MESSAGE_SENT_EVENT_SIG` is `0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036`.

Here's an example of [how to use the proof generation API](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/0x70bb6dbee84bd4ef1cd1891c666733d0803d81ac762ff7fdc4726e4525c1e23b?eventSignature=0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036).

1. Implement `_processMessageFromChild()` in your root contract.
2. Use the generated proof as an input to `receiveMessage()` to retrieve data sent from child tunnel into your contract.
