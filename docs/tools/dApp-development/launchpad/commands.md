---
comments: true
---

## `init`

Initializes a new project in a new directory which has the same name as the project. If a project name is not mentioned, a random one is chosen.

```sh
dapp-launchpad init [PROJECT-NAME]
```

### Options

|         Option        |     Description                        |
|:---------------------:|----------------------------------------|
| -t, --template [NAME] | Name of the scaffold template to use; default: "javascript". To get list of available templates, run list scaffold-templates. (default: "javascript") |
| -h, --help            | display help for command               |

### Help

```sh
dapp-launchpad init -h
```

## `dev`

Starts a local dev environment; a local blockchain (Hardhat) and a local front end (Next.js) server.

```sh
dapp-launchpad dev [options]
```

The `dev` command starts 

### Options

| Option                               | Description                                                                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -n, --fork-network-name [NAME]       | Name of the network to fork; optional. By default, it starts a new chain from genesis block. (choices: "ethereum", "goerli", "polygonPos", "polygonAmoy", "polygonZkevm", "polygonZkevmTestnet")             |
| -b, --fork-block-num [number]        | Block number to fork at. By default, it's the latest block.                                                                                                                                                    |
| -r, --reset-on-change                | Resets the entire local blockchain when any code is changed; for forked mode, it resets back to forked block number; NOT DEFAULT.                                                                              |
| --only-smart-contracts               | Deploys only smart contracts (having started local test chain) and updates Smart contract configs for frontend; does not start frontend dev environment.                                                       |
| --only-frontend                      | Deploys only frontend (having started local server); does not start local blockchain. Smart contracts data is read from pre-existing configs. To generate these manually, use generate smart-contracts-config. |
| -e, --enable-explorer                | Sets up a chain explorer for the local test blockchain started; NOT DEFAULT; sign up at https://app.tryethernal.com/.                                                                                          |
| --ethernal-login-email [EMAIL]       | Ethernal login email; needed only if --explorer is enabled. This overrides env variable ETHERNAL_EMAIL if present.                                                                                             |
| --ethernal-login-password [PASSWORD] | Ethernal login password; needed only if --explorer is enabled. This overrides env variable ETHERNAL_PASSWORD if present.                                                                                       |
| --ethernal-workspace [WORKSPACE]     | Ethernal workspace name; needed only if --explorer is enabled. This overrides env variable ETHERNAL_WORKSPACE if present.                                                                                      |
| -h, --help                           | Display help for command                                                                                                                                                                                       |

### Help

```sh
dapp-launchpad dev -h
```

## `deploy`

The deploy command deploys the smart contracts and frontend app to production.

```sh
dapp-launchpad deploy -n CHAIN_NAME
```

### Options

|        Option         |        Description         |
|:----------------------:|:-------------------------------------------------------|
| -n, --network-name     | Name of the network to deploy smart contracts to. (choices: "ethereum", "goerli", "polygonPos", "polygonAmoy", "polygonZkevm", "polygonZkevmTestnet")               |
| --only-smart-contracts | Deploys only smart contracts and updates Smart contracts config for frontend.                                                                                         |
| --only-frontend        | Deploys only frontend; smart contracts data is read from Smart contracts config which must pre-exist. To generate these manually, use generate smart-contracts-config |
| -h, --help             | Display help for command                                                                                                                                              |

### Help

```sh
dapp-launchpad deploy -h
```

## `list`

List options.

```sh
dapp-launchpad list <WHAT TO LIST>
```

### `scaffold-templates`

List the available scaffold template languages.

```sh
dapp-launchpad list scaffold-templates
```

## `generate`

Generate the specified.

```sh
dapp-launchpad generate <WHAT TO GENERATE>
```

### `smart-contracts-config`

Generate the smart contract configuration.

```sh
dapp-launchpad generate smart-contracts-config
```

### Options

|          Option         |                         Description      |
|:-----------------------:|:-----------------------------------------|
| -e, --environment <ENV> | Environment where this config would be used (choices: "development", "production", default: "development")                                        |
| -n, --network-name      | Name of the network to generate config for. (choices: "ethereum", "goerli", "polygonPos", "polygonAmoy", "polygonZkevm", "polygonZkevmTestnet") |
| -h, --help              | Display help for command                  |