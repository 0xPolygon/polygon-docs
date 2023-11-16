[comment]: <> (data comes from here: https://www.notion.so/polygontechnology/CDK-Validium-TPS-Analysis-8aafda0d6b824c3781270cca30a8f70d#c6725ef8b93748ea8879d7e49e67c2fc and results are marked as OLD.. SME > @ruchawalawalkar)

## Strategy

The team calculated transactions-per-second, `tps`, for three transaction types:

- **EOA to EOA**: Simple value transfers between user accounts.
- **ERC20**: Token transfers, simulating the exchange of tokens on the network.
- **ERC721**: Non-fungible token (NFT) transfers representing the exchange of unique digital assets.

## Environment

The tests ran on the following configurations:

### CDK validium test

| Component (Service) | Instance Type | Instance Count | vCPUs | RAM (GB) | Disk Size (GB) | Disk Type |
| --- | --- | --- | --- | --- | --- | --- |
| Sequencer | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| RPC Node | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| Executor | c2-standard-16 | 1 | 16 | 64 | 100 | SSD persistent disk |
| Aggregator | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| Prover | n2-highmem-128 | 1 | 128 | 864 | 500 | SSD persistent disk |
| Synchronizer | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| SequenceSender | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| ETH TX Manager | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| L2 Gas Pricer | n2d-custom-8-16384 | 1 | 8 | 16 | 30 | Balanced persistent disk |
| HashDB Node | c2-standard-16 | 1 | 16 | 64 | 100 | SSD persistent disk |
| Data Availability | n2d-custom-8-16384 | 4 | 8 | 16 | 30 | Balanced persistent disk |

### Cloud SQL DB

| DB Instance | vCPUs | RAM (GB) | Size (GB) | Count |
| --- | --- | --- | --- | --- |
| zkEVM DB | 16 | 60 | 100 | 1 |
| contains: | State DB | 100 (Shared) |  |  |
|  | Pool DB | 100 (Shared) |  |  |
|  | Prover DB | 100 (Shared) |  |  |

## Results

### Key

- `mode`: Type of transaction.
- `concurrency`: Number of concurrent requests.
- `requests`: Number of requests over the benchmarking session. 
- `rate-limit`: Overall limit to the number of requests per second. 

### Results (OLD?)

| `tps` | `mode` | `concurrency` | `requests` | `rate-limit` | `total requests` | `notes` |
| --- | --- | --- | --- | --- | --- | --- |
| 6.269592476 | t (EOA Transactions) | 20 | 100 | 0 (disabled) | 2000 |  |
| 12.6984127 | t (EOA Transactions) | 20 | 200 | 0 (disabled) | 4000 |  |
| 0 | t (EOA Transactions) | 50 | 500 | 0 (disabled) | 25000 | ERRORED (see note) |
| 17.27115717 | t (EOA Transactions) | 20 | 500 | 0 (disabled) | 10000 |  |
| 20.13422819 | t (EOA Transactions) | 30 | 500 | 0 (disabled) | 15000 |  |
| 24.8447205 | t (EOA Transactions) | 40 | 500 | 0 (disabled) | 20000 |  |
| 20.51983584 | t (EOA Transactions) | 30 | 1000 | 0 (disabled) | 30000 |  |
| 18.71804452 | t (EOA Transactions) | 30 | 100000 | 0 (disabled) | 3000000 |  |
| 14.82799526 | t (EOA Transactions) | 50 | 1000 | 0 (disabled) | 50000 |  |
| 8.650519031 | t (EOA Transactions) | 50 | 100 | 100 | 5000 |  |
| 16.20745543 | t (EOA Transactions) | 40 | 500 | 0 (disabled) | 20000 | DUPLICATE OF TEST10 |
| 8.896797153 | t (EOA Transactions) | 20 | 2000 | 0 (disabled) | 40000 |  |
| 27.02702703 | t (EOA Transactions) | 10 | 100 | 50 | 1000 | Test ran on n2-standard-8 |
| 29.19708029 | t (EOA Transactions) | 20 | 200 | 50 | 4000 | Test ran on n2-standard-8, with increase AccountQueue and GlobalQueue |
| 36.86635945 | t (EOA Transactions) | 20 | 400 | 50 | 8000 |  |
| 29.19708029 | t (EOA Transactions) | 20 | 200 | 0 (disabled) | 4000 |  |
| 32.78688525 | t (EOA Transactions) | 50 | 200 | 0 (disabled) | 10000 |  |
| 29.19708029 | t (EOA Transactions) | 20 | 200 | 0 (disabled) | 4000 |  |
| 17.13062099 | t (EOA Transactions) | 20 | 400 | 50 | 8000 |  |
| 14.28571429 | 2 (ERC20 Transactions) | 10 | 100 | 0 (disabled) | 1000 |  |
| 18.01801802 | 2 (ERC20 Transactions) | 20 | 200 | 0 (disabled) | 4000 |  |
| 13.98601399 | 2 (ERC20 Transactions) | 30 | 200 | 40 | 6000 |  |
| 17.66004415 | 2 (ERC20 Transactions) | 20 | 400 | 30 | 8000 |  |
| 17.54385965 | 2 (ERC20 Transactions) | 20 | 500 | 30 | 10000 |  |
| 17.76198934 | 2 (ERC20 Transactions) | 20 | 500 | 40 | 10000 |  |
| 17.51313485 | 2 (ERC20 Transactions) | 20 | 500 | 50 | 10000 |  |
| 17.76198934 | 2 (ERC20 Transactions) | 20 | 500 | 100 | 10000 |  |
| 0 | 2 (ERC20 Transactions) | 30 | 500 | 100 | 15000 | ERRORED (resource exhausted) |
| 17.36111111 | 2 (ERC20 Transactions) | 20 | 1000 | 0 (disabled) | 20000 |  |
| 17.33102253 | 2 (ERC20 Transactions) | 20 | 1500 | 0 (disabled) | 30000 |  |
| 18.61330852 | 2 (ERC20 Transactions) | 20 | 2000 | 0 (disabled) | 40000 |  |
| 17.24732666 | 2 (ERC20 Transactions) | 20 | 2500 | 0 (disabled) | 50000 |  |
| 4.545454545 | 7 (ERC721 Transactions) | 10 | 100 | 0 (disabled) | 1000 |  |
| 6.097560976 | 7 (ERC721 Transactions) | 10 | 200 | 0 (disabled) | 2000 |  |
| 12.86173633 | 7 (ERC721 Transactions) | 20 | 200 | 0 (disabled) | 4000 |  |
| 13.14060447 | 7 (ERC721 Transactions) | 20 | 500 | 0 (disabled) | 10000 |  |
| 0 | 7 (ERC721 Transactions) | 30 | 200 | 0 (disabled) | 6000 | ERRORED (resource exhausted) |
| 14.18439716 | 7 (ERC721 Transactions) | 20 | 1000 | 0 (disabled) | 20000 |  |
| 12.39669421 | 7 (ERC721 Transactions) | 20 | 1500 | 0 (disabled) | 30000 |  |
| 13.81692573 | 7 (ERC721 Transactions) | 20 | 2000 | 0 (disabled) | 40000 |  |
| 13.49892009 | 7 (ERC721 Transactions) | 20 | 2500 | 0 (disabled) | 50000 |  |

## Conclusions

TODO: summary of data results

## Comparison with competitors

TODO: in progress


