The following document describes how proofs of execution correctness are generated using pil-stark package.

Once the constant and the committed polynomials are filled (as seen in the [Filling polynomials section](filling-polynomials.md)), the next step is generation of a proof of correctness.

A Javascript package called `pil-stark` has been specially designed to work together with `pilcom` to generate STARK proofs for execution correctness of programs being verified.

The `pil-stark` package utilizes three functions: `starkSetup`, `starkGen`, and `starkVerify`.

## `starkSetup`

The first function, `starkSetup`, is for setting up the STARK. Its computational output is independent of the values of committed polynomials. This includes computation of the tree of evaluations of the constant polynomials.

In order to execute the setup generation, one needs an object called `starkStruct`, which specifies the following FRI-related parameters:

- the size of the trace domain (which must coincide with $\texttt{N}$, as defined in PIL),

- the size of the extended domain (which together with the previous parameter specifies the correspondent **blowup factor**),

- the number of queries to be executed and the reduction factors for each of the FRI steps.

We execute the setup using the code below:

```js
const { FGL, starkSetup } = require("pil-stark");

async function execute() {

  // ... input PIL Code

  const starkStruct = {
    "nBits": 10, 
    "nBitsExt": 11, 
    "nQueries": 128, 
    "verificationHashType": "GL", 
    "steps": [ 
      {"nBits": 11}, 
      {"nBits": 5}, 
      {"nBits": 3}, 
      {"nBits": 1} 
    ]
  };

  const setup = await starkSetup(constPols, pil, starkStruct); 
} 
```

## `starkGen`

After setting up the STARK with the `starkSetup` function, the proof of execution correctness can be generated with the `starkGen` function.

The code shown below carries out this task.

```js
const { FGL, starkSetup, starkGen } = require("pil-stark"); 

async function execute() {

  // ... Previous Code

  const resProof = await starkGen(cmPols, constPols, setup.constTree, setup.starkInfo); 
} 
```

Observe that the `starkGen` object contains a `starkInfo` field which contains, besides all the `starkStruct` parameters, a lot of useful information about how the input PIL code looks like.

## `starkVerify`

Now that a proof has been generated, it can be verified by invoking the `starkVerify` function.

This function needs some information provided by the outputs of both the `starkSetup` and `starkGen` function as arguments.

```js
const { FGL, starkSetup, starkGen, starkVerify } = require("pil-stark"); 

async function execute() {
  // ... Previous Code

  const resVerify = await starkVerify( 
    resP.proof, resP.publics, setup.constRoot, setup.starkInfo
  );

  if (resVerify === true) { 
    console.log("The proof is VALID!");
  } else {
    console.log("INVALID proof!");
  }
}
```

If the output of the `starkVerify` function is `true`, the proof is valid. Otherwise, the verifier should invalidate the proof sent by the prover.

A `pil-stark` DIY guide is given [here](../../concepts/mfibonacci/pil-stark-demo.md).
