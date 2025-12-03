# Quickstart for Buyers

_To implement x402 with Polygon and your applications or agents, checkout our_
_[Agentic Payments documentation.](https://agentic-docs.polygon.technology)_

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
";

## 2. Create a Wallet Client

Create a wallet client using a tool like [viem](https://viem.sh/):


```bash
npm install viem
```

Then, instantiate the wallet account and client:

```typescript
import { wrapFetchWithPayment, decodeXPaymentResponse } from "x402-fetch";
import { createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { polygonAmoy } from 'viem/chains';
import 'dotenv/config';

const privateKey = process.env.PRIVATE_KEY;
if (!privateKey) {
  throw new Error("PRIVATE_KEY not set in .env file");
}

const account = privateKeyToAccount(`0x${privateKey}`);
const client = createWalletClient({
  account,
  chain: polygonAmoy,
  transport: http()
});

console.log("Using wallet address:", account.address);
```

## 3. Make Paid Requests Automatically

You can use either `x402-fetch` or `x402-axios` to automatically handle 402 Payment Required responses and complete payment flows.

!!! info x402-fetch
    **x402-fetch** extends the native `fetch` API to handle 402 responses and payment headers for you. [Full example here](https://github.com/AkshatGada/x402_Polygon/tree/feature/facilitator-amoy/demo/quickstart-local)

```typescript
import { wrapFetchWithPayment, decodeXPaymentResponse } from "x402-fetch";
// other imports...

// wallet creation logic...

const FACILITATOR_URL = process.env.FACILITATOR_URL || "https://x402-amoy.polygon.technology"
const fetchWithPayment = wrapFetchWithPayment(fetch, client);

const url = process.env.QUICKSTART_RESOURCE_URL || 'http://127.0.0.1:4021/weather';

fetchWithPayment(url, { //url should be something like https://api.example.com/paid-endpoint
  method: "GET",
})
  .then(async response => {
    const body = await response.json();
    console.log('Response body:', body);

    // Only try to decode payment response if we got the weather data (not the 402 response)
    if (body.report) {
      console.log('All response headers:', Object.fromEntries(response.headers.entries()));
      const rawPaymentResponse = response.headers.get("x-payment-response");
      console.log('Raw x-payment-response:', rawPaymentResponse);

      try {
        const paymentResponse = decodeXPaymentResponse(rawPaymentResponse);
        console.log('Decoded payment response:', paymentResponse);
      } catch (e) {
        console.error('Error decoding payment response:', e);
        console.error('Failed to decode response:', rawPaymentResponse);
        throw e;
      }
    }
  })
  .catch(async error => {
    console.error('Error:', error.message);
    if (error.response) {
      try {
        const text = await error.response.text();
        console.error('Response text:', text);
        console.error('Response status:', error.response.status);
        console.error('Response headers:', error.response.headers);
      } catch (e) {
        console.error('Error reading response:', e);
        console.error('Raw error:', error);
      }
    } else {
      console.error('Raw error:', error);
    }
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