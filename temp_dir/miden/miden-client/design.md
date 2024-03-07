The Miden client contains a few key features:

- Store
- RPC client
- Transaction Executor

The RPC client and Store are defined as Rust traits, in order to allow developers and users to utilize the implementation they desire for any specific environment.

## Store

The store is central to the client's design and is in charge of enabling persistence over the following entities:

- Accounts, their history of states and related information such as vault assets or account code
- Transactions and their scripts
- Notes
- Block headers and chain information that the client needs to properly execute transactions and consume notes
 
Because Miden allows for off-chain executing and proving, the client needs to know about the state of the blockchain at the moment of execution. To avoid state bloat, however, the client does not deal with the whole blockchain history, but rather with the parts of the chain history that are relevant to the user. 

The store can track any number of accounts, and in turn any number of notes that those accounts might have created or may want to consume. 

## RPC client

The RPC client allows for communicating with the node through a defined set of gRPC methods. Currently, these methods are:

- `GetBlockHeaderByNumber`
- `SyncState`: Asks the node for relevant information to the client. That is, account changes for accounts that it's tracking, whether relevant notes have been created or consumed, etc.
- `SubmitProvenTransaction`: After a transaction has been locally proven, the client will send it to the node for inclusion in the blockchain

## Transaction Executor

Lastly, the client contains a transaction executor that allows for executing transactions with the Miden VM. 

When executing, the executor will need to access relevant blockchain history, which is why the executor is generic over a `DataStore` which is an interface for accessing this data. Because of this, the executor and the store might be somewhat coupled as well.
