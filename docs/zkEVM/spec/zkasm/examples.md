## EVM ADD

Let's take the EVM ADD opcode as our first starting example:

```
opADD:
    SP - 2          :JMPN(stackUnderflow)
    SP - 1 => SP
    $ => A          :MLOAD(SP--)
    $ => C          :MLOAD(SP)

    ; Add operation with Arith
    A               :MSTORE(arithA)
    C               :MSTORE(arithB)
                    :CALL(addARITH)
    $ => E          :MLOAD(arithRes1)
    E               :MSTORE(SP++)
    1024 - SP       :JMPN(stackOverflow)
    GAS-3 => GAS    :JMPN(outOfGas)
                    :JMP(readCode)
```

Here is a detailed explanation of how the ADD opcode gets interpreted. Recall that at the beginning, the stack pointer is pointing to the next "empty" address in the stack:

1. First, we check if the stack is filled "properly" in order to carry on the ADD operation. This means that, as the ADD opcode needs two elements to operate, it is checked that these two elements are actually in the stack:

        SP - 2          :JMPN(stackUnderflow)

    If less than two elements are present, then the `stackUnderflow` function gets executed.

2. Next, we move the stack pointer to the first operand, load its value and place the result in the `A` register. Similarly, we move the stack pointer to the next operated, load its value and place the result in the `C` register.

        SP - 1 => SP
        $ => A          :MLOAD(SP--)
        $ => C          :MLOAD(SP)

3. Now its when the operation takes place. We perform the addition operation by storing the value of the registers `A` and `C` into the variables `arithA` and `arithB` and then we call the subroutine `addARITH` that is the one in charge of actually performing the addition.

        A               :MSTORE(arithA)
        C               :MSTORE(arithB)
                        :CALL(addARITH)
        $ => E          :MLOAD(arithRes1)
        E               :MSTORE(SP++)

    Finally, the result of the addition gets placed into the register `E` and the corresponding value gets placed into the stack pointer location; moving it forward afterwise.

4. A bunch of checks are performed. It is first checked that after the operation, the stack is not full and then that we do not run out of gas.

        1024 - SP       :JMPN(stackOverflow)
        GAS-3 => GAS    :JMPN(outOfGas)
                        :JMP(readCode)

Last but not the least, there is an instruction indicating to move forward to the next instruction.
