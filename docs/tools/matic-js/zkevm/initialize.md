---
id: initialize-zkevm
title: Initialize ZkEvmClient
sidebar_label: Initialize
description: ZkEvmClient allows you to interact with the Polygon zkEVM network.
keywords:
  - docs
  - maticjs
  - polygon
  - zkEvm client
image: https://wiki.polygon.technology/img/polygon-logo.png
---

MaticJS library also provides **ZkEvmClient** to interact with the Polygon zkEVM network.

```js
import { ZkEvmClient, use } from "@maticnetwork/maticjs"

const zkEvmClient = new ZkEvmClient();

await zkEvmClient.init({
  network: <network name>,  // 'testnet'
  version: <network version>, // 'blueberry'
  parent: {
    provider: <parent provider>,
    defaultConfig: {
      from: <from address>
    }
  },
  child: {
    provider: <child provider>,
    defaultConfig: {
      from: <from address>
    }
  }
});
```

Once the `ZkEvmClient` is initialized, you can interact with all available APIs from MaticJS SDK.
