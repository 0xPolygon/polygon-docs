!!! warning "Third-party content"

    Polygon technical documentation may contain third-party content, including websites, products, and services, that are provided for informational purposes only.

    Polygon Labs does not endorse, warrant, or make any representations regarding the accuracy, quality, reliability, or legality of any third-party websites, products, or services. If you decide to access any third-party content, you do so entirely at your own risk and subject to the terms and conditions of use for such websites. Polygon Labs reserves the right to withdraw such references and links without notice.

    Polygon technical documentation serves as an industry public good and is made available under the [MIT License](https://opensource.org/license/mit/). In addition, please view the official [Polygon Labs Terms of Use](https://polygon.technology/terms-of-use).

SmartPress is an AI tool that crafts custom smart contracts from language prompts.

> For details on the variety of contracts SmartPress can create, check out [SmartPress’s website](https://smartpress.ai).

## Create a Smart Contract using SmartPress

To create a new smart contract with SmartPress, follow these steps:

1. In your browser, navigate to [smartpress.ai](https://smartpress.ai).
2. Enter the specifications for your desired contract.
3. Let SmartPress generate the contract for you; no need for an IDE or code editor.
4. Review the output. If satisfied, proceed to validation and testing. If not, modify your input and repeat the process.

## Deploy your Contract using SmartPress

To deploy your smart contract on Polygon PoS:

1. After creation, connect your wallet and switch your network to either Mumbai testnet or Polygon PoS.
2. Press the 'Deploy' button. If you lack transaction gas, use the provided faucet links to obtain some.

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
