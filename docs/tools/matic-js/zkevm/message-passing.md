<!--
---
comments: true
---
-->

This document demonstrates inter-layer message passing using the messaging layer of the Polygon bridge. As an example, we go over how to customize wrapped tokens using adapter contracts, and how to use Matic.js to bridge assets from Ethereum to Polygon zkEVM and vice versa.

!!! info "Terminology"

    Within the scope of this doc, we refer to Ethereum as the _root_ chain and zkEVM as the _child_ chain.

The existing zkEVM bridge uses the ERC20 standard contract for creating wrapped tokens depending on the token's native network.

Often, organizations want to customize their wrapped tokens by extending some functionalities. 

These functionalities could include: blacklisting, putting a cap on minting, or any sound auxiliary functionality.

This can be done by deploying **adapter contracts** that use the messaging layer of the bridge.

## Adapter contracts

An adapter is a wrapper contract that implements the [Polygon bridge library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol). An example implementation for ERC20 can be found [here](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/lib/PolygonERC20BridgeLib.sol).

Ideally, the following adapter contracts are expected,

1. `OriginChainBridgeAdapter`
2. `WrapperChainBridgeAdapter`

Irrespective of whether an ERC20 token is Ethereum native (root chain) or zkEVM native (child chain), an adapter contract should have the following functions: (these are already part of the [library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol)).

```solidity
function bridgeToken(
        address destinationAddress,
        uint256 amount,
        bool forceUpdateGlobalExitRoot
    ) external {}
    
function onMessageReceived(
				address originAddress,
				uint32 originNetwork,
				bytes memory data
) external payable {}
```

For the sake of maintaining consistency among wrapped tokens in terms of the bridging mechanism, there are certain standard functions and variables that need to be included in the adapter contracts.

## Standardizations

1. Adapter contracts need to implement the [Polygon bridge library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol) and expose `bridgeToken()` and `onMessageReceived()` functions.
2. There should be two separate adapter contracts; `OriginChainBridgeAdapter` and `WrapperChainBridgeAdapter`.
3. `bridgeToken` function should match the exact function signature and be similar to [this](https://github.com/maticnetwork/static/blob/master/network/mainnet/cherry/artifacts/zkevm/ZkEVMBridgeAdapter.json) ABI.

### Nice to have

Expose the following variables,

1. `originTokenAddress`: Address of the native token.
2. `originTokenNetwork`: `networkId` of the chain to which the token is native.
3. `wrappedTokenAddress`: Address of the wrapped token.

## Bridging mechanism

`PolygonZkEVMBridge` is the main bridge contract. It exposes a `bridgeMessage()` function, which users can call in order to bridge messages from L1 to L2, or vice versa. The `claimMessage()` function can be called on the receiving chain to claim the sent message.

For example, a user who wants to bridge a message from Ethereum to zkEVM, can call `bridgeMessage()` on Ethereum and then call `claimMessage()` on zkEVM. Once the `claimMessage()` function is called, the bridge calls `onMessageReceived` for the specified destination address.

Adapter contracts are basically abstractions that use `bridgeMessage()` to bridge and `onMessageReceived()` to process a `claimMessage()` on respective chains.

![Figure: Adapter contract](../../../img/learn/maticjs-adapter-contract-01.png)

## ERC20 transfer contract interaction 

The transfer of ERC20 tokens using each of the adapter contracts and the actions performed in the process are described below.

### OriginChainBridgeAdapter

When depositing an ERC20 token from Ethereum to zkEVM, the adapter contract calls the `bridgeToken()` function.

During withdrawal from zkEVM, the [PolygonZkEvmBridge.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMBridge.sol) contract calls the `onMessageReceived()` function when `claimMessage()` is invoked.

### WrapperChainBridgeAdapter

When withdrawing an ERC20 token from zkEVM to Ethereum, the adapter contract calls the `bridgeToken()` function.

During a deposit to zkEVM, the [PolygonZkEvmBridge.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMBridge.sol) contract calls the `onMessageReceived()` function when `claimMessage()` is invoked.

### From Ethereum → zkEVM

!!! warning

    It is assumed that the token being bridged is native to the root chain.

1. Deploy your adapter contracts on both the root chain and the child chain. (Note the address, you’ll need it later!)
2. Approve the tokens to be transferred by calling the `approve()` function (on the root token) with the address of the `originChainBridgeAdapter` and the token amount, as arguments.
3. Proceed to call `bridgeToken()` while using as arguments: the recipient, amount, and setting `forceUpdateGlobalExitRoot` to `true` on the `originChainBridgeAdapter` in the root chain (i.e., Ethereum).
4. Get the Merkle proof for this bridge transaction using the [proof API](https://proof-generator.polygon.technology/api/zkevm/testnet/merkle-proof?net_id=0&deposit_cnt=).
5. Proceed to call `claimMessage()` with the respective arguments on the `PolygonZkEVMBridge.sol` contract in the child chain (i.e., zkEVM).

The bridge will call the `onMessageReceived` function in the `WrapperChainBridgeAdapter` contract. Which should ideally have the logic to mint wrapped tokens to the recipient.

### From zkEVM → Ethereum

!!! warning

    It is assumed that the token being bridged is native to the root chain.

1. Deploy your adapter contracts on both the root chain and the child chain. (Note the address, you’ll need it later!)
2. Approve the tokens to be transferred by calling the `approve()` function (on the wrapped token) with the address of the `wrapperChainBridgeAdapter` and the token amount as arguments.
3. Proceed to call `bridgeToken()`, using as arguments: the recipient, amount, and setting `forceUpdateGlobalExitRoot` to `true` on the `WrapperChainBridgeAdapter` in the child chain (i.e., zkEVM). Ideally, this function should have the logic to burn the wrapped tokens.
4. Get the Merkle proof for this bridge transaction using the [proof API](https://proof-generator.polygon.technology/api/zkevm/testnet/merkle-proof?net_id=0&deposit_cnt=).
5. Proceed to call `claimMessage()` with the respective arguments on the `PolygonZkEVMBridge.sol` contract in the root chain (i.e., Ethereum).

The bridge will call the `onMessageReceived` function in the `OriginChainBridgeAdapter` contract. Which should Ideally have the logic to mint unwrapped tokens to the recipient.

## Listing tokens in Bridge UI

!!! tip

    Note that it is important to follow [standardizations](#standardizations) for easy listing.

1. Add your token to this [token list on GitHub](https://github.com/maticnetwork/polygon-token-list/blob/dev/src/tokens/zkevmPopularTokens.json).
    
    Example:

    ```solidity
    {
        "chainId": 1101,
        "name": "Token Name",
        "symbol": "Token Symbol",
        "decimals": 6, // token decimal
        "address": "ZkEVM Address of the token",
        "logoURI": "Token logo url",
        "tags": ["zkevm", "stablecoin", "erc20, custom-zkevm-bridge"],
        "originTokenNetwork": 0, // 0 here is networkId of ethereum,
        "wrappedTokenNetwork": 1, // 1 here is networkId of zkEvm,
        "extensions": {
            "rootAddress": "Ethereum Address of the Token",
            "wrapperChainBridgeAdapter": "",
            "originChainBridgeAdapter": "",
            }
    },
    ```

    !!! note "Setting the correct network ID"
        
        If the token is Ethereum native, then `originTokenNetwork` should be `0`. If the token is zkEVM native, then `originTokenNetwork` should be `1`. The same rule applies for the `wrappedTokenNetwork` field.

2. Raise a PR 🚀.

## Using Matic.js to bridge using adapter contracts

Deploy your `OriginChainBridgeAdapt` and `WrapperChainBridgeAdapter`. 

Make sure you are using `matic.js version > 3.6.4`.

- Create an instance of the zkEVM client, passing the necessary parameters. Refer [here](./initialize.md) for more info.
    
    ```jsx
    const client = new ZkEvmClient();
    *await* client.init({})
    ```

- Create an ERC20 token instance which you would like to bridge,
    
    ```jsx
    *const* erc20Token = client.erc20("<tokenAddress>", "<isRootChain>", "<bridgeAdapterAddress>");
    ```

### Bridge from Ethereum → zkEVM

1. **Deposit**
    
    ```jsx
    const depositTx = await erc20Token.depositCustomERC20("1000000000000000000", "recipent address",true);
    const txHash = await depositTx.getTransactionHash();
    console.log("Transaction Hash", txHash);
    ```

2. **Claim deposit**
    
    ```jsx
    const claimTx = await erc20.customERC20DepositClaim("<deposit tx hash>");
    const txHash = await claimTx.getTransactionHash();
    console.log("claimed txHash", ctxHash);
    ```

### Bridge from zkEVM → Ethereum

1. **Withdraw**
    
    ```jsx
    const depositTx = await erc20Token.withdrawCustomERC20("1000000000000000000", "recipent address",true);
    const txHash = await depositTx.getTransactionHash();
    console.log("Transaction Hash", txHash);
    ```

2. **Claim withdrawal**
    
    ```jsx
    const claimTx = await erc20.customERC20WithdrawExit("<withdraw tx hash>");
    const txHash = await claimTx.getTransactionHash();
    console.log("claimed txHash", ctxHash);
    ```


## Basic functions for error passing

Below we provide the two basic functions used for _error passing_ in each of the two directions: L1 --> L2 and L2 --> L1.

### Root to child (L1 → L2)

```jsx
const bridgeTx = zkEvmClient.rootChainBridge.bridgeMessage(
				destinationNetwork: number,
        destinationAddress: string,
        forceUpdateGlobalExitRoot: boolean,
        permitData = '0x',
        option?: ITransactionOption
);

const claimTx = zkEvmClient.childChainBridge.claimMessage(
				smtProof: string[],
        smtProofRollup: string[],
        globalIndex: string,
        mainnetExitRoot: string,
        rollupExitRoot: string,
        originNetwork: number,
        originTokenAddress: string,
        destinationNetwork: number,
        destinationAddress: string,
        amount: TYPE_AMOUNT,
        metadata: string,
        option: ITransactionOption
);

// proof can be fetched from the proof gen API
```

### Child to root (L2 → L1)

```jsx
const bridgeTx = zkEvmClient.childChainBridge.bridgeMessage(
				destinationNetwork: number,
        destinationAddress: string,
        forceUpdateGlobalExitRoot: boolean,
        permitData = '0x',
        option?: ITransactionOption
);

const claimTx = zkEvmClient.rootChainBridge.claimMessage(
				smtProof: string[],
        smtProofRollup: string[],
        globalIndex: string,
        mainnetExitRoot: string,
        rollupExitRoot: string,
        originNetwork: number,
        originTokenAddress: string,
        destinationNetwork: number,
        destinationAddress: string,
        amount: TYPE_AMOUNT,
        metadata: string,
        option: ITransactionOption
);

// proof can be fetched from the proof gen API
```
