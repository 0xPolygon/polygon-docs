Focusing specifically on the **Proving Phase** of the **Recursion** process; it is a process that starts with proofs of batches (these are sequenced batches of transactions) and culminates in a ready-to-be-published validity proof, which is a SNARK proof.

There are five intermediate stages to achieving this; the **Compression Stage**, the **Normalization Stage**, the **Aggregation Stage**, the **Final Stage** and the **SNARK Stage**.

An overview of the overall process can be seen in the below figure.

![Proving architecture with recursion, aggregation and composition](../../../../img/zkEVM/10prf-rec-proving-arch-outline.png)

## Compression Stage

Recall that the first STARK, in the sequence of Recursive provers seen in the **Proving Phase** subsection of the **Recursion** section, generates a big proof because of its many polynomials, and its attached FRI uses a low blowup factor.

Henceforth, in each proof of batches, a **Compression Stage** is invoked, aiming at reducing the number of polynomials used. This allows the blowup factor to be augmented, and thus reduce the proof size.

A component called the $\mathtt{c12a\ Prover}$ is utilized in this stage which takes a batch proof $\mathtt{{\pi}_{batch}}$ as input and outputs a 'compressed' proof, denoted by $\mathtt{{\pi}_{\texttt{c12a}}}$ in the above figure.

## Normalization Stage

Following the completion of the Compression Stage, is the Normalization Stage.

Each output of the $\mathtt{c12a\ Prover}$ is taken as an input to the $\mathtt{recursive_1}$ $\mathtt{Prover}$ circuit. Outputs of this circuit are referred to as $\mathtt{\pi_{rec1}}$-type proofs.

It is in the next stage, called the **Aggregation Stage**, which is in charge of joining several batch proofs into a single proof which validates each of the single input proofs all at once.

The way to proceed will be to construct a binary tree of proofs, where a pair of proofs is proved one pair at a time.

However, since the aggregation of two proofs requires the constant root of the previous circuits, through a public input coming from the previous circuit, the **Normalization Stage** is basically created for this very purpose. The stage is in charge of transforming the obtained verifier circuit, that validates the $\pi_{\texttt{c12a}}$ proof, into a circuit that makes the constant root public to the next circuit.

This step allows each aggregator verifier and the normalization verifier to be exactly the same, permitting successful aggregation via recursion.

## Aggregation Stage

Once the normalization step has been completed, the next stage is the aggregation of proofs (i.e., normalized proofs).

In this stage, two normalized proofs are joined together by a $\mathtt{recursive_2}$ $\mathtt{Prover}$ component.

In order to achieve this, a circuit capable of aggregating two verifiers is created, call it the $\mathtt{recursive_2\ Prover}$ circuit. Its outputs are proofs of the $\mathtt{\pi_{rec2}}$-type. This $\mathtt{recursive_2\ Prover}$ circuit is repeatedly applied to pairs of proofs until there are no more normalized proofs to be aggregated.

However, as observed in the figure above, the inputs to the $\mathtt{recursive_2}$ $\mathtt{Prover}$ can be proofs of either the $\mathtt{\pi_{rec1}}$-type or the $\mathtt{\pi_{rec2}}$-type.

This allows us to aggregate a pair of $\mathtt{\pi_{rec1}}$-type proofs, or a pair of $\mathtt{\pi_{rec2}}$-type proofs, or even a combination of a $\mathtt{\pi_{rec1}}$-type proof and a $\mathtt{\pi_{rec2}}$-type proof.

## Final Stage

The **Final Stage** is the very last **STARK** step during the recursion process, and it is in charge of verifying a $\mathtt{{\pi}_{rec2}}$ proof over a completely different finite field, the one defined by the $\text{BN}128$ elliptic curve.

More specifically, the hash used in generating the transcript works over the field of the $\text{BN}128$ elliptic curve. Hence, all the challenges (and so, all polynomials) belong to this new field.

The reason for the changing to the $\text{BN}128$ elliptic curve is because a $\texttt{FFLONK}$ SNARK proof, which works over this type of elliptic curves, is to be generated in the next step of the process.

This step is very much similar to the $\mathtt{recursive_2\ Prover}$ circuit. It instantiates a verifier circuit for $\mathtt{{\pi}_{rec2}}$ except that, in this case, $2$ constant roots should be provided (a constant for each of the proofs aggregated in the former step).

## SNARK Stage

The last step of the whole process is called the **SNARK Stage**, and its purpose is to produce a $\texttt{FFLONK}$ proof $\mathtt{{\pi}_{FFLONK}}$ which validates the previous $\mathtt{{\pi}_{recf}}$ proof.

In fact, $\texttt{FFLONK}$ can be replaced with any other SNARKs. One alternative SNARK which was previously used is $\texttt{Groth16}$, which requires a trusted setup for every new circuit.

A SNARK is chosen to replace a STARK with the aim to reduce both verification complexity and proof size. SNARKs, unlike STARK proofs, have constant complexity.

The $\mathtt{{\pi}_{FFLONK}}$ proof gets published on-chain as the validity proof. The verifier smart contract living on the L1 verifies the validity proof.

## Remark on inputs

All the public inputs used throughout the entire recursion procedure get hashed together, and the resulting digest forms the public input to the SNARK circuit.

The set of all public inputs is listed below (see the documents on [zkEVM L2 state management](../../protocol/state-management.md) and [bridge](../../protocol/zkevm-bridge/index.md)):

- `oldStateRoot`
- `oldAccInputHash`
- `oldBatchNum`
- `chainId`
- `midStateRoot`
- `midAccInputHash`
- `midBatchNum`
- `newStateRoot`
- `newAccInputHash`
- `localExitRoot`
- `newBatchNum`
