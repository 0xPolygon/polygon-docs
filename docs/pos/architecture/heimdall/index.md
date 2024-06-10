# Heimdall

Heimdall is the heart of the Polygon PoS network. It performs the following functions:

- Manages validators.
- Handles block producer selection.
- Facilitates spans.
- Orchestrates the state sync mechanism between Ethereum and Polygon PoS.
- Addresses other essential aspects of the system.

It uses the *Cosmos SDK* and a forked version of Tendermint, called *Peppermint*. Here is the Peppermint source: [https://github.com/maticnetwork/tendermint/tree/peppermint](https://github.com/maticnetwork/tendermint/tree/peppermint)

Heimdall removes certain modules from Cosmos SDK but primarily utilizes a customized version of it, following a similar pattern.
