# Keywords

AirScript defines the following keywords:

- `boundary_constraints`: used to declare the source section where the [boundary constraints are described](constraints.md#boundary_constraints).
  - `first`: used to access the value of a trace column at the first row of the trace. _It may only be used when defining boundary constraints._
  - `last`: used to access the value of a trace column at the last row of the trace. _It may only be used when defining boundary constraints._
- `case`: used to declare arms of [conditional constraints](convenience.md#conditional-constraints).
- `const`: used to declare [constants](type-declarations.md#constant-constant).
- `def`: used to [define the name](code-organization.md#root-module) of a root AirScript module.
- `enf`: used to describe a single [constraint](constraints.md).
  - `enf match`: used to describe [conditional constraints](convenience.md#conditional-constraints).
- `ev`: used to declare a transition constraint [evaluator](evaluators.md).
- `integrity_constraints`: used to declare the source section where the [integrity constraints are described](constraints.md#integrity_constraints).
- `let`: used to declare intermediate variables in the boundary_constraints or integrity_constraints source sections.
- `mod`: used to [define a name](code-organization.md#library-modules) of a library AirScript module.
- `periodic_columns`: used to declare the source section where the [periodic columns are declared](type-declarations.md). _They may only be referenced when defining integrity constraints._
- `prod`: used to fold a list into a single value by multiplying all of the values in the list together.
- `public_inputs`: used to declare the source section where the [public inputs are declared](type-declarations.md). _They may only be referenced when defining boundary constraints._
- `random_values`: used to declare the source section where the [random values are described](type-declarations.md).
- `sum`: used to fold a list into a single value by summing all of the values in the list.
- `trace_columns`: used to declare the source section where the [execution trace is described](type-declarations.md). _They may only be referenced when defining integrity constraints._
  - `main`: used to declare the main execution trace.
  - `aux`: used to declare the auxiliary execution trace.
- `use`: used to [import evaluators](code-organization.md#importing-evaluators) from library AirScript modules.
- `$<identifier>`: used to access random values provided by the verifier.
- `$main`: used to access columns in the main execution trace by index.
- `$aux`: used to access columns in the auxiliary execution trace by index.