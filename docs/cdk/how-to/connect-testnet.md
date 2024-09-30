---
comments: true
---

## Stavanger

!!! warning
    - Stavanger is waiting for a stable redeployment.
    - You may experience errors on the testnet until the next CDK release.

The [CDK Stavanger testnet](https://polygon.technology/cdk-stavanger-testnet) is a validium testnet based on Sepolia.

- Add the RPC network details to your wallet by navigating to the add network input and entering the data as given in the table below.
- Use the faucet to get test ETH.
- Bridge assets from Sepolia to Stavanger using the bridge.
- Confirm your transactions with the block explorer.

!!! tips "Setting up your wallet"
    - Click **Connect wallet** on the [Stavanger explorer](https://sn2-stavanger-blockscout.eu-north-2.gateway.fm/) to auto set up your wallet.
    - Check out the latest on [setting up a custom network with MetaMask](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).

### Stavanger network details

| Name | Value | Usage |
| ------- | ----------- | --------- | 
| JSON RPC | https://sn2-stavanger-rpc.eu-north-2.gateway.fm | Make remote procedure calls to the CDK testnet. |
| Faucet | https://sn2-stavanger-faucet.eu-north-2.gateway.fm | Get testnet ETH |
| Bridge | https://sn2-stavanger-bridge.eu-north-2.gateway.fm | Bridge tokens from Sepolia |
| Block explorer | https://sn2-stavanger-blockscout.eu-north-2.gateway.fm | Confirm transactions with the explorer |
| Chain id | 686669576 | Chain identification value |
| Currency | ETH | Test token |

## Blackberry

The [Blackberry testnet](https://raas.gelato.network/rollups/details/public/polygon-blackberry) is a zero-knowledge-powered, layer 2 testnet based on Sepolia. It uses Polygon CDK for transaction validity while keeping transaction data off-chain using [DACs](https://docs.polygon.technology/cdk/glossary/#data-availability-committee-dac). 

- Add the RPC network details to your wallet by navigating to the add network input and entering the data as given in the table below.
- Obtain Sepolia ETH from the public faucets available.
- Bridge assets from the Ethereum Sepolia network to Blackberry using the bridge service.
- Confirm your transactions with the block explorer.

!!! tips "More information"
    - For more information on bridging and faucet services on Blackberry, head over to the [Gelato documentation](https://docs.gelato.network/rollup-public-testnet/faucets-and-bridging).

### Blackberry network details

| Name           | Value                                                     | Usage                                                  |
| -------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| JSON RPC       | `https://rpc.polygon-blackberry.gelato.digital`           | Make remote procedure calls to the Blackberry testnet. |
| Faucet         | `https://www.alchemy.com/faucets/ethereum-sepolia`        | Obtain sepolia ETH                                     |
| Bridge         | `https://bridge.gelato.network/bridge/polygon-blackberry` | Bridge assets from the ethereum sepolia network        |
| Block explorer | `https://polygon-blackberry.gelatoscout.com/`             | Confirm transactions with the explorer                 |
| Chain id       | `94204209`                                                | Chain identification value                             |
| Currency       | sETH                                                      | Test token                                             |
