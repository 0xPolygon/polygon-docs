One of the core features of Polynomial Identity Language is that it allows modular design of its programs. This document describes how PIL connects programs.

## Modular design

One of PIL's core features is that it allows **modular design** of its programs. By modular, we mean the ability to split the design of a program $M$ into multiple smaller programs, such that a proper combination of these small programs leads to $M$.

Without this feature, one would need to combine the logic of multiple pieces in a single design, and as a consequence, a lot of redundant polynomials would be included in the design. Moreover, the resulting design would be too big and difficult to validate and test.

The following example is used throughout this section to illustrate PIL's modularity.

## Example

Suppose that we want to design a program that verifies the operation $a \cdot \bar{a}$, where $a$ is a 4-bit integer and $\bar{a}$ is defined as the integer obtained by negating each of the bits of $a$. (i.e., $\bar{a}$ is the bitwise negation of $a$).

The difficulty here is that bitwise operations are difficult to describe when working directly with chunks of 4 bits.

Then, the idea is to split these integers into bits in another program, allowing us to check the operations in a trivial way.

The main program will consist of $3$ columns; $\texttt{a}$, $\mathtt{neg\_a}$, and $\texttt{op}$. In each row, the column $\texttt{a}$ contains the integer $a$ of the computation $a \cdot \bar{a}$. The columns, $\mathtt{neg\_a}$ and $\texttt{op}$, contain $\bar{a}$ and $a \cdot \bar{a}$, respectively.

The below table represents a valid execution trace of the program that validates negated strings of bits.

$$
    \begin{aligned}
        \begin{array}{|c|c|c|}\hline
        \texttt{row} & \mathtt{a} & \mathtt{neg\_a} & \texttt{op} \\ \hline
        \ \text{ 1} & \texttt{1101} & \texttt{0010} & \texttt{00011010} \\
        \ \text{ 2} & \texttt{0100} & \texttt{1011} & \texttt{00101100} \\
        \ \text{ 3} & \texttt{1111} & \texttt{0000} & \texttt{00000000} \\
        \ \text{ 4} & \texttt{1000} & \texttt{0111} & \texttt{00111000} \\ \hline
        \end{array}
    \end{aligned}
$$

First, there is a need to enforce that each of the inputs is a 4-bit integer. That is, an integer in the range $[0, 15]$.

This can be enforced via an inclusion argument. Specifically, this argument enforces that all the values of a vector belong to a certain range (publicly known). For this reason, such a family of inclusion arguments is often referred to as **range checks**.

The PIL code for a **range check** of a column $\texttt{a}$ is as follows:

    ```
    include "config.pil";

    namespace Global(%N);
    pol constant BITS4;

    namespace Main(%N);
    pol commit a, neg_a , op;

    a in Global.BITS4;
    ```

!!! info "Remarks about the above code"

    `BITS4` is a polynomial containing each of the possible 4-bit integers. These 4-bit integers can be chosen in any order when constructing `BITS4` because **inclusion checks do not respect orderings**.

    Also, observe that `BITS4` is called from a namespace which is different from where it is defined. The syntax `Namespace.polynomial` can be used to access polynomials of other namespaces.

The traditional procedure is to put different namespaces in separate files and then use the include keyword to **“connect”** them. For instance, two programs can be defined as follows.

```
// Filename: global.pil

include "config.pil";

namespace Global(%N); 
pol constant L1;
pol constant BITS4;
```

```
// Filename: main.pil

include "config.pil"; 
include "global.pil"

namespace Main(%N);
pol commit a, neg_a , op;

a in Global.BITS4;
```

As mentioned before, working directly with $4$-bits would be difficult. Hence, a separate program that works bitwise is designed. This program contains a column called $\texttt{bits}$ that stores the single bits that shape each of the integers present in $\texttt{a}$, expressed in [little-endian](https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/). Similarly, another column called $\texttt{nbits}$ containing the negation of each one of the $4$-bit integers in $\texttt{a}$.

See the below table for a concrete example of the execution trace.

$$
\begin{aligned}\begin{array}{|c|c|c|}\hline
\texttt{row} & \mathtt{bits} & \mathtt{nbits} & \mathtt{FACTOR} \\ \hline
\text{1} & \texttt{1} & \texttt{0} & \texttt{1} \\
\text{2} & \texttt{0} & \texttt{1} & \texttt{2} \\
\text{3} & \texttt{1} & \texttt{0} & \mathtt{2^2} \\
\text{4} & \texttt{1} & \texttt{0} & \mathtt{2^3} \\ \hline
\text{5} & \texttt{0} & \texttt{1} & \texttt{1} \\
\text{6} & \texttt{0} & \texttt{1} & \texttt{2} \\
\text{7} & \texttt{1} & \texttt{0} & \mathtt{2^2} \\
\text{8} & \texttt{0} & \texttt{1} & \mathtt{2^3} \\ \hline
\vdots & \vdots & \vdots & \vdots \\ \hline
\end{array}
\end{aligned}
$$

Since $\overline{\mathtt{bits}} = \mathtt{nbits}$, and $\mathtt{bits}$, $\mathtt{nbits} \in \{ 0, 1 \}$, we can express the relation between the columns $\mathtt{bits}$ and $\mathtt{nbits}$ as:

$$
\mathtt{bits} + \mathtt{nbits} = 1.
$$

The idea to connect the $\mathtt{Main}$ program with the $\mathtt{Negation}$ program will be to construct $a$ and $\bar{a}$ from the given bits of each free input integer $a$. Therefore, the inclusion argument that verifies that the tuple $(a,\bar{a})$ from the $\mathtt{Main}$ program is included in the $\mathtt{Negation}$ program will also prove the fact that $\bar{a}$ is correctly constructed. In order to achieve this, we will need a constant polynomial called $\mathtt{FACTOR}$. As depicted in the above table, $\mathtt{FACTOR}$ places the bits in their correct bit-position.

At the same time, a constant polynomial $\texttt{RESET}$ is necessary so as to allow resetting the generation of columns $\texttt{a}$ and $\mathtt{neg\_a}$ from the bits of $\mathtt{bits}$ and $\mathtt{nbits}$ respectively, after every 4 rows.

Observe that the cyclic behavior is ensured in this situation because $4$ divide $\mathtt{N} = 2^{10}$. Since $\mathtt{N}$ should be a power of $2$, this requirement will always be satisfied.

The following are the constraints that should be added to PIL in order to describe this generation:

$$
\mathtt{a}'\ = \ \mathtt{FACTOR}' \cdot \mathtt{bits}' \ +\ (1 - \mathtt{RESET}) \cdot \mathtt{a} \qquad\qquad\qquad \tag{Eqn. 11a}
$$

$$
\mathtt{neg\_a}'\ =\ \mathtt{FACTOR}' \cdot \mathtt{nbits}'\ +\ (1 - \mathtt{RESET}) \cdot \mathtt{neg\_a} \quad\ \tag{Eqn. 11b}
$$

The below table shows a complete example of what the execution trace of the $\mathtt{Negation}$ program looks like.

$$
\begin{aligned}\begin{array}{|c|c|c|}\hline
\texttt{row} & \mathtt{bits} & \mathtt{nbits} & \mathtt{FACTOR} & \mathtt{a} & \mathtt{neg\_a} & \mathtt{RESET} \\ \hline
\text{1} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} \\
\text{2} & \texttt{0} & \texttt{1} & \texttt{2} & \texttt{01} & \texttt{10} & \texttt{0} \\
\text{3} & \texttt{1} & \texttt{0} & \mathtt{2^2} & \texttt{101} & \texttt{010} & \texttt{0} \\
\text{4} & \texttt{1} & \texttt{0} & \mathtt{2^3} & \texttt{1101} & \texttt{0010} & \texttt{1} \\ \hline
\text{5} & \texttt{0} & \texttt{1} & \texttt{1}  & \texttt{0} & \texttt{1} & \texttt{0} \\
\text{6} & \texttt{0} & \texttt{1} & \texttt{2} & \texttt{00} & \texttt{11} & \texttt{0} \\
\text{7} & \texttt{1} & \texttt{0} & \mathtt{2^2} & \texttt{100} & \texttt{011} & \texttt{0} \\
\text{8} & \texttt{0} & \texttt{1} & \mathtt{2^3} & \texttt{0100} & \texttt{1011} & \texttt{1} \\ \hline
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ \hline
\end{array}
\end{aligned}
$$

Observe that the $\mathtt{RESET}$ polynomial ensures that the constraints labelled $\text{Eqn. 11}$ above, are satisfied in each row.

The file which describes correct execution of the $\texttt{Negation}$ program (`negation.pil`) is now as follows:

```
namespace Negation(%N);
pol commit bits, nbits;
pol commit a, neg_a;
pol constant FACTOR , RESET;

bits*(1-bits) = 0; 
nbits*(1-nbits) = 0;

bits + nbits - 2*bits*nbits = 1;

a' = FACTOR'*bits' + (1 - RESET)*a;
neg_a ' = FACTOR '*nbits ' + (1 - RESET)*neg_a;
```

Observe that binary checks for the columns $\texttt{bits}$ and $\texttt{nbits}$ have been added because we need to ensure that both of them are actually bits.

Now, we will connect the $\texttt{Main}$ and the $\texttt{Negation}$ program via an inclusion check, adding the following line into the $\texttt{Main}$ PIL’s namespace:

```
{a, neg_a} in {Negation.a, Negation.neg_a};
```

PIL also allows users to add selectors in the inclusion checks. This feature allows huge malleability as it allows the user to check inclusions between smaller subsets of rows of the execution trace.

With the next line of code, a check on whether a tuple $(\mathtt{a}, \bar{\mathtt{a}})$ is contained in columns $\mathtt{a}$ and $\mathtt{neg\_a}$ in a row where $\mathtt{RESET} = 1$, is enforced.

```
{a, neg_a} in Negation.RESET {Negation.a, Negation.neg_a}
```

However, this introduces redundancy in the PIL because of the design of program itself.

The same is possible from the other side, adding a selector polynomial $\texttt{SEL}$ in the Main program:

```
sel {a, neg_a} in {Negation.a, Negation.neg_a}
```

The above feature, of enforcing row-selective inclusion checks, is crucial in PIL especially in situations where inclusions must be satisfied only in a subset of rows. We will later on see that this is important for improved proving performance.

Also, we can use a combination of selectors, one for each side:

```
sel {a, neg_a} in Negation.RESET {Negation.a, Negation.neg_a}
```

Up to this point, we have created a program (called $\mathtt{Main}$) that uses another program (called $\texttt{Negation}$) to validate that the negation of a specific column $\texttt{a}$ is well constructed.

However, the product of the columns $\texttt{a}$ and $\mathtt{neg\_a}$ still needs to be validated.

In order to handle this, the following constraint can be introduced in the PIL code of $\mathtt{Main}$ program:

$$
\texttt{a} \cdot \mathtt{neg\_a}\ =\ \mathtt{op}
$$

Since the aim here is to illustrate application of the $\mathtt{op}$ polynpomial, and how connections among several programs work, the first version of our previously constructed $\texttt{Multiplier}$ program suffices.

We simply add the following line of code to achieve this:

```
{a, neg_a, op} in {Multiplier.freeIn1, Multiplier.freeIn2, Multiplier.out};
```

## PIL codes

PIL codes of all the newly developed programs can be found below.

```
include "config.pil"; 

namespace Global(%N);
pol constant BITS4;
```

```
include "global.pil"; 
include "multiplier.pil"; 
include "negation.pil"; 
include "config.pil";

namespace Main(%N);
pol commit a, neg_a , op;

a in Global.BITS4;

{a, neg_a} in {Negation.a, Negation.neg_a};
{a, neg_a, op} in {Multiplier.freeIn1, Multiplier.freeIn2, Multiplier.out};
```

```
include "config.pil";

namespace Negation(%N);
pol commit bits, nbits;
pol commit a, neg_a;
pol constant FACTOR , RESET;

bits*(1-bits) = 0; 
nbits*(1-nbits) = 0;

bits + nbits - 2*bits*nbits = 1;

a' = FACTOR'*bits' + (1 - RESET)*a;
neg_a ' = FACTOR '*nbits ' + (1 - RESET)*neg_a;
```

Having all the `.pil` files in the same directory, we can compile `main.pil` and obtain the following debug message:

```bash
Input Pol Commitments: 10
Q Pol Commitments: 0
Constant Pols: 3
Im Pols: 0
plookupIdentities: 3
permutationIdentities: 0
connectionIdentities: 0
polIdentities: 6
```
