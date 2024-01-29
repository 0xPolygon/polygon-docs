
For information on what a signer address is, see
[Key Management](../../architecture/heimdall/key-management.md).

## Prerequisites

Make sure your new validator node is fully synced and is running with the new signer address.

## Change the Signer Address

This guide refers to your current validator node as Node 1 and your new validator node as Node 2.

1. Log in to the [staking dashboard](https://staking.polygon.technology/) with the Node 1 address.
2. On your profile, click **Edit Profile**.
3. In the **Signer's address** field, provide the Node 2 address.
4. In the **Signer's public key** field, provide the Node 2 public key.

   To get the public key, run the following command on the validator node:

   ```sh
   heimdalld show-account
   ```

Clicking **Save** will save your new details for your node. This essentially means that Node 1 will be your address that controls the stake, where the rewards will be sent to, etc. And Node 2 will now be performing activities like signing blocks, signing checkpoints, etc.
