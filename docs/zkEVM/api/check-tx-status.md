Here's how to verify the status of a transaction when using an RPC node as an intermediary step to the Polygon zkEVM network.

This guide is for users who send transactions to an RPC node, which in turn relays these transactions to the Polygon zkEVM network.

## Recommended endpoints

After sending a transaction (TX) to the network using the `eth_sendRawTransaction`, use the following endpoints to check the TX status:

1. `eth_getTransactionByHash`
2. `eth_getTransactionReceipt`

### Using `eth_getTransactionByHash`

When checking the TX status using the `eth_getTransactionByHash`, the result can be either one of the following.

(a) If the result is null, it means either the TX doesn't exist in the network or it was discarded.

(b) If the result contains some data, then

- If the fields `block_num` and `block_hash` are null, it means the TX is still in the pool and is pending.

- If the fields `block_num` and `block_hash` are NOT null, it means the TX was mined.

### Using `eth_getTransactionReceipt`

When checking the TX status using the `eth_getTransactionReceipt`, again the result can either one of the following.

(a) If the result is null, it means either the TX doesn't exist or it is still pending to be mined. In this case, use the `eth_getTransactionByHash` endpoint to check it.

(b) If the result contains some data, it means the TX was already mined. However,

- If the field status is 1 (success), it means the TX affected the state as expected.

- If the field status is 0 (failure), it means the TX has consumed gas used while processing the TX, but hasn't changed the state as expected.
