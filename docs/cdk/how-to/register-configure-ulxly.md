This document describes how to register and configure your CDK chain to use the Polygon uXLXY bridge.

## Prerequisites

You should have already deployed a CDK chain stack which has integrated the bridge service.

Please check our [get started](../get-started/quickstart-validium.md) section for guidance, quickstarts, and deployment tutorials for more information.

## Step 1: Attach a chain to the uLXLY bridge

1. If your CDK chain is not yet registered with Polygon, [make a request to register your chain](https://discord.gg/XvpHAxZ). 

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
