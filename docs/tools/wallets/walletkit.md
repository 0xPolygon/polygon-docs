!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

![WalletKit](../../img/tools/wallet/walletkit/walletkit-overview.png)

[WalletKit](https://walletkit.com) is an all-in-one platform for adding smart, gasless wallets to your app. WalletKit offers pre-built components for onboarding users with email and social logins, which can be integrated in under 15 minutes using their React SDK or the wagmi connector. Alternatively, build completely bespoke experiences for your users using WalletKit's Wallets API.

WalletKit is compatible with most EVM chains, including Polygon. It has integrated support for ERC-4337 and comes with a paymaster and bundler included, requiring no extra setup.

You can check out the [WalletKit documentation here](https://docs.walletkit.com). Start building for free on the Polygon testnet today.

## Integration

### Install the SDK

```bash
npm i @walletkit/react-link walletkit-js
```
or 
```bash
yarn add @walletkit/react-link walletkit-js
```

### Setup WalletKit

Initialize `WalletKitLink` with your Project ID and wrap your app with `WalletKitProvider`, adding it as close to the
root as possible.

You can get your Project ID from the API Keys page in the [WalletKit dashboard](https://app.walletkit.com).

```ts
import { WalletKitLink, WalletKitLinkProvider } from "@walletkit/react-link";

const wkLink = new WalletKitLink({
  projectId: "<WalletKit-Project-ID>",
});

export function App() {
  return <WalletKitLinkProvider link={wkLink}>...</WalletKitLinkProvider>;
}
```

> ☝️ If you'd like to integrate WalletKit with wagmi, check out
the [installation docs here](https://docs.walletkit.com/link/installation).
