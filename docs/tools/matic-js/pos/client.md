Matic.js provides `POSClient` to interact with the **PoS Bridge**.

```js
import { POSClient,use } from "@maticnetwork/maticjs"

const posClient = new POSClient();

await posClient.init({
    network: <network name>,  // 'testnet' or 'mainnet'
    version: <network version>, // 'mumbai' or 'v1'
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

Once the `POSClient` is initiated, you can interact with all available APIs.
