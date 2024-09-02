Polygon zkEVM is to Ethereum a Layer 2 network and a scalability solution utilizing zero-knowledge technology to provide validation and fast finality of off-chain transactions.

Polygon zkEVM supports a majority of Ethereum EIPs, precompiles, and opcodes. Developers benefit from the seamless deployment of smart contracts, developer tools, and wallets that already work on Ethereum, but in an environment with significantly lower costs.

Connect to the fully-audited Polygon zkEVM mainnet or its testnet (Cardona testnet) using the details in the table below.

| Network | RPC URL | ChainID | Block explorer URL | Gas token |
| ------- | ------------------------------- | ---------------- | ---------------- | ----- |
| Polygon zkEVM | `https://zkevm-rpc.com` | `1101` | `https://zkevm.polygonscan.com/` | **ETH** |
| Cardona zkEVM testnet | `https://rpc.cardona.zkevm-rpc.com` | `2442` | `https://cardona-zkevm.polygonscan.com/` | **ETH** |

## Protocol development highlights

The Polygon zkEVM testnet launched with a complete ZK proving system and full transaction data availability in October 2022. The proving system uses a combination of eSTARK proofs and FRI, that are then compressed using FFLONK SNARKs to create the final ZK proof.

Following the launch of the testnet, the code base for Polygon zkEVM underwent several security audits. These were among the first audits ever performed on a complete, in-production ZK proving system.  

After the audits, Polygon zkEVM Mainnet Beta [launched in March 2023](https://www.youtube.com/watch?v=UvQIX5i09A4&ab_channel=ETHGlobal). Since then, the zkEVM network has had two major upgrades: [Dragon Fruit (ForkID5)](https://polygon.technology/blog/polygon-zkevm-dragon-fruit-upgrade-with-new-opcode-coming-to-mainnet-beta), in September 2023, and [Inca Berry (ForkID6)](https://polygon.technology/blog/polygon-zkevm-inca-berry-upgrade-coming-to-mainnet-beta), in November 2023.

All updates and upgrades of both the mainnet and testnet can be found in the [Historical data document](../zkEVM/get-started/historical-data.md).

## Security measures

zkEVM's upgrades are on par with Ethereum's security standards as they involve deployment of the following contracts:

- An admin multisig contract to avoid having one account controlling upgrades.
- A timelock contract to give users sufficient time delay to withdraw before execution.
- A transparent upgradeable proxy, from OpenZeppelin’s libraries of audited and battle-tested contracts.

The activation of the 10-day timelock for upgrading zkEVM's smart contracts on Ethereum requires approval by the network's [Admin](https://etherscan.io/address/0x242daE44F5d8fb54B198D03a94dA45B5a4413e21), a three-participant multisig that acts as a [governance tool](../zkEVM/architecture/protocol/admin-role.md#governance-of-zkevm-contracts) for the protocol. This is a Gnosis Safe with a 2/3 threshold.

In the event of an emergency that puts user funds at risk, the network's [Security Council](https://etherscan.io/address/0x37c58Dfa7BF0A165C5AAEdDf3e2EdB475ac6Dcb6) may remove the 10-day timelock. In such an emergency, the network state stops advancing and bridge functionality is paused. The Security Council is an eight-participant multisig. This is a Gnosis Safe with a 6/8 threshold. Learn more about [zkEVM upgradability](https://docs.polygon.technology/zkEVM/architecture/protocol/upgradability/).

## Design characteristics

Polygon zkEVM was designed with security in mind. As an L2 solution, it inherits its security from Ethereum.

Smart contracts are deployed to ensure that everyone who executes state changes does so appropriately, creates a proof that attests to the validity of each state change, and makes validity proofs available on-chain for verification.

Development efforts aim at permissionless-ness, that is, allowing anyone with the zkEVM software to participate in the network. 

For instance, the network allows anyone to circumvent any transaction-censorship by triggering the [force batches](./architecture/protocol/malfunction-resistance/sequencer-resistance.md) mechanism, or to avoid denial of validity-proving by activating the [force verification](./architecture/protocol/malfunction-resistance/aggregator-resistance.md) feature. 

The ultimate aim is to ensure that there is no censorship and that no one party can control the network.

Since data availability is most crucial for decentralization, Polygon zkEVM posts all transaction data and validity proofs on Ethereum. This means every Polygon zkEVM user has sufficient data needed to rebuild the full state of a rollup.

## Efficiency and overall strategy

As a scalability solution, efficiency is key to Polygon zkEVM. 

The network therefore utilizes several implementation strategies to maximize efficiency.

A few of these strategies are listed below:

1. Deployment of the consensus contract, which incentivizes the aggregator for participating in the proof generation process.
2. Carry out all computations off-chain while keeping only the necessary data and ZK-proofs on-chain.
3. Implementation of the bridge smart contract is made efficient by using only Merkle roots of exit trees.
4. Utilization of specialized cryptographic primitives within the proving component, [zkProver](https://docs.polygon.technology/zkEVM/architecture/zkprover/), to speed up computations and minimize proof sizes. This is seen in:
    * Running a special zero-knowledge assembly language ([zkASM](./spec/zkasm/index.md)) for interpretation of bytecode.
    * Using zero-knowledge technology such as zk-STARKs for proving purposes; these proofs are very fast though they are big in size.
    * Instead of publishing the sizeable zk-STARK proofs as validity proofs, a zk-SNARK is used to attest to the correctness of the zk-STARK proofs. 
    * Publishing zk-SNARKs as the validity proofs to state changes.
    
	These help in reducing gas costs from 5M to 350K (wei).

The Polygon zkEVM network is therefore secure, efficient, comes with verifiable block data, and cost-effective.
