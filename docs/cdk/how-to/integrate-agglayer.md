Polygon AggLayer is a web service that receives zero-knowledge proofs from different CDK chains and checks their soundness before sending the proof to L1 for verification.

!!! warning
    - The AggLayer is in development and subject to architectural changes.
    - The code is still being audited.

## Prerequisites

Make sure you have the following software installations.

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Golang](https://go.dev/doc/install)
- [GCloud cli](https://cloud.google.com/sdk/docs/install) - production only.

### Clone the repo.

```sh
git clone https://github.com/0xPolygon/agglayer.git
cd agglayer/
```

## Set up and installation

### Local

Run the following command to bring up a zkEVM node, a prover, and a mock L1 network.

```sh
make run-docker
```

### Production build - managed by Polygon

!!! warning
    - The AggLayer in production is currently managed by Polygon.
    - Currently only one instance of the AggLayer can run at one time.
    - The AggLayer should, therefore, automatically start in the case of failure using a containerized setup or an OS level service manager/monitoring system.

Install the Golang dependencies.

```sh
go install .
```

#### Key-signing configurations

Install polygon-cli:

```sh
go install github.com/maticnetwork/polygon-cli@latest
```

Create a new signature:

```sh
polygon-cli signer create --kms GCP --gcp-project-id gcp-project --key-id mykey-tmp
```

Set up ADC in GCloud:

```sh
gcloud auth application-default login
```

In the `../agglayer/docker/data/agglayer.toml` file, add the `KMSKeyName` from GCloud.

## Setting up the AggLayer

Each CDK chain requires a corresponding RPC node configuration that is synced with the target CDK. This node checks the state root after executions of L2 batches.

!!! info "Storage recommendations"
    - Use a durable HA PostgresDB for storage; ideally AWS Aurora PostgreSQL or Cloud SQL for PostgreSQL in GCP.

Add the chain configurations to the `../agglayer/docker/data/agglayer.toml` file by amending the following details to add the required chain(s).

* Configure `[FullNodeRPCs]` to point to the corresponding L2 full node.
* Configure `[L1]` to point to the corresponding L1 chain.
* Configure the `[DB]` section with the managed database details.


</br>