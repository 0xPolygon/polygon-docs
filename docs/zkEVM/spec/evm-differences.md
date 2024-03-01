This document provides brief remarks on the differences between the EVM and the Polygon zkEVM. Lists of supported and unsupported EIPs, opcodes, and additional changes made when building the Polygon zkEVM, can be found [here](../architecture/protocol/etrog-upgrade.md).

### EVM-equivalence

Polygon zkEVM is designed to be EVM-equivalent rather than just compatible.

The difference between EVM-compatibility and EVM-equivalence is that;
   
   - Solutions that are compatible support most of the existing applications, but sometimes with code changes. Additionally, compatibility may lead to breaking developer tooling.

   - Polygon zkEVM strives for EVM-equivalence which means most applications, tools, and infrastructure built on Ethereum can immediately port over to Polygon zkEVM, with limited to no changes needed. Things are designed to work 100% on day one. 

EVM-equivalence is critical to Polygon zkEVM for several reasons, including the following:
   
   1. Development teams don't have to make changes to their code, and this eliminates the possibility of introducing new security vulnerabilities.

   2. No code changes means no need for additional audits. This saves time and money.

   3. Since consolidation of batches and finality of transactions is achieved via smart contracts on Ethereum, Polygon zkEVM benefits from the security of Ethereum.

   4. EVM-equivalence allows Polygon zkEVM to benefit from the already vibrant and active Ethereum community.

   5. It also allows for significant and quick dApp adoption, because applications built on Ethereum are automatically compatible.

Ultimately, Polygon zkEVM offers developers the same UX as on Ethereum, with significantly improved scalability.

The following differences have no impact on the developer's experience on the zkEVM compared to the EVM:

   - Gas optimization techniques.
   - Interacting with libraries, like Web3.js and Ethers.js.
   - Deploying contracts seamlessly on the zkEVM without any overhead.

