This document gives further details on the client-server protocol messages.

The stream client-server protocol messages are $\texttt{Start}$, $\texttt{StartBookmark}$, $\texttt{Stop}$, $\texttt{Header}$, $\texttt{Entry}$ and $\texttt{Bookmark}$​.

- The $\texttt{Start}$​​ message is sent from the stream client to the stream server in order to request for a stream to be sent.
    
    If the stream client wants to receive all the stream file, a $\texttt{Start}$ message is sent with an $\mathtt{entryNumber}$ $= \texttt{0}$.

    If the stream client knows the entry number at which the stream should start, it sends a $\texttt{Start}$ message with that particular entry number. That is, $\mathtt{entryNumber} \not= \texttt{0}$.

- $\texttt{StartBookmark}$ message is the type of message the stream client can send if the stream client does not know the entry number, but knows something more meaningful to the application, like a bookmark.
    
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
