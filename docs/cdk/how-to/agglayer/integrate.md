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
    GenBlockNumber = 1
    PolygonBridgeAddress = "0xCca6ECD73932e49633B9307e1aa0fC174525F424"
    PolygonZkEVMGlobalExitRootAddress = "0x8A791620dd6260079BF849Dc5567aDC3F2FdC318"
    PolygonRollupManagerAddress = "0xB7f8BC63BbcaD18155201308C8f3540b07f84F5e"
    PolygonZkEvmAddress = "0x8dAF17A20c9DBA35f005b6324F493785D239719d"
    L2PolygonBridgeAddresses = ["0xCca6ECD73932e49633B9307e1aa0fC174525F424"]
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

## Step 2: Polygon configuration

!!! important
    - These steps are done by Polygon.

Once registered, Polygon creates a permissionless node that points to the corresponding L2 full node.

We then add your details to our AggLayer configuration file [`../agglayer/docker/data/agglayer.toml`](https://github.com/0xPolygon/agglayer/blob/main/docker/data/agglayer/agglayer.toml); specifically these configurations:

* `[FullNodeRPCs]` points to the corresponding L2 full node.
* `[L1]` points to the corresponding L1 chain.
* The `[DB]` section has the managed database details.

## Step 3: External CDK chain configuration

The last step is to update your node configuration to map to the Polygon Agglayer.

Open the `config.toml` file and include the following:

```sh
[Aggregator]
### Agglayer
SettlementBackend = "agglayer"
AggLayerURL = "http://agglayer-001.{{ base_dn }}:{{ zkevm_agglayer_server_port }}"
AggLayerTxTimeout = "30s"
SequencerPrivateKey = {Path = "/etc/zkevm/sequencer.key", Password = "{{ zkevm_keystore_password }}"}
SenderAddress = ""
```

- `SettlementBackend` defines how a final zk-proof is settled. All chains connected to the AggLayer use the `agglayer` value.
- `AggLayerTxTimeout` is the interval a transaction is mined on the AggLayer.
- `AggLayerURL` is the url of the agglayer service. Supplied by Polygon.
- `SequencerPrivateKey` is the private key of the trusted sequencer. Only a CDK trusted sequencer can interact with the AggLayer.
- `SenderAddress` is the address specified by the aggregator when it creates a proof. Supplied by Polygon. Supplied by Polygon.

You now have a fully integrated AggLayer in your Polygon CDK stack.

</br>
