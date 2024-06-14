The following document describes why Polynomial Identity Language uses a special configuration file.

In order for PIL to securely enable modularity, especially in complex settings such as the Polygon zkEVM's, where the Main SM has several secondary state machines executing different computations, a _dependency inclusion feature_ among different _.pil_ files needed to be developed.

## Dependency inclusion feature

Let's consider a scenario. If the PIL code of Secondary SMs reflects unique properties such as the maximum length (for example, the length $\mathtt{2^{10}}$ of the Multiplier SM as seen in the first line of [the _multiplier.pil_ code](compiling-using-pilcom.md)), such properties can easily become magic numbers which attackers could use as distinguishers of which computation is running at a given point in time.

This is where the _dependency inclusion feature_ comes in.

In order to circumvent such possible attacks, a common configuration file written in PIL called _config.pil_, is created to contain configuration-related properties shared among various programs.

Therefore, the file _config.pil_ gets included in the PIL codes of relevant programs, and constants are no longer declared by their values but with keywords or symbols.

Below is the PIL code of the Optimized Multiplier SM, with the _config.pil_ file.

```
include "config.pil"; 

namespace Multiplier(%N);

// Constant Polynomials
pol constant RESET;

// Committed Polynomials
pol commit freeIn; pol commit out;

// Intermediate Polynomials
pol carry = out*freeIn; 

// Constraints
out' = RESET*freeIn + (1-RESET)*carry;
```

Observe that the number $\mathtt{2^{10}}$ does not appear in the PIL code but the symbol "$\texttt{%N}$". In this particular example, it means the _config.pil_ file contains the value $\mathtt{2^{10}}$ as indicated below.

```
constant %N = 2**10;
```

The compiler distinguishes between constant's identifiers and other identifiers via the _percent symbol (%)_. Therefore, all constant identifiers in PIL should be preceded by the _percent symbol (%)_.
