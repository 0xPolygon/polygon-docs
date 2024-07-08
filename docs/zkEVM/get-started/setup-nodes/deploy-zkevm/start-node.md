---
comments: true
---

## Start node

From the `zkevm` root directory, run the following:

```sh
sudo docker compose -f mainnet/docker-compose.yml up
```

This command spins up the following services:

- RPC node
- Synchronizer
- State DB
- Pool DB
- Mock prover

## Log sample

???     "Logs sample"
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274
        zkevm-rpc         | github.com/urfave/cli/v2.(*Command).Run
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267
        zkevm-rpc         | github.com/urfave/cli/v2.(*App).RunContext
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332
        zkevm-rpc         | github.com/urfave/cli/v2.(*App).Run
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309
        zkevm-rpc         | main.main
        zkevm-rpc         | /src/cmd/main.go:191
        zkevm-rpc         | runtime.main
        zkevm-rpc         | /usr/local/go/src/runtime/proc.go:267
        zkevm-rpc         | 2024-01-24T11:32:03.043Z INFO config/config.go:163 config file not found {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | Version:      v0.4.4
        zkevm-rpc         | 2024-01-24T11:32:03.045Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | Git revision: 9ef6f20
        zkevm-rpc         | Git branch:   HEAD
        zkevm-rpc         | Go version:   go1.21.5
        zkevm-rpc         | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-rpc         | OS/Arch:      linux/amd64
        zkevm-rpc         | 2024-01-24T11:32:03.054Z ERROR db/db.go:117 error getting migrations count: ERROR: relation "public.gorp_migrations" does not exist (SQLSTATE 42P01)
        zkevm-rpc         | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-rpc         | /src/log/log.go:217 github.com/0xPolygonHermez/zkevm-node/log.Error()
        zkevm-rpc         | /src/db/db.go:117 github.com/0xPolygonHermez/zkevm-node/db.checkMigrations()
        zkevm-rpc         | /src/db/db.go:53 github.com/0xPolygonHermez/zkevm-node/db.CheckMigrations()
        zkevm-rpc         | /src/cmd/run.go:263 main.checkStateMigrations()
        zkevm-rpc         | /src/cmd/run.go:70 main.start()
        zkevm-state-db    | 2024-01-24 13:49:21.909 UTC [78] ERROR:  relation "public.gorp_migrations" does not exist at character 22

## Troubleshooting

### Configuration issues

If you have errors related to configuration issues, see the warning at step 4 in the [configure node deployment](configure-node-deployment.md#set-up) section.

### Process binding issue

If you  need to restart, make sure you kill any hanging db processes with the following commands.

!!! info
    You can find the port number from the log warnings.

```sh
sudo lsof -t -i:<DB_PORT>
kill -9 <PID>
```

### Kill all Docker containers and images 

You can fix many restart issues and persistent errors by stopping and deleting all Docker containers and images.

```sh
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
```
