---
id: network-agnostics
title: Network Agnostic Transactions
sidebar_label: Network Agnostic Transactions
description: "Integrate Network Agnostic Transactions in your dApp."
keywords:
  - docs
  - matic
image: https://matic.network/banners/matic-network-16x9.png
---

## Goal

Execute transactions on Polygon chain, without changing provider on MetaMask (this tutorial caters to metamask's inpage provider, can be modified to execute transactions from any other provider)

Under the hood, user signs on an intent to execute a transaction, which is relayed by a simple relayer to execute it on a contract deployed on Polygon chain.


## What is enabling transaction execution?

The client that the user interacts with (web browser, mobile apps, etc) never interacts with the blockchain, instead it interacts with a simple relayer server (or a network of relayers), similar to the way GSN or any meta-transaction solution works ( see: [Meta Transactions: An Introduction](https://www.notion.so/Meta-Transactions-An-Introduction-8f54cf75321e4ec3b6d755e18e406590)).

For any action that requires blockchain interaction,

- Client requests an EIP712 formatted signature from the user
- The signature is sent to a simple relayer server (should have a simple auth/spam protection if used for production, or biconomy's mexa sdk can be used: [https://github.com/bcnmy/mexa-sdk](https://github.com/bcnmy/mexa-sdk))
- The relayer interacts with the blockchain to submit user's signature to the contract. A function on the contract called `executeMetaTransaction` processes the signature and executes the requested transaction (via an internal call).
- The relayer pays for the gas making the transaction effectively free 🤑

## Integrate Network Agnostic Transactions in your dApp

- Choose between a custom simple relayer node/biconomy.

  - For biconomy, setup a dapp from the dashboard and save the api-id and api-key, see: [Tutorial: Biconomy](https://www.notion.so/Tutorial-Biconomy-7f578bfb4e7d4904b8c79522085ba568) or [https://docs.biconomy.io/](https://docs.biconomy.io/)

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
