This document shows you how to customize wrapped tokens using adapter contracts, transfer tokens between Ethereum and Polygon zkEVM networks, and how to use Matic.js to bridge assets from Ethereum to Polygon zkEVM and vice versa.

## Basic functions for error passing

We refer to Ethereum as the _root_ chain and zkEVM as the _child_ chain.

Below we provide the two basic functions used for _error passing_ in each of the two directions: L1 --> L2 and L2 --> L1.

**Message**

- From root to child

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

// proof can be found from the proof gen API
```

- From child to root

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

// proof can be found from the proof gen API
```

## Bridging customized ERC20 token

The existing zkEVM bridge uses the ERC-20 standard contract for creating wrapped tokens depending on the token's native network.

Often, organizations want to customise their wrapped tokens by extending some functionalities. 

These functionalities could include: blacklisting, putting a cap on minting, or any sound auxiliary functionality.

This can be done by deploying adapter contracts that use the messaging layer of the bridge.

However, for the sake of maintaining consistency among wrapped tokens, strict standards must be followed when extending their functionalities.

## Standardizations

1. Adapter contracts need to implement the [Polygon bridge library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol) and expose `bridgeToken()` and `onMessageReceived()` functions.
2. There should be two separate adapter contracts; `OriginChainBridgeAdapter` and `WrapperChainBridgeAdapter`.
3. `bridgeToken` function should match the exact function signature and be similar to [this](https://github.com/maticnetwork/static/blob/master/network/mainnet/cherry/artifacts/zkevm/ZkEVMBridgeAdapter.json) ABI.

### Nice to have

Expose the following variables,

1. `originTokenAddress`: Address of the native token.
2. `originTokenNetwork`: `networkId` of the chain to which the token is native.
3. `wrappedTokenAddress`: Address of the wrapped token.

## What is an adapter?

An adapter is a wrapper contract that implements the [Polygon bridge library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol). An implementation example for ERC20 can be found [here](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/lib/PolygonERC20BridgeLib.sol).

Ideally, the following adapter contracts are expected,

1. `OriginChainBridgeAdapter`
2. `WrapperChainBridgeAdapter`

Irrespective of whether an ERC-20 token is Ethereum native (root chain) or ZkEvm native (child chain), an adapter contract should have the following functions (these are already part of the [library](https://github.com/0xPolygonHermez/code-examples/blob/main/customERC20-bridge-example/contracts/base/PolygonERC20BridgeBase.sol).

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

## How does it work?

`PolygonZkEVMBridge` is the main bridge contract. It exposes a `bridgeMessage()` function, which users can call in order to bridge messages from L1 to L2, or vice versa. The `claimMessage()` function can be called in the receiving chain to claim the sent message.

For example, a user who wants to bridge a message from Ethereum to zkEVM, can call `bridgeMessage()` in Ethereum and then call `claimMessage()` in zkEVM. Once the `claimMessage()` function is called, the bridge calls `onMessageReceived` in the destination address.

Adapter contracts are basically abstractions that uses `bridgeMessage()` to bridge and `onMessageReceived()` to process a `claimMessage()` in respective chains.

![Figure: Adapter contract](../../../img/learn/maticjs-adapter-contract-01.png)

## ERC-20 transfer

The transfer of ERC-20 tokens using each of the adapter contracts can be broken down as follows.

### OriginChainBridgeAdapter

The `bridgeToken()` function is called by the deployed adapter contract, to deposit an ERC-20 token from Ethereum to zkEVM.

The `onMessageReceived()` function is then called by the [PolygonZkEvmBridge.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMBridge.sol) contract when `claimMessage()` is called during withdrawal of tokens from zkEVM.

### WrapperChainBridgeAdapter

The `bridgeToken()` function is called by the deployed adapter contract to withdraw ERC20 from ZkEVM to Ethereum

The `onMessageReceived` function is called by the [PolygonZkEvmBridge.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/PolygonZkEVMBridge.sol) contract when `claimMessage()` is called when tokens are deposited to ZkEVM.

### From Ethereum → zkEVM

1. Deploy your adapter contracts on both the root chain and the child chain. (Note the address, you’ll need it later!)
2. Approve the tokens to be transferred by calling the `approve()` function (on the root token) with the address of the `originChainBridgeAdapter` and the token amount, as arguments.
3. Proceed to call `bridgeToken()` while using as arguments: the recipient, amount, and setting `forceUpdateGlobalExitRoot` to `true` on the `originChainBridgeAdapter` in the root chain (i.e., Ethereum).
4. Get the Merkle proof for this bridge transaction using the [proof api](https://proof-generator.polygon.technology/api/zkevm/testnet/merkle-proof?net_id=0&deposit_cnt=).
5. Proceed to call `claimMessage()` with the respective arguments on the `PolygonZkEVMBridge.sol` contract in the child chain (i.e., zkEVM).

The bridge will call the `onMessageReceived` function in the `WrapperChainBridgeAdapter` contract. Which should ideally have the logic to mint wrapped tokens to the recipient.

Note: It is assumed, in the above steps, that the token being bridged is native to the root chain.

### From zkEVM → Ethereum

1. Deploy your adapter contracts on both the root chain and the child chain. (Note the address, you’ll need it later!)
2. Approve the tokens to be transferred by calling the `approve()` function (on the wrapped token) with the address of the `wrapperChainBridgeAdapter` and the token amount as arguments.
3. Proceed to call `bridgeToken()`, using as arguments: the recipient, amount, and setting `forceUpdateGlobalExitRoot` to `true` on the `WrapperChainBridgeAdapter` in the child chain (i.e., zkEVM). Ideally, this function should have the logic to burn the wrapped tokens.
4. Get the Merkle proof for this bridge transaction using the [proof api](https://proof-generator.polygon.technology/api/zkevm/testnet/merkle-proof?net_id=0&deposit_cnt=).
5. Proceed to call `claimMessage()` with the respective arguments on the `PolygonZkEVMBridge.sol` contract in the root chain (i.e., Ethereum).

The bridge will call the `onMessageReceived` function in the `OriginChainBridgeAdapter` contract. Which should Ideally have the logic to mint unwrapped tokens to the recipient.

Note: It is assumed, in the above steps, that the token being bridge is native to the root chain.

## How to list my token in the BridgeUI?

Note that it is important to follow standardizations for easy listing.

1. Add your token to this list [https://github.com/maticnetwork/polygon-token-list/blob/dev/src/tokens/zkevmPopularTokens.json]
    
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

    !!!Note
        
        If the token is ethereum native then `originTokenNetwork` should be `0`. If the token is zkEVM native, then `originTokenNetwork` should be `1`. Similarly for the `wrappedTokenNetwork`.

2. Raise a PR 🚀

## How to use Matic.js to bridge using adapter contracts?

Deploy your `OriginChainBridgeAdapt` and `WrapperChainBridgeAdapter`. 

Make sure you are using `matic.js version > 3.6.4`.

- Create an instance of the zkEVM client, passing the necessary parameters. Refer [here](./initialize.md) for more info.
    
    ```jsx
    const client = new ZkEvmClient();
    *await* client.init({})
    ```

- Create an ERC-20 token instance which you would like to bridge,
    
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

2. **Claim Deposit**
    
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

2. **Claim Deposit**
    
    ```jsx
    const claimTx = await erc20.customERC20WithdrawExit("<withdraw tx hash>");
    const txHash = await claimTx.getTransactionHash();
    console.log("claimed txHash", ctxHash);
    ```
