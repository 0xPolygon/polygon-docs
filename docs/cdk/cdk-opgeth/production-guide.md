# Production Deployment Guide

Welcome! This document provides a comprehensive, step-by-step guide to deploying a **Pessimistic Proofs (PP)** (cdk-opgeth-sovereign) network with support from **Polygon Labs**.

---

## Prerequisites

Before starting, ensure you have:

- A valid L1 RPC URL
- A wallet address with Sepolia testnet funds (deployer)
- [Docker](https://www.docker.com/)
- [Cast](https://book.getfoundry.sh/cast/)
- [Polycli](https://github.com/0xPolygon/polygon-cli)

Export these variables:

```bash
export L1_RPC_URL=https://...
export SEPOLIA_PROVIDER=${L1_RPC_URL}
export DEPLOYER_PRIVATE_KEY=0x0000000000000000000000000000000000000000
```
> 💡 The values shown are specific to this example — be sure to replace them with those relevant to your own setup.

---

## Rollup Network Creation

### Step 1: Submit a Request

To initiate the rollup creation:

1. The **Implementation Provider (IP)** must submit a request to Polygon Labs.
2. Use the [Polygon Support Portal](https://polygon.atlassian.net/servicedesk/customer/portal/22) to raise a support ticket.

#### Required Parameters

| Parameter              | Description                                                | Example                                   |
|------------------------|------------------------------------------------------------|-------------------------------------------|
| Rollup Type            | Type of rollup                                             | `Pessimistic Proofs (PP)`                 |
| Chain ID               | Unique identifier for your rollup                          | `473`                                     |
| Admin Address          | Your control address for rollup modifications              | `0xBe46896822BD1d415522F3a5629Fe28447b95563`                            |
| Sequencer Address      | Used by AggKit, must be under your control                 | `0x0769fcb9ca9369b0494567038E5d1f27f0CBE0aC`                             |
| Gas Token Address      | Token or zero address                                      | `0x0000000000000000000000000000000000000000`                            |
| Sequencer URL          | *(Not used for PP)*                                        | `https://...`                                 |
| Datastream URL         | *(Not used for OP)*                                        | `https://...`                                 |
| Network Name           | Final network name (non-editable)                          | `bali-36-op`                              |

---

### Step 2: Setup by Polygon Labs

Once approved:

- Polygon Labs provisions your Rollup.
- A transaction is recorded (e.g., [example](https://sepolia.etherscan.io/tx/0x111618eedb16b416aef393db6dd2d73d5a190dd5e15bdaa704473ba89a497f92)).

You will receive:

- `combined.json`: Core deployment details
- `genesis-base.json`: Needed for genesis generation

> 💡 **Secure these files.** They are required for further deployment steps.

---

## 🌱 Genesis File Generation

### Option Selection

Choose one:

- **Option 1 (Recommended)**: Merge OP + Polygon Genesis with pre-deployed contracts.
- **Option 2**: Manual L2 contract deployment.

This guide focuses on **Option 1**.

---

### Step-by-Step Instructions

1. **Environment Setup**

Checkout the Desired Version. We will be using`v10.0.0-rc.7` in this example
```bash
git clone https://github.com/0xPolygonHermez/zkevm-contracts.git
cd zkevm-contracts
git checkout v10.0.0-rc.7
```

Install dependencies as described in the repo's [README](https://github.com/0xPolygonHermez/zkevm-contracts).

2. **Parameter File Creation**

```bash
cp ./tools/createSovereignGenesis/create-genesis-sovereign-params.json.example ./tools/createSovereignGenesis/create-genesis-sovereign-params.json
```

Update this file with the relevant information from your `combined.json` and your wallet addresses.

```json
{
   "rollupManagerAddress": "polygonRollupManagerAddress",
   "rollupID": rollupID,
   "chainID": chainID,
   "gasTokenAddress": "gasTokenAddress",
   "bridgeManager": "admin address",
   "sovereignWETHAddress": "0x0000000000000000000000000000000000000000",
   "sovereignWETHAddressIsNotMintable": false,
   "globalExitRootUpdater": "aggoracle address",
   "globalExitRootRemover": "0x0000000000000000000000000000000000000000",
   "emergencyBridgePauser": "admin address",
   "setPreMintAccounts": true,
   "preMintAccounts": [ # add as many as you like
      {
         "balance": "1000000000000000000",
         "address": "admin address"
      }
   ],
   "setTimelockParameters": true,
   "timelockParameters": {
      "adminAddress": "admin address",
      "minDelay": 0 # timelock delay, for devnets it's convinient to set it to zero
   },
   "formatGenesis": "geth"
}
```

3. **Base Genesis Template**

```bash
cp ./tools/createSovereignGenesis/genesis-base.json.example ./tools/createSovereignGenesis/genesis-base.json
```

Paste the contents of your `genesis-base.json` into this file.

4. **Generate Genesis Files**

```bash
npx hardhat run ./tools/createSovereignGenesis/create-sovereign-genesis.ts --network sepolia
```

5. **Rename the Output Files for Clarity**

```bash
mv ./tools/createSovereignGenesis/genesis-rollupID-*.json ./tools/createSovereignGenesis/polygon-genesis.json
mv ./tools/createSovereignGenesis/output-rollupID-*.json ./tools/createSovereignGenesis/polygon-genesis-info.json
```

---

## Network Deployment

### Environment Variables

```bash
export CLAIMTX_ADDRESS=0x0e40237b464f9945FDE774a2582109Aa943b9111
export AGGORACLE_ADDRESS=0x94e8844309E40f4FFa9146a7a890077561f925bc
export CHAIN_ID=473
```

> 💡 The values shown are specific to this example — be sure to replace them with those relevant to your own setup.

### L2 Deployment (Using op-deployer)

To set up your Layer 2 (L2) network using the OP Stack, we recommend starting with the [official Optimism L2 Rollup tutorial](https://docs.optimism.io/operators/chain-operators/tutorials/create-l2-rollup). This guide provides a practical reference based on that tutorial and leverages the [op-deployer](https://docs.optimism.io/operators/chain-operators/tools/op-deployer) tool to streamline the deployment process.

> 💡 All commands in this section are executed from the root directory of your project.

1. **Initialize deployer Folder**

```bash
docker run --rm -v $(pwd)/deployer:/deployer -it us-docker.pkg.dev/oplabs-tools-artifacts/images/op-deployer:v0.0.13 \
	init \
	--l1-chain-id 11155111 \
	--l2-chain-ids "${CHAIN_ID}" \
	--workdir /deployer
```

2. **Edit `intent.toml`** with your parameters.

3. **Deploy L1 Contracts**

```bash
docker run --rm -v $(pwd)/deployer:/deployer -it us-docker.pkg.dev/oplabs-tools-artifacts/images/op-deployer:v0.0.13 \
	apply \
	--workdir /deployer \
	--l1-rpc-url ${L1_RPC_URL} \
	--private-key ${DEPLOYER_PRIVATE_KEY}
```

4. **Merge Genesis Files**


Next, you'll need to combine the `polygon-genesis.json` file with the OP Stack's `genesis.json`. The recommended approach is to embed the contents of `polygon-genesis.json` directly into the op-deployer state.
```bash
# extract the allocs
cat deployer/state.json | jq -r '.opChainDeployments[].allocs' | base64 -d | gzip -d > allocs.json

# merge
jq -s add allocs.json files/polygon-genesis.json | gzip | base64 > merge

# create a copy of the original state
cp deployer/state.json deployer/original-state.json

# replace the original allocs by the merged
cat deployer/state.json | jq ".opChainDeployments[].allocs=\"$( cat merge )\"" > state.json && mv state.json deployer/state.json

# cleanup
rm allocs.json merge
```

5. **Generate Files**

```bash
docker run --rm -v $(pwd)/deployer:/deployer -it us-docker.pkg.dev/oplabs-tools-artifacts/images/op-deployer:v0.0.13 \
   inspect genesis \
   --workdir /deployer "${CHAIN_ID}" > ./deployer/genesis.json

docker run --rm -v $(pwd)/deployer:/deployer -it us-docker.pkg.dev/oplabs-tools-artifacts/images/op-deployer:v0.0.13 \
   inspect rollup \
   --workdir /deployer "${CHAIN_ID}" > ./deployer/rollup.json
```

---

## Component Setup

### OP Stack

1. **Create `.env` values**
```bash
CHAIN_ID=473
SEQUENCER_PRIVATE_KEY=redacted
BATCHER_PRIVATE_KEY=redacted
L1_RPC_URL_HTTP=https://...
L1_RPC_URL_WS=wss://...
```
> 💡 The values shown are specific to this example — be sure to replace them with those relevant to your own setup.

2. **Generate secret**

```bash
openssl rand -hex 32 > deployer/jwt.txt
```

3. **Fund the batcher wallet on L1**

4. **Initialize Data Directory**

```bash
docker run --rm -it \
   -v $(pwd)/deployer/genesis.json:/etc/optimism/genesis.json:ro \
   -v $(pwd)/datadir:/datadir \
   us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101411.3 \
   init \
   --state.scheme=hash \
   --datadir=/datadir \
   /etc/optimism/genesis.json
```

5. **Start Services**

```bash
docker compose up -d op-geth
docker compose up -d op-node
docker compose up -d op-batcher
```

---

### Polygon Components

1. **Config**

Update the `config/aggkit.toml` and `config/bridge.toml` config files with the relevant information from your `combined.json`, `polygon-genesis-info.json` and your wallet addresses.

2. **Create keystore files**

The aggkit and bridge services require the sequencer, aggoracle, and claimtx wallet addresses to be provided through an encrypted keystore.

```bash
mkdir keystore

cast wallet import --private-key ${SEQUENCER_PRIVATE_KEY} --keystore-dir .keystore/ sequencer.keystore
cast wallet import --private-key ${AGGORACLE_PRIVATE_KEY} --keystore-dir .keystore/ aggoracle.keystore
cast wallet import --private-key ${CLAIMTX_PRIVATE_KEY} --keystore-dir .keystore/ claimtx.keystore
```

3. **Fund ClaimTX & Aggoracle**

```bash
cast send \
   --value 100ether \
   --mnemonic "test test test test test test test test test test test junk" \
   --rpc-url http://$(docker compose port op-geth 8545) \
   "${CLAIMTX_ADDRESS}"

cast send \
   --value 10ether \
   --mnemonic "test test test test test test test test test test test junk" \
   --rpc-url http://$(docker compose port op-geth 8545) \
   ${AGGORACLE_ADDRESS}
```

4. **Start PostgreSQL DB**

```bash
docker compose up -d db
```

5. **Run Services**

```bash
docker compose up -d bridge
docker compose up -d aggkit
```

---

## Bridge

### Environment Variables

```bash
export ROLLUP_ID=36
export BRIDGE_ADDRESS=0x1348947e282138d8f377b467f7d9c2eb0f335d1f
export TEST_ADDRESS=0xda9f3DCA867C4Bc7b1f8e2DB47Aa8C338Ba2e056
export TEST_PRIVATE_KEY=redacted
```
> 💡 The values shown are specific to this example — be sure to replace them with those relevant to your own setup.

### L1 to L2

1. **Initiate the Deposit from L1**


Use the following command to bridge assets from L1 to your L2 network:
```bash
polycli ulxly bridge asset \
    --bridge-address ${BRIDGE_ADDRESS} \
    --destination-network ${ROLLUP_ID} \
    --private-key ${TEST_PRIVATE_KEY} \
    --rpc-url ${L1_RPC_URL} \
    --value $(cast to-wei 0.1)
```

2. **Verify the Deposit on L2**


Once the deposit is claimed on L2, you can verify it by checking the balance of the target address:
```bash
cast balance ${TEST_ADDRESS} --ether --rpc-url=http://$(docker compose port op-geth 8545)
```

### L2 to L1

1. **Initiate a Deposit**


Start by making a deposit from L2 using the following command:
```bash
polycli ulxly bridge asset \
    --bridge-address ${BRIDGE_ADDRESS} \
    --destination-network 0 \
    --private-key ${TEST_PRIVATE_KEY} \
    --rpc-url http://$(docker compose port op-geth 8545) \
    --value $(date +%s) \
    --destination-address ${TEST_ADDRESS}
```

2. **Wait for the Pessimistic Proof**


Once the deposit is made, a pessimistic proof will be generated. After this proof is available, the deposit becomes eligible for claiming.

3. **Verify the Deposit Status**


You can check the status of your deposit by querying the bridge service:
```bash
curl -s http://$(docker compose port bridge 8080)/bridges/${TEST_ADDRESS} | jq '.'
{
  "deposits": [
    {
      "leaf_type": 0,
      "orig_net": 0,
      "orig_addr": "0x0000000000000000000000000000000000000000",
      "amount": "1746047601",
      "dest_net": 0,
      "dest_addr": "0xda9f3DCA867C4Bc7b1f8e2DB47Aa8C338Ba2e056",
      "block_num": "14136",
      "deposit_cnt": 0,
      "network_id": 36,
      "tx_hash": "0x4a5d4914e4ae315af941e1fad2b2aac54dfd6c9bc2ca6033e0ea0b325fbcd90e",
      "claim_tx_hash": "",
      "metadata": "0x",
      "ready_for_claim": true,
      "global_index": "150323855360"
    }
  ],
  "total_cnt": "1"
}
```
> ✅ If "ready_for_claim": true, the deposit is ready to be claimed.

4. Claim the Deposit on L1


Run the following command to claim the deposit:
```bash
polycli ulxly claim asset \
    --bridge-address ${BRIDGE_ADDRESS} \
    --bridge-service-url http://$(docker compose port bridge 8080) \
    --deposit-count 0 \
    --destination-address ${TEST_ADDRESS} \
    --deposit-network ${ROLLUP_ID} \
    --private-key ${TEST_PRIVATE_KEY} \
    --rpc-url ${L1_RPC_URL}
```

5. Confirm the Claim

Finally, confirm that the deposit has been successfully claimed by checking the balance of the destination address:
```bash
cast balance ${TEST_ADDRESS} --ether --rpc-url=${L1_RPC_URL}
```

---

### Congratulations! Your PP Network is Live!