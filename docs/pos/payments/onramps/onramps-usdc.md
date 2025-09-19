# USDC

## Prerequisites

	* Use (Circle’s sandbox environment)[https://app-sandbox.circle.com/signin] for development and testing. Production requires a separate API key and account setup.  ￼ 
	* Authenticate HTTP requests via (the Authorization: Bearer YOUR_API_KEY header.)[https://developers.circle.com/circle-mint/getting-started-with-the-circle-apis?utm_source=chatgpt.com#api-key-authentication]
	* [Circle SDK](https://developers.circle.com/circle-mint/circle-sdks)
!!! info 
    Keep your API key secure! Never expose it in client-side code.  ￼

## Minting USDC

```js
import { Circle, CircleEnvironments } from '@circle-fin/circle-sdk';

const circle = new Circle(
  process.env.CIRCLE_API_KEY || '', 
  CircleEnvironments.sandbox
);

async function mintUSDC() {
  const res = await circle.paymentIntents.createPaymentIntent({
    idempotencyKey: 'unique-key-12345',
    amount: { amount: '100.00', currency: 'USD' },
    settlementCurrency: 'USD',
    paymentMethods: [
      { chain: 'POLY', type: 'blockchain' }
    ],
  });

  console.log(res);
}

mintUSDC().catch(console.error);
```

## 
