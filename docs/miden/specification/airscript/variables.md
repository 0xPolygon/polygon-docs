This section describes the syntax for declaring local variables and built-in variables.

## Local variables

In AirScript, variables can be declared in `boundary_constraints` and `integrity_constraints` sections and can contain any expression that would be valid within that source section. Variables can be of type scalar, vector or matrix. In the example below, `x` is a variable of type `scalar`, `y` is a variable of type `vector` and `z` is a variable of type `matrix`.

```
def VariablesExample

const A = 1
const B = 2

trace_columns:
    main: [a, b, c, d]
    aux: [e, f]

public_inputs:
    stack_inputs: [16]

random_values:
    rand: [16]

boundary_constraints:
    let x = stack_inputs[0] + stack_inputs[1]   
    let y = [$rand[0], $rand[1]]  
    enf e.first = x + y[0] + y[1]

integrity_constraints:
    let z = [
        [a + b, c + d],
        [A * a, B * b]
    ]
    enf a' = z[0][0] + z[0][1] + z[1][0] + z[1][1]
```

### Syntax restrictions

Currently, it is not possible to:

1. Create matrices containing both arrays and references to arrays.

    Example:

    ```
    ...
    boundary_constraints:
        let a = [[1,2], [3,4]]  # <-- this is allowed
        let b = [1, 2]
        let c = [a[1], b]  # <-- this is allowed
        let d = [b, [3, 4]]  # <-- this is not allowed, because `d` consists of array `[3, 4]` and reference to array `b`
        enf ...
    ...
    ```
2. Create variables with list comprehension for which the source array is a inlined vector, a matrix row, or a range in matrix row.

    Example: 

    ```
    ...
    integrity_constraints:
        let a = [[1, 2], [3, 4]]
        let b = [5, 6]
        let c = 7
        let d = [e for e in [8, 9, 10]]  # <-- source array is an inlined vector
        let f = [g for g in a[1]]  # <-- source is a matrix row
        let h = [i for i in a[0][0..2]]  # <-- source is a range in matrix row
        enf ...
    ...
    ```

## Built-in variables

Built-in variables are identified by the starting character `$`. There are two built-in variables:

### \$main

`$main` is used to access columns in the [main execution trace](appendix.md#main-vs-auxiliary-execution-trace-segments-main-and-aux).

These columns may be accessed by using the indexing operator on `$main`. For example, `$main[i]` provides the `(i+1)th` column in the main execution trace.

Columns using the `$main` built-in may only be accessed within source sections for integrity constraints, i.e. the [`integrity_constraints` section](constraints.md#integrity-constraints-integrity_constraints).

### \$aux

`$aux` is used to access columns in the [auxiliary execution trace](appendix.md#main-vs-auxiliary-execution-trace-segments-main-and-aux).

These columns may be accessed by using the indexing operator on `$aux`. For example, `$aux[i]` provides the `(i+1)th` column in the auxiliary execution trace.

Columns using the `$aux` built-in may only be accessed within source sections for integrity constraints, i.e. the [`integrity_constraints` section](constraints.md#integrity-constraints-integrity_constraints).