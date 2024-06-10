The Poseidon state machine is one of the zkProver's 14 state machines. It is a secondary state machine that receives instructions from the Main state machine of the zkProver.

It uses the [Poseidon](https://eprint.iacr.org/2019/458.pdf) hash function to generate hash values in response to requests from the Storage SM and instructions from the Main SM executor. _Poseidon Actions_ are the directives that the Poseidon SM receives from one of the two SMs. It performs the Poseidon Actions as a secondary SM and also verifies that the output hash values were accurately calculated.

The Poseidon state machine therefore consists of an executor component (the Poseidon SM executor) and an internal Poseidon PIL (program), which is a collection of verification rules written in the PIL language. The Poseidon SM executor is written in two languages; Javascript and C/C++.

## Poseidon hash function

The Poseidon Hash, as used in the zkEVM, is defined over the Goldilocks-like field $\mathbb{F}_p$ where the prime $p = 2^{64} - 2^{32} + 1$. It operates on $\mathtt{64}$-bit field elements. The state width of the Poseidon permutation is $8$ field elements, which amounts to $\mathtt{512}$ bits, while the capacity is $\mathtt{4}$ field elements.

As a sponge construction, $\text{POSEIDON}^{\pi}$ has internal states each of  $t$ cells (words), and iterates execution of the _round function_ for as many times as it is regarded safe against round-dependent attacks such as _Differential or Linear Cryptanalytic attacks_.

A typical _round function_ consists of three operations; an addition of a round-key ($ARC$), a non-linear function $S$ (i.e., a substitution box or S-box), and a linear function $L$ which is often an affine transformation (in particular, an MDS matrix $M$).

Some rounds are _partial rounds_ because they use only one S-box instead of the full number of $t$ S-boxes. For the specific construction given in [[GKR+20](https://eprint.iacr.org/2019/458.pdf)], a _full round_ means the round function utilizes $t$ instances of the same S-box. For security purposes against certain cryptanalytic attacks, outer rounds are _full rounds_, while the inner rounds are _partial rounds_.

Denote the number of rounds by $\mathtt{R = R_F + R_P}$ where  $\mathtt{R_F}$  is the number of full rounds and $\mathtt{R_P}$ is the number of partial rounds. Also, let $\mathbf{M}(\cdot)$ denote the linear diffusion layer.

[The figure](https://eprint.iacr.org/2019/458.pdf) below, depicts a HADES-based $\text{POSEIDON}^{\pi}$ permutation.

![POSEIDON Hash](../../../../img/zkEVM/01psd-hades-based-poseidon-perm.png)

The _Poseidon S-box_, $S$, is defined over a finite field as the power map $x\mapsto x^d$, where $d\geq 3$  is chosen as the smallest integer that guarantees invertibility and provides non-linearity.

The commonly used S-box is the cubic, $f(x) = x^3$. However, for fields where the cubic is not bijective, either $f(x) = x^5$ or $f(x) = x^{-1}$ is used as an alternative permutation.

The Poseidon S-box layer used in the zkProver is specified as:

$$
f(x) = x^7.
$$

_Maximum distance separable_ (MDS) matrices are used as the _Linear Diffusion Layer_ in Poseidon, where an MDS matrix $\mathbf{M} \in \mathbb{F}^{t \times t}$ is characterised by the following known result;

$$
\text{A matrix } \mathbf{M} \text{ is an MDS matrix } \text{ iff } \text{ every submatrix of } \mathbf{M} \text{ is non-singular. }
$$

There are various ways to construct an MDS matrix. Some are secure while some are not so secure. However, [algorithms exist](https://eprint.iacr.org/2020/500.pdf) that can be used to test whether a given MDS is secure against certain cryptanalytic attacks, such as _Differential Cryptanalysis Attacks_.

The number of full and partial rounds of the permutation, guaranteed to make Poseidon secure, is specified as follows,

$$
\mathtt{R_F = 8 \text{ (number of full rounds)}, \quad R_P = 22 \text{ (number of partial rounds)}}
$$

Only one squeezing iteration is enforced, with an output of the first $4$ field elements of the state (which consists of approximately $256$-bits, but no more than that).

## Description of the Poseidon SM

Poseidon SM is the most straight forward once one understands the internal mechanism of the original Poseidon hash function. The hash function's permutation process translates readily to the Poseidon SM states.

The Poseidon state machine carries out Poseidon Actions in accordance with instructions from the Main SM executor and requests from the Storage SM. It computes hashes of messages sent from any of the two SMs, and also checks if the hashes were correctly computed.

The zkProver uses the Goldilocks-like Poseidon defined over the field  $\mathbb{F}_p$, where  $p = 2^{64} - 2^{32} + 1$.

The states of the Poseidon SM coincide with the twelve (12) internal states of the $\text{POSEIDON}^{\pi}$ permutation function. These are; _in0_, _in1_, ... , _in7_, _hashType_, _cap1_, _cap2_ and _cap3_.

![POSEIDON Hash ](../../../../img/zkEVM/02psd-poseidon-hash-pic.png)

The parameters of the $\text{POSEIDON}^{\pi}$ permutation are as follows;

- The number of internal states (or cells/words) is $t = 12$. That is, twelve $\mathbb{F}_p$ elements consisting of; the eight (8) input words _in0_, _in1_, ... , _in7_; the hash type _hashType_; and three capacity cells.
- Capacity cells, denoted in the code as _cap1_, _cap2_ and _cap3_. That is, $c = 3$.
- S-box used is the mapping, $f(x) = x^7$.
- It has 8 full rounds. A _full round_ means applying the same S-box on each of the 12 words.
- It has 22 partial rounds. A _partial round_ means the S-box is applied only to the first input word, _in0_.
- The _MDS_ matrix used is a $(t\times t)$ Cauchy matrix, with $2t + 1 \leq p$ and where each $(i,j)$-entry is of the form $\dfrac{1}{x_i + y_i}$, where the two pairwise distinct sets $\{ x_i \}$ and $\{ y_i \}$ are defined as _MCIRC_ and _MDIAG_, respectively. The linear diffusion layer is defined in lines 104 to 116 of the code [sm_poseidon.js](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/src/sm/sm_poseidong.js), and it is explicitly used in lines 99 to 110 of [poseidon.pil](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/pil/poseidong.pil) code.

$\text{POSEIDON}^{\pi}$ runs 30 rounds, 3 times. Adding up to a total of 90 rounds. It outputs four hash values; _hash0_, _hash1_, _hash2_ and _hash3_.

The Poseidon MDS matrix is constructed as shown below.

```js title="sm_poseidong.js"
// definition of the MDS in sm_poseidong.js

const MCIRC = [17n, 15n, 41n, 16n, 2n, 28n, 13n, 13n, 39n, 18n, 34n, 20n];
const MDIAG = [8n, 0n, 0n, 0n, 0n, 0n, 0n, 0n, 0n, 0n, 0n, 0n];

const M = [];
for (let i = 0; i < 12; i++) {
    M[i] = [];
    for (let j = 0; j < 12; j++) {
        M[i][j] = F.e(MCIRC[(-i + j + 12) % 12]);
        if (i === j) M[i][j] = F.add(M[i][j], MDIAG[i]);
    }
}
```

## In a nutshell

Firstly, the Poseidon SM executor translates the Poseidon Actions into the PIL language.

Secondly, it executes the Poseidon Actions (i.e., hashing).

And thirdly, it uses the Poseidon PIL (program) [poseidon.pil](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/pil/poseidong.pil), to check execution correctness of the Poseidon Actions.

### Translation to PIL

It builds the constant polynomials, which are generated once-off at the beginning. These are;

- Three (3) arrays of Add-Round Constants (ARCs), each an array of size 12, denoted by  _C[12]_.
- The _LAST_ constant polynomial, can either be _0_ or _1_. It is used for resetting register values to _0_.
- The _LATCH_ constant polynomial, can either be _0_ or _1_.
- The _LASTBLOCK_ constant polynomial, can either be _0_ or _1_. It is used for resetting hash values.
- The _PARTIAL_ constant polynomial, can either be _0_ or _1_. It is used to set a round to either _PARTIAL_ or _FULL_ round.

### Execution of Poseidon Actions

The main part of the Poseidon SM executor is found in the _lines 138 to 256_ of [sm_poseidong.js](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/src/sm/sm_poseidong.js). This is where it executes Poseidon Actions.

It computes all the committed polynomials;

1. The input words; _in0_, _in1_, ... , _in7_.
2. The type of the hash used and the values representing the capacity; _hashType_, _cap1_, _cap2_ and _cap3_.
3. The four hash values; _hash0_, _hash1_, _hash2_ and _hash3_, which are the outputs of the $\text{POSEIDON}^{\pi}$ permutation.

It also exports all these committed polynomials for verification (checking the hash values _hash0_, _hash1_, _hash2_, and _hash3_), carried out by the [poseidon.pil](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/pil/poseidong.pil) program.

### Poseidon PIL program

The inputs to the Poseidon PIL program are; the constant polynomials and all the committed polynomials.

Here, the input vector (_in0_, _in1_, ... , _in7_, _hashType_, _cap1_, _cap2_, _cap3_) is taken through the various stages of the $\text{POSEIDON}^{\pi}$ permutation;

1. The round constants are added to each element of this input vector.
2. The S-box function is applied to each element (i.e., to the result of the addition of the round constant), where the first four rounds and the last four of the 30 rounds are full rounds, while the other 22 rounds are partial rounds.
3. The MDS matrix is applied to the intermediate vector, whose elements are the results of Step 2 above.
4. The final results are checked against the hash values given as input polynomial commitments; _hash0_, _hash1_, _hash2_, and _hash3_.

## GitHub source

The Polygon zkEVM Repository is available here: [Polygon zkEVM on GitHub](https://github.com/0xPolygonHermez)

Poseidon SM executor: [sm_poseidong.js](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/src/sm/sm_poseidong.js)

Poseidon SM PIL:  [poseidong.pil](https://github.com/0xPolygonHermez/zkevm-proverjs/blob/main/pil/poseidong.pil)

Test vectors: [poseidong_test.js](https://github.com/0xPolygonHermez/zkevm-testvectors/tree/main/test/poseidon)
