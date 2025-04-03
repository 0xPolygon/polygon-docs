<!--
---
comments: true
---
-->

Tables often deal with 256-bit words which are split into 16-bit limbs. This helps to avoid field overflows. Range-checks are used for examining integrity of values in these 16-bit limbs. 

### What to range-check?

The idea here is to range-check every field element pushed into the Stack, as well as every memory writes. That is, Range-checking the PUSH and MSTORE opcodes.

Other range-checks are:
  
  - Pushes and memory writes for `MSTORE_32BYTES`, range-checked in the "BytePackingStark".
  - Syscalls, exceptions and prover inputs are range-checked in "ArithmeticStark".
  - Inputs and outputs of binary and ternary arithmetic operations are range-checked in "ArithmeticStark".
  - Inputs' bits of logic operations are checked to be either $1$ or $0$ in "LogicStark". Since “LogicStark” only deals with bitwise operations, it is sufficient to range-check outputs.
  - Inputs to Keccak operations are range-checked in “KeccakStark”. The output digest is written as bytes in “KeccakStark”. Those bytes are used to reconstruct the associated 32-bit limbs checked against the limbs in “CpuStark”. This implicitly ensures that the output is range-checked.



### What not to range-check

Some operations do not require range-checks, including the following:
  
  - `MSTORE_GENERAL`, which writes values read from Stack. Therefore, the written values were already range-checked by previous pushes.
  - `EQ`, which reads two -- already range-checked -- elements on the Stack, and checks their equality. The output is either 0 or 1, and therefore need not be range-checked.
  - `NOT`, which reads one -- already range-checked -- element. The result is constrained to be equal to $\texttt{0xFFFFFFFF} - \texttt{input}$, which implicitly enforces the range-check.
  - `PC`, the Program Counter, which cannot be greater than $2^{32}$ in user mode. Indeed, the user code cannot be longer than $2^{32}$, and jumps are constrained to be JUMP destinations, JUMPDESTs. Moreover, when in kernel mode, every JUMP's destination is a location within the kernel, and the kernel code is smaller than $2^{32}$. These two points implicitly enforce  range-check on PC's.
  - `GET_CONTEXT`, `DUP`, and `SWAP`, all read and push values that were already written in memory. These pushed values were therefore already range-checked.

Note that range-checks are performed on the range $[0, 2^{16} - 1]$, so as to limit the trace length.



### Lookup argument

Enforcement of range-checks leverages [LogUp](https://eprint.iacr.org/2022/1530.pdf), a lookup argument introduced by Ulrich Häbock. 

Given a `looking table` $s = (s_1, ..., s_n)$ and a `looked table` $t = (t_1, ..., t_m)$, the goal is to prove that

$$
\text{for all}\ 1 \leq i \leq n,\ \text{there exists}\  1 \leq j \leq r\ \text{ such that }\ s_i = t_j
$$

In our case, $t = (0, .., 2^{16} - 1)$ and $s$ is composed of all the columns in each STARK that must be range-checked.

The [LogUp paper](https://eprint.iacr.org/2022/1530.pdf) explains that proving the previous assertion is equivalent to proving that there exists a sequence $\{l_j \}$ such that:

$$
\sum_{i=1}^n \frac{1}{X - s_i} = \sum_{j=1}^r \frac{l_j}{X-t_j} \tag{1}
$$

The values in the `looking table` $s = (s_1, ..., s_n)$, can be stored in columns each  of length $n$. And if these columns are $c$ in number, the above equality becomes:

$$
\sum_{k=1}^c \sum_{i=1}^n \frac{1}{X - s_i^k} = \sum_{j=1}^r \frac{l_j}{X-t_j} \tag{2}
$$

The `multiplicity` $m_i$ of each value $t_i$ is defined as the number of times $t_i$ appears in the `looking table` $s = (s_1, ..., s_n)$. In other words, $m_i$ is the cardinality of a set, given by:

$$
m_i = \big|\{ s_j \in s\ |\ s_j = t_i \} \big|
$$

Multiplicities of the $\{ t_j \}$ form a sequence $\{ m_j \}$  and thus proves existence of the required $\{ l_j \}$ sequence of Equation $1$ above. This means Equation $2$ can be rewritten as:

$$
\sum_{k=1}^c \sum_{i=1}^n \frac{1}{X - s_i^k} = \sum_{j=1}^r \frac{m_j}{X-t_j}
$$

For each random challenge $\alpha$, provided by the verifier, proving the lookup argument amounts to checking this equation:

$$
\sum_{k=1}^c \sum_{i=1}^n \frac{1}{\alpha - s_i^k} = \sum_{j=1}^r \frac{m_j}{\alpha-t_j}
$$

However, this yields a high degree equation.

Häbock suggests circumventing this issue by providing helper columns $\{h_i\}$ and $d$ , such that at any given row $i$:

$$
\begin{aligned}
&h_i^k = \frac{1}{\alpha + s_i^k }\ \text{ for all }\ 1 \leq k \leq c \\
  &d_i = \frac{1}{\alpha + t_i}
  \end{aligned}
$$

The $h$ helper columns can be batched together to save columns. At most $\texttt{constraint\_degree} - 1$ helper functions can be batched together.

In our case, they are batched 2 by 2. For row $i$, we therefore obtain:

$$
h_i^k = \frac{1}{\alpha + s_i^{2k}} + \frac{1}{\alpha + s_i^{2k+1}}\ \text{ for all }\ 1 \leq k \leq c/2
$$

If the number of column $c$ is odd, we have one extra helper column:

$$
h_i^{c/2+1} = \frac{1}{\alpha + s_i^{c}}
$$

We henceforth assume $c$ to be even.

Now, let $g$ be a generator of a subgroup of order $n$. Extrapolate $h$, $m$, and $d$ in order to get polynomials such that,

$$
f(g^i) = f_i \ \text{ for }\ f \in \{h^k, m, g\}
$$

Define the following polynomial:

$$
Z(x) :=  \sum_{i=1}^n {\huge[}\sum_{k=1}^{c/2} h^k(x) - m(x) * d(x){\huge]}
$$


### Constraints

Given the above definitions and a challenge $\alpha$, the following constraints can be used to determine whether the assertion holds true:

$$
  \begin{aligned}
&Z(1) = 0 \\
  &Z(g \alpha) = Z(\alpha) + \sum_{k=1}^{c/2} h^k(\alpha) - m(\alpha) d(\alpha)
  \end{aligned}
$$

It still remains to ensure that $h^k$ is well constructed for all $1 \leq k \leq c/2$:

$$
h(\alpha)^k \cdot (\alpha + s_{2k}) \cdot (\alpha + s_{2k+1}) = (\alpha + s_{2k}) + (\alpha + s_{2k+1})
$$

Note that, if $c$ is odd, then ther is one unbatched helper column $\{h^{{(c/2)}+1}\}$ for which we need a last constraint:

$$
h(\alpha)^{{(c/2)}+1} \cdot (\alpha + s_{c}) = 1
$$

Finally, the verifier needs to ensure that the `looked table` $t = (t_1, ..., t_m)$, was correctly computed.

In each STARK, $t$ is computed starting from 0 and adding at most 1 at each row. This construction is constrained as follows:

$$
\begin{aligned}
\text{1. }\quad &t(1) = 0  \\
\text{2. }\quad &(t(g^{i+1}) - t(g^{i})) \cdot ((t(g^{i+1}) - t(g^{i})) - 1) = 0 \\
\text{3. }\quad &t(g^{n-1}) = 2^{16} - 1
\end{aligned}
$$

