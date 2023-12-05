**Polynomial Identity Language (PIL)** is a domain-specific language (DSL) created to provide developers with a holistic framework for constructing programs through an easy-to-use interface, and abstracting the complexity of proof/verification mechanisms. In the zkEVM context, PIL is the very DNA of verification.

One of the main peculiarities of PIL is its modularity, which allows programmers to define parametrizable programs called `namespaces`. Developers can therefore create their own custom namespaces and instantiate them from larger programs or some public library.

The advantage of building modular programs makes for easy testing, reviewing, auditing, and formally verifying even larger and complex programs. Some of the keys features of PIL are:

- Providing `namespaces` for naming the essential parts that constitute programs
- Denoting whether the polynomials are `committed` or `constant`
- Expressing polynomial relations, including `identities` and `lookup arguments`
- Specifying the type of a polynomial, such as `bool` or `u32`

## Computational model

Many other domain-specific languages (DSL) or toolstacks, such as [Circom](https://docs.circom.io/) or [Halo2](https://zcash.github.io/halo2/), focus on the abstraction of a particular computational model, such as an arithmetic circuit.

However, recent proof systems such as STARKs have shown that arithmetic circuits might not be the best computational models for all use cases. For example, given a complete programming language, computing a valid proof for a circuit satisfiability problem may result in long proving times due to the overhead of re-used logic.

By opting for deployment of programs with their low-level programming, shorter proving times are attainable, especially with the advent of proof/verification-aiding languages such as PIL. Hence the decision to adopt state machines as the best computational model for the Polygon zkEVM.
