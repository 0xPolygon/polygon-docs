---
comments: true
---

When setting up a new sentry, validator, or full node server, it is recommended that you use snapshots for faster syncing without having to sync over the network. Using snapshots will save you several days for both Heimdall and Bor. 

## Community snapshots

Polygon PoS has transitioned to a community-driven model for snapshots. Active community members now contribute to provide snapshots. Some of these members include:

| Name                                                                  | Available snapshots   | Note                                         |
| --------------------------------------------------------------------- | --------------------- | -------------------------------------------- |
| Stakecraft                                                            | Mainnet, Amoy, Erigon | Support for Erigon archive snapshot          |
| [PublicNode (by Allnodes)*](https://publicnode.com/snapshots#polygon) | Mainnet, Amoy         | Support for PBSS + PebbleDB enabled snapshot |
| Stakepool                                                             | Mainnet, Amoy         | -                                            |
| Vaultstaking                                                          | Mainnet               | -                                            |
| Girnaar Nodes                                                         | Amoy                  | -                                            |

> *\*The PBSS + PebbleDB snapshot provided by PublicNode is currently in the beta phase.*

!!! info "Snapshot aggregator"

    Visit [All4nodes.io](https://all4nodes.io/Polygon) for a comprehensive list of community snapshots.

## Downloading and using client snapshots

To begin, ensure that your node environment meets the **prerequisites** outlined [here](../how-to/full-node/full-node-binaries.md). 

The majority of snapshot providers have also outlined the steps that need to be followed to download and use their respective client snapshots. Navigate to [All4nodes](https://all4nodes.io/Polygon) to view the snapshot source. 

In case the steps are unavailable or the procedure is unclear, the following tips will come in handy:

- You can use the `wget` command to download and extract the `.tar` snapshot files. For example:

```bash
wget -O - snapshot_url_here | tar -xvf -C /target/directory
```

- Configure your client's `datadir` setting to match the directory where you downloaded and extracted the snapshot data. This ensures the `systemd` services can correctly register the snapshot data when the client is spun up.

- To maintain your client's default configuration settings, consider using symbolic links (symlinks).

## Example

Let's say you have mounted your block device at `~/snapshots` and have downloaded and extracted the chain data into the `heimdall_extract` directory for Heimdall, and into the `bor_extract` directory for Bor. Use the following commands to register the extracted data for Heimdall and Bor `systemd` services:

```bash
# remove any existing datadirs for Heimdall and Bor
rm -rf /var/lib/heimdall/data
rm -rf /var/lib/bor/chaindata

# rename and setup symlinks to match default client datadir configs
mv ~/snapshots/heimdall_extract ~/snapshots/data
mv ~/snapshots/bor_extract ~/snapshots/chaindata
sudo ln -s ~/snapshots/data /var/lib/heimdall
sudo ln -s ~/snapshots/chaindata /var/lib/bor

# bring up clients with all snapshot data properly registered
sudo service heimdalld start
# wait for Heimdall to fully sync then start Bor
sudo service bor start
```

!!! tip "Appropriate user permissions"
    
    Ensure that the Bor and Heimdall user files have appropriate permissions to access the `datadir`. To set correct permissions for Bor, execute `sudo chown -R bor:nogroup /var/lib/heimdall/data`. Similarly, for Heimdall, run `sudo chown -R heimdall:nogroup /var/lib/bor/data/bor`

## Recommended disk size guidance

### Polygon Amoy testnet

| Metric                            | Calculation Breakdown               | Value   |
| --------------------------------- | ----------------------------------- | ------- |
| approx. compressed total          | 250 GB (Bor) + 35 GB (Heimdall)     | 285 GB  |
| approx. data growth daily         | 10 GB (Bor) + 0.5 GB (Heimdall)     | 10.5 GB |
| approx. total extracted size      | 350 GB (Bor) + 50 GB (Heimdall)     | 400 GB  |
| suggested disk size (2.5x buffer) | 400 GB * 2.5 (natural chain growth) | 1 TB    |

### Polygon mainnet

| Metric                            | Calculation Breakdown             | Value   |
| --------------------------------- | --------------------------------- | ------- |
| approx. compressed total          | 3000 GB (Bor) + 500 GB (Heimdall) | 3500 GB |
| approx. data growth daily         | 100 GB (Bor) + 5 GB (Heimdall)    | 105 GB  |
| approx. total extracted size      | 4 TB (Bor) + 500 GB (Heimdall)    | 4.5 TB  |
| suggested disk size (2.5x buffer) | 4 TB * 2 (natural chain growth)   | 8 TB    |

### Polygon Amoy Erigon archive

| Metric                            | Calculation Breakdown               | Value  |
| --------------------------------- | ----------------------------------- | ------ |
| approx. compressed total          | 210 GB (Erigon) + 35 GB (Heimdall)  | 245 GB |
| approx. data growth daily         | 4.5 GB (Erigon) + 0.5 GB (Heimdall) | 5 GB   |
| approx. total extracted size      | 875 GB (Erigon) + 50 GB (Heimdall)  | 925 GB |
| suggested disk size (2.5x buffer) | 925 GB * 2.5 (natural chain growth) | 2.5 TB |

## Recommended disk type and IOPS guidance

- Disk IOPS will affect the speed of downloading/extracting snapshots, getting in sync, and performing LevelDB compaction.
- To minimize disk latency, direct-attached storage is ideal.
- In AWS, when using gp3 disk types, we recommend provisioning IOPS of 16,000 and throughput of 1,000. This minimizes costs while providing significant performance benefits. io2 EBS volumes with matching IOPS and throughput values offer similar performance.
- For GCP, we recommend using performance (SSD) persistent disks (`pd-ssd`) or extreme persistent disks (`pd-extreme`) with similar IOPS and throughput values as mentioned above.
