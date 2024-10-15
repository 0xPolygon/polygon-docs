!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

Particle Network's Wallet Abstraction services facilitate user onboarding and interactions that bridge Web2 and Web3. At its core is [Smart Wallet-as-a-Service (WaaS)](https://developers.particle.network/landing/wallet-abstraction/waas/overview), designed to onboard users into MPC-secured smart accounts that support any blockchain. This service offers developers enhanced user experiences through modular, fully customizable EOA/AA embedded wallets. 

Developers can integrate Particle's Smart Wallet-as-a-Service via APIs and SDKs for mobile and desktop. This enables secure key generation and management initiated by social or Web3 logins.

Additionally, across various EVM chains, including Polygon, Particle's Smart Wallet-as-a-Service can facilitate full-stack, modular implementation of Account Abstraction- handling key management.

Particle Wallet itself is available either in an application-embedded format, depending on the type of integration a specific developer chooses, or standalone through the [mobile](https://apps.apple.com/us/app/particle-crypto-wallet/id1632425771) or [web](https://wallet.particle.network) application, and it can be integrated via various SDKs. This page will cover [Particle Connect](https://developers.particle.network/api-reference/connect/desktop/web). 

Particle Connect is a React-based SDK that offers a unified solution for managing user onboarding through social logins (via Particle Auth) and standard Web3 wallets. This creates a consistent and accessible experience for Web3-native users and traditional consumers. 

- **Type**: Non-custodial.

- **Private Key Storage**: User’s local device/encrypted and stored with Particle.

- **Communication to Ethereum Ledger**: Mixed/Particle.

- **Key management mechanism**: MPC-TSS.

## Integrating Particle Connect

The [Particle Connect](https://developers.particle.network/api-reference/connect/desktop/web) SDK is the primary tool for facilitating wallet creation, login, and interaction with Particle. It provides a unified modal for connecting through social logins (via Particle Auth) or traditional Web3 wallets, ensuring an accessible experience for both Web3 users and mainstream consumers.

### Install dependencies

```js
yarn add @particle-network/connectkit viem@^2
```

OR

```js
npm install @particle-network/connectkit viem@^2

```

### Configure particle Connect

Now that you've installed the initial dependencies, you'll need to head over to the [Particle Network dashboard](https://dashboard.particle.network/#/login) to create a project & application so that you can acquire the required keys/IDs (`projectId`, `clientKey`, and `appId`) for configuration.

After obtaining your project keys, you can configure the SDK by wrapping your application with the `ParticleConnectkit` component. This allows you to apply customizations and input the project keys. 

Here is an example of a `Connectkit.tsx` file (based on Next.js) exporting the `ParticleConnectkit` component:

````ts
"use client";

import React from "react";
import { ConnectKitProvider, createConfig } from "@particle-network/connectkit";
import { authWalletConnectors } from "@particle-network/connectkit/auth";
import type { Chain } from "@particle-network/connectkit/chains";
// embedded wallet start
import { EntryPosition, wallet } from "@particle-network/connectkit/wallet";
// embedded wallet end
// aa start
import { aa } from "@particle-network/connectkit/aa";
// aa end
// evm start
import { polygon, polygonAmoy } from "@particle-network/connectkit/chains";
import {
  evmWalletConnectors,
  passkeySmartWallet,
} from "@particle-network/connectkit/evm";
// evm end

const projectId = process.env.NEXT_PUBLIC_PROJECT_ID as string;
const clientKey = process.env.NEXT_PUBLIC_CLIENT_KEY as string;
const appId = process.env.NEXT_PUBLIC_APP_ID as string;
const walletConnectProjectId = process.env
  .NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID as string;

if (!projectId || !clientKey || !appId) {
  throw new Error("Please configure the Particle project in .env first!");
}

const config = createConfig({
  projectId,
  clientKey,
  appId,
  appearance: {
    //  optional, sort wallet connectors
    connectorsOrder: ["passkey", "social", "wallet"],
    recommendedWallets: [
      { walletId: "metaMask", label: "Recommended" },
      { walletId: "coinbaseWallet", label: "Popular" },
    ],
    language: "en-US",
  },
  walletConnectors: [
    authWalletConnectors({
      authTypes: ["google", "apple", "twitter", "github"], // Optional, restricts the types of social logins supported
    }),
    // evm start
    evmWalletConnectors({
      // TODO: replace it with your app metadata.
      metadata: {
        name: "Connectkit Demo",
        icon:
          typeof window !== "undefined"
            ? `${window.location.origin}/favicon.ico`
            : "",
        description: "Particle Connectkit Next.js Scaffold.",
        url: typeof window !== "undefined" ? window.location.origin : "",
      },
      walletConnectProjectId: walletConnectProjectId,
      connectorFns: [passkeySmartWallet()],
      multiInjectedProviderDiscovery: false,
    }),

    // evm end
  ],
  plugins: [
    // embedded wallet start
    wallet({
      visible: true,
      entryPosition: EntryPosition.BR,
    }),
    // embedded wallet end

    // aa config start
    // With Passkey auth use Biconomy or Coinbase
    aa({
      name: "BICONOMY",
      version: "2.0.0",
    }),
    // aa config end
  ],
  chains: [polygon, polygonAmoy],
});

// Wrap your application with this component.
export const ParticleConnectkit = ({ children }: React.PropsWithChildren) => {
  return <ConnectKitProvider config={config}>{children}</ConnectKitProvider>;
};
````

Then, wrap your application with the `ParticleConnectkit` component. Here is an example of a `layout.tsx` file:

```ts
import { ParticleConnectkit } from '@/connectkit';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Particle Connectkit App',
  description: 'Generated by create next app',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ParticleConnectkit>{children}</ParticleConnectkit>
      </body>
    </html>
  );
}
```

### Facilitating login/connection

With Particle Connect configured, you can enable social logins in your application using the `ConnectButton` component.

```ts
import { ConnectButton, useAccount } from '@particle-network/connectkit';

export const App = () => {
    const { address, isConnected, chainId } = useAccount();

    // Standard ConnectButton utilization
    return (
        <div>
            <ConnectButton />
            {isConnected && (
                <>
                    <h2>Address: {address}</h2>
                    <h2>Chain ID: {chainId}</h2>
                </>
            )}
        </div>
    );
};

```

For managing interactions at the application level after onboarding, `@particle-network/connectkit` offers various hooks. You can explore all the available hooks in the [Particle Connect SDK](https://developers.particle.network/api-reference/connect/desktop/web#key-react-hooks-for-particle-connect) documentation. 

## Particle Connect Quickstart

Explore the [Particle Connect Quickstart](https://developers.particle.network/guides/wallet-as-a-service/waas/connect/web-quickstart) in the Particle Network documentation for a step-by-step guide on starting and configuring a new project.
