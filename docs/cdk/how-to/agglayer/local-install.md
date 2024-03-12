The following instructions are for users who may like to test and run a local installation of the AggLayer for research purposes.

## Prerequisites

Make sure you have the following software installations.

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Golang](https://go.dev/doc/install)

## Clone the repo.

```sh
git clone https://github.com/0xPolygon/agglayer.git
cd agglayer/
```

## Set up and installation

Run the following command to bring up a zkEVM node, a prover, and a mock L1 network.

```sh
make run-docker
```