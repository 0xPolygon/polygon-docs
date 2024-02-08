This document shows you how to run the Polygon Type-1 Prover, specifically for proving transactions, but with the option to test full blocks of less than 4M gas, which means it is similar to [`eth-proof`](https://github.com/wborgeaud/eth-proof) but for transaction proofs.

## Quick start

There are two ways to run the prover. The simplest way to get started is to use the `in-memory` runtime of [Paladin](https://github.com/0xPolygonZero/paladin). This requires very little setup, but it's not really suitable for large scale testing. 

The other method for testing the prover is to use an [AMQP](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol) like [RabbitMQ](https://en.wikipedia.org/wiki/RabbitMQ) to distribute the workload over many workers.

!!! info
    It's worth noting that you'll need at least 40GB of physical memory to run the prover.

## Setup

Start by cloning the repo [here](https://github.com/0xPolygonZero/eth-tx-proof/tree/jhilliard/deployment).

Before running the prover, compile the application. 

```bash
env RUSTFLAGS='-C target-cpu=native' cargo build --release
```

You should end up with two binaries in your `target/release` folder. One is called `worker` and the other is `leader`. Typically, we'll install these somewhere in our `$PATH` for convenience.

Once you have the application available, you'll need to create a block [witness](https://nmohnblatt.github.io/zk-jargon-decoder/definitions/witness.html) which essentially serves as the input for the prover. 

Assuming you've deployed the `leader` binary, you should be able to generate a witness like this:

```bash
paladin-leader rpc -u $RPC_URL -t 0x2f0faea6778845b02f9faf84e7e911ef12c287ce7deb924c5925f3626c77906e > 0x2f0faea6778845b02f9faf84e7e911ef12c287ce7deb924c5925f3626c77906e.json
```

You'll need access to an Ethereum RPC in order to run the command. The input argument is a transaction hash and in particular it is the _last_ transaction hash in the block.

Once you've successfully generated a witness, you're ready to start proving either with the `in-memory` runtime or the `amqp` runtime.

### In-memory proving

Running the prover with the `in-memory` setup requires no setup. You can attempt to generate a proof with a command like this:

```bash
env RUST_MIN_STACK=33554432 \
ARITHMETIC_CIRCUIT_SIZE="15..28" \
BYTE_PACKING_CIRCUIT_SIZE="9..28" \
CPU_CIRCUIT_SIZE="12..28" \
KECCAK_CIRCUIT_SIZE="14..28" \
KECCAK_SPONGE_CIRCUIT_SIZE="9..28" \
LOGIC_CIRCUIT_SIZE="12..28" \
MEMORY_CIRCUIT_SIZE="17..30" \
paladin-leader prove \
--runtime in-memory \
--num-workers 1 \
--input-witness 0x2f0faea6778845b02f9faf84e7e911ef12c287ce7deb924c5925f3626c77906e.json
```

The circuit parameters here are meant to be compatible with virtually all Ethereum blocks. This creates a block proof from an input state root of the preceding block. You can adjust the `--num-workers` flag based on the number of available compute resources. 

!!! info "Rule of thumb" 
    You probably want at least 8 cores per worker.

### AMQP proving

Proving in a distributed compute environment depends on an AMQP server. We're not going to cover the setup of RabbitMQ, but assuming you have something like that available you can run a "leader" which
distributes proving tasks to a collection of "workers" which actually do the proving work.

In order to run the workers, use a command like:

```bash
env RUST_MIN_STACK=33554432 \
ARITHMETIC_CIRCUIT_SIZE="15..28" \
BYTE_PACKING_CIRCUIT_SIZE="9..28" \
CPU_CIRCUIT_SIZE="12..28" \
KECCAK_CIRCUIT_SIZE="14..28" \
KECCAK_SPONGE_CIRCUIT_SIZE="9..28" \
LOGIC_CIRCUIT_SIZE="12..28" \
MEMORY_CIRCUIT_SIZE="17..30" \
paladin-worker --runtime amqp --amqp-uri=amqp://localhost:5672
```

This starts the worker and has it await tasks. Depending on your machine's system capacity, you can run several workers on the same operating system. An example [systemd service](https://github.com/0xPolygonZero/eth-tx-proof/blob/jhilliard/deployment/deploy/paladin-worker@.service) is included. Once that service is installed, you can enable up to 16 workers on the same VM like this:

```bash
seq 0 15 | xargs -I xxx systemctl enable paladin-worker@xxx
seq 0 15 | xargs -I xxx systemctl start paladin-worker@xxx
```

Now that you have your pool of paladin workers, you can start proving with a command like this:

```bash
paladin-leader prove \
--runtime amqp \
--amqp-uri=amqp://localhost:5672 \
--input-witness 0x2f0faea6778845b02f9faf84e7e911ef12c287ce7deb924c5925f3626c77906e.json
```

This command runs the same way as the `in-memory` mode except that the leader itself isn't doing the work. The separate worker processes are doing the heavy lifting.
