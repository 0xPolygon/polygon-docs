Open a terminal window and run the following commands to install the required software.

## Install base dependencies

```sh
sudo apt update -y
sudo apt install -y tmux git curl unzip jq aria2 pv
```

## Install Docker

```sh
sudo apt-get install docker-ce
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER
newgrp docker && newgrp $USER
```

## Install Node/npm

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.bashrc
nvm install 16
node -v
```

## Install Golang

```sh
wget https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz
rm -rf go1.20.4.linux-amd64.tar.gz
```

Confirm the Golang installation with `$ go version`.

## Update profile configuration

Add the following environment variables to your `~/.profile`.

```bash
echo '
  export ZKEVM_NET=mainnet
  export ZKEVM_DIR=~/zkevm/zkevm-node
  export ZKEVM_CONFIG_DIR=~/zkevm/zkevm-config
 
  [ -d "/usr/local/go/bin" ] && PATH="/usr/local/go/bin:$PATH"
  ' >> ~/.profile
  source .profile
```

<!--
## Download/extract mainnet files

Next step in the process is to download the mainnet files. 

!!! important
    - The download is over **70GB**. 
    - You might like to run the download in a tmux/screen session to handle any network interruptions.

The files are located in several urls, so a script can be used as shown below:

```sh
urls=(
  "https://storage.googleapis.com/zkevm/zkproverc/v0.6.0.0-rc.1.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v0.7.0.0-rc.1.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v0.7.0.0-rc.3.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v0.7.0.0-rc.7-fork.1.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v0.8.0.0-rc.1-fork.1.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v0.8.0.0-rc.2-forkid.2.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v1.0.0-rc.1-fork.3.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v1.1.0-rc.1-fork.4.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v2.0.0-RC4-fork.5.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v3.0.0-RC2-fork.6.tgz"
  "https://storage.googleapis.com/zkevm/zkproverc/v3.0.0-RC3-fork.6.tgz"
)

for url in "${urls[@]}"; do
  aria2c -x6 -s6 "$url"
done
```

Once the download is finished, you should extract the files using the following command:

```bash
tar xzvf v1.1.0-rc.1-fork.4.tgz
```

-->