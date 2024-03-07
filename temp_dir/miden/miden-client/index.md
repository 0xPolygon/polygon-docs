# Overview

## Components

The Miden client currently consists of two main components:

1. Miden client library.
2. Miden client CLI.

### Miden client library

This is a Rust library that can be integrated into projects, allowing developers to programmatically interact with the Miden rollup. It provides a set of APIs and functions for executing transactions, generating proofs, and managing interactions with the Miden network.

### Miden client CLI 

The Miden client also includes a command-line interface (CLI) that serves as a wrapper around the library, exposing its basic functionality in a user-friendly manner. It allows users to execute various commands to interact with the Miden rollup, such as submitting transactions, syncing with the network, and managing account data.

## Key features

The Miden client offers a range of functionality for interacting with the Miden rollup.

### Transaction execution

The Miden client facilitates the execution of transactions on the Miden rollup; allowing users to transfer assets, mint new tokens, and perform various other operations.

### Proof generation

The Miden rollup allows for user-generated proofs. This means that the client contains functionality that executes, proves, and submits transactions. These proofs are key to ensuring the validity of transactions on the Miden rollup.

### Interaction with the Miden network

The Miden client enables users to interact with the Miden network; syncing with the latest blockchain data and managing account information.

### Account generation and tracking

The Miden client provides features for generating and tracking accounts within the Miden rollup ecosystem. Users can create accounts and track their changes based on transactions.
