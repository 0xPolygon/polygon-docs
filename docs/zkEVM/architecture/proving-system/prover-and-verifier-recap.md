The Prover, shown in the figure below, is the component within the Proving System which is in charge of generating a proof for the correct execution of some program. 

The program, which takes care of the computational aspect of the computation, is written in a language called **zkASM**, developed by the Polygon team. 

Providing also the private and the public inputs, the **Executor** component within the Prover is able to generate the execution traces designed to model the willing computation. 

The executor produces two binary files: one containing the **fixed columns**, which should only be generated once if we do not change the computation itself, and the other containing the **witness columns**, which vary with inputs and thus need to be generated anew for each proof. 

The files containing the pre- processed fixed columns and the processed witness columns for the zkEVM are temporary stored in binary files and are quite large, consisting on more than 100Gb. 

Subsequently, the cryptographic backend of the prover, in conjunction with the compiled PIL constraints through pilcom and the execution trace binary files generated earlier, can produce the proof and provide the public values, both inputs and outputs, for the verifier.

![Figure: ](../../../img/zkEVM/prover-overall-schema-output-proof.png)

The figure above depicts the schema of the prover component.

The Prover component has 3 subcomponents:

- The Executor, which is in charge of populating the execution trace based on some computation with values depending on some inputs.
- The PIL compiler or pilcom, which compiles PIL files into JSON files prepared to be consumed by the Prover.
- The cryptographic backend, which takes the output of both the Executor and the pilcom and generates the proof and the publics for the verifier.

Posteriorly, as depicted below, the verifier uses both the proof and the public values to check if the prover has performed the computation in a correct way.

![Figure: ](../../../img/zkEVM/prover-publics-verifier-ok-o-ko.png)

The verifier utilizes both the proof and the public values to validate the correctness of the computation performed by the prover.
