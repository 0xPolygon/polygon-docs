---
comments: true
---

### MetaMask transactions fail with a nonce error in dev environment 

Every time the dev environment starts, a new local test chain is started. Metamask maintains a cache of "latest block number" and "account transaction nonce". Since every run of `dev` creates a new chain, it never matches with this cache.

To clear the cache, follow the [MetaMask documentation](https://support.metamask.io/hc/en-us/articles/360015488891-How-to-clear-your-account-activity-reset-account).

### MetaMask transactions fail with a nonce error when using the **reset on change** option in dev environment

The reset on change option resets the blockchain on every code change. 

MetaMask maintains a cache of *latest block number* and *account transaction nonce*. After resetting the chain, the latest block number and account transaction nonce should go back to the initial state as well, but MetaMask does not update this cache on its own.

To clear the cache, follow the [MetaMask documentation](https://support.metamask.io/hc/en-us/articles/360015488891-How-to-clear-your-account-activity-reset-account).

### Error: `could not coalesce error (error={ "code": -32603, "message": "Internal JSON-RPC error." })`

Clear your wallet cache and try again.

To clear the cache, follow the [MetaMask documentation](https://support.metamask.io/hc/en-us/articles/360015488891-How-to-clear-your-account-activity-reset-account).