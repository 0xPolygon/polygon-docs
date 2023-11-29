# Heimdall

Heimdall is the heart of the Polygon network. It manages validators, block producer selection, spans, the state-sync mechanism between Ethereum and Matic and other essentials aspects of the system.

It uses the **Cosmos-SDK** and a forked version of Tendermint, called **Peppermint**. Here is the Peppermint source: [https://github.com/maticnetwork/tendermint/tree/peppermint](https://github.com/maticnetwork/tendermint/tree/peppermint)

Heimdall removes some of the modules from Cosmos-SDK, but mostly uses a customised version of it while following the same pattern.
