# Heimdall v2

Heimdall v2 is a modernized and revamped consensus client that is at the heart of the Polygon PoS network. Similar to the previous version of Heimdall it performs the following functions:

- Manages validators.
- Handles block producer selection.
- Facilitates spans.
- Orchestrates the state sync mechanism between Ethereum and Polygon PoS.
- Addresses other essential aspects of the system.

It uses the latest [*Cosmos SDK*](https://github.com/maticnetwork/cosmos-sdk) and [*CometBFT*](https://github.com/cometbft/cometbft) for its consensus.

Heimdall removes certain modules from Cosmos SDK but primarily utilizes a customized version of it, following a similar pattern.

For detailed instructions on running Heimdall v2, refer to the [Readme](https://github.com/0xPolygon/heimdall-v2/blob/develop/README.md) in the Github repository