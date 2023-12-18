Heimdall's governance operates identically to the Cosmos-sdk `x/gov` module, as detailed in [Cosmos-sdk documentation](https://docs.cosmos.network/main/build/modules/gov).

## Overview

In Heimdall, token holders can influence decisions by voting on proposals. Each token equals one vote. The governance system currently supports:

- **Proposal submission:** Validators can submit proposals along with a deposit. If the deposit reaches the minimum threshold within a set period, the proposal moves to a voting phase. Validators can reclaim their deposits after the proposal's acceptance or rejection.
- **Voting:** Validators are eligible to vote on proposals that have met the minimum deposit requirement.

The governance module includes two critical periods: the deposit and voting periods. Proposals failing to meet the minimum deposit by the end of the deposit period are automatically rejected. Upon reaching the minimum deposit, the voting period commences, during which validators cast their votes. After the voting period, the `gov/Endblocker.go` script tallies the votes and determines the proposal's fate based on `tally_params`: quorum, threshold, and veto. The tallying process is detailed in the source code at [Heimdall GitHub repository](https://github.com/maticnetwork/heimdall/blob/develop/gov/endblocker.go).

### Types of proposals

Currently, Heimdall supports the **Param Change Proposal**, allowing validators to modify parameters in any of Heimdall's modules.

#### Param Change Proposal example

For instance, validators might propose to alter the minimum `tx_fees` in the `auth` module. If the proposal is approved, the parameters in the Heimdall state are automatically updated without the need for an additional transaction.

## Command Line Interface (CLI) commands

### Checking governance parameters

To view all parameters for the governance module:

```go
heimdallcli query gov params --trust-node
```

This command displays the current governance parameters, such as voting period, quorum, threshold, veto, and minimum deposit requirements.

### Submitting a proposal

To submit a proposal:

```bash
heimdallcli tx gov submit-proposal \
 --validator-id 1 param-change proposal.json \
 --chain-id <heimdall-chain-id>
```

`proposal.json` is a JSON-formatted file containing the proposal details.

### Querying proposals

To list all proposals:

```go
heimdallcli query gov proposals --trust-node
```

To query a specific proposal:

```go
heimdallcli query gov proposal 1 --trust-node
```

### Voting on a proposal

To vote on a proposal:

```bash
heimdallcli tx gov vote 1 "Yes" --validator-id 1 --chain-id <heimdall-chain-id>
```

Votes are automatically tallied after the voting period concludes.

## REST APIs

Heimdall also offers REST APIs for interacting with the governance system:

| Name | Method | Endpoint |
| ---- | ------ | -------- |
| Get all proposals | GET | `/gov/proposals` |
| Get proposal details | GET | `/gov/proposals/{proposal-id}` |
| Get all votes for a proposal | GET | `/gov/proposals/{proposal-id}/votes` |

These APIs facilitate access to proposal details, voting records, and overall governance activity.
