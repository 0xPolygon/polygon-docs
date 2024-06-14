Generating a proof for the valid processing of a single batch requires multiple inputs.

In addition to the data from each transaction in the processed batch, other inputs are necessary to ensure the network's overall security.

For example, some inputs need to be sent to the smart contract.

Central to generation of proofs and their verification are the verifier smart contract and the prover, as well as their interaction.

This document, therefore, explores what the prover transmits to the verifier smart contract and why.

In the zkEVM context, the focus is on generating _succinct_[^1] proofs rather than privacy concerns. 

Consequently, L2 transactions and L2 state data are public. 

We therefore delve into the initial design of the proving system, which operates without private inputs.

## Public inputs

Recall that the prover generates a proof, and sends the proof and an array of public inputs, denoted by $\texttt{[publics]}$ to the smart contract. The figure below depicts this.

![Figure: _ ](../../../img/zkEVM/psi-prover-sends-to-verif-sc.png)

The public inputs consist of the following data:

- `batchData` which is the data of all the L2 transactions in the batch being proved.

- `currentStateRoot` referring to the current L2 state root.

- `proverAccount` which is the prover's account due to receive rewards. This account is attached to the proof so as to avoid successful plagiariasm of the proof.

- `timestamp` specifies the time at which the proof was generated.

- `forkId` is the current version of the L2 EVM being used.

- `chainId` is the identifier of the chain for which the proof is being generated. The protocol is designed with the capability to host multiple layer 2 networks.

The public output of this process is a new L2 state root, denoted by `newStateRoot`.

The prover does not send all these public inputs to the L1 smart contract. Some inputs are already stored in the contract. These include: `currentStateRoot`, `forkId`, and `chainId`.

The rest of the inputs need to be included in the `calldata` of the transaction sent to the L1’s smart contract. That is, `batchData`, `timestamp`, `newStateRoot`.

Since the `proverAccount` is included in the L1 transaction’s signature, it need not be explicitly provided.

Finally, the prover also sends the proof of correct execution of all L2 transactions within the batch.


[^1]: The term [_succinct_](https://www.di.ens.fr/~nitulesc/files/Survey-SNARKs.pdf) refers to the size of the proof being very small compared to the size of the statement or the witness (i.e., the size of the computation itself).
