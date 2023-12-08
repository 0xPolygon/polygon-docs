<div class="flex-figure" markdown="1">
<div class="flex-figure-left" markdown="1">
# Polygon zkEVM
Polygon zkEVM is a Layer 2 network of the Ethereum Virtual Machine (EVM), a zero-knowledge (ZK) rollup scaling solution. Polygon zkEVM uses a cryptographic primitive called a ZK proof to validate state transitions.
</div>
<div class="flex-figure-right">
<img src="../img/home/zkevm.svg" class="figure figure-right" alt="" />
</div>
</div>

Polygon zkEVM is compatible with the EVM, supporting the majority of Ethereum EIPs, pre-compiles, and opcodes. Developers benefit from the seamless deployment of smart contracts, developer tools, and wallets that already work on Ethereum, but in an environment with significantly lower costs.

## Protocol development highlights

The Goërli testnet for Polygon zkEVM launched with a complete ZK proving system and full transaction data availability in October 2022. The proving system for Polygon zkEVM uses a combination of eSTARK proofs and FRI that are then compressed using FFLONK SNARKs to create the final ZK proof.

Following the launch of the testnet, the code base for Polygon zkEVM underwent several security audits. These were among the first audits ever performed on a complete, in-production ZK proving system.

After the audits, Polygon zkEVM Mainnet Beta [launched in March 2023](https://www.youtube.com/watch?v=UvQIX5i09A4&ab_channel=ETHGlobal). Since then, the zkEVM network has had two major upgrades: [Dragon Fruit (ForkID5)](https://polygon.technology/blog/polygon-zkevm-dragon-fruit-upgrade-with-new-opcode-coming-to-mainnet-beta), in September 2023, and [Inca Berry (ForkID6)](https://polygon.technology/blog/polygon-zkevm-inca-berry-upgrade-coming-to-mainnet-beta), in November 2023.

## Security measures

The security measures taken by the zkEVM team for an upgrade are on par with Ethereum's security standards as they involve the deployment of:

- An Admin Multisig Contract to avoid having one account controlling upgrades,
- A Timelock Contract to give users sufficient time delay to withdraw before execution, and
- A Transparent Upgradeable Proxy, from OpenZeppelin's libraries of audited and battle-tested contracts.

The activation of the 10-day timelock for upgrading zkEVM's smart contracts on Ethereum requires approval by the network's [Admin](https://etherscan.io/address/0x242daE44F5d8fb54B198D03a94dA45B5a4413e21), a three-participant multisig that acts as a [governance tool](https://wiki.polygon.technology/docs/zkevm/protocol/admin-role/#:~:text=Governance%20of%20zKEVM%20Contracts%E2%80%8B&text=sol%20contract%20instance%20is%20assigned,of%20Polygon%20zkEVM%20L1%20contracts.) for the protocol. This is a Gnosis Safe with a 2/3 threshold.

In the event of an emergency that puts user funds at risk, the network's [Security Council](https://etherscan.io/address/0x37c58Dfa7BF0A165C5AAEdDf3e2EdB475ac6Dcb6) may remove the 10-day timelock. In such an emergency, the network state stops advancing and bridge functionality is paused. The Security Council is an eight-participant multisig. This is a Gnosis Safe with a 6/8 threshold. Learn more about [zkEVM upgradability](https://docs-staging.polygon.technology/zkEVM/architecture/protocol/upgradability/).

## Resources to get you started

- **How to**: Learn how to write, verify, and deploy a smart contract.
- **Deploy**: Learn how to deploy a full implementation of Polygon zkEVM with Goërli as the underlying L1.
- **Architecture**: Understand Polygon zkEVM's major components, how it handles state transitions and the consensus contract, and the lifecycle of a transaction.
- **Concepts**: Learn about EVM basics, CIRCOM, and Polygon zkEVM's state machine design model.

## What you'll find here

This documentation contains guides for connecting wallets to the Polygon zkEVM network, deploying new or existing Ethereum smart contracts, and bridging assets between Polygon zkEVM and Ethereum.

Protocol developers will find guides for setting up an RPC Node, spinning up local and production nodes, and deploying a complete implementation of the Polygon zkEVM mainnet beta or testnet networks.