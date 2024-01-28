
## Moving Stake from Foundation nodes to External Nodes

Watch the below muted video on how to move your stake. 

<video loop autoplay width="100%" height="100%" controls="true" >
  <source type="video/mp4" src="/img/pos/MoveStakeDemo.mp4"></source>
  <source type="video/quicktime" src="/img/pos/MoveStakeDemo.mov"></source>
  <p>Your browser does not support the video element.</p>
</video>

Delegators are now given an option to move their stake from the Foundation nodes to any External nodes of their choice by using the Move Stake functionality on the Staking UI

Moving Stake from the foundation node to external node is a single transaction. So there are no delays or unbonding periods durind this event.

Please note that Moving Stake is only allowed from Foundation node to External nodes. If you want to move your stake from an External node to another External node, you will have to Unbond first and then Delegate on the new external node.

Also, the Move Stake function is a temporary function developed by the Polygon team to ensure smooth transitioning of funds from the Foundation nodes to External. And will only stay active until the foundation nodes are turned off.

## How to Move Stake

In order to Move stake, first you will need to login to the [Staking UI](https://wallet.polygon.technology/staking) using your Delegator Address.

**Delegator Address** : The address that you have already used for Staking on the Foundation Nodes.

Once logged in, you will see a list of Validators.

![Figure: validator list](../../../img/pos/validator-list.png)

Now go to your Delegator Profile by clicking on the **Show Delegator Details** button or the **My Delegator Details** option on the left.

![Figure: show validator details](../../../img/pos/show-delegator-details.png)

Here you will find a new button called **Move Stake**.

![Figure: move stake button](../../../img/pos/move-stake-button.png)

Clicking on that button would navigate you to a page with a list of validators that you can delegate to. You can delegate to any Validator on this list.

![Figure: move stake button](../../../img/pos/move-stake-validator.png)

Now after choosing your validator that you want to delegate to, click on the **Delegate Here** button. Clicking on that button would open up a popup window.

![Figure: move stake button](../../../img/pos/stake-funds.png)

Here you would see an **Amount** field which would automatically populate with entire amount for Delegation. You can also use a partial amount to delegate to a validator.

For example, if you have delegated 100 MATIC tokens to Foundation Node 1 and now you want to move your stake from the foundation node to an external node, you can delegate a partial amount to the external node of your choice, lets say 50 MATIC tokens. The rest of the 50 MATIC tokens will stay on Foundation node 1. You can then choose to either delegate the rest of the 50 tokens to another external node or the same external node.

Once you have entered the amount you can then click on **Stake Funds** button. This will then ask for confirmation on your MetaMask to sign the address.

Once you have signed the transaction your stake would have successfully moved from the Foundation node to the External node. However, you will have to wait for 12 block confirmations for it reflect on the Staking UI. If your moved funds do not show up after 12 block confirmations, try refreshing the page once to see updated stakes.

If you have any questions or any issues please submit a ticket [here](https://support.polygon.technology/support/home).
