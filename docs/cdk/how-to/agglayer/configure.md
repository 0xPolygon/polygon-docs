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

</br>