To make writing constraints easier, AirScript provides a number of syntactic conveniences. These are described in this section.

## List comprehension

List comprehension provides a simple way to create new vectors. It is similar to the list comprehension syntax in Python. The following examples show how to use list comprehension in AirScript.

```
let x = [a * 2 for a in b]
```

This will create a new vector with the same length as `b` and the value of each element will be twice that of the corresponding element in `b`.

```
let x = [a + b for (a, b) in (c, d)]
```

This will create a new vector with the same length as `c` and `d` and the value of each element will be the sum of the corresponding elements in `c` and `d`. This will throw an error if `c` and `d` vectors are of unequal lengths.

```
let x = [2^i * a for (i, a) in (0..5, b)]
```

Ranges can also be used as iterables, which makes it easy to refer to an element and its index at the same time. This will create a new vector with length 5 and each element will be the corresponding element in `b` multiplied by 2 raised to the power of the element's index. This will throw an error if `b` is not of length 5.

```
let x = [m + n + o for (m, n, o) in (a, 0..5, c[0..5])]
```

Slices can also be used as iterables. This will create a new vector with length 5 and each element will be the sum of the corresponding elements in `a`, the range 0 to 5, and the first 5 elements of `c`. This will throw an error if `a` is not of length 5 or if `c` is of length less than 5.

## List folding

List folding provides syntactic convenience for folding vectors into expressions. It is similar to the list folding syntax in Python. List folding can be applied to vectors, list comprehension or identifiers referring to vectors and list comprehension. The following examples show how to use list folding in AirScript.

```
trace_columns:
    main: [a[5], b, c]

integrity_constraints:
    let x = sum(a)
    let y = sum([a[0], a[1], a[2], a[3], a[4]])
    let z = sum([a * 2 for a in a])
```

In the above, `x` and `y` both represent the sum of all trace column values in the trace column group `a`. `z` represents the sum of all trace column values in the trace column group `a` multiplied by `2`.

```
trace_columns:
    main: [a[5], b, c]

integrity_constraints:
    let x = prod(a)
    let y = prod([a[0], a[1], a[2], a[3], a[4]])
    let z = prod([a + 2 for a in a])
```

In the above, `x` and `y` both represent the product of all trace column values in the trace column group `a`. `z` represents the product of all trace column values in the trace column group `a` added by `2`.

## Constraint comprehension

Constraint comprehension provides a way to enforce the same constraint on multiple values. Conceptually, it is very similar to the list comprehension described above. For example:

```
trace_columns:
    main: [a[5], b, c]

integrity_constraints:
    enf v^2 = v for v in a
```

The above will enforce $a_i^2 = a_i$ constraint for all columns in the trace column group `a`. Semantically, this is equivalent to:

```
trace_columns:
    main: [a[5], b, c]

integrity_constraints:
    enf a[0]^2 = a[0]
    enf a[1]^2 = a[1]
    enf a[2]^2 = a[2]
    enf a[3]^2 = a[3]
    enf a[4]^2 = a[4]
```

Similar to list comprehension, constraints in constraint comprehension can involve values from multiple lists. For example:

```
trace_columns:
    main: [a[5], b[5]]

integrity_constraints:
    enf x' = i * y for (x, y, i) in (a, b, 0..5)
```

The above will enforce that $a_i' = i \cdot b_i$ for $i \in [0, 5)$. If the length of either `a` or `b` is not 5, this will throw an error.

## Conditional constraints

Frequently, we may want to enforce constraints based on some selectors. For example, let's say our trace has 4 columns: `a`, `b`, `c`, and `s`, and we want to enforce that $c' = a + b$ when $s = 1$ and $c' = a \cdot c$ when $s = 0$. We can write these constraints directly like so:

```
trace_columns:
    main: [a, b, c, s]

integrity_constraints:
    enf s^2 = s
    enf c' = s * (a + b) + (1 - s) * (a * b)
```

Notice that we also need to enforce $s^2 = s$ to ensure that column $s$ can contain only binary values.

While the above approach works, it gets more and more difficult to manage as selectors and constraints get more complicated. To simplify describing constraints for this use case, AirScript introduces `enf match` statement. The above constraints can be described using `enf match` statement as follows:

```
trace_columns:
    main: [a, b, c, s]

integrity_constraints:
    enf s^2 = s
    enf match:
        case s: c' = a + b
        case !s: c' = a * c
```

In the above, the syntax of each "option" is `case <selector expression>: <constraint>`, where selector expression consists of values composed using binary operands and logical operators `!`, `&`, and `|`. AirScript reduces logical operations to their equivalent algebraic operations as follows:

- `!a` reduces to $1 - a$.
- `a & b` reduces to $a \cdot b$.
- `a | b` reduces to $a + b - a \cdot b$.

The example below illustrates how these operators can be used to build more complex selectors:

```
trace_columns:
    main: [a, b, c, s0, s1]

integrity_constraints:
    enf s0^2 = s0
    enf s1^2 = s1
    enf match:
        case s0 & s1:   c' = a + b
        case s0 & !s1:  c' = a * c
        case !s0 & s1:  c' = a - b
        case !s0 & !s1: c' = c
```

AirScript makes the following assumptions about selector expressions, which are not yet enforced by the language:

1. All selector expressions are based on binary values. To enforce these, we must manually add constraints of the form $x^2 = x$ for all values involved in selector expressions.
2. All selector expressions are mutually exclusive. That is, for a given set of inputs, only one of the selector expressions in an `enf match` statement can evaluate to $1$, and all other selectors must evaluate to $0$. Note: it is OK if all selector expressions evaluate to $0$.

### Conditional evaluators

In addition to applying selectors to individual constraints, we can apply them to [evaluators](evaluators.md). For example:

```
trace_columns:
    main: [a, b, c, s]

integrity_constraints:
    enf s^2 = s
    enf match:
        case s: foo([a, b, c])
        case !s: bar([a, b, c])

ev foo([a, b, c]):
    enf c' = a + b

ev bar([a, b, c]):
    enf c' = a * b
```

The above is equivalent to the first example in this section. However, the real power of combining evaluators and conditional constraints comes from two aspects:

1. Evaluators can be [imported](code-organization.md#importing-evaluators) from other modules. Thus, the logic of defining constraints, and then selecting which one is applied in a given case can be cleanly separated.
2. Evaluators can contain multiple constraints. In such cases, selector expressions would be applied to all constraints of an evaluator.

The example below illustrates the latter point.

```
trace_columns:
    main: [a, b, c, s]

integrity_constraints:
    enf s^2 = s
    enf match:
        case s: foo([a, b, c])
        case !s: bar([a, b, c])

ev foo([a, b, c]):
    enf a' = a * 2
    enf b' = b + 1
    enf c' = a + b

ev bar([a, b, c]):
    enf a' = a + 1
    enf b' = b * 3
    enf c' = a * b
```