
!!! info "Limited spots for new validators"

    There is limited space for accepting new validators. New validators can only join the active set when an already active validator unbonds. Check out the following links for more information and to apply for a validator slot:

    - [Admission form](https://polygoncommunity.typeform.com/validatorshub?typeform)
    - [Admission dashboard](https://play.validatrium.club/public-dashboards/1b29d3bbdcd14007a0858b68dee76bdd?orgId=1)

Once your validator node is onboarded into the active set, do the following:

- Log in to the [staking dashboard](https://staking.polygon.technology/) with the owner address.
- Go to my account, and click on edit details below the validator name.
- Click on Profile Details and update your **name**, **website**, **description**, **logo URL**, and click on **Save Profile Details**.

## Stake tokens

### Initial staking

1. Access the [validator dashboard](https://staking.polygon.technology/validators/).
2. Log in with your wallet. You can use a popular wallet such as MetaMask. Make sure you login using the owner address, and that you have POL tokens in the wallet.
3. Select **Become a Validator**. You will be asked to set up your node. If you haven't already set up your node by now, you will need to do so, else if you proceed ahead you will receive an error when you attempt to stake.
4. On the next screen, add your validator details, the commission rate, and the staking amount.
5. Select **Stake Now**.
6. Now, you'll be prompted for three confirmations to send the transaction. Once complete, your POL tokens will be added to the staked amount on the validator node. The three confirmations include:
    - Approve Transaction: This approves your stake transaction.
    - Stake: Confirms your stake transaction.
    - Save: Saves your validator details.

!!! info
    
    For the changes to take effect on the [staking dashboard](https://staking.polygon.technology/account), it requires a *minimum of 12 block confirmations*.


### Add stake

1. Access the [validator dashboard](https://staking.polygon.technology/validators/).
2. Log in with your wallet. You can use a popular wallet such as MetaMask. Make sure you login using the owner address, and that you have POL tokens in the wallet.
3. Select **Add more Stake**.
4. Enter the amount, and select **Add More Stake**.
5. Now, you'll be prompted for three confirmations to send the transaction. Once complete, your POL tokens will be added to your staked amount on the validator node. The three confirmations include:
    - Approve Transaction: This approves your stake transaction.
    - Stake: Confirms your stake transaction.
    - Save: Saves your validator details.

!!! info
    
    For the changes to take effect on the [staking dashboard](https://staking.polygon.technology/account), it requires a *minimum of 12 block confirmations*.

## Set commission rate

You can set up and change your commission as a validator.

A validator is entitled to charge any commission rate. The minimum commission would be 0% and the maximum commission would be 100% of the rewards earned.

You set up the commission rate as part of your initial [validator staking process](#initial-staking).

## Changing your commission rate

You are allowed to freely adjust the commission rate as and when necessary.

As a validator, it is one of your responsibilities to inform the community on commission changes. See [Validator Responsibilities](../../get-started/becoming-a-validator.md#validator-responsibilities).

Follow the steps below to change your commission rate:

1. With your owner address, login to the [staking dashboard](https://staking.polygon.technology/).
2. On your profile, select **Edit Profile**.
3. In the **Commission** field, enter your new commission rate.

Once you have confirmed and signed the transaction your commission rate will be set.

Note that once the commission is updated, there is a cool down period of *80 checkpoints*.

## Claim validator rewards

Once you are set up and staked as a validator, you will earn rewards for performing validator duties. When you perform validator duties dutifully, you get rewarded.

To claim rewards you can go to your [validator dashboard](https://staking.polygon.technology/account).

You will see two buttons on your profile:

- **Withdraw Reward**
- **Restake Reward**

### Withdraw Reward

As a validator, you earn rewards as long as you are performing your validator duties correctly.

Selecting **Withdraw Reward** will get your rewards back to your wallet.

The dashboard will update after *12 block confirmations*.

### Restake Reward

Restaking your rewards is an easy way to increase your stake as a validator.

Selecting **Restake Reward** will restake your reward and increase your stake.

The dashboard will update after *12 block confirmations*.

## Common operations

You can use the following commands to check if your validator node is set up correctly.

### Check validator account

Run the following command *on your validator node* to check if the account is set up correctly:

```sh
heimdalld show-account
```

The output should appear in the following format:

```json
{
    "address": "0x6c468CF8c9879006E22EC4029696E005C2319C9D",
    "pub_key": "0x04b12d8b2f6e3d45a7ace12c4b2158f79b95e4c28ebe5ad54c439be9431d7fc9dc1164210bf6a5c3b8523528b931e772c86a307e8cff4b725e6b4a77d21417bf19"
}
```

This will display your address and public key for your validator node. Note that *this address must match with your signer address on Ethereum*.

### Show private key

Run the following command *on your validator node* to check if the private key configured correctly:

```sh
heimdalld show-privatekey
```

The output should appear in the following format:

```json
{
    "priv_key": "0x********************************************************"
}
```

### Check the balance

To check the balance of your address, run the following command:

```sh
heimdallcli query auth account SIGNER_ADDRESS --chain-id CHAIN_ID
```

where,

* `SIGNER_ADDRESS`: Your signer address.
* `CHAIN_ID`: The Polygon mainnet chain ID with the client prefix: `heimdall-137`.

The following output should appear:

```json
address: 0x6c468cf8c9879006e22ec4029696e005c2319c9d
coins:
- denom: pol
amount:
    i: "1000000000000000000000"
accountnumber: 0
sequence: 0
```