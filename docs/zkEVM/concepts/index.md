This section covers some of the basic concepts crucial to understanding the design approach of Polygon zkEVM. Since Polygon zkEVM emulates the EVM, a few EVM basics are herein detailed.

One of the differences between Polygon zkEVM and Ethereum is in the way their states are recorded. Ethereum uses Patricia Merkle tries while Polygon zkEVM uses Sparse Merkle trees (SMTs). The Concepts section therefore discusses how SMTs are constructed and the operations executable on the SMTs. These are Create, Read, Update and Delete, or simply CRUD.

The design approach is delineated in terms of an example: the multiplicative Fibonacci state machine. Further details of the Polygon zkEVM's state machine design are given in the form of a 'Generic state machine', which involves a program written in zkASM called the ROM.

This section also includes a brief discussion on what CIRCOM is, and how it is used in the zkProver.