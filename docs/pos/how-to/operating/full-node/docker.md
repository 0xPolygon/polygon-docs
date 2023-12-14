Polygon provides official Docker images for setting up nodes on the Polygon Mainnet. This guide details the process for running a Full Node, with the flexibility to adapt these instructions for sentry nodes and validators.

## Prerequisites

To run a Polygon full node, your machine should meet these minimum specifications:

- **CPU and RAM**: At least 4 CPUs/cores and 16 GB of RAM. In this guide, we use an AWS `t3.2xlarge` instance, suitable for both x86 and ARM architectures.
- **Operating System**: This guide is based on Docker, compatible with most operating systems, but we'll focus on Ubuntu for simplicity.
- **Storage Requirements**: For a full node, expect to need between 2.5 to 5 terabytes of SSD storage, or faster.
- **Network Configuration**: Polygon full nodes typically require ports 30303 and 26656 to be open. Ensure these ports are accessible in your firewall or AWS security group settings.

Summary:

- Ensure a minimum of 4 cores and 16GB RAM.
- Have 2.5 TB to 5 TB of high-speed storage.
- Use a public IP and open ports 30303 and 26656.

## Initial setup

You should have root-level shell access to a Linux machine.

### Installing Docker

Your operating system likely doesn't include Docker by default. Follow these steps to install Docker, consulting the [official Docker installation guide](https://docs.docker.com/engine/install/) for the latest instructions:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Verify the installation:

```bash
sudo docker run hello-world
```

For convenience, configure Docker to run without requiring `sudo`:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Logout and log back in to apply these changes.

### Disk setup

The specific steps for disk setup will vary. Typically, you'll have a root partition for the OS and separate devices for blockchain data. For this guide, we'll assume an additional device mounted at `/mnt/data`.

Example setup with a 4 TB device at `/dev/nvme1n1`:

```bash
sudo mkdir /mnt/data
sudo mount /dev/nvme1n1 /mnt/data
```

Use `df -h` to verify the mount. Then, create directories for Bor and Heimdall:

```bash
sudo mkdir /mnt/data/bor
sudo mkdir /mnt/data/heimdall
```

To ensure the device mounts on reboot, add it to `/etc/fstab`:

1. Obtain the UUID with `blkid`.
2. Edit `/etc/fstab` and add a line for your device, e.g., `UUID={your uuid} /mnt/data {your filesystem} defaults 0 1`.
3. Use `sudo emacs /etc/fstab` to edit the file.
4. Verify with `sudo findmnt --verify --verbose`.

Reboot to confirm the proper loading of your mount.

### Heimdall setup

With Docker running and storage prepared, it's time to set up Heimdall:

1. Test Heimdall with Docker:

      ```bash
         docker run -it 0xpolygon/heimdall:1.0.3 heimdallcli version
      ```

   2. Initialize Heimdall's home directory:

      ```bash
         docker run -v /mnt/data/heimdall:/heimdall-home:rw --entrypoint /usr/bin/heimdalld -it 0xpolygon/heimdall:1.0.3 init --home=/heimdall-home
      ```

   3. Edit `config.toml` in `/mnt/data/heimdall/config`:

      - Set `moniker` to a unique node name.
      - Change `laddr` to `tcp://0.0.0.0:26657`.
      - Update `seeds` with the latest list (found in the section on seed nodes and bootnodes).

   4. Edit `heimdall-config.toml`:

      - Set `eth_rpc_url` to your Ethereum Mainnet RPC URL.
      - Change `bor_rpc_url` to `<http://bor:8545>`.

   5. Update the `genesis.json` for Mainnet:


      ```bash
         sudo curl -o /mnt/data/heimdall/config/genesis.json https://raw.githubusercontent.com/maticnetwork/heimdall/master/builder/files/genesis-mainnet-v1.json
      ```

      

   Verify the hash with `sha256sum genesis.json`.

## Starting Heimdall

Create a Docker network for container communication:

```bash
docker network create polygon
```

Start Heimdall:

```bash
docker run -p 26657:26657 -p 26656:26656 -v /mnt/data/heimdall:/heimdall-home:rw --net polygon --name heimdall --entrypoint /usr/bin/heimdalld -d --restart unless-stopped  0xpolygon/heimdall:1.0.3 start --home=/heimdall-home
```

Monitor Heimdall with `docker ps` and `docker logs -ft heimdall`. Verify syncing status with `curl localhost:26657/status`.

## Starting Bor

Start Heimdall's REST server:

```bash
docker run -p 1317:1317 -v /mnt/data/heimdall:/heimdall-home:rw --net polygon --name heimdallrest --entrypoint /usr/bin/heimdalld -d --restart unless-stopped 0xpolygon/heimdall:1.0.3 rest-server --home=/heimdall-home --node "tcp://heimdall:26657"
```

Verify the REST server with `curl localhost:1317/bor/span/1`.

Download and verify the Bor `genesis` file:

```bash
sudo curl -o /mnt/data/bor/genesis.json 'https://raw.githubusercontent.com/maticnetwork/bor/master/builder/files/genesis-mainnet-v1.json'
```

Generate and configure the Bor `config.toml`:

```bash
docker run -it  0xpolygon/bor:1.1.0 dumpconfig | sudo tee /mnt/data/bor/config.toml
```

Edit the `config.toml` file as needed.

Start Bor:

```bash
docker run -p 30303:30303 -p 8545:8545 -v /mnt/data/bor:/bor-home:rw --net polygon --name bor -d --restart unless-stopped  0xpolygon/bor:1.1.0 server --config /bor-home/config.toml
```

Check Bor's sync status with:

```bash
curl 'localhost:8545/' --header 'Content-Type: application/json' -d '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'
```

### Seed nodes and bootnodes

- **Heimdall Seed Nodes**:

  Update the `seeds` in `config.toml` with the appropriate values for Mainnet or Testnet.

- **Bootnodes**:

  Update the `bootnodes` in Bor's `config.toml` as per the Mainnet or Testnet requirements.

Congratulations! You've successfully set up a Polygon full node using Docker.
