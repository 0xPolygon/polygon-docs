---
hide:
  - toc
---

# Get Started

This getting started guide will walk you through the process of setting up a Layer 2 blockchain using the Polygon CDK on your local machine, running the components in Docker containers.

## Setting Up Your Environment

To run the Polygon CDK locally, the following prerequisites are required:

**Hardware Requirements:**

- A Linux-based Operating System (or [WSL](https://learn.microsoft.com/en-us/windows/wsl/about))
- 8GB RAM with a 2-core CPU
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
✅ kurtosis 0.89.12 is installed, meets the requirement (=0.89).
✅ docker 25.0.3 is installed, meets the requirement (>=24.7).

You might as well need the following tools to interact with the environment...
✅ jq 1.7.1 is installed.
✅ yq 3.2.3 is installed, meets the requirement (>=3.2).
✅ cast 0.2.0 is installed.
✅ polycli v0.1.43-5-g73ad3f4 is installed.

🎉 You are ready to go!
```

### Customizing Your Chain

To begin understanding the codebase, there are two key files to inspect:

1. [main.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/main.star): The script that defines what steps to take to set up the chain on your machine.
2. [params.yml](https://github.com/0xPolygon/kurtosis-cdk/blob/main/params.yml): The main configuration file that defines the parameters of the chain.

#### main.star

The `main.star` file defines the step-by-step process of the deployment process. It is the main "hub" of the chain setup process; orchestrating the setup of all the components in sequential order by pulling in necessary logic from other files.

By default, this script performs the following steps:

1. Deploy a local layer 1 devnet chain ([ethereum.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/ethereum.star))
2. Deploy the zkEVM smart contracts on the L1 ([deploy_zkevm_contracts.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/deploy_zkevm_contracts.star))
3. Deploy the zkEVM node and CDK peripheral databases ([databases.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/databases.star))
4. Deploy the CDK central environment ([cdk_central_environment.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_central_environment.star))
5. Deploy the bridge infrastructure ([cdk_bridge_infrastructure.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_bridge_infra.star))
6. Deploy the permissionless node ([zkevm_permissionless_node.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/zkevm_permissionless_node.star))
7. Deploy the observability stack and block explorer ([observability.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/observability.star) and [blockscout.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/blockscout.star))
8. Apply a load test to the chain ([load_test.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/workload.star))
9. Deploy [Blutgang](https://github.com/rainshowerLabs/blutgang) for load balancing & caching ([cdk_blutgang.star](https://github.com/0xPolygon/kurtosis-cdk/blob/main/cdk_blutgang.star))

You can customize (or skip) the logic for each of these steps by modifying the logic in the respective files.

#### params.yml

The `params.yml` file defines the parameters of the chain and the deployment process. It includes configurations for simple parameters such as the chain ID and more complex configurations such as the gas token smart contract address.

You can modify each of these parameters to customize the chain to your specific needs.

## Running the Chain Locally

Use the [kurtosis clean](https://docs.kurtosis.com/clean) and [kurtosis run](https://docs.kurtosis.com/run) commands to begin the deployment process. Run the following commands to begin executing the `main.star` script and start the deployment process:

```bash
kurtosis clean --all
kurtosis run --enclave cdk-v1 --args-file params.yml --image-download always .
```

This command typically takes around 10 minutes to complete. It will output the logs of each step in the deployment process, allowing you to monitor the progress of the chain setup.

!!! info

     - `--encalve cdk-v1` specifies the name of the [enclave](https://docs.kurtosis.com/advanced-concepts/enclaves/) (isolated environment) to use for the deployment process.
     - `--args-file params.yml` specifies the configuration file to use for the deployment process.
     - `--image-download always` specifies to always download the latest Docker images for the deployment process.
