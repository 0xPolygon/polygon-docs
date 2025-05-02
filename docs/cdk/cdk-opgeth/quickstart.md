# Quickstart: Run cdk-opgeth Locally with Kurtosis

Use this guide to deploy a local testnet instance of `cdk-opgeth` using [Kurtosis](https://docs.kurtosis.com/install). It includes a local L1 + L2 environment with Agglayer components and OP Stack infrastructure.

---

## 1. Install Kurtosis

Follow the official installation instructions:

👉 [Kurtosis Installation Docs](https://docs.kurtosis.com/install)

---

## 2. Launch the cdk-opgeth Stack

Run the following command:

```bash
kurtosis run \
    --enclave cdk \
    --args-file https://raw.githubusercontent.com/0xPolygon/kurtosis-cdk/refs/tags/v0.4.0/.github/tests/chains/op-succinct.yml \
    github.com/0xPolygon/kurtosis-cdk@v0.4.0
```

This will:
- Start an L1 devnet (Ethereum-like chain)
- Deploy Agglayer common contracts
- Deploy `op-geth`, `op-node`, and `op-batcher`
- Deploy AggKit and op-succinct infrastructure

📸 Screenshot: Kurtosis services output  
![Kurtosis Services](..docs/img/cdk/cdk-opgeth-quickstart-1.png)

---

## 3. Bridge Funds from L1 to L2

Use `polycli` to bridge assets:

```bash
polycli ulxly bridge asset \
  --bridge-address $(kurtosis service exec cdk contracts-001 'jq -r ".polygonZkEVMBridgeAddress" /opt/zkevm/combined.json') \
  --private-key 0x12d7de8621a77640c9241b2595ba78ce443d05e94090365ab3bb5e19df82c625 \
  --destination-address 0x9175f8176014543492234099F37a385335a017d6 \
  --destination-network 1 \
  --value 1000000000000000000 \
  --rpc-url http://$(kurtosis port print cdk el-1-geth-lighthouse rpc)
```

### Explanation:
- `bridge-address`: Reads from Kurtosis' internal contract JSON
- `private-key`: Wallet used for sending
- `destination-address`: L2 recipient
- `value`: Bridged amount in wei
- `rpc-url`: Dynamically prints RPC port

📸 Screenshot: Bridge command execution  
![Bridge Command](../screenshot-2.png)

📸 Screenshot: Bridge success confirmation  
![Bridge Success](../screenshot-3.png)

---

## 4. Check L2 Balance

Run:

```bash
cast balance --ether \
  --rpc-url $(kurtosis port print cdk op-el-1-op-geth-op-node-001 rpc) \
  0x9175f8176014543492234099F37a385335a017d6
```

📸 Screenshot: L2 Balance Confirmation  
![L2 Balance](../screenshot-4.png)

---

## 5. Send a Transaction on L2 (Inscription)

Use `cast send` to embed a message:

```bash
cast send --rpc-url $(kurtosis port print cdk op-el-1-op-geth-op-node-001 rpc) \
  --private-key 0xfa5f1cc57271a4ccbc5f0becd6bbca6a542973fa2b323d918c5e625fb67bdb20 \
  0x9175f8176014543492234099F37a385335a017d6 $(echo -n 'data:,Hello Agglayer!' | xxd -p)
```

📸 Screenshot: Successful transaction with calldata  
![Transaction Result](../screenshot-5.png)

---

## 6. View the Inscription

Read calldata using:

```bash
cast tx --rpc-url $(kurtosis port print cdk op-el-1-op-geth-op-node-001 rpc) \
  0x2ec6e2097ef85360cdb1fde9d711412c4ce304a79da5afa69ef9abdbebd6757e input | xxd -r -p
```

Expected output:

```
data:,Hello Agglayer!
```