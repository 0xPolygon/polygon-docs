---
comments: true
---

Plonky relates to active research and the development of libraries containing performant cryptographic functions for use in zero-knowledge proof systems.

[Plonky](https://github.com/0xPolygonZero/plonky?tab=readme-ov-file) was Polygon's original implementation of a zk-SNARK computational cryptographic library based on [Plonk](https://eprint.iacr.org/2019/953) with some customizations. The original library was decommissioned in 2021 to be replaced by Plonky2.

## Plonky 2

Plonky2 is a performant Rust library of cryptographic functions that includes a SNARK implementation based on techniques from [Plonk](https://eprint.iacr.org/2019/953) and [FRI](https://drops.dagstuhl.de/storage/00lipics/lipics-vol107-icalp2018/LIPIcs.ICALP.2018.14/LIPIcs.ICALP.2018.14.pdf) as well as tools such as Starky. 

The library has an emphasis on fast recursive techniques.

Polygon's [type 1 prover](../cdk/architecture/type-1-prover/intro-t1-prover.md) system uses the Plonky2 library.

### Examples

The Polygon [Plonky2](https://github.com/0xPolygonZero/plonky2) repo provides some example functions that you can try out:

- [`factorial`](https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/examples/factorial.rs): Proving knowledge of 100 factorial.
- [`fibonacci`](https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/examples/fibonacci.rs): Proving knowledge of the hundredth Fibonacci number.
- [`range_check`](https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/examples/range_check.rs): Proving that a field element is in a given range.
- [`square_root`](https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/examples/square_root.rs): Proving knowledge of the square root of a given field element

!!! tip "More info"
    - Check out the [Plonky2 tutorial](https://polymerlabs.medium.com/a-tutorial-on-writing-zk-proofs-with-plonky2-part-i-be5812f6b798) for more information on the library and how to use it.
    - Check out the [Plonky2 whitepaper](https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/plonky2.pdf).

## Plonky 3

Plonky3 is an ongoing effort to provide a new and enhanced cryptographic library which aims to further improve on the speed and efficiency of recursive zero-knowledge proofs. It contains optimizations for newer CPU specifications.

It implements polynomial IOPs, such as PLONK and STARKS, and commitment schemes such as Brakedown. Check out the [Plonky3 README](https://github.com/Plonky3/Plonky3) for an update on what is included.

Head over to the [Polygon Plonky3 repo](https://github.com/Plonky3/Plonky3) and try it out yourself.

!!! tip "Learn more about Plonky 1, 2, and 3"
    Watch the [Polygon Zero team's introduction to Plonky](https://www.youtube.com/watch?v=v9xZrhAuTio) on YouTube.

</br>