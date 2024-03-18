!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

Particle Network's Wallet Abstraction services enable universal, Web2-adjacent onboarding and interactions. Its core technology, [Smart Wallet-as-a-Service](https://blog.particle.network/announcing-our-smart-wallet-as-a-service-modular-stack-upgrading-waas-with-erc-4337) (WaaS) aims to onboard users into MPC-secured smart accounts supporting any chain. It also allows developers to offer an improved user experience through modular, fully customizable EOA/AA embedded wallets. Particle supports its Smart Wallet-as-a-Service through a Modular L1 powering chain abstraction, acting as a settlement layer across chains for a seamless multi-chain experience.

Through APIs and SDKs available on both mobile and desktop platforms, developers can integrate Particle's Smart Wallet-as-a-Service to enable secure key generation and management initiated by Web2 logins, with the capacity to be customized and implemented in a way that matches the specific needs of a given application.

Additionally, across a variety of EVM chains, including Polygon, Particle's Smart Wallet-as-a-Service can facilitate full-stack, modular implementation of Account Abstraction- handling key management.

Particle Wallet itself is available either in an application-embedded format, depending on the type of integration a specific developer chooses, or standalone through the [mobile](https://apps.apple.com/us/app/particle-crypto-wallet/id1632425771) or [web](https://wallet.particle.network) application. Particle Wallet offers a range of features, including a toggleable ERC-4337 mode, 1inch-powered swaps, LI.FI-powered bridging, and other standard and miscellaneous functions.

- **Type**: Non-custodial.
- **Private Key Storage**: User’s local device/encrypted and stored with Particle.
- **Communication to Ethereum Ledger**: Mixed/Particle.
- **Key management mechanism**: MPC-TSS.

## Integrating Particle Auth

The [Particle Auth](https://developers.particle.network/reference/auth-web) SDK represents the primary method of facilitating connection (wallet generation or login) and interaction with Particle.

#### Install dependencies

```js
yarn add @particle-network/auth @particle-network/provider
```

OR

```js
npm install --save @particle-network/auth @particle-network/provider
```

#### Configure particle

Now that you've installed the initial dependencies from Particle Network, you'll need to head over to the [Particle Network dashboard](https://dashboard.particle.network/#/login) to create a project & application so that you can acquire the required keys/IDs (`projectId`, `clientKey`, and `appId`) for configuration.

````js
import { ParticleNetwork } from "@particle-network/auth";
import { ParticleProvider } from "@particle-network/provider";
import Web3 from "web3";

const particle = new ParticleNetwork({
  projectId: "xx",
  clientKey: "xx",
  appId: "xx",
  chainName: "polygon", //optional: current chain name, default Ethereum.
  chainId: "137", //optional: current chain id, default 1.
  wallet: {   //optional: by default, the wallet interface is displayed in the bottom right corner of the webpage as an embedded popup.
    displayWalletEntry: true,  //show wallet when connecting with particle.
    uiMode: "dark",  //optional: light or dark, if not set, the default is the same as web auth.
    supportChains: [{ id: 137, name: "Polygon"}, { id: 1, name: "Ethereum"}], // optional: web wallet support chains.
    customStyle: {}, //optional: custom wallet style
  },
  securityAccount: { //optional: particle security account config
    //prompt set payment password. 0: None, 1: Once(default), 2: Always
    promptSettingWhenSign: 1,
    //prompt set master password. 0: None(default), 1: Once, 2: Always
    promptMasterPasswordSettingWhenLogin: 1
  },
});

const particleProvider = new ParticleProvider(particle.auth);
window.web3 = new Web3(particleProvider);
````

#### Facilitating login/connection

````js
if (!particle.auth.isLogin()) {
    // Request user login if needed, returns current user info
    const userInfo = await particle.auth.login();
}
````

From this point, you can utilize `web3.js` as usual via `window.web3`. Signatures, confirmations, and other interactions will be routed to the embedded Particle interface, provided that a user is connected.

The functionality of this SDK, alongside the various other SDKs & APIs that Particle offers, extends far. You can learn more about integrating and interacting with Particle [here](https://docs.particle.network/getting-started/get-started).
