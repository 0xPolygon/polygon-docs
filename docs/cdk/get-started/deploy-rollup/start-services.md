## Run the docker-compose file

From the `zkevm` root, run the following:

```sh
docker-compose -f mainnet/docker-compose.yaml up
```

## Logs

??? "Logs sample"
        zkevm-rpc         | Version:      v0.4.4
        zkevm-rpc         | Git revision: 9ef6f20
        zkevm-rpc         | Git branch:   HEAD
        zkevm-rpc         | Go version:   go1.21.5
        zkevm-rpc         | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-rpc         | OS/Arch:      linux/amd64
        zkevm-rpc         | 2024-01-18T17:07:55.195Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | 2024-01-18T17:07:55.205Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | Version:      v0.4.4
        zkevm-sync        | Git revision: 9ef6f20
        zkevm-sync        | Git branch:   HEAD
        zkevm-sync        | Go version:   go1.21.5
        zkevm-sync        | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-sync        | OS/Arch:      linux/amd64
        zkevm-sync        | 2024-01-18T17:07:55.318Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:07:55.318Z INFO cmd/run.go:274 running migrations for zkevm-state-db {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:07:55.318Z INFO db/db.go:47 running migrations up {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:07:55.328Z INFO db/db.go:83 successfully ran 0 migrations {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:07:55.336Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | 2024-01-18T17:07:55.887Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-rpc         | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-rpc         | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-rpc         | /src/cmd/run.go:115 main.start()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-rpc         | /src/cmd/main.go:191 main.main()
        zkevm-rpc         | /usr/local/go/src/runtime/proc.go:267 runtime.main()
        zkevm-rpc         | {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | main.start
        zkevm-rpc         | /src/cmd/run.go:115
        zkevm-rpc         | github.com/urfave/cli/v2.(*Command).Run
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
        zkevm-sync        | 2024-01-18T17:07:55.916Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-sync        | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-sync        | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-sync        | /src/cmd/run.go:115 main.start()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-sync        | /src/cmd/main.go:191 main.main()
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267 runtime.main()
        zkevm-sync        | {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | main.start
        zkevm-sync        | /src/cmd/run.go:115
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267
        zkevm-sync        | github.com/urfave/cli/v2.(*App).RunContext
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332
        zkevm-sync        | github.com/urfave/cli/v2.(*App).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309
        zkevm-sync        | main.main
        zkevm-sync        | /src/cmd/main.go:191
        zkevm-sync        | runtime.main
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267
        zkevm-sync exited with code 1
        zkevm-rpc exited with code 1
        zkevm-sync        | Version:      v0.4.4
        zkevm-sync        | Git revision: 9ef6f20
        zkevm-sync        | Git branch:   HEAD
        zkevm-sync        | Go version:   go1.21.5
        zkevm-sync        | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-sync        | OS/Arch:      linux/amd64
        zkevm-sync        | 2024-01-18T17:08:56.244Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:08:56.244Z INFO cmd/run.go:274 running migrations for zkevm-state-db {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:08:56.244Z INFO db/db.go:47 running migrations up {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | Version:      v0.4.4
        zkevm-rpc         | Git revision: 9ef6f20
        zkevm-rpc         | Git branch:   HEAD
        zkevm-rpc         | Go version:   go1.21.5
        zkevm-rpc         | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-rpc         | OS/Arch:      linux/amd64
        zkevm-rpc         | 2024-01-18T17:08:56.244Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | 2024-01-18T17:08:56.255Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:08:56.255Z INFO db/db.go:83 successfully ran 0 migrations {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:08:56.263Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | 2024-01-18T17:08:56.920Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-rpc         | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-rpc         | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-rpc         | /src/cmd/run.go:115 main.start()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-rpc         | /src/cmd/main.go:191 main.main()
        zkevm-rpc         | /usr/local/go/src/runtime/proc.go:267 runtime.main()
        zkevm-rpc         | {"pid": 1, "version": "v0.4.4"}
        zkevm-rpc         | main.start
        zkevm-rpc         | /src/cmd/run.go:115
        zkevm-rpc         | github.com/urfave/cli/v2.(*Command).Run
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
        zkevm-sync        | 2024-01-18T17:08:56.928Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-sync        | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-sync        | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-sync        | /src/cmd/run.go:115 main.start()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-sync        | /src/cmd/main.go:191 main.main()
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267 runtime.main()
        zkevm-sync        | {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | main.start
        zkevm-sync        | /src/cmd/run.go:115
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267
        zkevm-sync        | github.com/urfave/cli/v2.(*App).RunContext
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332
        zkevm-sync        | github.com/urfave/cli/v2.(*App).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309
        zkevm-sync        | main.main
        zkevm-sync        | /src/cmd/main.go:191
        zkevm-sync        | runtime.main
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267
        zkevm-sync exited with code 1
        zkevm-rpc exited with code 1
        zkevm-pool-db     | 2024-01-18 17:09:51.816 UTC [63] LOG:  checkpoint starting: time
        zkevm-state-db    | 2024-01-18 17:09:52.078 UTC [66] LOG:  checkpoint starting: time
        zkevm-pool-db     | 2024-01-18 17:09:55.952 UTC [63] LOG:  checkpoint complete: wrote 44 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.115 s, sync=0.015 s, total=4.136 s; sync files=12, longest=0.013 s, average=0.002 s; distance=252 kB, estimate=252 kB
        zkevm-rpc         | 2024-01-18T17:09:57.402Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:57.402Z INFO cmd/run.go:52 Starting application {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:57.402Z INFO cmd/run.go:274 running migrations for zkevm-state-db {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:57.402Z INFO db/db.go:47 running migrations up {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | Version:      v0.4.4
        zkevm-sync        | Git revision: 9ef6f20
        zkevm-sync        | Git branch:   HEAD
        zkevm-sync        | Go version:   go1.21.5
        zkevm-sync        | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-sync        | OS/Arch:      linux/amd64
        zkevm-rpc         | Version:      v0.4.4
        zkevm-rpc         | Git revision: 9ef6f20
        zkevm-rpc         | Git branch:   HEAD
        zkevm-rpc         | Go version:   go1.21.5
        zkevm-rpc         | Built:        Tue, 12 Dec 2023 17:18:45 +0000
        zkevm-rpc         | OS/Arch:      linux/amd64
        zkevm-rpc         | 2024-01-18T17:09:57.413Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:57.413Z INFO db/db.go:83 successfully ran 0 migrations {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:57.422Z INFO db/db.go:121 Found 12 migrations as expected {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | 2024-01-18T17:09:58.066Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-sync        | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-sync        | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-sync        | /src/cmd/run.go:115 main.start()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-sync        | /src/cmd/main.go:191 main.main()
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267 runtime.main()
        zkevm-sync        | {"pid": 1, "version": "v0.4.4"}
        zkevm-sync        | main.start
        zkevm-sync        | /src/cmd/run.go:115
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274
        zkevm-sync        | github.com/urfave/cli/v2.(*Command).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267
        zkevm-sync        | github.com/urfave/cli/v2.(*App).RunContext
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332
        zkevm-sync        | github.com/urfave/cli/v2.(*App).Run
        zkevm-sync        | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309
        zkevm-sync        | main.main
        zkevm-sync        | /src/cmd/main.go:191
        zkevm-sync        | runtime.main
        zkevm-sync        | /usr/local/go/src/runtime/proc.go:267
        zkevm-rpc         | 2024-01-18T17:09:58.068Z FATAL cmd/run.go:115 no contract code at given address
        zkevm-rpc         | /src/log/log.go:142 github.com/0xPolygonHermez/zkevm-node/log.appendStackTraceMaybeArgs()
        zkevm-rpc         | /src/log/log.go:223 github.com/0xPolygonHermez/zkevm-node/log.Fatal()
        zkevm-rpc         | /src/cmd/run.go:115 main.start()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:274 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/command.go:267 github.com/urfave/cli/v2.(*Command).Run()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:332 github.com/urfave/cli/v2.(*App).RunContext()
        zkevm-rpc         | /go/pkg/mod/github.com/urfave/cli/v2@v2.25.7/app.go:309 github.com/urfave/cli/v2.(*App).Run()
        zkevm-rpc         | /src/cmd/main.go:191 main.main()