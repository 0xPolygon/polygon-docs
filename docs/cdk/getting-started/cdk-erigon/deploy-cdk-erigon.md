## Prerequisites

There are a few prerequisites for successfully deploying the CDK node.

### Hardware requirements

* Operating system: A Linux-based OS (e.g. Ubuntu 22.04 LTS).
* Memory: At least 64GB RAM.
* CPU: A minimum 4-core CPU, or higher (both Apple Silicon and amd64 are supported).

!!! tip
    - On x86, the following packages are required to use the optimal, vectorized-Poseidon-hashing for the sparse Merkle tree:

        - Linux: `libgtest-dev libomp-dev libgmp-dev`
        - MacOS: `brew install libomp` `brew install gmp`

    - For Apple silicon, the `iden3` library is used instead.

### Software

The installation requires [Go 1.19](https://go.dev/doc/manage-install).

### Set up

1. Clone the repo and `cd` to the root:

    ```sh
    git clone https://github.com/0xPolygonHermez/cdk-erigon
    cd cdk-erigon/
    ```

2. Install the relevant libraries for your architecture by running:

    ```sh
    make build-libs
    ```

## L1 interaction

In order to retrieve data from L1, the L1 syncer needs to know how to request the highest block. 

This can be configured by the flag: `zkevm.l1-highest-block-type`.

The flag defaults to retrieving the `finalized` block. However, there are cases where you may wish to pass `safe` or `latest`.

## Set up sequencer 

!!! warning "Work in progress"
    - Sequencer is production ready from `v2.x.x` onwards.
    - Please check the [roadmap](releases.md#roadmap) for more information.

Enable the sequencer by setting the following environment variable:

```sh
CDK_ERIGON_SEQUENCER=1 ./build/bin/cdk-erigon <flags>
```

### Special mode - L1 recovery

The sequencer supports a special recovery mode which allows it to continue the chain using data from the L1. 

To enable this, add the following flag:

```sh
`zkevm.l1-sync-start-block: [first l1 block with sequencer data]`. 
```

!!! important
    Find the first block on the L1 from the sequencer contract that contains the `sequenceBatches` event. 

When the node starts up, it pulls the L1 data into the `cdk-erigon` database and uses it during execution, effectively rebuilding the chain from the L1 data rather than waiting for transactions from the transaction pool. 

You can use this in tandem with unwinding the chain or by using the `zkevm.sync-limit` flag to limit the chain to a specific block height before starting the L1 recovery. This is useful if you have an RPC node available to speed up the process.

!!! warning
    If using the `zkevm.sync-limit` flag, you need to go to the boundary of a `batch+1` block; so if batch `41` ends at block `99` then set the flag to `100`.

## Enable zkEVM APIs

In order to enable the `zkevm_ namespace`, add `zkevm` to the [`http.api`](#configurations) flag.

### Supported functions

- `zkevm_batchNumber`
- `zkevm_batchNumberByBlockNumber`
- `zkevm_consolidatedBlockNumber`
- `zkevm_isBlockConsolidated`
- `zkevm_verifiedBatchNumber`
- `zkevm_isBlockVirtualized`
- `zkevm_virtualBatchNumber`
- `zkevm_getFullBlockByHash`
- `zkevm_getFullBlockByNumber`
- `zkevm_virtualCounters`
- `zkevm_traceTransactionCounters`

### Supported functions (remote)

- `zkevm_getBatchByNumber`

### Not yet supported

- `zkevm_getNativeBlockHashesInRange`

### Deprecated

- `zkevm_getBroadcastURI` - removed by zkEVM.

## Warnings

- The instantiation of Poseidon over the Goldilocks field is much faster on x86, but developers using MacOS M1/M2 chips may experience slower processing.

- Developers should avoid falling significantly behind the network, especially for longer chains, as this triggers an SMT rebuild, which takes a considerable amount of time to complete.

## Configuration files

- Config files are the easiest way to configure `cdk-erigon`.

- There are examples files in the repository for each network; e.g. [`hermezconfig-mainnet.yaml.example`](https://github.com/0xPolygonHermez/cdk-erigon/blob/1d56fb0a5a64160fd8c05e11ffc8b668bd70b9e8/hermezconfig-mainnet.yaml.example#L4).

- Depending on your RPC provider, you may wish to alter `zkevm.rpc-ratelimit` in the yaml file.

## Running CDK Erigon

1. Build the node with the following command:

    ```sh
    make cdk-erigon
    ```

2. Set up your config file by copying one of the examples found in the repository root directory, and edit as required and add your network name to the following command.

    ```sh
    run ./build/bin/cdk-erigon --config="./hermezconfig-{network}.yaml"
    ```

!!! warn
    Be aware that the `--externalcl` flag is removed upstream in `cdk-erigon` so take care when reusing commands/configurations.

### Run modes

`cdk-erigon` can run as an RPC node which uses the data stream to fetch new block/batch information and track a remote sequencer. This is the default behavior. 

It can also run as a sequencer. To enable the sequencer, set the `CDK_ERIGON_SEQUENCER` environment variable to `1` and start the node. 

!!! warning "Work in progress"
    - Sequencer is production ready from `v2.x.x` onwards.
    - Please check the [roadmap](releases.md#roadmap) for more information.

`cdk-erigon` supports migrating a node from being an RPC node to a sequencer and vice versa. To do this, stop the node, set the `CDK_ERIGON_SEQUENCER` environment variable to the desired value and restart the node. Please ensure that you do include the sequencer specific flags found below when running as a sequencer. You can include these flags when running as an RPC to keep a consistent configuration between the two run modes.

### Docker (DockerHub)

The image comes with three preinstalled default configurations which you can edit according to the configuration section below; otherwise you can mount your own config to the container as necessary.

A datadir must be mounted to the container to persist the chain data between runs.

#### Example `docker` commands

##### Mainnet

```sh
docker run -d -p 8545:8545 -v ./cdk-erigon-data/:/home/erigon/.local/share/erigon hermeznetwork/cdk-erigon  --config="./mainnet.yaml" --zkevm.l1-rpc-url=https://rpc.eth.gateway.fm
```

##### Cardona

```sh
docker run -d -p 8545:8545 -v ./cdk-erigon-data/:/home/erigon/.local/share/erigon hermeznetwork/cdk-erigon  --config="./cardona.yaml" --zkevm.l1-rpc-url=https://rpc.sepolia.org
```

#### Example `docker-compose` commands

##### Mainnet

```sh
NETWORK=mainnet L1_RPC_URL=https://rpc.eth.gateway.fm docker-compose -f docker-compose-example.yml up -d
```

##### Cardona:

```sh
NETWORK=cardona L1_RPC_URL=https://rpc.sepolia.org docker-compose -f docker-compose-example.yml up -d
```

## Configurations

The following examples are comprehensive. There are key fields which must be set, such as `datadir`, and some you may wish to change to increase performance, such as `zkevm.l1-rpc-url` as the provided RPCs may have restrictive rate limits.

- `datadir`: Path to your node's data directory.
- `chain`: Specifies the L2 network to connect with; e.g. `hermez-mainnet`. For dynamic configs this should always be in the format `dynamic-{network}`.
- `http`: Enables HTTP RPC server (set to `true`).
- `private.api.addr`: Address for the private API, typically `localhost:9091`. Change this to run multiple instances on the same machine.
- `zkevm.l2-chain-id`: Chain ID for the L2 network; e.g. 1101.
- `zkevm.l2-sequencer-rpc-url`: URL for the L2 sequencer RPC.
- `zkevm.l2-datastreamer-url`: URL for the L2 data streamer.
- `zkevm.l1-chain-id`: Chain ID for the L1 network.
- `zkevm.l1-rpc-url`: L1 Ethereum RPC URL.
- `zkevm.address-sequencer`: The contract address for the sequencer.
- `zkevm.address-zkevm`: The address for the zkevm contract.
- `zkevm.address-admin`: The address for the admin contract.
- `zkevm.address-rollup`: The address for the rollup contract.
- `zkevm.address-ger-manager`: The address for the GER manager contract.
- `zkevm.rpc-ratelimit`: Rate limit for RPC calls.
- `zkevm.data-stream-port`: Port for the data stream. This needs to be set to enable the datastream server.
- `zkevm.data-stream-host`: The host for the data stream i.e. `localhost`. This must be set to enable the datastream server.
- `zkevm.datastream-version`: Version of the data stream protocol.
- `externalcl`: External consensus layer flag.
- `http.api`: List of enabled HTTP API modules.

### Sequencer specific config

- `zkevm.executor-urls`: A csv list of the executor URLs. These are used in a round robbin fashion by the sequencer.
- `zkevm.executor-strict`: Default is true but can be set to false when running the sequencer without verifications (_use with extreme caution_).
- `zkevm.witness-full`: Default is true. Controls whether the full or partial witness is used with the executor.
- `zkevm.sequencer-initial-fork-id`: The fork id to start the network with.

### Useful config entries

- `zkevm.sync-limit`: This ensures the network only syncs to a given block height.
