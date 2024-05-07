The data streamer is another component of the zkEVM infrastructure through which external nodes can access raw block data.

Any trustless node connected to the zkEVM can be up-to-date with the current L2 state by using the data streamer instead of using the JSON RPC.

Any archive node that needs to receive all information about blocks and their transactions with minimal delay can use the data streamer.

The usual procedure when working with the JSON RPC is that, for example;

-  The user's external node makes requests for information to the zkNode, 
-  The zkNode fetches this information from the internal database, and 
-  The zkNode relays it back to the requesting node.

Developer experience has shown that although the JSON RPC is perfect for small queries, it is not an efficient way to obtain huge amounts of data often required for fetching the entire L2 state.

A data streamer is best suited for the purpose of serving raw block data to external nodes that need to keep an up-to-date L2 state, irrespective of the required amount of data.

## Design approach

The design of the data streamer emulates the conventional L1 networks, where blocks are delivered to all nodes in the network via some peer-to-peer protocol, typically referred to as the gossip protocol.

With this approach the zkNode does not serve processed data via the JSON-RPC API to downstream nodes, but just ”fast streams” L2 data (which includes; batch data, block header data and transactions data) using a protocol with a low overhead. 

Instead of using existing streaming protocols, such as MQTT from IoT, the Polygon zkEVM team has developed a new custom-ware protocol, tailor-made for the zkEVM.

Developing their own protocol has the advantage of owning the code, and thus the team can alter it as required for the purpose of improving the zkEVM network.

The data streamer is a service that does not process blocks but sends them raw as they are generated.

## Data streamer building blocks

We present a general abstraction of the data streamer.

The basic architecture consists of a **data source**, **data server**, and **data client**, with an added option of a **stream relay** for better scalability.

![Figure: Data streamer archtectural overview](../../../img/zkEVM/ds-architectural-overview.png)

In the case of the Polygon zkEVM network, the data streamer is used by the sequencer.

The stream source is in fact the zkNode, in particular, the sequencer zkNode. And stream clients are requesters of network data.

By implementing the data streamer, it means stream clients do not have direct access to the stream source but go through stream servers. 

So, the data source sends L2 data to data servers, and data clients fetch the data from the stream servers.

This way, there can be a few stream servers connected to the stream source, and many stream clients fetching L2 data from any of the stream servers.

Ultimately, the stream server helps in easing congestion that could occur at the stream source.

There are two protocols to consider in this framework; the server-source protocol, and client-server protocol.

## Stream relay

For increased scalability, an intermediate node called **stream relay** is added to the architecture. And it is utilized as a "relayer" node between a stream server and a number of stream clients.

Such a stream relay is a client to some stream server but acts as a server to connected stream clients.

That is, each connected stream client sends messages to the stream relay according to the afore-mentioned client-server protocol.

And, the stream relay in turn acts as a client to a stream server, to which the stream relay sends the messages received from stream clients, also in line with the client-server protocol.

This design creates a highly scalable data streaming infrastructure.

![Figure](../../../img/zkEVM/ds-architectural-overview-w-relay.png)

