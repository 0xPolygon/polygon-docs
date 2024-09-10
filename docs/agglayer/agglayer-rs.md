AggLayer-rs is a Rust-based service designed to receive ZK proofs from various CDK chains and verify their validity before sending them to the L1 for final settlement. 

It replaces the previous [Golang implementation](agglayer-go.md).

## Architecture

The AggLayer Rust architecture supports interactions with multiple CDK chains for proof-verification. Its architecture is the same as `agglayer-go`, but without the PostgreSQL database for storage. 

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

#### Submit proof

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