This quickstart guides you through the process of setting up a CDK validium on your local machine.

!!! note
    - The documentation describes standard deployments. 
    - Edit the configuration files to implement your own custom setups.

## Prerequisites

### System requirements

- A Linux-based OS (e.g., Ubuntu Server 22.04 LTS).
- At least 16GB RAM with a 4-core CPU.
- An AMD64 architecture system.

!!! warning
    CDK does not support ARM-based Macs.

### Software requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 1. Clone the repo

Run the following commands:

```bash
git clone https://github.com/Snapchain/zkValidium-quickstart.git
cd zkValidium-quickstart
```

Create the `.env` file by copying the example:

```bash
cp .env.example .env
```

## 2. Launch validium locally

2.1 Pull the required Docker images from Docker Hub:

```bash
sudo docker-compose pull
```

2.2 After pulling the images, start your local CDK validium:

```bash
sudo make run
```

2.3 To ensure all services are running properly, check the status of each container:

```bash
docker-compose ps 
```

You should see the following output:

<details>
<summary>Container status details ↓</summary>

```shell
             Name                           Command                  State                                   Ports                            
----------------------------------------------------------------------------------------------------------------------------------------------
cdk-validium-aggregator          /bin/sh -c /app/cdk-validi ...   Up             0.0.0.0:50081->50081/tcp,:::50081->50081/tcp, 8123/tcp,      
                                                                                 0.0.0.0:9093->9091/tcp,:::9093->9091/tcp                     
cdk-validium-approve             /bin/sh -c /app/cdk-validi ...   Exit 0                                                                      
cdk-validium-data-availability   /bin/sh -c /app/cdk-data-a ...   Up             0.0.0.0:8444->8444/tcp,:::8444->8444/tcp                     
cdk-validium-data-node-db        docker-entrypoint.sh postg ...   Up (healthy)   0.0.0.0:5444->5432/tcp,:::5444->5432/tcp                     
cdk-validium-eth-tx-manager      /bin/sh -c /app/cdk-validi ...   Up             8123/tcp, 0.0.0.0:9094->9091/tcp,:::9094->9091/tcp           
cdk-validium-event-db            docker-entrypoint.sh postg ...   Up             0.0.0.0:5435->5432/tcp,:::5435->5432/tcp                     
cdk-validium-explorer-json-rpc   /bin/sh -c /app/cdk-validi ...   Up             8123/tcp, 0.0.0.0:8124->8124/tcp,:::8124->8124/tcp,          
                                                                                 0.0.0.0:8134->8134/tcp,:::8134->8134/tcp                     
cdk-validium-explorer-l1         /bin/sh -c mix do ecto.cre ...   Up             0.0.0.0:4000->4000/tcp,:::4000->4000/tcp                     
cdk-validium-explorer-l1-db      docker-entrypoint.sh postg ...   Up             0.0.0.0:5436->5432/tcp,:::5436->5432/tcp                     
cdk-validium-explorer-l2         /bin/sh -c mix do ecto.cre ...   Up             0.0.0.0:4001->4000/tcp,:::4001->4000/tcp                     
cdk-validium-explorer-l2-db      docker-entrypoint.sh postg ...   Up             0.0.0.0:5437->5432/tcp,:::5437->5432/tcp                     
cdk-validium-json-rpc            /bin/sh -c /app/cdk-validi ...   Up             0.0.0.0:8123->8123/tcp,:::8123->8123/tcp,                    
                                                                                 0.0.0.0:8133->8133/tcp,:::8133->8133/tcp,                    
                                                                                 0.0.0.0:9091->9091/tcp,:::9091->9091/tcp                     
cdk-validium-l2gaspricer         /bin/sh -c /app/cdk-validi ...   Up             8123/tcp                                                     
cdk-validium-mock-l1-network     geth --http --http.api adm ...   Up             30303/tcp, 30303/udp,                                        
                                                                                 0.0.0.0:8545->8545/tcp,:::8545->8545/tcp,                    
                                                                                 0.0.0.0:8546->8546/tcp,:::8546->8546/tcp                     
cdk-validium-pool-db             docker-entrypoint.sh postg ...   Up             0.0.0.0:5433->5432/tcp,:::5433->5432/tcp                     
cdk-validium-prover              zkProver -c /usr/src/app/c ...   Up             0.0.0.0:50052->50052/tcp,:::50052->50052/tcp,                
                                                                                 0.0.0.0:50061->50061/tcp,:::50061->50061/tcp,                
                                                                                 0.0.0.0:50071->50071/tcp,:::50071->50071/tcp                 
cdk-validium-sequence-sender     /bin/sh -c /app/cdk-validi ...   Up             8123/tcp                                                     
cdk-validium-sequencer           /bin/sh -c /app/cdk-validi ...   Up             0.0.0.0:6060->6060/tcp,:::6060->6060/tcp, 8123/tcp,          
                                                                                 0.0.0.0:9092->9091/tcp,:::9092->9091/tcp                     
cdk-validium-state-db            docker-entrypoint.sh postg ...   Up             0.0.0.0:5432->5432/tcp,:::5432->5432/tcp                     
cdk-validium-sync                /bin/sh -c /app/cdk-validi ...   Up             8123/tcp                                                     
dac-setup-committee              docker-entrypoint.sh npm r ...   Exit 0                                                                      
zkevm-bridge-db                  docker-entrypoint.sh postg ...   Up             0.0.0.0:5438->5432/tcp,:::5438->5432/tcp                     
zkevm-bridge-service             /bin/sh -c /app/zkevm-brid ...   Up             0.0.0.0:8080->8080/tcp,:::8080->8080/tcp,                    
                                                                                 0.0.0.0:9090->9090/tcp,:::9090->9090/tcp                     
zkevm-bridge-ui                  /bin/sh /app/scripts/deploy.sh   Up             0.0.0.0:8088->80/tcp,:::8088->80/tcp 
```

</details>

2.3.1 If a service isn't running (i.e. it is in `Exit 1` state), investigate further using the logs:

```bash
sudo docker-compose logs <container_name>
```

!!! info
    Find the `<container_name>` in the log output.

2.4 Useful commands

To stop CDK validium, use:

```bash
sudo make stop
```

To restart all services:

```bash
sudo make restart
```

!!! note
    This local deployment runs on an L1 Geth instance.

## 3. Test validium

3.1 Verify the block explorer is running by navigating to [localhost:4001](http://localhost:4001/).

You should see a page similar to this:

<div align="center">
  <img src="/img/cdk/cdk-block-explorer-empty.png" alt="bridge" width="90%" height="30%" />
</div>

## 4. Add the network to a Web3 wallet

4.1 Follow MetaMask's instructions on [how to set up a network manually](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC).

- Set the chain ID to **1001**.
- The currency symbol can be anything but we will use **POL** by default.
- The RPC node and block explorer containers can be found at ports **8123** and **4001**, respectively.

<div align="center">
  <img src="/img/cdk/cdk-metamask-add-network.png" alt="bridge" width="90%" height="30%" />
</div>

4.2 Switch to the new network:

<div align="center">
  <img src="/img/cdk/cdk-metamask-switch-network.png" alt="bridge" width="90%" height="30%" />
</div>

!!! danger "Important"
    - An account with test funds is available with private key `0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80`.
    - NEVER transfer real assets to the address associated with this private key.

4.3 [Import the account to MetaMask](https://support.metamask.io/hc/en-us/articles/360015489331-How-to-import-an-account). The balance shows up as 100000 POL:

<div align="center">
  <img src="/img/cdk/cdk-metamask-import-account.png" alt="bridge" width="90%" height="30%" />
</div>

4.4 Transfer some tokens to another account:

<div align="center">
  <img src="/img/cdk/cdk-metamask-transfer.gif" alt="bridge" width="90%" height="30%" />
</div>

4.5 After confirming the transaction, check the updated balances:

<div align="center">
  <img src="/img/cdk/cdk-metamask-transfer-result.gif" alt="bridge" width="90%" height="30%" />
</div>

4.6 You can also view the transaction details in the block explorer by clicking on the transaction details in MetaMask:

<div align="center">
  <img src="/img/cdk/cdk-tx-view-on-block-explorer.png" alt="bridge" width="90%" height="30%" />
</div>

## 5. Test the bridge

CDK has a native bridge with UI that allows you to transfer funds between the L1 and the L2 validium.

### 5.1 L1 to L2

5.1.1 Add the L1 RPC to MetaMask:

<div align="center">
  <img src="/img/cdk/cdk-metamask-add-l1.png" alt="bridge" width="90%" height="30%" />
</div>

5.1.2 Switch to the L1 network and you will see the previously imported account with ~999 POL on the L1 chain.

5.1.3 Verify the bridge UI by navigating to [localhost:8088](http://localhost:8088/).

5.1.4 Click on **Connect a wallet > MetaMask**.

<div align="center">
  <img src="/img/cdk/cdk-bridge.png" alt="bridge" width="90%" height="30%" />
</div>

5.1.5 Select the previously imported account (0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266). Once you are connected, you should see a page like this:

<div align="center">
  <img src="/img/cdk/cdk-bridge-connected.png" alt="bridge" width="90%" height="30%" />
</div>

5.1.6 Enter the amount (e.g. 5) to bridge and click **Continue**, you will see the **Confirm Bridge** page.

5.1.7 Click **Bridge** and approve the transaction on the MetaMask pop-up:

<div align="center">
  <img src="/img/cdk/cdk-bridge-confirm.png" alt="bridge" width="90%" height="30%" />
</div>

5.1.8 Once bridging is complete, you should see the **Activity** page:

<div align="center">
  <img src="/img/cdk/cdk-bridge-completed-l1-to-l2.png" alt="bridge" width="90%" height="30%" />
</div>

### 5.2 L2 to L1

5.2.1 Switch network on MetaMask to your validium chain and navigate back to [localhost:8088](http://localhost:8088/).

5.2.2 You should see both the updated L1 and L2 balances:

<div align="center">
  <img src="/img/cdk/cdk-bridge-l2-to-l1.png" alt="bridge" width="90%" height="30%" />
</div>

5.2.3 Enter an amount and follow the same process to bridge the fund back to the L1.

!!! note
    You cannot bridge back fund more than what you have previously bridged from L1 to the L2.

The L2->L1 bridging is slightly different than L1->L2 and you will see the **Activity** page like this after the transaction is executed:

<div align="center">
  <img src="/img/cdk/cdk-bridge-l2-to-l1-on-hold.png" alt="bridge" width="90%" height="30%" />
</div>

5.2.4 Click **Finalise** and approve the transaction (Note: MetaMask will pop up a window to ask you to switch to the L1 network first). Then you will see this once the bridging is completed:

<div align="center">
  <img src="/img/cdk/cdk-bridge-l2-to-l1-completed.png" alt="bridge" width="90%" height="30%" />
</div>
