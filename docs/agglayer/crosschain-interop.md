---
hide:
  - toc
---

<style>
   .git-revision-date-localized-plugin, .md-source-file, .md-content__button.md-icon {
      display: none;
   }
</style>

# Cross-chain Interoperability

In the context of the Agglayer, cross-chain interoperability is the functionality for the direct exchange of tokens and data between different blockchain networks, even those with different underlying execution logic. 

The **Unified Bridge** provides two key mechanisms for cross-chain transactions:

- **Token Bridging**: Transfers assets, such as native tokens, ERC20 tokens, or wrapped tokens, from one blockchain to another.
- **Message Bridging**: Enables the transmission of data and execution of messages between chains, supporting interactions like contract-to-contract communication.

For developers, **Bridge-and-Call** extends this functionality of cross-chain interop to allow for direct contract execution on destination chains from a source chain. These components make it possible to build decentralized applications that operate across chains while maintaining data consistency and transaction integrity.

## Unified Bridge: Bridging Interface

There are two types of bridging transactions on the Unified Bridge:

- **Token**: `bridgeAsset` & `claimAsset` are used for bridging tokens from one chain to another.
- **Message**: `bridgeMessage` & `claimMessage` are used for bridging messages from one chain to another.

### Token Bridging

The code for `BridgeAsset` can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L204).

#### Steps to complete the bridging process:
1. Ensure the `destinationNetwork` is not the same as the source network's ID.
2. Prepare tokens for bridging. Token preparation varies based on token type:
   - **Native Gas Token (e.g., ETH, Custom Gas Token)**: Tokens are held in the bridge contract.
   - **WETH**: WETH tokens are burned from the user's address.
   - **Foreign ERC20 Token**: Burn the token if it does not originate from the source network.
   - **Native ERC20 Token**: Run `permitData` (if provided), then transfer tokens to the bridge contract.
   - **Note**: For ETH as the native token, the `WETHToken` address is `0x0`.
3. Emit the `BridgeEvent`.
4. Add the `bridgeAsset` data to the Local Exit Tree as a leaf node.

The code for `claimAsset` can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L446).

#### Inputs required for `claimAsset`:
- Proofs (`smtProofLocalExitRoot` and `smtProofRollupExitRoot`) are obtained via the **Proof Generation API**.
- `GlobalIndex` can be constructed as per instructions in **Global Exit Root, L1 Info Tree, Global Index**.
- Other details can be fetched via the **Transaction API**.

### Message Bridging

The `BridgeMessage` & `BridgeMessageWETH` code can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L325).

#### Steps to complete the bridging process:
1. Validate the value conditions based on the type of bridging method.
2. Confirm that the `destinationNetwork` differs from the source network's ID.
3. Emit the `BridgeEvent`.
4. Add `bridgeMessage` or `bridgeMessageWETH` data to the Local Exit Tree as a leaf node.

The `ClaimMessage` code can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L599).

The claiming process for messages is similar to the token claiming process, with additional steps to execute the message if the destination address is a smart contract.

## Bridge-and-Call

**Bridge-and-Call** allows developers to initiate cross-chain transaction calls from a source chain to a destination chain.

### Key Components
- **BridgeExtension.sol**: Manages bridge interactions.
- **JumpPoint.sol**: Handles asset transfers and contract calls on the destination chain.

For more examples, refer to the [lxly.js examples folder](https://github.com/0xPolygon/lxly.js/tree/main/examples/lxly).
