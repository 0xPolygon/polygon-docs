## Prerequisite steps

You have previously deployed a CDK using previous versions.

### Deployment guides

- [Deploy a validium CDK](../get-started/deploy-validium/intro.md)
- [Deploy a zkEVM CDK](../get-started/deploy-rollup/intro.md)

!!! warning
    The rollup documentation is currently being updated.

## Use a custom native token

Open the deploy_parameters.json file and add a new entry:

```json
{
    "":"",
    "":"",
    "maxPriorityFeePerGas":"",
    "multiplierGas": ""
    "gasTokenAddress": "<TOKEN-ADDRESS>"
}
```

`TOKEN-ADDRESS` is the address of a deployed ERC20 L1 token.

If you leave the value empty, the ETH token address is used as a default.