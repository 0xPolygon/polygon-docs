## Dealing with negative numbers

Before looking at ways to properly end a program, let us first make a few remarks on how to handle negative numbers.

Recall that all values of the execution trace belong to a field $\mathbb{F}_p$ where $p=2^{64} −2^{32} +1$.

Since $\mathtt{(p-x) + x \equiv p \texttt{ modulo } p}$  for all $\mathtt{x \in \mathbb{F}_p }$  and  $\mathtt{p \equiv 0 \texttt{ modulo } p}$, it follows that $\mathtt{-x \equiv p-x \texttt{ modulo } p}$. Any negative number $\mathtt{-a}$ is therefore interpreted as $\mathtt{p − a}$.

Consider the same zkASM program with four instructions, as discussed before, except that instead of moving a positive constant 3 into registry $\mathtt{B}$, it now moves a negative constant $\mathtt{-3}$. The execution trace, where the free input is still $\mathtt{7}$, is as a follows.

$$
\begin{aligned}
\begin{array}{|l|c|c|c|c|c|c|c|}\hline
 \texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ } \bf{Instructions } & \texttt{FREE} & \texttt{CONST}& \texttt{setB}& \mathtt{setA}& \texttt{inFREE}& \mathtt{inB} & \mathtt{inA} & \mathtt{A} & \mathtt{A'} & \mathtt{B} & \mathtt{B'} \\ \hline
\mathtt{\$\{getAFreeInput()\} => A} & \texttt{7} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{7} & \mathtt{0} & \mathtt{0} \\ \hline
\texttt{ } \mathtt{-3 => B} & \texttt{0} & \texttt{p-3} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{7} & \mathtt{7} & \mathtt{0} & \mathtt{p-3} \\ \hline
\texttt{ } \mathtt{:ADD } & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \mathtt{7} & \mathtt{4} & \mathtt{p-3} & \mathtt{p-3} \\ \hline
\texttt{ } \mathtt{:END } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{4} & \mathtt{0} & \mathtt{p-3} & \mathtt{0} \\ \hline
\end{array}
\end{aligned}
$$

## Using conditional jumps

The FFTs are most efficient for polynomials of degree $\mathtt{T + 1 = 2^N}$. This causes descrepancies when the program being executed has fewer instructions than an appropriate power of $2$.

Consider the following program, with only five instructions, and its corresponding execution trace.

$$
   \begin{aligned}
   \begin{array}{|l|c|}
   \hline
   \texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ } \bf{Instructions } & \texttt{FREE} & \texttt{CONST}& \texttt{setB} & \mathtt{setA}& \texttt{inFREE}& \mathtt{inB} & \mathtt{inA} & \mathtt{A} & \mathtt{A'} & \mathtt{B} & \mathtt{B'} \\ \hline
   \texttt{ } \mathtt{\$\{getAFreeInput()\} => A} & \texttt{7} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{7} & \mathtt{0} & \mathtt{0} \\\hline
   \texttt{ } \mathtt{3 => B} \qquad\qquad\qquad\qquad\quad & \texttt{0} & \texttt{3} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{7} & \mathtt{7} & \mathtt{0} & \mathtt{3} \\\hline
   \texttt{ } \mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \mathtt{7} & \mathtt{10} & \mathtt{3} & \mathtt{3} \\\hline
   \texttt{ } \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \mathtt{10} & \mathtt{13} & \mathtt{3} & \mathtt{3} \\\hline
   \texttt{ } \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{13} & \mathtt{0} & \mathtt{3} & \mathtt{0} \\\hline
   \end{array}
   \end{aligned}
$$

The question is: How (or when) to end the program when the trace has size $\mathtt{5}$ and the polynomials have are of degree $\mathtt{2^3 = 8}$?

## Naïve way to end a program

A simple and naïve fix could be to repeating the "$\texttt{:END}$" instruction in order to fill the $\mathtt{8 - 5}$ rows of the execution trace. However, for the sake of preserving the cyclicity of the state machine, the last instruction still has to ensure that the next values of registries must revert back to their initial values.

$$
\begin{aligned}
\begin{array}{|l|c|} \hline
\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ } \bf{Instructions } & \texttt{FREE} & \texttt{CONST}& \texttt{setB}& \mathtt{setA}& \texttt{inFREE}& \mathtt{inB} & \mathtt{inA} & \mathtt{A} & \mathtt{A'} & \mathtt{B} & \mathtt{B'} \\ \hline
 \mathtt{\$\{getAFreeInput()\} => A} & \texttt{7} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{7} & \mathtt{0} & \mathtt{0}  \\\hline
 \mathtt{3 => B} \qquad\qquad\qquad\qquad\quad & \texttt{0} & \texttt{3} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{7} & \mathtt{7} & \mathtt{0} & \mathtt{3} \\\hline
 \mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \mathtt{7} & \mathtt{10} & \mathtt{3} & \mathtt{3} \\\hline
 \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{0} & \texttt{1} & \texttt{1} & \mathtt{10} & \mathtt{13} & \mathtt{3} & \mathtt{3} \\\hline
 \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{13} & \mathtt{0} & \mathtt{3} & \mathtt{0} \\\hline
 \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} \\\hline
 \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} \\\hline
 \mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \texttt{0} & \texttt{0} & \texttt{1} & \texttt{1} & \texttt{0} & \texttt{0} & \texttt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} & \mathtt{0} \\\hline
\end{array}
\end{aligned}
$$

Note that, since there are no restrictions placed on the next values of $\mathtt{A'}$ and $\mathtt{B'}$, we can set these to any values. In the above case, both $\mathtt{A'}$ and $\mathtt{B'}$ are set to zeros.

## Programs with conditional jumps

We now add to the zkASM program, the instruction 

$$
\texttt{jump } \texttt{to } \texttt{a } \texttt{particular } \texttt{address } \texttt{if } ...
$$

denoted by $\mathtt{JMPZ(addr)}$. This means the executor must jump to the specified position in the program *on condition* that the preceding operation, denoted by $\texttt{op}$, is zero.

Since this instruction needs to specify the destination of the jump, we need to add the line column so as to indicate which row is each instruction placed in the program. See the table below.

$$
\begin{aligned}
\begin{array}{|l|c|}
\hline
\texttt{ line } & \bf{Instructions } \text{ }\text{ }\text{ }\text{ } \\ \hline
\quad\texttt{ 0 } & \text{ }\mathtt{\$\{getAFreeInput()\} => A} \text{ }\\ \hline
\quad\texttt{ 1 } & \text{ }\mathtt{-3 => B} \qquad\qquad\qquad\quad\quad \\ \hline
\quad\texttt{ 2 } & \text{ }\mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } \\ \hline
\quad\texttt{ 3 } & \text{ }\mathtt{A : JMPZ(5) } \quad\qquad\quad\quad\quad\text{ }\text{ } \\ \hline
\quad\texttt{ 4 } & \text{ }\mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } \\ \hline
\quad\texttt{ 5 } & \text{ }\mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } \\ \hline
\end{array}
\end{aligned}
$$

With regards to the instruction "$\texttt{A:JMPZ(5)}$" in $\texttt{line}$ $\texttt{3}$ of the zkASM program,

1. The $\texttt{A}$ registry, preceding the colon, means that $\texttt{op}$ is set to the value of $\texttt{A}$.

2. If $\texttt{op = 0}$, the program jumps to $\texttt{line}$ $\texttt{5}$.

3. If $\mathtt{op \not= 0}$,  the program continues sequentially with the instruction at $\texttt{line}$ $\texttt{4}$.

## Conditional jumps examples

Suppose the executor of our SM reads a zkASM program where one of its instructions requires a free input to be taken. The aim here is to observe how a variation in free inputs affects the length of the execution trace.

For the sake of brevity, we present execution traces with only five columns (i.e., we omit the columns corresponding to the selectors and setters).

### Example A

In this example, the free input is $\mathtt{FREE = 7}$. Focusing on $\texttt{line}$ $\texttt{3}$: Since in the previous operation, $\mathtt{op=ADD}$ and $\mathtt{A = A + B = 4 \not= 0}$, and thus the condition for the $\texttt{JMPZ}$ is not satisfied. There must be no jump. The execution continues sequentially to the instruction in $\texttt{line}$ $\texttt{4}$. The resulting execution trace is therefore $6$ steps long.

$$
\begin{aligned}
\begin{array}{|l|c|c|c|c|c|c|c|}\hline
\texttt{ line } & \bf{Instructions }\text{ }\text{ }\text{ }\text{ } & \mathtt{FREE} & \mathtt{A} & \mathtt{A'} & \mathtt{B} & \mathtt{B'\ }\\\hline
\quad\texttt{ 0 } & \text{ }\mathtt{\$\{getAFreeInput()\} => A} \text{ } & \quad\mathtt{7} & \mathtt{0} & \mathtt{7} & \mathtt{0} & \mathtt{0\ }\\\hline
\quad\texttt{ 1 } & \text{ }\mathtt{-3 => B} \qquad\qquad\qquad\quad\quad & \quad\mathtt{0} &\mathtt{7} & \mathtt{7} & \mathtt{0} & \mathtt{-3\ }\\\hline
\quad\texttt{ 2 } & \text{ }\mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } & \quad\mathtt{0} & \mathtt{7} & \mathtt{4} & \mathtt{-3\ } & \mathtt{-3\ }\\\hline
\quad\texttt{ 3 } & \text{ }\mathtt{A : JMPZ(5) } \quad\qquad\quad\quad\quad\text{ }\text{ } & \quad\mathtt{0} & \mathtt{4} & \mathtt{4} & \mathtt{-3\ } & \mathtt{-3\ }\\\hline
\quad\texttt{ 4 } & \text{ }\mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } & \quad\mathtt{0} & \mathtt{4} & \mathtt{1} & \mathtt{-3\ } & \mathtt{-3\ }\\\hline
\quad\texttt{ 5 } & \text{ }\mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \quad\mathtt{0} & \mathtt{1} & \mathtt{0} & \mathtt{-3\ } & \mathtt{0}\\\hline
\end{array}
\end{aligned}
$$

### Example B

In this case, the free input is $\mathtt{FREE = 3}$. Again, focusing on $\texttt{line}$ $\texttt{3}$: Since in the previous operation, $\mathtt{op=ADD}$ and $\mathtt{A = A + B = 0}$, it means the condition for the $\texttt{JMPZ}$ is satisfied. Hence the executor jumps to $\texttt{line}$ $\texttt{5}$ as per instruction in $\texttt{line}$ $\texttt{3}$. The execution trace is now only $5$ steps long.

$$
\begin{aligned}
\begin{array}{|l|c|c|c|c|c|c|c|}\hline
\texttt{ line } & \texttt{Instructions } \text{ }\text{ }\text{ }\text{ } & \mathtt{FREE} & \mathtt{A} & \mathtt{A'} & \mathtt{B} & \mathtt{B'\ }\\\hline
\quad\texttt{ 0 } & \text{ }\mathtt{\$\{getAFreeInput()\} => A} \text{ } & \quad\mathtt{3} & \mathtt{0} & \mathtt{3} & \mathtt{0} & \mathtt{0\ }\\\hline
\quad\texttt{ 1 } & \text{ }\mathtt{-3 => B} \qquad\qquad\qquad\quad\quad & \quad\mathtt{0} &\mathtt{3} & \mathtt{3} & \mathtt{0} & \mathtt{-3\ }\\\hline
\quad\texttt{ 2 } & \text{ }\mathtt{:ADD } \qquad\qquad\qquad\quad\quad\quad\text{ }\text{ } & \quad\mathtt{0} & \mathtt{3} & \mathtt{0} & \mathtt{-3\ } & \mathtt{-3\ }\\\hline
\quad\texttt{ 3 } & \text{ }\mathtt{A : JMPZ(5) } \quad\qquad\quad\quad\quad\text{ }\text{ } & \quad\mathtt{0} & \mathtt{0} & \mathtt{0} & \mathtt{-3\ } & \mathtt{-3\ }\\\hline
\quad\texttt{ 5 } & \text{ }\mathtt{:END } \qquad\qquad\qquad\quad\qquad\text{}\text{ }\text{ } & \quad\mathtt{0} & \mathtt{0} & \mathtt{0} & \mathtt{-3\ } & \mathtt{0}\\\hline
\end{array}
\end{aligned}
$$

We observe that the inclusion of conditional jumps in the zkASM programs introduces dynamics to the executor's output. For example, the instructions in the zkASM program (in Example B) are not sequentially executed. This requires more agility in our proving system, more especially that our aim is to lighten the verifier's work.

## Correctness checks for state machines with jumps

The dynamism brought about by the inclusion of jumps in our zkASM programs means more checks need to be added so that the state machine can properly prove correct behaviour.

Since the instructions require the executor to perform varied operations, and due to the presence of jumps, these operations are not sequentially executed, we then need to do a few more checks;

   1. Check program operations.

      Every operation being executed needs to be checked if it is the correct one. That is, if the instruction is an $\texttt{ADD}$, then we must check that indeed an $\texttt{ADD}$ was performed and not a different operation.

   2. Check instructions’ sequence.

      The sequence in which the operations are executed must tally with the instructions in the zkASM program, and not necessarily their usual chronological sequence of the lines of code. e.g., The lines of instructions executed in Example B above, are lines $\texttt{0, 1, 2, 3, 5}$ , where $\texttt{line}$ $\texttt{4}$ was skipped.

      Note that more complicated programs can be built where, for instance, the SM execution jumps to a previous line of code, and thus repeating execution of some instructions.

   3. Check correct program ending.

      How the program ends also needs to be managed. Due to the presence of jumps, the length of the execution trace is no longer constant for the same program if the free inputs are varied.

   4. Check positioning of Publics.

      We must ensure that all $\texttt{publics}$ (the inputs and the outputs) are in the expected positions. So, $\texttt{publics}$ should be placed at known steps. This ensures that the SM's PIL does not have to change with every execution.

      For this reason, $\texttt{publics}$ are going to be placed in either the first positions of the polynomial or the last positions of the polynomial (these are specified positions in the arrays representing the columns of the trace).

   5. Check correct Program (ROM) Execution.

      Although the polynomial identities are there to monitor correct state transitions (checking that each instruction does what it is supposed to do), and also that the correct sequence of instructions is followed, one still needs to make sure the instruction being executed belongs to the program in the first place. So, if for instance, the third instruction is being executed, is it really the third instruction of the right program or not.

      One of the implications of a dynamic execution trace, due to the inclusion of jumps, is that some of the previously *constant* (or preprocessed) polynomials must now be *committed* polynomials.

   If we are going to allow polynomials (i.e., columns in the execution trace) corresponding to the instructions to be committed, we need to be cautious that only instructions belonging to the right program are being executed. For this purpose, we use a tool called [Plookup](https://eprint.iacr.org/2020/315.pdf).
