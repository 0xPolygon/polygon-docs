Interaction between the stream source and each stream server is enabled by the [`server-source`](https://github.com/0xPolygonHermez/zkevm-data-streamer#data-streamer-interface-api) library, which is a Go library with six main functions for modifying or adding entries to operations.

### Send data functions

When each of these functions is called, a corresponding message is generated and sent to the stream server:

1. $\texttt{StartAtomicOp}(\ )$ starts an atomic operation. When called, a message that amounts to saying: "start an atomic operation," is generated and sent from the stream source to the stream server.
2. $\texttt{AddStreamEntry(u32 entryType, u8[] data)}$ adds an entry to the atomic operation and returns an $\texttt{u64 entryNumber}$. When called, a message equivalent to saying: "Add an entry of this type, with this data, to the current atomic operation," is generated and sent to the stream server.
3. $\texttt{AddStreamBookmark(u8[] bookmark)}$ adds an entry to the atomic operation and returns an $\texttt{u64}$ $\texttt{entryNumber}$. 
4. $\texttt{CommitAtomicOp}(\ )$ commits an operation $\texttt{Op}$ so that its entries can be sent to stream clients. When called, a message which is tantamount to saying: "All entries associated with the current operation have been sent, the operation ends with the last sent entry," is generated and sent to the stream server.
5. $\texttt{RollbackAtomicOp}(\ )$ rolls back an atomic operation. 
6. $\texttt{UpdateEntryData(u64 entryNumber, u32 entryType, u8[] newData)}$ updates an existing entry. This function only applies to entries for which the atomic operation has not been committed.

### Query data functions

The stream source uses the following functions of the stream server-source library to get information from the stream server.


- $\texttt{GetHeader()}$: The stream source uses this function to query the header of a particular entry. The function returns, $\texttt{struct HeaderEntry}$.
- $\texttt{GetEntry(u64 entryNumber)}$: This function is used to get an entry that corresponds to a given entry number. It returns, $\texttt{struct FileEntry}$.
- $\texttt{GetBookmark(u8[ ] bookmark)}$: The stream source uses this function to get a bookmark. The function returns, $\texttt{u64 entryNumber}$.
- $\texttt{GetFirstEventAfterBookmark(u8[ ] bookmark)}$: This function is used to get the first entry after a given bookmark. It returns, $\texttt{struct FileEntry}$.

!!! tip

    Find out more about the [DATA STREAMER INTERFACE (API)](https://github.com/0xPolygonHermez/zkevm-data-streamer#data-streamer-interface-api).

It's possible to create, using the stream source-server library, a stream source that connects with a server, opens and commits operations.
