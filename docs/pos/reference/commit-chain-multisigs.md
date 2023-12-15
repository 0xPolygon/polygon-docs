
## Purpose and capabilities

The primary role of multi-signature wallets (multisigs) is to facilitate contract upgrades during the early stages of development. As these contracts become more robust, Polygon plans to:

- Transition from multisigs to governance-controlled proxies.
- Implement timelocks for added security.
- Phase out multisigs entirely in the long term.

**It's important to note that the existing multisigs do not have the capability to censor transactions, including bridge transactions.**

## Active multi-signature wallets

### Ethereum chain multisigs

| Multisig Address  | **5/9 Multisig**<br/>`0xFa7D2a996aC6350f4b56C043112Da0366a59b74c` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To upgrade PoS and staking contracts on Ethereum.                    |
| Chain            | Ethereum                                                            |
| Rights           | - Update staking contracts for optimizations and upgrades.<br/>- Address unexpected bugs in PoS contracts. |
| Signatories      | Quickswap, Curve, Polygon, Horizon Games, Cometh                     |

### Polygon commitchain multisigs

| Multisig Address  | **5/8 Multisig**<br/>`0x355b8E02e7F5301E6fac9b7cAc1D6D9c86C0343f` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To update custom ChildERC20s on Polygon Commitchain.                 |
| Chain            | Polygon Commitchain                                                  |
| Rights           | Ability to upgrade custom child contracts.                           |
| Signatories      | Quickswap, Curve, Polygon, Horizon Games, Cometh                     |

### Custom child ERC20s mapping

| Multisig Address  | **4/8 Multisig**<br/>`0x424bDE99FCfB68c5a1218fd3215caFfD031f19C4` |
|:----------------:|---------------------------------------------------------------------|
| Purpose          | To enable the mapping of custom ChildERC20s with Mainnet contracts.  |
| Chain            | Ethereum                                                            |
| Rights           | Limited to mapping; no access to Child tokens or deposit/withdrawal rights. |
| Signatories      | Polygon                                                             |

### Permissionless mapping

| Multisig Address  | **Permissionless Mapping of Standard ChildERC20 Tokens (No Multisig Required)** |
|:----------------:|--------------------------------------------------------------------------------|
| Purpose          | FxPortal supports permissionless token mapping of standard ChildERC20 for any ERC20 token on Ethereum. |
| Chain            | Permissionless                                                                 |
| Rights           | Permissionless                                                                 |
| Signatories      | Permissionless                                                                 |

<sub>*Plans are underway to transition these functions to governance. We are currently exploring options such as Aave's governance contracts and Compound’s timelock contracts.</sub>
