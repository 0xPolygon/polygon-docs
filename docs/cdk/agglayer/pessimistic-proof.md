## Overview

Pessimistic proof is a Rust-based project for the AggLayer, focusing on performance-optimized proof generation using AVX512 instructions. 

It uses zero-Knowledge proofs for secure computations in web3 applications.

## Get Started

### Prerequisites

- Rust installed
- An AVX512 enabled CPU

### Installation

Clone the repository:

```sh
git clone https://github.com/AggLayer/pessimistic-proof.git
cd pessimistic-proof
```

### Run the project

```sh
RUST_LOG=info RUSTFLAGS='-C target-cpu=native -C target_feature=+avx512ifma,+avx512vl --cfg curve25519_dalek_backend="simd"' cargo run --release
```

## How to

### Compile the code

Ensure you have the required Rust version and run:

```sh
cargo build --release
```

### Run tests

Run the following command to execute tests:

```sh
cargo test
```

## Architecture

### Directory structure

- `pessimistic_proof/`: Core library for proof generation.
- `program/`: Contains the main program logic.
- `script/`: Helper scripts.

### Core components

- Proof generation: Uses `curve25519_dalek` for cryptographic operations.
- SIMD optimization: Employs SIMD (Single Instruction, Multiple Data) for performance improvements using AVX512.

## API Reference

### Data structures

- Input: Represents the input data structure for proof generation.
- Proof: Represents the generated proof structure.

### Key functions

#### `generate_proof` 

Generates a proof for given inputs.

```rust
fn generate_proof(input: &Input) -> Proof
```

#### `verify_proof`

Verifies the generated proof.

```rust
fn verify_proof(proof: &Proof) -> bool
```

---

For more information, visit the [AggLayer pessimistic proof repository](https://github.com/AggLayer/pessimistic-proof).