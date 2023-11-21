:::caution **Important Update**

There is a proposal to transition the native token of the Polygon PoS network from MATIC to POL. This document will provide details on what this means for users of MATIC, the Polygon ecosystem, and the planned changes. Please read carefully and find more information [<ins>here</ins>](https://polygon.technology/blog/polygon-2-0-implementation-officially-begins-the-first-set-of-pips-polygon-improvement-proposals-released).

:::

## General Overview

### What is POL?

POL is the native token upgrade for the Polygon ecosystem, designed for use in a wide range of activities and purposes, including as a tool for network participation and security. By staking POL, participants can actively contribute to the ecosystem as validators. Importantly, POL has many of the same features as MATIC, is built on OpenZeppelin's ERC20 implementations, and supports [<ins>EIP-2612</ins>](https://eips.ethereum.org/EIPS/eip-2612) for signature-based permit approvals.

### Do I Need to Do Anything Today as an Active Participant?

**No**, if you’re currently using MATIC in the Polygon PoS network, there is nothing to do in the near term. 

Separately, you are encouraged to engage in the governance and decision-making processes put forward by the recent PIPs. 
Your involvement and input can play a significant role in shaping the future of the Polygon ecosystem.

You can participate in governance proposals to vote on various aspects of the Polygon ecosystem through the PIP program.
Check out how to do so [<ins>here</ins>](/docs/category/proposals/).

### **Do** I Need to Do Anything Today **as a Node Operator or Delegator?**

**No**. You can provide feedback on the proposed changes in the PIPs and monitor Github and the forum for new node software versions to remain compatible with your given chain when PIPs are approved by the community.

### **Do** I Need to Do Anything **Today as an Application or Tooling Developer?**

**No**. You can review the [<ins>PIPs</ins>](https://forum.polygon.technology/t/pip-17-polygon-ecosystem-token-pol/12912) and provide feedback on the proposed changes and analyze if any changes break your smart contracts. Developers for applications on the Polygon PoS should not see any breaking changes.

### When Will POL Be Officially Upgraded?

If the POL proposal is supported by the community, the POL upgrade is estimated to take place in Q4 2023. The systems utilizing MATIC will not begin the transition until Q1 2024, allowing time for a smooth migration/upgrade and stakeholder preparation.

### What is the Initial Amount of POL Tokens?

The initial amount of POL refers to the **total number** of POL when the upgrade occurs. In the case of POL, the initial amount is **10 billion tokens — 1:1** with MATIC since this is an **upgrade**.

## Technical Specifications

### Does the Amount of POL Increase Over Time?

Yes, the amount of POL **will increase**, starting at 3% per year at genesis. Governance may change this rate through an upgrade of the `EmissionManager` contract.

### How is POL Minted?

The `EmissionsManager` smart contract is responsible for initiating the upgrade to POL through a minting process. This contract is upgradeable, allowing for future changes through governance. It also ensures that the `StakeManager` and `Treasury` contracts receive their respective amounts of the newly minted tokens.

### What Determines the Emission Rate?

The emission rate is governed by a variable named `mintPerSecondCap` in the primary POL smart contract. Additionally, the `EmissionManager` contract uses a constant called `INTEREST_PER_YEAR_LOG2` to calculate an **annual emission rate, compounded per year**.

### Can the Emission Rate Be Modified?

Yes, the emission rate can be modified through a governance proposal, but cannot surpass `mintPerSecondCap` in the primary POL smart contract.

### What Considerations Go Into POL’s Design?

The economic design of POL incorporates several key considerations to aim for stability, such as:

- **Community Governance**: Active community participation in governance processes allows for adaptability and responsiveness to changing conditions.
- **Smart Contract Security**: The integrity of the underlying smart contracts is crucial for maintaining a stable environment.

## Token Migration and Reversal

### What Is the Purpose of Token Migration?

Token migration serves the purpose of allowing for the upgrade from MATIC to POL. This migration operates on a **1-to-1 conversion** basis.

A migration smart contract will allow users to upgrade from MATIC to POL by calling a smart contract function that will accept MATIC and provide an equal amount of POL in return.  The contract is designed to permit the entire supply of MATIC tokens to be upgraded.

### What Happens to the MATIC Tokens After Migration?

MATIC is held in the migration contract and can be used for unmigration.

### Can POL Tokens Be Reverted Back to MATIC?

**Yes**, the migration contract includes a feature known as "unmigration." This allows users to convert their POL to an equivalent amount of MATIC. Governance controls this feature, providing flexibility in response to network conditions or security concerns.
## Bridging Mechanisms

### How Does the Modified Plasma Bridge Function?

The Plasma Bridge will undergo modifications, with community approval, to change the native token of Polygon PoS to the new POL token. Specifically, the following changes are being proposed:

- **Bridging POL to Polygon PoS**: if you bridge POL tokens to Polygon PoS, you will receive 
an equal amount of native tokens (POL) on Polygon PoS.
- **Bridging POL to Ethereum****: when bridging native tokens (POL), the bridge will always disburse POL tokens.

### Are There Any Breaking Changes?

Yes, if an existing contract relies on receiving MATIC from a bridge and receives POL instead, this might result in locked funds. **Developers must check their contracts, verify the transaction lifecycle, and engage on the forum for any doubts.**

## Governance and Security Protocols

### Who Holds the Authority to Govern the POL-based Contracts?

The contracts are governed by the Polygon decentralized governance model. **In accordance with the PIP process, the community can propose changes and provide feedback.**

### What Security Measures Are in Place?

The contracts have been designed with various security measures, including rate limits on minting and the ability to lock or unlock features like unmigration.

## Implications and Safeguards

### How Is POL Used to Reward Ecosystem Participation?

POL's design aims to foster a sustainable and predictable growth model. This model primarily rewards active contributors and participants within the ecosystem.

### How Can I Avoid Scams?

Always verify contract addresses and use reputable platforms for transactions. Exercise extreme caution when dealing with claims like "swaps" or “transfers” from unverified sources.