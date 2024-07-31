This document explains the fundamentals of Polynomial Identity Language with the help of a simple multiplier program.

PIL was designed with the aim to simplify the proving and verification of execution correctness. Given that PIL is geared towards modularity, each PIL code has to stipulate a unique identifier for each program. It therefore has an effective syntax that is easy to learn.

In the nutshell, a typical PIL code states the program identifier, the parameters used in the program's computations as well as constraints these parameters must satisfy.

## Key features

A PIL code starts with the program's $\texttt{namespace}$ which is a reserved keyword used to identify the program being executed and to frame the scope of the program definition.

The $\texttt{namespace}$ has to be instantiated with a unique name together with an argument representing the $\texttt{length}$ of the program, which is the maximum number of rows in any execution trace of the program.

In a PIL code, one should define the $\texttt{polynomials}$ used by its program and the $\texttt{constraints}$ among the defined polynomials. Polynomials are identified by the keyword $\texttt{pol}$.

As opposed to $\texttt{constant}$ polynomials which are preprocessed for a given program, $\texttt{committed}$ polynomials are allowed to change from one execution to the next. Constant polynomials are considered public as they are known by all parties, while committed polynomials are in most cases, only known by one party (usually the proving party).

The keyword $\texttt{commit}$ allows the compiler to identify the corresponding polynomial as committed.

## Multiplier program in PIL

Let us create a simple PIL program that models the computation of the product of two integers. Consider a program that, at each step, takes two input numbers and multiplies them.

Such a program is commonly referred to as the $\text{Multiplier}$ program, and it can be modelled by using 3 polynomials;

$$
\mathtt{freeIn1},\  \mathtt{freeIn2}\ \text{ and }\ \mathtt{out}
$$

where $\mathtt{freeIn1}$ and $\mathtt{freeIn2}$ are "free" inputs and $\mathtt{out}$ is the output. The term “free" refers to the fact the values are arbitrarily chosen and they do not strictly depend on any previously computed values.

The corresponding execution trace would be correct if the values in the output $\mathtt{out}$ column satisfy the following identity:

$$
\mathtt{out}\ =\ \mathtt{freeIn1}\ *\ \mathtt{freeIn2}. \tag{Eqn. 1}
$$

See the execution trace of the Multiplier program in the table below:

$$
    \begin{aligned}
        \begin{array}{|l|c|c|c|c|c|c|c|}\hline
        \texttt{row} & \mathtt{freeIn1} & \mathtt{freeIn2} & \texttt{out} \\ \hline
        \ \text{ 1} & \texttt{4} & \texttt{2} & \texttt{8} \\ \hline
        \ \text{ 2} & \texttt{3} & \texttt{1} & \texttt{3}  \\ \hline
        \ \text{ 3} & \texttt{0} & \texttt{9} & \texttt{0} \\ \hline
        \ \text{ 4} & \texttt{7} & \texttt{3} & \texttt{21} \\ \hline
        \ \text{ 5} & \texttt{4} & \texttt{4} & \texttt{16} \\ \hline
        \ \text{ 6} & \texttt{5} & \texttt{6} & \texttt{30} \\ \hline
        \text{ } \ \vdots & \vdots & \vdots & \vdots \\ \hline
        \end{array}
    \end{aligned}
$$

Since the above identity, labelled $\text{Eqn. 1}$, is satisfied in each of the rows of the execution trace, it means that the output column is filled with correct values.

In the language of proof/verification systems concerned with proving and verifying the correctness of the execution trace, the two inputs $\mathtt{freeIn1}$ and $\mathtt{freeIn2}$ together with the output $\mathtt{out}$ are referred to as $\text{polynomials}$.

So, the values in each column of the execution trace actually represents or describes a particular polynomial. Such polynomials can be computed by $\text{interpolation}$.

The PIL code for the above _Multiplier_ program is as follows.

```
namespace Multiplier(2**10);

// Polynomials
pol commit freeIn1;
pol commit freeIn2;
pol commit out;

// Constraints
out = freeIn1*freeIn2;
```

In the above figure, the namespace given to the _Multiplier_ program is $\texttt{Multiplier}$, and its specified length is $2^{10}$.

In the zkEVM context, these polynomials would be committed by the Main state machine for verification, they appear in the PIL code as _pol commit_.

## Optimized Multiplier program

The above design of the _Multiplier_ program, as represented by its execution trace, does not scale easily to more complex operations. The number of polynomials (or number of columns) grows linearly with the number of operations that needs to be performed.

For example, if we were to design a Multiplier program that computes $2^{10}$ operation, the above design would require $2^{10}$ committed polynomials, which is far from being practical.

Here's a more practical design, which reduces the $2^{10}$ committed polynomials to only 3 polynomials;

1. The $\texttt{freeIn}$ polynomial which records, as a column in the execution trace, each input one at a time.

2. The $\texttt{RESET}$ polynomial (column) which flags the starting row of each operation by evaluating to $1$ in each odd row and $0$ otherwise.

3. The $\texttt{out}$ polynomial which holds the result of the operation as before.

See the below table for the corresponding execution trace:

$$
    \begin{aligned}
        \begin{array}{|l|c|c|c|c|}\hline
        \texttt{row} & \mathtt{freeIn} & \mathtt{RESET} & \texttt{out} \\ \hline
         \ \text{ 1} & \texttt{4} & \texttt{1} & \texttt{0} \\ \hline
         \ \text{ 2} & \texttt{2} & \texttt{0} & \texttt{4}  \\ \hline
         \ \text{ 3} & \texttt{3} & \texttt{1} & \texttt{8} \\ \hline
         \ \text{ 4} & \texttt{1} & \texttt{0} & \texttt{3} \\ \hline
         \ \text{ 5} & \texttt{9} & \texttt{1} & \texttt{3} \\ \hline
         \ \text{ 6} & \texttt{0} & \texttt{0} & \texttt{9} \\ \hline
         \ \text{ 7} & \texttt{0} & \texttt{1} & \texttt{0} \\ \hline
         \text{ }\ \text{ } \vdots & \vdots & \vdots & \vdots \\ \hline
        \end{array}
    \end{aligned}
$$

Observe how each column of the execution trace records the "state" in each row.

- $\texttt{row 1}$ : The $\texttt{freeIn}$ column records the first input $4$ of the operation, hence $\texttt{RESET}$ reflects a $1$, while $\texttt{out}$ records $0$ as its default initial value.

- $\texttt{row 2}$ : The $\texttt{freeIn}$ column records the second input $2$ of the operation, $\texttt{RESET}$ reflects a $0$ because the operation has started in the previous row, and now $\texttt{out}$ records the value $4$ which is the first input to the operation.

- $\texttt{row 3}$ : The $\texttt{freeIn}$ column now records the first input $3$ of the second operation (for the sake of simplicity, the same multiplication operation is used again), $\texttt{RESET}$ reflects a $1$ because a fresh operation has begun in this row, and then $\texttt{out}$ records the output value $8$ of the operation that started in $\texttt{row 1}$.

- $\texttt{row 4}$ : Similarly, the $\texttt{freeIn}$ column records the second input $1$ of the operation, $\texttt{RESET}$ reflects a $0$ to indicate the current operation has started in the previous row, and then $\texttt{out}$ records the value $3$ which is the first input to the current operation.

The same pattern is followed in the subsequent rows of the execution trace, for the three columns; $\texttt{freeIn}$, $\texttt{RESET}$ and $\texttt{out}$.  

### Constraints

In order to express the values of the $\texttt{out}$ polynomial in terms of the values of $\texttt{freeIn}$ and $\texttt{RESET}$ per row, we observe the following;

- Whenever $\texttt{RESET}$ equals $1$ (i.e., in every $\texttt{row 2i-1}$), the next value of the $\texttt{out}$ polynomial, denoted by $\texttt{out}'$, equals the value of current $\texttt{freeIn}$ value. That is,

    $$
        \texttt{out}' = \texttt{RESET} * \texttt{freeIn} \qquad\qquad\qquad\qquad \tag{Eqn. 2}
    $$

- Whenever $\texttt{RESET}$ equals $0$ (i.e., in every $\texttt{row 2i}$), the next value $\texttt{out}'$ is the product of the current and the previous values of $\texttt{freeIn}$.
    That is,

    $$
        \texttt{out}' = \texttt{freeIn}_{\texttt{row 2i}} * \texttt{freeIn}_{\texttt{row 2i-1}} \quad\quad \tag{Eqn. 3}
    $$

    which is the value of the $\texttt{out}$ polynomial in $\texttt{row 2i+1}$.

    But, whenever $\texttt{RESET}$ equals $0$  (for every $\texttt{row 2i}$), we have $\texttt{out} = \texttt{freeIn}_{\texttt{row 2i-1}}$. Hence $\text{Eqn. 3}$ can be rewritten as,

    $$
        \texttt{out}' = \texttt{freeIn} * \texttt{out} \qquad\qquad\qquad\qquad\quad \tag{Eqn. 4}
    $$

    Or equivalently, for every $\texttt{row 2i}$, the next output value $\texttt{out}'$ can be expressed as:

    $$
        \texttt{out}' = (1 - \texttt{RESET}) (\texttt{freeIn} * \texttt{out})\quad\quad\quad \tag{Eqn. 5}
    $$

    Putting $\text{Eqn. 2}$ and $\text{Eqn. 5}$ together yields the following constraint:

    $$
        \texttt{out}' = \texttt{RESET} * \texttt{freeIn}\ +\ (1 - \texttt{RESET}) (\texttt{freeIn} * \texttt{out})\quad  \tag{Eqn. 6}
    $$

    Therefore, the PIL code for an optimized Multiplier SM can be written as follows,

    ```
    namespace Multiplier(2**10);

    // Constant Polynomials
    pol constant RESET;

    // Committed Polynomials
    pol commit freeIn;
    pol commit out;

    // Constraints
    out' = RESET*freeIn + (1-RESET)*(out*freeIn);
    ```

    Observe that the $\texttt{RESET}$ polynomial is $\texttt{constant}$ because it does not change from one execution to the next. In an actual implementation of the _Multiplier_ program, $\texttt{RESET}$ would be among the preprocessed polynomials.
