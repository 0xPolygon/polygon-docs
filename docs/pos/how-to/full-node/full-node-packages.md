<!--
---
comments: true
---
-->

## Overview

- Prepare the Full Node machine.
- Install Heimdall and Bor packages on the Full Node machine.
- Configure the Full node.
- Start the Full node.

!!! warning
    
    It is essential to follow the outlined sequence of actions precisely, as any deviation may lead to potential issues.


## Install packages

### Prerequisites

- One machine is needed.
- Bash is installed on the machine.

### Heimdall

- Install the default latest version of sentry for Mainnet:

    ```shell
    curl -L https://raw.githubusercontent.com/0xPolygon/install/heimdall-v2/heimdall-v2.sh | bash -s -- <version> <network> <node_type> 
    ```

    or install a specific version, node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions can be found on
    [Heimdall GitHub repository](https://github.com/0xPolygon/heimdall-v2/releases).

    ```shell
    # Example:
    # curl -L https://raw.githubusercontent.com/maticnetwork/install/heimdall-v2/heimdall-v2.sh | bash -s -- v0.2.15 mainnet validator
    ```

### Bor

- Install the default latest version of sentry for Mainnet:

    ```shell
    curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash -s -- <version> <network> <node_type> 
    ```

    or install a specific version, node type (`sentry` or `validator`), and network (`mainnet` or `amoy`). All release versions could be found on
    [Bor Github repository](https://github.com/0xPolygon/bor/releases).

    ```shell
    # Example:
    # curl -L https://raw.githubusercontent.com/0xPolygon/install/main/bor.sh | bash -s -- v2.2.9 mainnet sentry
    ```

## Configuration

### Configure Heimdall

- Initialize Heimdall configs

```shell
# For mainnet
sudo -u heimdall heimdalld init <MONIKER> --chain-id=<CHAIN_ID> --home /var/lib/heimdall
```

Where `CHAIN_ID` is `heimdallv2-80002` for `amoy` and `heimdallv2-137` for `mainnet`

Then, edit the configuration files under `/var/lib/heimdall/config`  
The templates for each supported network are available [here](https://github.com/0xPolygon/heimdall-v2/tree/develop/packaging/templates/config)  
Download the `genesis.json` file and place it under `/var/lib/heimdall/config/`
Use the following commands based on your target network:
```bash
cd /var/lib/heimdall/config
curl -fsSL <BUCKET_URL> -o genesis.json
```

Where `BUCKET_URL` is

- https://storage.googleapis.com/amoy-heimdallv2-genesis/migrated_dump-genesis.json for amoy
- https://storage.googleapis.com/mainnet-heimdallv2-genesis/migrated_dump-genesis.json for mainne


- You will need to change a few details in the config files.  
- Templates for each supported network are available [here](https://github.com/0xPolygon/heimdall-v2/tree/develop/packaging/templates/config)

### Configure service files for Bor and Heimdall

After successfully installing Bor and Heimdall through [packages](#install-packages), their service file could be found under `/lib/systemd/system`, and Bor's config file could be found under `/var/lib/bor/config.toml`.
You will need to check and modify these files accordingly.

- Make sure the chain is set correctly in `/lib/systemd/system/heimdalld.service` file. Open the file with following command `sudo vi /lib/systemd/system/heimdalld.service`

    - In the service file, set `--chain` to `mainnet` or `amoy` accordingly

Save the changes in `/lib/systemd/system/heimdalld.service`.

- Make sure the chain is set correctly in `/var/lib/bor/config.toml` file. Open the file with following command `sudo vi /var/lib/bor/config.toml`

    - In the config file, set `chain` to `mainnet` or `amoy` accordingly.

    - To enable Archive mode you can optionally enable the following flags:

      ```js
      gcmode "archive"

      [jsonrpc]
        [jsonrpc.ws]
          enabled = true
          port = 8546
          corsdomain = ["*"]
      ```

Save the changes in `/var/lib/bor/config.toml`.

## (Optional) Start Heimdall from snapshot

In case you want to start Heimdall from a snapshot,  
you can download it, and extract in the `data` folder.
Examples of snapshots can be found here https://all4nodes.io/Polygon, and they are managed by the community.

e.g.:
```bash
lz4 -dc polygon-heimdall-24404501-25758577.tar.lz4 | tar -x
```

## Start services

Reloading service files to make sure all changes to service files are loaded correctly.

```shell
sudo systemctl daemon-reload
```

Verify the installation by checking the Heimdall version on your machine:

```bash
heimdalld version
```

It should return the version of Heimdall you installed.

Start Heimdall, Heimdall rest server, and Heimdall bridge.

```shell
sudo service heimdalld start
```

You can also check Heimdall logs with the following command:

```shell
journalctl -u heimdalld.service -f
```

!!! warning
    At this point, please make sure that *Heimdall is synced completely*, and only then start Bor. If you start Bor without Heimdall syncing completely, you will run into issues frequently.

To check if Heimdall is synced:

- On the remote machine/VM, run `curl localhost:26657/status`
- In the output, `catching_up` value should be `false`

Now, once Heimdall is synced, run:

```shell
sudo service bor start
```

You can check Bor logs using the following command:

```shell
journalctl -u bor.service -f
```
