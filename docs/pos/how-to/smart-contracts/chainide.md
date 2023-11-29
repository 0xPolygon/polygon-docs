!!! warning "Third-party content"

    Polygon technical documentation may contain third-party content, including websites, products, and services, that are provided for informational purposes only.

    Polygon Labs does not endorse, warrant, or make any representations regarding the accuracy, quality, reliability, or legality of any third-party websites, products, or services. If you decide to access any third-party content, you do so entirely at your own risk and subject to the terms and conditions of use for such websites. Polygon Labs reserves the right to withdraw such references and links without notice.

    Polygon technical documentation serves as an industry public good and is made available under the [MIT License](https://opensource.org/license/mit/). In addition, please view the official [Polygon Labs Terms of Use](https://polygon.technology/terms-of-use).

[ChainIDE](https://chainide.com/) is a chain agnostic, cloud-based IDE for creating decentralized applications. It enhances development cycle through pre-configured plugins that save users' time and effort. This is a beginner guide on creating and deploying a simple ERC-721 smart contract on the Polygon Mumbai Testnet.

## Prerequisites

1. ChainIDE
2. MetaMask
3. Solidity

## What you will do

The following are general steps for deploying an ERC-721 smart contract:

1. Set up a wallet
2. Write down an ERC-721 smart contract
3. Compile an ERC-721 Smart Contract
4. Deploy an ERC-721 Smart Contract
5. Create a Flattened File using Flattener Library
6. Verify a Smart Contract
7. NFT Minting

## Setting up a Wallet

### Install MetaMask

A gas fee must be paid when deploying a smart contract on the blockchain or making a transaction to a deployed smart contract, and we must do so using a crypto wallet, such as MetaMask. To download MetaMask, click [here](https://metamask.io/).

### Adding the Mumbai testnet

After installing MetaMask, you need to add the Polygon Mumbai Testnet to MetaMask. In order to add Mumbai Testnet, check out the configuration guide for [MetaMask](https://docs.polygon.technology/docs/tools/wallets/metamask/config-polygon-on-metamask).

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
  <img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image.png" />
</div>

### Obtaining MATIC tokens on Testnet

After adding the Mumbai testnet on MetaMask, visit the [Polygon Faucet](https://faucet.polygon.technology/) to request testnet tokens. These tokens are required to pay gas fees in order to deploy and interact with the smart contract. On the faucet page, select **Mumbai** as the network, **MATIC** as the token, and paste your MetaMask wallet address. Then, click **Submit** and the faucet will send you some test MATIC within a minute.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/Polygon_PR_get_tokens.png" width="100%" height="100%" />

## Write an ERC-721 Smart Contract

You need to write down all the required functions that you want to implement in your ERC-721 smart contract. A general ERC-721 smart contract has the following functions:

- `balanceOf()`: returns the number of NFTs held by the owner.
- `ownerOf()`: returns the address of the token holder.
- `approve()`: approves the permission to transfer tokens on the owner’s behalf. Approval event needs to be triggered after the method is successful.
- `setApprovalForAll()`: Sets the approval of a given operator, and the `approvalforall` event needs to be triggered after success.
- `getApproved()` : Get the approved address for a single NFT.
- `isApprovedForAll()`: Query if an address is an authorized operator for another address.
- `safeTransferFrom()`: To transfer the ownership of an NFT, a successful transfer operation must initiate a transfer event.
- `transferFrom()`: Used to transfer NFTs. After the method succeeds, it needs to trigger the transfer event. The caller confirms he can receive NFT normally, otherwise, this NFT will be lost. When this function is implemented, it needs to check whether it meets the judgment conditions.

The ChainIDE team has prepared a complete ERC-721 template contract that includes all the required functions; you may use this built-in template and add/delete functions according to your requirements.

Visit the [ChainIDE site](https://chainide.com/) and click on **Try Now**.

<img src="https://3869740696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MYy-lqJKjq1m0yBAX4r%2Fuploads%2Fnpdf7fg51675wYmFcL6b%2Fimage.png?alt=media&token=353fc876-a319-49cb-92d5-1ed23c39aa90" width="100%" height="100%" />

Then, click on **New Project** and select **Polygon**. You will be presented with a list of available public templates. Select **ERC721 Showcase**.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/Using+ChainIDE+polygon/select+polygon+showcase.png" width="100%" height="100%" />

Now, you can see the template contract, `Creature.sol`, that includes all the required functions.

After creating the project, click on the **Unconnected** button in the upper right corner, select the **Injected Web3 Provider** button, and then click on MetaMask to connect your wallet (Polygon Mainnet is the main network, and Mumbai is the test network - connect to Mumbai).

<img src="https://d3gvnlbntpm4ho.cloudfront.net/Using+ChainIDE+polygon/connect+mumbai.png" width="100%" height="100%" />

## Compile an ERC-721 Smart Contract

After you have completed your smart contract, it is time to compile it. To compile, navigate to "compile the module", choose an appropriate compiler according to your source code, and press the "compile" button. An ABI and bytecode for the source code are generated upon successful compilation. If there are any errors in your source code, they will be displayed in the "Logger module" under the output panel. You may need to carefully read the error, resolve it, and recompile the contract.

!!! note

    Note down the **compiler version** and the **license** for your source code. It would be needed when you **Verify** your smart contract on the **Polygon Mumbai Testnet**.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(1).png" width="100%" height="100%" />

## Deploy an ERC-721 Smart Contract

After successful compilation, it's time to deploy your compiled ERC-721 smart contract to the Polygon Mumbai Testnet. Before you deploy, you need to have MetaMask installed, the Mumbai test network added to your wallet, and some testnet MATIC tokens to pay for the transaction fees.

Navigate to the **Deploy & Interaction** module and choose among the compiled smart contract. Select the smart contract you want to deploy and click the **Deploy** button. For this tutorial, the `GameItem` smart contract will be deployed.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(2).png" width="100%" height="100%" />

### Check Functions from the Deployed Contract

After successful deployment, an output message should state that your smart contract was deployed successfully. You can now verify the deployed contract. All the functions in the deployed smart contract can be seen in the **INTERACT** panel.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(3).png" width="100%" height="100%" />

## Create a Flattened File using Flattener Library

To verify a smart contract that imports other smart contracts, we need to create a flattened file. A flattened file includes all the source codes of imported contracts in a single file. To create a flattened file, you need to add a **Flattener** plug-in.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(7).png" width="100%" height="100%" />

Once the **Flattener** plug-in is activated, you'll be able to access it as a separate module as shown in the figure below. Choose the compiled file, and click on the **Flatten** button to create a flattened file. Once the flattened file is created, it will be automatically copied to the clipboard. You may paste it into a file and save it for later usage.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(8).png" width="100%" height="100%" />

If you want to save the flattened file, click the **Save** button, and a flattened file will be saved in the current repository.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(9).png" width="100%" height="100%" />

The saved flattened file can be accessed under the explorer module.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(10).png" width="100%" height="100%" />

## Verify a Smart Contract

To verify a smart contract, you need to visit [Mumbai Polygonscan](https://mumbai.polygonscan.com/), and search for the deployed smart contract using the contract address.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(11).png" width="100%" height="100%" />

Click on the **Verify and Publish** link shown under the contract section.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(12).png" width="100%" height="100%" />

Once you click on the verify and publish link, you will be asked for the following:

- Contract Address: The address of a deployed smart contract that you want to verify
- Compiler Type: Either you want to verify a single file or multiple files
- Compiler Version: The compiler version that you used to compile the smart contract
- License: Open-source license type that you used for your source code

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(13).png" width="100%" height="100%" />

After that, you need to paste the flattened file that you created in step 5, and your smart contract will be verified.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(14).png" width="100%" height="100%" />

If there are no issues with your smart contract, it would be verified, and you'll be able to see an image similar to the one that is shown below.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(15).png" width="100%" height="100%" />

## Minting NFT

To mint an NFT, you need to use the **Award Item** function, the wallet address of someone to whom you want to award an NFT, and the link of the photo uploaded to IPFS to be pasted in the token URL input field.

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(4).png" width="100%" height="100%" />

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(5).png" width="100%" height="100%" />

After successful minting, you can check the minted NFT on the OpenSea NFT marketplace. Visit [OpenSea Testnet](https://testnets.opensea.io/), connect your MetaMask wallet and make sure the selected network is Polygon Mumbai Testnet, and you'll be able to see and trade the minted NFT on the OpenSea NFT marketplace.

**Congratulations! You have successfully minted an NFT on Polygon using ChainIDE.**

<img src="https://d3gvnlbntpm4ho.cloudfront.net/ERC+721+Deployment+on++Mumbai/image+(6).png" width="100%" height="100%" />
