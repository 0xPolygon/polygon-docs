Before using the Miden client, make sure you have a [Rust installation](https://www.rust-lang.org/tools/install). Miden client requires Rust version 1.67 or later.

As mentioned in the overview, the client is comprised of a library and a CLI that exposes its main functionality.

## CLI interface

### Installation

1. Clone the [miden-client repository](https://github.com/0xPolygonMiden/miden-client/).

```sh
git clone https://github.com/0xPolygonMiden/miden-client.git
```

2. Run the client CLI using:

```sh
cargo run
```

Or you can install it on your system. 

The current recommended way of installing and running the client is to utilize the `testing` and `concurrent` features.

```sh
cargo install --features testing,concurrent --path .
```

This installs the `miden-client` binary (at `~/.cargo/bin/miden-client`) and adds it to your `PATH`.

## Features

### `Testing` feature

The `testing` feature allows mainly for faster account creation. When using the the client CLI alongside a locally-running node, **you will need to make sure the node is installed/executed with the `testing` feature as well**, as some validations can fail if flag does not match up both on the client and the node.

### `Concurrent` feature

Additionally, the client supports another feature: The `concurrent` flag enables optimizations that will result in faster transaction execution and proving.

## Building in `release`

When running the client using `cargo run`, it's important to keep in mind that the `release` build will be significantly faster than `debug` for executing and proving transactions, so defaulting to running in `release` is encouraged. Note that when installing with `cargo install`, this is the default build configuration. 