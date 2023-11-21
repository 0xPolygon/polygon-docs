---
id: bloxroute
title: BloXroute Instructions
sidebar: BloXroute Instructions
description: Connect your Polygon network nodes to BloXroute gateways using BDN.
keywords:
  - docs
  - matic
  - polygon
  - bloXroute
  - BDN
image: https://wiki.polygon.technology/img/polygon-logo.png
---

As validators, we need to keep track of block propagation time, given that we offer a 2 sec block time. We are working with [bloXroute](https://bloxroute.com/) to leverage their infrastructure ([Blockchain Distribution Network or BDN](https://docs.bloxroute.com/bdn-architecture)), which would help lower the block propagation time. For this, we need your support in connecting your Polygon network nodes to bloXroute’s gateways.

:::info
To get your bloXroute endpoints, please ping the **Validator Support team** on Discord.
:::

You will be able to add this gateway as a static (trusted) peer/node on your sentry node. If you are having any apprehensions about divulging the enode and region of your sentry node, you can rest assured that this information will be only shared with the bloXroute team and will be safe with them.

## Connecting to the BDN

**Step 1**: Create an account at the **bloXroute user portal** and subscribe to the Introductory Plan (free of charge).

**Step 2**: Contact the Validator Support Team for the bloXroute endpoint.

**Step 3**: Once bloXroute team creates a trusted peer specifically for your node, you will receive the hosted gateway information (enode public key). To add this enode as a trusted peer in your sentry node, follow these steps:

Add the following content using `vim ~ /var/lib/bor/config.toml`:

```
[Node.P2P]
TrustedNodes = ["enode://<node_id_of_gateway_provided_by_bloxroute>"]

[Node.P2P]
StaticNodes = ["enode://static_node_enode1@ip:port", "enode://static_node_enode2@ip:port", ... ]
TrustedNodes = ["enode://<enode_id_of_gateway_provided_by_bloxroute>"]
```

Now restart Bor:

```bash
sudo service bor restart
```

**Step 4**: Inform the Polygon team on the Discord channel **#mainnet-validator-queries** once you are done adding the trusted peer. bloXroute will activate the hosted gateway and confirm the success of the connection within the next 24 hours.
