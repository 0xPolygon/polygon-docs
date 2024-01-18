This document provides a comprehensive list of differences between the EVM and the Polygon zkEVM. The list includes supported EIPs, opcodes, and additional changes made when building the Polygon zkEVM.

### EVM-equivalence

Polygon zkEVM is designed to be EVM-equivalent rather than just compatible.

The difference between EVM-compatibility and EVM-equivalence is that;
   
   - Solutions that are compatible support most of the existing applications, but sometimes with code changes. Additionally, compatibility may lead to breaking developer tooling.

   - Polygon zkEVM strives for EVM-equivalence which means most applications, tools, and infrastructure built on Ethereum can immediately port over to Polygon zkEVM, with limited to no changes needed. Things are designed to work 100% on day one. 

EVM-equivalence is critical to Polygon zkEVM for several reasons, including the following:
   
   1. Development teams don't have to make changes to their code, and this eliminates the possibility of introducing new security vulnerabilities.

   2. No code changes means no need for additional audits. This saves time and money.

   3. Since consolidation of batches and finality of transactions is achieved via smart contracts on Ethereum, Polygon zkEVM benefits from the security of Ethereum.

   4. EVM-equivalence allows Polygon zkEVM to benefit from the already vibrant and active Ethereum community.

   5. It also allows for significant and quick dApp adoption, because applications built on Ethereum are automatically compatible.

Ultimately, Polygon zkEVM offers developers the same UX as on Ethereum, with significantly improved scalability.


!!!info
    No impact on developer experience

    Note that the following differences have no impact on the developer experience with the zkEVM as compared to the EVM. Gas optimization techniques, interacting with libraries like Web3.js and Ethers.js, and deploying contracts work seamlessly on the zkEVM without any overhead.

The following differences have no impact on the developer's experience on the zkEVM compared to the EVM:

   - Gas optimization techniques.
   - Interacting with libraries, like Web3.js and Ethers.js.
   - Deploying contracts seamlessly on the zkEVM without any overhead.


### Opcodes

Below is a list of the changes we have made to opcodes in zkEVM in comparison to the EVM.
   
   - **SELFDESTRUCT** &rarr; removed and replaced by **SENDALL**.

   - `EXTCODEHASH` returns the hash of the contract bytecode from the zkEVM state tree without checking if the account is empty.

   - **DIFFICULTY** &rarr;  returns "0" instead of a random number as in the EVM.

   - **BLOCKHASH** &rarr; returns all previous block hashes instead of just the last 256 blocks.

   > **BLOCKHASH** is the state root at the end of a processable transaction and is stored on the system smart contract.

   - **NUMBER** &rarr; returns the number of processable transactions.


### Precompiled contracts

Among Ethereum's precompiled contracts, the zkEVM currrently supports: **ecRecover** and **identity**.

Other precompiled contracts have no effect on the zkEVM state tree and are treated as reverts, returning all gas to the previous context and setting the `success` flag to "0".


## Additions

**zk-counters** &rarr; batch resources are available, linked to state-machine components, as a supplementary addition to gas computation.


## Other minor differences
   
   - zkEVM doesn't clean storage when a contract is deployed at an address due to the zkEVM state tree specification.

   - `JUMPDEST` is allowed in push bytes to avoid runtime bytecode analysis.

   - The zkEVM implements [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541) from the [London hardfork](https://ethereum.org/en/history/#london).

   - [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) which defines the Typed Transaction Envelope, is not supported

   - [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930), which defines the Optional Access Lists transaction type, is not supported.

   - [`BASEFEE`](https://ethereum-org-fork.netlify.app/en/developers/docs/gas#base-fee) opcode is not supported. The zkEVM implements the Berlin hardfork, but not the London hardfork.
