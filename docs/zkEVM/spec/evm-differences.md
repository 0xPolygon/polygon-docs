This document provides a comprehensive list of differences between the Ethereum Virtual Machine (EVM) and the Polygon Zero-Knowledge Ethereum Virtual Machine (zkEVM). The list includes supported EIPs, opcodes, and additional changes made to build the zkEVM.

!!!info
    No impact on developer experience

    Note that the following differences have no impact on the developer experience with the zkEVM as compared to the EVM. Gas optimization techniques, interacting with libraries like Web3.js and Ethers.js, and deploying contracts works seamlessly on the zkEVM without any overhead.

## Opcodes

This section lists the changes we have done with Opcodes in zKEVM as compared to the EVM.

- **SELFDESTRUCT** &rarr; removed and replaced by **SENDALL**.

- **EXTCODEHASH** &rarr; returns the hash of the contract bytecode from the zkEVM state tree without checking if the account is empty.

- **DIFFICULTY** &rarr;  returns "0" instead of a random number as in the EVM.

- **BLOCKHASH** &rarr; returns all previous block hashes instead of just the last 256 blocks.

> **BLOCKHASH** is the state root at the end of a processable transaction and is stored on the system smart contract.

- **NUMBER** &rarr; returns the number of processable transactions.

## Precompiled contracts

The following precompiled contracts are supported in the zkEVM:

- [**ecRecover**](https://ethereum.github.io/execution-specs/autoapi/ethereum/frontier/vm/precompiled_contracts/ecrecover/index.html)
- [**identity**](https://ethereum.github.io/execution-specs/autoapi/ethereum/frontier/vm/precompiled_contracts/identity/index.html)

Other precompiled contracts have no effect on the zkEVM state tree and are treated as a `revert`, returning all gas to the previous context and setting the `success` flag to "0".

## Additions

**zk-counters** &rarr; batch resources are available, linked to state-machine components, as a supplementary addition to gas computation.

## Other minor differences

- zkEVM doesn't clean storage when a contract is deployed at an address due to the zkEVM state tree specification.

- **JUMPDEST** opcode is allowed in push bytes to avoid runtime bytecode analysis.

- The zkEVM implements [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541) from the [London hardfork](https://ethereum.org/en/history/#london).

- [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) which defines **Typed Transaction Envelope**, is not supported
- [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930), which defines the **Optional Access Lists** transaction type, is not supported.
