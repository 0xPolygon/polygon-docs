# CDK-opgeth Architecture

This page outlines the full system architecture for CDK-opgeth across supported and upcoming modes.

## 🖥️ Sovereign Mode (Live)
![CDK-opgeth Sovereign](../img/cdk/CDK-opgeth-sovereign.png)

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| OP Stack     | OP Geth              | EL (Execution Layer)                     | [op-geth](https://github.com/ethereum-optimism/op-geth) |
|              | OP Node              | CL (Consensus Layer)                     | [optimism](https://github.com/ethereum-optimism/optimism) |
| Aggkit       | AggOracle            | GER update component                     | [aggkit](https://github.com/agglayer/aggkit) |
|              | AggSender            | Sends certificates to Agglayer           | — |
|              | Bridge API           | Cross-chain messaging                    | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | OP Batcher           | Data to Ethereum L1                      | [optimism](https://github.com/ethereum-optimism/optimism) |
|              | Agglayer             | Bridge/messaging network                 | [agglayer](https://github.com/agglayer/agglayer) |
| Contracts    | OP-Contracts-L1      | Bedrock contracts (L1)                   | [v0.0.11](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11) |
|              | OP-Contracts-L2      | Bedrock contracts (L2)                   | [v0.0.11](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11) |
|              | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |

## 🧪 Validium Mode (In Development)

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| OP Stack     | OP Geth              | EL (Execution Layer)                     | [op-geth](https://github.com/ethereum-optimism/op-geth) |
|              | OP Node              | CL (Consensus Layer)                     | [optimism](https://github.com/ethereum-optimism/optimism) |
|              | OP Proposer          | Prover publishing logic                  | [optimism](https://github.com/ethereum-optimism/optimism) |
| Aggkit       | AggOracle            | GER update component                     | [aggkit](https://github.com/agglayer/aggkit) |
|              | AggSender            | Sends certificates to Agglayer           | — |
|              | Bridge API           | Cross-chain messaging                    | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | Alt-DA               | TBD data availability network            | [alt-da-mode](https://docs.optimism.io/stack/beta-features/alt-da-mode) |
|              | Agglayer             | Bridge/messaging network                 | [agglayer](https://github.com/agglayer/agglayer) |
| Prover       | SP1 Prover           | zkVM proofs                              | [sp1](https://github.com/succinctlabs/sp1) |
| Contracts    | OP-Contracts-L1/L2   | Bedrock L1/L2 Contracts                  | [v0.0.11](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11) |
|              | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |

## 🔒 zkRollup Mode (In Development)
![CDK-opgeth zkRollup](../img/cdk/CDK-opgeth-zkrollup.png)

| Layer         | Component           | Description                              | Repository |
|---------------|----------------------|------------------------------------------|------------|
| OP Stack     | OP Geth              | EL (Execution Layer)                     | [op-geth](https://github.com/ethereum-optimism/op-geth) |
|              | OP Node              | CL (Consensus Layer)                     | [optimism](https://github.com/ethereum-optimism/optimism) |
|              | OP Proposer          | Prover publishing logic                  | [optimism](https://github.com/ethereum-optimism/optimism) |
| Aggkit       | AggOracle            | GER update component                     | [aggkit](https://github.com/agglayer/aggkit) |
|              | AggSender            | Sends certificates to Agglayer           | — |
|              | Bridge API           | Cross-chain messaging                    | [bridge-service](https://github.com/0xPolygonHermez/zkevm-bridge-service) |
| DA           | Ethereum DA          | On-chain data storage                    | — (uses Ethereum L1) |
|              | Agglayer             | Bridge/messaging network                 | [agglayer](https://github.com/agglayer/agglayer) |
| Prover       | SP1 Prover           | zkVM proofs                              | [sp1](https://github.com/succinctlabs/sp1) |
| Contracts    | OP-Contracts-L1/L2   | Bedrock L1/L2 Contracts                  | [v0.0.11](https://github.com/ethereum-optimism/optimism/releases/tag/op-deployer%2Fv0.0.11) |
|              | Ethereum Bridge      | Final settlement                         | [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts) |