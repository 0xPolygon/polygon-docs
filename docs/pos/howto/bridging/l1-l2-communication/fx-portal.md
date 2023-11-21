---
id: fx-portal
title: FxPortal Overview
sidebar_label: Overview
description: Transfer state or data from Ethereum to Polygon without mapping using FxPortal.
keywords:
  - docs
  - polygon wiki
  - polygon
  - FxPortal
  - ethereum to polygon
image: https://wiki.polygon.technology/img/polygon-logo.png
---

import useBaseUrl from '@docusaurus/useBaseUrl';

The usual mechanism to natively read Ethereum data from Polygon is using **State Sync**. This enables the transfer of arbitrary data from Ethereum to Polygon. However, this approach also requires mapping of the root and child contracts if the default interface cannot be used. FxPortal offers an alternative where ERC standardized tokens can be deployed without any mapping involved, simply using the deployed base FxPortal contracts.

## What is FxPortal?

It is a powerful yet simple implementation of the Polygon [state sync](/pos/design/validator/core-components/state-sync-mechanism.md) mechanism. The Polygon PoS bridge is built on the same architecture. The code in the [examples](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples) folder are some examples of usage. You can easily use these examples to build your own implementations or own custom bridge which allows any state-sync without mapping.

You can check out the [GitHub's repository folder](https://github.com/0xPolygon/fx-portal/tree/main/contracts) for contracts and examples.

## How does it work?

[FxChild](https://github.com/0xPolygon/fx-portal/blob/main/contracts/FxChild.sol) and [FxRoot](https://github.com/0xPolygon/fx-portal/blob/main/contracts/FxRoot.sol) are the main contracts on which FxPortal works. It calls and passes data to user-defined methods on the other chain without any mapping using the state sync mechanism. To use the deployed main contracts, you can implement FxPortal's base contracts in the smart contracts you deploy - [FxBaseRootTunnel](https://github.com/0xPolygon/fx-portal/blob/main/contracts/tunnel/FxBaseRootTunnel.sol) and [FxBaseChildTunnel](https://github.com/0xPolygon/fx-portal/blob/main/contracts/tunnel/FxBaseChildTunnel.sol). By building on these contracts, your deployed contracts will be able to communicate with each other using the data tunnel mechanism.

Otherwise, you can choose to map your tokens with the already deployed tunnel contracts. Default FxTunnel deployment details for Polygon Mainnet and Mumbai Testnet are as follows:

- [Polygon Mainnet](https://static.polygon.technology/network/mainnet/v1/index.json)
- [Mumbai Testnet](https://static.polygon.technology/network/testnet/mumbai/index.json)

Look for the keyword `FxPortalContracts` in the above links to find all the default tunnel contracts and other important FxPortal contract deployments.

## Do I need a Custom FxTunnel Implementation ?

You must go for a **custom FxTunnel implementation** only if the default tunnel implementations do not align with your use case. When you use the default FxPortal tunnels, you can not modify the child contract code. The bytecode for the child token contract is always fixed and always remains the same for the [default FxTunnel deployments](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples). In case you need a custom child token, you must go for your own custom FxTunnel, and reading the next part will guide you more in deploying your own custom FxTunnels.

It is highly recommended to read and understand [FxPortal State Transfer](state-transfer.md) before you read the upcoming section. Each of these upcoming sections will have example tunnel contract links attached to it. These examples can be taken as a reference while building your own custom fx-tunnels.

## ERC20 Transfer

The [child and root tunnel contracts](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/erc20-transfer) enable the deposit of tokens on the root chain and withdrawal on the child chain.

#### `FxERC20RootTunnel`

- `mapToken(address rootToken)`: You can call the function on the deployed contract to map your ERC20 token and create a corresponding child token on the child chain.
- `deposit(address rootToken, address user, uint256 amount, bytes memory data)`: call `deposit()` method with the address of the mapped token, the address that can withdraw with a corresponding amount (along with data if needed). You must have approved the contract using the standard ERC20 `approve` function to spend your tokens first.

#### `FxERC20ChildTunnel`

- `withdraw(address childToken, uint256 amount)`: The address assigned in `deposit()` can withdraw all the amount of child token using this function. They will receive the child token created when first mapped.
- `rootToChildToken`: This public variable contains the root token to child token mapping. You can query the mapping with the address of the root token to know the address of the deployed child token.

### From Ethereum &rarr; Polygon

1. Deploy your own ERC20 token on the root chain. You will need this address later.
2. Approve the tokens for transfer by calling the `approve()` function of the root token with the address of the root tunnel and the amount as the arguments.
3. Proceed to call `deposit()` with the address of the receiver and amount on the root chain to receive the equivalent child token on the child chain. This will also map the token automatically. Alternatively, you can call `mapToken()` first before depositing.
4. After mapping, you should now be able to execute cross-chain transfers using the `deposit` and `withdraw` functions of the tunnel.

:::note

After you have performed `deposit()` on the root chain, it will take 22-30 minutes for state sync to happen. Once state sync happens, you will get the tokens deposited at the given address.

:::

### From Polygon &rarr; Ethereum

1. Proceed to call `withdraw()` with the respective token address and amount as arguments on the child contract to move the child tokens back to the designated receiver on the root chain. **Note the tx hash** as this will be used to generate the burn proof.

2. You can find the steps to complete the withdrawal [here](#withdraw-tokens-on-the-root-chain).

## ERC721 Transfer

In case you need an example, please check out this [ERC721 Root and Child Tunnels](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/erc721-transfer) guide.

### From Ethereum &rarr; Polygon

1. Deploy your own ERC721 token on the root chain. You will need this address later.
2. Approve the tokens for transfer by calling the `approve()` function of the root token with the address of the root tunnel and the token ID as the arguments.
3. Proceed to call `deposit()` with the address of the receiver and token ID on the root chain to receive the equivalent child token on the child chain. This will also map the token automatically. Alternatively, you can call `mapToken()` first before depositing.

:::note

After you have performed `deposit()` on the root chain, it will take 22-30 minutes for state sync to happen. Once state sync happens, you will get the tokens deposited at the given address.

:::

### From Polygon &rarr; Ethereum

1. Proceed to call `withdraw()` with the respective token address and token id as arguments on the child contract to move the child tokens back to the designated receiver on the root chain. **Note the tx hash** will be used to generate the burn proof.

2. You can find the steps to complete the withdrawal [here](#withdraw-tokens-on-the-root-chain).

## ERC1155 Transfer

In case you need an example, please check out this [ERC1155 Root and Child Tunnels](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/erc1155-transfer) guide.

#### `FxERC1155RootTunnel`

- `mapToken(rootToken)`: Used to map your root ERC1155 token to child chain
- `deposit(rootToken, user, id, amount, data)`: Function used to deposit root tokens to child chain
- `depositBatch(rootToken, user,  ids, amounts, bytes memory data)`: Used for multiple token ids and corresponding amounts
- `receiveMessage(inputData)`: To be called after burn proof has been generated with the payload as `inputData`

#### `FxERC1155ChildTunnel`

- `withdraw(childToken, id, amount, data)`: Used to withdraw token from Polygon to Ethereum
- `withdrawBatch(childToken, ids, amounts, data)`: Same as withdraw but for withdrawing multiple token ids

### From Ethereum &rarr; Polygon

1. Deploy your ERC1155 token on the root chain. You will need this address later.
2. Call `setApprovalForAll(operator, approved)` on the deployed token with `FxERC1155RootTunnel` address as `operator` to allow `FxERC1155RootTunnel` to transfer your tokens to `FxERC1155ChildTunnel` on Polygon.
3. Call `mapToken()` on `FxERC1155RootTunnel` with your deployed token's address as `rootToken`. This will send a message to `FxERC1155ChildTunnel` instructing it to deploy and map the ERC1155 token on Polygon. To query your child token address, call `rootToChildToken` on `FxERC1155ChildTunnel`.
4. Call `deposit()` on `FxERC1155RootTunnel` with the address of the token on Ethereum as `rootToken`, receiver as `user`, token id as `id` and the amount as `amount`. Alternatively, you can also call `depositBatch()` for multiple token ids.

:::note

After you have performed `deposit()` on the root chain, it will take 22-30 minutes for state sync to happen. Once state sync happens, you will get the tokens deposited at the given address.

:::

### From Polygon &rarr; Ethereum

1. Call `withdraw()` on `FxERC1155ChildTunnel` with the address of the child token deployed on Polygon as the `childToken` and the token id as `id` (the child token address can be queried from `rootToChildToken` mapping). Alternatively, you can also call `withdrawBatch()` for multiple token ids and corresponding amounts. **Note the tx hash** will be used to generate the burn proof.

2. You can find the steps to complete the withdrawal [here](#withdraw-tokens-on-the-root-chain).

## Withdraw Tokens on the Root Chain

:::info

After you have performed `withdraw()` on the child chain, it will take 30-90 minutes for a checkpoint to happen. Once the next checkpoint includes the burn transaction, you can withdraw the tokens on the root chain.

:::

1. Generate the burn proof using the **tx hash** and **MESSAGE_SENT_EVENT_SIG**. To generate the proof, you can either use the proof generation API hosted by Polygon or you can also spin up your own proof generation API by following the instructions [here](https://github.com/maticnetwork/proof-generation-api).

  The proof generation endpoint hosted by Polygon is available [here](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/{burnTxHash}?eventSignature={eventSignature}).

  - `burnTxHash` is the transaction hash of the `withdraw()` transaction you initiated on Polygon.
  - `eventSignature` is the event signature of the event emitted by the `withdraw()` function. The event signature for the MESSAGE_SENT_EVENT_SIG is `0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036`.

  The proof generation API usage examples for the Mainnet and Testnet are as follows:-

  &rarr; [Polygon Mainnet Proof generation](https://proof-generator.polygon.technology/api/v1/matic/exit-payload/0x70bb6dbee84bd4ef1cd1891c666733d0803d81ac762ff7fdc4726e4525c1e23b?eventSignature=0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036)

  &rarr; [Mumbai Testnet Proof generation](https://proof-generator.polygon.technology/api/v1/mumbai/exit-payload/0x4756b76a9611cffee3d2eb645819e988c34615621ea256f818ab788d81e1f838?eventSignature=0x8c5261668696ce22758910d05bab8f186d6eb247ceac2af2e82c7dc17669b036)

2. Feed the generated payload as the argument to `receiveMessage()` in the respective root tunnel contract on Goerli or Ethereum.

## Mintable ERC-20 Transfer

In case you need an example, please check out these [Mintable ERC20 Root and Child Tunnels](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/mintable-erc20-transfer) examples.

:::info

In the case of Mintable Token FxTunnels, the child token gets deployed first and the root token is deployed only when the first withdraw/exit process is completed. The root token contract address can be pre-determined right after the child contract is deployed, but the mapping will technically exist only when the first withdrawal/exit is completed.

:::

#### `FxMintableERC20RootTunnel`

- `deposit(address rootToken, address user, uint256 amount, bytes memory data)`: To deposit tokens from Ethereum to Polygon
- `receiveMessage(bytes memory inputData)`: Burn proof to be fed as the `inputData` to receive tokens on the root chain

#### `FxMintableERC20ChildTunnel`

- `deployChildToken(uint256 uniqueId, string memory name, string memory symbol, uint8 decimals)`: To deploy an ERC20 token on the Polygon network
- `mintToken(address childToken, uint256 amount)`: Mint a particular amount of tokens on Polygon
- `withdraw(address childToken, uint256 amount)`: To burn tokens on the child chain in order to withdraw on the root chain

### Minting Tokens on Polygon

1. Call the `deployChildToken()` on `FxMintableERC20ChildTunnel` and pass the necessary token info as parameters. This emits a `TokenMapped` event which contains the `rootToken` and `childToken` addresses. Note these addresses.
2. Call `mintToken()` on `FxMintableERC20ChildTunnel` to mint tokens on the child chain.
3. Call `withdraw()` on `FxMintableERC20ChildTunnel` to withdraw tokens from Polygon. Note the transaction hash as this will come in handy to generate the burn proof.
4. You can find the steps to complete the withdrawal [here](#withdraw-tokens-on-the-root-chain).

### Withdrawing Tokens on Ethereum

Feed the generated burn proof as the argument to `receiveMessage()` in `FxMintableERC20RootTunnel`. After this, the token balance would be reflected on the root chain.

### Deposit Tokens back to Polygon

1. Make sure you approve `FxMintableERC20RootTunnel` to transfer your tokens.
2. Call `deposit()` in `FxMintableERC20RootTunnel` with the `rootToken` as address of root token and `user` as the recipient.
3. Wait for the state sync event (22-30 mins). After this, you can query the target recipient's balance on the child chain.

The **ERC721** and **ERC1155** Mintable FxTunnel examples are as follows :-

- [FxMintableERC721Tunnels](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/mintable-erc721-transfer)
- [FxMintableERC1155Tunnels](https://github.com/0xPolygon/fx-portal/tree/main/contracts/examples/mintable-erc1155-transfer)

## Example Deployments

### Goerli

- Checkpoint Manager: [0x2890bA17EfE978480615e330ecB65333b880928e](https://goerli.etherscan.io/address/0x2890bA17EfE978480615e330ecB65333b880928e)
- Dummy ERC20 token: [0xe9c7873f81c815d64c71c2233462cb175e4765b3](https://goerli.etherscan.io/address/0xe9c7873f81c815d64c71c2233462cb175e4765b3)
- FxERC20RootTunnel: [0x3658ccFDE5e9629b0805EB06AaCFc42416850961](https://goerli.etherscan.io/address/0x3658ccFDE5e9629b0805EB06AaCFc42416850961)
- FxMintableERC20RootTunnel: [0xA200766a7D64E54611E2D232AA6c1f870aCb63c1](https://goerli.etherscan.io/address/0xA200766a7D64E54611E2D232AA6c1f870aCb63c1)
- Dummy ERC721 token: [0x73594a053cb5ddDE5558268d28a774375C4E23dA](https://goerli.etherscan.io/address/0x73594a053cb5ddDE5558268d28a774375C4E23dA)
- FxERC721RootTunnel: [0xF9bc4a80464E48369303196645e876c8C7D972de](https://goerli.etherscan.io/address/0xF9bc4a80464E48369303196645e876c8C7D972de)
- Dummy ERC1155 Token: [0x1906d395752FE0c930f8d061DFEb785eBE6f0B4E](https://goerli.etherscan.io/address/0x1906d395752FE0c930f8d061DFEb785eBE6f0B4E)
- FxERC1155RootTunnel : [0x48DE785970ca6eD289315036B6d187888cF9Df48](https://goerli.etherscan.io/address/0x48DE785970ca6eD289315036B6d187888cF9Df48)

### Mumbai

- FxERC20: [0xDDE69724AeFBdb084413719fE745aB66e3b055C7](https://mumbai.polygonscan.com/address/0xDDE69724AeFBdb084413719fE745aB66e3b055C7)
- FxERC20ChildTunnel: [0x9C37aEbdb7Dd337E0215BC40152d6689DaF9c767](https://mumbai.polygonscan.com/address/0x9C37aEbdb7Dd337E0215BC40152d6689DaF9c767)
- FxMintableERC20ChildTunnel: [0xA2C7eBEf68B444056b4A39C2CEC23844275C56e9](https://mumbai.polygonscan.com/address/0xA2C7eBEf68B444056b4A39C2CEC23844275C56e9)
- Child token dummy ERC20: 0x346d21bc2bD3dEE2d1168E1A632b10D1d7B9c0A
- FxERC721: [0xf2720927E048726267C0221ffA41A88528048726](https://mumbai.polygonscan.com/address/0xf2720927E048726267C0221ffA41A88528048726)
- FxERC721ChildTunnel: [0x3658ccFDE5e9629b0805EB06AaCFc42416850961](https://mumbai.polygonscan.com/address/0x3658ccFDE5e9629b0805EB06AaCFc42416850961)
- FxERC1155: [0x80be8Cf927047A40d3f5791BF7436D8c95b3Ae5C](https://mumbai.polygonscan.com/address/0x80be8Cf927047A40d3f5791BF7436D8c95b3Ae5C)
- FxERC1155ChildTunnel: [0x3A0f90D3905601501652fe925e96d8B294243Efc](https://mumbai.polygonscan.com/address/0x3A0f90D3905601501652fe925e96d8B294243Efc)

The corresponding Mainnet deployments can be found [here](https://static.polygon.technology/network/mainnet/v1/index.json). Look for the keyword `FxPortalContracts` to find all the default tunnel contracts and other important FxPortal contract deployments. You can make use of the [`maticnetwork/meta`](https://www.npmjs.com/package/@maticnetwork/meta) package to access the contract addresses and ABIs.

## Contract Addresses

### Mumbai Testnet

| Contract | Deployed address  |
| :----- | :- |
| [FxRoot (Goerli)](https://goerli.etherscan.io/address/0x3d1d3E34f7fB6D26245E6640E1c50710eFFf15bA#code) | `0x3d1d3E34f7fB6D26245E6640E1c50710eFFf15bA` |
| [FxChild (Mumbai)](https://mumbai.polygonscan.com/address/0xCf73231F28B7331BBe3124B907840A94851f9f11/contracts) | `0xCf73231F28B7331BBe3124B907840A94851f9f11`|

### Polygon Mainnet


| Contract | Deployed address  |
| :----- | :- |
| [FxRoot (Ethereum Mainnet)](https://etherscan.io/address/0xfe5e5d361b2ad62c541bab87c45a0b9b018389a2#code) | `0xfe5e5D361b2ad62c541bAb87C45a0B9B018389a2` |
| [FxChild (Polygon Mainnnet)](https://polygonscan.com/address/0x8397259c983751DAf40400790063935a11afa28a/contracts) | `0x8397259c983751DAf40400790063935a11afa28a`|
