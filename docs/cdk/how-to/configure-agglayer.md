Polygon AggLayer is a ZK-powered interoperability solution that enables a shared state across multiple chains. It receives zero-knowledge proofs from multiple CDK chains and checks their soundness before sending them on to the L1 for verification. 

!!! important
    - Polygon manages the AggLayer in production at the current time.

!!! warning
    - The AggLayer is in development and subject to architectural changes.
    - The code is still being audited.

## Configure the AggLayer

The AggLayer integrates with external CDK chains using an RPC node configuration for each chain.

Add the respective chain configurations to the [`../agglayer/docker/data/agglayer.toml`](https://github.com/0xPolygon/agglayer/blob/main/docker/data/agglayer/agglayer.toml) file by amending the following details to add the required chain(s).

* Configure `[FullNodeRPCs]` to point to the corresponding L2 full node.
* Configure `[L1]` to point to the corresponding L1 chain.
* Configure the `[DB]` section with the managed database details.

## Run a local AggLayer

The following instructions are for users who may like to test and run a local installation of the AggLayer for research purposes.

### Prerequisites

Make sure you have the following software installations.

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Golang](https://go.dev/doc/install)

### Clone the repo.

```sh
git clone https://github.com/0xPolygon/agglayer.git
cd agglayer/
```

### Set up and installation

Run the following command to bring up a zkEVM node, a prover, and a mock L1 network.

```sh
make run-docker
```

</br>