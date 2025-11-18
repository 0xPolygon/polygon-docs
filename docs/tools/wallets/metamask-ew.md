!!!caution
    Content disclaimer

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).


Integrate **MetaMask Embedded Wallets** (formerly *Web3Auth*) to enable instant, secure, and seamless wallet onboarding for your users on **Polygon** — with **no additional code** required.

MetaMask Embedded Wallets lets users sign in with familiar logins (Google, Apple, Discord, etc.) and instantly creates a **non-custodial wallet** connected to **Polygon**.  
 It’s fast, simple, and fully managed through the MetaMask Dashboard.

## Why Use MetaMask Embedded Wallets on Polygon?

* **Instant onboarding:** Use OAuth providers like Google or Apple for quick user authentication  
* **Simple configuration:** Set up Polygon once through the dashboard  
* **Non-custodial:** Users retain full control of their private keys  
* **Cross-platform support:** Works on web, mobile, and game engines  
* **Web2 \- friendly UX:** Familiar login and onboarding flows

### Key Features

* **External Wallet Aggregator:** Integrates SSO logins with existing crypto wallets (e.g. MetaMask), compatible with EVM and Solana.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/features/external-wallets/) 

* **Flexible Authentication:** Supports Google, Facebook, X, passwordless email, and custom OAuth2.0, enabling frictionless Web2-to-Web3 onboarding.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/dashboard/authentication/)

* **Group Connections:** Link multiple SSOs using a shared unique ID (e.g. same email) so users can access the same wallet via different logins.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/authentication/group-connections/)

* **Wallet Pregeneration:** Create wallets pre-registration using unique identifiers (e.g. email) to pre-fund for airdrops or bonuses.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/features/wallet-pregeneration/)

* **Multi-Factor Authentication:** Enforce additional security layers like OTPs or secondary SSOs for sensitive use cases.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/sdk/vue/advanced/mfa/)

* **Cross-Platform SDKs:** Available for React, Vue, JavaScript, Android, iOS, React Native, Flutter, Unity, and Unreal—users access the same wallet across devices.

* **Native Smart Accounts:** Enable gas sponsorships, batch/automated transactions, spending caps, and automatic paymaster/bundler setup (Infura \+ Pimlico).  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/features/smart-accounts/)

* **UI Flexibility:** Choose between prebuilt white-labelled UI or headless SDK for full customization and brand control.  
   🔗 [Docs](https://docs.metamask.io/embedded-wallets/sdk/vue/advanced/wallet-services/)

## **1\. Dashboard Configuration (No Code Required)**

All setup happens inside the **MetaMask Embedded Wallets Dashboard** — no SDK changes or code edits are required.

### **Steps**

1. Go to the [MetaMask Embedded Wallets Dashboard](https://dashboard.web3auth.io/).  
2. Select your project or create a new one.  
3. Navigate to the **Chains** tab.  
4. Search for **Polygon**.  
5. Save your configuration.

✅ Once enabled, all MetaMask Embedded Wallets SDKs (React, Vue, JavaScript) will automatically connect to **Polygon** — **no code updates needed**.

## **3\. Multi-Platform SDKs**

MetaMask Embedded Wallets supports every major developer environment — so your dApps, mobile apps, and games can all connect seamlessly to **Polygon**.

| Platform | SDK Documentation |
| ----- | ----- |
| **React** | [docs.metamask.io/embedded-wallets/sdk/react](https://docs.metamask.io/embedded-wallets/sdk/react) |
| **Vue** | [docs.metamask.io/embedded-wallets/sdk/vue](https://docs.metamask.io/embedded-wallets/sdk/vue) |
| **JavaScript** | [docs.metamask.io/embedded-wallets/sdk/js](https://docs.metamask.io/embedded-wallets/sdk/js) |
| **Node.js** | [docs.metamask.io/embedded-wallets/sdk/node](https://docs.metamask.io/embedded-wallets/sdk/node) |
| **Android** | [docs.metamask.io/embedded-wallets/sdk/android](https://docs.metamask.io/embedded-wallets/sdk/android) |
| **iOS** | [docs.metamask.io/embedded-wallets/sdk/ios](https://docs.metamask.io/embedded-wallets/sdk/ios) |
| **React Native** | [docs.metamask.io/embedded-wallets/sdk/react-native](https://docs.metamask.io/embedded-wallets/sdk/react-native) |
| **Flutter** | [docs.metamask.io/embedded-wallets/sdk/flutter](https://docs.metamask.io/embedded-wallets/sdk/flutter) |
| **Unity** | [docs.metamask.io/embedded-wallets/sdk/unity](https://docs.metamask.io/embedded-wallets/sdk/unity) |
| **Unreal Engine** | [docs.metamask.io/embedded-wallets/sdk/unreal](https://docs.metamask.io/embedded-wallets/sdk/unreal) |

## **4\. Connecting to Polygon**

After enabling **Polygon** on the dashboard, MetaMask Embedded Wallets handles all connection logic automatically.

### **For JS based SDKs (React, Vue, JS & Node)**

The wallet connects to **Polygon** using the chain configuration you set in the dashboard.  
 No developer setup required — the provider is pre-configured and ready to use.

### **For Mobile & Gaming SDKs (Android, iOS, Flutter, Unity, Unreal)**

These SDKs expose a **user’s private key** securely. Developers can use it with their preferred blockchain library (e.g., `ethers.js`, `web3j`, or engine-native signing tools) to interact with **Polygon** RPCs.

**Navigate to the dedicated documentation for Polygon on MetaMask Embedded Wallets docs.**

## **Learn More**

* **MetaMask Embedded Wallets Overview:** [docs.metamask.io/embedded-wallets](https://docs.metamask.io/embedded-wallets/)

* **Polygon Integration Guide:** [docs.metamask.io/embedded-wallets/connect-blockchain/evm/polygon](https://docs.metamask.io/embedded-wallets/connect-blockchain/evm/polygon)

* **Dashboard Access:** [dashboard.web3auth.io](https://dashboard.web3auth.io/)

