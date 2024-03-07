Polygon Miden is a bi-directional token bridge and state machine. Miden Nodes act as operators that keep the state and compress state transitions recursively into STARK-proofs. The token bridge on Ethereum verifies these proofs. Users can run Miden clients to send RPC requests to the Miden Nodes to update the state.

The major components of Polygon Miden are:

- Miden Clients - represent Miden users
- Miden Nodes - manage the Miden rollup and compress proofs
- Verifier Contract - keeps and verifies state on Ethereum
- Bridge Contract - entry and exit point for users


## Network Slide
![Miden Architecture Overview](../img/network/architecture-overview.svg)

## Miden Clients
Users will run Miden Clients. They are designed to provide an interface for wallets representing accounts on Miden. Miden Clients can execute and prove transactions in the Tx Prover. They can handle arbitrary signature schemes - whereas the default is Falcon. The wallet interface serves a user interface, a wallet database to be able to store account data locally, and the required smart contract code that represents the account on Miden.

## Miden Nodes
Operators will run Miden Nodes. Operators ensure integrity of the Account, Note and Nullifier State - which represent the state of Polygon Miden. Operators can execute and proof transactions against single accounts and they can verify proofs of locally executed transactions. Furthermore, the operator compresses the proofs in several steps up to a single proofs that gets published and verified on the Verifier contract. Operators also watch events emitted by the Bridge Contract to detect deposits and withdrawals.

To manage all of this, Miden Nodes have different modules. The Node orchestrates a Tx Prover, a Tx Aggregator and a Block Producer. The Tx Prover executes and proves transactions, like in the Miden Client. The Tx Aggregator can batch multiple proofs together to reduce the final state proof size using recursive proving. The Block Producer exposes the RPC interface to the user. The Block Producer collects transactions in the Tx Pool and stores the state of Polygon Miden in its three databases (Accounts, Notes, Nullifiers).

## Verifier Contract
This contract on Ethereum verifies proofs sent by the operator running a Miden Node. The proof is verified against the current state root. If accepted the state root changes.

## Bridge Contract
This contract serves the Miden users on Ethereum as bridge. Users can deposit their tokens and get an equivalent amount minted and sent to the specified address on Polygon Miden.

