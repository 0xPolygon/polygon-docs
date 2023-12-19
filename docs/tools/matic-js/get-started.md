Matic.js is a javascript library which helps in interacting with the various components of Matic Network.

In this get started document we will learn about how we can setup and interact with the POS bridge.

In case you face any issues or have any queries, feel free to raise a [ticket](https://support.polygon.technology/support/tickets/new) to our Support Team or reach out to us on [Discord](https://discord.gg/32j4qNDn).

!!! important
    Make sure you have followed the [installation step](installation.md).

## Initializing

To code with matic, import the relevant libraries in your scripts. For example:

```javascript
import { use } from '@maticnetwork/maticjs'
import { Web3ClientPlugin } from '@maticnetwork/maticjs-web3'

// install web3 plugin
use(Web3ClientPlugin)
```

- Click for more details on POS applications that use [`web3js`](setup/web3js.md).
- Click for more details on POS applications that use [`ethers`](setup/ethers.md).