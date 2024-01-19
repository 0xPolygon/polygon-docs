Polygon Miden's AirScript is designed to make it simple to describe AIR constraints and generate efficient and accurate constraint evaluation code in the required target language. The code for AirScript can be found [here](https://github.com/0xPolygonMiden/air-script/).

## Current version

At the time of writing, AirScript is on version 0.3, which includes about 95% of features needed to describe Miden VM constraints, and supports generation of constraint evaluation code for the following backends:

AirScript includes the following features:

- **Trace columns**: Users can declare trace columns for main and auxiliary traces as individual columns or groups of columns (e.g. `main: [a, b, c[3], d]` where `a`, `b`, and `d` are single columns and `c` refers to a group of 3 columns)

- **Public inputs**: Users can declare public inputs where each public input is a named vector (e.g. `stack_inputs: [16]`)

- **Periodic columns**: Users can declare periodic columns (e.g. `k0: [1, 0, 0, 0]`)

- **Random values**: Users can define random values provided by the verifier (e.g. `alphas: [x, y[14], z]` or `rand: [16]`)

- **Boundary constraints**: Users can enforce boundary constraints on main and auxiliary trace columns using public inputs, random values, constants and variables.

- **Integrity constraints**: Users can enforce integrity constraints on main and auxiliary trace columns using trace columns, periodic columns, random values, constants and variables.

- **Constants**: Users can declare module level constants. Constants can be scalars, vectors or matrices.
  (e.g. `const A = 123`, `const B = [1, 2, 3]`, `const C = [[1, 2, 3], [4, 5, 6]]`)

- **Variables**: Local variables can be declared for use in defining boundary and integrity constraints. Variables can be scalars, vectors or matrices built from expressions (e.g. `let x = k * c[1]'`, `let y = [k * c[1], l * c[2], m * c[3]]` or `let z = [[k * c[1], l * c[2]], [m * c[3], n * c[4]]]`)

- **Evaluators**: Users can declare evaluator functions to group multiple related integrity constraints together. Evaluators can be declared locally or imported from other modules. This helps increase modularity and readability of AirScript code.

The language also includes some convenience syntax to make writing constraints easier. This includes:

- **List comprehension** - e.g., `let x = [k * c for (k, c) in (k, c[1..4])]`.
- **List folding** - e.g., `let y = sum([k * c for (k, c) in (k, c[1..4])])`.
- **Constraint comprehension** - e.g., `enf x^2 = x for x in a`.
- **Conditional constraints** - which enable convenient syntax for turning constraints on or off based on selector values.

### CLI

There is a command-line interface available for emitting constraint evaluation code in Rust or Miden assembly. There are also several example `.air` files written in AirScript which can be found in the `examples/` directory.

To use the CLI, first run:

```sh
cargo build --release
```

Then, run the `airc` target with the `transpile` option. For example:

```sh
./target/release/airc transpile examples/example.air
```
This will output constraint evaluation code targeted for the Winterfell prover.

You can use the `help` option to see other available options.

```sh
./target/release/airc transpile --help
```

## Future work

The following changes are some of the improvements under consideration for future releases.

- More advanced language functionality for better ergonomics and modularity, such as:
  - Support for functions.
  - Specialized expressions for multiset checks.
- Optimizations, such as:
  - Constant folding.
  - Removing unnecessary nodes from the `AlgebraicGraph` of boundary and integrity constraints.
  - Combining integrity constraints with mutually exclusive selectors to reduce the total number of constraints.
  - Optimizing constraint evaluation logic for Miden assembly backend.
- Additional language targets for simplifying verifier implementations:
  - Solidity.
- Formal verification.
