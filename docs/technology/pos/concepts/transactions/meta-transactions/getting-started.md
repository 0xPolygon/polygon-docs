---
id: meta-transactions
title: Meta Transactions
sidebar_label: Meta Transactions
description: Learn about meta transactions and how you can use them.
keywords:
  - docs
  - polygon
  - matic
  - transactions
  - meta transactions
  - gasless
image: https://matic.network/banners/matic-network-16x9.png
slug: meta-transactions
---

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

:::note The words meta and batch may be analogous to some

To clarify: a meta transaction is different from a batch transaction, where a batch transaction is
a transaction that can send multiple transactions at once and are then executed from a single sender
(single nonce specified) in sequence.

:::

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
