POL is the native token upgrade for the Polygon ecosystem, designed for use in a wide range of activities and various purposes. For instance, POL is used as a tool for network participation and security. By staking POL, participants can actively contribute to the ecosystem as validators. Importantly, like MATIC, POL is built on OpenZeppelin's ERC20 implementations, supports [EIP-2612](https://eips.ethereum.org/EIPS/eip-2612) for signature-based permit approvals, and thus inherits most of the features found in MATIC.

## PIPs

Community-driven governance and feedback played a crucial role in refining the POL token's design and functionality. Learn more about the proposals by following the links below.

1. [PIP-17: Polygon Ecosystem Token (POL)](https://forum.polygon.technology/t/pip-17-polygon-ecosystem-token-pol/12912)
2. [PIP-18: Polygon 2.0 Phase 0 - Frontier](https://forum.polygon.technology/t/pip-18-polygon-2-0-phase-0-frontier/12913)
3. [PIP-19: Update Polygon PoS Native Token to POL](https://forum.polygon.technology/t/pip-19-update-polygon-pos-native-token-to-pol/12914)
4. [PIP-25: Adjust POL Total Supply](https://forum.polygon.technology/t/pip-25-adjust-pol-total-supply/13008)
5. [PIP-26: Transition from MATIC to POL Validator Rewards](https://forum.polygon.technology/t/pip-26-transition-from-matic-to-pol-validator-rewards/13046)

!!! info "Initial amount of POL tokens"

    In the case of POL, the initial amount (the total number of POL when the upgrade occurs) is 10 billion tokens — 1:1 with MATIC since this is an upgrade.

## Do I need to do anything manually?

Please refer to the [MATIC to POL migration guide](../../get-started/matic-to-pol.md) for details on what action you need to take, if any, depending on the chain they are currently located, i.e., Ethereum, Polygon PoS, Polygon zkEVM, etc. 

!!! tip "Deep dive into POL"

    Read the detailed [blog post on the POL migration](https://polygon.technology/blog/save-the-date-matic-pol-migration-coming-september-4th-everything-you-need-to-know) to learn more about the POL token, its properties, and what the migration means for the Polygon ecosystem.

As a dApp developer, feel free to review the PIP's to analyze the changes to the token protocol. Ideally, developers shouldn't see any breaking changes. But if you do, feel free to reach out to us via the [Polygon R&D Discord](https://discord.com/invite/0xpolygonrnd).

## POL technical information

### Does the amount of POL increase over time?

Yes, the amount of POL will increase on an emissions schedule that has reached community consensus. Originally proposed as a $2\%$ yearly emission rate, with $1\%$ to the community treasury and $1\%$ to validator rewards, community consensus was reached in [PIP-26](https://forum.polygon.technology/t/pip-26-transition-from-matic-to-pol-validator-rewards/13046) to continue the original emissions reward schedule, in addition to the proposed POL emissions rate, with an end date of the original emissions reward schedule in June 2025. PIP-26 revised the percentage of validator rewards to $2\%$ for the fourth year (2023-2024), $1.5\%$ for the fifth year (2024-2025), and $1\%$ thereafter—for an effective emission of $2\%$ increase of POL per year beginning after June 2025. Governance may change this rate through an upgrade of the `EmissionManager` contract.

### How is POL minted?

The `EmissionManager` smart contract is responsible for initiating the upgrade to POL through a minting process. This contract is upgradeable, allowing for future changes through governance. It also ensures that the `StakeManager` and `Treasury` contracts receive their respective amounts of the newly minted tokens.

### What determines the emission rate?

The emission rate is governed by a variable named `mintPerSecondCap` in the primary POL smart contract. Additionally, the `EmissionManager` contract uses a constant called `INTEREST_PER_YEAR_LOG2` to calculate an annual emission rate, compounded per year.

### Can the emission rate be modified?

Yes, the emission rate can be modified through a governance proposal, but cannot surpass `mintPerSecondCap` in the primary POL smart contract.

### What considerations go into POL’s design?

The economic design of POL incorporates several key considerations to aim for stability, such as:

- Community Governance: Active community participation in governance processes allows for adaptability and responsiveness to changing conditions.
- Smart Contract Security: The integrity of the underlying smart contracts is crucial for maintaining a stable environment.

## Token migration and reversal

### What is the purpose of token migration?

Token migration serves the purpose of allowing for the upgrade from MATIC to POL. This migration operates on a 1-to-1 conversion basis.

A migration smart contract will allow users to upgrade from MATIC to POL by calling a smart contract function that will accept MATIC and provide an equal amount of POL in return.  The contract is designed to permit the entire supply of MATIC tokens to be upgraded.

### What happens to the MATIC tokens after migration?

MATIC is held in the migration contract and can be used for unmigration.

### Can POL tokens be reverted back to MATIC?

Yes, the migration contract includes a feature known as 'unmigration'. This allows users to convert their POL to an equivalent amount of MATIC. Governance controls this feature, providing flexibility in response to network conditions or security concerns.

## Bridging mechanisms

### How does the modified bridge function?

The bridge will undergo modifications, with community approval, to change the native token of Polygon PoS to the new POL token. Specifically, the following changes are being proposed:

- Bridging POL to Polygon PoS: if you bridge POL tokens to Polygon PoS, you will receive
an equal amount of native tokens (POL) on Polygon PoS.
- Bridging POL to Ethereum: when bridging native tokens (POL), the bridge will always disburse POL tokens.

### Are there any breaking changes?

Yes, if an existing contract relies on receiving MATIC from a bridge and receives POL instead, this might result in locked funds. Developers must check their contracts, verify the transaction lifecycle, and engage on the forum for any doubts.

## Governance and security protocols

### Who holds the authority to govern the POL-based contracts?

The contracts are governed by the Polygon decentralized governance model. In accordance with the PIP process, the community can propose changes and provide feedback.

### What security measures are in place?

The contracts have been designed with various security measures, including rate limits on minting and the ability to lock or unlock features like 'unmigration'.

## Implications and safeguards

### How is POL used to reward ecosystem participation?

POL's design aims to foster a sustainable and predictable growth model. This model primarily rewards active contributors and participants within the ecosystem.

### How can I avoid scams?

Always verify contract addresses and use reputable platforms for transactions. Exercise extreme caution when dealing with claims like "swaps" or “transfers” from unverified sources.
