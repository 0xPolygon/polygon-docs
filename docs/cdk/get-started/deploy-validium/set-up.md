## Download the `cdk-validium-contracts`

1. Create a new directory to store the `cdk-validium-contracts` and the `cdk-validium-node` and cd into it.

    ```bash
    mkdir cdk-validium
    cd cdk-validium/
    ```

2. Download the `0.0.2` release from the [cdk-validium-contracts github repo](https://github.com/0xPolygon/cdk-validium-contracts/releases/tag/v0.0.2-RC1).

    !!! note
        It is available in both `.tar.gz` and `.zip` formats

    ```bash
    ~/cdk-validium % curl -L -o cdk-validium-contracts.tar.gz https://github.com/0xPolygon/cdk-validium-contracts/archive/refs/tags/v0.0.2.tar.gz

    tar -xzf cdk-validium-contracts.tar.gz
    ```

## Prepare the environment

`cd` into `cdk-validium-contracts-0.0.2/`

```bash
~/cdk-validium % cd cdk-validium-contracts-0.0.2/
```

### Install the dependencies

```bash
~/cdk-validium/cdk-validium-contracts-0.0.2 % npm install
```

### Create the .env configuration

1. Copy the environment configuration example file into a new `.env` file.

    ```bash
    ~/cdk-validium/cdk-validium-contracts-0.0.2 % cp .env.example .env
    ```

2. The file requires the following environment variables.

    ```bash
    # ~/cdk-validium/cdk-validium-contracts-0.0.2/.env
    MNEMONIC="<generated mnemonic>"  # see instructions below
    INFURA_PROJECT_ID="<INFURA_PROJECT_ID>"  # Generate a project id on [Infura](https://www.infura.io/)
    ETHERSCAN_API_KEY="<ETHERSCAN_API_KEY>" # Generate a project id on [Etherscan](https://etherscan.io)
    ```

3. Generate a new mnemonic using `cast`.

    ```bash
    cast wallet new-mnemonic --words 12
    ```

    *note: if command **`new-mnemonic`** is not found, update foundry using **`foundryup`***

    The output should look something like this:

    ```bash
    Phrase:
    island debris exhaust typical clap debate exhaust little verify mean sausage entire
    Accounts:
    - Account 0:
    Address:     0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE
    Private key: 0x3b01870a8449ada951f59c0275670bea1fc145954ee7cb1d46f7d21533600726
    ```

4. Copy and paste the newly generated `Phrase` into the `MNEMONIC` field inside `.env`


5. Load the variables into `/tmp/cdk.env`. This is an important step and allows us to use `jq` and `tomlq` later on to setup our configuration files.

    ```bash
    # /tmp/cdk/.env
    TEST_ADDRESS=0x8Ea797e7f349dA91078B1d833C534D2c392BB7FE
    TEST_PRIVATE_KEY=0x3b01870a8449ada951f59c0275670bea1fc145954ee7cb1d46f7d21533600726 
    L1_URL=https://sepolia.infura.io/v3/<YOUR INFURA PROJECT ID>
    L1_WS_URL=wss://sepolia.infura.io/ws/v3/<YOUR INFURA PROJECT ID>
    ```
