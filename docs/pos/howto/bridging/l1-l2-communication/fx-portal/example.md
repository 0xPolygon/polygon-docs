## Overview

The contracts in the following example consist of two main parts, one for
the root chain (Goerli in this case), and one for the child chain (Mumbai).
The Goerli contract is responsible for mapping tokens from the root chain to
the child chain and sending deposits to the child chain. The Mumbai contract
is responsible for handling incoming messages from the Goerli contract, minting
child tokens, and processing child-to-root withdrawals.

Here is an overview of the following contracts used:

- **`SafeToken`** (Goerli): This contract deploys a simple ERC20 token that can be
  used to test the FxPortal functionality.
- **`FxERC20`** (Goerli): This contract template will create
  new child tokens on the Mumbai network. The contract is initialized with the
  address of the FxPortal contract and the address of the corresponding token on
  the root network. It contains a mint function that the root
  network contract to mint new child tokens can use.
- **`FxERC20`** (Mumbai): This contract is a child token minted by the root
  network contract. It is initialized with the address of the FxPortal contract,
  the address of the corresponding token on the root network, and the token's name, symbol,
  and decimals. It contains a burn function that can be used to burn
  child tokens.
- **`FxERC20RootTunnel`** (Goerli): This contract is responsible for mapping tokens
  from the root network to the child network and sending deposits to the child network.
  When a new token is mapped, the contract deploys a new child token contract using
  the `FxERC20` template and then maps the root token to the child token. The contract sends a
  message to the child network containing the deposit details when a deposit is made.
- **`FxERC20ChildTunnel`** (Mumbai): This contract is responsible for processing messages
  from the root network and minting new child tokens, as well as handling child-to-root
  withdrawals. When a new token is mapped, the contract deploys a new child token contract
  using the `FxERC20` template and then maps the root token to the child token. When a
  deposit message is received, the contract mints new child tokens and calls the
  `onTokenTransfer` function on the receiver (if it is a contract). When a withdrawal
  is made, the contract burns the child tokens and sends a message to the root network
  containing the withdrawal details.

## Prerequisites

- Goerli and Mumbai testnet accounts with some testnet ETH and MATIC tokens, respectively
- Metamask wallet

## Steps

1. Deploy the
   [SafeToken contract](https://gist.github.com/jamesyoung/d6d769f6792ad9cb35bfa01b8f37a082)
   on the Goerli testnet (using Remix or Truffle).
   This will be the ERC20 token to test the FxPortal functionality.

2. Deploy an
   [FxERC20 contract](hhttps://github.com/0xPolygon/fx-portal/blob/main/contracts/tokens/FxERC20.sol)
   on the Goerli network. This contract will be used as a template to create child tokens on the
   Mumbai network. The FxERC20 contract should be initialized with the address of the FxPortal
   contract and the address of the corresponding token on the root network.

3. Deploy an
   [FxERC20Child contract](https://github.com/0xPolygon/fx-portal/blob/main/contracts/tokens/FxERC20.sol)
   on the Mumbai network. This contract will be the child token minted by the root network contract.
   It should be initialized with the address of the FxPortal contract, the address of the corresponding
   token on the root network, and the token's name, symbol, and decimals.

4. Deploy an
   [FxERC20RootTunnel contract](https://github.com/0xPolygon/fx-portal/blob/main/contracts/examples/erc20-transfer/FxERC20RootTunnel.sol) on the Goerli network. This contract will map tokens
   from the root network to the child network and send deposits to the child network. When a new
   token is mapped, the contract deploys a new child token contract using the FxERC20 template and
   then maps the root token to the child token. The contract sends a message
   to the child network containing the deposit details when a deposit is made.
   - Constructor arguments:
     - **_checkpointManager** : 0x2890bA17EfE978480615e330ecB65333b880928e
     - **_fxRoot** : 0x3d1d3E34f7fB6D26245E6640E1c50710eFFf15bA
     - **_fxERC20Token** : SafeToken (address of ERC20 token created in step 1)

5. Deploy an
   [FxERC20ChildTunnel contract](https://github.com/0xPolygon/fx-portal/blob/main/contracts/examples/erc20-transfer/FxERC20ChildTunnel.sol) on the Mumbai network. This contract will be responsible for
   processing messages from the root network, minting new child tokens, and handling
   child-to-root withdrawals. When a new token is mapped, the contract deploys a new child token
   contract using the FxERC20 template and then maps the root token to the child token. When a
   deposit message is received, the contract mints new child tokens and calls the onTokenTransfer
   function on the receiver (if it is a contract). When a withdrawal is made, the contract burns
   the child tokens and sends a message to the root network containing the withdrawal details.
   - Constructor arguments:
     - **_fxChild** : 0xCf73231F28B7331BBe3124B907840A94851f9f11
     - **_tokenTemplate** : FxERC20 address (address of FxERC20 contract created in step 2)

6. On the FxERC20ChildTunnel contract (step 5), set the setFxRootTunnel function. This should be
   done with the FxERC20RootTunnel contract address from step 4.

7. On the FxERC20RootTunnel contract (step 4), set the setFxChildTunnel function. This should be
   done with the FxERC20ChildTunnel contract address from step 5.

8. On the SafeToken contract from step 1, call the mint function to mint the desired amount of
   tokens.

9. On the SafeToken contract, call the approve function with the FxERC20RootTunnel contract address
   from step 4 and the mint amount from step 9.

10. On the FxERC20RootTunnel contract from step 4, call the deposit function with the SafeToken on
    the Goerli network from step 1, the user address, the mint amount from step 9, and the data
    parameter `0x00`.

### Additional steps

11. On the FxERC20ChildTunnel contract from step 5, call the balanceOf function to check that
    the child tokens have been minted.

12. To withdraw the child tokens back to the Goerli network, call the withdraw function on the
    FxERC20ChildTunnel contract with the amount of child tokens to be burned.

13. Wait for the transaction to be confirmed and the withdrawal to be processed. You can check
    the status of the withdrawal using the FxExplorer.

14. On the SafeToken contract from step 1, call the balanceOf function to check that the
    corresponding amount of tokens has been deposited on the Goerli network.

Congratulations, you have successfully tested the FxPortal functionality for transferring
tokens between the Goerli and Mumbai networks!
