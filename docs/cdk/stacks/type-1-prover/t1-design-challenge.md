<!--
---
comments: true
---
-->

The EVM wasn't designed with zero-knowledge proving and verification in mind, and this makes the design of an efficient type 1 prover extremely challenging.

Some of the challenges stem from the way the EVM is implemented. Here are some of the discrepancies that occur when deploying the most common zero-knowledge primitives to the EVM.
  
## Word size

The native EVM word size is 256 bits long, whereas the chosen SNARK Plonky2, operates internally over 64-bit field elements.

Matching these word sizes requires a work-around where word operations are performed in multiples of smaller limbs for proper handling internally.

This unfortunately incurs overheads, even for simple operations like the ADD opcode.
  
## Supported fields 

Selecting a field for the most efficient proving scheme can become complicated.

Ethereum transactions are signed over the [secp256k1 curve](https://secg.org/sec2-v2.pdf), which involves a specific prime field $\mathbb{F}_p$, where $p = 2^{256} - 2^{32} - 2^9 - 2^8 -2^7 - 2^6 - 2^4 - 1$. The EVM also supports precompiles for [BN254 curve](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-197.md) operations, where the computations are carried out in an entirely different field arithmetic.

This adds a major overhead when it comes to proving modular arithmetic, as there is a need to deal with modular reductions in the field of the proving system.

Such incongruous modular arithmetic is not uncommon. Recursive proving schemes like [Halo](https://electriccoin.co/wp-content/uploads/2019/09/Halo.pdf) resorted to utilising two pairing-friendly elliptic curves where proving and verification are instantiated in two different field arithmetics.

Other curves, such as the pairing-friendly [BLS12-381](https://eips.ethereum.org/EIPS/eip-2537) popularly used in recursive proving systems, are yet to be EVM-supported in the form of precompiled contracts.
  
## Hash functions

The EVM uses [Keccak](https://keccak.team/keccak_specs_summary.html) as its native hash function both for state representation and arbitrary hashing requests, through the `Keccak256` opcode.

While Keccak is fairly efficient on a CPU, since Plonky2 implements polynomials of degree 3, Keccak operations would need to be expressed as constraints of degree 3. This results in an extremely heavy Algebraic Intermediate Representation (AIR) compared to some of the most recent [STARK-friendly](https://eprint.iacr.org/2020/948.pdf) hash functions, tailored specifically for zero-knowledge proving systems.

Although the EVM supports precompiles of hash functions such as SHA2-256, RIPEMD-160, and Blake2f, they are all quite heavy for a ZK proving system.
  
## State representation 

Ethereum uses Merkle Patricia Tries with RLP encoding. Both of these are not zero-knowledge-friendly primitives, and incur huge overheads on transaction processing within a ZK-EVM context.
  