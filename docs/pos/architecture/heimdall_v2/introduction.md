# Heimdall-v2

Heimdall-v2 is a modernized and revamped consensus client that is at the heart of the Polygon PoS network. Similar to the previous version of Heimdall it performs the following functions:

- Manages validators.
- Handles block producer selection.
- Facilitates spans.
- Orchestrates the state sync mechanism between Ethereum and Polygon PoS.
- Addresses other essential aspects of the system.

It uses a fork of [*Cosmos SDK*](https://github.com/0xPolygon/cosmos-sdk) based on `v0.50.13` and a fork of [*CometBFT*](https://github.com/0xPolygon/cometbft/) based on `v0.38.17` for its consensus.

Heimdall leverages some modified versions of `cosmos-sdk` modules (`auth`, `bank` and `gov`) plus some fully customized modules (`bor`, `chainmanager`, `checkpoint`, `clerk`, `milestone`, `stake` and `topup`).

For detailed instructions on running Heimdall, refer to the [Readme](https://github.com/0xPolygon/heimdall-v2/blob/develop/README.md) in the Github repository
