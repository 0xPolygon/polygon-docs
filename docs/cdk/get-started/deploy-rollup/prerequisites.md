                            |
## Preliminary setup

Implementing the Polygon CDK zkRollup EVM-compatible network requires either a Linux machine or a virtual machine running Linux as a Guest OS.

Since the CDK zkRollup implementation involves running Docker containers, ensure that a Docker daemon is installed on your machine.

Here's how to get setup;

For Linux machines, install the Docker engine directly on the machine.

For other operating systems (MacOS, Windows), this is achieved in 4 steps, executed in the given sequential order;

- Install a hypervisor, e.g., VirtualBox, VMware Fusion (MacOS), VMware Workstation (Windows), VMware ESXi (Bare Metal Hypervisor).
- Setup a virtual machine, e.g., if you are using VirtualBox, which is open-source, Vagrant is the quickest way to automatically setup a virtual machine and also set up ssh private/public keys.
- Install Linux as Guest OS, preferably the latest version of Ubuntu Linux.
- Install [Docker](https://docs.docker.com/desktop/install/linux-install/).

Search the internet for quick guides on creating virtual machines. Here's an example of a video on [how to create a Linux VM on a Mac](https://www.youtube.com/watch?v=KAd7FafXfJQ).

In order to run multiple Docker containers, an extra tool called `docker compose` needs to be [downloaded and installed](https://docs.docker.com/compose/install/linux/). As you will see, a YAML file is used for configuring all CDK zkRollup services.

!!!info
    One more thing, since the prover is resource-heavy, you will need to run its container externally. Access to cloud computing services such as AWS EC2 or DigitalOcean will be required.

### Prerequisites

Next, ensure that you have checked your system specs, and have at hand all the variables listed below.

#### Environment variables

You'll need the following items to begin:

- `INFURA_PROJECT_ID` // Same as API Key in your Infura account
- `ETHERSCAN_API_KEY`
- Public IP address
- L1 Goërli node RPC
- Goërli address with **0.5 GöETH**

See this guide here for [**setting up your own Goërli node**](setup-goerli-node.md).

#### Computing requirements

Keep in mind that the mainnet files you will be downloading are 70GB in size.

If the prover is the only container you will be running externally in a cloud, then it is preferable to have a minimum 300GB of storage in the primary machine.

Depending on the user's resources, the zkEVM network can be implemented with either the actual full prover or the mock prover.

The full prover is resource-intensive as it utilizes the exact same proving stack employed in the real and live CDK zkRollup network.

!!!info
    The full prover's system requirements are:

    - 96-core CPU
    - Minimum 768GB RAM

The mock prover is a dummy prover which simply adds a "Valid ✅" checkmark to every batch.

!!!info
    The mock prover, on the other hand, only requires:

    - 4-core CPU
    - 8GB RAM (16GB recommended)

As an example, the equivalent [AWS EC2s](https://aws.amazon.com/ec2/instance-types/r6a/) for each of these two provers are as follows:

- `r6a.xlarge` for mock prover.
- `r6a.24xlarge` for full prover.

The initial free disk space requirement is minimal (<2TB), but you should monitor available space as the network is always adding more data.

Once all the layers are setup and all prerequisites are in place, you can proceed to the next step of this guide.
