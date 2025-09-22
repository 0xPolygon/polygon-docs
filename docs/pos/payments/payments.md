## USDC 
USDC is ranked as the 7th largest cryptocurrency, with a circulation of $65 billion. Nearly 5 million monthly active users engage with USDC on Polygon protocols. Cost-efficient transactions on Polygon makes it the default chain for USDC payments, especially micro or high-volume payments.    

### Integrating USDC
Circle has [excellent documentation,](https://developers.circle.com/) including ready-to-use SDKs and sample applications

For those looking to easily integrate USDC to Polygon, we have two options below: **Native USDC integration** or crosschain USDC using Circle’s **Gateway integration**

### Native USDC integration:

USDC is an ERC-20 contract with the standard `approve`/`transfer` process

```ts
// pnpm add viem
import { createPublicClient, createWalletClient, http, parseUnits } from "viem";
import { polygon } from "viem/chains";
import { privateKeyToAccount } from "viem/accounts";

// Native USDC on Polygon PoS (NOT the old bridged USDC.e)
// Source: Circle "USDC Contract Addresses"
const USDC = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359";

// Testnet USDC on Amoy
// const USDC = "0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582";

const erc20 = [
  { type: "function", name: "decimals", stateMutability: "view", inputs: [], outputs: [{ type: "uint8" }] },
  { type: "function", name: "balanceOf", stateMutability: "view", inputs: [{ type: "address" }], outputs: [{ type: "uint256" }] },
  { type: "function", name: "approve", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
  { type: "function", name: "transfer", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
];

const account = privateKeyToAccount(process.env.PRIV_KEY as `0x${string}`);

const rpc = http(process.env.POLYGON_RPC_URL); // e.g. https://polygon-rpc.com
const pub = createPublicClient({ chain: polygon, transport: rpc });
const wallet = createWalletClient({ chain: polygon, transport: rpc, account });

async function main() {
  const me = account.address as `0x${string}`;
  const decimals = await pub.readContract({ address: USDC, abi: erc20, functionName: "decimals" });
  const bal = await pub.readContract({ address: USDC, abi: erc20, functionName: "balanceOf", args: [me] });
  console.log("USDC balance:", Number(bal) / 10 ** Number(decimals));

  // Transfer 1 USDC
  const amount = parseUnits("1", Number(decimals));
  const hash = await wallet.writeContract({ address: USDC, abi: erc20, functionName: "transfer", args: ["0xRecipient...", amount] });
  console.log("tx:", hash);
}
main();
```

### Gateway integration:

```ts

import { createPublicClient, createWalletClient, http, parseUnits } from "viem";
import { polygon } from "viem/chains";
import { privateKeyToAccount } from "viem/accounts";
import { fetch } from "undici";

const USDC = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359";
const GATEWAY_WALLET = "0x77777777Dcc4d5A8B6E418Fd04D8997ef11000eE";
const GATEWAY_MINTER = "0x2222222d7164433c4C09B0b0D809a9b52C04C205";

const erc20 = [
  { type: "function", name: "decimals", stateMutability: "view", inputs: [], outputs: [{ type: "uint8" }] },
  { type: "function", name: "approve", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
];

const gatewayWalletAbi = [
  { type: "function", name: "deposit", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [] },
];

const gatewayMinterAbi = [
  { type: "function", name: "gatewayMint", stateMutability: "nonpayable", inputs: [{ type: "bytes" }, { type: "bytes" }], outputs: [] },
];

const account = privateKeyToAccount(process.env.PRIV_KEY as `0x${string}`);
const rpc = http(process.env.POLYGON_RPC_URL);
const pub = createPublicClient({ chain: polygon, transport: rpc });
const wallet = createWalletClient({ chain: polygon, transport: rpc, account });

async function gatewayTransfer() {
  // 1) Approve + deposit into GatewayWallet on Polygon
  const decimals = await pub.readContract({ address: USDC, abi: erc20, functionName: "decimals" });
  const amount = parseUnits("25", Number(decimals)); // example

  await wallet.writeContract({ address: USDC, abi: erc20, functionName: "approve", args: [GATEWAY_WALLET, amount] });
  await wallet.writeContract({ address: GATEWAY_WALLET, abi: gatewayWalletAbi, functionName: "deposit", args: [USDC, amount] });

  // 2) Request attestation from Circle Gateway API
  // Build and sign a BurnIntent (EIP-712 typed data) for source=Polygon, destination=Polygon (same-chain "withdraw") or another chain.
  // For brevity, assume you already produced `burnIntent` and EIP-712 signature with your EOA.
  const res = await fetch("https://gateway-api.circle.com/v1/transfer", {
    method: "POST",
    headers: { "content-type": "application/json", authorization: `Bearer ${process.env.CIRCLE_API_KEY}` },
    body: JSON.stringify({
      burnIntent: {
        maxBlockHeight: "999999999999",
        maxFee: "0",
        spec: {
          version: 1,
          sourceDomain: 7,          // Polygon PoS domain id (per Circle docs)
          destinationDomain: 7,     // or another supported domain id
          sourceContract: GATEWAY_WALLET,
          destinationContract: GATEWAY_MINTER,
          sourceToken: USDC,
          destinationToken: USDC,
          sourceDepositor: account.address,
          destinationRecipient: "0xRecipient...", // who receives on destination
          sourceSigner: account.address,
          destinationCaller: "0x0000000000000000000000000000000000000000",
          value: amount.toString(),
        },
      },
      // include your EIP-712 signature of BurnIntent here if required by your flow
    }),
  });
  const { attestationPayload, signature } = await res.json();

  // 3) Submit attestation to GatewayMinter on destination chain
  const tx = await wallet.writeContract({
    address: GATEWAY_MINTER,
    abi: gatewayMinterAbi,
    functionName: "gatewayMint",
    args: [attestationPayload as `0x${string}`, signature as `0x${string}`],
  });
  console.log("gatewayMint tx:", tx);
}

gatewayTransfer();
```

## Tether

USDT makes up over half of the stablecoins on Polygon and has been upgraded from USDT to Polygon-native USDT0, the omnichain deployment of USDT.

### Integrating Tether

Tether is an ERC-20 and follows the common `approve`/`transfer` flow:

```ts
import { createPublicClient, createWalletClient, http, parseUnits } from "viem";
import { polygon } from "viem/chains";
import { privateKeyToAccount } from "viem/accounts";

// Mainnet, No testnet version of USDT
const USDT = "0xc2132d05d31c914a87c6611c10748aeb04b58e8f";
const erc20 = [
  { type: "function", name: "decimals", stateMutability: "view", inputs: [], outputs: [{ type: "uint8" }] },
  { type: "function", name: "balanceOf", stateMutability: "view", inputs: [{ type: "address" }], outputs: [{ type: "uint256" }] },
  { type: "function", name: "approve", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
  { type: "function", name: "transfer", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
];

const account = privateKeyToAccount(process.env.PRIV_KEY as `0x${string}`);
const rpc = http(process.env.POLYGON_RPC_URL);
const pub = createPublicClient({ chain: polygon, transport: rpc });
const wallet = createWalletClient({ chain: polygon, transport: rpc, account });

async function main() {
  const me = account.address as `0x${string}`;
  const decimals = await pub.readContract({ address: USDT, abi: erc20, functionName: "decimals" });
  const bal = await pub.readContract({ address: USDT, abi: erc20, functionName: "balanceOf", args: [me] });
  console.log("USDT balance:", Number(bal) / 10 ** Number(decimals));

  // Transfer 1 USDT
  const amount = parseUnits("1", Number(decimals));
  const hash = await wallet.writeContract({
    address: USDT,
    abi: erc20,
    functionName: "transfer",
    args: ["0xRecipient...", amount],
  });
  console.log("tx:", hash);
}
main();
```

## Stripe



## Bridge

Bridge is a paid enterprise developer platform that joins together fiat and stablecoin rails. The product requires API access. Once granted, you can create virtual accounts, setup transfers, and even establish credit cards for your users.

### Prerequisites

You need an API key and a unique Idempotency-Key 
for each POST which you can get through [the Bridge dashboard.](https://apidocs.bridge.xyz/api-reference/introduction/authentication)

### Create a USD → USDC transfer on Polygon

```curl 
--request POST https://api.bridge.xyz/v0/transfers \
  --header "Api-Key: $BRIDGE_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: $(uuidgen)" \
  --data '{
    "client_reference_id": "order-1234",
    "amount": "25.00",
    "on_behalf_of": "cust_abc123",
    "source": {
      "currency": "usd",
      "payment_rail": "ach"
    },
    "destination": {
      "currency": "usdc",
      "payment_rail": "polygon",
      "to_address": "0xRecipientAddressHere"
    }
  }'
```