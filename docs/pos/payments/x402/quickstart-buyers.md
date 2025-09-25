# Quickstart for Buyers

This guide will walk you how to use x402 on Polygon 
to interact with services that require payment.

By the end of this guide, you will be able to programmatically discover
payment requirements, complete a payment, and access a paid resource.

## Prerequisites
Before you begin, ensure you have:

* Metamask, Rabby or any wallet that support Polygon with USDC

* [Node.js](https://nodejs.org/en) and npm

## 1. Install Dependencies

**HTTP Clients**

Install [x402-axios](https://www.npmjs.com/package/x402-axios) or [x402-fetch](https://www.npmjs.com/package/x402-fetch):

```bash
npm install x402-axios
# or
npm install x402-fetch
```

## 2. Create a Wallet Client

Create a wallet client using a tool like [viem](https://viem.sh/):


```bash
npm install viem
```

Then, instantiate the wallet account:

```typescript
import { createWalletClient, http } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygonAmoy } from "viem/chains";

// Create a wallet client (using your private key)
const account = privateKeyToAccount("0xYourPrivateKey"); // we recommend using an environment variable for this
```

## 3. Make Paid Requests Automatically

You can use either `x402-fetch` or `x402-axios` to automatically handle 402 Payment Required responses and complete payment flows.

!!! info x402-fetch
    **x402-fetch** extends the native `fetch` API to handle 402 responses and payment headers for you. [Full example from Coinbase here](https://github.com/coinbase/x402/tree/main/examples/typescript/clients/fetch)

```typescript
import { wrapFetchWithPayment, decodeXPaymentResponse } from "x402-fetch";
// other imports...

// wallet creation logic...

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

fetchWithPayment(url, { //url should be something like https://api.example.com/paid-endpoint
  method: "GET",
})
  .then(async response => {
    const body = await response.json();
    console.log(body);

    const paymentResponse = decodeXPaymentResponse(response.headers.get("x-payment-response")!);
    console.log(paymentResponse);
  })
  .catch(error => {
    console.error(error.response?.data?.error);
  });
```

## 4. Error Handling
Clients will throw errors if:

* The request configuration is missing

* A payment has already been attempted for the request

* There is an error creating the payment header

## Summary
* Install an x402 client package

* Create a wallet client

* Use the provided wrapper/interceptor to make paid API requests

* Payment flows are handled automatically for you

## References:

* [x402-fetch npm docs](https://www.npmjs.com/package/x402-fetch)

* [x402-axios npm docs](https://www.npmjs.com/package/x402-axios)