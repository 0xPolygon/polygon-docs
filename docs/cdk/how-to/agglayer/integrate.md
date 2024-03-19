Polygon AggLayer is a ZK-powered interoperability solution that enables a shared state across multiple chains. It receives zero-knowledge proofs from CDK chains and checks their soundness before sending them on to the L1 for verification. 

This document shows you how to integrate and configure the AggLayer into your stack.

!!! important
    - Polygon manages the AggLayer in production at the current time.
    - In the future, the AggLayer will be decentralized.

!!! warning
    - The AggLayer is in development and subject to architectural changes.
    - The code is still being audited.

## Prerequisites

You should have already deployed a CDK chain stack which has integrated the bridge service.

Please check our [get started](../../get-started/quickstart-validium.md) section for guidance, quickstarts, and deployment tutorials for more information.

!!! important
    - If you want to register your chain on the uLXLY bridge, follow the [instructions here](../register-configure-ulxly.md).
    - However, you may only be interested in integrating the AggLayer with your chain, in which case you do not have to register for the uLXLY bridge.

## Configure your chain to use the AggLayer

To access the Polygon AggLayer, you need to update your node configuration.

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
- `SenderAddress` is the address specified by the aggregator when it creates a proof. Supplied by Polygon.

You now have a fully integrated AggLayer in your Polygon CDK stack.

</br>
