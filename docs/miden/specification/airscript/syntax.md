This page specifies the basic syntax and types.

## Delimiters and special characters

- `:` is used as a delimiter when declaring [source sections](code-organization.md#source-sections) and [types](type-declarations.md)
- `.` is used to access a boundary on a trace column, e.g. `a.first` or `a.last`
- `[` and `]` are used for defining arrays in [type declarations](type-declarations.md) and for indexing in [constraint descriptions](constraints.md)
- `,` is used as a delimiter for defining arrays in [type declarations](type-declarations.md)
- `$` is used to access random values or built-in variables by their identifier. For example, the column at index `i` in the main execution trace can be accessed by `$main[i]`.

## Identifiers

Valid identifiers are strings that start with a letter `a-z` or `A-Z` followed by any combination of letters, digits `0-9` or an underscore `_`.

## Numbers

The only supported numbers are integers, and all integers are parsed as u64. Using a number larger than 2^64 - 1 will result in a `ParseError`.

## Operations

The following operations are supported in [constraint descriptions](constraints.md) with the specified syntax:

- Equality (`a = b`)
- Addition (`a + b`)
- Subtraction (`a - b`)
- Multiplication (`a * b`)
- Exponentiation by a constant integer x (`a^x`)

### Unsupported operations

- Negation
- Division
- Inversion

### Parentheses and complex expressions

Parentheses (`(` and `)`) are supported and can be included in any expression except exponentiation, where complex expressions are not allowed.

The following is allowed:

```
a * (b + c)
```

The following is not allowed:

```
a^(2 + 3)
```

## Section-specific accessors

These accessors may only be used in the specified [source section](code-organization.md) in which they are described below.

### [Boundary constraints](constraints.md#boundary_constraints)

The following accessors may only be applied to trace columns when they are in boundary constraint definitions.

- First boundary (`.first`): accesses the trace column's value in the first row. It is only supported in [boundary constraint descriptions](constraints.md#boundary_constraints).
- Last boundary (`.last`): accesses the trace column's value in the last row. It is only supported in [boundary constraint descriptions](constraints.md#boundary_constraints).

The following accessor may only be applied to public inputs declared in `public_inputs` when they are referenced in boundary constraint definitions.

- Indexing (`input_name[i]`): public inputs may be accessed by using the indexing operator on the declared identifier name with an index value that is less than the declared size of its array.

Here is an example of usage of first and last boundaries and a public input within a boundary constraint:

```
trace_columns:
    main: [a]

public_inputs:
    stack_inputs: [4]
    stack_outputs: [4]

boundary_constraints:
    enf a.first = stack_inputs[0]
    enf a.last = stack_outputs[0]
```

### [Integrity constraints](constraints.md#integrity_constraints)

The following accessor may only be applied to trace columns when they are referenced in integrity constraint definitions.

- Next Row (`a'`): `'` is a postfix operator that indicates the value of the specified trace column in the next row. It is only supported in [integrity constraint descriptions](./constraints.md#integrity_constraints).

Here is an example of usage of the Next Row operator within an integrity constraint:

```
trace_columns:
  main: [a]
  aux: [p]

integrity_constraints:
  enf p' = p * a
```
