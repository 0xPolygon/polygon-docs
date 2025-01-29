# LayerZero

!!! note "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

[LayerZero](https://layerzero.network) is an **omnichain interoperability protocol** that enables smart contracts to seamlessly communicate between different blockchain networks. With LayerZero V2, applications deployed on Polygon can connect and interact with 100+ supported blockchains through secure, configurable messaging channels.

## Key Features

LayerZero enables powerful cross-chain capabilities for builders on Polygon:

1. **Cross-chain Messaging** - Send arbitrary messages and data between contracts on different chains
2. **Omnichain Tokens** - Deploy tokens (fungible `OFT` and non-fungible `ONFT`) that work seamlessly across multiple chains
3. **External Chain Data Access** (`lzRead`) - Fetch and compute on-chain state from other networks
4. **Composed Messages** - Chain multiple cross-chain operations together

!!! tip "Quickstart"

    Check out this **[Quickstart Guide](https://docs.layerzero.network/v2/developers/evm/create-lz-oapp/start)** to see how to create your first omnichain app.

## How it works

1. **DVNs** independently verify that a message is valid, waiting for a configured number of block confirmations on the source chain.
2. When the message is verified, **Executors** on the destination chain deliver the message to the target contract, paying for the destination gas automatically in the background. The user only pays for gas on the source chain.

Because each application can configure its own DVN sets, your security is not locked into a single aggregator or middlechain. For more details, check out the [LayerZero docs](https://docs.layerzero.network/).

To run your own DVN as part of your security set, check out the [DVN docs](https://docs.layerzero.network/v2/developers/evm/off-chain/build-dvns).

## Polygon Integration

When integrating with LayerZero, there are two key aspects to understand:

1. The [LayerZero Endpoint](https://docs.layerzero.network/v2/home/protocol/layerzero-endpoint)
   - Immutable smart contract that serves as the entry and exit point for messages
   - Allows applications to configure security and execution parameters
   - Provides interfaces for sending, receiving and reading cross-chain data
2. [Security Stack](https://docs.layerzero.network/v2/home/modular-security/security-stack-dvns)
   - Configurable set of Decentralized Verifier Networks (DVNs) that validate messages
   - Allows applications to customize security and cost tradeoffs
   - Ensures message integrity across chains

### Contract Addresses

| Chain                         | Chain Id | Endpoint Id | Endpoint Address                                                                                                                                          |
| ----------------------------- | -------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Polygon Mainnet               | 137      | 30109       | [0x1a44076050125825900e736c501f859c50fE728c](https://layerzeroscan.com/api/explorer/polygon/address/0x1a44076050125825900e736c501f859c50fE728c)           |
| Polygon Amoy Testnet          | 80002    | 40267       | [0x6EDCE65403992e310A62460808c4b910D972f10f](https://layerzeroscan.com/api/explorer/amoy-testnet/address/0x6EDCE65403992e310A62460808c4b910D972f10f)      |
| Polygon zkEVM Mainnet         | 1101     | 30158       | [0x1a44076050125825900e736c501f859c50fE728c](https://layerzeroscan.com/api/explorer/zkevm/address/0x1a44076050125825900e736c501f859c50fE728c)             |
| Polygon zkEVM Sepolia Testnet | 2442     | 40247       | [0x6EDCE65403992e310A62460808c4b910D972f10f](https://layerzeroscan.com/api/explorer/zkpolygon-sepolia/address/0x6EDCE65403992e310A62460808c4b910D972f10f) |

Once a transaction is submitted, you can trace it on [LayerZero Scan](https://layerzeroscan.com/), which shows cross-chain message flow from source to destination in real time.

## Getting Started

Developers should:

1. Deploy contracts on each chain: [Quickstart - Create Your First Omnichain App](https://docs.layerzero.network/v2/developers/evm/create-lz-oapp/start)
2. Configure a Security Stack by selecting DVNs & block confirmations (optional).
3. Optionally configure an Executor or use defaults to deliver messages.
4. Send messages, send tokens (OFT, ONFT), or read state on any chain, using LayerZero.

## Example Use Cases

LayerZero powers various cross-chain applications across different categories:

1. **Omnichain Tokens (OFTs)** (e.g., [Ethena's USDe](https://ethena.fi/), Wrapped Bitcoin)
   - Unified token supply across chains
   - Native bridging without intermediary tokens
   - Real-world examples include USDe, sUSDe, ENA tokens, and WBTC
2. **Cross-chain DEXs** (e.g., [Trader Joe](https://traderjoexyz.com/))
   - Unified liquidity pools across chains
   - Cross-chain swaps and trading
3. **Omnichain Lending** (e.g., [Radiant Capital](https://radiant.capital/))
   - Supply assets on any chain
   - Borrow against cross-chain collateral
4. **Cross-chain Governance** (e.g., [Stargate DAO](https://stargate.finance/))
   - Vote on one chain, execute on many
   - Unified governance across deployments
5. **Chain Data Oracles**
   - Read and verify external chain state
   - Make decisions based on cross-chain data

## Resources

1. [LayerZero Developer Documentation](https://docs.layerzero.network/v2)
2. [LayerZero Scan](https://layerzeroscan.com/) - Message explorer and debugging
3. [Discord Community](https://discord.gg/layerzero)
4. [GitHub](https://github.com/LayerZero-Labs/)
