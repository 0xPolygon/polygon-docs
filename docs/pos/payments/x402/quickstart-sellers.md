# Quickstart for Sellers

This guide walks you through integrating with x402 
to enable payments for your API or service. By the end, 
your API will be able to charge buyers and AI agents for access.

## Prerequisites

Before you begin, ensure you have:

* A crypto wallet to receive funds (any EVM-compatible wallet)
* [Node.js](https://nodejs.org/en) and npm (or Python and pip) installed
* An existing API or server

**Note**\
There are pre-configured examples available in the Coinbase repo for both
 [Node.js](https://github.com/coinbase/x402/tree/main/examples/typescript/servers). We also have an [advanced example](https://github.com/coinbase/x402/tree/main/examples/typescript/servers/advanced) 
 that shows how to use the x402 SDKs to build a more complex payment flow.
The following example shows how to adapt these for Polygon.

## 1. Install Dependencies

Install the [x402 Express middleware package](https://www.npmjs.com/package/x402-express).

```bash
npm install x402-express
npm install @coinbase/x402 # for the mainnet facilitator
```

Install the [x402 Next.js middleware package](https://www.npmjs.com/package/x402-next).

```bash
npm install x402-next
```

Install the [x402 Hono middleware package](https://www.npmjs.com/package/x402-hono).

```bash
npm install x402-hono
```

This [community package](https://github.com/ethanniser/x402-mcp) showcases how you can use MCP (Model Context Protocol) with x402. We're working on enshrining an official MCP spec in x402 soon.

```bash
npm install x402-mcp
```

Full example in the repo [here](https://github.com/ethanniser/x402-mcp/tree/main/apps/example).


### 2. Add Payment Middleware

Integrate the payment middleware into your application. You will need 
to provide:

* The Facilitator URL or facilitator object. For testing, 
use `https://x402.org/facilitator` which works on Base Sepolia.
* For more information on running in production on mainnet, check 
out [CDP's Quickstart for Sellers](https://docs.cdp.coinbase.com/x402/docs/
quickstart-sellers)
* The routes you want to protect.
* Your receiving wallet address.


Full example in the repo [here](https://github.com/coinbase/x402/tree/main/examples/typescript/servers/express). 
Please adapt for Polygon.


```javascript
import express from "express";
import { paymentMiddleware, Network } from "x402-express";

const app = express();

app.use(paymentMiddleware(
  "0xYourAddress", // your receiving wallet address 
  {  // Route configurations for protected endpoints
      "GET /weather": {
        // USDC amount in dollars
        price: "$0.001",
        network: "polygon-amoy",
      },
    },
  {
    url: "https://facilitator.x402.rs/", // Facilitator URL for Polygon Amoy testnet. 
  }
));

// Implement your route
app.get("/weather", (req, res) => {
  res.send({
    report: {
      weather: "sunny",
      temperature: 70,
    },
  });
});

app.listen(4021, () => {
  console.log(`Server listening at http://localhost:4021`);
});
```

Full example in the repo [here](https://github.com/coinbase/x402/tree/main/examples/typescript/fullstack/next). 
Since this is a fullstack example, we recommend using the example to build
this yourself, and treat the code snippet below as a reference to adapt for
Polygon.

```javascript
import { paymentMiddleware, Network } from 'x402-next';

// Configure the payment middleware
export const middleware = paymentMiddleware(
  "0xYourAddress", // your receiving wallet address 
  {  // Route configurations for protected endpoints
    '/protected': {
      price: '$0.01',
      network: "base-sepolia",
      config: {
        description: 'Access to protected content'
      }
    },
  }
  {
    url: "https://facilitator.x402.rs/", // Facilitator URL for Polygon testnet and mainnet
  }
);

// Configure which paths the middleware should run on
export const config = {
  matcher: [
    '/protected/:path*',
  ]
};
```

Full example in the repo [here](https://github.com/coinbase/x402/tree/main/examples/typescript/servers/express).

```javascript
import { Hono } from "hono";
import { paymentMiddleware, Network } from "x402-hono";

const app = new Hono();

// Configure the payment middleware
app.use(paymentMiddleware(
  "0xYourAddress",
  {
    "/protected-route": {
      price: "$0.01",
      network: "polygon-amoy",
      config: {
        description: "Access to premium content",
      }
    }
  },
  {
    url: 'https://facilitator.x402.rs' // 👈 Facilitator URL
  }
));

// Implement your route
app.get("/protected-route", (c) => {
  return c.json({ message: "This content is behind a paywall" });
});

serve({
  fetch: app.fetch,
  port: 3000
});
```