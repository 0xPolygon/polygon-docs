Operating as a validator on the Polygon Network involves playing a pivotal role in validating transactions within the blockchain. This guide provides details on how to run a Validator Node (including Sentry and Validator components) on the Polygon Network, the responsibilities involved, and the technical and operational aspects to consider.

## Eligibility and responsibilities

To qualify as a validator on the Polygon Network, participants must:

- Stake a minimum of 1 MATIC token in the ecosystem.
- Fulfill various responsibilities, including technical operations and effective communication.

Key responsibilities include:

- **Technical Node Operations**: These are largely automated by the node software.
- **Operational Duties**:
  - Ensure high uptime.
  - Conduct daily checks of node-related services and processes.
  - Implement node monitoring.
  - Maintain an Ethereum (ETH) balance of approximately 0.5 to 1 ETH in the signer address for transaction fees.
- **Delegation Management**:
  - Be open to accepting delegations.
  - Transparently communicate commission rates to delegators.
- **Communication**:
  - Promptly report any issues.
  - Offer feedback and suggestions to the Polygon team.
- **Rewards**: Earn staking rewards and transaction fees for validating blocks.

## Technical Node Operations

These operations are automatically executed by the nodes:

- **Block Producer Selection**: A subset of validators is chosen periodically to form the block producer set.
- **Validating Blocks on Bor**: Validators independently validate block data on Heimdall.
- **Checkpoint Submission**: Proposers among validators create, validate, and submit checkpoints to the Ethereum mainnet.
- **State Sync**: Contract state data is synchronized between Ethereum and Polygon, particularly through Bor.

## Operational guidelines

### Maintaining high uptime

- Validators must sign checkpoint transactions approximately every 34 minutes.
- Failure to sign these transactions affects node performance.
- Node health maintenance and monitoring are crucial for uninterrupted operations.

### Daily checks and monitoring

- Regularly check and prune Heimdall and Bor services and processes.
- Utilize Grafana Dashboards or alternative monitoring tools.
- Monitor the Ethereum endpoint used on nodes to stay within request limits.

### ETH balance management

- Adequate ETH balance is required for checkpoint transaction fees.
- Fluctuations in Ethereum network gas prices must be considered.

## Earning rewards

Validators stake MATIC tokens for network security and receive rewards:

- **Staking Rewards**: Validators are compensated for their contributions to network security.
- **Transaction Fees**: Validators earn a portion of the transaction fees from the blocks they produce.

### Reward distribution

- A portion of Polygon's total token supply is allocated for staking rewards.
- Rewards are designed to gradually shift from staking to transaction fee-based as the network matures.

### Incentives for validators

- Validators earn rewards from both staking and transaction fees.
- The reward structure is designed to balance the payout between staking and fees over time.

## Delegation

Validators should:

- Be open to delegations from the community.
- Clearly communicate their commission rates.

## Effective communication

- Report issues promptly on platforms like Discord, the Polygon Forum, or GitHub.
- Provide constructive feedback and suggestions.

## System requirements

### Minimum requirements

- **RAM**: 32 GB
- **CPU**: 8-core
- **Storage**: 2.5 TB SSD
- **AWS Equivalent**: c5.2xlarge for Sentry, c5.4xlarge for Validator node (with unlimited credits).

### Recommended requirements

- **RAM**: 64 GB
- **CPU**: 16-core
- **Storage**: 5 TB SSD
- **Bandwidth**: 1 Gbit/s

These specifications ensure that your nodes are well-equipped for current and future network demands. Separate machines for Sentry and Validator nodes are advised for optimal performance and security.
