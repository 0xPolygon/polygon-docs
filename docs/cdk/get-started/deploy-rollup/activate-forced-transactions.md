
Continue with the **sixth step** of this deployment-guide where you activate forced transactions, as well as bridging and claiming assets.

## Activate forced transactions

You can check out [this](../../architecture/protocol/malfunction-resistance/sequencer-resistance.md) document to learn more about forced batches of transactions.

```bash
cd ~/zkevm-contracts
npx hardhat console --network goerli
```

```js
const zkevm = await ethers.getContractFactory("PolygonZkEVM");
const zkevmContract = zkevm.attach("_polygonZkEVMAddress_"); // From ~/zkevm-contracts/deployments/goerli_*/deploy_output.json polygonZkEVMAddress

const provider = ethers.getDefaultProvider(""); // set Geth Goerli RPC endpoint
const privateKey = ""; // Deployment Address prvkey from wallet.txt
const wallet = new ethers.Wallet(privateKey, provider);

const zkevmContractWallet = zkevm.connect(wallet);

await zkevmContract.activateForceBatches();
```

## Provide L1 ETH to the bridge

Run the below commands in CLI to **create a bridge transaction** and send L1 Ether to the zkEVM Bridge.

```bash
mkdir -p ~/zkevm/initial-bridge
cd zkevm/initial-bridge

wget https://raw.githubusercontent.com/0xPolygonHermez/zkevm-bridge-service/develop/test/scripts/deposit/main.go
vim main.go
```

Populate the `main.go` file with following variables:

```go
l1BridgeAddr       = "" // ~/zkevm-contracts/deployments/goerli_*/deploy_output.json: polygonZkEVMBridgeAddress

l1AccHexAddress    = "" // ~/zkevm-contracts/wallets.txt: sequencer address
l1AccHexPrivateKey = "" // ~/zkevm-contracts/wallets.txt: sequencer prvkey
l1NetworkURL       = "http://X.X.X.X:8545"      // set your public IP
```

Initialize a new Go module with the module path `example.com/deposit`.

```bash
go mod init example.com/deposit
go mod tidy
go run main.go

# 2023-06-07T06:29:14.211Z      INFO    initial-bridge/main.go:46       Success!        {"pid": 776268, "version": "v0.1.0"}
```

## Claim your L2 zkETH

After sending your first bridge transaction to your zkEVM network, create a **forced claim to get the zkETH in L2**.

```bash
mkdir -p ~/zkevm/initial-claim
cd ~/zkevm/initial-claim

wget https://raw.githubusercontent.com/0xPolygonHermez/zkevm-bridge-service/develop/test/scripts/initialClaim/main.go
vim main.go
```

Open `main.go` and update the following parameters:

```go
const (
    l2BridgeAddr = ""  // ~/zkevm-contracts/deployments/goerli_*/deploy_output.json: polygonZkEVMBridgeAddress
    zkevmAddr    = ""  // ~/zkevm-contracts/deployments/goerli_*/deploy_output.json: polygonZkEVMAddress

    accHexAddress    = ""  // ~/zkevm-contracts/wallets.txt: sequencer address
    accHexPrivateKey = ""  // ~/zkevm-contracts/wallets.txt: sequencer prvkey
    l1NetworkURL     = "http://X.X.X.X:8545"  // public IP
    l2NetworkURL     = "http://X.X.X.X:8123"  // public IP
    bridgeURL        = "http://X.X.X.X:8080"  // public IP

    l2GasLimit = 1000000

    mtHeight      = 32
    miningTimeout = 180
)
```

Time to execute the claim transaction:

```bash
go mod init example.com/claim
go mod tidy
go get github.com/0xPolygonHermez/zkevm-bridge-service@4e1ca558144cac00fe0762329aaf7b3e9482b57a
go run main.go

# 2023-06-07T06:41:50.731Z     INFO    initial-claim/main.go:196       Success!!!!     {"pid": 783804, "version": "v0.1.0"}
```

!!!congratulations
    Congratulations on reaching this far in setting up your own zkEVM network.
    **Your network is live on the Testnet** and you can send transactions to verify the same. Also, we have provided a Goerli full node setup guide below in case you are looking for one.
