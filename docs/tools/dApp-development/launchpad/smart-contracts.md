<!--
---
comments: true
---
-->

## Environment variables

Make sure you have followed the [steps in the quickstart](quickstart.md#set-up-environment-variables).

## Framework

The smart contracts run on a [Hardhat](https://hardhat.org/) environment. They are written in [Solidity](https://docs.soliditylang.org/) and reside in the `smart-contracts` directory.

Tests are written in JavaScript and TypeScript, and are in the `tests` directory. An example test is available.

Scripts are also written in JavaScript and TypeScript, and reside in the `scripts` directory. Some mandatory scripts are already there to get started with.

## Deploying on local test chain

Follow the [start developing instructions](quickstart.md#start-developing) to spin up a local chain.

For all available options run:

```sh
dapp-launchpad dev -h
```

Internally, the [`dev`](commands.md#dev) command runs the `scripts/deploy_localhost` script that deploys all contracts in the correct sequence. 

!!! warning
    When working on your own smart contracts, make sure to update this script.

## Local test chain explorer with Ethernal

Optionally, you can enable a local blockchain explorer, which auto-indexes all transactions, and provides a feature-loaded dashboard with an overview of the chain.

### Prerequisite steps

To run the explorer, you first have to:

- Sign up on [Ethernal](https://app.tryethernal.com/), and create a workspace. 
- Then, add your login email, password, and workspace details in the `.env` file in the `smart-contracts` directly.

Check and set the configs with [`dev`](commands.md#dev) command params `--ethernal-login-email`, `--ethernal-login-password` and `--ethernal-workspace`, which override the preset environment variables.

### Run the local block explorer

To use it, run the [`dev`](commands.md#dev) command with `-e`.

Access the chain explorer at the [Ethernal](https://app.tryethernal.com/) URL.

## Deploying to production

The [`deploy`](commands.md#deploy) command automates deploying to any EVM compatible chain. It runs the provided `scripts/deploy_prod` script to deploy all contracts in the correct sequence. When working on your own smart contracts, make sure to update this script.

For all available options run:

```sh
dapp-launchpad dev -h
```