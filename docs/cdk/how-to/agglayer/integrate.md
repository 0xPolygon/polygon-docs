Polygon AggLayer is a ZK-powered interoperability solution that enables a shared state across multiple chains. It receives zero-knowledge proofs from CDK chains and checks their soundness before sending them on to the L1 for verification. 

This document shows you how to integrate and configure the AggLayer into your stack.

!!! important
    - Polygon manages the AggLayer in production at the current time.
    - In the future, the AggLayer will be decentralized.

!!! warning
    - The AggLayer is in development and subject to architectural changes.
    - The code is still being audited.

## Step 1: Attach a chain to the uLXLY bridge

1. If you do not have a CDK chain set up with Polygon, [make a request to register your chain](https://discord.gg/XvpHAxZ). 

    We will ask you for the following data:

    ```json
    "rollupTypeID": 0,
    "chainID": 0000,
    "admin": "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "sequencer": "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "gasTokenAddress": "0x0000000000000000000000000000000000000000",
    "sequencerURL": "https://rpc.chain.name",
    "networkName": "chain name"
    ```

    !!! note
        - If you are using a wrapped-token on the bridge, we use the original token address. 
        - You can use any token on any network that is attached to the LxLy bridge, including those from the Ethereum mainnet.

2. Once registered, we provide you with the following network parameters:

    - `rollupID`
    - `rollupAddress`

3. We also give you a pre-configured `genesis.json` file to use.

4. You will need the Polygon bridge configuration details.

    ```sh
    [NetworkConfig]
    GenBlockNumber = "16896721"
    PolygonBridgeAddress = "0x2a3DD3EB832aF982ec71669E178424b10Dca2EDe"
    PolygonZkEVMGlobalExitRootAddress = "0x580bda1e7A0CFAe92Fa7F6c20A3794F169CE3CFb"
    PolygonRollupManagerAddress = "0x5132a183e9f3cb7c848b0aac5ae0c4f0491b7ab2"
    ...
    ```

5. Configure your nodes with the data.

    !!! info "Configure your nodes"
        - Add the `rollupID` and `rollupAddress` parameters to the `L1config` section of the `genesis.json` file of the CDK node. For example:

        ```sh
        {
            "rollupTypeID": 1,
            "chainID": 3776,
            "admin": "0xxxxx",
            "sequencer": "0xxxxx",
            "gasTokenAddress": "0x0000000000000000000000000000000000000000",
            "sequencerURL": "https://rpc.xxx",
            "networkName": "xxx zkEVM",
        }
        ```

6. Polygon registers the CDK chain on the uLxLy bridge.

7. Chain owners then need to add POL and ETH tokens to the sequencer on the CDK chain.

## Configuring the Polygon managed AggLayer

Once registered, Polygon creates a permissionless node that points to the corresponding L2 full node.

We then add your details to our AggLayer configuration file [`../agglayer/docker/data/agglayer.toml`](https://github.com/0xPolygon/agglayer/blob/main/docker/data/agglayer/agglayer.toml); specifically these configurations:

* `[FullNodeRPCs]` points to the corresponding L2 full node.
* `[L1]` points to the corresponding L1 chain.
* The `[DB]` section has the managed database details.

For example:

```sh
[FullNodeRPCs]
# 0x0DCd1Bf9A1b36cE34237eEaFef220932846BCD82 = "http://zkevm-node:8123"
# {{ zkevm_l1_rollup_manager_addr }} = "http://int-rpc.{{ base_dn }}:{{ zkevm_rpc_server_port }}"
1 = "http://int-rpc.{{ base_dn }}:{{ zkevm_rpc_server_port }}"

[RPC]
Host = "0.0.0.0"
Port = {{ zkevm_agglayer_server_port }}
ReadTimeout = "60s"
WriteTimeout = "60s"
MaxRequestsPerIPAndSecond = 5000

[Log]
Environment = "development" # "production" or "development"
Level = "debug"
Outputs = ["stderr"]

[DB]
User = "{{ zkevm_agglayer_db_user }}"
Password = "{{ zkevm_agglayer_db_password }}"
Name = "{{ zkevm_agglayer_db_name }}"
Host = "{{ zkevm_postgres_host }}"
Port = "5432"
EnableLog = false
MaxConns = 200

[EthTxManager]
FrequencyToMonitorTxs = "1s"
WaitTxToBeMined = "2m"
ForcedGas = 0
GasPriceMarginFactor = 1
MaxGasPriceLimit = 0
PrivateKeys = [
	{Path = "/etc/agglayer/agglayer.keystore", Password = "{{ zkevm_agglayer_keystore_password }}"},
]

[L1]
ChainID = {{ zkevm_l1_chain_id }}
NodeURL = "{{ zkevm_l1_rpc }}"
RollupManagerContract = "{{ zkevm_l1_rollup_manager_addr }}"

[Telemetry]
PrometheusAddr = "0.0.0.0:2223"
```

## Configuring the client-managed AggLayer

The last step is to update your node configuration to map to the Polygon Agglayer.

Open the `config.toml` file and include the following:

```sh
[Aggregator]
SettlementBackend = "agglayer"
AggLayerURL = "https://agglayer-test.polygon.technology"
AggLayerTxTimeout = "300s"
SenderAddress = "0x0325686a18aA829B9FaaAD70f22ea0830aA6076F"
```

You now have a fully integrated AggLayer in your Polygon CDK stack.

</br>