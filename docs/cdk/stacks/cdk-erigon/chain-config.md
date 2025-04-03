To use chains other than the [defaults](releases.md#current-chainfork-support-status), supply a set of custom configuration files.

1. Ensure the chain name starts with the word `dynamic` e.g. `dynamic-mynetwork`.

2. Create the following files for dynamic configs. The examples for Cardona are in `zk/examples/dynamic-configs` and can be edited as required:

    - `dynamic-{network}-allocs.json` - the allocs file.
    - `dynamic-{network}-chainspec.json` - the chainspec file.
    - `dynamic-{network}-conf.json` - an additional configuration file.
    - `dynamic-{network}.yaml` - the run config file for erigon.  
    
    You can use any of the example yaml files at the root of the repo as a base and edit as required, but ensure the `chain` field is in the format `dynamic-mynetwork` and matches the names of the config files above.

3. Put the erigon config file, along with the other files, in the directory of your choice. For example `dynamic-mynetwork`.

    !!! tip
        - If you have allocs in the Polygon format from the original network launch, save this file to the root of the `cdk-erigon` code base and run `go run cmd/hack/allocs/main.go [your-file-name]` to convert it to the format needed by erigon. 
        - This creates the `dynamic-{network}-allocs.json` file.

    !!! tip
        Find the following contract addresses for the `dynamic-{network}.yaml` in the output files created at network launch:

        - `zkevm.address-sequencer` => `create_rollup_output.json` => `sequencer`
        - `zkevm.address-zkevm` => `create_rollup_output.json` => `rollupAddress`
        - `zkevm.address-admin` => `deploy_output.json` => `admin`
        - `zkevm.address-rollup` => `deploy_output.json` => `polygonRollupManagerAddress`
        - `zkevm.address-ger-manager` => `deploy_output.json` => `polygonZkEVMGlobalExitRootAddress`

4. Mount the directory containing the config files on a Docker container. For example `/dynamic-mynetwork`.

5. To use the new config when starting erigon, use the `--config` flag with the path to the config file e.g. `--config="/dynamic-mynetwork/dynamic-mynetwork.yaml"`.
