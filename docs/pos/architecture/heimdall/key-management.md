Each validator uses two keys to manage validator related activities on Polygon. The Signer key is kept on the node and is generally considered a `hot` wallet, whereas the Owner key is supposed to kept very secure, is used infrequently, and is generally considered a `cold` wallet. The staked funds are controlled by the Owner key.

This separation of responsibilities has been done to ensure an efficient tradeoff between security and ease of use. Both keys are Ethereum compatible addresses and work exactly the same manner. And yes, it is possible to have same Owner and Signer keys.

## Signer key

The signer key is an address that is used for signing Heimdall blocks, checkpoints, and other signing related activities. This key's private key will be on the Validator node for signing purposes. It cannot manage stake, rewards or delegations.

The validator must keep two types of balances on this address:

- Matic tokens on Heimdall (through Topup transactions) to perform validator responsibilities on Heimdall
- ETH on Ethereum chain to send checkpoints on Ethereum

## Owner key

The owner key is an address that is used for staking, re-stake, changing the signer key, withdraw rewards and manage delegation related parameters on the Ethereum chain. The private key for this key must be secure at all cost.

All transactions through this key will be performed on the Ethereum chain.

## Signer change

Following event is generated in case of signer change on Ethereum chain on `StakingInfo.sol`: [https://github.com/maticnetwork/contracts/blob/develop/contracts/staking/StakingInfo.sol](https://github.com/maticnetwork/contracts/blob/develop/contracts/staking/StakingInfo.sol)

```go
// Signer change
event SignerChange(
  uint256 indexed validatorId,
  address indexed oldSigner,
  address indexed newSigner,
  bytes signerPubkey
);
```

Heimdall bridge processes these events and sends transactions on Heimdall to change state based on the events.
