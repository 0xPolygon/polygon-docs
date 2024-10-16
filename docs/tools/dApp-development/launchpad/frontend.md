<!--
---
comments: true
---
-->

## Framework

The frontend runs on a Next.js server. 

To get started, modify the component file at `./frontend/src/pages/index`.

!!! info
    If you're new to Next.js but know React.js, getting used to Next.js is trivial. 
    To learn more about Next.js, [read the Next.js docs](https://nextjs.org/docs).

## Environment variables

Make sure you have followed the [steps in the quickstart](quickstart.md#set-up-environment-variables).

!!! note
    All environment variable names exposed in client requests should be prefixed with `NEXT_PUBLIC_`.

## Connecting wallets

To connect a wallet, [Web3Modal v3](https://web3modal.com/) has been integrated and pre-configured for you.

Use the provided [`useWallet`](https://github.com/0xPolygon/dapp-launchpad/blob/scaffold-template/javascript/frontend/src/hooks/useWallet.js) hook to interact with Web3Modal and wallets. This contains utilities to simplify anything you need related to wallets.

## Sending transactions to smart contracts

To send transactions to either a locally deployed smart contract or a smart contract on a prod chain, use the [`useSmartContract`](https://github.com/0xPolygon/dapp-launchpad/blob/scaffold-template/javascript/frontend/src/hooks/useSmartContract.js) hook. This contains utilities that simplify getting and interacting with a Ethers.js contract instance.

When [deploying to local or production](https://0xpolygon.gitbook.io/dapp-launchpad/commands/deploy), this hook automatically uses the correct chain and contracts.

## Deploying to local test server

The [`dev`](https://0xpolygon.gitbook.io/dapp-launchpad/commands/dev) command automates everything needed for setting up a local Next.js test server.

## Deploying to Vercel

We use Vercel for deployments. Vercel offers free quotas to developers to get started.

To deploy, follow the [deployment steps](quickstart.md#deploy-your-app-to-production).

With the [`deploy`](https://0xpolygon.gitbook.io/dapp-launchpad/commands/deploy) command, the frontend deployment is fully automated. 

No pre-configuration is necessary for running the `deploy` command. You'll be taken through all relevant steps upon running it.