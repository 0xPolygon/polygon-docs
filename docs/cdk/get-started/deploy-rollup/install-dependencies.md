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