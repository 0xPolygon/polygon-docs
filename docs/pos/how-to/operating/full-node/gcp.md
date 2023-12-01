Deploying Polygon nodes on a Virtual Machine (VM) instance in the Google Cloud Platform (GCP) is a straightforward process. This guide focuses on Ubuntu 20.04, a modern OS with long-term support, but the steps are adaptable to Debian 11 or other similar distributions.

## Deploying a VM instance on Google Cloud Platform

To create a VM instance on GCP, you can use either the Google Cloud CLI or the Web Console. This guide will detail the process using the Google Cloud CLI.

1. **Preparation**:
   - Install and configure the `gcloud` command-line tool. Follow the [official guide](https://cloud.google.com/compute/docs/instances/create-start-instance#before-you-begin) for detailed instructions.
   - Choose a default region and zone close to your target audience. Use [gcping.com](https://gcping.com) to find the lowest latency location.

2. **Configure Variables**:
   - Edit the following variables according to your requirements:
     - `POLYGON_NETWORK`: Choose `mainnet` or `mumbai` testnet.
     - `POLYGON_NODETYPE`: Select the node type, e.g., `archive` or `fullnode`.
     - `POLYGON_BOOTSTRAP_MODE`: Choose the bootstrap mode, either `snapshot` or `from_scratch`.
     - `POLYGON_RPC_PORT`: Set the JSON RPC port for the Bor node, defaulting to the VM's creation settings and firewall rules.
     - `EXTRA_VAR`: Specify Bor and Heimdall branches. Use `network_version=mainnet-v1` for mainnet and `network_version=testnet-v4` for the Mumbai network.
     - `INSTANCE_NAME`: Name your VM instance.
     - `INSTANCE_TYPE`: Choose a [GCP machine type](https://cloud.google.com/compute/docs/machine-types).
     - `BOR_EXT_DISK_SIZE`: Set the additional disk size for Bor, with 1024GB recommended for full nodes. Archive nodes require 8192GB+.
     - `HEIMDALL_EXT_DISK_SIZE`: Additional disk size for Heimdall.
     - `DISK_TYPE`: Choose a [disk type](https://cloud.google.com/compute/docs/disks#disk-types), with SSD recommended.

3. **Create the Instance**:
   - Run the following command, adjusted for your chosen network, node type, and configuration:

     ```bash
     # Export configuration variables
     export [VARIABLES]

     # Create firewall rules for Polygon
     gcloud compute firewall-rules create [...]

     # Deploy the VM instance
     gcloud compute instances create [COMMANDS]
     ```

   - This command initializes the instance with the required hardware and software settings.

## Logging in to the VM

After deploying the VM, software installation and snapshot downloading (if chosen) will take some time.

- **Checking the Node Processes**:
  - Use `gcloud compute ssh ${INSTANCE_NAME}` to access the VM.
  - Once logged in, check the Bor and Heimdall processes and disk usage with:

    ```bash
    sudo su -
    ps uax|egrep "bor|heimdalld"
    df -l -h
    ```

- **Monitoring Installation Progress**:
  - Inside the VM, use `screen -dr` to watch the installation.
  - Detach from the screen session with `Control+a d`.

- **Viewing Logs**:
  - To monitor Bor and Heimdall logs, execute:

    ```bash
    journalctl -fu bor
    journalctl -fu heimdalld
    ```

!!! note

    Blockchain data is stored on additional drives, retained by default when the VM is removed. Manually delete these disks if they are no longer needed.

Upon completion, your GCP console should display the newly created Polygon node instance, similar to the illustration below.

<img src="/img/pos/polygon-instance.svg" />

This guide provides a detailed walkthrough for deploying Polygon nodes on GCP, ensuring a smooth and efficient setup.
