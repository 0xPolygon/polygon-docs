This gives further details on the client-server protocol messages.

The stream client-server protocol messages are $\texttt{Start}$, $\texttt{StartBookmark}$, $\texttt{Stop}$, $\texttt{Header}$, $\texttt{Entry}$ and $\texttt{Bookmark}$​.

- The $\texttt{Start}$​​ message is sent from the stream client to the stream server in order to request for a stream to be sent.
    
    If the stream client wants to receive all the stream file, a $\texttt{Start}$ message is sent with an $\mathtt{entryNumber}$ $= \texttt{0}$.

    If the stream client knows the entry number at which the stream should start, it sends a $\texttt{Start}$ message with that particular entry number. That is, $\mathtt{entryNumber} \not= \texttt{0}$.

- $\texttt{StartBookmark}$ message is the type of message the stream client can send if the the stream client does not the know entry number, but knows something more meaningful to the application, like a bookmark.
    
    In the case of the Polygon zkEVM, if the stream client wants to receive information from a certain L2 block number, then it provides the appropriate bookmark by sending a $\texttt{StartBookmark}$ message.

    Such a bookmark is actually a codification of the L2 block number.

- $\texttt{Stop}$ message is a message the stream client can send to the stream server if it wants to stop receiving the stream.
    
- $\texttt{Header}$ message can be sent if the stream client requests just the header of a particular entry.
    
    We discuss the information an entry contains, in more detail, later in this document.

    In summary, an entry has two parts: a part called a $\texttt{Header}$, and a part called the $\texttt{data}$.

    So, a $\texttt{Header}$ message is used to request for just the header, but not the full data of an entry.

    It's like asking for only the block header and not the entire L2 block, in the Polygon zkEVM case.

- $\texttt{Entry}$ message can be sent by the stream client in order to request for a specific entry in the stream file. Thus, instead of requesting the stream server to start streaming from a particular entry onwards, only one entry is obtained by sending an $\texttt{Entry}$ message.
    
- $\texttt{Bookmark}$ message is a message in which a stream client sends a bookmark to the stream server, and the stream server in turn tells the stream client what entry number is linked to the bookmark.

The above six messages are all messages used in the client-server protocol. And they can be found [here](https://github.com/0xPolygonHermez/zkevm-data-streamer#stream-tcp-commands).

## Stream server-source library

Interaction between the stream source and each stream server is enabled by the Server-source library, which is a Go library with six main functions for modifying or adding entries to operations.

### Send data functions

When each of these functions is called, a corresponding message is generated and sent to the stream server:

1. $\texttt{StartAtomicOp}(\ )$ starts an atomic operation. When called, a message that amounts to saying: "start an atomic operation," is generated and sent from the stream source to the stream server.
2. $\texttt{AddStreamEntry(u32 entryType, u8[] data)}$ adds an entry to the atomic operation and returns an $\texttt{u64 entryNumber}$. When called, a message equivalent to saying: "Add an entry of this type, with this data, to the current atomic operation," is generated and sent to the stream server.
3. $\texttt{AddStreamBookmark(u8[] bookmark)}$ adds an entry to the atomic operation and returns an $\texttt{u64}$ $\texttt{entryNumber}$. 
4. $\texttt{CommitAtomicOp}(\ )$ commits an operation $\texttt{Op}$ so that its entries can be sent to stream clients. When called, a message which is tantamount to saying: "All entries associated with the current operation have been sent, the operation ends with the last sent entry," is generated and sent to the stream server.
5. $\texttt{RollbackAtomicOp}(\ )$ rolls back an atomic operation. 
6. $\texttt{UpdateEntryData(u64 entryNumber, u32 entryType, u8[] newData)}$ updates an existing entry. This function only applies to entries for which the atomic operation has not been committed.



### Query data functions

The stream source can use a few more functions of the stream server-source library, to get information from the stream server.

It uses the following functions:

- $\texttt{GetHeader()}$: The stream source uses this function to query the header of a particular entry. The function returns, $\texttt{struct HeaderEntry}$.
- $\texttt{GetEntry(u64 entryNumber)}$: This function is used to get an entry that corresponds to a given entry number. It returns, $\texttt{struct FileEntry}$.
- $\texttt{GetBookmark(u8[ ] bookmark)}$: The stream source uses this function to get a bookmark. The function returns, $\texttt{u64 entryNumber}$.
- $\texttt{GetFirstEventAfterBookmark(u8[ ] bookmark)}$: This function is used to get the first entry after a given bookmark. It returns, $\texttt{struct FileEntry}$.



The complete stream source-server library is described, but referred to as the DATA STREAMER INTERFACE (API), [here](https://github.com/0xPolygonHermez/zkevm-data-streamer#data-streamer-interface-api).

It's possible to create, using the stream source-server library, a stream source that connects with a server, opens and commits operations.
