!!!info
    This document series describes in detail the various forms and stages that L2 users' transactions go through, from the time they are created in users' wallets to the time they are finally verified with indisputable evidence on L1.

## Submit transaction

Transactions in the Polygon zkEVM network are created in users' wallets and signed with their private keys.

Once generated and signed, the transactions are sent to the trusted sequencer's node via their JSON-RPC interface. The transactions are then stored in the pending transactions pool, where they await the sequencer's selection for execution or discard.

Users and the zkEVM communicate using JSON-RPC, which is fully compatible with Ethereum RPC. This approach allows any EVM-compatible application, such as wallet software, to function and feel like actual Ethereum network users.

### Transactions and blocks on zkEVM

In the current design, a single transaction is equivalent to one block.

This design strategy not only improves RPC and P2P communication between nodes, but also enhances compatibility with existing tooling and facilitates fast finality in L2. It also simplifies the process of locating user transactions.
