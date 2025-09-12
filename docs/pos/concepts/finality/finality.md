!!! info "5 Second Finality in Polygon"

    NOTE: With the upgrade to Heimdall v2, deterministic finality on PoS is now achieved in between 2-5 seconds thanks to the 1-2 seconds block time in Heimdall, meaning miletones are voted on and finalized much faster.

## How to Get Finalized Block

Simply use the standard `eth_getBlockByNumber` JSON-RPC method with the `"finalized"` block parameter to retrieve information about the most recently finalized block in Polygon PoS. Finalized blocks are considered highly secure and irreversible, making them crucial for applications requiring strong transaction certainty. 

To get the finalized block, you can use the following JSON-RPC call: 


```
{
  "method": "eth_getBlockByNumber",
  "params": ["finalized", true],
  "id": 1,
  "jsonrpc": "2.0"
}
```
## Using the Milestone API

Here's a simple code example to check if a transaction has reached finality
using the milestone mechanism.

```ts
async function milestones_checkFinality(client: any, txHash: string): Promise<boolean> {
  const tx = await client.getTransaction({ hash: `0x${txHash}` })
  if (!tx || !tx.blockNumber) return false
  const latestBlock: Block = await client.getBlock({ blockTag: 'finalized' })

  console.log(`Latest finalized block: ${latestBlock.number}`)
  console.log(`Your transaction block: ${tx.blockNumber}`)

  // Checking whether the finalized block number via milestones has reached the transaction block number.
  if (latestBlock.number !== null && latestBlock.number > tx.blockNumber) {
    console.log("Your transaction block has been confirmed after 16 blocks");
    return true
  } else {
    return false
  }
}
```

### Running the Code Locally

- Step 1: Copy the code into a file named `milestones.ts`.

- Step 2: Install the required dependencies by running:

  ```bash
  npm install
  ```

- Step 3: Run the code using Node.js with the required command-line arguments:

  ```bash
  npx ts-node milestones.ts --txHash <transaction_hash> --function <function_name> --network <network_name>
  ```

  Replace <transaction_hash> with the actual transaction hash, <function_name>
  with either pre_milestones or milestones, and <network_name> with either
  polygon or amoy.

- Step 4: Observe the output to determine if your transaction has been finalized
  based on the selected milestone mechanism and network.

### Results

The results should show whether the transaction has been finalized based on the
selected milestone mechanism and network. Usually Milestones will take 3-5
seconds to finalize the transaction.



## The Evolution of Finality

There are two main types of finality in blockchains: probabilistic and
deterministic. Probabilistic finality means that there is a chance of a
reorganization (reorg) where a different chain might become the canonical chain.
Deterministic finality means that there is no chance of a reorganization. A
popular chain with probabilistic finality is Bitcoin. A popular chain with
deterministic finality is Ethereum.

### With Milestones in Polygon

With the introduction of milestones:

- Finality is **deterministic** even before a checkpoint is submitted to L1.
  After a certain number of blocks in consensus layer, a milestone is proposed and
  validated by Heimdall. Once 2/3+ of the network agrees, the milestone is
  finalized, and all transactions up to that milestone are considered final,
  with no chance of reorganization.

- Separation of Checkpoints and Milestones: Checkpoints still occur every 256
  blocks (minimum) and are submitted to Ethereum. However, milestones provide
  much faster finality on Polygon chain, using Heimdall layer for
  finalization, improving the user experience significantly.

_Finality achieved after a number of blocks confirmation,
as well as a consensus period among the validators (approx. 3-5 seconds)_

