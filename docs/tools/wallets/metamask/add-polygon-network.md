<!--
---
comments: true
---
-->

!!! warning "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

To track your assets and send transactions on any of the Polygon networks using MetaMask, you need to add the respective network configurations to the wallet.

In this doc, we demonstrate a few ways to do this for Polygon PoS testnet (Amoy) and mainnet. You can use the same methods to add Polygon zkEVM to your MetaMask wallet.

## ChainList

1. Depending on the network profile that you want to add to your MetaMask wallet, use one of the following links to navigate to the respective ChainList page.

    - [Polygon PoS testnet (Amoy)](https://chainlist.org/chain/80002)
    - [Polygon PoS mainnet](https://chainlist.org/chain/137)
    - [Polygon zkEVM testnet (Cardona)](https://chainlist.org/chain/2442)
    - [Polygon zkEVM mainnet](https://chainlist.org/chain/1101)

2. Select the **Add to Metamask** option on the page. This brings up your MetaMask wallet.

    <center>
    ![chainlist-1](../../../img/tools/wallet/metamask/chainlist-1.png){width=50%}
    </center>

3. Select the **Approve** option. This lets ChainList add the network configuration such as the network RPC URL, the chain ID, etc., to your MetaMask wallet.

    <center>
    ![chainlist-2](../../../img/tools/wallet/metamask/chainlist-2.png){width=50%}
    </center>

4. Finally, select **Switch network** to switch to Amoy testnet in MetaMask.

    <center>
    ![chainlist-3](../../../img/tools/wallet/metamask/chainlist-3.png){width=50%}
    </center>

5. You can now see your MATIC balance on Amoy. You can also switch between Amoy and other networks directly from the drop-down menu in the top-left corner.

    <center>
    ![chainlist-4](../../../img/tools/wallet/metamask/chainlist-4.png){width=50%}
    </center>

## Polygonscan

1. Navigate to the [Polygonscan website](https://polygonscan.com/).
2. Select the network you want to add to your MetaMask wallet from the drop-down list in the top-right corner of the home page.

    <center>
    ![polygonscan-1](../../../img/tools/wallet/metamask/polygonscan-1.png){width=50%}
    </center>

3. The explorer window refreshes and loads the explorer home page for the network you selected.
4. Next, scroll down to the bottom of the page, and select the button in the bottom-left corner prompting you to add the network to your MetaMask wallet. For instance, in the case of Amoy testnet, the button says **Add Polygon Amoy Network**.

    <center>
    ![polygonscan-2](../../../img/tools/wallet/metamask/polygonscan-2.png){width=50%}
    </center>

5. Select **Approve** from the MetaMask window. This allows the explorer to add the network configuration to your wallet.

    <center>
    ![polygonscan-3](../../../img/tools/wallet/metamask/polygonscan-3.png){width=50%}
    </center>

6. Finally, click on **Switch network** to switch to your selected network.

    <center>
    ![polygonscan-4](../../../img/tools/wallet/metamask/polygonscan-4.png){width=50%}
    </center>

7. You can now see your MATIC balance on Amoy. You can also switch between Amoy and other networks directly from the drop-down menu in the top-left corner.

    <center>
    ![polygonscan-5](../../../img/tools/wallet/metamask/chainlist-4.png){width=50%}
    </center>

## Add a network manually

MetaMask gives you the option to add a network profile manually. 

Follow the [MetaMask guide to add a custom network](https://support.metamask.io/networks-and-sidechains/managing-networks/how-to-add-a-custom-network-rpc/). 

The following table contains the mainnet and testnet network configurations for Polygon PoS and zkEVM.

|         Network         |                 RPC URL                  | Chain ID | Native token |             Explorer URL              |
| :---------------------: | :--------------------------------------: | :------: | :----------: | :-----------------------------------: |
|       PoS mainnet       |    https://polygon-mainnet.infura.io     |   137    |    MATIC     |       https://polygonscan.com/        |
|   PoS Amoy (testnet)    |   https://rpc-amoy.polygon.technology    |  80002   |    MATIC     |     https://amoy.polygonscan.com      |
|      zkEVM mainnet      |          https://zkevm-rpc.com           |   1101   |     ETH      |     https://zkevm.polygonscan.com     |
| zkEVM Cardona (testnet) | https://etherscan.cardona.zkevm-rpc.com/ |   2442   |     ETH      | https://cardona-zkevm.polygonscan.com |