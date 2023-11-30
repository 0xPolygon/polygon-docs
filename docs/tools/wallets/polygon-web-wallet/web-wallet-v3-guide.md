**A new version of our Polygon Wallet is live**. Now called **Polygon Wallet Suite**, our new environment provides a more seamless experience with great improvements on the user interface as well as on its overall experience.

This guide shows instructions to deposit and withdraw funds using [Polygon Wallet Suite](https://wallet.polygon.technology/). For performing those actions, you need to connect a wallet to Polygon's environment. In this tutorial, we used Metamask, but Polygon is integrated with other wallets such as Coinbase, Bitski, Venly and WalletConnect.

!!! tip

    Please refer to [<ins>this guide</ins>](/tools/wallets/metamask/config-polygon-on-metamask.md) to learn how to connect Polygon to Metamask.

## Logging into the Polygon Wallet Suite

To log into the Polygon Wallet Suite you need to access the following URL: https://wallet.polygon.technology/.

Once you connect your account with the Web Wallet, you will be taken to the landing page with various means on how to transact with the web wallet. Polygon PoS chain currently offers the following services:

- **Polygon Wallet**: for sending, receiving and storing your assets on the Polygon network
- **Polygon Bridge**: for withdrawals and deposits across networks
- **Polygon Staking**: your go-to place for staking and getting rewards with your MATIC tokens
- and the **Polygon Safe Bridge**.

Click on the Polygon Wallet or Polygon Bridge, and you will see all your token balances on the Polygon Wallet across the bridges.

![img](/img/tools/wallet/v3/landing-page.png)

!!! tip "Metamask"

    Be attentive to all Metamask's popups. Throughout the deposit and withdrawal processes, you will be prompted with Metamask's popups to confirm transactions, switch networks and other procedures. You can only proceed with those transactions if you confirm the actions on Metamask.

## Deposit funds from Ethereum to Polygon

You can either watch the **video tutorial** here or follow the **step-by-step guide** provided below.

<div align="center">
  <video loop autoplay width="70%" height="70%" controls="true" >
    <source type="video/mp4" src="/img/wallet/v3/deposit/deposit-polygon-wallet.mp4"></source>
    <p>Your browser does not support the video element.</p>
  </video>
</div>

#### Step-by-Step Guide

1. Click on the **Move Funds from Ethereum to Polygon** button or on the **Deposit** button from any of the token types in the **Token** Balance** section.
  ![img](/img/tools/wallet/v3/deposit/balances.png)

2. You will be redirected to the bridge page where you need to enter the deposit amount.

    ![img](/img/tools/wallet/v3/deposit/bridge.png)

    !!! note
        The **transfer mode** will be enabled based on the token chosen.

3. Once you have added the amount that you want to deposit, you can then click on the **Transfer** button. After you click on the **Transfer** button, you need to click on the **Continue** button on the next popup.

    ![img](/img/tools/wallet/v3/deposit/please-note.png)

    You will see a **Transfer Overview** popup with an estimate of the total gas required for the transaction:

    ![img](/img/tools/wallet/v3/deposit/transfer-overview.png)

    After that, you can review your transaction details:

    ![img](/img/tools/wallet/v3/deposit/review-transfer.png)

4. Once you confirm the transaction, you will see a **Transfer in Progress** popup which will show you the Deposit status. It will take ~7-8 minutes for the tokens to show up on Polygon.

5. After the required time, the transaction will be completed.

    ![img](/img/tools/wallet/v3/deposit/completed.png)

You can always check your past and current transactions by clicking on the **Transactions** tab on the left.

##  Withdraw funds from Polygon to Ethereum

### On Polygon PoS bridge

Withdrawing funds from Polygon back to the Ethereum Mainnet via PoS Bridge is an extremely simple process. For the funds to be available back on Ethereum it will take from 45 minutes to 3 hours. You can either watch the **video tutorial** here or follow the **step-by-step guide** provided below.

<div align="center">
  <video loop autoplay width="70%" height="70%" controls="true" >
    <source type="video/mp4" src="/img/wallet/v3/pos/withdraw-polygon-wallet.mp4"></source>
    <p>Your browser does not support the video element.</p>
  </video>
</div>

#### Step-by-step guide

1. To withdraw funds, click on the **Withdraw** option on any of the tokens from the **Token Balance** section.
    ![img](/img/tools/wallet/v3/pos/balances.png)

2. You will be redirected to the Bridge page where you need to enter the Withdrawal amount.

    ![img](/img/tools/wallet/v3/pos/bridge.png)

    !!! note
        The **transfer mode** will be enabled based on the token chosen.

3. Once you have added the amount that you want to withdraw, you can then click on the **Transfer** button. After you click on the **Transfer** button, you need to click on the **Continue** button on the next popup.

    ![img](/img/tools/wallet/v3/pos/please-note.png)

    You will see a **Transfer Overview** popup with an estimate of the total gas required for the transaction:

    ![img](/img/tools/wallet/v3/pos/transfer-overview.png)

    After that, you can review your transaction details:

    ![img](/img/tools/wallet/v3/pos/review-transfer.png)

4. Once the transaction is approved, you will see a popup on your screen like this:

    ![img](/img/tools/wallet/v3/pos/transaction-progress.png)

    The first transaction is to initiate your withdrawal. You need to wait for the checkpoint to arrive. This could take up to 3 hours to complete.

    ![img](/img/tools/wallet/v3/pos/waiting-checkpoint.png)

5. Once the checkpoint has arrived, you will need to **confirm the second transaction**. Then, when you have confirmed the second transaction, you will receive your funds back on Ethereum.

    ![img](/img/tools/wallet/v3/pos/completed.png)

## Swap for gas

The MATIC token is used for paying gas fees in the Polygon ecosystem. It's always important to have a minimum amount of MATIC to perform transactions on Polygon. **In fact, 0.01 MATIC can pay for about 20 transactions**. There are a few ways you can acquire MATIC tokens:

- buy them using Fiat On-ramp platforms,
- swap for other tokens, or
- trade them on a supported exchange.

Polygon also offers the possibility of swapping tokens for MATIC. You can currently choose from a range of cryptocurrencies to swap for MATIC, namely ETH, USDC, USDT, and others.

!!! tip
    This is a gasless transaction. You do not have to pay any gas fees.

You can either watch the video tutorial below or follow the step-by-step guide.

<div align="center">
<video loop autoplay width="70%" height="70%" controls="true" >
  <source type="video/mp4" src="/img/wallet/v3/swap-gas.mp4"></source>
  <p>Your browser does not support the video element.</p>
</video>
</div>

#### Step-by-step guide

1. Assuming you are on the assets homepage, find the **Swap for Gas** feature on the sidebar on your left.

    ![img](/img/tools/wallet/swap-gas-home.png)

2. Now, you need to set the amount of MATIC you need, either by choosing one of the given quantities or entering the amount you need (1). You should also select the token that will be swapped for MATIC (2). **The minimum amount for requesting MATIC tokens is 0.5 MATIC**.

    ![img](/img/tools/wallet/swap-gas-tokens.png)

3. MetaMask will then prompt you to sign the transaction. If you haven't added the Polygon network to your Metamask, you will be prompted to install it. Please proceed with the installation or check out this guide [here](/tools/wallets/metamask/config-polygon-on-metamask.md).

    ![img](/img/tools/wallet/swap-gas-signature.png)

    !!! note
        If the **Sign** button is not visible, try scrolling down by clicking on the down arrow in the **Message** field.

4. After you signed it, you will be able to transfer the requested amount of MATIC to your wallet.

    ![img](/img/tools/wallet/swap-gas-transfer.png)

5. A new signature will be requested:

    ![img](/img/tools/wallet/swap-gas-sign-swap.png)

    Transaction completed. Remember that you can always verify it on [Polygonscan](https://polygonscan.com/)!


## Token swap

You can swap tokens for other tokens using the **Token Swap** feature, which uses decentralized exchanges under the hood. The Token Swap feature may be found in the Wallet Suite side menu.

![img](/img/tools/wallet/swap-token-home.png)

You can either watch the video tutorial here or follow the step-by-step guide provided below.

<div align="center">
<video loop autoplay width="70%" height="70%" controls="true" >
  <source type="video/mp4" src="/img/wallet/v3/swap-token.mp4"></source>
  <p>Your browser does not support the video element.</p>
</video>
</div>

#### Step-by-step guide

1. The token on the top is the one you are swapping. The other one on the bottom is what you are going to receive.

    ![img](/img/tools/wallet/swap-token.png)

2. Review the transaction before it goes through.

    ![img](/img/tools/wallet/swap-token-review.png)

3. **Sign** and confirm the transaction on MetaMask and the transaction will be completed successfully.

## Token lists

You can customize the list of tokens you may see on the Polygon Wallet Suite homepage. For that, click on **Manage Token List**:

![img](/img/tools/wallet/token-list-home.png)

There are some default options provided by Polygon, but you can always add new token lists by entering their URLs.

!!! tip
    You can find some of the token lists here: https://tokenlists.org/

![img](/img/tools/wallet/token-list-manage.png)

You can also **make your own list**, import it to Polygon Wallet and even share it with the community.
To learn more about creating your own token lists, check out this guide to [Authoring Token Lists on Github](https://github.com/uniswap/token-lists#authoring-token-lists).

!!! note
    The **Chain ID should be 137** when creating a Polygon list.

If you need to add a token to one of our lists, [<ins>add a Token Request</ins>](https://github.com/maticnetwork/polygon-token-list/issues/new?assignees=&labels=add+token+request&template=add_token_request.md&title=Add+%7BTOKEN_SYMBOL%7D%3A+%7BTOKEN_NAME%7D) with the required information, and it’ll be reviewed by our team.
