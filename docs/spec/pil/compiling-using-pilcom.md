This document describes how Polynomial Identity Language programs are compiled by PILCOM.

Depending on the language used in implementation, every PIL code can be compiled into either a $\texttt{JSON}$ file or a $\texttt{C++}$ code by using a compiler called $\bf{pilcom}$.

The $\bf{pilcom}$ compiler package can be found at this Github repository [here](https://github.com/0xPolygonHermez/pilcom). Setup can be fired up at the command line with the usual $\texttt{clone}$, $\texttt{install}$ and $\texttt{build}$ CLI commands.

Any PIL code can be compiled into a $\texttt{JSON}$ file with the command,

```bash
node src/pil.js <input.pil> -o <output.pil.json>
```

which is a basic $\texttt{JSON}$ representation of the PIL program (with some extra metadata) to be later consumed on by the [pil-stark](https://github.com/0xPolygonHermez/pil-stark) package in order to generate a STARK proof.

Similarly, any PIL code can be compiled into C++ code with this command,

```bash
node src/pil.js <input.pil> -c -n namespace
```

in which case the corresponding header files (`.hpp`) will be generated in the `./pols_generated` folder.

## Restriction on polynomial degrees

The current version of PIL can only handle quadratics. Simply put, **given any set of polynomials; $\texttt{a}$, $\texttt{b}$ and $\texttt{c}$; PIL can only handle products of two polynomials at a time**,

$$
\mathtt{a * a},\ \ \mathtt{a * b}\ \ \text{and}\ \ \mathtt{a * c}
$$

but not higher degrees such as,

$$
\mathtt{a * a * a},\ \ \mathtt{a * b * b},\ \ \mathtt{(1-a) * b * c}\ \ \text{ or }\ \ \mathtt{a * b * c * c}
$$

These higher degree products are handled via an $\texttt{intermediate}$ polynomial, conveniently dubbed $\texttt{carry}$. Consider again the constraint of the optimized Multiplier program:

$$
\texttt{out}' = \texttt{RESET} * \texttt{freeIn}\ +\ (1 - \texttt{RESET}) (\texttt{freeIn} * \texttt{out}) \tag{Eqn. 6}
$$

which involves the trinomial,

$$
(1 - \texttt{RESET}) (\texttt{freeIn} * \texttt{out}) .
$$

A $\texttt{carry}$ can be used in $\text{Eqn. 6}$ as follows,

$$
\texttt{out}' = \texttt{RESET} * \texttt{freeIn}\ +\ (1 - \texttt{RESET})* \texttt{carry} \tag{Eqn. 7}
$$

where in this case, $\texttt{carry} = \texttt{freeIn} * \texttt{out}$.

In the same sense that keywords $\texttt{commit}$ and $\texttt{constant}$ can be thought of as $\text{types}$ of polynomials, $\texttt{intermediate}$ can also be regarded as a third type of polynomial in PIL.

## PIL compilation

In order to compile the above PIL code to a JSON file, follow the following steps.

- Create a subdirectory/folder for the Multiplier SM and call it `multiplier_sm`.

- Switch directory to the new subdirectory `multiplier_sm`, and open a new file. Name it `multiplier.pil` , copy in it the text below and save;

    ```
    namespace Multiplier(2**10); 

    // Constant Polynomials
    pol constant RESET;

    // Committed Polynomials
    pol commit freeIn;
    pol commit out;

    // Intermediate Polynomials
    pol carry = out*freeIn; 

    // Constraints
    out' = RESET*freeIn + (1-RESET)*carry;
    ```

- Switch directory to $\texttt{pilcom}/$ and run the below command,

    ```bash
    node src/pil.js ~/multiplier_sm/multiplier.pil -o multiplier-1st.json
    ```

If compilation is successful, the following debug message will be printed on the command line,

```
Input Pol Commitments: 2
Q Pol Commitmets: 1
Constant Pols: 1
Im Pols: 1
plookupIdentities: 0
permutationIdentities: 0
connectionIdentities: 0
polIdentities: 1
```

The debug message reflects the numbers of;

- Input committed polynomials, denoted by $\texttt{Input Pol Commitments}$,
- Quadratic polynomials, denoted by $\texttt{Q Pol Commitmets}$,
- Constant polynomials, denoted by $\texttt{Constant Pols}$,
- Intermediate polynomials, denoted by $\texttt{Im Pols}$,
- The various identities that can be checked; the $\texttt{Plookup}$, the $\texttt{Permutation}$, the $\texttt{connection}$ and the $\texttt{Polynomial}$ identities.

The resulting $\texttt{JSON}$ file into which the `multiplier.pil` code is compiled looks like this:

```json
{
  "name": "multiplier_sm",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

This $\texttt{JSON}$ file contains all the information needed by the proof/verification package called $\texttt{pil-stark}$ for processing.
