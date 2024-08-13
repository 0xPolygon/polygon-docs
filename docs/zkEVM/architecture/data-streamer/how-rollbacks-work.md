---
comments: true
---

Recall that the server-source protocol begins with calling the $\texttt{StartAtomicOp}(\ )$, corresponding to which a message is sent to the stream server, preparing to receive entries related to a specific atomic operation.

When the stream source sends the entries, the stream server appends the data of the entries to the stream file.

Once all entries have been sent, the stream source calls the $\texttt{CommitAtomicOp}(\ )$ function, and the header of the stream file is subsequently updated. In particular, the $\texttt{totalLength}$ and $\texttt{totalEntries}$ fields.

But if the $\texttt{RollbackAtomicOp}(\ )$ is triggered instead of the $\texttt{CommitAtomicOp}(\ )$, the header is not updated.

In other words, the header of the stream file is updated only when the $\texttt{CommitAtomicOp}(\ )$ function is called. So, although some entries related to the atomic operation have already been added to the stream file, the header of the stream file is updated only with information of entries related to committed atomic operations.

Since the $\texttt{RollbackAtomicOp}(\ )$​ function can only be executed before a given atomic operation is committed, the header is not updated because the added entries (of the uncommitted atomic operation) will be overwritten with entries of the next atomic operation(s).

This means a rollback amounts to overwriting entries in the stream file that are related to an uncommitted atomic operation.

## Example (Commit and rollback)

Suppose an operation $\mathtt{Op_A}$ has been started, and $\texttt{100}$ entries had already been added to the stream file when a rollback was triggered. 

Since a rollback was triggered before $\mathtt{Op_A}$ was committed, the header of the stream file remains unaffected by the $\texttt{100}$​ added entries.

Let's say the $\texttt{totalLength}$ of the stream file is $\texttt{1712}$ when the rollback occurred. Although the actual length of the stream is $\texttt{1812}$, the $\texttt{totalLength}$ in the header of the stream file remains unchanged. 

Suppose that the next atomic operation $\mathtt{Op_B}$ gets started and committed, but has only $40$​ related entries.

Since $\mathtt{Op_B}$ is committed but only $40$ entries have been added to the stream file, the header will now reflect the $\texttt{totalLength}$ to be $1752$. This means only $\texttt{40}$ of the $\texttt{100}$ entries of the previously uncommitted operation $\mathtt{Op_A}$ got overwritten, but the actual stream is still $\texttt{1812}$.

How is this not a problem from an application point of view?

It's because if a stream client requests for the stream, the stream server sends the stream only up to the $\texttt{totalLength}$ recorded in the header of the stream file, $1752$, and not the actual length of the stream, $\texttt{1812}$.

## Concluding remarks

The basic trick here is for the stream server to only use the information recorded in the header of the stream file, and to change that information only if an atomic operation is committed.

This way the stream server always sends the stream only up to the last entry of the committed operation.

All-in-all, this is just an optimal way to rollback. There's no need to delete information from the stream file. The header of the stream file is updated only if an atomic operation has been committed. 

This is the main reason why parameters such as the $\texttt{totalLength}$ and $\texttt{totalEntries}$ are recorded in the header of the stream file.
