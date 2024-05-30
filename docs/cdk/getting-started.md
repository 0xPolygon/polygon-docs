# Get Started

This getting started guide will walk you through the process of setting up a Layer 2 blockchain using the Polygon CDK on your local machine, running the components in Docker containers.

## Setting Up Your Environment

To run the Polygon CDK locally, the following prerequisites are required:

**Hardware Requirements:**

- A Linux-based Operating System (or [WSL](https://learn.microsoft.com/en-us/windows/wsl/about))
- Minimum 8GB RAM and 2-core CPU
- An AMD64 architecture system

**Software Dependencies:**

- [Docker Engine](https://docs.docker.com/engine/) (version 4.27 or higher)
- [Kurtosis CLI](https://docs.kurtosis.com/install/)
- [Foundry](https://book.getfoundry.sh/getting-started/installation)
- Optional: [yq](https://github.com/mikefarah/yq), [jq](https://stedolan.github.io/jq/), and [polycli](https://github.com/maticnetwork/polygon-cli) help submit transactions and interact with the environment.

## Exploring the CDK Kurtosis Package

The [Polygon CDK Kurtosis Package](https://github.com/0xPolygon/kurtosis-cdk/) allows you to easily customize and instantiate all of the components of a CDK chain. It uses the [Kurtosis](https://docs.kurtosis.com/) tool to orchestrate the setup of the chain components in Docker containers, with logic defined in [Starlark](https://github.com/bazelbuild/starlark) (a Python dialect) scripts to define the step-by-step process of setting up the chain.

### Cloning the Repository

To get started, clone the repository and navigate to the `kurtosis-cdk` directory:

```bash
git clone https://github.com/0xPolygon/kurtosis-cdk.git
cd kurtosis-cdk
```

### Checking Your Environment

Ensure Docker is running on your machine, then run the following command to confirm all prerequisites are installed:

```bash
sh scripts/tool_check.sh
```

If everything is installed correctly, you should see the following output:

```bash
Checking that you have the necessary tools to deploy the Kurtosis CDK package...
✅ kurtosis is installed, meets the requirement (=0.89).
✅ docker is installed, meets the requirement (>=24.7).

You might as well need the following tools to interact with the environment...
✅ jq is installed.
✅ yq is installed, meets the requirement (>=3.2).
✅ cast is installed.
✅ polycli is installed.

🎉 You are ready to go!
```

### Customizing Your Chain

To begin understanding the codebase, there are two key files to inspect:

1. [main.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/main.star): The script that defines what steps to take to set up the chain on your machine.
2. [params.yml](https://github.com/0xPolygon/kurtosis-cdk/blob/main/params.yml): The main configuration file that defines the parameters of the chain.

#### main.star

The `main.star` file defines the step-by-step instructions of the deployment process. It is the main "hub" of the chain setup process; orchestrating the setup of all the components in sequential order by pulling in necessary logic from other files.

It defines the following steps for the deployment process:

| Step Number | Deployment Step                                                                            | Relevant Starlark Code                                                                                               | Enabled by Default |
| ----------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
| 1           | Deploy a local layer 1 devnet chain                                                        | [ethereum.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/ethereum.star)                                   | True               |
| 2           | Deploy the zkEVM smart contracts on the L1                                                 | [deploy_zkevm_contracts.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/deploy_zkevm_contracts.star)       | True               |
| 3           | Deploy the zkEVM node and CDK peripheral databases                                         | [databases.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/databases.star)                                 | True               |
| 4           | Deploy the CDK central environment                                                         | [cdk_central_environment.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_central_environment.star)     | True               |
| 5           | Deploy the bridge infrastructure                                                           | [cdk_bridge_infrastructure.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_bridge_infra.star)          | True               |
| 6           | Deploy the permissionless node                                                             | [zkevm_permissionless_node.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/zkevm_permissionless_node.star) | False              |
| 7           | Deploy the observability stack                                                             | [observability.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/observability.star)                         | True               |
| 8           | Deploy the block explorer                                                                  | [blockscout.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/blockscout.star)                               | False              |
| 9           | Apply a load test to the chain                                                             | [load_test.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/workload.star)                                  | False              |
| 10          | Deploy [Blutgang](https://github.com/rainshowerLabs/blutgang) for load balancing & caching | [cdk_blutgang.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_blutgang.star)                           | False              |

You can customize (or skip) the logic for each of these steps by modifying the logic in the respective files.

#### params.yml

The `params.yml` file defines the parameters of the chain and the deployment process. It includes configurations for simple parameters such as the chain ID and more complex configurations such as the gas token smart contract address.

You can modify each of these parameters to customize the chain to your specific needs.

## Running the Chain Locally

First run the [kurtosis clean](https://docs.kurtosis.com/clean) to remove any existing Kurtosis environments:

```bash
kurtosis clean --all
```

Then, in the `kurtosis-cdk` directory, use the [kurtosis run](https://docs.kurtosis.com/run) command to deploy the chain on your local machine by executing the `main.star` script provided with the `params.yml` configuration file:

```bash
kurtosis run --enclave cdk-v1 --args-file params.yml --image-download always .
```

!!! info

     - `--enclave cdk-v1` specifies the name of the [enclave](https://docs.kurtosis.com/advanced-concepts/enclaves/) (isolated environment) to use for the deployment process.
     - `--args-file params.yml` specifies the configuration file to use for the deployment process.
     - `--image-download always` specifies to always download the latest Docker images for the deployment process.

This command typically takes around 10 minutes to complete and outputs the logs of each step in the deployment process for you to monitor the progress of the chain setup. Once the command is complete, you should see the following output:

```bash
Starlark code successfully run. No output was returned.

===============================================
||          Created enclave: cdk-v1          ||
===============================================
Name:            cdk-v1
Status:          RUNNING

========================================= Files Artifacts =========================================

... List of files generated during the deployment process ...

========================================== User Services ==========================================

... List of services with "RUNNING" status - none should be "FAILED"! ...

```

Run `kurtosis enclave inspect cdk-v1` to see the status of the enclave and the services running within it at any time.

## Interacting with the Chain

Now that your chain is running, you can explore and interact with each component!

Below are a few examples of how you can interact with the chain.

### Sending Test Transactions

Let&rsquo;s perform some basic read and write operations on the L2 using Foundry.

Export the RPC URL of your L2 to an environment variable called `ETH_RPC_URL` with the following command:

```bash
export ETH_RPC_URL="$(kurtosis port print cdk-v1 zkevm-node-rpc-001 http-rpc)"
```

Then, use `cast` to view information about the chain, such as the latest block number:

```bash
cast block-number
```

View the balance of an address, such as the pre-funded admin account:

```bash
cast balance --ether 0xE34aaF64b29273B7D567FCFc40544c014EEe9970
```

Send simple transactions to the chain, such as a transfer of some ETH:

```bash
cast send --legacy --value 0.01ether 0x0000000000000000000000000000000000000000 --private-key "0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625"
```

!!! info

      The `0xE34...9970` and `0x12d...c625` public-private key pair used in the above commands is the default admin account configured in `params.yml`.

### Load Testing the Chain

Use the [polycli loadtest](https://github.com/maticnetwork/polygon-cli/blob/main/doc/polycli_loadtest.md) command to send multiple transactions at once to the chain to test its performance:

```bash
polycli loadtest --rpc-url "$ETH_RPC_URL" --legacy --verbosity 700 --requests 500 --rate-limit 5 --mode t --private-key "0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625"
```

### Viewing Transaction Finality

A common way to check the status of the system is to ensure that batches are being sent and verified on the L1 chain.

Use `cast` to view the progression of batches from trusted, virtual, and verified states:

```bash
cast rpc zkevm_batchNumber          # Latest batch number on the L2
cast rpc zkevm_virtualBatchNumber   # Latest batch received on the L1
cast rpc zkevm_verifiedBatchNumber  # Latest batch verified or "proven" on the L1
```

### Opening the Bridge UI

To open the bridge interface and bridge tokens across the L1 and L2, run the following command:

```bash
open $(kurtosis port print cdk-v1 zkevm-bridge-proxy-001 bridge-interface)
```

### Viewing Chain Metrics

To view information such as how many transactions are being processed, the amount of gas being used, the time since a batch was last verified, how many addresses have bridged, and much more, a Grafana dashboard is included in the deployed observability stack which can be opened by running the following command:

```bash
open $(kurtosis port print cdk-v1 grafana-001 dashboards)
```

From the hamburger menu, navigate to `Dashboards` and select the `Panoptichain` dashboard to view all of the metrics.

![Panoptichain Dashboard](../img/cdk/grafana.png)

### Stopping the Chain

If you want to **stop** the chain and remove all the containers, run the following command:

```bash
kurtosis clean --all
```

## Going to Production

While it is possible to run a CDK chain on your own, we strongly recommend getting in touch with one of our [Implementation Providers](https://ecosystem.polygon.technology/spn/cdk/) for production deployments.

## Dive Deeper into the CDK

For more detailed information on the CDK&rsquo;s architecture, components, and how to customize your chain, refer to the [CDK architecture documentation](https://docs.polygon.technology/cdk/architecture/cdk-zkevm/).
