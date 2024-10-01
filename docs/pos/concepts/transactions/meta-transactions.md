
## The current state of transacting

The traditional transaction model on Ethereum and similar blockchains has notable limitations. One key issue is that users must pay gas fees to initiate transactions, which can be a barrier, as they often need to acquire cryptocurrency first.

To address this, the transaction sender can be decoupled from the gas payer. This allows for scaling transaction execution and creating a more seamless user experience. 

By implementing middleware through a third party, gas payments can be handled separately. This is where meta transactions come in.

## What are meta transactions?

Meta transactions enable users to interact with the blockchain without needing tokens to cover transaction fees. This is achieved by decoupling the transaction sender from the gas payer.

In this model, the executor submits a transaction request by signing the intended action with their private key, rather than paying gas directly. The meta transaction consists of a standard Ethereum transaction augmented with additional parameters.

The signed transaction parameters are sent to a secondary network acting as a relayer. Relayers validate transactions based on relevance to the dApp, then wrap the request into a standard transaction, paying the gas fee. The network broadcasts this transaction, and the contract unwraps it by validating the original signature, executing the action on behalf of the user.

!!! info "Meta transactions vs. batch transactions"

    To clarify: a meta transaction is different from a batch transaction, where a batch transaction is a transaction that can send multiple transactions at once and are then executed from a single sender (single nonce specified) in sequence.

In summary, meta transactions are a design pattern where:

- A user (sender) signs a request with their private key and sends it to a relayer
- The relayer wraps the request into a transaction and sends it to a contract
- The contract unwraps the transaction and executes it

Native transactions imply that the *sender* is also the *payer*. When taking the *payer* away from
the *sender*, the *sender* becomes more like an *intender* - the sender shows the intent of the transaction they would like executed on the blockchain by signing a message containing specific parameters related to their message, and not an entirely constructed transaction.

## Use cases

One can imagine the capabilities of meta transactions for scaling dApps and interactions with smart contracts. Not only can a user create a gasless transaction, but they can also do so many times, and with an automation tool, meta transactions can influence the next wave of applications for practical use cases. Meta transactions enable real utility in smart contract logic, which is often limited because of gas fees and the interactions required on-chain.

Let's look at a few scenarios highlighting how meta transactions can enhance user experience in dApps.

### Voting

A user wishing to participate in on-chain governance can vote through a voting contract by signing a message with their decision. Traditionally, they would need to pay gas fees and know how to interact with the contract directly. But in this case they sign a meta transaction containing the vote details off-chain and send it to a relayer. 

The relayer receives the signed message, validates the priority of the vote, wraps it into a standard transaction, pays the gas fees, and submits it to the voting contract. Once validated, the contract executes the vote on behalf of the user.

### Gaming

In blockchain-based games, players often need to pay gas fees to perform in-game actions like trading items or upgrading characters. By using meta transactions, players can interact with the game without needing to hold ETH, making it easier for casual gamers to enjoy the experience without the hassle of managing crypto.

### Minting NFTs

In NFT marketplaces, users often face high gas fees when minting, buying, or selling NFTs. By utilizing meta transactions, users can create or purchase NFTs without having to manage Ether for gas. They simply sign the transaction request, and a relayer submits it on their behalf, enhancing user experience and lowering the barrier to entry for those unfamiliar with handling cryptocurrencies.

## Try 'em out

Assuming your familiarity with the different approaches you can take to integrate meta transactions in your dApp, and depending on whether you're migrating to meta transactions or building fresh dApp on using it.

To integrate your dApp with meta transactions on Polygon PoS, you can choose to go with one of the following relayers or spin up a custom solution:

- [Biconomy](https://docs.biconomy.io/quickstart)
- [Gas Station Network (GSN)](https://docs.opengsn.org/#ethereum-gas-station-network-gsn)
- [Infura](https://infura.io/product/ethereum/transactions-itx)
- [Gelato](https://docs.gelato.network/developer-products/gelato-relay-sdk)

## Goal

Execute transactions on Polygon PoS without changing provider on MetaMask (this tutorial caters to MetaMask's in-page provider, can be modified to execute transactions from any other provider)

Under the hood, user signs on an intent to execute a transaction, which is relayed by a simple relayer to execute it on a contract deployed on Polygon chain.

## What is enabling transaction execution?

The client that the user interacts with (web browser, mobile apps, etc.) never interacts with the blockchain, instead it interacts with a simple relayer server (or a network of relayers), similar to the way GSN or any meta-transaction solution works.

For any action that requires blockchain interaction,

- Client requests an EIP-712 formatted signature from the user
- The signature is sent to a simple relayer server (should have a simple auth/spam protection if used for production, or Biconomy's Mexa SDK can be used: [https://github.com/bcnmy/mexa-sdk](https://github.com/bcnmy/mexa-sdk))
- The relayer interacts with the blockchain to submit user's signature to the contract. A function on the contract called `executeMetaTransaction` processes the signature and executes the requested transaction (via an internal call).
- The relayer pays for the gas making the transaction effectively free 🤑

## Example implementation

- Choose between a custom simple relayer node/Biconomy.

  - For Biconomy, setup a dApp from the dashboard and save the `api-id` and `api-key`, see: [https://docs.biconomy.io/](https://docs.biconomy.io/)

    Steps:

    1. Let's register our contracts to Biconomy dashboard
       1. Visit [Biconomy's offical docs](https://docs.biconomy.io/dashboard).
       2. Navigate and login to the Dashboard.
       3. Select **Polygon Amoy Testnet** when registering your dApp.
    2. Copy the API key to use for you dApp's frontend.
    3. And add function `executeMetaTransaction` in **Manage-Api** and make sure to enable meta-tx (Check **native-metatx** option).

  - If you'd like to use your own custom API that sends signed transactions on the blockchain, you can refer to the server code here: [https://github.com/angelagilhotra/ETHOnline-Workshop/tree/master/2-network-agnostic-transfer](https://github.com/angelagilhotra/ETHOnline-Workshop/tree/master/2-network-agnostic-transfer)

- Make sure that the contract you'd like to interact with inherits from `NativeMetaTransactions` - 👀 peep into `executeMetaTransaction` function in the contract.
- Link: [https://github.com/maticnetwork/pos-portal/blob/34be03cfd227c25b49c5791ffba6a4ffc9b76036/flat/ChildERC20.sol#L1338](https://github.com/maticnetwork/pos-portal/blob/34be03cfd227c25b49c5791ffba6a4ffc9b76036/flat/ChildERC20.sol#L1338)

```jsx

let data = await web3.eth.abi.encodeFunctionCall({
    name: 'getNonce',
    type: 'function',
    inputs: [{
        name: "user",
        type: "address"
      }]
  }, [accounts[0]]);

  let _nonce = await web3.eth.call ({
    to: token["80001"],
    data
  });

  const dataToSign = getTypedData({
    name: token["name"],
    version: '1',
    salt: '0x0000000000000000000000000000000000000000000000000000000000013881',
    verifyingContract: token["80001"],
    nonce: parseInt(_nonce),
    from: accounts[0],
    functionSignature: functionSig
  });

  const msgParams = [accounts[0], JSON.stringify(dataToSign)];

  let sig = await eth.request ({
    method: 'eth_signTypedData_v3',
    params: msgParams
  });

```

- Once you have a relayer and the contracts set up, what is required is for the client to be able to fetch an EIP-712 formatted signature and simply call the API with the required parameters

ref: [https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/sign.js#L47](https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/sign.js#L47)

```jsx

let data = await web3.eth.abi.encodeFunctionCall({
    name: 'getNonce',
    type: 'function',
    inputs: [{
        name: "user",
        type: "address"
      }]
  }, [accounts[0]]);

  let _nonce = await web3.eth.call ({
    to: token["80001"],
    data
  });

  const dataToSign = getTypedData({
    name: token["name"],
    version: '1',
    salt: '0x0000000000000000000000000000000000000000000000000000000000013881',
    verifyingContract: token["80001"],
    nonce: parseInt(_nonce),
    from: accounts[0],
    functionSignature: functionSig
  });
  const msgParams = [accounts[0], JSON.stringify(dataToSign)];

  let sig = await eth.request ({
    method: 'eth_signTypedData_v3',
    params: msgParams
  });
```

Calling the API, ref: [https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/sign.js#L110](https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/sign.js#L110)

```jsx
const response = await request.post(
    'http://localhost:3000/exec', {
      json: txObj,
    },
    (error, res, body) => {
      if (error) {
        console.error(error)
        return
      }
      document.getElementById(el).innerHTML =
      `response:`+ JSON.stringify(body)
    }
  )
```

If using Biconomy, the following should be called:

```jsx
const response = await request.post(
    'https://api.biconomy.io/api/v2/meta-tx/native', {
      json: txObj,
    },
    (error, res, body) => {
      if (error) {
        console.error(error)
        return
      }
      document.getElementById(el).innerHTML =
      `response:`+ JSON.stringify(body)
    }
  )
```

where the `txObj` should look something like:

```json
{
    "to": "0x2395d740789d8C27C139C62d1aF786c77c9a1Ef1",
    "apiId": <API ID COPIED FROM THE API PAGE>,
    "params": [
        "0x2173fdd5427c99357ba0dd5e34c964b08079a695",
        "0x2e1a7d4d000000000000000000000000000000000000000000000000000000000000000a",
        "0x42da8b5ac3f1c5c35c3eb38d639a780ec973744f11ff75b81bbf916300411602",
        "0x32bf1451a3e999b57822bc1a9b8bfdfeb0da59aa330c247e4befafa997a11de9",
        "27"
    ],
    "from": "0x2173fdd5427c99357ba0dd5e34c964b08079a695"
}
```

- If you use the custom API, it executes the `executeMetaTransaction` function on the contract:

(ref: [https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/server/index.js#L40](https://github.com/angelagilhotra/ETHOnline-Workshop/blob/6b615b8a4ef00553c17729c721572529303c8e1b/2-network-agnostic-transfer/server/index.js#L40))

```jsx
try {
    let tx = await contract.methods.executeMetaTransaction(
      txDetails.from, txDetails.fnSig, r, s, v
    ).send ({
      from: user,
      gas: 800000
    })
    req.txHash = tx.transactionHash
  } catch (err) {
    console.log (err)
    next(err)
  }
```

is using biconomy, the client side call looks like:

```jsx
// client/src/App.js
import React from "react";
import Biconomy from "@biconomy/mexa";

const getWeb3 = new Web3(biconomy);
biconomy
    .onEvent(biconomy.READY, () => {
      // Initialize your dapp here like getting user accounts etc
      console.log("Mexa is Ready");
    })
    .onEvent(biconomy.ERROR, (error, message) => {
      // Handle error while initializing mexa
    console.error(error);
    });

/**
* use the getWeb3 object to define a contract and calling the function directly
*/

```