<!--
---
comments: true
---
-->

This document shows you how to deploy a [docker-compose file](https://github.com/0xPolygonZero/eth-pos-devnet-provable/blob/959da56673c25c2094b1a23bc9e1fa9ae9a9db6e/docker-compose.yml) for running a fully-functional, local development network (devnet) for Ethereum with proof-of-stake enabled.

The configuration uses [Prysm](https://github.com/prysmaticlabs/prysm) as a consensus client, with either [geth](https://github.com/ethereum/go-ethereum) or [erigon](https://github.com/ledgerwatch/erigon) as an execution client.

<!-- **It starts from proof-of-stake** and does not go through the Ethereum merge. -->

The setup is a single node devnet with 64 deterministically-generated validators[^1] to drive the creation of blocks in an Ethereum proof-of-stake chain.

The devnet is fully functional and allows for deployment of smart contracts and all features that come with the Prysm consensus client, such as its rich set of APIs for retrieving data from the blockchain.

Running a devnet like this provides the best way to understand Ethereum proof-of-stake under the hood, and gives allowance for devs to tinker with various settings that suit their system design.

## Running the devnet

1. Checkout this [repository](https://github.com/0xPolygonZero/eth-pos-devnet-provable/tree/344fff4ee1032a0b095ab0c8d757e0ede72da156) and install docker. 

2. Run the following command to fire up the devnet containers:

    ``` bash
    docker compose up -d
    ```

    You should see the statuses of the containers as shown below:

    ``` example
    $ docker compose up -d
    [+] Running 7/7
    [+] Running 10/10
    ✔ Container eth-pos-devnet-create-beacon-chain-genesis-1  Exited
    ✔ Container eth-pos-devnet-create-beacon-node-keys-1      Exited
    ✔ Container eth-pos-devnet-beacon-chain-2-1               Started
    ✔ Container eth-pos-devnet-beacon-chain-1-1               Started
    ✔ Container eth-pos-devnet-geth-genesis-1                 Exited
    ✔ Container eth-pos-devnet-geth-import-1                  Exited
    ✔ Container eth-pos-devnet-erigon-genesis-1               Started
    ✔ Container eth-pos-devnet-validator-1                    Started
    ✔ Container eth-pos-devnet-erigon-1                       Started
    ✔ Container eth-pos-devnet-geth-1                         Started
    ```

3. Stop the containers with this command: `docker compose stop`.

4. Before each restart, wiping old data with `make clean`.

5. Inspect the logs of launched services with this command:

    ``` bash
    docker logs eth-pos-devnet-geth-1 -f
    ```

## Available features

-   Starts from the Capella Ethereum hard fork.
-   The network launches with a [Validator Deposit Contract](https://github.com/ethereum/consensus-specs/blob/dev/solidity_deposit_contract/deposit_contract.sol) deployed at the address `0x4242424242424242424242424242424242424242`. This can be used to onboard new validators into the network by depositing 32 ETH into the contract.
-   The default account used in the go-ethereum node is at the address `0x85da99c8a7c2c95964c8efd687e95e632fc533d6`, which comes seeded with ETH for use in the network. This can be used to send transactions, deploy contracts, and more.
-   The default account at `0x85da99c8a7c2c95964c8efd687e95e632fc533d6` is also set as the fee recipient for transaction fees proposed by validators in Prysm. This address will be receiving the fees of all proposer activity.
-   The go-ethereum JSON-RPC API is available at `http://geth:8545`.
-   The Prysm client's REST APIs are available at `http://beacon-chain:3500`. For more info on what these APIs are, see [here](https://ethereum.github.io/beacon-APIs/)
-   The Prysm client also exposes a gRPC API at `http://beacon-chain:4000`.

## Type 1 prover testing procedure

The aim of this devnet setup is to use Polygon Type 1 Prover to test Erigon state witnesses.

The following steps create some test data.

1. Start the devnet up with `docker compose up`. If you had previously run this command, you might want to wipe old data with a `make clean` to avoid running from a previous state.
2. Wait for blocks to start being produced. This should only take a few seconds. You can use `polycli monitor` to quickly check that blocks are being created.
3. Generate some load and test transactions, by using a tool like [polycli](https://github.com/0xPolygon/polygon-cli/blob/main/doc/polycli_loadtest.md) to create transactions.
4. Once the load is done, and if you ran docker in detached mode, you can stop the devnet with `docker compose stop`.
5. Checkout and build [jerrigon](https://github.com/0xPolygonZero/erigon/tree/feat/zero) from the `feat/zero` branch. You can use `make all` to build everything.
6. Create a copy of the erigon state directory to avoid corrupting things

    ```bash
    sudo cp -r execution/erigon/ execution/erigon.bak
    sudo chown -R $USER:$USER execution/erigon.bak/
    ```

7. Now we can start the Jerrigon fork of Erigon. This will give us RPC access to the state that we created in the previous steps.

    ```bash
    ~/code/jerrigon/build/bin/erigon \
     --http \
     --http.api=eth,net,web3,erigon,engine,debug \
     --http.addr=0.0.0.0 \
     --http.corsdomain=* \
     --http.vhosts any \
     --ws \
     --nodiscover=true \
     --txpool.disable=true \
     --no-downloader=true \
     --maxpeers 0 \
     --datadir=./execution/erigon.bak
    ```

8. With the RPC running we can retrieve the blocks, witnesses, and use zero-bin to parse them. 
    In one particular test case below, about 240 blocks worth of data were generated.
    So, `seq 0 240` was used for generating ranges of block numbers for testing purposes.

    ``` bash
    # Create a directory for storing the outputs
    mkdir out

    # Call the zeroTracer to get the traces
    seq 0 240 | awk '{print "curl -o " sprintf("out/wit_%02d", $0) ".json -H '"'"'Content-Type: application/json'"'"' -d '"'"'{\"method\":\"debug_traceBlockByNumber\",\"params\":[\"" sprintf("0x%X", $0) "\", {\"tracer\": \"zeroTracer\"}],\"id\":1,\"jsonrpc\":\"2.0\"}'"'"' http://127.0.0.1:8545"}' | bash

    # download the blocks (this assumes you have foundry/cast installed)
    seq 0 240 | awk '{print "cast block --full -j " $0 " > out/block_" sprintf("%02d", $0) ".json"}' | bash
    ```

9. At this point, we'll want to checkout and build [zero-bin](https://github.com/0xPolygonZero/zero-bin) in order to test proof generation.
    Make sure to checkout that repo and run `cargo build --release` to compile the application for testing.

    The snippets below assume [zero-bin](https://github.com/0xPolygonZero/zero-bin) has been checked out and compiled in `$HOME/code/zero-bin`.

    After compiling, the `leader` and `rpc` binaries will be created in the `target/release` folder.

    ``` bash
    # use zero-bin to convert witness formats. This is a basic test
    seq 0 240 | awk '{print "~/code/zero-bin/target/release/rpc fetch --rpc-url http://127.0.0.1:8545 --block-number " $0 " > " sprintf("out/zero_%02d", $0) ".json" }' | bash

    # use zero-bin to generate a proof for the genesis block
    ./leader --arithmetic 16..23 --byte-packing 9..21 --cpu 12..25 --keccak 14..20 --keccak-sponge 9..15 --logic 12..18 --memory 17..28 --runtime in-memory -n 1 jerigon --rpc-url http://127.0.0.1:8545 --block-number 1 --proof-output-path 1.json 
    seq 2 240 | awk '{print "./leader --arithmetic 16..23 --byte-packing 9..21 --cpu 12..25 --keccak 14..20 --keccak-sponge 9..15 --logic 12..18 --memory 17..28  --runtime in-memory -n 4 jerigon --rpc-url http://127.0.0.1:8545 --block-number " $1 " --proof-output-path " $1 ".json --previous-proof " ($1 - 1) ".json"}'
    ```

### Operational notes

- Pay attention to memory usage on the system running `zero-bin`. Certain transactions can consume a lot of memory and lead to an out-of-memory (OOM) error.
- You'll want to run `zero-bin` on a system with at least 32GB of RAM.
- When you run `zero-bin`, a local file will be created with a name like `prover_state_*`. This file needs to be deleted if any of the [circuit sizes are changed](https://github.com/0xPolygonZero/zero-bin#leader-usage).
- There is a [useful script](https://github.com/0xPolygonZero/zero-bin/blob/assorted_fixes/tools/prove_blocks.sh) in `zero-bin` to run a range of proofs.

!!! important
    Both the state witness generation and decoding logic are actively being improved. 

We expect that the following transaction types or use-cases to prove without any issues:

- Empty blocks (important use case)
- EOA transfers
- ERC-20 mints & transfers
- ERC-721 mintes & transfers

### Shortcuts

1. There is a shortcut that creates the genesis file allocations for our mnemonic which has already been hard-coded into the genesis file. However, if you want to use a different testing account, use the one below.

    ``` bash
    polycli wallet inspect --mnemonic "code code code code code code code code code code code quality" | jq '.Addresses[] | {"key": .ETHAddress, "value": { "balance": "0x21e19e0c9bab2400000"}}' | jq -s 'from_entries'
    ```

[^1]: See Line# 11 of the docker-compose.yml https://github.com/0xPolygonZero/eth-pos-devnet-provable/blob/959da56673c25c2094b1a23bc9e1fa9ae9a9db6e/docker-compose.yml#L11 
