Public Values refers to values of committed polynomials that are known to both the prover and the verifier, as part of the arithmetization process.

Public Values refers to values of committed polynomials that are known to both the prover and the verifier, as part of the arithmetization process. For example, if the prover is claiming to know the output of a certain computation, then its arithmetization would lead to the inclusion of a public value to some of the polynomials representing such a computation.

In this section, we build a PIL program that arithmetizes a Fibonacci sequence, and illustrate how it makes use of public values.

## Modular Fibonacci sequence

Suppose one wants to prove knowledge of the first two terms $F_1$ and $F_2$ of a Fibonacci sequence $(F_n)_{n \in N}$ whose $1024$-th term $F_{1024}$ is:

$$
F_{1024} = 180312667050811804,
$$

modulo the prime $p = 2^{64} − 2^{32} + 1$.

The witness (that is, the input kept private by the prover) is $F_1 = 2$ and $F_2 = 1$.

The modular Fibonacci sequence can be arithmetized with $3$ columns (i.e., $3$ polynomials):

- First, two committed polynomials $\texttt{a}$ and $\texttt{b}$ that keep track of the sequence elements. We naturally obtain the following constraints between $\texttt{a}$ and $\texttt{b}$;

 $$
 \texttt{a}’ =\ \texttt{b}\qquad \\
 \texttt{b}’ =\ \texttt{a} + \texttt{b}
 $$

- Second, the constant polynomial $\texttt{ISLAST}$, which is defined as,

 $$
 \texttt{ISLAST}(g^i)\ = 0,\ \text{ for all}\ \ i \in [\texttt{N}−1]\ \text{and}\\
 \texttt{ISLAST}(g^i)\ = 1,\ \text{ for}\ i = \texttt{N}.\ \qquad\qquad\quad
 $$

With the introduction of the $\texttt{ISLAST}$ polynomial, the above constraints can be rewritten as follows:

$$
(1−\texttt{ISLAST}) \cdot (a’−b) = 0\quad\quad \\
(1−\texttt{ISLAST}) \cdot (b’−a−b) = 0.
$$

This way, $\texttt{ISLAST}$ ensures that the above constraints are valid in all rows of the execution trace, including the last row. Note that this last row is precisely the point where it is checked whether the claimed $1024$-th term is correct or not.

Based on the above description, the PIL code for the Fibonacci sequence is as follows:

```
// Filename: "fib.pil"

namespace Fibonacci(2**10);
pol constant ISLAST;
pol commit a, b;

(1-ISLAST) * (a' - b) = 0;
(1-ISLAST) * (b' - a - b) = 0;
ISLAST * (a - 180312667050811804) = 0;
```

Notice that the $1024$-th Fibonacci term is hardcoded as $180312667050811804$ in the above PIL code.

This means, every time one uses the same PIL with a different witness ($F_1$, $F_2$) or even a different Fibonacci term, the PIL code would need to be modified.

We solve this by introducing mutable **public values** which the Prover can use to change the witness ($F_1$, $F_2$) or the $\texttt{N}$-th Fibonacci term without the need to alter the PIL code.

```
public result = a(%N-1);
```

The compiler distinguishes between public values identifier and other identifiers with the colon "$\mathtt{:}$". So the syntax for public value $\mathtt{result}$ is "$\mathtt{:result}$".

The updated PIL file is as follows:

```
// Filename: "fib.pil"

include "config.pil";

namespace Fibonacci(%N);
pol constant ISLAST;
pol commit a, b;

public result = a(%N-1);

(1-ISLAST) * (a' - b) = 0;
(1-ISLAST) * (b' - a - b) = 0;
ISLAST * (a - :result) = 0;
```
