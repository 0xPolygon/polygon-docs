---
id: smartpress
title: How to Deploy a Smart Contract Using SmartPress
sidebar_label: Using SmartPress
description: "Learn how to deploy smart contracts on Polygon PoS using SmartPress."
keywords:
  - docs
  - matic
  - polygon
  - smartpress
  - ai
  - create smart contract
  - deploy on polygon
image: https://wiki.polygon.technology/img/polygon-logo.png
---

:::caution Content disclaimer

Please view the third-party content disclaimer [<ins>here</ins>](https://github.com/0xPolygon/wiki/blob/master/CONTENT_DISCLAIMER.md).

:::

SmartPress is an AI tool that crafts custom smart contracts from language prompts.

> For details on the variety of contracts SmartPress can create, check out [SmartPress’s website](https://smartpress.ai).

## Create a Smart Contract using SmartPress

To create a new smart contract with SmartPress, follow these steps:

1. In your browser, navigate to [smartpress.ai](smartpress.ai).
2. Enter the specifications for your desired contract.
3. Let SmartPress generate the contract for you; no need for an IDE or code editor.
4. Review the output. If satisfied, proceed to validation and testing. If not, modify your input and repeat the process.

![Screenshot 2023-08-15 at 12 33 59 pm](https://github.com/crokau/wiki/assets/71380821/c43ccb48-3b1b-4cad-814b-8eddc0f735c1)

## Deploy your Contract using SmartPress

To deploy your smart contract on Polygon PoS:

1. After creation, connect your wallet and switch your network to either Mumbai testnet or Polygon PoS.
2. Press the 'Deploy' button. If you lack transaction gas, use the provided faucet links to obtain some.

![Screenshot 2023-08-15 at 12 37 39 pm](https://github.com/crokau/wiki/assets/71380821/ea20889b-1b5e-44b7-ba9c-f208abf1e944)

## Verify the Contract


To verify your new contract, follow these steps:

1. Start by clicking on 'View Code' and copy the flattened version of your code to the clipboard.
2. In your preferred block explorer, navigate to the verification screen (typically found under 'contracts/code').
3. Select single file (flattened).
4. Select the compiler version as indicated on the deployment page.
5. Set the optimizer to 'TRUE' and runs to '200'.
6. Choose your preferred licence.
7. Paste the flattened code in the code box.
8. Verification will complete.

## Need help?

If you have any questions or encounter any issues during the process, **please reach out to the [official SmartPress support](contact@smartpress.ai)**.
