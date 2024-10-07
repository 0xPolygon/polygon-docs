---
comments: true
---

This document shows you how to integrate a third-party data availability (DAC) solution into your CDK stack.

## Prerequisites

!!! tip
    Make sure you have upgraded your CDK stack if necessary.

## Set up contracts

This section shows you how to create a custom CDK validium DAC contract.

1. Clone [zkevm-contracts](https://github.com/0xPolygonHermez/zkevm-contracts).

2. `cd` into `zkevm-contracts` and checkout tag `v6.0.0-rc.1-fork.9`.

3. Run `npm install` from the root.

4. `cd` to the `contracts/v2/consensus/validium` directory. 

    !!! tip
        - Until further notice, these contracts run on the [etrog release](https://polygon.technology/blog/polygon-zkevm-the-etrog-upgrade-is-live-on-mainnet).

5. Create your custom contract in the same directory, and make sure it implements the [IDataAvailabilityProtocol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/contracts/v2/interfaces/IDataAvailabilityProtocol.sol) interface.

    !!! tip
        - Use the Polygon DAC implementation contract: [PolygonDataCommittee.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/contracts/v2/consensus/validium/PolygonDataCommittee.sol) as a guide.
        - The contract supports custom smart contract implementation and, through this, DACs can add their custom on-chain verification logic.

6. You can leave the `verifyMessage` function empty but make sure the `getProcotolName` function returns a unique name (such as Avail, Celestia, etc). The following example code comes from the [PolygonDataCommitee.sol](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/contracts/v2/consensus/validium/PolygonDataCommittee.sol)  implementation.

    ```solidity
    // Name of the data availability protocol
    string internal constant _PROTOCOL_NAME = "<MY_PROTOCOL_NAME>";

    ...

    /**
     * @notice Return the protocol name
     */
    function getProcotolName() external pure override returns (string memory) {
        return _PROTOCOL_NAME;
    }
    ```

7. Update the [/deployment/v2/4_createRollup.ts](https://github.com/0xPolygonHermez/zkevm-contracts/blob/54f58c8b64806429bc4d5c52248f29cf80ba401c/deployment/v2/4_createRollup.ts#L77) script to add your contract name.

    ```ts
    const supporteDataAvailabilityProtocols = ["<CONTRACT_NAME>"];
    ```

8. Make your contract deployable by copying, editing for your custom implementation, and pasting back in, the `if` statement from the [/deployment/v2/4_createRollup.ts#L251](https://github.com/0xPolygonHermez/zkevm-contracts/blob/54f58c8b64806429bc4d5c52248f29cf80ba401c/deployment/v2/4_createRollup.ts#L260) node creation script. 

!!! info "`PolygonValidiumEtrog.sol` solution"

    The [Etrog DAC integration contract](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/contracts/v2/consensus/validium/PolygonValidiumEtrog.sol) is still work-in-progress at the time of writing but there are some interesting things to note.

    1. It implements the function [`verifyMessage` function](https://github.com/0xPolygonHermez/zkevm-contracts/blob/54f58c8b64806429bc4d5c52248f29cf80ba401c/contracts/v2/consensus/validium/PolygonValidiumEtrog.sol#L231):

        ```solidity
        // Validate that the data availability protocol accepts the dataAvailabilityMessage
        // note This is a view function, so there's not much risk even if this contract was vulnerable to reentrant attacks
        dataAvailabilityProtocol.verifyMessage(
            accumulatedNonForcedTransactionsHash,
            dataAvailabilityMessage
        );
        ```

        where `accumulatedNonForcedTransactionsHash` is used for verification against the protocol and `dataAvailabilityMessage` is a byte array containing the signature and addresses of the committee in ascending order.

    2. It also implements a function to set the data availability protocol at [line 287](https://github.com/0xPolygonHermez/zkevm-contracts/blob/54f58c8b64806429bc4d5c52248f29cf80ba401c/contracts/v2/consensus/validium/PolygonValidiumEtrog.sol#L287) to see how they do this.

        ```solidity
        /**
        * @notice Allow the admin to set a new data availability protocol
        * @param newDataAvailabilityProtocol Address of the new data availability protocol
        */
        function setDataAvailabilityProtocol(
            IDataAvailabilityProtocol newDataAvailabilityProtocol
        ) external onlyAdmin {
            dataAvailabilityProtocol = newDataAvailabilityProtocol;

            emit SetDataAvailabilityProtocol(address(newDataAvailabilityProtocol));
        }
        ```

## Deploy Docker image

This section shows you how to deploy the Docker image containing your custom DAC contract.

1. Edit the following parameters in the [`docker/scripts/v2/deploy_parameters_docker.json`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/docker/scripts/v2/deploy_parameters_docker.json) file:

    ```json
    "minDelayTimelock": 3600, // BECOMES "minDelayTimelock": 1,
    ```

2. Edit the following parameters in the [`/docker/scripts/v2/create_rollup_parameters_docker.json`](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/docker/scripts/v2/create_rollup_parameters_docker.json) file:

    ```json
    "consensusContract": "PolygonValidiumEtrog",  // CHANGE THIS TO YOUR CONTRACT NAME
    "dataAvailabilityProtocol": "PolygonDataCommittee", // ADD THIS PARAMETER
    ```

3. Run the following command:

    ```sh
    cp docker/scripts/v2/hardhat.example.paris hardhat.config.ts
    ```

4. Edit [docker/scripts/v2/deploy-docker.sh](https://github.com/0xPolygonHermez/zkevm-contracts/blob/v6.0.0-rc.1-fork.9/docker/scripts/v2/deploy-docker.sh) to add the following line:

    ```sh
    sudo chmod -R go+rxw docker/gethData before docker build -t hermeznetwork/geth-zkevm-contracts -f docker/Dockerfile .  
    ```

5. In the [deployment/v2/4_createRollup.ts](https://github.com/0xPolygonHermez/zkevm-contracts/blob/54f58c8b64806429bc4d5c52248f29cf80ba401c/deployment/v2/4_createRollup.ts#L290) file, uncomment the 290-291, and add a `console.log` output that grabs the address of the DAC:

    ```ts
    // Setup data committee to 0
    await (await polygonDataCommittee?.setupCommittee(0, [], "0x")).wait();
    console.log(dataAvailabilityProtocol, "deployed to:", polygonDataCommittee.target);
    ```

6. Build the image with the following commands:

    ```sh
    sudo npx hardhat compile
    sudo npm run docker:contracts
    ```

7. Tag the image with the following command, where `XXXX` is custom: 

    ```sh
    docker image tag hermeznetwork/geth-zkevm-contracts hermeznetwork/geth-cdk-validium-contracts:XXXX
    ```

## Set up the node

This section shows you how to set up your CDK node that sends and receives data from the DAC.

1. Create a package that implements the [`DABackender`](https://github.com/0xPolygon/cdk-validium-node/blob/b6ee6cb087099c2e97f3e596f84672fc021b517a/dataavailability/interfaces.go#L14) interface and place it under the [`cdk-validium-node/tree/develop/dataavailability`](https://github.com/0xPolygon/cdk-validium-node/tree/develop/dataavailability) directory. 

2. Add a new constant to the [/dataavailability/config.go](https://github.com/0xPolygon/cdk-validium-node/blob/b6ee6cb087099c2e97f3e596f84672fc021b517a/dataavailability/config.go) file that represents the DAC.

    ```go
    const (
        // DataAvailabilityCommittee is the DAC protocol backend
        DataAvailabilityCommittee DABackendType = "DataAvailabilityCommittee"
    )
    ```

    where `DataAvailabilityCommittee` matches the `_PROTOCOL_NAME` see in the [Set up contracts](#set-up-contracts) section.

3. _OPTIONAL_: Add a config struct to the new package inside the main config.go file so that your package can receive custom configurations using the node’s main config file.

4. Instantiate your package and use it to create the main data availability instance, as done in the Polygon implementation.

## Test the integration

!!! tip
    - By default, all E2E tests run using the DAC. 
    - It is possible to run the E2E tests using other DAC backends by amending the `test.node.config.toml` file.

To test your DAC integration, follow the steps below.

1. Create an E2E test that uses your protocol by following the [test/e2e/datacommittee_test.go](https://github.com/0xPolygon/cdk-validium-node/blob/develop/test/e2e/datacommittee_test.go) example.

2. Generate a docker image containing the changes to the node:

    ```sh
    make build-docker
    ```

3. Build the genesis file for the node:

    - First, clone the [cdk-validium-node](https://github.com/0xPolygon/cdk-validium-node) repo and checkout v0.6.4-cdk.5.
    - Edit the `test/config/test.genesis.config.json` file taking values in the generated output files created previously in the contract repo's `docker/deploymentOutputs` folder:

    !!! info "Parameters to change"
        `l1Config.polygonZkEVMAddres`s ==> `rollupAddress` @ `create_rollup_output.json`
        `l1Config.polygonRollupManagerAddress` ==> `polygonRollupManager` @ `deploy_output.json`
        `l1Config.polTokenAddress` ==> `polTokenAddress` @ `deploy_output.json`
        `l1Config.polygonZkEVMGlobalExitRootAddress` ==> `polygonZkEVMGlobalExitRootAddress` @ `deploy_output.json`
        `rollupCreationBlockNumber` ==> `createRollupBlock` @ `create_rollup_output.json`
        `rollupManagerCreationBlockNumber` ==> `deploymentBlockNumber` @ `deploy_output.json`
        `root` ==> `root` @ `genesis.json`
        `genesis` ==> `genesis` @ `genesis.json`

    !!! important
        - You should follow this step every time you build a new Docker image.

4. Update the contracts Docker image tag with the custom tag you created at the [deploy Docker image](#deploy-docker-image) section, step 7, by amending the node's [Docker compose file](https://github.com/0xPolygon/cdk-validium-node/blob/develop/test/docker-compose.yml).

5. Modify the Makefile so it can run your test. Use the [Polygon DAC Makefile](https://github.com/0xPolygon/cdk-validium-node/blob/develop/test/Makefile) as an example.

