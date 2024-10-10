# Gas fees

CDK chains have full control over how gas fees are set for users, including what token to use for the native gas fees of the L2 chain, which is set to ETH by default.

Gas fees can also be omitted entirely, allowing users to interact with the chain without needing to pay gas fees for transactions and have the fees covered by the chain operator.

By default, gas fees on the L2 are determined by a combination of several factors, including the current gas price on Ethereum, the complexity of the submitted transaction, and the current demand on the L2 network itself.

## Further reading

- [zkEVM gas fees documentation](../../zkEVM/architecture/effective-gas/index.md).