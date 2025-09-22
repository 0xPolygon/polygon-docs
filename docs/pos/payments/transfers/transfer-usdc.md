!!! info 
    NOTE: Like all of crypto, payments require handling sensitive data. The following examples are demonstrations of integrations but should not be used in production. In production, sensitive information such as API keys, private-key wallets, etc., should be put in a secrets manager or vault.

## USDC 
USDC is a [top stablecoin used for payments on Polygon.](https://defillama.com/stablecoins/Polygon) Cost-efficient transactions on Polygon makes it the default chain for USDC payments, especially micro or high-volume payments.    

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

Gateway collects USDC balances across any chain with USDC. Users need to send USDC to the Gateway Wallet (not an ERC-20), [more details here.](https://developers.circle.com/gateway#setting-up-a-balance)     

Once the users have a balance, they can send USDC to any chain using the Gateway implementation.

## Prerequisites

The follow example requires a Circle API key, which you can create through [the Circle Developer dashboard.](https://console.circle.com/) (You do not need a Cirlce  license to get a sandbox API key).

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