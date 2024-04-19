!!! caution "Content disclaimer" 
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

**Venly** allows you to easily integrate your app to the Polygon blockchain, whether you already have an app integrated with Web3 or are building a new app from scratch. Venly provides a smooth and delightful experience for you and your users on both web & mobile.

Venly will help you interact with the Polygon network, create blockchain wallets, create different asset types such as fungible (ERC20), and non-fungible tokens (ERC721 and ERC1155), and interact with smart contracts. Next to a superior developer experience, you can give your users a user-friendly interface.

Each application is unique and has different needs, providing different ways of interacting with Venly. We recommend that web3 applications integrate the [Venly web3 provider](https://docs.venly.io/docs/web3js), others may use the [Venly Widget](https://docs.venly.io/docs/widget-overview).

## Key features

- Support web and mobile.
- Offers social logins.
- Offers fiat-on-ramp.
- Supports both Polygon and Ethereum.
- Supports NFTs (ERC721 and ERC1155) on Polygon.
- Easy to integrate using Web3.
- Built for a mainstream audience.
- Offers in-app customer support.

## Getting started 

If you already support web3 technology, you can improve your application's UX by integrating the [Venly web3 provider](https://docs.venly.io/docs/web3js), a smart wrapper around the existing web3 Ethereum JavaScript API.

By using our [web3 provider](https://docs.venly.io/docs/web3js), you can leverage the full potential of Venly with minimal effort, and you will be able to onboard less tech-savvy users without making them leave your application or download third-party plugins. Integrating just takes two steps and 5 minutes!

**Don't support web3 yet?**

> Don't worry we've got you covered with our 📦 [Venly - Widget](https://docs.venly.io/docs/widget-overview).

### Step 1: Add the library to your project

Install the library by downloading it to your project via NPM.

```javascript
npm i @venly/web3-provider
```

Alternatively, you could also include the library directly from a CDN.

```javascript
<script src="https://unpkg.com/@venly/web3-provider/umd/index.js"></script>
```

```javascript
<script src="https://cdn.jsdelivr.net/npm/@venly/web3-provider/umd/index.js"></script>
```

## Step 2: Initialize the web3 provider

Add the following lines of code to your project, it will load the Venly web3 provider.

### Simple

```javascript
import Web3 from 'web3';
import { VenlyProvider } from '@venly/web3-provider';

const Venly = new VenlyProvider();
const options: VenlyProviderOptions = {
  clientId: 'YOUR_CLIENT_ID'
};

const provider = await Venly.createProvider(options);
const web3 = new Web3(provider);
```

### Advanced

```javascript
import Web3 from 'web3';
import { VenlyProvider } from '@venly/web3-provider';

const Venly = new VenlyProvider();
const options = {
  clientId: 'YOUR_CLIENT_ID',
  environment: 'staging', //optional, production by default
  signMethod: 'POPUP', //optional, REDIRECT by default
  bearerTokenProvider: () => 'obtained_bearer_token', //optional, default undefined
  //optional: you can set an identity provider to be used when authenticating
  authenticationOptions: {
    idpHint: 'google'
  },
  secretType: 'ETHEREUM' //optional, ETHEREUM by default
};

const provider = await Venly.createProvider(options);
const web3 = new Web3(provider);
```

You can fetch wallets, and sign transactions, and messages.

Congratulations, your dapp now supports Venly.

Ready to try out the Wallet-Widget? [Click here to get started](https://docs.venly.io/docs/widget-getting-started).
Want to know more about what Venly has to offer? [Check out the documentation](https://docs.venly.io/docs/widget-overview).

## More about Venly

Venly stands out because of its commitment to supporting not only their wallet users by explaining what gas is, or by helping them import an Ethereum wallet into Polygon, but also the developers that are using Venly to build new products.

At Venly, we offer a diverse range of products spanning various categories, including Wallet Solutions, NFT Tools, and Marketplaces. Let's begin with a brief overview of these three product categories:

- [Wallet solutions](https://docs.venly.io/docs/wallet-api-overview): Empower your users by providing them with a wallet or seamlessly integrating the Venly wallet into your application.
- [NFT tools](https://docs.venly.io/docs/nft-api-overview): Facilitate the creation and distribution of NFTs, along with fetching comprehensive NFT data and information.
- [Marketplaces](https://docs.venly.io/docs/market-api-overview): Build your own NFT marketplace or list your NFT collection on our existing marketplace.

Even in their test environments, they add an in-app chat so that developers can directly communicate with the team behind the Venly platform. In case you want to learn more, check out their [detailed product documentation](https://docs.venly.io/docs/getting-started-with-venly).

## Resources

- [Venly widget](https://docs.venly.io/docs/widget-overview)
- [Web3 wallet providers](https://docs.venly.io/docs/ethersjs)
- [Web3.js](https://docs.venly.io/docs/web3js)
