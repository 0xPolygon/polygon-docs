
Matic.js library also provides the **ZkEvmClient** to interact with the Polygon zkEVM network.

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
