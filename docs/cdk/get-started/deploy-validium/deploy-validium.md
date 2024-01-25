!!! important "Recommendation"
    Follow the [quickstart](quickstart-validium.md) for a hands-on introduction to CDK in validium mode.

!!! note
    - The documentation describes standard deployments. 
    - Edit the configuration files to implement your own custom setups.

Follow the steps below to deploy a CDK validium instance.

## 1. Deploy validium-specific contracts

!!! important
    - Follow this step if you are deploying to a public testnet.
    - For a local deploy, follow step 2 instead which deploys a local L1 network plus CDK contracts.

First, deploy the relevant contracts.

Follow the steps in the [CDK validium contracts repository's README](https://github.com/0xPolygon/cdk-validium-contracts).

## 2. Run the CDK validium node

!!! important
    - If you are deploying to a public testnet, follow the previous step 1.

Next, set up and run the CDK validium node.

Follow the instructions in the [CDK validium node repository's README](https://github.com/0xPolygon/cdk-validium-node).

## 3. Run the data availability (DA) node (optional step)

Finally, once the CDK validium node is operational, set up and run the data availability node.

Check for instructions here: [CDK DA Node GitHub running instructions](https://github.com/0xPolygon/cdk-data-availability/blob/main/docs/running.md).
