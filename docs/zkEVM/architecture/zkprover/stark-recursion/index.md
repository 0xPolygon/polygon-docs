The Polygon zkEVM's rollup strategy is to develop a zero-knowledge Prover (zkProver) that takes a batch of many transactions, proves their validity, and publishes a minimally-sized validity proof for verification.

This document provides details of how such a validity proof is created. It is a process that involves collating a number of proofs into one, using three methods; recursion, aggregation, and composition.

## Proving approach

zkProver is the main component of Polygon zkEVM and solely responsible for proving execution correctness. Instead of using the arithmetic circuit model, the zkProver follows the state machine model.

The approach therefore is to develop a _state machine_ that allows a prover to create and submit a verifiable proof of knowledge, and anyone can take such a proof to verify it.

The process that leads to achieving such a state machine-based system takes a few steps;

- Modeling the deterministic computation involved as a state machine, described in the form of an _Execution Trace_.
- Stating the equations that fully describe the state transitions of the state machine, called _Arithmetic Constraints_.
- Using established and efficient mathematical methods to define the corresponding polynomials.
- Expressing the previously stated Arithmetic Constraints into their equivalent _Polynomial Identities_.

These Polynomial Identities are equations that can be easily tested in order to verify the Prover's claims.

A _Commitment Scheme_ is required for facilitating the proving and verification. Henceforth, in the zkProver context, a proof/verification scheme called _PIL-STARK_ is used. Check out the documentation [here](../../../concepts/mfibonacci/commitment-scheme.md) for the Polygon zkEVM's commitment scheme setting.

## Overall process

In a nutshell, a state machine's execution trace is expressed in PIL, and this expression is called the _PIL Specification_ of the computation represented by the state machine.

In the non-recursive case, a PIL specification is transformed into a verifiable _STARK_ proof by using PIL-STARK.

Subsequently, CIRCOM takes the above _STARK_ proof as an input and generates an _Arithmetic circuit_ and its corresponding _witness_.

The Arithmetic circuit is expressed in terms of its equivalent _Rank-1 Constraint System (R1CS)_, while the _witness_ is actually a set of input, intermediate and output values of the circuit wires, satisfying the R1CS.

Finally, _Rapid SNARK_ takes the above Witness together with the _STARK Verifier data_ and generates a _SNARK_ proof corresponding to the previous _STARK_ proof.

The _SNARK_ proof gets published as the validity proof of the original computation.
