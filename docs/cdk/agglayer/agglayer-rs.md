## Overview

AggLayer is a Rust-based web service designed to enhance interoperability among heterogeneous blockchain networks by securely handling zero-knowledge proofs. 

The service verifies the soundness of proofs from various CDK chains before forwarding them to L1 for verification.

It replaces the previous [Golang implementation](agglayer-go.md)

## Architecture

### Components

1. Aggregator: Receives and verifies zk-proofs.

2. Verifier: Confirms the soundness of proofs before submitting them to L1.

### Data flow

1. Input: Proofs from various CDK chains.
2. Processing: Verification of proofs.
3. Output: Verified proofs sent to L1.

## Getting started

### Prerequisites

#### Hardware 

- RPC nodes: Configure RPC nodes for each CDK chain, and synced with the target CDK, to check the state roots post L2 batch executions.

#### Software

- Rust

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/AggLayer/agglayer-rs.git
   cd agglayer-rs
   ```

2. Build and run:

   ```sh
   cargo build
   cargo run
   ```

## How to

### Configure the service

Edit configuration by modifying the `agglayer.toml` file for service settings like RPC endpoints and network parameters. For example:

```toml
[network]
rpc_url = "https://your_rpc_url"
chain_id = "your_chain_id"
```

### Run tests

1. Run unit tests:

   ```sh
   cargo test
   ```

2. Run integration tests by first ensuring all necessary services are running, then execute:

   ```sh
   cargo test -- --ignored
   ```

## API reference

### Endpoints

1. **Submit proof**:
   - **Endpoint**: `/submit_zkp`
   - **Method**: POST
   - **Payload**: 

     ```json
     {
       "zkp": "base64_encoded_zkp",
       "chain_id": "cdk_chain_id"
     }
     ```
   - **Response**:

     ```json
     {
       "status": "success",
       "message": "ZKP submitted successfully"
     }
     ```

---

For more information, visit the [AggLayer Rust repository](https://github.com/AggLayer/agglayer-rs).