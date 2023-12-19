Daily smart contract calls are at their highest, hitting around 2.5 to 3 million per day.
DApps are starting to realize their utility but are becoming victims of their success or others’
success due to gas fees. Not to mention, the onboarding hurdles of users and the challenges of current
UX are no easy fix.

## Servicing Smart Contracts

By design, smart contracts are deterministic state machines that execute when transaction fees are
paid to service the contract’s logic by using the network’s computational resources.
This is accomplished by a gas-metered model on Ethereum (and Polygon).

## The Current State of Transacting

There are limitations to this traditional transaction model on Ethereum (and other blockchains alike).
A common limitation is a user not having the means to pay for gas. By default, the sender of the
transaction acts as the payer, as these behaviors are coupled, so if a user attempts to create and send
a transaction, they are responsible for the associated gas fees. Likewise, if a user builds, interacts
with, or runs a dApp, the user is required to pay gas.

It is unrealistic to expect the average user to buy crypto and pay for gas to interact with an
application. What can be done to address this is to decouple the sender of a transaction from acting
as a payer, enabling the opportunity to scale transaction execution and initiate a seamless transacting
experience.

Instead of direct transaction execution, a middleware would exist (via a third party) to handle the gas.
This is where meta transactions come in.

## What are Meta Transactions?

Meta transactions allow anyone to interact with the blockchain. They do not require users to have
tokens to pay for the network’s services through transaction fees. This is done by decoupling the
sender of a transaction and the payer of gas.

A solution that can onboard new users and helps current ones.

The executor of a transaction acts as a sender. Rather than spending gas, they only create a
transaction request by signing their intended action (the transaction parameters) with their private
key. The meta transaction is a regular Ethereum transaction that includes additional parameters to craft
the meta transaction.

The signed transaction parameters are passed onto a secondary network, which acts as a relayer.
While there are different schemes for this, relayers would generally choose which transactions are worth
submitting by validating the transaction (e.g., being relevant to the dApp). Upon validation, the relayer
will wrap the request (the signed message) into an actual transaction (which means paying the gas fee)
and broadcast it to the network, where the contract unwraps the transaction by validating the original
signature and executes it on behalf of the user.

!!! note "The words meta and batch may be analogous to some"

    To clarify: a meta transaction is different from a batch transaction, where a batch transaction is a transaction that can send multiple transactions at once and are then executed from a single sender (single nonce specified) in sequence.

In summary, meta transactions are a design pattern where:

- A user (sender) signs a request with their private key and sends it to a relayer
- The relayer wraps the request into a tx and sends it to a contract
- The contract unwraps the tx and executes it

Native transactions imply that the “sender” is also the “payer”. When taking the “payer” away from
the “sender”, the “sender” becomes more like an “intender” - the sender shows the intent of the transaction
they would like executed on the blockchain by signing a message containing specific parameters related to
their message, and not an entirely constructed transaction.

## Use Cases

One can imagine the capabilities of meta transactions for scaling dApps and interactions with smart contracts.
Not only can a user create a gasless transaction, but they can also do so many times, and with an automation
tool, meta transactions can influence the next wave of applications for practical use cases. Meta transactions
enable real utility in smart contract logic, which is often limited because of gas fees and the interactions
required on-chain.

### Example with voting

A user wants to participate in on-chain governance, and they intend to vote for a particular outcome via a
voting contract. The user would sign a message which states the user’s decision in a vote in this particular
contract. Traditionally, they would need to pay a gas fee for interacting with the contract (and know how to
interact with the contract), but instead, they can sign a meta transaction (off-chain) with the necessary
information for their vote and pass it to a relayer which would execute the transaction on their behalf.

The signed message gets sent to a relayer (the signed tx params about the voting information). The relayer
validates that this transaction is a priority vote, wraps the voting request into an actual transaction,
pays the gas fees, and broadcasts it to the voting contract. Everything checks out on the voting contract’s
end, and the vote executes on behalf of the user.

## Try Them Out

Assuming your familiarity with the different approaches you can take to integrate meta transactions in your
dApp, and depending on whether you're migrating to meta transactions or building fresh dApp on using it.

To integrate your dApp with Meta Transactions on Polygon, you can choose to go with one of the following
relayers or spin up a custom solution:

- [Biconomy](https://docs.biconomy.io/products/enable-gasless-transactions)
- [Gas Station Network (GSN)](https://docs.opengsn.org/#ethereum-gas-station-network-gsn)
- [Infura](https://infura.io/product/ethereum/transactions-itx)
- [Gelato](https://docs.gelato.network/developer-products/gelato-relay-sdk)

## Goal

Execute transactions on Polygon chain, without changing provider on MetaMask (this tutorial caters to metamask's inpage provider, can be modified to execute transactions from any other provider)

Under the hood, user signs on an intent to execute a transaction, which is relayed by a simple relayer to execute it on a contract deployed on Polygon chain.

## What is enabling transaction execution?

The client that the user interacts with (web browser, mobile apps, etc) never interacts with the blockchain, instead it interacts with a simple relayer server (or a network of relayers), similar to the way GSN or any meta-transaction solution works.

For any action that requires blockchain interaction,

- Client requests an EIP712 formatted signature from the user
- The signature is sent to a simple relayer server (should have a simple auth/spam protection if used for production, or biconomy's mexa sdk can be used: [https://github.com/bcnmy/mexa-sdk](https://github.com/bcnmy/mexa-sdk))
- The relayer interacts with the blockchain to submit user's signature to the contract. A function on the contract called `executeMetaTransaction` processes the signature and executes the requested transaction (via an internal call).
- The relayer pays for the gas making the transaction effectively free 🤑

## Integrate Network Agnostic Transactions in your dApp

- Choose between a custom simple relayer node/biconomy.

  - For biconomy, setup a dapp from the dashboard and save the api-id and api-key, see: [https://docs.biconomy.io/](https://docs.biconomy.io/)

    **Steps:**

    1. Let's Register our contracts to biconomy dashboard
       1. Visit the [official documents of biconomy](https://docs.biconomy.io/biconomy-dashboard).
       2. While registering the dapp, select `Polygon Mumbai`
    2. Copy the`API key` to use in frontend
    3. And Add function `executeMetaTransaction` in Manage-Api and make sure to enable meta-tx. (Check 'native-metatx' option)

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

- Once you have a relayer and the contracts setup, what is required is for the client to be able to fetch an EIP712 formatted signature and simply call the API with the required parameters

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

- If you use the custom API it executes the `executeMetaTransaction` function on the contract:

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

Account Abstraction is a blockchain technology that enables users to utilize smart contracts as their accounts. While the default account for most users is an Externally Owned Account (EOA), which is controlled by an external private key, it requires users to have a considerable understanding of blockchain technology to use them securely. Fortunately, smart contract accounts can create superior user experiences.

## Benefits

Contract accounts offer numerous benefits, including:

- **Arbitrary verification logic:** Rather than use an external private key, contract accounts can use any arbitrary signature type. This feature supports single and multi-signature verification and any signature scheme.
- **Sponsored transactions:** Users can pay transaction fees in ERC-20 tokens or create their fee logic, including sponsoring transaction fees on their app.
- **Account security:** Contract accounts enable social recovery and security features such as time-locks and withdraw limits.
- **Atomic multi-operations:** Users can perform multiple operations simultaneously, such as trading in a single click instead of approving and swapping separately.

## Using Account Abstraction on Polygon

There are two primary ways users can use account abstraction on Polygon: by sending ERC-4337 transactions or with third party meta transaction services.

### ERC-4337

ERC-4337, also known is EIP-4337, brings account abstraction to the Polygon ecosystem and all EVM-compatible chains.

### Meta Transactions

Meta transactions are bespoke third party services for achieving account abstraction.
