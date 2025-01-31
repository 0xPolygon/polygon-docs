## Introduction to the Unified Bridge

The Unified Bridge (prev. LxLy bridge) is an interoperability layer aimed at enabling cross-chain communication among AggLayer connected chains. It enables the interaction between different networks such as L2 to L2, L1 to L2, and L2 to L1.

### Why do we need a Unified Bridge?

The Unified Bridge is needed to enable cross-chain communication among different networks to solve the problem of fragmentation as well as to initiate one-step cross-chain transactions for seamless UX.

For the **AggLayer**, it is a critical component to facilitate unified experience among AggLayer-connected chains. In the process of cross-chain communication, the Unified Bridge is the interface for developers and users to initiate cross-chain transactions, which the AggLayer will then monitor and validate the validity of via a Pessimistic Proof. Once validated, the cross-chain message will be accepted and ready to be claimed on the destination chain.

## Unified Bridge: Data Structure

The data structures for the Unified Bridge are as follows:

The AggLayer maintains a merkle tree to record all cross-chain transactions and verify the validity of all cross-chain transactions, ensuring source chain transactions are indeed finalized on the L1 before claiming on the destination chain.

### Local Exit Root & Local Index

All cross-chain transactions using the Unified Bridge are recorded in a Sparse Merkle Tree called the Local Exit Tree. Each AggLayer-connected chain maintains its own local exit tree. This is maintained in the [`PolygonZKEVMBridgeV2.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol) contract on each AggLayer-connected L2 and L1.

- `Local Exit Root(LET)`: The root of the tree is called the local exit root. It is a binary tree with a height of 32. The root is updated every time a new cross-chain transaction is initiated.

- `depositCount(Local Root Index)`: The index of the leaf node, per leaf node is a hash of cross-chain transaction such as `bridgeAsset`/`bridgeMessage`.

### Rollup Exit Root

`rollupExitRoot` is the merkle root of all L2s' Local Exit Root. All AggLayer-connected L2s constantly update their Local Exit Root in [`PolygonRollupManager.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonRollupManager.sol), which updates the Rollup Exit Sparse Merkle Tree.

For each cross-chain transaction, it is the Source Chain's responsibility to submit its LET to the `RollupManager` smart contract on L1. The frequency with which LETs are submitted is up to the chain itself. 

Once the RollupManager has updated a `localExitRoot` of an L2, it will then update the `rollupExitRoot` on it, which will then update the `globalExitRoot` in [`PolygonZkEVMGlobalExitRootV2.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol) on the L1.

### Mainnet Exit Root

`mainnetExitRoot` is functionally the same as the Local Exit Root, but maintained on the L1, which tracks the bridging activities of the L1 to all AggLayer-connected L2s. When the Mainnet Exit Root is updated in the `PolygonZKEVMBridgeV2.sol` contract on the L1, it will then update the `mainnetExitRoot` in the [`PolygonZkEVMGlobalExitRootV2.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol) on the L1.

### Global Exit Root, L1 Info Tree, Global Index:

`globalExitRoot` is the hash of `rollupExitRoot` and `mainnetExitRoot`. When a new RER or MER is submitted to [`PolygonZkEVMGlobalExitRootV2.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMGlobalExitRootV2.sol), it will append the new GER to the L1 Info Tree. AggLayer-connected chains sync the L1's latest GER by calling the `updateExitRoot` function in the [`PolygonZkEVMGlobalExitRootL2.sol`] contract on L2.

`L1InfoTree` is the Sparse Merkle Tree that maintains the GERs. It is a binary tree with a height of 32. The root is updated every time a new GER is submitted.

`Global Index` is used to locate the unique leaf in the new global exit tree when creating and verifying the SMT proof. It is a 256-bit string composed of unused bits, mainnet flag, rollup index bits, and local root index bits. Beginning with the most significant, `Global Index` consists of the following bits:

- **191 bits of unused bits**: These bits are unused, and can be filled with any value. The best option is to fill them with zeros because zeros are cheaper.
- **1 bit of mainnet flag**: This single bit serves as a flag indicating whether an exit pertains to a rollup (represented by 0) or the mainnet (indicated by 1).
- **32 bit of the rollup Index**: These bits indicate the specific rollup being pointed at, within the rollup exit tree. These bits are therefore only used whenever mainnet flag is 0.
- **32 bits of the local root index**: These bits indicate the specific index being pointed at, within each rollup’s local exit tree.

## Unified Bridge: Components

There are two main components of the Unified Bridge: the on-chain contracts and the off-chain services, along with additional tools to help interact with the Unified Bridge. 

### Unified Bridge Contracts

The core of the service that acts as the interface for developers to initiate cross-chain transactions and facilitate contract calls on the destination chain if specified. It is deployed on both the source and destination chains.

These [contracts](https://github.com/0xPolygonHermez/zkevm-contracts/tree/main/contracts) consist of:

- `PolygonZKEVMBridgeV2.sol`: Bridge contract on both L1 and L2, maintains its own LET. It is the access point for all cross-chain transactions, including `bridgeAsset`, `bridgeMessage`, `claimAsset`, and `claimMessage`. 
- `PolygonRollupManager.sol`: Rollup Manager contract on L1, all L2 contracts settle on L1 and update their LET via the Rollup Manager on the L1. Then Rollup Manager updates the RET on L1.
- `PolygonZkEVMGlobalExitRootV2.sol`: The Global Exit Root contract on the L1 and L2, the root of which is updated each time a new Rollup Exit Root or Mainnet Exit Root is updated.

### Bridge Service

- **[Chain Indexer Framework](https://docs.polygon.technology/tools/chain-indexer-framework/overview/#2-why-do-dapps-need-a-blockchain-data-indexer)**: An EVM blockchain data indexer. It parses, sorts, and organizes blockchain data for the Bridge Service API. Each chain connected to AggLayer will have its own indexer instance.

- **Transaction API**: All details of a bridge transaction initiated by or incoming to a user’s walletAddress. Details include the real time status, the token bridged, the amount, the source and destination chain, etc. It is used for the user interface to display the status of the transaction. 

    - API endpoints: 
    
        - Testnet: `https://api-gateway.polygon.technology/api/v3/transactions/testnet?userAddress={userAddress}`
        
        - Mainnet: `https://api-gateway.polygon.technology/api/v3/transactions/mainnet?userAddress={userAddress}`

    - `userAddress` should be the address that is associated with the cross-chain transaction.

    - Attach API Key in the header.

    - An example Transaction API can be seen as follows:
      ```bash
      curl --location 'https://api-gateway.polygon.technology/api/v3/transactions/mainnet?userAddress={userAddress}' \
      --header 'x-api-key: <your-api-key-here>'
      ```
      > API Key: **Transaction API** & **Proof Generation API** requires API Key to access. Please Check this [guide](https://polygontechnology.notion.site/api-gateway-service-documentation) to generate one.


- **Proof Generation API**: The merkle proof payload needed to process claims on the destination chain. 

    - API endpoints:
    
        - Testnet: `https://api-gateway.polygon.technology/api/v3/proof/testnet/merkle-proof?networkId={sourceNetworkId}&depositCount={depositCount}`
        - Mainnet: `https://api-gateway.polygon.technology/api/v3/proof/mainnet/merkle-proof?networkId={sourceNetworkId}&depositCount={depositCount}`
    
    - `networkId` is the network ID registered on the AggLayer, `0` for Ethereum/Sepolia, and `1` for Polygon zkEVM/Cardona, and more.
    
    - `depositCount` is the leaf index of the Local Exit Tree from the source chain. The depositCount can be determined by checking the `bridgeAsset`/`bridgeMessage` event logs or by querying the Transaction API above.

    - Remember to attach API Key in header

### Tools

- **Claimer**: Any network participant may complete the bridging process by becoming the claimer. The Claim Service can be deployed by dapps, chains, or any individual end-user. There's also an [auto claiming script](https://github.com/0xPolygon/auto-claim-service) which automates the claim process on the destination chain.
- **[Lxly.js](https://github.com/0xpolygon/lxly.js?tab=readme-ov-file)**: LxLy.js is a javascript library which has all the prebuilt functions for interacting with the unified bridge contracts. It does most of the heavy lifting, including type conversion, formatting, error handling, etc., making it very easy for a developer to invoke the bridge, claim, and other functions required for bridging.

## Unified Bridge: Bridging Interface

There are two types of bridging transactions on the Unified Bridge.

- Token: `bridgeAsset` & `claimAsset` are used for bridging tokens from one chain to another.
- Message: `bridgeMessage` & `claimMessage` are used for bridging messages from one chain to another

### Token Bridging

**The code for `BridgeAsset` can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L204); the interface is as follows:** 

```solidity
/**
* @notice Deposit add a new leaf to the merkle tree
* note If this function is called with a reentrant token, it would be possible to `claimTokens` in the same call
* Reducing the supply of tokens on this contract, and actually locking tokens in the contract.
* Therefore we recommend to third parties bridges that if they do implement reentrant call of `beforeTransfer` of some reentrant tokens
* do not call any external address in that case
* note User/UI must be aware of the existing/available networks when choosing the destination network
* @param destinationNetwork Network destination
* @param destinationAddress Address destination
* @param amount Amount of tokens
* @param token Token address, 0 address is reserved for ether
* @param forceUpdateGlobalExitRoot Indicates if the new global exit root is updated or not
* @param permitData Raw data of the call `permit` of the token
*/
function bridgeAsset(
    uint32 destinationNetwork,
    address destinationAddress,
    uint256 amount,
    address token,
    bool forceUpdateGlobalExitRoot,
    bytes calldata permitData
)
```

These steps complete the bridging process:
1. Check the `destinationNetwork` is not set as the source network's ID.
2. Prepare tokens to be bridged.

There are different ways to prepare the tokens to be bridged, depending on the token type:

| Token type | Action |
| --- | --- |
| Native Gas Token, including ETH and Custom Gas Token | The bridge contract holds the tokens. |
| WETH | Burn the `WETH` tokens from user's address. |
| Foreign ERC20 Token | If the token contract is not originally from the source network, burn the ERC20 token from user's address. |
| Native ERC20 Token | If the token contract is originally from the source network, run the `permitData` if provided, then transfer the ERC20 token from user's address to the bridge contract. |

> Note that in case `ETH` is the native token, WETHToken will be at `0x0` address.

1. Emit the `BridgeEvent`
2. Add the `bridgeAsset` data to the `Local Exit Tree` as a leaf node

**The code for `claimAsset` can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L446); the interface is as follows:**

```solidity
/**
* @notice Verify merkle proof and withdraw tokens/ether
* @param smtProofLocalExitRoot Smt proof to proof the leaf against the network exit root
* @param smtProofRollupExitRoot Smt proof to proof the rollupLocalExitRoot against the rollups exit root
* @param globalIndex Global index is defined as:
* | 191 bits |    1 bit     |   32 bits   |     32 bits    |
* |    0     |  mainnetFlag | rollupIndex | localRootIndex |
* note that only the rollup index will be used only in case the mainnet flag is 0
* note that global index do not assert the unused bits to 0.
* This means that when synching the events, the globalIndex must be decoded the same way that in the Smart contract
* to avoid possible synch attacks
* @param mainnetExitRoot Mainnet exit root
* @param rollupExitRoot Rollup exit root
* @param originNetwork Origin network
* @param originTokenAddress  Origin token address, 0 address is reserved for ether
* @param destinationNetwork Network destination
* @param destinationAddress Address destination
* @param amount Amount of tokens
* @param metadata Abi encoded metadata if any, empty otherwise
*/
function claimAsset(
    bytes32[_DEPOSIT_CONTRACT_TREE_DEPTH] calldata smtProofLocalExitRoot,
    bytes32[_DEPOSIT_CONTRACT_TREE_DEPTH] calldata smtProofRollupExitRoot,
    uint256 globalIndex,
    bytes32 mainnetExitRoot,
    bytes32 rollupExitRoot,
    uint32 originNetwork,
    address originTokenAddress,
    uint32 destinationNetwork,
    address destinationAddress,
    uint256 amount,
    bytes calldata metadata
)
```

Before the `claimAsset` function is initiated, these inputs must be satisfied:

- Both `smtProofLocalExitRoot` and `smtProofRollupExitRoot` can be fetched via the **Proof Generation API**, the `depositCount` param for the Proof API is located at the fetch result of **Transaction API**, is your bridge transaction's `counter` field in the response.
- `GlobalIndex` can be constructed as described in **Global Exit Root, L1 Info Tree, Global Index**
- The rest can be found via **Transaction API**.

Then the code will go through a few steps to complete the claiming process:

1. Check the `destinationNetwork` is in fact the current network.
2. Verify the SMT Proofs.
   1. Construct the new `globalExitRoot` using `mainnetExitRoot` and `rollupExitRoot` and compare with the L2 chain's recorded updated `globalExitRoot`. If they are different, then revert.
   2. According to `Global Index` to check if source chain is L1 or L2
      - If L1, then verify `smtProofLocalExitRoot` with `mainnetExitRoot`
      - If L2, then verify the L2 leaf node with `smtProofLocalExitRoot`, `smtProofRollupExitRoot`, and `rollupExitRoot`
   3. Record that it's claimed on the destination network.
3. Once the proof passes, tokens are claimed according to the token type:

| Token type | Action |
| --- | --- |
| ETH is gas token | Bridge contract will transfer the amount from itself to the destination address. |
| WETH where ETH is not gas token | Mint new WETH to the destination address. |
| Custom gas token | Bridge contract will transfer the amount from itself to the destination address. |
| Native ERC20 Token | If the token contract is originally from this destination network, the transfer the ERC20 token from bridge contract to destination address. |
| Foreign ERC20 Token, First time bridging | Deploy a new ERC20 Token contract to host this new Foreign ERC20 Token. and mint the transfer amount to destination address. |
| Foreign ERC20 Token, Contract exist | Mint the transfer amount to destination address. |

4. Emit the `ClaimEvent`

### Message Bridging

**The `BridgeMessage` & `BridgeMessageWETH` code can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L325); the interface is as follows:** 

```solidity
/**
* @notice Bridge message and send ETH value
* note User/UI must be aware of the existing/available networks when choosing the destination network
* @param destinationNetwork Network destination
* @param destinationAddress Address destination
* @param forceUpdateGlobalExitRoot Indicates if the new global exit root is updated or not
* @param metadata Message metadata
*/
function bridgeMessage(
    uint32 destinationNetwork,
    address destinationAddress,
    bool forceUpdateGlobalExitRoot,
    bytes calldata metadata
) payable

/**
* @notice Bridge message and send ETH value
* note User/UI must be aware of the existing/available networks when choosing the destination network
* @param destinationNetwork Network destination
* @param destinationAddress Address destination
* @param amountWETH Amount of WETH tokens
* @param forceUpdateGlobalExitRoot Indicates if the new global exit root is updated or not
* @param metadata Message metadata
*/
function bridgeMessageWETH(
    uint32 destinationNetwork,
    address destinationAddress,
    uint256 amountWETH,
    bool forceUpdateGlobalExitRoot,
    bytes calldata metadata
)
```

These steps complete the bridging process:

1. Check value condition:
   - [For `BridgeMessage`], if the custom gas token exist in the source chain, then this function is only callable without value. A value should only be transferable via this function if the native gas token is `ETH`
   - [For `BridgeMessageWETH`], only allowed to use if `ETH` is not the gas token of the chain.
2. Check the `destinationNetwork` is not set as the source network's ID.
3. Emit the `BridgeEvent`
4. Add the `bridgeMessage` / `bridgeMessageWETH`  data to the `Local Exit Tree` as a leaf node.

**The `ClaimMessage` code can be found [here](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/v2/PolygonZkEVMBridgeV2.sol#L599); the interface is as follows:** 

```solidity
/**
* @notice Verify merkle proof and execute message
* If the receiving address is an EOA, the call will result as a success
* Which means that the amount of ether will be transferred correctly, but the message
* will not trigger any execution
* @param smtProofLocalExitRoot Smt proof to proof the leaf against the exit root
* @param smtProofRollupExitRoot Smt proof to proof the rollupLocalExitRoot against the rollups exit root
* @param globalIndex Global index is defined as:
* | 191 bits |    1 bit     |   32 bits   |     32 bits    |
* |    0     |  mainnetFlag | rollupIndex | localRootIndex |
* note that only the rollup index will be used only in case the mainnet flag is 0
* note that global index do not assert the unused bits to 0.
* This means that when synching the events, the globalIndex must be decoded the same way that in the Smart contract
* to avoid possible synch attacks
* @param mainnetExitRoot Mainnet exit root
* @param rollupExitRoot Rollup exit root
* @param originNetwork Origin network
* @param originAddress Origin address
* @param destinationNetwork Network destination
* @param destinationAddress Address destination
* @param amount message value
* @param metadata Abi encoded metadata if any, empty otherwise
*/
function claimMessage(
    bytes32[_DEPOSIT_CONTRACT_TREE_DEPTH] calldata smtProofLocalExitRoot,
    bytes32[_DEPOSIT_CONTRACT_TREE_DEPTH] calldata smtProofRollupExitRoot,
    uint256 globalIndex,
    bytes32 mainnetExitRoot,
    bytes32 rollupExitRoot,
    uint32 originNetwork,
    address originAddress,
    uint32 destinationNetwork,
    address destinationAddress,
    uint256 amount,
    bytes calldata metadata
)
```

The data preparation steps are the same as with `claimAsset`. Completing the claiming process requires the following:

1. Check the `destinationNetwork` is in fact the current network.
2. Verify the SMT Proofs.
   1. Construct the new `globalExitRoot` using `mainnetExitRoot` and `rollupExitRoot` and compare with the L2 chain's recorded updated `globalExitRoot`. If they are different, then revert.
   2. According to `Global Index` to check if source chain is L1 or L2:
      - If L1, then verify `smtProofLocalExitRoot` with `mainnetExitRoot`
      - If L2, then verify the L2 leaf node with `smtProofLocalExitRoot`, `smtProofRollupExitRoot`, and `rollupExitRoot`
   3. Record that it is claimed on the destination chain.
3. Once the proof passes, execute the message, (please note: message can only be executed if the `destinationAddress` is a smart contract that inherited the [`IBridgeMessageReceiver.sol`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/main/contracts/interfaces/IBridgeMessageReceiver.sol) interface).
   - If the native gas token is `ETH`, then transfer `ETH` to the `destinationAddress` and execute the message.
   - If `ETH` is not the native gas token, then mint `WETH` to the `destinationAddress` and exeute the message.
4. Emit the `ClaimEvent`.


## Bridge-and-Call

Bridge-and-Call is a feature in the Unified Bridge that allows developers to initiate a cross-chain transaction call on the destination chain from the source chain.

Bridge-and-Call is differentiated from **Bridge Message**, where Bridge Message requires the destination address to be a smart contract that implemented the `IBridgeMessageREceiver.sol` interface. Whereas **Bridge-and-Call** itself is the contract that has implemented the interface, allowing it to execute any function on any smart contract on the destination network.

### Bridge-and-Call: Components

There are multiple interfaces and helper contracts, as well as the extension contract. The key ones are:

- [`BridgeExtension.sol`](https://github.com/agglayer/lxly-bridge-and-call/blob/755088953ddd2f586a2009ae34a33ae12e60f0eb/src/BridgeExtension.sol): Bridge Extension contract on both L1 and L2 that access the `PolygonZKEVMBridgeV2.sol` contract. 
- [`JumpPoint.sol`](https://github.com/agglayer/lxly-bridge-and-call/blob/755088953ddd2f586a2009ae34a33ae12e60f0eb/src/JumpPoint.sol): Process the Destination Chain asset transfer as well as the contract call.

## Bridging Interface in Bridge-and-Call

### BridgeExtention.sol

**The `bridgeAndCall` code can be found [here](https://github.com/agglayer/lxly-bridge-and-call/blob/755088953ddd2f586a2009ae34a33ae12e60f0eb/src/BridgeExtension.sol#L29); the interface is as follows:** 

```solidity
/**
* @notice Bridge and Call from source chain to destination chain
* @param token Token to send to destination chain
* @param amount Amount of token to send to destination Chain
* @param callAddress The smart contract address to call at the destination network from destination
* BridgeExtension contract.
* @param fallbackAddress If the JumpPoint Execution fails on callAddress, the assets will be transferred to the fallbackAddress on destination network
* @param callData Abi encoded callData if any, empty otherwise
* @param forceUpdateGlobalExitRoot Indicates if the new global exit root is updated or not
*/
function bridgeAndCall(
    address token,
    uint256 amount,
    uint32 destinationNetwork,
    address callAddress,
    address fallbackAddress,
    bytes calldata callData,
    bool forceUpdateGlobalExitRoot
) external payable
```

These steps complete the bridging process:

1. Preparing Bridging Tokens:
   - When the source chain's gas token is not `ETH`, then send `WETH` from sender address to the bridge extension contract
   - When transfering gas token, gas token already transferred to the extension contract
   - When transfering any ERC-20 tokens, send the token from sender address to the bridge extension contract
2. Compute JumpPoint address on destination network and call `bridgeAssets`
3. Check if `bridgeAsset` was successful 
4. If successful, encode message to bridge and call `bridgeMessage`

**The `onMessageReceived` code can be found [here](https://github.com/agglayer/lxly-bridge-and-call/blob/755088953ddd2f586a2009ae34a33ae12e60f0eb/src/BridgeExtension.sol#L218); the interface is as follows:** 

```solidity
/**
* @notice interface for PolygonZkEVM Bridge message receiver
* @param originAddress Message origin sender address. (BridgeExtension Address on source chain)
* @param originNetwork Message origin network. (Source chain network id)
* @param data Abi encoded callData. 
*/
function onMessageReceived(
	address originAddress, 
	uint32 originNetwork, 
	bytes calldata data
) external payable
```

Note: This function is called when calling `claimMessage` on the destination chain; it's only callable by the Bridge Contract.

1. Access control, making sure its Bridge Contract Calling, and the message origin on the source chain is also bridge contract.

2. Decode `data` into 

   ```solidity
   uint256 dependsOnIndex,
   address callAddress,
   address fallbackAddress,
   uint32 assetOriginalNetwork,
   address assetOriginalAddress,
   bytes memory callData
   ```

3. Check if the Bridge Message is claimed 

4. Instantiate a new JumpPoint smart contract and execute the asset that was transferred from Bridge Contract to the JumpPoint smart contract, then transfer them to the final `callAddress` contract and execute `callData`.

### JumpPoint.sol

```solidity
constructor(
    address bridge,
    uint32 assetOriginalNetwork,
    address assetOriginalAddress,
    address callAddress,
    address fallbackAddress,
    bytes memory callData
) payable
```

The assets transferred from the source chain via `bridgeAsset` should have already transferred to this new jumpPoint smart contract on the destination chain.

1. Once instantiated, check that the asset that was transferred to the jumpPoint smart contract, whether it is a `ETH` token, `WETH` token, Custom Gas Token, or ERC-20 token.
2. Depending on the token type, transfer the token accordingly to the final `callAddress`, and then perform the smart contract call with `callData`
3. If the execution fails on the `callAddress` contract, tokens are transferred to `fallbackAddress`

## Security of the Unified Bridge
- **Secured by Ethereum**: Settlement on Ethereum
  
  All cross-chain transactions are settled on Ethereum before they can be claimed on the destination chain. This ensures that asset transfers originating from the source chain are valid and secure.

- **Secured by Mathematics**: Merkle Proof Validation
  
  Once the source chain bridging transaction is finalized on Ethereum, the destination chain verifies the proof to confirm that the assets transferred from the source chain are indeed settled on Ethereum.

- **Secured by Design**: Immutable Data Packaging 

  During an asset transfer from the source chain, the transaction requires the caller to specify the destination chain, the destination address, and the amount of assets to be transferred. These details are bundled together in an immutable cross-chain transaction.

  When claiming the assets on the destination chain, the smart contract verifies the correct destination network and processes the claim using the pre-defined destination address and asset amount. This design ensures:
  - Assets cannot be claimed on an incorrect network.
  - Assets cannot be claimed to an incorrect address.
  - Assets cannot be claimed in excess of the transferred amount.

  The claim process is open to anyone, as the outcome is predetermined regardless of who initiates the claim. Claimers simply pay the gas fee to facilitate the completion of the cross-chain transaction.

- **Secured by Access Control**: No Administrative Privileges
  
  The bridge contract can only mint, burn, or transfer assets through user-initiated bridge transactions. There is no administrative control over assets locked in the bridge contract. Only users with a balance of the specific tokens have access to their respective assets.

The supply of tokens shown on an individual chain’s contracts may be much higher than what has actually been deposited; this is an implementation detail to provide a sufficient virtual balance to handle any bridging activity. These figures do not reflect the circulating supply. The actual movement of tokens is strictly controlled by cryptographic proofs, mathematical constraints, and the immutable total supply of that particular token.

To learn more about the actions for different types of tokens (gas token, ETH, ERC-20 tokens, etc), refer to the above [specs](#assets-bridging)

# Using it as a Developer

> For more `lxly.js` examples, please refer to the [examples](https://github.com/0xPolygon/lxly.js/tree/main/examples/lxly) folder.

## L1 -> L2 using `BridgeAsset` interface in `Lxly.js`:

### Flow for L1 -> L2 Bridging Transactions

1. User/Developer/Dapp initiate `bridgeAsset` call on L1
2. Bridge contract on L1 appends an exit leaf to mainnet exit tree of the L1, and update its mainnet exit root.
3. Global exit root manager appends the new L1 mainnet exit root to global exit tree and computes the new global exit root.
4. L2 sequencer fetches and updates the latest global exit root from the global exit root manager.
5. User/Developer/Dapp/Chain initiates `claimAsset` call, and also provides the smtProof.
6. Bridge contract on destination L2 chain validates the smtProof against the global exit root on its chain. If passes next step.
7. Transfer/Mint the asset to the destination address.

### Code Walkthrough

The following example uses `lxly.js` to initiate the `bridgeAsset` call and `claimAsset` call.

1. Check your Balance: `node scripts/src/balance.js`

```javascript
const { getLxLyClient, tokens, configuration, from } = require('./utils/utils_lxly');

const execute = async () => {
  // instantiate a lxlyclient
  const client = await getLxLyClient();
  // Sepolia NetworkId is 0, Cardona NetworkId is 1
  const networkId = 0;
  // get an api instance of ether token on sepolia testnet
  const erc20Token = client.erc20(tokens[networkId].ether, networkId);
  // check balance
  const result = await erc20Token.getBalance(from);
  console.log("result", result);
}

execute().then(() => {
}).catch(err => {
  console.error("err", err);
}).finally(_ => {
  process.exit(0);
});
```

2. Bridge ETH from sepolia to Cardona: `node scripts/src/bridge_asset.js`

```javascript
const { getLxLyClient, tokens, configuration, from, to } = require('./utils/utils_lxly');

const execute = async () => {
    // instantiate a lxlyclient
    const client = await getLxLyClient();
    // source NetworkId is 0, since its Sepolia
    const sourceNetworkId = 0;
    // get an api instance of ether token on sepolia testnet
    const token = client.erc20(tokens[sourceNetworkId].ether, sourceNetworkId);
    // Set Destination Network as Cardona
    const destinationNetworkId = 1;
    // call the `bridgeAsset` api. Bridging 1 eth
    const result = await token.bridgeAsset("1000000000000000000", to, destinationNetworkId);
  	// getting the transactionhash if rpc request is sent
    const txHash = await result.getTransactionHash();
    console.log("txHash", txHash);
  	// getting the transaction receipt.
    const receipt = await result.getReceipt();
    console.log("receipt", receipt);
}

execute().then(() => {
}).catch(err => {
    console.error("err", err);
}).finally(_ => {
    process.exit(0);
});
```

3. Claim Assets after `GlobalExitRootManager` is synced from the source to destination chains. As Cardona currently has an autoclaiming bot running, there is no need to performs a claim asset call. The code for `scripts/src/claim_asset.js` is as follows:

```javascript
const { getLxLyClient, tokens, configuration, from } = require('./utils/utils_lxly');

const execute = async () => {
  	// the source chain txn hash of `bridgeAsset` call.
    const bridgeTransactionHash = "";
		
    // instantiate a lxlyclient
  	const client = await getLxLyClient();
    // the source networkId
    const sourcenNetworkId = 0;
    // the destination networkId
    const destinationNetworkId = 1;
    // get an api instance of ether token on cardona testnet
    const token = client.erc20(tokens[destinationNetworkId].ether, destinationNetworkId);
	  // call the `claimAsset` api.
    const result = await token.claimAsset(bridgeTransactionHash, sourcenNetworkId, {returnTransaction: true});
    console.log("result", result);
  	// getting the transactionhash if rpc request is sent
    const txHash = await result.getTransactionHash();
    console.log("txHash", txHash);
  	// getting the transaction receipt.
    const receipt = await result.getReceipt();
    console.log("receipt", receipt);

}

execute().then(() => {
}).catch(err => {
    console.error("err", err);
}).finally(_ => {
    process.exit(0);
});
```

4. After about 20 mins, the balance of `ETH` on the destination chain will have increased to the transfered amount. You can check using the `balance.js` script, being careful to ensure you have changed the network id.

## L2 -> L1 using `BridgeMessage` interface in `Lxly.js`: 

### Flow for L2 -> L1 Bridging Transactions

1. User/Developer/Dapp initiate `bridgeMessage` call on L2
2. Bridge contract on L2 appends an exit leaf to local exit tree of the L2, and update its global exit root on L2.
3. Sends the new local exit root to L1 to verify. Once passed, the L2's local exit root will be updated, which will cause a chain of updates to the Global Exit Root and the L1InfoTree on the L1.
4. User/Developer/Dapp/Chain initiates `claimMessage` call, and also provides the smtProof.
5. Bridge contract on the destination L1 chain validates the smtProof against the global exit root on its chain. 
6. Execute `onMessageReceived` process.

### Code Walkthrough

The following example uses `lxly.js` to initiate the `bridgeMessage` call and `claimMessage` call:

1. Deploy a `onMessageReceived` function implemented smart contract `counter.sol` on the destination chain. In this example, it will be Sepolia.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.16;

contract counter {
    uint256 public count;

    constructor() {
        count = 0;
    }

    function increment(uint256 amount) public {
        count = count + amount;
    }

    // Function to handle the received message
    // this is the interface that `claimMessage` will be able to access with.
    function onMessageReceived(
        address originAddress, 
        uint32 originNetwork, 
        bytes calldata metadata
    ) external payable {
        uint256 amount = abi.decode(metadata, (uint256));
        require(amount > 0, "Has to increment at least 1");
        require(amount < 5, "Has to increment less than 5");
        // its also better to check if the msg.sender is the bridge address
        // for this demo we will assume it always will be

        increment(amount);
    }
}
```

2. Bridge Message from Cardona to Sepolia: `node scripts/src/bridge_message.js`

```javascript
const { getLxLyClient, tokens, configuration, from, to } = require('./utils/utils_lxly');
const { Bridge } = require('@maticnetwork/lxlyjs');
const { encodePacked } = require('viem');

// Encode the amount into a uint256.
function encodeMetadata(amount) {
    return encodePacked(["uint256"], [amount]);
}

const execute = async () => {
    const client = await getLxLyClient();
    // change this with your smart contract deployed on destination network.
    const destinationAddress = "0x43854F7B2a37fA13182BBEA76E50FC8e3D298CF1"; 
    // the destination Network ID for this example is spolia, therefore is 0.
    const sourceNetworkId = 1;
    // Call bridgeMessage function.
    const destinationNetworkId = 0; 
    // the source Network ID for this example is Cardona, therefore is 1.
    const result = await client.bridges[sourceNetworkId]
        .bridgeMessage(destinationNetworkId, destinationAddress, true, encodeMetadata(3));
    const txHash = await result.getTransactionHash();
    console.log("txHash", txHash);
    const receipt = await result.getReceipt();
    console.log("receipt", receipt);
}

execute().then(() => {
}).catch(err => {
    console.error("err", err);
}).finally(_ => {
    process.exit(0);
});

```

3. Claim Message after GlobalExitRootManager is synced on the L1.  `scripts/src/claim_message.js`:

```javascript
const { getLxLyClient, tokens, configuration, from, to } = require('./utils/utils_lxly');

const execute = async () => {
    const client = await getLxLyClient();
    // bridge txn hash from the source chain.
    const bridgeTransactionHash = "0xfe25c1d884a7044ba18f6cee886a09a8e94f9ae12c08fd5d94cdc6f430376bf2"; 
    // Network should be set as 1 since its from cardona.
    const sourceNetworkId = 1;
    // Network should be set as 0 since its to sepolia
    const destinationNetworkId = 0;
    // API for building payload for claim
    const result = 
        await client.bridgeUtil.buildPayloadForClaim(bridgeTransactionHash, sourceNetworkId)
        // payload is then passed to `claimMessage` API
        .then((payload) => {
            console.log("payload", payload);
            return client.bridges[destinationNetworkId].claimMessage(
                payload.smtProof,
                payload.smtProofRollup,
                BigInt(payload.globalIndex),
                payload.mainnetExitRoot,
                payload.rollupExitRoot,
                payload.originNetwork,
                payload.originTokenAddress,
                payload.destinationNetwork,
                payload.destinationAddress,
                payload.amount,
                payload.metadata
            );
        });

    const txHash = await result.getTransactionHash();
    console.log("txHash", txHash);
    const receipt = await result.getReceipt();
    console.log("receipt", receipt);
}

execute().then(() => {
}).catch(err => {
    console.error("err", err);
}).finally(_ => {
    process.exit(0);
});
```


## L2 to L2 using `Bridge-and-Call` in Lxly.js:

### Flow for L2 to L2 Bridging Transactions

1. User/Developer/Dapp initiate `bridgeAndCall` call on the L2 source chain
2. Similar to the L2 to L1 flow, the global exit root on the L1 is updated, which includes the source chain bridging transaction.
3. Then destination L2 sequencer fetches and updates the latest global exit root from the global exit root manager.
4. THe Bridge contract on the destination chain validates the smtProof against the global exit root on its chain. 
5. Process the `claimAsset`, `claimMessage` on destination chain.

### Code Walkthrough

The following example uses lxly.js to initiate the `bridgeAndCall` call and `claimMessage` call:

1. Deploy the same `counter.sol` contract on `zkyoto` testnet.
2. Call `bridgeAndCall` from cardona to zkyoto: `node scripts/src/bridge_and_call.js`

```javascript
const { getLxLyClient, tokens, configuration, from } = require('./utils/utils_lxly');
const { CounterABI } = require("../../ABIs/Counter");

const execute = async () => {
    const client = await getLxLyClient();

    // set token as `eth`.
    const token = "0x0000000000000000000000000000000000000000";
    // not bridging any token this time
    const amount = "0x0";
    // because we are bridging from cardona.
    const sourceNetwork = 1; 
    // sending to zkyoto.
    const destinationNetwork = 2;
    // change it to the counter smart contract deployed on destination network.
    const callAddress = "0x43854F7B2a37fA13182BBEA76E50FC8e3D298CF1";
    // if transaction fails, then the funds will be sent back to user's address on destination network.
    const fallbackAddress = from;
    // if true, then the global exit root will be updated.
    const forceUpdateGlobalExitRoot = true;
    // get the call Contract ABI instance.
    const callContract = client.contract(CounterABI, callAddress, destinationNetwork);
    // prepare the call data for the counter smart contract on destination chain.
    const callData = await callContract.encodeAbi("increment", "0x4");  
    
    let result;
    // Call bridgeAndCall function.
    if (client.client.network === "testnet") {
        console.log("testnet");
        result = await client.bridgeExtensions[sourceNetwork].bridgeAndCall(
            token,
            amount,
            destinationNetwork,
            callAddress,
            fallbackAddress,
            callData,
            forceUpdateGlobalExitRoot,
            permitData="0x0", // permitData is optional
        )
    } else {
        console.log("mainnet");
        result = await client.bridgeExtensions[sourceNetwork].bridgeAndCall(
            token,
            amount,
            destinationNetwork,
            callAddress,
            fallbackAddress,
            callData,
            forceUpdateGlobalExitRoot,
        )
    }

    console.log("result", result);
    const txHash = await result.getTransactionHash();
    console.log("txHash", txHash);
    const receipt = await result.getReceipt();
    console.log("receipt", receipt); 
}

execute().then(() => {
}).catch(err => {
    console.error("err", err);
}).finally(_ => {
    process.exit(0);
});
```

3. Claim Message after GlobalExitRootManager is synced on zkyoto using `scripts/src/claim_message.js` Remember to update `bridgeTransactionHash`, and `destinationNetworkId` to `2`, for zkyoto's network id.