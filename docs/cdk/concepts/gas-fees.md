# Gas Fees

CDK-built chains have full control over how gas fees are set for users.

By default, gas fees on the L2 are paid in ETH and are determined by a combination of several factors, including the current gas price on Ethereum, the complexity of the submitted transaction, and the current demand on the L2 network itself.

However, developers can use any [ERC-20 token](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) deployed on the L1 as their native gas token (see the [custom native gas token for a Polygon CDK chain tutorial](https://polygon.technology/blog/tutorial-launch-a-custom-native-gas-token-for-a-polygon-cdk-chain)).
Gas fees can also be omitted entirely, allowing users to interact with the chain without needing to pay gas fees for transactions and have the fees covered by the chain operator.

When building your chain, common options for gas fee configuration include:
- Using ETH as the native gas token for easy onboarding from L1.
- Using an existing ERC-20 token as the native gas token.
- Sponsoring gas fees for all transactions.

For more complex use cases, the CDK is also compatible with several [account abstraction providers](https://ecosystem.polygon.technology/spn/explore/?search=&competency=Wallet&chain=CDK) to provide more flexibility for users in regards to wallet support and gas fee payment.

## Further Reading

- [zkEVM gas fees documentation](https://docs.polygon.technology/zkEVM/architecture/effective-gas/)
