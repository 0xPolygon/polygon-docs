An AirScript project can consist of one or more modules, each module located in a separate file with a `.air` extension. For projects consisting of multiple modules, one module must be declared as the root module, and all other modules must be declared as library modules.

Currently, all modules must be located in a single directory, but in the future this limitation will be removed.

All modules must start with a module name declaration followed by a set of source sections. These sections describe both the metadata and constraint evaluation logic for the AIR. Depending on the module type, some source sections may be required, be optional, or may not be allowed. The table below summarizes this information.

<center>

| Section                                                                               | Root module | Library module |
| ------------------------------------------------------------------------------------- | :---------: | :---------------: |
| [constants](type-declarations.md#constants-const)                                        | optional    | optional          |
| [trace columns](type-declarations.md#execution-trace-trace_columns)                      | required    | not allowed       |
| [public inputs](type-declarations.md#public-inputs-public_inputs)                        | required    | not allowed       |
| [periodic columns](type-declarations.md#periodic-columns-periodic_columns)               | optional    | optional          |
| [random values](type-declarations.md#random-values-random_values)                        | optional    | not allowed       |
| [boundary constraints](constraints.md#boundary-constraints-boundary_constraints)    | required    | not allowed       |
| [integrity constraints](constraints.md#integrity-constraints-integrity_constraints) | required    | not allowed       |
| [evaluators](evaluators.md)                                                         | optional    | optional          |

</center>

!!! note 
    Constants and evaluators are not really distinct sections but rather a set of declarations which can be done in-between any other sections.

### Root module

A root module defines an entrypoint into an AirScript project. It must start with a name declaration which consists of a `def` keyword followed by the name of the AIR project. For example:

```
def ExampleAir
```

where the name of the module must:

- Be a string consisting of alpha-numeric characters and underscores.
- Start with a letter.
- End with a newline.

Besides the name declaration, a root module must:

- Describe the shape of the execution trace (done via the *trace columns* section).
  - If the trace consists of more than one segment (e.g., main and auxiliary segments), describe random values available to the prover after each segment commitment (done via the *random values* section).
- Describe the shape of the public inputs (done via the *public inputs* section).
- Describe the boundary constraints placed against the execution trace (done via the *boundary constraints* section).
- Describe the integrity constraints placed against the execution trace (done via the *integrity constraints* section).

To aid with boundary and integrity constraint descriptions, a root module may also contain definitions of constants, evaluators, and periodic columns.

### Library modules

Library modules can be used to split integrity constraint descriptions across multiple files. A library module must start with a name declaration which consists of a `mod` keyword followed by the name of the module. For example:

```
mod example_module
```

where the name of the module must:

- Be the same as the name of the file in which the library module is defined (e.g., the above module must be located in `example_module.air` file).
- Be a string consisting of alpha-numeric characters and underscores.
- Start with a letter.
- End with a newline.

Besides the name declaration, library modules my contain definitions of constants, evaluators, and periodic columns. Constants and evaluators defined in a library module may be imported by a root or other library modules.

Library modules inherit random value declarations of the root module. That is, evaluators defined in a library module can reference random values declared in the root module.

## Importing evaluators

A module can import constants and evaluators from library modules via a `use` statement. For example:

```
use my_module::my_evaluator
use my_module::my_constant
```

where:

- `my_module` is a library module located in the same directory as the importing module.
- `my_evaluator` and `my_constant` is an evaluator and a constant defined in `my_module`.

Once an evaluator or a constant is imported, it can be used in the same way as evaluators and constants defined in the importing module.

To import multiple evaluators and constants, multiple `use` statements must be used:

```
use my_module::foo
use my_module::bar
use my_other_module::baz
```

!!! note
    `use` statements can appear anywhere in the module file.
