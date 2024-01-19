!!! note "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

## Checkpoint

| Field            | Type    | Description                                 |
| ---------------- | ------- | ------------------------------------------- |
| id               | ID!     | Checkpoint ID                               |
| Proposer         | Bytes!  | The address of the proposer                 |
| headerBlockId    | BigInt! | The Id of the header block                  |
| checkpointNumber | BigInt! | The checkpoint number                       |
| reward           | BigInt! | The reward of the proposed checkpoint       |
| start            | BigInt! | Start block of the proposed checkpoint      |
| end              | BigInt! | End block of the proposed checkpoint        |
| root             | Bytes!  | Merkle root hash of the proposed checkpoint |
| logIndex         | String! | LogIndex ID                                 |
| transactionHash  | Bytes!  | Transaction hash of proposed checkpoint     |
| timeStamp        | BigInt! | The checkpoint timestamp                    |

## StateSync

| Field                      | Type    | Description                                                |
| -------------------------- | ------- | ---------------------------------------------------------- |
| id                         | ID!     | StateSync ID                                               |
| stateId                    | BigInt! | The stateId number                                         |
| contract                   | Bytes!  | The contract address                                       |
| syncType                   | Int!    | Type of sync                                               |
| depositorOrRootToken       | String! | Depositor or root token address                            |
| depositedTokenOrChildToken | String! | Address of deposited token or child token address          |
| data                       | String! | Data containing the state of the contract at sync time     |
| rawData                    | String! | Raw data containing the state of the contract at sync time |
| logIndex                   | String! | logIndex ID                                                |
| transactionHash            | Bytes!  | Transaction hash                                           |
| timeStamp                  | BigInt! | Timestamp during sync of contract state                    |
| blockNumber                | BigInt! | Block number of the state sync                             |

## StateRegistration

| Field    | Type   | Description           |
| -------- | ------ | --------------------- |
| id       | ID!    | State registration ID |
| user     | Bytes! | User address          |
| receiver | Bytes! | Receiver address      |
| sender   | Bytes! | Sender address        |
                                            |

## PredicateRegistration

| Field            | Type    | Description                                |
| ---------------- | ------- | ------------------------------------------ |
| id               | ID!     | Predicate registration ID                  |
| tokenType        | Bytes!  | Token contract address                     |
| predicateAddress | Bytes!  | Predicate address                          |
| timestamp        | BigInt! | Predicate registration timestamp           |
| transactionHash  | Bytes!  | Transaction hash of predicate registration |

## TokenMapping

| Field           | Type     | Description                         |
| --------------- | -------- | ----------------------------------- |
| id              | ID!      | Token mapping ID                    |
| rootToken       | Bytes!   | Root token address                  |
| childToken      | Bytes!   | Child token address                 |
| tokenType       | String!  | Token contract address              |
| isPOS           | Boolean! | Checks whether POS is true or false |
| timestamp       | BigInt!  | Token mapping timestamp             |
| transactionHash | Bytes!   | Transaction hash                    |

## FxTokenMapping

| Field           | Type    | Description                                    |
| --------------- | ------- | ---------------------------------------------- |
| id              | ID!     | Fx token mapping ID                            |
| counter         | BigInt! | Fx token mapping counter                       |
| contractAddress | Bytes!  | Contract address that handles Fx token mapping |
| rootToken       | Bytes!  | Root token address                             |
| childToken      | Bytes!  | Child token address                            |
| tokenType       | String! | Token contract address                         |
| timestamp       | BigInt! | Fx token mapping timestamp                     |
| transactionHash | Bytes!  | Fx transaction hash                            |

## FxTokenMappingCounter

| Field   | Type    | Description                        |
| ------- | ------- | ---------------------------------- |
| id      | ID!     | Fx token mapping ID                |
| current | BigInt! | Current count for fx token mapping |

## FxDeposit

| Field           | Type    | Description                               |
| --------------- | ------- | ----------------------------------------- |
| id              | ID!     | Fx deposit ID                             |
| counter         | BigInt! | Fx deposit counter                        |
| contractAddress | Bytes!  | Contract address that handles fx deposits |
| rootToken       | Bytes!  | Root token address                        |
| tokenType       | String! | Token contract address                    |
| depositor       | Bytes!  | Address of the depositor                  |
| userAddress     | Bytes!  | User address                              |
| amount          | BigInt! | Amount of fx deposited in the transaction |
| tokenId         | BigInt! | Token ID                                  |
| timestamp       | BigInt! | Block timestamp                           |
| transactionHash | Bytes!  | Fx transaction hash                       |

## FxDepositCounter

| Field   | Type    | Description                  |
| ------- | ------- | ---------------------------- |
| id      | ID!     | Fx deposit counter ID        |
| current | BigInt! | Current number of FxDeposits |

## FxWithdraw

| Field           | Type    | Description                               |
| --------------- | ------- | ----------------------------------------- |
| id              | ID!     | Fx withdraw ID                            |
| counter         | BigInt! | Fx withdraw counter                       |
| contractAddress | Bytes!  | Contract address that handles withdrawals |
| rootToken       | Bytes!  | Root token address                        |
| childToken      | Bytes!  | Child token address                       |
| tokenType       | String! | Token contract address                    |
| userAddress     | Bytes!  | User address                              |
| amount          | BigInt! | Amount of fx withdrawn in the transaction |
| tokenId         | BigInt! | Token ID                                  |
| timestamp       | BigInt! | Block timestamp                           |
| transactionHash | Bytes!  | Fx transaction hash                       |

## FxWithdrawCounter

| Field   | Type    | Description                     |
| ------- | ------- | ------------------------------- |
| id      | ID!     | Fx withdraw counter ID          |
| current | BigInt! | Current number of FxWithdrawals |

## Validator

| Field             | Type     | Description                                                      |
| ----------------- | -------- | ---------------------------------------------------------------- |
| id                | ID!      | Validator ID                                                     |
| validatorId       | BigInt!  | Validator ID                                                     |
| owner             | Bytes!   | Address of the owner                                             |
| signer            | Bytes!   | Address of the signer                                            |
| signerPubKey      | Bytes!   | Public key of the signer                                         |
| liquidatedRewards | BigInt!  | Liquidated reward for the validator                              |
| activationEpoch   | BigInt!  | Epoch validation was activated                                   |
| deactivationEpoch | BigInt!  | Epoch validation was deactivated                                 |
| totalStaked       | BigInt!  | Total amount of tokens staked                                    |
| selfStake         | BigInt!  | Amount staked by the validator                                   |
| delegatedStake    | BigInt!  | Amount delegated to the validator for staking                    |
| commissionRate    | BigInt!  | Commission rate                                                  |
| nonce             | BigInt!  | Transaction nonce                                                |
| status            | Int!     | Status codes: 0 - staked, 1 - unstaked, 2 - jailed, 3 - unjailed |
| jailEndEpoch      | BigInt!  | Epoch where validator is unjailed                                |
| auctionAmount     | BigInt!  | Auction amount                                                   |
| isInAuction       | Boolean! | Checks whether validator is in auction                           |

## StakeUpdate

| Field           | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| id              | ID!     | Stake update ID                  |
| validatorId     | BigInt! | Validator ID                     |
| totalStaked     | BigInt! | Total amount staked by validator |
| block           | BigInt! | Block number                     |
| nonce           | BigInt! | Transaction nonce                |
| transactionHash | Bytes!  | Transaction hash                 |
| logIndex        | BigInt! | Log index number                 |

## GlobalDelegatorCounter

| Field   | Type    | Description                                                                    |
| ------- | ------- | ------------------------------------------------------------------------------ |
| id      | ID!     | Global delegator counter ID                                                    |
| current | BigInt! | Keeps track of current delegator counter i.e. delegators are present as of now |

## Delegator

| Field           | Type    | Description                                                                 |
| --------------- | ------- | --------------------------------------------------------------------------- |
| id              | ID!     | Delegator ID                                                                |
| counter         | BigInt! | Traverse through large number of delegator list                             |
| validatorId     | BigInt! | Validator ID                                                                |
| address         | Bytes!  | Delegator address                                                           |
| delegatedAmount | BigInt! | Total delegated amount                                                      |
| unclaimedAmount | BigInt! | total unclaimed amount (after sellVoucher and before claiming it)           |
| claimedAmount   | BigInt! | total claimed amount (after withdraw delay, while claiming unstaked amount) |
| tokens          | BigInt! | total current shares (works until tokens are non-transferable)              |
| claimedRewards  | BigInt! | Total claimed rewards                                                       |

## Topup

| Field          | Type    | Description       |
| -------------- | ------- | ----------------- |
| id             | ID!     | Heimdall topup ID |
| address        | Bytes!  | Merkle root hash  |
| topupAmount    | BigInt! | Topup amount      |
| withdrawAmount | BigInt! | Amount withdrawn  |

## StakingNFTTransfer

| Field             | Type      | Description                        |
| ----------------- | --------- | ---------------------------------- |
| id                | ID!       | Staking NFT transfer ID            |
| tokenId           | BigInt!   | NFT ID                             |
| currentOwner      | Bytes!    | Current owner address              |
| previousOwners    | [Bytes!]! | Array of previous owners addresses |
| transactionHashes | [Bytes!]! | Array of transaction hashes        |

## DelegatorUnbond

| Field                  | Type     | Description                                |
| ---------------------- | -------- | ------------------------------------------ |
| id                     | ID!      | Delegator unbond ID                        |
| nonce                  | BigInt!  | Transaction nonce                          |
| validatorId            | BigInt!  | Validator ID                               |
| user                   | Bytes!   | Delegator address                          |
| amount                 | BigInt!  | Total amount                               |
| tokens                 | BigInt!  | Token amount                               |
| completed              | Boolean! | Checks whether unbond is complete          |
| unbondStartedTXHash    | Bytes!   | Transaction hash when unbond was initaited |
| unbondStartedTimeStamp | BigInt!  | Timestamp when when unbond was initaited   |
| unbondClaimedTXHash    | Bytes!   | Transaction hash when unbond was claimed   |
| unbondClaimedTimeStamp | BigInt!  | Timestamp when unbond was claimed          |
| activeStake            | BigInt!  | Active stake                               |

## MaticTransfer

| Field           | Type    | Description                 |
| --------------- | ------- | --------------------------- |
| id              | ID!     | Matic transfer ID           |
| token           | Bytes!  | Token address               |
| from            | Bytes!  | Sender address              |
| to              | Bytes!  | Receiver address            |
| value           | BigInt! | Amount of matic transferred |
| block           | BigInt! | Transaction block           |
| timestamp       | BigInt! | Transaction timestamp       |
| transactionHash | Bytes!  | Transaction hash            |

## GlobalDelegationCounter

| Field   | Type    | Description                   |
| ------- | ------- | ----------------------------- |
| id      | ID!     | Delegation counter ID         |
| current | BigInt! | Current number of delegations |

## Delegation

| Field           | Type    | Description                                     |
| --------------- | ------- | ----------------------------------------------- |
| id              | ID!     | Delegation ID                                   |
| counter         | BigInt! | Traverse through large number of delegator list |
| validatorId     | BigInt! | Validator ID                                    |
| address         | Bytes!  | Delegator address                               |
| timestamp       | BigInt! | Transaction timestamp                           |
| transactionHash | Bytes!  | Delegation transaction hash                     |
| amount          | BigInt! | Delegation amount                               |
| block           | BigInt! | Transaction block                               |
| activeStake     | BigInt! | Active stake                                    |
