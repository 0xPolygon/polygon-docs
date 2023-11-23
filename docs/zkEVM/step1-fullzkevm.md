Welcome to your step-by-step guide to implementing a full Polygon zkEVM network on the Goërli testnet as the L1 network.

Users with good internet connection can schedule a 2-hour window for completing the entire process in one go.

However, in order to allow for in-between breaks, the process is aesthetically split into 6 steps.

- [**First Step**](/docs/zkevm/deploy-fullzkevm.md#overview-and-setting-up): Preliminary Setup, checking system requirements and prerequisites variables.

- [**Second Step**](/docs/zkevm/step2-fullzkevm.md#step2-fullzkevm): Installing Dependencies and downloading Mainnet Files.

- [**Third Step**](/docs/zkevm/step3-fullzkevm.md#step3-fullzkevm): Creating wallets and Deploying Contracts.

- [**Fourth Step**](/docs/zkevm/step4-fullzkevm.md#step4-fullzkevm): Deployment of the zkNode.

- [**Fifth Step**](/docs/zkevm/step5-fullzkevm.md#step5-fullzkevm): Configuring the Prover and Services.

- [**Sixth Step**](/docs/zkevm/step6-fullzkevm.md#step6-fullzkevm): Activating forced txs and Bridging/Claiming Assets.

:::caution

Instructions in this document are subject to frequent updates as the zkEVM software is still in early development stages.

Please report [<ins>here</ins>](https://support.polygon.technology/support/tickets/new) or reach out to our [<ins>support team on Discord</ins>](https://discord.com/invite/0xPolygon) if you encounter any issues.

:::

## Overview And Setting Up

Implementing the full stack Polygon zkEVM involves more than just running an RPC zkNode or the Prover to validate batches, and deploying Smart Contracts. In its entirety, it encompasses all these processes and more.

The common rollup actors, mainly from the zkNode view, are the **Sequencer**, the **Aggregator**, the **Synchroniser** and the JSON **RPC** node. All these affect the L2 **State**.

Also, the Aggregator uses the **Prover** to avail verifiable proofs of sequenced batches. And the sequenced batches are composed of transactions taken from the **Pool DB**.

This highlights just a few main components. The rest of the zkEVM components and those working in the background, are listed in the next subsection.

### Why You Need Docker

The modular design of the zkEVM allows for most components to be separately instantiated, and we therefore run each of these instances in a separate Docker container.

The below table enlists all the zkEVM components/services and their corresponding container-names.

Our zkEVM Deployment-guide provides CLI commands to automatically create these Docker containers.

$$
\begin{aligned}
\begin{array}{|l|l|l|l}\hline
\bf{Component} & \bf{Container} & \bf{Brief\ Description} \\ \hline
\texttt{Sequencer} & \texttt{zkevm-sequencer} & \texttt{Fetches txs from Pool DB, checks if valid, then puts valid ones into a batch.} \\ \hline

\texttt{Aggregator} & \texttt{zkevm-aggregator}  & \texttt{Validates sequenced batches by generating verifiable Zero Knowledge proofs.} \\ \hline

\texttt{Synchronizer} & \texttt{zkevm-sync}  & \texttt{Updates the state by fetching data from Ethereum through the Etherman.} \texttt{ }\\ \hline

\texttt{JSON RPC} & \texttt{zkevm-rpc} & \texttt{An interface for interacting with the zkEVM. e.g., Metamask, Etherscan or Bridge.} \\ \hline

\texttt{State DB} & \texttt{zkevm-state-db}  & \texttt{A database for permanently storing state data (apart from the Merkle tree). } \\ \hline

\texttt{Prover} & \texttt{zkevm-prover-server}  & \texttt{Used by the Aggregator to create ZK proofs. Runs on an external cloud server.} \\ \hline

\texttt{Pool DB} & \texttt{zkevm-pool-db} & \texttt{Stores txs from the RPC nodes, waiting to be put in a batch by the Sequencer.} \\ \hline

\texttt{Executor} & \texttt{zkevm-executor}  & \texttt{Executes all processes. Collects results’ metadata (state root, receipts, logs)} \\ \hline

\texttt{Etherman} & \texttt{zkevm-eth-tx-manager}  & \texttt{Implements methods for all interactions with the L1 network and smart contracts.} \\ \hline

\texttt{Bridge UI} & \texttt{zkevm-bridge-ui}  & \texttt{User-Interface for bridging ERC-20 tokens between L2 and L1 or another L2.} \\ \hline

\texttt{Bridge DB} & \texttt{zkevm-bridge-db}  & \texttt{A database for storing Bridge-related transactions data.} \\ \hline

\texttt{Bridge Service} & \texttt{zkevm-bridge-service}  & \texttt{A backend service enabling clients like the web UI to interact with Bridge smart contracts.} \\ \hline

\texttt{zkEVM Explorer} & \texttt{zkevm-explorer-l2}  & \texttt{L2 network's Block explorer. i.e., The zkEVM Etherscan [Explorer](https://zkevm.polygonscan.com).} \\ \hline

\texttt{zkEVM Explorer DB} & \texttt{zkevm-explorer-l2-db}  & \texttt{Database for the L2 network's Block explorer. i.e., Where all the zkEVM Etherscan Explorer queries are made.} \\ \hline

\texttt{Gas Pricer} & \texttt{zkevm-l2gaspricer }  & \texttt{Responsible for suggesting the gas price for the L2 network fees.} \\ \hline

\texttt{Goërli Execution} & \texttt{goerli-execution}  & \texttt{L1 node's execution layer.} \\ \hline

\texttt{Goërli Consensus} & \texttt{goerli-consensus}  & \texttt{L1 node's consensus layer.} \\ \hline
\end{array}
\end{aligned}
$$

:::info

The **First Step** of this Deployment-Guide begins here!

:::

### Preliminary Setup

Implementing the Polygon zkEVM requires either a Linux machine or a virtual machine running Linux as a Guest OS.

Since the zkEVM implementation involves running Docker containers, ensure that a Docker daemon is installed on your machine.

Here's how to get setup;

For _Linux machines_, Install **Docker engine** directly on the machine.

For other _Operating Systems_ (MacOS, Windows), this is achieved in 4 steps, executed in the given sequential order;

- Install a **Hypervisor**. (e.g., VirtualBox, VMware Fusion (MacOS), VMware Workstation (Windows), VMware ESXi (Bare Metal Hypervisor)).
- Setup a **Virtual Machine**. (e.g., If you are using VirtualBox, which is open-source, Vagrant is the quickest way to automatically setup a virtual machine and also set up ssh private/public keys.)
- Install **Linux** as Guest OS, preferably the latest version of Ubuntu Linux.
- Install [**Docker**](https://docs.docker.com/desktop/install/linux-install/).

Search the internet for quick guides on creating virtual machines. Here's an example of a video on [How to Create a Linux Virtual Machine on a Mac](https://www.youtube.com/watch?v=KAd7FafXfJQ).

In order to run multiple Docker containers, an extra tool called **Docker Compose** needs to be [downloaded and installed](https://docs.docker.com/compose/install/linux/). As you will see, a YAML file is used for configuring all zkEVM services.

:::info

One more thing, since the Prover is resource-heavy, you will need to run its container externally. Access to cloud computing services such as AWS EC2 or DigitalOcean will be required.

:::


### Prerequisites

Next, ensure that you have checked your system specs, and have at hand all the variables listed below.

#### Environment Variables

You'll need the following items to begin:

- INFURA_PROJECT_ID // Same as API Key in your Infura account
- ETHERSCAN_API_KEY
- Public IP address
- L1 Goërli node RPC
- Goërli address with **0.5 GöETH**

See this guide here for [**setting up your own Goërli node**](/docs/zkevm/setup-goerlinode.md#setup-goerlinode).

#### Computing Requirements

Keep in mind that the mainnet files you will be downloading are 70GB big.

If the Prover is the only container you will be running externally in a cloud, then it is preferable to have a minimum 300GB of storage in the primary machine.

Depending on the user's resources, the zkEVM network can be implemented with either the actual _Full Prover_ or the _Mock Prover_.

The Full Prover is resource-intensive as it utilises the exact same proving stack employed in the real and live zkEVM network.

:::info

The **Full Prover**'s system requirements are:

- 96-core CPU
- Minimum 768GB RAM

:::

The Mock Prover is a dummy prover which simply adds a "Valid ✅" checkmark to every batch.

:::info

The **Mock Prover**, on the other hand only requires:

- 4-core CPU
- 8GB RAM (16GB recommended)

:::

As an example, the equivalent [AWS EC2s](https://aws.amazon.com/ec2/instance-types/r6a/) for each of these two provers are as follows:

- r6a.xlarge for **Mock Prover**
- r6a.24xlarge for **Full Prover**

The initial free disk space requirement is minimal (<2TB), but you should monitor available space as the network is always adding more data.

Once all the layers are setup and all prerequisites are in place, you can proceed to the next step of this guide.
