This document describes how to fill Polynomials in PIL using JavaScript and Pilcom.

In this document, we are going to use **Javascript** and **pilcom** to generate a specific execution trace for a given PIL.

To do so, we are going to use the execution trace of a program previously discussed in the [Connection arguments](connection-arguments.md) section.

We will also use the **pil-stark** library, which is a utility that provides a framework for setup, generation and verification of proofs. It uses an FGL class which mimics a finite field, and it is required by some functions that provide the **pilcom** package.

## Execute code

First of all, under the scope of an asynchronous function called `execute`, we parse the provided PIL code (which is, in our case, `main.pil`) into a **Javascript** object using the `compile` function of **pilcom**.

In code, we obtain the following;

```js
const { FGL } = require("pil-stark"); 
const { compile } = require("pilcom"); 
const path = require("path");

async function execute() { 
  const pil = await compile(FGL, path.join(__dirname, "main.pil"));
}
```

## Pilcom package

The **pilcom** package also provides two functions; `newConstPolsArray` and `newCommitPolsArray`. Both these functions use the `pil` object in order to create two crucial objects:

1. First is the constant polynomials object `constPols`, which is created by the `newConstPolsArray` function, and
2. Second is the committed polynomials object `cmPols`, created by `newCommitPolsArray`.

Below is an outline of the **pilcom** package.

```js
const { newConstantPolsArray, newCommitPolsArray, compile } = require("pilcom");

async function execute() {

  // ... Previous Code

  const constPols = newConstantPolsArray(pil); 
  const cmPols = newCommitPolsArray(pil); 
}
```

## Accessing execution trace

The above-mentioned objects contain useful information about the PIL itself, such as the provided length of the program `N`, the total number of constant polynomials and the total number of committed polynomials. Accessing these objects will allow us to fill the entire execution trace for that PIL.

A specific position of the execution trace can be accessed by using the syntax:

```js
pols.Namespace.Polynomial[i]
```

Note that;

- `pols` points to one of the above-mentioned objects; `constPols` and `cmPols` objects
- `Namespace` is a specific `namespace` among the ones defined by the PIL files
- `Polynomial` refers to one of the polynomials defined under the scope of the `namespace`
- index $i$ is an integer in the range $[0, N − 1]$, representing the row of the current polynomial

Using these, the polynomials can now be filled.

## `Main.pil` code example

In our example, we recall the `main.pil` seen in the [Connection arguments](connection-arguments.md) section about $4$-bit integers.

Since we are only allowed to use $4$-bit integers, inputs for the trace, which are also the ones introduced in the $\mathtt{Main.a}$ polynomial, is a chain of integers n ascending cyclically from $0$ to $15$.

We propose two functions here.

- One for building the constant polynomials:

    ```js
    async function buildConstantPolynomials(constPols, polDeg) {
      for (let i=0; i < polDeg; i++) { 
        constPols.Global.BITS4[i] = BigInt(i & 0b1111); 
        constPols.Global.L1[i] = i === 0 ? 1n : 0n; 
        constPols.Negation.RESET[i] = (i % 4) == 3 ? 1n : 0n; 
        constPols.Negation.FACTOR[i] = BigInt(1 << (i % 4));
        constPols.Negation.ISLAST[i] = i === polDeg-1 ? 1n : 0n;
      } 
    }
    ```

- And another function for building the committed polynomials:

```js
async function buildcommittedPolynomials(cmPols, polDeg) { 
  cmPols.Negation.a[-1] = 0n;
  cmPols.Negation.neg_a[-1] = 1n; 

  for (let i=0; i < polDeg; i++) {
    let fourBitsInt = i % 16;

    cmPols.Main.a[i] = BigInt(fourBitsInt); 
    cmPols.Main.neg_a[i] = BigInt(fourBitsInt ^ 0b1111); 
    cmPols.Main.op[i] = FGL.mul(cmPols.Main.a[i], cmPols.Main.neg_a[i]);
    
    cmPols.Multiplier.freeIn1[i] = cmPols.Main.a[i]; 
    cmPols.Multiplier.freeIn2[i] = cmPols.Main.neg_a[i]; 
    cmPols.Multiplier.out[i] = cmPols.Main.op[i];
    
    let associatedInt = Math.floor(i/4); 
    let bit = (associatedInt >> (i%4) & 1) % 16; 
    cmPols.Negation.bits[i] = BigInt(bit); 
    cmPols.Negation.nbits[i] = BigInt(bit ^ 1);
    
    let factor = BigInt(1 << (i % 4)); 
    let reset = (i % 4) == 0 ? 1n : 0n; 
    cmPols.Negation.a[i] = factor*cmPols.Negation.bits[i] 
      + (1n-reset)*cmPols.Negation.a[i-1]; 
    cmPols.Negation.neg_a[i] = factor*cmPols.Negation.nbits[i] 
      + (1n-reset)*cmPols.Negation.neg_a[i-1];
  }
}
```

Once the constant and committed polynomials have been filled in, we can check whether these polynomials actually satisfy the constraints defined in the PIL file, by using a function called `verifyPil`.

Below is the piece of code that constructs the polynomials and checks the constraints. If the verification procedure fails, we should not proceed to the proof generation because it will lead to false proof. For the sake of brevity, we simply use the line ```// ... Previous Code``` to indicate where the PIL code being verified would be inserted.

```js
const { newConstantPolsArray, newCommitPolsArray, compile, verifyPil } = require("pilcom"); 

async function execute() {

  // ... Previous Code

  const N = constPols.Global.BITS4.length; 

  await buildConstantPolynomials(constPols, N); 
  await buildcommittedPolynomials(cmPols, N);

  const res = await verifyPil(FGL, pil, cmPols , constPols); 
  if (res.length != 0) {
    console.log("The execution trace do not satisfy PIL restrictions. Aborting...");
    for (let i=0; i<res.length; i++) {
      console.log(res[i]);
      return;
  }
}
```
