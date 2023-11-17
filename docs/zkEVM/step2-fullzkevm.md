
Continue with the **Second Step** of this Deployment-Guide where you install dependencies and download Mainnet files.

## Install Dependencies

1. First, install base dependencies:

```bash
sudo apt update -y
sudo apt install -y tmux git curl unzip jq aria2 pv

curl -fsSL get.docker.com | CHANNEL=stable sh
sudo apt install docker-ce
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER
newgrp docker && newgrp $USER

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.bashrc
nvm install 16
node -v

wget https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz
rm -rf go1.20.4.linux-amd64.tar.gz
```

2. Next, add these to your `.profile`:

   ```bash
   echo '
    export ZKEVM_NET=mainnet
    export ZKEVM_DIR=~/zkevm/zkevm-node
    export ZKEVM_CONFIG_DIR=~/zkevm/zkevm-config
   
    [ -d "/usr/local/go/bin" ] && PATH="/usr/local/go/bin:$PATH"
    ' >> ~/.profile
    source .profile
   ```

3. Lastly, confirm the installation of Golang by running this command: `$ go version`

## Download/Extract Mainnet Files

Next step in the process is to download the zkEVM Mainnet files. This download is over **70GB**, so it's recommended to run the download in a tmux/screen session to handle any network interruptions:

```bash
aria2c -x6 -s6 "https://de012a78750e59b808d922b39535e862.s3.eu-west-1.amazonaws.com/v1.1.0-rc.1-fork.4.tgz"
pv v1.1.0-rc.1-fork.4.tgz | tar xzf -
```

Once the download is finished, you should extract the files using the following command:

```bash
tar xzvf v1.1.0-rc.1-fork.4.tgz
```
