Before staking on Polygon as a validator, ensure the following prerequisites are met:

## Prerequisites

### Validator Node Setup

- **Validator Node Synced**: Ensure your validator node is fully set up and synchronized. For guidance, refer to [Run a Validator Node](index.md).

### Account Verification

- **Account Setup**: On your validator node, verify the account setup by running `heimdalld show-account`. This command displays your address and public key. Ensure this address corresponds with your Ethereum signer address.

### Private Key Verification (Optional)

- **Checking Private Key**: Optionally, you can verify your private key by executing `heimdalld show-privatekey` on your validator node. It displays your private key, which should be securely managed.

## Staking on Polygon

Stake on Polygon using the [Validator Dashboard](https://staking.polygon.technology/validators/).

### Steps to Stake Using the Dashboard

1. **Access Validator Dashboard**: Visit [validator dashboard](https://staking.polygon.technology/validators/).

2. **Wallet Login**: Log in using your wallet (MetaMask recommended). Use the address where your MATIC tokens are stored.

3. **Become a Validator**: Click on **Become a Validator**. Note: Ensure your node is already set up; otherwise, an error will occur during staking.

4. **Validator Details**: Fill in your validator details, commission rate, and the amount you wish to stake.

5. **Complete Staking Process**: Click **Stake Now** and follow the prompts to approve and confirm the transaction.

!!! note

    Your staking will reflect on the [dashboard](https://staking.polygon.technology/account) after approximately 12 block confirmations.

### Balance verification

To check the balance of your address, use the following command:

```sh
heimdallcli query auth account SIGNER_ADDRESS --chain-id CHAIN_ID
```

- Replace `SIGNER_ADDRESS` with your Ethereum signer address.
- `CHAIN_ID` is the Polygon mainnet chain ID (e.g., `heimdall-137`).

### Claiming Validator Rewards

As a validator, you're entitled to rewards for your contributions to the network.

- **Withdraw Reward**: Click this option on your [dashboard](https://staking.polygon.technology/account) to transfer rewards to your wallet. Updates occur post 12 block confirmations.

- **Restake Reward**: To compound your stake, choose this option. It reinvests your rewards into your stake, enhancing your validator position.

Following these steps and guidelines ensures a smooth setup and management process for validators on the Polygon network.
