!!! warning "Third-party content"

    Polygon technical documentation may contain third-party content, including websites, products, and services, that are provided for informational purposes only.

    Polygon Labs does not endorse, warrant, or make any representations regarding the accuracy, quality, reliability, or legality of any third-party websites, products, or services. If you decide to access any third-party content, you do so entirely at your own risk and subject to the terms and conditions of use for such websites. Polygon Labs reserves the right to withdraw such references and links without notice.

    Polygon technical documentation serves as an industry public good and is made available under the [MIT License](https://opensource.org/license/mit/). In addition, please view the official [Polygon Labs Terms of Use](https://polygon.technology/terms-of-use).

The Polygon API endpoint by GetBlock is a useful tool for early-stage teams that want to take advantage of Polygon's benefits. In this tutorial, we will walk you through the steps to create and deploy an ERC-20 smart contract on the Polygon Mumbai testnet using [Metamask](https://metamask.io/), Remix, and [GetBlock](https://getblock.io/nodes/matic/).

You will learn how to use GetBlock to create and deploy a smart contract on the Mumbai Testnet using [GetBlock](https://getblock.io/) endpoints.

## What you will do

In this tutorial, you will:

1. Get started on GetBlock and access test nodes.
2. Create a wallet address with Metamask.
3. Add test tokens to your wallet.
4. Compile and deploy a smart contract using Remix
5. Check the status of your smart contract.

### Preparation

1. The first step is to [sign up with Getblock](https://account.getblock.io/sign-in) via wallet or email via

  ![img](https://storage.getblock.io/web/blog/article-images/img1+(2).png)

2. Create an endpoint for Polygon testnet (Mumbai).

  ![img](https://storage.getblock.io/web/blog/article-images/img2+(1).png)

3. Then enter Metamask and choose to connect a network manually, connect your Metamask to the Mumbai Testnet adding your GetBlock endpoint in the **RPC URL** line

  ![img](https://storage.getblock.io/web/blog/article-images/imga3.png)

If you don't have any tokens in your account, you can request some from the Mumbai faucet through the [faucet website](https://faucet.polygon.technology/).

## Smart Contract Development

1. Visit the [official Remix website](https://remix.ethereum.org/). Remix is a Web-based IDE for Ethereum smart contract development in Solidity.

2. Click on the "Create a new file" button located on the left side of the page.

3. Select “Storage.sol” from Remix as an example of a contract.

  ![img](https://storage.getblock.io/web/blog/article-images/imga4.png)

4. Deploy the smart contract by clicking on the “Deploy & Run Transactions” tab.

5. Click on the “Deploy & Run Transactions” tab in Remix, located on the left-hand side of the screen.

6. In the “Contract” dropdown menu, select the name of the smart contract you want to deploy and click on the “Deploy” button to deploy the smart contract.
A Metamask window will pop up asking you to confirm the transaction. Click on the “Confirm” button to proceed.Wait for the transaction to be confirmed on the Polygon network.

> You can track the status of the transaction in the Metamask window or by checking the transaction hash on the Polygon explorer.

Once the transaction has been confirmed, you should see a green checkmark and a message indicating that the contract has been deployed successfully.

  ![img](https://storage.getblock.io/web/blog/article-images/imga5.png)

7. Locate the storage variable you want to test.

8. Choose "Injected provider" as the provider and select "Metamask" as the wallet.

 ![img](https://storage.getblock.io/web/blog/article-images/imga6.png)

> Check that your smart contract has been created on the network by looking at the Remix output panel.

9. Click on the "Polygon (Matic) Mainnet" dropdown menu located at the top right corner of the page and select "Mumbai Testnet" from the list of available networks. Then enter the address of your smart contract in the search bar located at the top of the page.

10. Click on the search button or hit enter.

 ![img](https://storage.getblock.io/web/blog/article-images/img6+(1).png)

Smart contract URL: <https://mumbai.polygonscan.com/address/0xa4d552dce0e26564ec1737638705584ce9ed351b>

If your smart contract has been successfully deployed, you should see the contract details including its address, balance, and transaction history. Congratulations, you have successfully deployed a smart contract on the Mumbai Testnet!

## Testing and Verification

Once you have deployed your smart contract on the Polygon test network using GetBlock, it is important to test and verify its functionality to ensure that it works as intended. Here are some steps you can take for testing and verification:

1. Open the smart contract in Remix and locate the storage variable you want to test. In this example, we will use a variable called "storage" that initially has a value of 12."

 ![img](https://storage.getblock.io/web/blog/article-images/img7+(1).png)

2. Change the value of the variable to 14 by entering "14" in the "Store" field and saving the value on the network after confirming the operation in Metamask.

3. Click on the "Transact" button to confirm the transaction in Metamask.

 ![img](https://storage.getblock.io/web/blog/article-images/imga10.png)

4. Wait for the transaction to be added to a network block. Once the transaction is confirmed, navigate to the "Read Contract" section under "Deployed Contracts".

5. Find the "storage" variable and click on the "Read" button. The new value of the variable should now be displayed as "14".

 ![img](https://storage.getblock.io/web/blog/article-images/img9+(1).png)

By following these steps, you can ensure that your smart contract works as intended and is secure and reliable for your users.

Congratulations, you have successfully deployed a smart contract on the Mumbai Testnet!

If you have any additional questions or would like to share your experience, feel free to join our [community of Web3 developers](https://discord.gg/Jb9UZZUHN7) who are always ready to chat.
