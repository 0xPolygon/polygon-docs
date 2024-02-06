
This document provides instructions on how to top up the Heimdall fee for a PoS Validator. 

The easiest way is via the [Polygon Staking UI](https://staking.polygon.technology/account).

You can also do it manually by following the steps below; this requires basic Etherscan knowledge and key details like the Validator signer address.

1. Head over to [Etherscan.io](https://etherscan.io)

2. Enter the `StakeManagerProxy` contract address in the search box: [0x5e3Ef299fDDf15eAa0432E6e66473ace8c13D908](https://etherscan.io/address/0x5e3Ef299fDDf15eAa0432E6e66473ace8c13D908)

3. Under the **Code** menu, select the **Write as Proxy** tab. Connect your Web3 wallet using the **Connect to Web3** button.

    ![Figure: Connect wallet etherscan](../../../img/pos/connect-wallet-etherscan.png)

4. Scroll down to the `topUpForFee` method (#26 in the list) and select it. You will see something like the below screenshot.

    ![Figure: Topup Heimdall fee](../../../img/pos/topup-heimdall-fee.png)

5. Fill in the details:

    - `user`: Validator's Signer Address
    - `heimdallFee`: Topup fee (**minimum 1 MATIC**)

6. After filling in the details, click on **Write** to sign the transaction.

Your Heimdall fee will be updated soon after the transaction completes.
