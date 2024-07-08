!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

## Chronicle  

[Chronicle Protocol](https://chroniclelabs.org/) is a novel Oracle solution that has exclusively secured over $10B in assets for MakerDAO and its ecosystem since 2017. Chronicle overcomes the current limitations of transferring data on-chain by developing scalable, cost-efficient, decentralized, and verifiable Oracles, rewriting the rulebook on data transparency and accessibility.

### Querying the price of MATIC using Chronicle
Chronicle contracts are read-protected by a whitelist, meaning you won't be able to read them on-chain without your address being added to the whitelist. On the Testnet, users can add themselves to the whitelist through the SelfKisser contract, a process playfully referred to as "kissing" themselves. For access to production Oracles on the Mainnet, please open a support ticket on [Discord](https://discord.com/invite/CjgvJ9EspJ) in the 🆘｜support channel.

For the deployment addresses, please check out the [Dashboard](https://chroniclelabs.org/dashboard/oracles). 
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.16;

/**
 * @title OracleReader
 * @notice A simple contract to read from Chronicle oracles
 * @dev To see the full repository, visit https://github.com/chronicleprotocol/OracleReader-Example.
 * @dev Addresses in this contract are hardcoded for the zkEVM Testnet.
 * For other supported networks, check the https://chroniclelabs.org/dashboard/oracles.
 */
contract OracleReader {
    /**
    * @notice The Chronicle oracle to read from.
    * Chronicle_MATIC_USD_1 - 0x55a07a60cd9ed198B5Ba4360FF9800eBb6667388
    * Network: zkEVM Testnet
    */

    IChronicle public chronicle = IChronicle(address(0x55a07a60cd9ed198B5Ba4360FF9800eBb6667388));

    /** 
    * @notice The SelfKisser granting access to Chronicle oracles.
    * SelfKisser_1:0x0Dcc19657007713483A5cA76e6A7bbe5f56EA37d
    * Network: zkEVM Testnet
    */
    ISelfKisser public selfKisser = ISelfKisser(address(0x0Dcc19657007713483A5cA76e6A7bbe5f56EA37d));

    constructor() {
        // Note to add address(this) to chronicle oracle's whitelist.
        // This allows the contract to read from the chronicle oracle.
        selfKisser.selfKiss(address(chronicle));
    }

    /** 
    * @notice Function to read the latest data from the Chronicle oracle.
    * @return val The current value returned by the oracle.
    * @return age The timestamp of the last update from the oracle.
    */
    function read() external view returns (uint256 val, uint256 age) {
        (val, age) = chronicle.readWithAge();
    }
}

// Copied from [chronicle-std](https://github.com/chronicleprotocol/chronicle-std/blob/main/src/IChronicle.sol).
interface IChronicle {
    /** 
    * @notice Returns the oracle's current value.
    * @dev Reverts if no value set.
    * @return value The oracle's current value.
    */
    function read() external view returns (uint256 value);

    /** 
    * @notice Returns the oracle's current value and its age.
    * @dev Reverts if no value set.
    * @return value The oracle's current value using 18 decimals places.
    * @return age The value's age as a Unix Timestamp .
    * */
    function readWithAge() external view returns (uint256 value, uint256 age);
}

// Copied from [self-kisser](https://github.com/chronicleprotocol/self-kisser/blob/main/src/ISelfKisser.sol).
interface ISelfKisser {
    /// @notice Kisses caller on oracle `oracle`.
    function selfKiss(address oracle) external;
}
```
### More examples
For more examples on integrating Chronicle Oracles, please check the [documentation portal](https://docs.chroniclelabs.org/). 

    