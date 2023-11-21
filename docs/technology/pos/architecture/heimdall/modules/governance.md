---
id: governance
title: Governance
sidebar_label: Governance
description: System with a 1 token - 1 vote basis
keywords:
  - docs
  - matic
  - one token
  - one vote
  - governance
  - heimdall
image: https://matic.network/banners/matic-network-16x9.png 
---

# Governance

Heimdall governance works exactly the same as [Cosmos-sdk `x/gov` module](https://docs.cosmos.network/master/modules/gov/).

In this system, holders of the native staking token of the chain can vote on proposals on a `1 token = 1 vote` basis. Here is a list of features the module currently supports:

- **Proposal submission:** Validators can submit proposals with a deposit. Once the minimum deposit is reached, proposal enters voting period. Valdiators that deposited on proposals can recover their deposits once the proposal is rejected or accepted.
- **Vote:** Validators can vote on proposals that reached MinDeposit.

There are deposit period and voting period as params in `gov` module. Minimum deposit has to be achieved before deposit period ends, otherwise proposal will be automatically rejected. 

Once minimum deposits reached within deposit period, voting period starts. In voting period, all validators should vote their choices for the proposal. After voting period ends, `gov/Endblocker.go` executes `tally`  function and accepts or rejects proposal based on `tally_params` — `quorum`, `threshold` and `veto`. 

Source: [https://github.com/maticnetwork/heimdall/blob/develop/gov/endblocker.go](https://github.com/maticnetwork/heimdall/blob/develop/gov/endblocker.go)

There are different types of proposals that can be implemented in Heimdall. As of now, it supports only the **Param change proposal**.

### Param change proposal

Using this type of proposal, validators can change any `params` in any `module` of Heimdall.

Example: change minimum `tx_fees` for the transaction in `auth` module. When the proposal gets accepted, it automatically changes the `params` in Heimdall state. No extra TX is needed. 

## CLI Commands

### Query gov params

```go
heimdallcli query gov params --trust-node
```

This shows all params for governance module.

```go
voting_params:
  voting_period: 48h0m0s
tally_params:
  quorum: "334000000000000000"
  threshold: "500000000000000000"
  veto: "334000000000000000"
deposit_parmas:
  min_deposit:
  - denom: matic
    amount:
      i: "10000000000000000000"
  max_deposit_period: 48h0m0s
```

### Submit proposal

```bash
heimdallcli tx gov submit-proposal \
	--validator-id 1 param-change proposal.json \
	--chain-id <heimdall-chain-id>
```

`proposal.json` is a file which includes proposal in json format.

```json
{
  "title": "Auth Param Change",
  "description": "Update max tx gas",
  "changes": [
    {
      "subspace": "auth",
      "key": "MaxTxGas",
      "value": "2000000"
    }
  ],
  "deposit": [
    {
      "denom": "matic",
      "amount": "1000000000000000000"
    }
  ]
}
```

### Query proposal

To query all proposals:

```go
heimdallcli query gov proposals --trust-node
```

To query a particular proposal:

```go
heimdallcli query gov proposals 1 --trust-node
```

### Vote on proposal

To vote on a particular proposal:

```bash
heimdallcli tx gov vote 1 "Yes" --validator-id 1  --chain-id <heimdal-chain-id>
```

Proposal will be automatically tallied after voting period.

## REST APIs

|Name                  |Method|Endpoint          |
|----------------------|------|------------------|
|Get all proposals     |GET   |/gov/proposals    |
|Get proposal details  |GET   |/gov/proposals/`proposal-id`|
|Get all votes for the proposal|GET   |/gov/proposals/`proposal-id`/votes|
