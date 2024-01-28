Polygon Zero's Type-1 zkEVM is designed for efficient implementation of the STARK proving and verification of Ethereum transactions. It achieves efficiency by restricting the Algebraic Intermediate Representation (AIR) to constraints of degree 3.

The execution trace needed to generate a STARK proof can be assimilated to a large matrix, where columns are registers and each row represents a view of the registers at a given time.

From the initial register values on the first row to the final one, validity of each internal state transition is enforced through a set of dedicated constraints. Generating the execution trace for a given transaction unfortunately yields a considerable overhead for the prover.

A naïve design strategy would be to utilize a single table, which is solely dedicated to the entire EVM execution. Such a table would have thousands of columns, and although it would be a highly sparse matrix, the prover would treat it as fully dense.


### Modular design strategy

Since most of the operations involved in the EVM can be independently executed, the execution trace is split into separate STARK modules, where each is responsible for ensuring integrity of its own computations. 

These STARK modules are; 

- **Arithmetic module** handles binary operations including ordinary addition, multiplication, subtraction and division, comparison operations such as 'Less than' and 'Greater than', as well as ternary operations like modular operations. 
- **Keccak module** is responsible for computing a Keccak permutation.
- **KeccakSponge module** is dedicated to the sponge construction's 'absorbing' and 'squeezing' functions.
- **Logic module** specializes in performing bitwise logic operations such as AND, OR, or XOR.
- **Memory module** is responsible for memory operations like reads and writes.
- **BytePacking module** is used for reading and writing non-empty byte sequences of length at most 32 to memory.

Although these smaller STARK modules are different and each has its own set of constraints, they mostly operate on common input values.

In addition to the constraints of each module, this design requires an additional set of constraints in order to enforce that these common input values are not tampered with when shared amongst the various STARK modules.

For this reason, this design utilizes _Cross-table lookups_ (CTLs), based on a [logUp argument](https://eprint.iacr.org/2022/1530.pdf) designed by Ulrich Haböck, to cheaply add copy-constraints in the overall system.

Polygon Zero's Type-1 zkEVM uses a central component dubbed the **CPU** to orchestrate the entire flow of data that occurs among the STARK modules during execution of EVM transactions. The CPU dispatches instructions and inputs to specific STARK modules, as well as fetches their corresponding outputs.

Note here that “dispatching” and “fetching” means that initial values and final values resulting from a given operation are being copied with the CTLs to and from the targeted STARK module.



### Prover primitives

This document discusses the cryptographic primitives used to engineer the Polygon Zero's Type-1 zkEVM, which is a custom-built zkEVM capable of tracing, proving and verifying the execution of the EVM through all state changes.

The proving and verification process is made possible by the zero-knowledge (ZK) technology. In particular, a combination of STARK[^1] and SNARK[^2], proving and verification schemes, respectively.

#### STARK for proving

Polygon Zero's Type-1 zkEVM prover implements a STARK proving scheme, a robust cryptographic technique with fast proving time.

Such a scheme has a proving component, called the STARK prover, and a verifying component called the STARK verifier. A proof produced by the STARK prover is referred to as a STARK proof.

The process begins with constructing a detailed record of all the operations performed when transactions are executed. The record, called the `execution trace`, is then passed to a STARK prover, which in turn generates a STARK proof attesting to correct computation of transactions.

Although STARK proofs are relatively big in size, they are put through a series of recursive SNARK proving, where each SNARK proof is more compact than the previous one. This way the final transaction proof becomes significantly more succinct than the initial one, and hence the verification process is highly accelerated.

Ultimately, this SNARK proof can stand alone or be combined with preceding blocks of proofs, resulting in a single zkEVM validity proof that validates the entire blockchain back from genesis.

#### Plonky2 SNARK for verification

The Polygon Zero's Type-1 prover implements a SNARK called [Plonky2](https://github.com/0xPolygonZero/plonky2), which is a SNARK designed for fast recursive proofs composition. Although its arithmetization is based on [TurboPLONK](https://docs.zkproof.org/pages/standards/accepted-workshop3/proposal-turbo_plonk.pdf), it replaces the polynomial commitment scheme of [PLONK](https://eprint.iacr.org/2019/953) with a scheme based on [FRI](https://drops.dagstuhl.de/storage/00lipics/lipics-vol107-icalp2018/LIPIcs.ICALP.2018.14/LIPIcs.ICALP.2018.14.pdf). This allows encoding the witness in 64-bit words, represented as field elements of a low-characteristic field.

The field used, denoted by $\mathbb{F}_p$ , is called Goldilocks. It is a prime field where the prime $p$ is of the form $p = 2^{64} - 2^{32} + 1$.

Since SNARKs are succinct, a Plonky2 proof is published as the validity proof that attests to the integrity of a number of aggregated STARK proofs. This results in reduced verification costs.

This innovative approach holds the promise of a succinct, verifiable chain state, marking a significant milestone in the quest for blockchain verifiability, scalability, and integrity. It is the very innovation that plays a central role in the Polygon Zero's Type-1 zkEVM.



### Documentation remarks

The documentation of the Polygon Zero's Type-1 zkEVM is still WIP, some of the documents are in the Github repo.

The STARK modules, which are also referred to as **STARK tables**, have been documented in the Github repo [here](https://github.com/0xPolygonZero/plonky2/tree/main/evm/spec/tables). The **CPU component** is documented below, while the **CPU logic** is in the [repo](https://github.com/0xPolygonZero/plonky2/blob/main/evm/spec/cpulogic.tex).

In order to complete the STARK framework, the cross-table lookups (CTLs) and the **CTL protocol** can be found in this document, while **range-checks** are also discussed below.

Details on **Merkle Patricia tries** and how they are used in the Polygon Zero's Type-1 zkEVM, can be found [here](https://github.com/0xPolygonZero/plonky2/blob/main/evm/spec/mpts.tex). Included in there are outlines on the prover's internal memory, data encoding and hashing, and prover input format.



[^1]: STARK is short for Scalable Transparent Argument of Knowledge
[^2]: SNARK is short for Succinct Non-interactive Argument of Knowledge.
