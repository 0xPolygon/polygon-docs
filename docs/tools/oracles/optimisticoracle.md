!!! info "Content disclaimer"

    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

UMA's Optimistic Oracle allows contracts to quickly request and receive any kind of data. UMA's oracle system is comprised of two core components:

1. Optimistic oracle
2. Data verification mechanism (DVM)

## Optimistic oracle

UMA's **Optimistic Oracle** allows contracts to quickly request and receive price information. The Optimistic Oracle acts as a generalized escalation game between contracts that initiate a price request and UMA's dispute resolution system known as the Data Verification Mechanism (DVM).

Prices proposed by the Optimistic Oracle will not be sent to the DVM unless it is disputed. This enables contracts to obtain price information within any pre-defined length of time without writing the price of an asset on-chain.

## Data verification mechanism (DVM)

If a dispute is raised, a request is sent to the DVM. All contracts built on UMA use the DVM as a backstop to resolve disputes. Disputes sent to the DVM will be resolved 48 hours after UMA tokenholders vote on the price of the asset at a given time. Contracts on UMA do not need to use the Optimistic Oracle unless it requires a price of an asset faster than 48 hours.

The Data Verification Mechanism (DVM) is the dispute resolution service for contracts built on UMA Protocol. The DVM is powerful because it encompasses an element of human judgment to ensure contracts are securely and correctly managed when issues arise from volatile (and sometimes manipulatable) markets.

## Optimistic oracle interface

The Optimistic Oracle is used by financial contracts or any third party to retrieve prices. Once a price is requested, anyone can propose a price in response. Once proposed, the price goes through a liveness period where anyone can dispute the proposed price and send the disputed price to the UMA DVM for settlement.

!!! info

    This section explains how different participants can interact with the Optimistic Oracle. To view the most updated mainnet, kovan or L2 deployments of the Optimistic Oracle contracts, refer to the [production addresses](https://docs.umaproject.org/dev-ref/addresses).

There are twelve methods that make up the Optimistic Oracle interface.

- `requestPrice`
- `proposePrice`
- `disputePrice`
- `settle`
- `hasPrice`
- `getRequest`
- `settleAndGetPrice`
- `setBond`
- `setCustomLiveness`
- `setRefundOnDispute`
- `proposePriceFor`
- `disputePriceFor`

### requestPrice

Requests a new price. This must be for a registered price identifier. Note that this is called automatically by most financial contracts that are registered in the UMA system, but can be called by anyone for any registered price identifier. For example, the Expiring Multiparty (EMP) contract calls this method when its `expire` method is called.

Parameters:

- `identifier`: price identifier being requested.
- `timestamp`: timestamp of the price being requested.
- `ancillaryData`: ancillary data representing additional args being passed with the price request.
- `currency`: ERC20 token used for payment of rewards and fees. Must be approved for use with the DVM.
- `reward`: reward offered to a successful proposer. Will be paid by the caller. Note: this can be 0.

### proposePrice

Proposes a price value for an existing price request.

Parameters:

- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.
- `proposedPrice`: price being proposed.

### disputePrice

Disputes a price value for an existing price request with an active proposal.

Parameters:

- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### settle

Attempts to settle an outstanding price request. Will revert if it can’t be settled.

Parameters:

- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### hasPrice

Checks if a given request has resolved or been settled (i.e the optimistic oracle has a price).

Parameters:

- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### getRequest

Gets the current data structure containing all information about a price request.

Parameters:

- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### settleAndGetPrice

Retrieves a price that was previously requested by a caller. Reverts if the request is not settled or settleable. Note: this method is not view so that this call may actually settle the price request if it hasn’t been settled.

Parameters:

- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### setBond

Set the proposal bond associated with a price request.

Parameters:

- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.
- `bond`: custom bond amount to set.

### setCustomLiveness

Sets a custom liveness value for the request. Liveness is the amount of time a proposal must wait before being auto-resolved.

Parameters:

- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.
- `customLiveness`: new custom liveness.

### setRefundOnDispute

Sets the request to refund the reward if the proposal is disputed. This can help to "hedge" the caller in the event of a dispute-caused delay. Note: in the event of a dispute, the winner still receives the other’s bond, so there is still profit to be made even if the reward is refunded.

Parameters:

- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### disputePriceFor

Disputes a price request with an active proposal on another address' behalf. Note: this address will receive any rewards that come from this dispute. However, any bonds are pulled from the caller.

Parameters:

- `disputer`: address to set as the disputer.
- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.

### proposePriceFor

Proposes a price value on another address' behalf. Note: this address will receive any rewards that come from this proposal. However, any bonds are pulled from the caller.

Parameters:

- `proposer`: address to set as the proposer.
- `requester`: sender of the initial price request.
- `identifier`: price identifier to identify the existing request.
- `timestamp`: timestamp to identify the existing request.
- `ancillaryData`: ancillary data of the price being requested.
- `proposedPrice`: price being proposed.

## Integrating the optimistic oracle

This demo will set up an `OptimisticDepositBox` contract which custodies a user’s ERC-20 token balance.

On a local testnet blockchain, the user will deposit wETH (Wrapped Ether) into the contract and withdraw wETH denominated in USD. For example, if the user wants to withdraw $10,000 USD of wETH, and the ETH/USD exchange rate is $2,000, they would withdraw 5 wETH.

- The user links the `OptimisticDepositBox` with one of the price identifiers enabled on the DVM.

- The user deposits wETH into the `OptimisticDepositBox` and register it with the `ETH/USD` price identifier.

- The user can now withdraw a USD-denominated amount of wETH from their `DepositBox` via smart contract calls, with the Optimistic Oracle enabling optimistic on-chain pricing.

In this example, the user would not have been able to transfer USD-denominated amounts of wETH without referencing an off-chain `ETH/USD` price feed. The Optimistic Oracle therefore enables the user to "pull" a reference price.

Unlike price requests to the DVM, a price request to the Optimistic Oracle can be resolved within a specified liveness window if there are no disputes, which can be significantly shorter than the DVM voting period. The liveness window is configurable, but is typically two hours, compared to 2-3 days for settlement via the DVM.

The price requester is not currently required to pay fees to the DVM. The requester can offer a reward for the proposer who responds to a price request, but the reward value is set to `0` in this example.

The price proposer posts a bond along with their price, which will be refunded if the price is not disputed, or if a dispute is resolved in the proposer's favor. Otherwise, this bond is used to pay the final fee to the DVM and pay a reward to a successful disputer.

In the demo, the requester does not require an additional bond from the price proposer, so the total bond posted is equal to the wETH final fee currently 0.2 wETH. See the `proposePriceFor` function in the `OptimisticOracle` [contract](https://docs-dot-uma-protocol.appspot.com/uma/contracts/OptimisticOracle.html) for implementation details.

## Running the demo

1. Ensure that you have followed all the prerequisite setup steps [here](https://docs.umaproject.org/developers/setup).
2. Run a local Ganache instance (i.e. not Kovan/Ropsten/Rinkeby/Mainnet) with `yarn ganache-cli --port 9545`
3. In another window, migrate the contracts by running the following command:

  ```bash
  yarn truffle migrate --reset --network test
  ```

1. To deploy the `OptimisticDepositBox` [contract](https://github.com/UMAprotocol/dev-quickstart/blob/main/contracts/OptimisticDepositBox.sol) and go through a simple user flow, run the following demo script from the root of the repo:

```bash
yarn truffle exec ./packages/core/scripts/demo/OptimisticDepositBox.js --network test
```

You should see the following output:

```
1. Deploying new OptimisticDepositBox
  - Using wETH as collateral token
  - Pricefeed identifier for ETH/USD is whitelisted
  - Collateral address for wETH is whitelisted
  - Deployed an OptimisticOracle
  - Deployed a new OptimisticDepositBox


2. Minting ERC20 to user and giving OptimisticDepositBox allowance to transfer collateral
  - Converted 10 ETH into wETH
  - User's wETH balance: 10
  - Increased OptimisticDepositBox allowance to spend wETH
  - Contract's wETH allowance: 10


3. Depositing ERC20 into the OptimisticDepositBox
  - Deposited 10 wETH into the OptimisticDepositBox
  - User's deposit balance: 10
  - Total deposit balance: 10
  - User's wETH balance: 0


4. Withdrawing ERC20 from OptimisticDepositBox
  - Submitted a withdrawal request for 10000 USD of wETH
  - Proposed a price of 2000000000000000000000 ETH/USD
  - Fast-forwarded the Optimistic Oracle and Optimistic Deposit Box to after the liveness window so we can settle.
  - New OO time is [fast-forwarded timestamp]
  - New ODB time is [fast-forwarded timestamp]
  - Executed withdrawal. This also settles and gets the resolved price within the withdrawal function.
  - User's deposit balance: 5
  - Total deposit balance: 5
  - User's wETH balance: 5
```

## Explaining the contract functions

The `OptimisticDepositBox` [contract code](https://github.com/UMAprotocol/dev-quickstart/blob/main/contracts/OptimisticDepositBox.sol) shows how to interact with the Oracle.

The `constructor` function includes a `_finderAddress` argument for the UMA `Finder` contract, which maintains a registry of the `OptimisticOracle` address, approved collateral and price identifier whitelists, and other important contract addresses.

This allows the `constructor` to check that the collateral type and price identifier are valid, and allows the `OptimisticDepositBox` to find and interact with the `OptimisticOracle` later.

The `requestWithdrawal` function includes an internal call to the `OptimisticOracle` requesting the `ETH/USD` price. Once it's returned, the user can call `executeWithdrawal` to complete the withdrawal.

There is much more information and explanation in the code comments, so please take a look if you're interested in learning more.

## Additional resources

Here are some additional resources regarding the UMA DVM:

- [Technical architecture](https://docs.umaproject.org/oracle/tech-architecture).
- [Economic architecture](https://docs.umaproject.org/oracle/econ-architecture).
- [Blog post](https://medium.com/uma-project/umas-data-verification-mechanism-3c5342759eb8) on UMA’s DVM design.
- [Whitepaper](https://github.com/UMAprotocol/whitepaper/blob/master/UMA-DVM-oracle-whitepaper.pdf) on UMA’s DVM design.
- [Research repo](https://github.com/UMAprotocol/research) for optimal fee policy.
- [UMIP repo](https://github.com/UMAprotocol/UMIPs) for governance proposals.
