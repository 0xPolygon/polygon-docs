## Hardware

- A Linux-based OS (e.g., Ubuntu Server 22.04 LTS).
- At least 16GB RAM with a 4-core CPU.
- An AMD64 architecture system.

!!! info "Computing resources"
    - Running a full prover is an enterprise level installation and extremely resource-heavy. 
    - These instructions run the mock prover instead.

## Software

The commands on the [install dependencies page](install-dependencies.md) fulfill all software requirements.

### Mock prover requirements

!!! info
    The mock prover is a light resource by skipping validation and instead adding a `Valid ✅` checkmark to every batch.

- 4-core CPU
- 8GB RAM (16GB recommended)

## Miscellaneous requirements

- `INFURA_API_KEY`: [Infura](https://infura.io/) API key
- `ETHERSCAN_API_KEY`: [Etherscan](https://etherscan.io/) API key
- Goërli node RPC URL: e.g. https://goerli.infura.io/v3/YOUR-INFURA-API-KEY
- Goërli account address holding minimum 0.5 GoërliETH