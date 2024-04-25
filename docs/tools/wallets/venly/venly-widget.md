# Venly Widget

Venly Widget is a JavaScript SDK created to streamline everyday blockchain tasks. Its purpose is to enable functionalities otherwise restricted due to security implications, such as creating signatures. By encapsulating Venly's extensive capabilities within a user-friendly JavaScript layer, Venly Widget empowers developers and simplifies the development process.

!!! tip "Please note"
    If you are new to Web3 and don't have experience with blockchain technologies, we recommend you use the Venly Widget natively for a better developer experience.

## Create Polygon wallets with Venly Widget

Venly Wallet allows you to create and manage wallets on the Polygon network. You can send and receive MATIC, Polygon NFTs, and ERC20 tokens. Apart from this, the Venly Wallet also supports:

- Multiple blockchains.
- Native token swap functionality.
- Signing messages (including EIP712 message).
- Calling smart contracts.
- Importing wallets.

## Look and feel

As the Widget is a product that incorporates a user interface (UI), let's look at how some of the more regular flows would appear for an end user.

### NFT transfer

The application prompts users to transfer an NFT from their wallet to a different destination in this flow.

![Polygon NFT transfer](https://github.com/0xPolygon/polygon-docs/assets/139292301/da696d64-9dbc-4a1c-9527-ae91bfd19cb0)

### Token transfer

The application prompts the user to transfer a token from their wallet to a different destination in this flow.

![MATIC token transfer](https://github.com/0xPolygon/polygon-docs/assets/139292301/ae45b544-8ee3-4cfc-94f6-0cc430658f98)

## Integration options

Multiple integration options are available to incorporate the Venly Widget into your application. Here is a brief overview of some of these options:

1. [Native integration with Venly SDK](https://docs.venly.io/docs/widget-overview): This approach involves utilizing the Venly SDK directly within your application's codebase. It allows you to access the full functionality of the Venly Widget and customize its behavior according to your requirements.
2. [Ethers.js integration](https://docs.venly.io/docs/ethersjs): You can integrate the Venly Widget with your application using the popular Ethers.js library. This involves utilizing the Ethers.js API to interact with the Venly Widget and manage user wallets, transactions, and other blockchain-related operations.
3. [Web3Modal integration](https://docs.venly.io/docs/web3modal-walletconnect) (WalletConnect): Web3Modal is a library that simplifies connecting to different wallet providers using standard protocols like WalletConnect. Integrating Web3Modal and WalletConnect enables users to interact with the Venly Widget and connect their wallets to your application seamlessly.

These are just a few integration options to incorporate the Venly Widget into your application. The choice of integration method depends on your specific requirements, preferences, and the existing infrastructure of your application.

![Venly widget integration options](https://github.com/0xPolygon/polygon-docs/assets/139292301/edcbb6b1-b17c-424f-bfa9-c8448cc8e441)

## When to choose what?

If you want to build your wallet app for users to interact with, you should use the [Wallet API](https://venly.readme.io/docs/overview).

If you want to integrate an existing and complete wallet solution, you can use the Venly Widget.  
There are multiple ways to integrate it - natively or by using another library (which also uses the Venly Widget in the background):

![Decision making flowchart for web3modal and widget](https://github.com/0xPolygon/polygon-docs/assets/139292301/7a6a6f02-10d9-48d3-83db-250d86406fff)

| Integration type | Description | UI flexibility | Blockchains |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------- |
| **Native**       | A JavaScript SDK that seamlessly integrates with various API functionalities, empowering users to execute diverse blockchain operations effortlessly.           | The Widget delivers pre-designed screens tailored explicitly for end users, offering a ready-to-use solution. These screens are not customizable, ensuring consistency and simplicity in the user experience. | All supported chains |
| **Ethers.js**    | A JavaScript library is used to interact with the EVM blockchains. It provides a wide range of functionality for developers to build decentralized applications | This integration ensures that the Widget is invoked when needed, allowing users to conveniently and securely perform the required actions within the context of your application.                             | Only EVM chains      |
| **Wagmi**        | A collection of React Hooks containing everything to work with EVMs.                                                                                            | This integration ensures that the Widget is invoked when needed, allowing users to conveniently and securely perform the required actions within the context of your application.                             | Only EVM chains      |
| **Web3-React**   | A JavaScript SDK based on ethers.js.                                                                                                                            | This integration ensures that the Widget is invoked when needed, allowing users to conveniently and securely perform the required actions within the context of your application.                             | Only EVM chains      |
| **Web3Modal**    | Web3Modal is a library that simplifies the process of connecting to different wallet providers using standard protocols like WalletConnect                      | When users opt to log in with Venly, the modal will initiate the Venly Widget upon various user actions, facilitating seamless integration between your application and the Venly platform.                   | Only EVM chains      |

!!! success 
    Ready to try out the Venly Widget? [Click here to read the getting started guide](https://docs.venly.io/docs/widget-getting-started).
