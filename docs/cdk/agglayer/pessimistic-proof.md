## Overview
Pessimistic Proof is a Rust-based project for the AggLayer, focusing on performance-optimized proof generation using AVX512 instructions. It leverages Zero-Knowledge Proof (ZKP) technology for secure computations in Web3 applications.

## Get Started

### Prerequisites
- Rust installed
- AVX512 enabled CPU

### Installation
Clone the repository:
```sh
git clone https://github.com/AggLayer/pessimistic-proof.git
cd pessimistic-proof
```

### Running the Project
```sh
RUST_LOG=info RUSTFLAGS='-C target-cpu=native -C target_feature=+avx512ifma,+avx512vl --cfg curve25519_dalek_backend="simd"' cargo run --release
```

## How To's

### How to Compile
Ensure you have the required Rust version and run:
```sh
cargo build --release
```

### How to Run Tests
Run the following command to execute tests:
```sh
cargo test
```

## Architectural Information

### Directory Structure
- `pessimistic_proof/`: Core library for proof generation.
- `program/`: Contains the main program logic.
- `script/`: Helper scripts.

### Core Components
- **Proof Generation**: Utilizes curve25519_dalek for cryptographic operations.
- **SIMD Optimization**: Employs SIMD (Single Instruction, Multiple Data) for performance improvements using AVX512.

## API Reference

### Key Functions
- **generate_proof**: Generates a proof for given inputs.
```rust
fn generate_proof(input: &Input) -> Proof
```
- **verify_proof**: Verifies the generated proof.
```rust
fn verify_proof(proof: &Proof) -> bool
```

### Data Structures
- **Input**: Represents the input data structure for proof generation.
- **Proof**: Represents the generated proof structure.

---

For more details, visit the [GitHub repository](https://github.com/AggLayer/pessimistic-proof).