The `withdrawExitFaster` method can be used to exit the withdraw process faster by using the txHash from `withdrawStart` method.

It is generally fast because it generates proof in the backend. You need to configure [setProofAPI](../../set-proof-api.md).

**Note**- withdrawStart transaction must be checkpointed in order to exit the withdraw.

```js
import { setProofApi } from '@maticnetwork/maticjs'

setProofApi("https://proof-generator.polygon.technology/");

const erc20RootToken = posClient.erc20(<root token address>, true);

// start withdraw process for 100 amount
const result = await erc20Token.withdrawExitFaster(<burn tx hash>);

const txHash = await result.getTransactionHash();

const txReceipt = await result.getReceipt();

```

Once the transaction is complete & checkpoint is completed, amount will be deposited to root chain.
