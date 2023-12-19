
### What is the staking dashboard URL?

The staking dashboard URL is https://staking.polygon.technology/.

### What is the minimum stake amount?

There is no minimum stake amount to delegate. However, you can always start with 1 MATIC token.

### How many rewards will I get if I delegate?

Please use the [Polygon earnings calculator](https://staking.polygon.technology/rewards-calculator) to determine your estimates.

### Why does my transaction take so long?

All staking transactions of Polygon happen on Ethereum for security reasons.

The time taken to complete a transaction depends on the gas fees that you have allowed and also the network congestion of Ethereum mainnet at that point in time. You can always use the “Speed Up” option to increase the gas fees so that your transaction can be completed soon.

### Which wallets are currently supported?

We have recently upgraded the wallet support to WalletConnect v2.0. Now you can choose from a plethora of wallets, including Metamask, Coinbase, and others, on both desktop and mobile devices to log in.
  
  <center>
  ![Figure: Supported wallet](../../../img/pos/supported-wallet.png)
  </center>
 
### Are hardware wallets supported?

Yes, hardware wallets are supported. You can use the "Connect Hardware Wallet" option on MetaMask and connect your Hardware wallet and then continue the delegation process.

### Why can’t I stake directly from Binance?

Staking through Binance is not yet supported. There will be an announcement if and when Binance starts supporting it.

### I have completed my delegation, where can I check details?

Once you have completed your delegation, wait for 12 block confirmations on Ethereum (approx. 3-5 minutes), then on the Dashboard, you can click on **My Account**.

![Figure: My account](../../../img/pos/my-account.png)


### Where can I check my rewards?

On the Dashboard, you can click on the **My Account** option on the left-hand side.

![Figure: My account](../../../img/pos/my-account.png)


### Do I need ETH to pay for gas fees?

Yes. You should provision for ~0.05-0.1 ETH to be safe.

### Do I need to deposit MATIC tokens to the Polygon mainnet network for staking?

No. All your funds need to be on the main Ethereum network.

### When I try to do the transaction my **Confirm** button is disabled.

Please check if you have enough ETH for the gas fees.

### When does reward get distributed?

The rewards are distributed whenever a checkpoint is submitted.

Currently, 71795 MATIC tokens are distributed proportionately on each successful checkpoint submission to each delegator based on their stake relative to the overall staking pool of all validators and delegators. Also, the percentage for the reward distributed to each delegator will vary with each checkpoint depending on the relative stake of the delegator, validator and the overall stake.

(Note that there is a 10% proposer bonus that accrues to the validator who submits the checkpoint, but over time, the effect of the extra bonus is nullified over multiple checkpoints by different validators.)

The checkpoint submission is done by one of the validators approximately every 30 minutes. This time is approximate and may vary based on validator consensus on the Polygon Heimdall layer. This may also vary based on Ethereum Network. Higher congestion in the network may result in delayed checkpoints.

You can track checkpoints on the staking contract [here](https://etherscan.io/address/0x86e4dc95c7fbdbf52e33d563bbdb00823894c287)

### Why does reward keep getting decreased every checkpoint?

Actual rewards earned will depend on the actual total locked supply in the network at each checkpoint. This is expected to vary significantly as more MATIC tokens get locked in the staking contracts.

Rewards will be higher, to begin with, and will keep decreasing as the locked supply % goes up. This change in locked supply is captured at every checkpoint, and rewards are calculated based on this.

### How can I claim my rewards?

You can claim your rewards instantly by clicking on the **Withdraw Reward** button. This will transfer the rewards accumulated to your delegated account on Metamask.

![Figure: Withdraw-reward](../../../img/pos/withdraw-reward.png)


### What is the unbonding period?

The unbonding period on Polygon is 80 checkpoints. This period applies to the originally delegated amount and re-delegated amounts - it does not apply to any rewards that were not re-delegated.

### Will I keep receiving rewards after I unbond?

No. Once you unbond, you will stop receiving rewards.

### How many transactions does the delegation require?

Delegation requires 2 transactions, one after the other. One to **Approve** the request and another to **Deposit**.

![Figure: Delegate ](../../../img/pos/delegate.png) 

### What does redelegate rewards mean?

Redelegating your rewards simply means that you want to increase your stake by restaking the rewards you have accumulated.

### Can I stake to any validator?
Yes, you can delegate to any validator except the ones which are offline.

### Which browser is compatible with the Polygon earnings calculator?

Chrome, Firefox, and Brave

### My MetaMask is stuck at confirming after login, what do I do? Or nothing happens when I try to login?

Check for the following:

- If you’re using Brave, please turn off the option for **Use Crypto Wallets** in the settings panel.
- Check if you are logged into Metamask
- Check if you are logged into MetaMask with Trezor/Ledger. You need to additionally turn on permission to call contracts on your Ledger device, if not enabled already.
- Check your system timestamp. If the system time is not correct, you will need to correct it.

### How do I send funds from Binance or other exchanges to Polygon wallet?

The Polygon Wallet Suite is a web application. 

First, you must withdraw your funds from Binance or any other exchange to your Ethereum address on Metamask. If you don't know how to use Metamask, google it a bit. There are plenty of videos and blogs to get started with it.

### When can I become a validator and how many tokens do I for that?

A user can earn a validator spot only by if the below conditions come into play:
1. When a validator decides to unstake from the network, or
2. Wait for the auction mechanism and replace the inactive validator.

The minimum stake depends on the auction process where one user outbids another.

### If I have earned rewards while delegating, and if I add additional funds to the same validator node, what happens?

If you have not re-delegated your rewards before delegating additional funds to the same validator node, your rewards will be withdrawn automatically.

In case you dont want that to happen, re-delegate your rewards before delegating additional funds.

### I have delegated my tokens via MetaMask on the dashboard. Do I need to keep my system or device on?

No. Once your delegation transactions are confirmed, and you can see your tokens reflected in the **Total Stake** and **New Reward** sections, then you are done. There is no need to keep your system or device on.

### I have unbonded, how long will it take to unbond?

The unbonding period is currently set to 80 checkpoints. Every checkpoint takes approximately 30 minutes. However, some checkpoints could be delayed upto ~1 hour due to congestion on Ethereum.

### I have unbonded, and I now see the **Claim Stake** button, but it is disabled.

The Claim Stake button will only be enabled when your unbonding period is complete. The unbonding period is currently set at 80 checkpoints.

### When will the **Claim Stake** button be enabled?

Under the **Claim Stake** button you should see a note on how many checkpoints are pending before the **Claim Stake** button is enabled. Every checkpoint takes approximately 30 minutes. However, some checkpoints could be delayed upto ~1 hour due to congestion on Ethereum.

![Figure: Unbound ](../../../img/pos/unbond.png)



### Have the foundations nodes been turned off?

Yes, the foundation nodes had been turned off.

### Will there be any foundation nodes in the future?

No, there won't be any Foundation nodes in the future.

### How many transactions do I need to pay for gas when I do a "move stake"?

The move stake is a single transaction only. All transactions are on the Ethereum blockchain so you will spend some ETH to make the transaction.
