This document describes how to introduce cyclicity to execution traces in Polynomial Identity Language.

In order to synchronize the execution trace of a given program with the subgroup $G$ of the multiplicative group $\mathbb{F}^*$, over which interpolation is performed, an extra constant polynomial (or precompiled column) is added to the trace.

An explanation of what this group $G = \langle g \rangle$ is, and why it is naturally a cyclic group, was discussed in the [Basic Concepts](../../concepts/mfibonacci/mfibonacci-example.md) section of the zkProver.

## Non-cyclic SM example

Consider a program with the following execution trace of length $\%\texttt{N} = 4$;

$$
\begin{aligned}\begin{array}{|l|c|c|}\hline
\texttt{row} &\ \mathtt{a} & \mathtt{b} \\ \hline
\ \text{ 0} & \ \texttt{1} & \texttt{1} \\ \hline
\ \text{ 1} & \ \texttt{0} & \texttt{2} \\ \hline
\ \text{ 2} & \texttt{-1} & \texttt{2} \\ \hline
\ \text{ 3} & \ \texttt{1} & \texttt{1} \\ \hline
\end{array}
\end{aligned}
$$

Denote the cyclic group over which interpolation is carried out as $G = \{ g, g^2, g^3, g^4 = 1 \} \subset \mathbb{F}$.

!!! info Concession to an abuse of notation
    We use the symbols $\texttt{a}$ and $\texttt{b}$, that denote columns of the execution trace, to also denote the corresponding polynomials resulting from interpolation. The columns $\texttt{a}$ and $\texttt{b}$ are best expressed as arrays,

    $$
    \texttt{a} = [1,0,-1,1] \ \text{and}\ \texttt{b} = [1,2,2,1]
    $$

    while the respective polynomials that result from interpolation, should rather be denoted differently, say with, $P(X)$ and $Q(X)$, such that for each row index $i$,

    $$
    P(g^i) = \texttt{a}[i]\ \ \text{and}\ \ Q(g^i) = \texttt{b}[i] \tag{eqn}
    $$

    But in order to keep the PIL code simple and easily relatable to the execution trace, we replace the $P$ and $Q$ with $\texttt{a}$ and $\texttt{b}$, respectively. The above $\text{eqn}$ is therefore seen written as,

    $$
    \texttt{a}(g^i) = \texttt{a}[i]\ \ \text{and}\ \ \texttt{b}(g^i) = \texttt{b}[i].
    $$

    For the sake of convenience, in this particular example, the row index starts at $0$ just so it syncs with the normal array indexing.

### Constraints and cyclicity

Observe that the column $\mathtt{a}$ only takes on the values; $0$, $1$ or $−1$; and these values satisfy the constraint,

$$
(\mathtt{a} + 1)\cdot\mathtt{a}\cdot(\mathtt{a} - 1) = 0,
$$

while the values of $\texttt{b}$ are such that

$$
\texttt{b}' = \texttt{a} + \texttt{b}.
$$

This second constraint should be interpreted as,

$$
\texttt{b}'(g^{i}) = \texttt{a}(g^i) + \texttt{b}(g^i).
$$

However, this second constraint is satisfied for every row except for the last one. That is, $\texttt{b}'(g^{3}) \not= \texttt{a}(g^3) + \texttt{b}(g^3)$. Let us proof this inequality.

But we first check one of the other cases. In particular, the case for $i = 2$.

Recall that  $\texttt{b}'(g^{i}) = \texttt{b}(g\cdot g^{i}) = \texttt{b}(g^{i+1})$ by definition. Then,

$$
\text{LHS} = \texttt{b}'(g^{2}) = \texttt{b}(g\cdot g^{2}) = \texttt{b}(g^3) = b[3] = 1 \ \ \text{and} \\
\text{RHS} = \texttt{a}(g^{2}) + \texttt{b}(g^{2}) = a[2] + b[2] = -1 + 2 = 1
$$

This proves that the second constraints holds true for the case $i = 2$.

Now for the case $i = 3$.

Note that $g^{4} = 1 = g^0$, and again by definition, $\texttt{b}'(g^{3}) = \texttt{b}(g\cdot g^{3}) = \texttt{b}(g^{4}) = \texttt{b}(g^{0})$. So then,

$$
\text{LHS} = \texttt{b}'(g^{3}) = \texttt{b}(g\cdot g^{3}) = \texttt{b}(g^{0}) = \texttt{b}[0] = 1\ \ \text{and} \\
\text{RHS} =\ \texttt{a}(g^3) + \texttt{b}(g^3) =\ \texttt{a}[3] + \texttt{b}[3] = 1 + 1 = 2.
$$

This proves that second constraint is not satisfied for $i = 3$. And therefore the execution trace is _not cyclic_.

## Introducing cyclicity

The execution trace can be made cyclic by introducing a selector polynomial, call it $\texttt{SEL}$, such that its column values are $1$ in every row  except the last, where it's $0$,

i.e., $\texttt{SEL}[i] = 1$ for all $i \in \{ 0, 1, 2 \}$, otherwise, $\texttt{SEL}[3] = 0$.

The above execution trace is now modified to the following:

$$
\begin{aligned}
\begin{array}{|l|c|c|c|}\hline
\texttt{row} & \ \mathtt{a} & \mathtt{b} & \mathtt{SEL} \\ \hline
\ \text{ 0} & \ \texttt{1} & \texttt{1} & \texttt{1} \\ \hline
\ \text{ 1} & \ \texttt{0} & \texttt{2} & \texttt{1} \\ \hline
\ \text{ 2} & \texttt{-1} & \texttt{2} & \texttt{1}\\ \hline
\ \text{ 3} & \ \texttt{1} & \texttt{1} & \texttt{0}\\ \hline
\end{array}
\end{aligned}
$$

Given these adjustments, we note that;

- For all $i \in \{ 0, 1, 2, 3 \}$, the constraint $(\mathtt{a} + 1)\cdot\mathtt{a}\cdot(\mathtt{a} - 1) = 0$ still holds true.

- For all $i \in \{ 0, 1, 2 \}$, the constraint  $\texttt{b}' = \texttt{a} + \texttt{b}$  holds true as before. And, even if the constraint is adjusted to $\texttt{b}' = \texttt{SEL} \cdot (\texttt{a} + \texttt{b})$, it still holds true for all $i \in \{ 0, 1, 2 \}$.

- For $i = 3$, we would like to have  $\texttt{b}'(g^3) = \texttt{b}(g^0) = \texttt{b}[0] = 1$. Note that $\texttt{SEL}[3] = 0$, for this particular case. And hence,

    $$
    \texttt{SEL} \cdot (\texttt{a} + \texttt{b}) = 0 \cdot  (\texttt{a} + \texttt{b}) = 0.
    $$

    All-in-all, the adjusted execution trace attains cyclicity if the second constraint is set to:

    $$
    \texttt{b}' =\ \texttt{SEL} \cdot (\texttt{a} + \texttt{b})\ +\ (1 - \texttt{SEL}).
    $$

    As seen earlier, for the case $i = 3$,

    $$
    \text{LHS} = \texttt{b}'(g^{3}) = \texttt{b}(g\cdot g^{3}) = \texttt{b}(g^{0}) = \texttt{b}[0] = 1
    $$

    and now,

    $$
    \text{RHS}\ =\ \texttt{SEL}(g^3)\cdot \big(\texttt{a}(g^3) + \texttt{b}(g^3)\big) +\ \big(1 - \texttt{SEL}(g^3)\big)\ \\
    =\ \texttt{SEL}[3] \cdot \big( \texttt{a}[3] + \texttt{b}[3] \big) +\ (1 - \texttt{SEL}[3])\ \text{ } \\
    =\ 0\cdot \big( 1 + 1 \big) + \big( 1 - 0 \big) =\ 0 + 1 = 1.\quad
    $$

    The valid PIL code, with all the adjustments, is as depicted below:

    ```
    namespace CyclicExample(4);

    pol commit a, b;
    pol constant SEL;
    pol carry = (a+1)*a;
    
    carry*(a-1) = 0;
    b' = SEL*(b+a) + (1-SEL);
    ```

    For implementation purposes, even as alluded to in the previous section, in order to prevent exposing distinguishing features, a configuration file is used to store the exact length of the program $\%\texttt{N} = 4$ so that only the symbol $\texttt{N}$ appears in the PIL code.
