# Stripe
!!! info 
    NOTE: Like all of crypto, payments require handling sensitive data. The following examples are demonstrations of integrations but should not be used in production. In production, sensitive information such as API keys, private-key wallets, etc., should be put in a secrets manager or vault.
    
!!! info Stripe Documentation

    [Full documentation available on Stripe.](https://docs.stripe.com/)

Stripe integration requires a US domicile (excluding Hawaii) and a registration for your business. Once that registration has cleared, the API `Crypto/Onramps_sessions` will be enabled. Below is an example using Stripe's Sandbox environment:

### Prerequisites

* [Stripe API access](https://docs.stripe.com/api)
* [Stripe SDK](https://github.com/stripe/stripe-node)  

### Server

```curl
# SERVER-SIDE ONLY
curl https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_your_secret_key: \
  -d "destination_currency"="usdc" \
  -d "destination_network"="polygon" \
  -d "wallet_addresses[0][type]"="self_custody" \
  -d "wallet_addresses[0][address]"="0xYOUR_POLYGON_ADDRESS"
```

If successful, the server will return `client_secret` in a format similar to this:

```json
{
  "id": "cos_0MYvmj589O8KAxCGp14dTjiw",
  "object": "crypto.onramp_session",
  "client_secret": "cos_0MYvmj589O8KAxCGp14dTjiw_secret_BsxEqQLiYKANcTAoVnJ2ikH5q002b9xzouk",
  "created": 1675794053,
  "livemode": false,
  [...]
  }
}
```

Once you have the `client_secret`, you can pass that to the frontend. (Note: Only pass the `client_secret`, not the `STRIPE_SECRET_KEY`)

### Node server

```js
import Stripe from "stripe";
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function createOnrampSession(req, res) {
  const session = await stripe.crypto.onramps.sessions.create({
    destination_currency: "usdc",
    destination_network: "polygon",
    wallet_addresses: [{
      type: "self_custody",
      address: "0xYOUR_POLYGON_ADDRESS"
    }],
    // optional: customer, email, reference, etc.
  });
  res.json({ client_secret: session.client_secret });
}
```

## Serving to Frontend

`client_secret` can now be served to the frontend:

```html
<script src="https://js.stripe.com/v3/crypto/onramp.js"></script>
<div id="onramp"></div>
<script>
(async () => {
  // Fetch client_secret from your server
  const { client_secret } = await fetch("/api/create-onramp-session").then(r => r.json());

  const onramp = await window.StripeOnramp.init({
    clientSecret: client_secret,
    appearance: { /* optional branding overrides */ },
  });

  onramp.mount("#onramp");
})();
</script>
```