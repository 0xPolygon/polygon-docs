## Prerequisites

1. The installation requires [Go 1.19](https://go.dev/doc/manage-install).

2. Install the relevant libraries for your architecture by running:

    ```sh
    make build-libs
    ```

!!! tip "Hardware specifics"
    - On x86, the following packages are used by the optimal, vectorized, Poseidon hashing for the sparse Merkle tree:

        - Linux: `libgtest-dev libomp-dev libgmp-dev`
        - MacOS: `libomp brew install gmp`

    - For Apple silicon, the `iden3` library is used instead.

## Set up sequencer (WIP)

Run the following to enable the sequencer:

```sh
CDK_ERIGON_SEQUENCER=1 ./build/bin/cdk-erigon <flags>
```

### Special mode - L1 recovery

The sequencer supports a special recovery mode which allows it to continue the chain using data from the L1. To enable this add the flag zkevm.l1-sync-start-block: [first l1 block with sequencer data]. It is important to find the first block on the L1 from the sequencer contract that contains the sequenceBatches event. When the node starts up it will pull of the L1 data into the cdk-erigon database and use this during execution rather than waiting for transactions from the txpool, effectively rebuilding the chain from the L1 data. This can be used in tandem with unwinding the chain, or using the zkevm.sync-limit flag to limit the chain to a certain block height before starting the L1 recovery (useful if you have an RPC node available to speed up the process).

Important Note: If using the zkevm.sync-limit flag you need to go to the boundary of a batch+1 block so if batch 41 ends at block 99 then set the sync limit flag to 100.

## Enable zkEVM APIs

In order to enable the `zkevm_ namespace`, add `zkevm` to the `http.api` flag (see the example config below??).

### Supported functions

`zkevm_batchNumber`
`zkevm_batchNumberByBlockNumber`
`zkevm_consolidatedBlockNumber`
`zkevm_isBlockConsolidated`
`zkevm_verifiedBatchNumber`
`zkevm_isBlockVirtualized`
`zkevm_virtualBatchNumber`
`zkevm_getFullBlockByHash`
`zkevm_getFullBlockByNumber`

### Supported (remote)

`zkevm_getBatchByNumber`

### Not yet supported

`zkevm_getNativeBlockHashesInRange`

### Deprecated

`zkevm_getBroadcastURI` - removed by zkEVM.

## Limitations/warnings

The golden poseidon hashing will be much faster on x86, so developers on Mac may experience slowness on Apple silicone
Falling behind the network significantly will cause a SMT rebuild - which will take some time for longer chains

### Configuration files

Config files are the easiest way to configure cdk-erigon, there are examples in the repository for each network e.g. hermezconfig-mainnet.yaml.example.

Depending on the RPC provider you are using, you may wish to alter zkevm.rpc-ratelimit.

## Running CDK-Erigon
Build using make cdk-erigon
Set up your config file (copy one of the examples found in the repository root directory, and edit as required)
run ./build/bin/cdk-erigon --config="./hermezconfig-{network}.yaml" (complete the name of your config file as required)
NB: --externalcl flag is removed in upstream erigon so beware of re-using commands/config

### Run modes
cdk-erigon can be run as an RPC node which will use the data stream to fetch new block/batch information and track a remote sequencer (the default behaviour). It can also run as a sequencer. To enable the sequencer, set the CDK_ERIGON_SEQUENCER environment variable to 1 and start the node. cdk-erigon supports migrating a node from being an RPC node to a sequencer and vice versa. To do this, stop the node, set the CDK_ERIGON_SEQUENCER environment variable to the desired value and restart the node. Please ensure that you do include the sequencer specific flags found below when running as a sequencer. You can include these flags when running as an RPC to keep a consistent configuration between the two run modes.

Docker (DockerHub)
The image comes with 3 preinstalled default configs which you may wish to edit according to the config section below, otherwise you can mount your own config to the container as necessary.

A datadir must be mounted to the container to persist the chain data between runs.

Example commands:

Mainnet
docker run -d -p 8545:8545 -v ./cdk-erigon-data/:/home/erigon/.local/share/erigon hermeznetwork/cdk-erigon  --config="./mainnet.yaml" --zkevm.l1-rpc-url=https://rpc.eth.gateway.fm
Cardona
docker run -d -p 8545:8545 -v ./cdk-erigon-data/:/home/erigon/.local/share/erigon hermeznetwork/cdk-erigon  --config="./cardona.yaml" --zkevm.l1-rpc-url=https://rpc.sepolia.org
docker-compose example:

Mainnet:
NETWORK=mainnet L1_RPC_URL=https://rpc.eth.gateway.fm docker-compose -f docker-compose-example.yml up -d
Cardona:
NETWORK=cardona L1_RPC_URL=https://rpc.sepolia.org docker-compose -f docker-compose-example.yml up -d
Config
The examples are comprehensive but there are some key fields which will need setting e.g. datadir, and others you may wish to change to increase performance, e.g. zkevm.l1-rpc-url as the provided RPCs may have restrictive rate limits.

For a full explanation of the config options, see below:

datadir: Path to your node's data directory.
chain: Specifies the L2 network to connect with, e.g., hermez-mainnet. For dynamic configs this should always be in the format dynamic-{network}
http: Enables HTTP RPC server (set to true).
private.api.addr: Address for the private API, typically localhost:9091, change this to run multiple instances on the same machine
zkevm.l2-chain-id: Chain ID for the L2 network, e.g., 1101.
zkevm.l2-sequencer-rpc-url: URL for the L2 sequencer RPC.
zkevm.l2-datastreamer-url: URL for the L2 data streamer.
zkevm.l1-chain-id: Chain ID for the L1 network.
zkevm.l1-rpc-url: L1 Ethereum RPC URL.
zkevm.address-sequencer: The contract address for the sequencer
zkevm.address-zkevm: The address for the zkevm contract
zkevm.address-admin: The address for the admin contract
zkevm.address-rollup: The address for the rollup contract
zkevm.address-ger-manager: The address for the GER manager contract
zkevm.rpc-ratelimit: Rate limit for RPC calls.
zkevm.data-stream-port: Port for the data stream. This needs to be set to enable the datastream server
zkevm.data-stream-host: The host for the data stream i.e. localhost. This must be set to enable the datastream server
zkevm.datastream-version: Version of the data stream protocol.
externalcl: External consensus layer flag.
http.api: List of enabled HTTP API modules.
Sequencer specific config:

zkevm.executor-urls: A csv list of the executor URLs. These will be used in a round robbin fashion by the sequencer
zkevm.executor-strict: Defaulted to true, but can be set to false when running the sequencer without verifications (use with extreme caution)
zkevm.witness-full: Defaulted to true. Controls whether the full or partial witness is used with the executor.
zkevm.sequencer-initial-fork-id: The fork id to start the network with.
Useful config entries:

zkevm.sync-limit: This will ensure the network only syncs to a given block height.

## Networks

| Network Name  | Chain ID | ForkID | Genesis File | RPC URL                                          | Rootchain        | Rollup Address                               |
|---------------|----------|--------|--------------|--------------------------------------------------|------------------|----------------------------------------------|
| zkEVM Mainnet | 1101     | 9      | [Link](https://hackmd.io/bpmxb5QaSFafV0nB4i-KZA) | [Mainnet RPC](https://zkevm-rpc.com/)            | Ethereum Mainnet | `0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2` |
| zkEVM Cardona | 2442     | 9      | [Link](https://hackmd.io/Ug9pB613SvevJgnXRC4YJA) | [Cardona RPC](https://rpc.cardona.zkevm-rpc.com/) | Sepolia          | `0x32d33D5137a7cFFb54c5Bf8371172bcEc5f310ff` |