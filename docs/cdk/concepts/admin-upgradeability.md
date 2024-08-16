# Admin upgradeability

As L2s work through the [stages of training wheels](https://medium.com/l2beat/introducing-stages-a-framework-to-evaluate-rollups-maturity-d290bb22befe) to become fully decentralized, chains that opt in to the [AggLayer](../glossary/index.md#agglayer-v1-al1) implement shared security mechanisms with other AggLayer chains including the [Polygon zkEVM](../../zkEVM/architecture/protocol/upgradability.md) to ensure the safety of users.

Chains opted into the AggLayer share the following upgradeability controls:

1. The [security council](../../zkEVM/architecture/protocol/security-council.md) ([contract address](https://etherscan.io/address/0x37c58Dfa7BF0A165C5AAEdDf3e2EdB475ac6Dcb6)) that can be used to trigger the [emergency state](../../zkEVM/architecture/protocol/malfunction-resistance/emergency-state.md) which can pause bridge functionality, prevent smart contract upgrades, or stop the [sequencer](./architecture.md#sequencer) from [sequencing batches](./transaction-lifecycle.md#sequenced).

2. The [admin role](../../zkEVM/architecture/protocol/admin-role.md) ([contract address](https://etherscan.io/address/0x242daE44F5d8fb54B198D03a94dA45B5a4413e21)) that can perform upgrades to patch bug fixes or add new features to the system by upgrading smart contracts with a 10-day waiting period (unless [emergency state](../../zkEVM/architecture/protocol/malfunction-resistance/emergency-state.md) is active).

## Further reading

- [zkEVM protocol upgradability](../../zkEVM/architecture/protocol/upgradability.md).
- [zkEVM admin role and governance](../../zkEVM/architecture/protocol/admin-role.md).
- [zkEVM upgrade process](../../zkEVM/architecture/protocol/upgrade-process.md).
- [zkEVM security council](../../zkEVM/architecture/protocol/security-council.md).
- [zkEVM emergency state](../../zkEVM/architecture/protocol/malfunction-resistance/emergency-state.md).
- [L2Beat - Polygon zkEVM](https://l2beat.com/scaling/projects/polygonzkevm?selectedChart=activity).