# Admin Upgradeability

As L2s work through the [stages of training wheels](https://medium.com/l2beat/introducing-stages-a-framework-to-evaluate-rollups-maturity-d290bb22befe) to become fully decentralized, chains built with the CDK that opt in to the [AggLayer](https://docs.polygon.technology/cdk/glossary/#agglayer-v1-al1) implement shared security mechanisms with other AggLayer chains including the [Polygon zkEVM](https://docs.polygon.technology/zkEVM/architecture/protocol/upgradability/) to ensure the safety of users.

Chains opted into the AggLayer share the following upgradeability controls:

1. The [security council](https://docs.polygon.technology/zkEVM/architecture/protocol/security-council/) ([contract address](https://etherscan.io/address/0x37c58Dfa7BF0A165C5AAEdDf3e2EdB475ac6Dcb6)) that can be used to trigger the [emergency state](https://docs.polygon.technology/zkEVM/architecture/protocol/malfunction-resistance/emergency-state/) which can pause bridge functionality, prevent smart contract upgrades, or stop the [sequencer](./architecture.md#sequencer) from [sequencing batches](./transaction-lifecycle.md#sequenced).
2. The [admin role](https://docs.polygon.technology/zkEVM/architecture/protocol/admin-role/) ([contract address](https://etherscan.io/address/0x242daE44F5d8fb54B198D03a94dA45B5a4413e21)) that can perform upgrades to patch bug fixes or add new features to the system by upgrading smart contracts with a 10-day waiting period (unless [emergency state](https://docs.polygon.technology/zkEVM/architecture/protocol/malfunction-resistance/emergency-state/) is active).

## Further Reading

- [zkEVM protocol upgradability](https://docs.polygon.technology/zkEVM/architecture/protocol/upgradability/)
- [zkEVM admin role and governance](https://docs.polygon.technology/zkEVM/architecture/protocol/admin-role/)
- [zkEVM upgrade process](https://docs.polygon.technology/zkEVM/architecture/protocol/upgrade-process/)
- [zkEVM security council](https://docs.polygon.technology/zkEVM/architecture/protocol/security-council/)
- [zkEVM emergency state](https://docs.polygon.technology/zkEVM/architecture/protocol/malfunction-resistance/emergency-state/)
- [L2Beat - Polygon zkEVM](https://l2beat.com/scaling/projects/polygonzkevm?selectedChart=activity)
