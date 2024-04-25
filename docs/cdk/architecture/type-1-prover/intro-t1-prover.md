The Polygon type 1 prover is a zk-evm proving component used for creating proofs on your ZK-EVM chain. It has been developed in collaboration with the Toposware team.

!!! info
    The [Polygon type 1 prover](https://github.com/0xPolygonZero/zk_evm) is not yet ready for full implementation into a CDK stack.

## Get started

If you want to get up and running quickly, follow the [how to deploy the type 1 prover guide](../../how-to/deploy-t1-prover.md).

!!! warning
    Throughout this section, we refer to ZK-EVM chains in a general sense and this should not be confused with Polygon's zkEVM product which is a specific example of a ZK-EVM.

## Type definitions

The emergence of various ZK-EVMs ignited the debate of how 'equivalent' is a given ZK-EVM to the Ethereum virtual machine (EVM).

Vitalik Buterin has since introduced some calibration to EVM-equivalence in his article, "[The different types of ZK-EVMs](https://vitalik.eth.limo/general/2022/08/04/zkevm.html)". He made a distinction among five types of ZK-EVMs, which boils down to the inevitable trade-off between Ethereum equivalence and the efficacy of the zero-knowledge proving scheme involved. For brevity, we refer to this proving scheme as the zk-prover or simply, prover.

The types, as outlined by Vitalik, are as follows;

- **Type 1** ZK-EVMs strive for full Ethereum-equivalence. These types do not change anything in the Ethereum stack except adding a zk-prover. They can therefore verify Ethereum and environments that are exactly like Ethereum.
- **Type-2** ZK-EVMs aim at full EVM-equivalence instead of Ethereum-equivalence. These ZK-EVMs make some minor changes to the Ethereum stack with the exception of the Application layer. As a result, they are fully compatible with almost all Ethereum apps, and thus offer the same UX as with Ethereum.
- **Type-2.5** ZK-EVMs endeavor for EVM-equivalence but make changes to gas costs. These ZK-EVMs achieve fast generation of proofs but introduces a few incompatibles.
- **Type-3** ZK-EVMs seek to be EVM-equivalent but make a few minor changes to the Application layer. These type of ZK-EVMs achieve faster generation of proofs, and are not compatible with most Ethereum apps.
- **Type-4** ZK-EVMs are high-level-language equivalent ZK-EVMs. These type of ZK-EVMs take smart contract code written in Solidity, Vyper or other high-level languages and compile it to a specialized virtual machine and prove it. Type-4 ZK-EVMs attain the fastest proof generation time.

The figure below gives a visual summary of the types, contrasting compatibility with performance.

![Figure: ZK-EVM types](../../../img/cdk/zkevm-types-vitalik.png)

Ultimately, choosing which type of ZK-EVM to develop involves a trade-off between EVM-equivalence and performance.

The challenge this poses for developers who favor exact Ethereum-equivalence is to devise ingenious designs and clever techniques to implement faster zk-provers. Vitalik mentions one mitigation strategy to improve proof generation times: cleverly engineered, and massively parallelized provers.