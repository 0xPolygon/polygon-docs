# ZK vs. optimistic rollups

Rollups can differ in how they ensure the validity of transactions that occur on the L2. They can be broadly categorized into two types: zero-knowledge (ZK) rollups and optimistic rollups.

Importantly, the Polygon CDK allows developers to build ZK rollups as they use cryptographic mechanisms (ZK-proofs) for security, which offers several advantages and are more secure than optimistic rollups that rely on the honesty of incentivized actors.

## Optimistic rollups

!!! note
    The CDK does not support the development of optimistic rollups.

Optimistic rollups act on an "innocent until proven guilty" basis, meaning they optimistically assume transactions that occurred on the L2 are valid and do not actively post any validity proofs to Ethereum to prove the validity of transactions.

Instead, they rely on a _challenge period_, a set period of time (typically 7 days) where users (or sometimes a set list of actors) can compute and submit a _fault proof_ (often called a *fraud proof*) to challenge the results of a rollup transaction.

If the fault proof is accepted, meaning there were fraudulent transactions posted to Ethereum, the state of the rollup is updated to reflect the correct state, and the malicious actor (the sequencer) is penalized.

The key advantage to optimistic rollups is that they are cost-effective. Because fraud proofs are only rarely submitted in the event of a dispute, the gas fees associated with optimistic rollups are lower than ZK rollups which are regularly posting proofs to Ethereum to prove the validity of transactions.

However, there are several disadvantages to this optimistic approach; users cannot withdraw their funds until the challenge period has passed, and the security of the rollup is dependent on the honesty of the actors. That is, at least one honest actor must be actively monitoring the rollup and submitting fault proofs to maintain the integrity of the chain, or the rollup could be compromised.

## Zero-knowledge rollups

ZK rollups act on a "guilty until proven innocent" basis, meaning transactions are only considered valid once an associated validity proof (ZK-proof) is posted and verified on Ethereum to prove the validity of transactions.

By using cryptographic mechanisms for security, ZK rollups are generally considered more secure than optimistic rollups as there is no situation where fraudulent transactions can be finalized; unlike optimistic rollups which rely on a challenge period to correct any fraudulent transactions.

As validity proofs are posted regularly to Ethereum to prove the validity of transactions (for example, see the [Polygon zkEVM trusted aggregator](https://etherscan.io/address/0x6329Fe417621925C81c16F9F9a18c203C21Af7ab)), the gas fees are typically slightly higher than optimistic rollups, as the L2 must pay Ethereum's high gas fees to store data on the L1.

ZK rollups have several advantages over optimistic rollups; users can withdraw their funds without waiting for a challenge period to pass, and the security of the rollup is not dependent on the honesty of actors, as the cryptographic mechanisms ensure the validity of transactions.

## Further reading

You can learn more about the differences between ZK and optimistic rollups on the official Ethereum documentation:

- [Ethereum documentation: ZK Rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/).
- [Ethereum documentation: Optimistic Rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/).