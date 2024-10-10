
### 1. Are the private keys same for Heimdall and Bor keystore?

Yes, the private key used for generating Validator keys and Bor Keystore is the same.
The private key used in this instance is your Wallet's ETH address where your Polygon
testnet tokens are stored.

### 2. List of Common Commands

Refer to the [list of common commands](../../reference/commands.md) that might come in handy while troubleshooting.

### 3. Default Directories

- Heimdall genesis file: `/var/lib/heimdall/config/genesis.json`
- Heimdall-config.toml file: `/var/lib/heimdall/config/heimdall-config.toml`
- Heimdall config.toml file: `/var/lib/heimdall/config/config.toml`
- Heimdall data directory: `/var/lib/heimdall/data/` 
- Bor config.toml file: `/var/lib/bor/config.toml` 
- Bor data directory: `/var/lib/bor/data/bor/chaindata`

### 4. From where do I create the API key?

You can access this link: [https://infura.io/register](https://infura.io/register) . Make sure that once you have setup your account and project, you copy the API key for Sepolia and not mainnet.

Mainnet is selected by default.

### 5. How do I delete remnants of Heimdall and Bor?

Run the following commands to delete the remnants of Heimdall and Bor from your machines.

For the Linux package, run: `$ sudo dpkg -i bor`

And delete the Bor directory using: `$ sudo rm -rf /var/lib/bor`

For binaries, run: `$ sudo rm -rf /var/lib/bor`

And then run: `$ sudo rm /var/lib/heimdall`

### 6. How many validators can be active concurrently?

Under the current limit, a maximum of 105 validators can be active at any given time. It's important to note that active validators are primarily those with high uptime, while participants with significant downtime may be removed.

### 7. How much should I stake?

A minimum stake of 10,000 POL tokens is required (as per PIP-4). We recommend setting a Heimdall fee of 10 POL.

### 8. I'm not clear on which Private Key should I add when I generate validator key.

The private key to be used is your wallet's ETH address where your Polygon testnet tokens are stored. You can complete the setup with one public-private key pair tied to the address submitted on the form.

### 9. Is there a way to know if Heimdall is synced?

You can run the following command to check it:

```bash
$ curl [http://localhost:26657/status](http://localhost:26657/status)
```

Check the value of the `catching_up` flag. If it is `false` then the node is all synced up.

### 10. Which file do I add the API key in?

Once you have created the API key, you need to add it to the `heimdall-config.toml` file.

### 11. How to check if the correct signer address is used for validator setup?

To check the signer address, run the following command *on the validator node*:

```bash
heimdalld show-account
```

### 12. `Error: Failed to unlock account (0x...) No key for given address or file`

This error occurs because the path for the `password.txt` file is incorrect. You can follow the below steps to rectify this:

1. Copy the Bor keystore file to `/var/lib/bor/keystore`
2. Copy `password.txt` to `/var/lib/bor/`
3. Make sure you have added correct address in `/var/lib/bor/config.toml`.
4. Ensure that the `priv_validator_key.json` and `UTC-<time>-<address>` files have relevant permissions. To set relevant permissions for priv_validator_key.json, run `sudo chown -R heimdall:nogroup /var/lib/heimdall/config/priv_validator_key.json`, and similarly, run `sudo chown -R bor:nogroup /var/lib/bor/data/keystore/UTC-<time>-<address>` for the `UTC-<time>-<address>` file.

### 13. My node is not signing any checkpoints

Try the following solutions:

1. Start by checking and updating the `bor_rpc_url` parameter in the `heimdall-config.toml` file of the validator to any external node RPC providers and restart the services. This change helps to avoid missing checkpoints.

    !!! info
        At this point in time, the node will not mine blocks. So once the issue is fixed, the changes made have to be reverted for the node to return to normal functionality.

2. Verify that the Heimdall service is running normally on both your sentry and validator nodes. If the service has stopped unexpectedly or is encountering errors, attempt to restart it and check if it resumes normal operation.
3. Check your Bor service logs for any errors or signs of abrupt halting. Try restarting your Bor service to resolve the issue.
4. If these steps don't resolve the issue, please contact our support team and share the relevant logs for further assistance.

### 14. Consequences of a validator missing checkpoints

- Economic impact
- Loss of reputation as a reliable validator
- Missed node rewards for delegators
- Repeatedly missing checkpoints can lead to grace period one and two, followed by final notice and removal from the network.