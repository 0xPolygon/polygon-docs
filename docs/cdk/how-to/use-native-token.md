## Prerequisite steps

- You should have a running CDK stack. 
- Follow one of the tutorials linked below if you haven't yet spun up a CDK stack.

!!! warning
    This document is currently being updated for the Kurtosis stack.

## Use a custom native token

1. Go to the `...contracts/deployment` folder and find the `deploy_parameters.json` file.

    !!! warning
        The directory naming is dependent on your build type (rollup or validium). 

2. Open the `deploy_parameters.json` file and add a new entry:

    ```json
    {
        "...":"...",
        "...":"...",
        "maxPriorityFeePerGas":"",
        "multiplierGas": ""
        "gasTokenAddress": "<TOKEN-ADDRESS>"
    }
    ```

    `TOKEN-ADDRESS` is the address of a deployed ERC20 L1 token.

    If you leave the value as empty string, the ETH token address is used as a default.


</br>