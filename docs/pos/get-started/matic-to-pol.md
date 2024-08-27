## Overview

The technical upgrade from MATIC to POL marks a critical juncture for the Polygon networks, enhancing utility and aligning with the vision as an aggregated network of blockchains. 

POL will serve as a hyperproductive token: the native gas and staking token on Polygon PoS, as well as supporting the network's future expansion and security as an aggregated network.

## Steps to migrate to POL

### MATIC tokens on Ethereum

!!! info "Stakers and delegators"

    MATIC stakers don't need to take any action to upgrade from MATIC to POL.

If your MATIC tokens are on Ethereum, you can use [Polygon Portal's migration interface](https://portal.polygon.technology/pol-upgrade) to migrate your MATIC tokens to POL. The process is as follows:

1. Navigate to Polygon Portal's migration interface: https://portal.polygon.technology/pol-upgrade
2. Switch to Ethereum network in your wallet and connect to the Portal UI.
3. Approve the migration action by granting the upgrade contract permission to access your MATIC tokens.
4. Perform the migration action to receive POL in your wallet.

### MATIC tokens on Polygon PoS

If your MATIC tokens are stored in your wallet on the Polygon PoS chain, you won't need to manually migrate them — they'll be automatically converted to POL at a 1:1 ratio.

However, you'll need to update the native token symbol in your wallet's network settings. If the token symbol isn't updated, the wallet may continue to display MATIC as the token name instead of POL.

Here’s how to do this in MetaMask.

1. Within your browser, open your MetaMask wallet in the expanded mode by selecting on the **Expand view** option from the options menu in the top-right corner.

    <center>
    ![change-token-name-1](../../img/pos/change-token-name-1.png){width=50%}
    </center>

2. Select the options menu again from the wallet's expanded view, and then select **Settings** from the drop-down list.

    ![change-token-name-2](../../img/pos/change-token-name-2.png)

3. Select the **Networks** tab from left sidebar to bring up the network settings. Switch to **Polygon Mainnet** if you're currently on another network. The list of configuration options on the right shows the **Currency symbol** which is currently set to **MATIC**.

    ![change-token-name-3](../../img/pos/change-token-name-3.png)

4. Change the **Currency symbol** to **POL**, and select **Save** at the bottom. You can ignore the warning in yellow in this case.

    <center>
    ![change-token-name-4](../../img/pos/change-token-name-4.png){width=50%}
    </center>

The process to change the token symbol may vary depending on the wallet you're using. Please refer to the docs specific to your wallet and follow the outlined steps accordingly.

### MATIC tokens on Polygon zkEVM

If your MATIC tokens are on the zkEVM chain, use [Polygon Portal](https://portal.polygon.technology/bridge) to bridge your tokens to Ethereum, and then follow the steps described in the [MATIC tokens on Ethereum section](#matic-tokens-on-ethereum).

## Read more about POL

1. [Detailed blog post on MATIC to POL migration](https://polygon.technology/blog/save-the-date-matic-pol-migration-coming-september-4th-everything-you-need-to-know)
2. [POL token reference doc](../concepts/tokens/pol.md)



