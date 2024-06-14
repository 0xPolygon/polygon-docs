This document describes the connection arguments and how they are used in Polynomial Identity Language.

### What is a connection argument?

Given a vector $a = ( a_1 , \dots , a_n) \in \mathbb{F}_n$ and a partition ${\large{\S}} = \{ S_1, \dots , S_t \}$ of $[n]$, we say "$a$ $\textit{copy-satisfies}$ ${\large{\S}}$" if for each $S_k \in {\large{\S}}$, we have that $a_i = a_j$ whenever $i, j \in S_k$ , with $i, j \in [n]$ and $k \in [t]$.

Moreover, we say that a protocol $(\mathcal{P}, \mathcal{V})$ is a _connection argument_ if the protocol can be used by $\mathcal{P}$ to prove to $\mathcal{V}$ that a vector $\textit{copy-satisfies}$ a partition of $[n]$.

!!! info

    We use the term “connection” instead of “copy-satisfaction” because the argument is used in PIL in a more general sense than in the original definition given in [GWC19](https://eprint.iacr.org/2019/953).

### Example

Let ${\large{\S}} = \{\{2\}, \{1, 3, 5\}, \{4, 6\}\}$ be a specified partition of $[6]$.

Observe the two columns depicted below:

$$
\begin{aligned}
\begin{array}{|c|c|}\hline
\texttt{ a }\\ \hline
\text{3}\\
\text{9}\\
\text{3}\\
\text{1}\\
\text{3}\\
\text{1}\\ \hline
\end{array}
\end{aligned}
\hspace{0.2cm}
\begin{aligned}
\begin{array}{|c|c|}\hline
\texttt{ b }\\ \hline
\text{3}\\
\text{9}\\
\text{7}\\
\text{1}\\
\text{3}\\
\text{1}\\ \hline
\end{array}
\end{aligned} \tag{Table 1}
$$

The vector $\mathtt{a}\ \textit{copy-satisfies}\ {\large{\S}}$ because $\mathtt{a}_1 = \mathtt{a}_3 = \mathtt{a}_5 = 3$ and $\mathtt{a}_4 = \mathtt{a}_6 = 1$.

Observe that, since the singleton $\{2\}$ is in ${\large{\S}}$, then $\mathtt{a}_2$ is not related to any other element in $\mathtt{a}$.

Also, the vector $\mathtt{b}$ does not $\textit{copy-satisfies}\ {\large{\S}}$ because $\mathtt{b}_1 = \mathtt{b}_5 =3 \not= 7 = \mathtt{b}_3$.

In the context of programs, connection arguments can be written easily in PIL by introducing a column associated with the chosen partition. This is also done in [[GWC19]](https://eprint.iacr.org/2019/953).

Recall that column values are evaluations of a polynomial at $G = \langle g \rangle$ and $\texttt{N}$ is the length of the execution trace.

Given a polynomial $\texttt{a}$ and a partition ${\large{\S}}$, suppose we want to write in PIL a constraint attesting to the $\textit{copy-satisfiability}$ of a certain ${\large{\S}}$.

We first construct a permutation $\sigma : [n] \to [n]$ such that for each set $S_i \in {\large{\S}}$, we have that $\sigma({\large{\S}})$ contains a cycle of all elements of $S_i$.

In the above example, we would have $\sigma = (5, 2, 1, 6, 3, 4)$. So then, we construct a polynomial $S_a$ that encodes $\sigma$ in the exponent of $g$. That is:

$$
S_{\texttt{a}}(g^i) = g^{\sigma(i)}
$$

for $i \in [n]$.

In the PIL context, the previous connection argument between a column $\texttt{a}$ and a column $\texttt{SA}$, encoding the values of $S_{\texttt{a}}$, can be declared using the keyword $\texttt{connect}$ using the syntax: $\texttt{a}\ \texttt{connect}\ \{\texttt{SA}\}$.

```
include "config.pil";

namespace Connection(%N); 
pol commit a; 
pol constant SA; 

{a} connect {SA};
```

A valid execution trace for this example was shown in Table 1 above.

!!! info Remark

    The column $\texttt{SA}$ does not need to be declared as a constant polynomial. The _connection argument_ still holds true even if it is declared as committed.

## Multiple copy satisfiability

Connection arguments can be extended to several columns by encoding each column with a “part” of the permutation. Informally, the permutation is now able to span across the values of each of the involved polynomials in a way that the cycles formed in the permutation must contain the same value.

### Multi-column copy satisfiability

Given vectors $a_1, \dots , a_k$ in $\mathbb{F}^n$ and a partition ${\large{\S}} = \{S_1,...,S_t\}$ of $[kn]$, we say $a_1,...,a_k$ $\textit{copy-satisfy}\ {\large{\S}}$ if for each $S_m \in {\large{\S}}$, we have that $a_{{l_1},i} = a_{{l_2},j}$ whenever $i,j \in S_m$, with $i,j \in [n]$, $l_1, l_2 \in [k]$ and $m \in [t]$.

For example, say that we have ${\large{\S}} = \{\{1\}, \{2,3,4,9\}, \{5\}, \{6\}, \{7,10\}, \{8,11\}, \{12\}\}$. Then, the below table depicts an execution trace for three columns $\texttt{a}, \texttt{b}, \texttt{c}$ that copy-satisfies ${\large{\S}}$.

![An execution trace subject to a connection argument](../../../img/zkEVM/21pil2-exec-trace-connection-arg.png)

We reduce this problem to the one column case by thinking of the permutation $\sigma$ as applied to the concatenation of column $\texttt{a}$, then $\texttt{b}$ and finally $\texttt{c}$.

So, the permutation $\sigma$ that makes $\texttt{a}$, $\texttt{b}$ and $\texttt{c}$ copy-satisfy ${\large{\S}}$ is $(1, 9, 2, 3, 5, 6, 10, 11, 4, 7, 8, 12)$.

In this case we construct polynomials $S_{\texttt{a}}$, $S_{\texttt{b}}$ and $S_c$ such that:

$$
S_{\texttt{a}}(g^i)\ = g^{\sigma(i)},\ S_{\texttt{b}}(g^i)\ = k_1 \cdot g^{\sigma(n+i)},\ S_{\texttt{c}}(g^i)\ = k_2 \cdot g^{\sigma(2n+i)}
$$

where $k_1, k_2 \in \mathbb{F}$ are introduced here as a way of obtaining more elements (in a group $G$ of size $n$) and enabling correct encoding of the $[3n] \to [3n]$ permutation $\sigma$.

See [[GWC19]](https://eprint.iacr.org/2019/953) for more details on this encoding.

The below table shows how to compute the polynomials $\texttt{SA}$, $\texttt{SB}$ and $\texttt{SC}$ encoding the permutation of the above example:

![Multi-column connection argument’s valid execution trace](../../../img/zkEVM/22pil2-multi-column-connection-arg.png)

The PIL code for this example is easily written as follows:

```
include "config.pil";

namespace Connection(%N);
pol commit a, b, c;
pol constant SA, SB, SC;

{ a, b, c } connect { SA, SB, SC };
```
