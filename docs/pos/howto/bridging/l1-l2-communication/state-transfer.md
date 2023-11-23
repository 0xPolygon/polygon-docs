Polygon validators continuously monitor a contract on Ethereum chain called `StateSender`. Each time a registered contract on Ethereum chain calls this contract, it emits an event. Using this event Polygon validators relay the data to another contract on Polygon chain. This **State Sync** mechanism is used to send data from Ethereum to Polygon.

Additionally, Polygon validators send an Ethereum hash of each transaction on the Polygon chain on a regular basis. You can use this **checkpoint** to validate any transaction that took place on Polygon. Once a transaction has been verified to have occurred on the Polygon chain, Ethereum can then be used to carry out the appropriate action.

These 2 mechanisms can be used together to enable two-way data (state) transfer between Ethereum and Polygon. To abstract out all these interactions, you can directly inherit our `FxBaseRootTunnel` (on Ethereum) and `FxBaseChildTunnel` (on Polygon) contracts.

## Root Tunnel Contract

Use the `FxBaseRootTunnel` contract from [here](https://github.com/jdkanani/fx-portal/blob/main/contracts/tunnel/FxBaseRootTunnel.sol). This contract gives access to the following functions:

- `function _processMessageFromChild(bytes memory data)`: This is a virtual function that needs to be implemented in the contract which inherits it to handle data being sent from `ChildTunnel`.
- `_sendMessageToChild(bytes memory message)`: This function can be called internally with any bytes data as a message. This data will be sent as it is to the child tunnel.
- `receiveMessage(bytes memory inputData)`: This function needs to be called to receive the message emitted by `ChildTunnel`. The proof of transaction needs to be provided as calldata. An example script to generate proof using **matic.js** is included below.

## Child Tunnel Contract

Use the `FxBaseChildTunnel` contract from [here](https://github.com/jdkanani/fx-portal/blob/main/contracts/tunnel/FxBaseChildTunnel.sol). This contract gives access to following functions:

- `function _processMessageFromRoot(uint256 stateId, address sender, bytes memory data)`: This is a virtual function that needs to implement the logic to handle messages sent from the `RootTunnel`.
- `function _sendMessageToRoot(bytes memory message)`: This function can be called internally to send any bytes message to the root tunnel.

## Prerequisites

- You need to inherit `FxBaseRootTunnel` contract in your root contract on Ethereum. As an example, you can follow this [contract](https://github.com/jdkanani/fx-portal/blob/main/contracts/examples/state-transfer/FxStateRootTunnel.sol) . Similarly, inherit `FxBaseChildTunnel` contract in your child on Polygon. Follow this [contract](https://github.com/jdkanani/fx-portal/blob/main/contracts/examples/state-transfer/FxStateChildTunnel.sol) as an example.
- While deploying your root contract on
  - **Goerli Testnet**, pass the address of `_checkpointManager` as **0x2890bA17EfE978480615e330ecB65333b880928e** and `_fxRoot` as **0x3d1d3E34f7fB6D26245E6640E1c50710eFFf15bA**.

  - **Ethereum Mainnet**, `_checkpointManager` is **0x86e4dc95c7fbdbf52e33d563bbdb00823894c287** and `_fxRoot` is **0xfe5e5D361b2ad62c541bAb87C45a0B9B018389a2**.
- For deploying the child contract on **Mumbai testnet**, pass **0xCf73231F28B7331BBe3124B907840A94851f9f11** as `_fxChild` in constructor. For **Polygon mainnet,** `_fxChild` will be **0x8397259c983751DAf40400790063935a11afa28a**.
- Call `setFxChildTunnel` on deployed root tunnel with the address of child tunnel. Example: [0x79cd30ace561a226258918b56ce098a08ce0c70707a80bba91197f127a48b5c2](https://goerli.etherscan.io/tx/0x79cd30ace561a226258918b56ce098a08ce0c70707a80bba91197f127a48b5c2)
- Call `setFxRootTunnel` on deployed child tunnel with address of root tunnel. Example: [0xffd0cda35a8c3fd6d8c1c04cd79a27b7e5e00cfc2ffc4b864d2b45a8bb7e98b8](https://mumbai.polygonscan.com/tx/0xffd0cda35a8c3fd6d8c1c04cd79a27b7e5e00cfc2ffc4b864d2b45a8bb7e98b8/internal-transactions)

## Example Contracts of State Transfer Bridge

- **Contracts**: [Fx-Portal Github Repository](https://github.com/jdkanani/fx-portal/tree/main/contracts/tunnel)
- **Goerli:** [0xc4432e7dab6c1b43f4dc38ad2a594ca448aec9af](https://goerli.etherscan.io/address/0xc4432e7dab6c1b43f4dc38ad2a594ca448aec9af)
- **Mumbai:** [0xa0060Cc969d760c3FA85844676fB654Bba693C22](https://mumbai.polygonscan.com/address/0xa0060Cc969d760c3FA85844676fB654Bba693C22/transactions)

## State Transfer from Ethereum &rarr; Polygon

- You need to call `_sendMessageToChild()` internally in your root contract and pass the data as an argument to be sent to Polygon. Example: [0x28705fcae757a0c88694bd167cb94a2696a0bc9a645eb4ae20cff960537644c1](https://goerli.etherscan.io/tx/0x28705fcae757a0c88694bd167cb94a2696a0bc9a645eb4ae20cff960537644c1)
- In your child contract, implement `_processMessageFromRoot()` virtual function in `FxBaseChildTunnel` to retrieve data from Ethereum. The data will be received automatically from the state receiver when the state is synced.

## State Transfer from Polygon &rarr; Ethereum

1. Call `_sendMessageToRoot()` internally in your child contract with data as a parameter to be sent to Ethereum. Example: [0x3cc9f7e675bb4f6af87ee99947bf24c38cbffa0b933d8c981644a2f2b550e66a](https://mumbai.polygonscan.com/tx/0x3cc9f7e675bb4f6af87ee99947bf24c38cbffa0b933d8c981644a2f2b550e66a/logs)

  Note the transaction hash as it will be used to generate proof after it has been included as a checkpoint.

2. **Proof Generation to complete the exit on root chain**: Generate the proof using the **tx hash** and **MESSAGE_SENT_EVENT_SIG**. To generate the proof, you can either use the proof generation API hosted by Polygon or you can also spin up your own proof generation API by following the instructions [here](https://github.com/maticnetwork/proof-generation-api).

  The proof generation endpoint hosted by Polygon is available [here](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/{burnTxHash}?eventSignature={eventSignature}).

    - `burnTxHash` is the transaction hash of the `_sendMessageToRoot()` transaction you initiated on Polygon.
    - `eventSignature` is the event signature of the event emitted by the `_sendMessageToRoot()` function. The event signature for the MESSAGE_SENT_EVENT_SIG is `0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036`.

  The proof generation API usage examples for the Mainnet and Testnet are as follows:-

  &rarr; [Mumbai Testnet Proof generation](https://proof-generator.polygon.technology/api/v1/mumbai/exit-payload/0x4756b76a9611cffee3d2eb645819e988c34615621ea256f818ab788d81e1f838?eventSignature=0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036)

  &rarr; [Polygon Mainnet Proof generation](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/0x70bb6dbee84bd4ef1cd1891c666733d0803d81ac762ff7fdc4726e4525c1e23b?eventSignature=0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036)

3. Implement `_processMessageFromChild()` in your root contract.

4. Use the generated proof as an input to `receiveMessage()` to retrieve data sent from child tunnel into your contract. Example: [0x436dcd500659bea715a09d9257295ddc21290769daeea7f0b666166ef75e3515](https://goerli.etherscan.io/tx/0x436dcd500659bea715a09d9257295ddc21290769daeea7f0b666166ef75e3515) )
