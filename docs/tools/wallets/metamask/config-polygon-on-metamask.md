---
id: config-polygon-on-metamask
title: Add Polygon Network
description: Integrate Polygon with MetaMask by using Polygonscan or adding it manually.
keywords:
  - wiki
  - polygon
  - metamask
  - polygonscan
image: https://wiki.polygon.technology/img/polygon-logo.png
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::caution Content disclaimer

Please view the third-party content disclaimer [<ins>here</ins>](https://github.com/0xPolygon/wiki/blob/master/CONTENT_DISCLAIMER.md).

:::

---

In order to view the flow of funds in your accounts, on the Polygon Network, you will need to configure Polygon testnet and mainnet URLs on Metamask.

There are two ways to do it:
1. [Using Polygonscan](/tools/wallets/metamask/config-polygon-on-metamask.md#polygon-scan)
2. [Add the Polygon network manually](/tools/wallets/metamask/config-polygon-on-metamask.md#add-the-polygon-network-manually)

:::tip
Find a tip at the end of this article on how to easily add **Polygon Mainnet** to Metamask.
:::

### Using Polygonscan

:::note
Please make sure you have already installed <ins>**[Metamask](https://metamask.io/)**</ins>!
:::


<Tabs
  defaultValue="mainnet"
  values={[
    { label: 'PoS Mainnet', value: 'mainnet', },
    { label: 'Mumbai Testnet', value: 'mumbai', },
  ]
}>

<TabItem value="mumbai">

Please follow the steps to add Polygon's Mumbai-Testnet:

1. Navigate to [mumbai.polygonscan.com](https://mumbai.polygonscan.com/)
2. Scroll down to the bottom of the page and click on the button `Add Mumbai Network`

<img src={useBaseUrl("img/metamask/testnet-button.png")} />
<p></p>

3. Once you click the button you will see a MetaMask Notification, now click on **Approve**.

<div align="center">
  <img  src={useBaseUrl("img/metamask/develop/testnet-addnetwork.png")} width="357" height="600" />
</div>
<br></br>

You will be directly switched to Polygon’s Mainnet now in the network dropdown list. You can now close the dialog.

</TabItem>

<TabItem value="mainnet">

Please follow the steps to add Polygon’s Mainnet:

1. Navigate to [polygonscan.com](https://polygonscan.com/)
2. Scroll down to the bottom of the page and click on the button `Add Polygon Network`

<img src={useBaseUrl("img/metamask/mainnet-button.png")} />
<p></p>
<br></br>
<br></br>

3. Once you click the button you will see a MetaMask Notification, now click on **Approve**.
You will be directly switched to Polygon’s Mainnet now in the network dropdown list. You can now close the dialog.

<div align="center">
<img src={useBaseUrl("img/metamask/mainnet-addnetwork.png")} width="357" height="600" />
</div>


</TabItem>

</Tabs>

If you are facing any issue, **add the network manually** according to the steps given below.

### Add the Polygon network manually

<Tabs
  defaultValue="mainnet"
  values={[
    { label: 'PoS Mainnet', value: 'mainnet', },
    { label: 'Mumbai Testnet', value: 'mumbai', },
  ]
}>

<TabItem value="mumbai">
To add Polygon's Mumbai-Testnet, click on the Network selection dropdown and then click on Custom RPC.

<img src={useBaseUrl("img/metamask/select-network.png")} />
<br></br>

It will open up a form with 2 tabs on the top, Settings and Info. In the Settings tab you can add `Matic Mumbai` in the Network Name field, URL `https://rpc-mumbai.maticvigil.com/` in the New RPC URL field, `80001` in Chain ID field, `MATIC` in Currency Symbol field and `https://mumbai.polygonscan.com/` in Block Explorer URL field.
<br></br>

<img src={useBaseUrl("img/metamask/metamask-settings-mumbai.png")} />
<br></br>

Once you’ve added the URL in the New Network field, click on Save. You will be directly switched to Polygon’s Mumbai-Testnet now in the network dropdown list. You can now close the dialog.
</TabItem>

<TabItem value="mainnet">
To add Polygon’s Mainnet, click on the Network selection dropdown and then click on Custom RPC.

<img src={useBaseUrl("img/metamask/select-network.png")} />

It will open up a form with 2 tabs on the top, Settings and Info. In the Settings tab you can add `Polygon Mainnet` in the Network Name field, URL `https://polygon-rpc.com/` in the New RPC URL field, `137` in Chain ID field, `MATIC` in Currency Symbol field and `https://polygonscan.com/` in Block Explorer URL field.

<img src={useBaseUrl("img/metamask/metamask-settings-mainnet.png")} />
<br></br>
<br></br>

Once you’ve added the information click on Save. You will be directly switched to Polygon’s Mainnet now in the network dropdown list. You can now close the dialog.
</TabItem>
</Tabs>

**You have successfully added Polygon Network to your Metamask!**

:::tip Easy way to add Polygon mainnet
If you just need to add Polygon Mainnet, you can follow these steps:

1. On Metamask, select the Network tab:
<div align="center">
<img src={useBaseUrl("img/metamask/add-polygon-mainnet.png")} width="400"/>
</div>

2. Click on **Add Network**:
<div align="center">
<img src={useBaseUrl("img/metamask/add-polygon-mainnet-2.png")} width="400" />
</div>

3.  Find Polygon Mainnet on the list of available networks:
<div align="center">
<img src={useBaseUrl("img/metamask/add-polygon-mainnet-3.png")} width="800" />
</div>

4. Approve the network addition:
<div align="center">
<img src={useBaseUrl("img/metamask/add-polygon-mainnet-4.png")} width="400" />
</div>

Now you may see the Polygon Mainnet on the Networks tab:
<div align="center">
<img src={useBaseUrl("img/metamask/add-polygon-mainnet-5.png")} width="400" />
</div>

:::