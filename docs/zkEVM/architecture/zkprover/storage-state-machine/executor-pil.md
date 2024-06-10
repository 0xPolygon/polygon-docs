The Storage executor is to the Storage Assembly code a like a slave-worker to the master. It carries out all _Storage Actions_ in accordance with rules and logic the Assembly code has set out.

As per instruction of the Main SM, the Storage executor makes function calls to the Storage ROM for a specific secondary Assembly code, stored as a JSON-file, by using the same aforementioned _selectors_ of secondary Assembly codes.

For example, if the Main SM requires a new leaf to be created at a found non-zero leaf, the Storage executor uses _isSetInsertFound_ as a function call for the _Set_InsertFound_ (or _SIF_) Storage Action. The Storage executor then proceeds to build committed polynomials and executes the _SIF_ Storage Action.

As previously observed, in our very first UPDATE example in this series of documents, all values are expressed as quadruplets of unsigned integers. For example, the _Remaining Key_ looks like this,

$$
\texttt{RKey} = \big( \texttt{RKey}_0, \texttt{RKey}_1, \texttt{RKey}_2, \texttt{RKey}_3 \big)
$$

The executor therefore uses an internal 4-element register called _op = [_,_,_,_]_, for handling values from the Storage ROM, which are needed in the internal step-by-step evaluations of the Storage Action being executed. It is thus reset to 0 after every evaluation.

All the function calls seen in the Assembly code:

$\texttt{GetSibling()}$, $\texttt{GetValueLow()}$, $\texttt{GetValueHigh()}$, $\texttt{GetRKey()}$, $\texttt{GetSiblingRKey()}$, $\texttt{GetSiblingHash()}$, $\texttt{GetSiblingValueLow()}$, $\texttt{GetSiblingValueHigh()}$, $\texttt{GetOldValueLow()}$, $\texttt{GetOldValueHigh()}$, $\texttt{GetLevelBit()}$, $\texttt{GetTopTree()}$, $\texttt{GetTopBranch()}$, and $\texttt{GetNextKeyBit()}$,

are actually performed by the Storage executor. The values being fetched are carried with the _op_ register. For instance, if the function call is _GetRKey()_ then the Storage executor gets the RKey from the rom.line file, carries it with _op_ as;

$$
\begin{aligned}
\texttt{op[0] = ctx.rkey[0]}; \\
\texttt{op[1] = ctx.rkey[1]}; \\
\texttt{op[2] = ctx.rkey[2]}; \\
\texttt{op[3] = ctx.rkey[3]};
\end{aligned}
$$

where _ctx_ signifies a _Storage Action_.

Also, since all _Storage Actions_ require some hashing, the Storage SM delegates all hashing actions to the Poseidon SM. However, from within the Storage SM, it is best to treat the Poseidon SM as a blackbox. The Storage executor simply specifies the sets of twelve values to be digested. And the Poseidon SM then returns the required digests of the values.

## Storage PIL

All computations executed in the Storage SM must be verifiable. A special _Polynomial identity language_ (PIL) code is therefore used to set up all the polynomial constraints the verifier needs so as to validate correctness of execution.

The preparation for these polynomial constraints actually starts in the Storage executor. In order to accomplish this, the Storage executor uses; selectors, setters and instructions; which are in fact Boolean polynomials. See the list of these Boolean committed polynomials in the table below.

<center>

| Selectors              | Setters                | Instructions      |
| :--------------------- | :--------------------- | :---------------- |
| selFree[i]             | setHashLeft[i]         | iHash             |
| selSiblingValueHash[i] | setHashRight[i]        | iHashType         |
| selOldRoot[i]          | setOldRoot[i]          | iLatchSet         |
| selNewRoot[i]          | setNewRoot[i]          | iLatchGet         |
| selValueLow[i]         | setValueLow[i]         | iClimbRkey        |
| selValueHigh[i]        | setValueHigh[i]        | iClimbSiblingRkey |
| selRkeyBit[i]          | setSiblingValueLow[i]  | iClimbSiblngRkeyN |
| selSiblingRkey[i]      | setSiblingValueHigh[i] | iRotateLevel      |
| selRkey[i]             | setRkey[i]             | iJmpz             |
|                        | setSiblingRkey[i]      | iConst0           |
|                        | setRkeyBit[i]          | iConst1           |
|                        | setLevel[i]            | iConst2           |
|                        |                        | iConst3           |
|                        |                        | iAddress          |

</center>  

Every time each of these Boolean polynomials are utilised or performed, a record of a "1" is kept in its register. This is called an _Execution trace_.

Therefore, instead of performing some expensive computations in order to verify correctness of execution (at times repeating the same computations being verified), the trace of execution is tested.

The verifier takes the execution trace, and tests if it satisfies the polynomial constraints (or identities) in the PIL code. This technique helps the zkProver to achieve succintness as a zero-knowledge proof-verification system.

## Poseidon hash

Poseidon SM is more straightforward once one understands the internal mechanism of the original Poseidon hash function. The hash function's permutation process translates readily to the Poseidon SM states.

The Poseidon State Machine carries out _Poseidon Actions_ in accordance with instructions from the Main SM executor and requests from the Storage SM. That is, it computes hashes of messages sent from any of the two SMs, and also checks if the hashes were correctly computed.

The zkProver uses Poseidon hash function defined over the Goldilocks field, denoted by $\mathbb{F}_p$, where $p = 2^{64} - 2^{32} + 1$.

The states of the Poseidon SM coincide with the twelve (12) internal states of the $\text{Poseidon}^{\pi}$ permutation function. These are; _in0_, _in1_, ... , _in7_, _hashType_, _cap1_, _cap2_ and _cap3_.

$\text{Poseidon}^{\pi}$ runs 30 rounds, 3 times. Adding up to a total of 90 rounds. It outputs four (4) hash values; _hash0_, _hash1_, _hash2_ and _hash3_.

![Poseidon HASH0 ](../../../../img/zkEVM/fig16-posdn-eg.png)

In the case of the zkProver storage, two slightly different Poseidon hashes are used; $\text{HASH0}$ is used when a branch node is created, whilst $\text{HASH1}$ is used when a leaf node is created. This depends on the _hashType_, which is a boolean. So Poseidon acts as $\text{HASH1}$ when _hashType_ = 1, and $\text{HASH0}$ when _hashType_ = 0.

Since the Poseidon hash outputs $4 * \lfloor(63.99)\rfloor \text{ bits} = 252$, and one bit is needed to encode each direction. The tree can therefore have a maximum of 252 levels.
