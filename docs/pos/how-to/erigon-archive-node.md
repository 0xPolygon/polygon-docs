---
comments: true
---

## System requirements

- CPU: 16-core, 64-bit architecture
- RAM: 64GB
- Storage
    - Basically `io1` or above with at least 20k+ iops and RAID-0 based disk structure
    - Mainnet archive node: 15TB
    - Amoy testnet archive node: 1TB
    - SSD or NVMe. Bear in mind that SSD performance deteriorates when close to capacity.
- Golang: >= v1.20
- GCC: >= v10

!!! tip "HDD not recommended"

    On HDDs, Erigon will always remain *N* blocks behind the chain tip, but will not fall further behind. 


## Install Erigon client

Run the following commands to install Erigon:

```bash
git clone --recurse-submodules -j8 https://github.com/ledgerwatch/erigon
cd erigon
git checkout v2.57.3
make erigon
```

This should create the binary at `./build/bin/erigon`

## Start Erigon client

If you're deploying to mainnet, run the following command:

```bash
erigon --chain=bor-mainnet --db.size.limit=12TB --db.pagesize=16KB # remaining flags follow
```

When connecting to Amoy testnet, use the following command to start your Erigon client:

```bash
erigon --chain=amoy
```

## Configure Erigon client

If you want to store Erigon files in a non-default location, use `-datadir` to specify a new location:
    
```bash
erigon --chain=amoy --datadir=<your_data_dir>
```
    
If you are not using local **heimdall**, use `-bor.heimdall=<your heimdall url>`. By default, it will try to connect to `localhost:1317`.
    
```bash
erigon --chain=amoy --bor.heimdall=<your heimdall url> --datadir=<your_data_dir>
```

## Node RPC

- If you want to connect to PoS Amoy Testnet, use: [https://heimdall-api-amoy.polygon.technology](https://heimdall-api-amoy.polygon.technology)

- For PoS mainnet, use: [https://heimdall-api.polygon.technology](https://heimdall-api.polygon.technology)

!!! tip 

    Remote heimdall is better suited for testing, and is not recommended for production use. 

## Tips for faster sync

- Use the machine with high IOPS and RAM for the faster initial sync
- Memory optimized nodes are recommended for faster sync. For example, AWS EC2 `r5` or `r6` series instances.

## Reporting issues

In case you encounter any issues and are looking for support, please get in touch with the Erigon team. More details available in [the Erigon GitHub README](https://github.com/ledgerwatch/erigon?tab=readme-ov-file#getting-in-touch).