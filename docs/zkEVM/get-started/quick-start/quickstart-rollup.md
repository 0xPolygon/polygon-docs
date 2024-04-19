---
comments: true
---

This quick start guide shows you how to deploy a CDK rollup (EVM compatible) environment on your local machine.

It sets up and runs the following components:

- Prover: `zkevm-prover`
- zkEVM node components: `zkevm-sync`, `zkevm-eth-tx-manager`, `zkevm-sequencer`, `zkevm-sequence-sender`, `zkevm-l2gaspricer`, `zkevm-aggregator`, `zkevm-json-rpc`
- L1 network: `zkevm-mock-l1-network`
- zkEVM node databases: `zkevm-event-db`, `zkevm-pool-db`, `zkevm-state-db`
- Explorer databases: `zkevm-explorer-l1-db`, `zkevm-explorer-l2-db`
- Explorers: `zkevm-explorer-l1`, `zkevm-explorer-l2`, `zkevm-explorer-json-rpc`

!!! note
    - The documentation describes standard deployments. 
    - Edit the configuration files to implement your own custom setups.

## Prerequisites

### Hardware

- A Linux-based OS (e.g., Ubuntu Server 22.04 LTS).
- At least 16GB RAM with a 4-core CPU.
- An AMD64 architecture system.

!!! warning
    - Some of the components aren't set up to run on MacOS. Please check the workaround. The explorers and the bridge service probably won't come up.
    - For Windows users, WSL/WSL2 use is not recommended. 

!!! tip "MacOS workaround"
    You may see errors related to `amd64` such as:
    
    ```sh
    ⠇ zkevm-prover 
    no matching manifest for linux/arm64/v8 in the manifest list entries
    make: *** [run] Error 18
    ```

    If so, go to the `docker-compose.yml` file in the `test` directory, search for the component details - in this case `zkevm-prover`, and add the `platform: linux/amd64` environment variable under the `environment` variable (which you should also add if it is not there):

    ```sh
    environment:
      - EXPERIMENTAL_DOCKER_DESKTOP_FORCE_QEMU=1
    platform: linux/amd64
    ```

    You may find the explorer components affected similarly.

### Software

- [`go`](https://go.dev/doc/install) <sub>version 1.21</sub>
- [`Docker`](https://www.docker.com/get-started)
- [`Docker Compose`](https://docs.docker.com/compose/install/)

## 1. Clone the repo

```sh
git clone https://github.com/0xPolygonHermez/zkevm-node.git
cd zkevm-node
```

## 2. Build the Docker image

```bash
make build-docker
```

!!! warning
    - Rerun this command every time there is a code-change.

## 3. Test the environment

`zkevm-node` provides commands that allow you to interact with smart contracts, run components, create encryption files, and print out debug information.

!!! warning
    - All the data is stored inside Docker containers. 
    - You will lose all the data whenever you remove the container.

### 3.1 Run the environment

The `test/` directory contains scripts and files for developing and debugging.

```bash
cd test/
```

Then:

```bash
make run
```

The `make run` command spins up the containers that run the environment, but nothing else. This means that the L2 has no data yet.

#### Run the explorers

!!! warning
    The L2 explorer may not come up on MacOS regardless of environment variables.

You need to bring up the explorer databases and networks separately:

```sh
make run-explorer-db run-explorer
```

### 3.2 Stop the environment

```bash
make stop
```

### 3.3 Restart the environment

```bash
make restart
```

## 4. Test with sample data

### 4.1 Add example transactions and smart contracts

This example builds and deploys contracts, funds accounts, and sends some transactions.

```bash
make deploy-sc
```

You should see output similar to this:

```sh
2024-04-17T10:05:17.729+0200	INFO	deploy_sc/main.go:42	connecting to Local L1: http://localhost:8545	{"pid": 16869, "version": "v0.1.0"}
2024-04-17T10:05:17.729+0200	INFO	deploy_sc/main.go:45	connected	{"pid": 16869, "version": "v0.1.0"}
2024-04-17T10:05:17.735+0200	DEBUG	deploy_sc/main.go:54	ETH Balance for 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266: 999899846763612022461	{"pid": 16869, "version": "v0.1.0"}
2024-04-17T10:05:17.735+0200	DEBUG	deploy_sc/main.go:57	Sending TX to deploy Counter SC	{"pid": 16869, "version": "v0.1.0"}
2024-04-17T10:05:19.763+0200	DEBUG	operations/wait.go:101	Transaction successfully mined: 0xfac2ebc78eada5141cf3737fd5c6ad399d3d18ed7a026d60e87d00c2db0d6ed9	{"pid": 16869, "version": "v0.1.0"}
...
```

### 4.2 Deploy a full Uniswap environment

This example builds out a Uniswap environment which creates token contracts and deploys them, mines tokens, and performs token swaps.

```bash
make deploy-uniswap
```

You should see output similar to this:

```sh
2024-04-17T10:07:56.298+0200	DEBUG	pkg/swap.go:40	after first swap aCoin.balanceOf[0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266]: 989999999999999999950	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.301+0200	DEBUG	pkg/swap.go:43	after first swap bCoin.balanceOf[0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266]: 980000000000000000009	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.305+0200	DEBUG	pkg/swap.go:46	after first swap cCoin.balanceOf[0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266]: 990000000000000000032	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.306+0200	DEBUG	pkg/swap.go:47	Swaping tokens from B <-> C	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.307+0200	DEBUG	pkg/swap.go:62	SwapExactTokensForTokens 0x70e0bA845a1A0F2DA3359C97E0285013525FFC49 <-> 0x4826533B4897376654Bb4d4AD88B7faFD0C98528 pair: 0x09dF250580cb3ba5D061f6dfcA783cDa4caa6461	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.308+0200	DEBUG	pkg/swap.go:67	SwapExactTokensForTokens 0x70e0bA845a1A0F2DA3359C97E0285013525FFC49 <-> 0x4826533B4897376654Bb4d4AD88B7faFD0C98528 reserves 0: 9999999999999999968 1: 10000000000000000036 Block Timestamp: 1713341274	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:56.309+0200	DEBUG	pkg/swap.go:70	SwapExactTokensForTokens 0x70e0bA845a1A0F2DA3359C97E0285013525FFC49 <-> 0x4826533B4897376654Bb4d4AD88B7faFD0C98528 exactAmountIn: 9 amountOut: 8	{"pid": 17666, "version": "v0.1.0"}
2024-04-17T10:07:58.338+0200	DEBUG	operations/wait.go:101	Transaction successfully mined: 0x5c0a2fdb27f6c681b898101883f278dee1ee78dcdacb8471872e5b00603643fe	{"pid": 17666, "version": "v0.1.0"}
```

### 4.3 Grant the Pol smart contract a set amount of tokens

This sets up accounts with POL and is run as part of the previous examples.

```sh
make run-approve-pol
```

## 5. Set up MetaMask

To configure MetaMask to use your local environment, make sure the network is running and follow these steps.

1. Log in to your MetaMask wallet.
2. Click your account picture and then on **Settings**.
3. On the left menu, click **Networks**.

### Add zkEVM L2 network

- Click the **Add Network** button and **Add a network manually**.
- Enter the following L2 network information:
    1. `Network name:` Polygon zkEVM - local
    2. `New RPC URL:` <http://localhost:8123>
    3. `Chain ID:` 1001
    4. `Currency symbol:` (accept default)
    5. `Block explorer URL:` <http://localhost:4000>
- Click **Save**.

### Add Geth L1 network

- Click the **Add Network** button and **Add a network manually**.
- Enter the following L1 network information:
    1. `Network name:` Geth - local
    2. `New RPC URL:` <http://localhost:8545>
    3. `Chain ID:` 1337
    4. `Currency symbol:` ETH
- Click **Save**.

## Environment configurations

- Use the following details for the running components to set up your applications and tests.
- You can find these details in the running logs also.

### Databases

#### zkEVM node *state* database 

- `Type:` Postgres DB
- `User:` state_user
- `Password:` state_password
- `Database:` state-db
- `Host:` localhost
- `Port:` 5432
- `URL:` <postgres://state_user:srare_password@localhost:5432/state-db>

#### zkEVM node *pool* database 

- `Type:` Postgres DB
- `User:` pool_user
- `Password:` pool_password
- `Database:` pool_db
- `Host:` localhost
- `Port:` 5433
- `URL:` <postgres://pool_user:pool_password@localhost:5433/pool_db>

#### zkEVM node *JSON-RPC* database 

- `Type:` Postgres DB
- `User:` rpc_user
- `Password:` rpc_password
- `Database:` rpc_db
- `Host:` localhost
- `Port:` 5434
- `URL:` <postgres://rpc_user:rpc_password@localhost:5434/rpc_db>

#### Explorer L1 database

- `Type:` Postgres DB
- `User:` l1_explorer_user
- `Password:` l1_explorer_password
- `Database:` l1_explorer_db
- `Host:` localhost
- `Port:` 5435
- `URL:` <postgres://l1_explorer_user:l1_explorer_password@localhost:5435/l1_explorer_db>

#### Explorer L2 database

- `Type:` Postgres DB
- `User:` l2_explorer_user
- `Password:` l2_explorer_password
- `Database:` l2_explorer_db
- `Host:` localhost
- `Port:` 5436
- `URL:` <postgres://l2_explorer_user:l2_explorer_password@localhost:5436/l2_explorer_db>

### Networks

#### L1 network

- `Type:` Geth
- `Host:` localhost
- `Port:` 8545
- `URL:` <http://localhost:8545>

#### zkEVM node

- `Type:` JSON RPC
- `Host:` localhost
- `Port:` 8123
- `URL:` <http://localhost:8123>

### Explorers

#### Explorer L1
    
- `Type:` Web
- `Host:` localhost
- `Port:` 4000
- `URL:` <http://localhost:4000>

#### Explorer L2

- `Type:` Web
- `Host:` localhost
- `Port:` 4001
- `URL:` <http://localhost:4001>

#### Prover

- `Type:` Mock
- `Host:` localhost
- `Port:` Depending on the prover image, if it's mock or not: 
    - Prod prover: 50052 for Prover, 50061 for Merkle Tree, 50071 for Executor
    - Mock prover: 43061 for MT, 43071 for Executor
- `URL:` <http://localhost:50001>

### Environment addresses

The following addresses are configured into the running environment.

#### L1 addresses

| Address | Description |
|---|---|
| 0x8dAF17A20c9DBA35f005b6324F493785D239719d | Polygon zkEVM |
| 0x40E0576c0A7dff9dc460B29ba73e79aBf73dD2a9 | Polygon bridge |
| 0x5FbDB2315678afecb367f032d93F642f64180aa3 | Pol token |
| 0x8A791620dd6260079BF849Dc5567aDC3F2FdC318 | Polygon GlobalExitRootManager |
| 0xB7f8BC63BbcaD18155201308C8f3540b07f84F5e | Polygon RollupManager |

#### Deployer account

| Address | Private Key |
|---|---|
| 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 | 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 |

#### Sequencer account

| Address | Private Key |
|---|---|
| 0x617b3a3528F9cDd6630fd3301B9c8911F7Bf063D | 0x28b2b0318721be8c8339199172cd7cc8f5e273800a35616ec893083a4b32c02e |

#### Aggregator account

| Address | Private Key |
|---|---|
| 0x70997970C51812dc3A010C7d01b50e0d17dc79C8 | 0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d |

### Test accounts with funds

The environment also provides a bunch of test accounts that contain funds.

| Address | Private Key |
|---|---|
| 0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC | 0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a |
| 0x90F79bf6EB2c4f870365E785982E1f101E93b906 | 0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6 |
| 0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65 | 0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a |
| 0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc | 0x8b3a350cf5c34c9194ca85829a2df0ec3153be0318b5e2d3348e872092edffba |
| 0x976EA74026E726554dB657fA54763abd0C3a0aa9 | 0x92db14e403b83dfe3df233f83dfa3a0d7096f21ca9b0d6d6b8d88b2b4ec1564e |
| 0x14dC79964da2C08b23698B3D3cc7Ca32193d9955 | 0x4bbbf85ce3377467afe5d46f804f221813b2bb87f24d81f60f1fcdbf7cbf4356 |
| 0x23618e81E3f5cdF7f54C3d65f7FBc0aBf5B21E8f | 0xdbda1821b80551c9d65939329250298aa3472ba22feea921c0cf5d620ea67b97 |
| 0xa0Ee7A142d267C1f36714E4a8F75612F20a79720 | 0x2a871d0798f97d79848a013d4936a73bf4cc922c825d33c1cf7073dff6d409c6 |
| 0xBcd4042DE499D14e55001CcbB24a551F3b954096 | 0xf214f2b2cd398c806f84e317254e0f0b801d0643303237d97a22a48e01628897 |
| 0x71bE63f3384f5fb98995898A86B02Fb2426c5788 | 0x701b615bbdfb9de65240bc28bd21bbc0d996645a3dd57e7b12bc2bdf6f192c82 |
| 0xFABB0ac9d68B0B445fB7357272Ff202C5651694a | 0xa267530f49f8280200edf313ee7af6b827f2a8bce2897751d06a843f644967b1 |
| 0x1CBd3b2770909D4e10f157cABC84C7264073C9Ec | 0x47c99abed3324a2707c28affff1267e45918ec8c3f20b8aa892e8b065d2942dd |
| 0xdF3e18d64BC6A983f673Ab319CCaE4f1a57C7097 | 0xc526ee95bf44d8fc405a158bb884d9d1238d99f0612e9f33d006bb0789009aaa |
| 0xcd3B766CCDd6AE721141F452C550Ca635964ce71 | 0x8166f546bab6da521a8369cab06c5d2b9e46670292d85c875ee9ec20e84ffb61 |
| 0x2546BcD3c84621e976D8185a91A922aE77ECEc30 | 0xea6c44ac03bff858b476bba40716402b03e41b8e97e276d1baec7c37d42484a0 |
| 0xbDA5747bFD65F08deb54cb465eB87D40e51B197E | 0x689af8efa8c651a91ad287602527f3af2fe9f6501a7ac4b061667b5a93e037fd |
| 0xdD2FD4581271e230360230F9337D5c0430Bf44C0 | 0xde9be858da4a475276426320d5e9262ecfc3ba460bfac56360bfa6c4c28b4ee0 |
| 0x8626f6940E2eb28930eFb4CeF49B2d1F2C9C1199 | 0xdf57089febbacf7ba0bc227dafbffa9fc08a93fdc68e1e42411a14efcf23656e |
