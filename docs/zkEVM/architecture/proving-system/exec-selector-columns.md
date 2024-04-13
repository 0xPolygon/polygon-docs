In the above discussions, we have generally signalled the operation applied to a specific row by writing the operation alongside that row, but outside the matrix.

There is a need to pull in this information into the execution matrix. 

For this purpose extra columns, called _selector columns_, are appended to the execution matrix.

A selector column will mostly consist of zeros, "$0$"s, and ones, "$1$"s, where a $1$ appears in the row to which the operation is applied.

## Example: (Selector columns)

Consider the two operations defined in the previous example:

$$
\begin{aligned}
&\texttt{Op1}:a' = a + b + c \\
&\texttt{Op2}:c' = a + b + c + a' + b'
\end{aligned}
$$

Their corresponding selector columns are given the same name, and are incorporated in the execution matrix as shown below.

$$
\begin{aligned}
	\begin{array}{|c|c|c|c|c|c|}\hline
		{\texttt{ A }} & {\texttt{ B }} & {\texttt{ C }} & {\texttt{OP1}} & {\texttt{OP2}} \\ \hline
		a_0 & b_0 & c_0 & 1 & 0 \\ \hline
		a_1 & b_1 & c_1 & 0 & 1 \\ \hline
		a_2 & b_2 & c_2 & - & - \\ \hline
    \end{array}
\end{aligned}
$$

This way, the appearance of $1$ in each of the columns $\texttt{Op1}$ and $\texttt{Op2}$ flags when the respective operation is executed.

Designing the execution traces in this way is fully aligned with how interpolation is applied to the execution traces, that is to say _column-wise_.

Selector columns are used to control whether the constraints of an operation apply or not, meaning whether $\texttt{Opx}$ or $\texttt{Opy}$ is applied to a particular row. 

## Selector columns and constraints

Next we explain how correctness of the execution trace can be tested in each row with just one equation. 

Firstly, note that:

$$
\begin{aligned}
&\texttt{Op1}:\ a' = a + b + c \quad\quad \Rightarrow \quad a + b + c - a' = 0 \\
&\texttt{Op2}:\ c' = a + b + c + a' + b' \quad \Rightarrow \quad a + b + c + a' + b' - c' = 0
\end{aligned}
$$

Secondly, correct execution of each operation is tested with a zero-check. That is, checking each of the second equations:

$$
\begin{aligned}
&\texttt{Op1}:\ a + b + c - a' = 0 \\
&\texttt{Op2}:\ a + b + c + a' + b' - c' = 0
\end{aligned}
$$

Thirdly, each operation is only checked if it was applied to the particular row. That is, only if a value $\texttt{Opx} = 1$ appears in the corresponding row. That is, with respect to each operation $\texttt{Opx}$, the following factor is tested:

$$
\texttt{Op1} \cdot \big( 1 - \texttt{Op2} \big) = 1\quad \text{only if}\quad \texttt{Op1} = 1  \\
\texttt{Op2} \cdot \big( 1 - \texttt{Op1} \big) = 1\quad \text{only if}\quad \texttt{Op2} = 1
$$

Note that, $\texttt{Op1} = 0$ if $\texttt{Op2} = 1$, and conversely,  $\texttt{Op2} = 0$ if $\texttt{Op1} = 1$.   

Putting all these together, checking correctness of execution culminates in testing the following constraint:

$$
\texttt{Op1}·(1− \texttt{Op2})·(a+b+c−a')+ \texttt{Op2}·(1− \texttt{Op1})·(a+b+c+a'+b'−c')=0
$$

## Example: (Checking execution correctness)

Consider the above execution trace of the operations $\texttt{Op1}$ and $\texttt{Op2}$.

In the first row, $\texttt{Op1}$ = 1 and $\texttt{Op2}$ = 0, so the right-hand side of the constraint reduces to:

$$
1·(1−0)·(a + b + c − a') + 0·(1 − 1)·(a + b + c + a' + b' − c')= a+b+c−a'
$$

which equals $0$ only if $a' = a + b + c$. And thus proving that $\texttt{Op1}$ was correctly executed. 

Similarly, in the second row,  $\texttt{Op2}$ = 1 and $\texttt{Op1}$ = 0, and the right-hand side of the constraint yields:

$$
0·(1−1)·(a + b + c − a') + 1·(1 − 0)·(a + b + c + a' + b' − c')= a + b + c + a' + b' − c'
$$

which is $0$ only if $c' = a + b + c + a' + b'$. And this proves that $\texttt{Op2}$ was correctly executed.

The values in the selector columns are independent of the input values $x = (x_0, x_1, x_2, ... , x_l)$, but are rather determined by the computation itself. 

That is, the input program: $\big( \texttt{Op1}, \texttt{Op2} \big)$, as seen in the above example. 

Note that the input program could well be $\big( \texttt{Op1}, \texttt{Op1}, \texttt{Op2}, \texttt{Op1}, \texttt{Op2}, \texttt{Op1} \big)$, resulting in the execution trace with the following selector columns:

$$
\begin{aligned}
	\begin{array}{|c|c|c|c|c|c|}\hline
		{\texttt{ A }} & {\texttt{ B }} & {\texttt{ C }} & {\texttt{OP1}} & {\texttt{OP2}} \\ \hline
		a_0 & b_0 & c_0 & 1 & 0 \\ \hline
		a_1 & b_1 & c_1 & 1 & 0 \\ \hline
		a_2 & b_2 & c_2 & 0 & 1 \\ \hline
		a_3 & b_3 & c_3 & - & - \\ \hline
		a_4 & b_4 & c_4 & 1 & 0 \\ \hline
		a_5 & b_5 & c_5 & 0 & 1 \\ \hline
		a_6 & b_6 & c_6 & - & - \\ \hline
		a_7 & b_7 & c_7 & 1 & 0 \\ \hline
	\end{array}
\end{aligned}
$$

Therefore, for each computation, selector columns can be preprocessed.
