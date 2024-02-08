The CPU is the central component of the Polygon CDK type-1 prover. Like any central processing unit, it reads instructions, executes them, and modifies the state (registers and the memory) accordingly. 

Other complex instructions, such as Keccak hashing, are delegated to specialized STARK tables. 

This section briefly presents the CPU and its columns. However, details on the CPU logic can be found [here](https://github.com/0xPolygonZero/plonky2/blob/main/evm/spec/cpulogic.tex).

## CPU flow

CPU execution can be decomposed into two distinct phases; CPU cycles, and padding.

This first phase of the CPU execution is a lot bulkier than the second, more so that padding comes only at the end of the execution.

### CPU cycles

In each row, the CPU reads code at a given program counter (PC) address, executes it, and writes outputs to memory. The code could be kernel code or any context-based code.

Executing an instruction therefore results in modifying registers, possibly performing memory operations, and updating the program counter (PC).

In the CPU cycles phase, the CPU can switch between contexts corresponding to different environments depending on calls made. 

Context 0 refers to the kernel, which handles initialization and termination before and after executing a transaction.
  
  - Initialization involves input processing, transaction parsing, and transaction trie updating.
  - While termination includes receipt creation and final trie checks.

Subsequent contexts are created when executing user code.

Syscalls, which are specific instructions written in the kernel, may be executed in a non-zero user context. They don't change the context but the code context, which is where the instructions are read from.

### Padding

At the end of any execution, the length of the CPU trace is padded to the next power of two.

When the program counter reaches the special halting label in the kernel, execution halts. And that's when padding should follow.

There are special constraints responsible for ensuring that every row subsequent to execution halting is a padded row, and that execution does not automatically resume. That is, execution cannot resume without further instructions.

## CPU columns

We now have a look at CPU columns as they relate to all relevant operations being executed, as well as how some of the constraints are checked.  

These are the register columns, operation flags, memory columns, and general columns.  

### Registers

- $\texttt{context}$: Indicates the current context at any given time. So, $\texttt{context}\ 0$ is for the kernel, while any context specified with a positive integer indicates a user context. A user context is incremented by $1$ at every call.
- $\texttt{code_context}$: Indicates the context in which the executed code resides.   
- $\texttt{program_counter}$: The address of the instruction to be read and executed.
- $\texttt{stack_len}$: The current length of the stack.
- $\texttt{is_kernel_mode}$: A boolean indicating whether the kernel is on or not. The kernel is a _privileged mode_ because it means kernel code is being executed, and thus privileged instructions can be accessed.
- $\texttt{gas}$: The amount of gas used in the prevailing context. It is eventually checked if it is below the current gas limit. And must fit in 32 bits.
- $\texttt{clock}$: Monotonic counter which starts at 0 and is incremented by 1 at each row. It is used to enforce correct ordering of memory accesses.
- $\texttt{opcode_bits}$  These are 8 boolean columns, indicating the bit decomposition of the opcode being read at the current PC.

### Operation flags

Operation flags are boolean flags indicating whether an operation is executed or not.

During the CPU cycles phase, each row executes a single instruction, which sets one and only one operation flag.

Note that no flag is set during padding. The decoding constraints ensure that the flag set corresponds to the opcode being read.

There is no 1-to-1 correspondence between instructions and flags. 

For efficiency, the same flag can be set by different, unrelated instructions. 

- Take $\texttt{eq_iszero}$ as an example. It represents both the $\texttt{EQ}$ and $\texttt{ISZERO}$ instructions.

When there is a need to differentiate them in constraints, they get filtered by their respective opcode.

This is possible because the first bit of $\texttt{EQ}$'s opcode is $0$, while that of $\texttt{ISZERO}$'s opcode is $1$.

$\texttt{EQ}$ can therefore be filtered with the constraint:

$$
  \texttt{eq_iszero * (1 - opcode_bits[0])}
$$

and $\texttt{ISZERO}$ with:

$$
  \texttt{eq_iszero * opcode_bits[0]}
$$

### Memory columns

The CPU interacts with the EVM memory via its memory channels. 

At each row, a memory channel can execute a write, a read, or be disabled.

A full memory channel is composed of the following:

- $\texttt{used}$: Boolean flag. If it's set to 1, a memory operation is executed in this channel at this row. If it's set to $0$, no operation is executed but its columns might be reused for other purposes.
- $\texttt{is_read}$: Boolean flag indicating if a memory operation is a read or a write.
- $3\ \texttt{address}$ columns. A memory address is made of three parts: $\texttt{context}$, $\texttt{segment}$ and $\texttt{virtual}$.
- $8\ \texttt{value}$ columns. EVM words are 256 bits long, and they are broken down in 8 32-bit limbs.

The last memory channel is a partial channel. It doesn't have its own $\texttt{value}$ columns but shares them with the first full memory channel. This allows saving eight columns.

### General columns

There are eight ($8$) shared general columns. Depending on the instruction, they are used differently:

- $\texttt{Exceptions}$: When raising an exception, the first three general columns are the bit decomposition of the exception code. These codes are used to jump to the correct exception handler.

- $\texttt{Logic}$: For $\texttt{EQ}$ and $\texttt{ISZERO}$ operations, it is easy to check that the result is $1$ if $\texttt{input0}$ and $\texttt{input1}$ are equal.

It is more difficult to prove that, if the result is $0$, the inputs are actually unequal. In order to prove this, each general column must contain the modular inverse of $(\texttt{input0}_i - \texttt{input1}_i)$ for each limb $i$, or $0$ if the limbs are equal.

Then, the quantity $\texttt{general}_i * (\texttt{input0}_i - \texttt{input1}_i)$ will be $1$ if and only if $\texttt{general}_i$ is indeed the modular inverse, which is only possible if the difference is non-zero.

- $\texttt{Jumps}$: For jumps, we use the first two columns: $\texttt{should_jump}$ and $\texttt{cond_sum_pinv}$. The $\texttt{should_jump}$ column determines whether the EVM should jump: it's $1$ for a JUMP, and $\texttt{condition} \neq 0$ for a JUMPI. To check if the condition is actually non-zero for a JUMPI, $\texttt{cond_sum_pinv}$ stores the modular inverse of $\texttt{condition}$, or $0$ if it's zero.

- $\texttt{Shift}$: For shifts, the logic differs depending on whether the displacement is lower than $2^{32}$ or not. That is, if it fits in a single value limb.
To check if this is not the case, we check if at least one of the seven high limbs is not zero. The general column $\texttt{high_limb_sum_inv}$ holds the modular inverse of the sum of the seven high limbs, and is used to check it's non-zero like the previous cases.
Contrary to the logic operations, we do not need to check limbs individually: each limb has been range-checked to 32 bits, meaning that it's not possible for the sum to overflow and be zero if some of the limbs are non-zero.

- $\texttt{Stack}$:  $\texttt{stack_inv}$, $\texttt{stack_inv_aux}$ and $\texttt{stack_inv_aux_2}$ are used by `popping-only` and `pushing-only` instructions.

The `popping-only` instruction uses the $\text{Stack}$ columns to check if the Stack is empty after the instruction.

While the `pushing-only` instruction uses the $\text{Stack}$ columns to check if the Stack is empty before the instruction.

$\texttt{stack_len_bounds_aux}$ is used to check that the Stack doesn't overflow in user mode. The last four columns are used to prevent conflicts with other general columns.
See the $\text{Stack Handling}$ subsection of this [document](https://github.com/0xPolygonZero/plonky2/blob/main/evm/spec/cpulogic.tex) for more details.