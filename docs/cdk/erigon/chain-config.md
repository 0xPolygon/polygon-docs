The following instructions show you how to set up configurations to use a chain other than the default chains.

1. Create a directory `~/dynamic-configs` in the user home directory.

2. Use a chain name that starts with the word `dynamic` e.g. `dynamic-my-network`, and create three files in the `dynamic-configs` directory:

    - `dynamic-{network}-allocs.json`: the allocs file.
    - `dynamic-{network}-chainspec.json`: the chainspec file.
    - `dynamic-{network}-conf.json`: an additional configuration file.
    - `dynamic-{network}.yaml`: the run config file for erigon. 
    
    Use any of the example yaml files at the root of the repo as a base and edit as required, but ensure the chain field is in the format `dynamic-{network}` and matches the names of the config files above.

3. Check the examples for Cardona in [`zk/examples/dynamic-configs`](https://github.com/0xPolygonHermez/cdk-erigon/tree/zkevm/zk/examples/dynamic-configs), copy these into your dynamic-configs folder, and edit as required.

    !!! tip "Allocs file format conversation"
        If you have allocs in the Polygon format from the original network launch, save this file to the root of the `cdk-erigon` code base and run the following:
        
        ```sh
        go run cmd/hack/allocs/main.go [your-file-name]
        ```
        
        This converts the file to the format required by erigon and forms the `dynamic-{network}-allocs.json` file.

    !!! tip "Contract addresses"
        Find the contract addresses for the `dynamic-{network}.yaml` in the files output when launching the network:

        - zkevm.address-sequencer => create_rollup_output.json => sequencer
        - zkevm.address-zkevm => create_rollup_output.json => rollupAddress
        - zkevm.address-admin => deploy_output.json => admin
        - zkevm.address-rollup => deploy_output.json => polygonRollupManagerAddress
        - zkevm.address-ger-manager => deploy_output.json => polygonZkEVMGlobalExitRootAddress

4. The mount point for the folder on docker container is `~/dynamic-configs`, i.e. the home directory of the erigon user.

5. To use the new config when starting erigon, update the `--config` flag with the path to the config file e.g. `--config="/path/to/home-dir/dynamic-networks/dynamic-mynetwork.yaml"`.
