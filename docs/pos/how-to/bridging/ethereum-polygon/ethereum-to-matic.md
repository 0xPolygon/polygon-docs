---
comments: true
---

!!! warning "Work in progress!"

    This doc is currently undergoing revision, and the instructions provided may not be up to date. Stay tuned for updates!

The mechanism to natively read Ethereum data from Polygon EVM chain is that of ‘State Sync’. In other words, this mechanism enables transfer of arbitrary data from Ethereum chain to Polygon chain. The procedure that makes it possible is: Validators on the Heimdall layer are listening for a particular event — `StateSynced` from a *sender* contract, as soon as the event is picked, the `data` that was passed in the event is written on the *receiver* contract. Read more [here](../../../architecture/bor/state-sync.md).

The sender and receiver contracts are required to be mapped on Ethereum — [StateSender.sol](https://github.com/maticnetwork/contracts/blob/release-betaV2/contracts/root/stateSyncer/StateSender.sol) needs to be aware of each sender and receiver.

!!! tip "Custom tokens"

    Looking to bridge your custom token to Polygon PoS using the official bridge? Check out the guide on [how to submit a request to get your token mapped](../ethereum-polygon/submit-mapping-request.md).

---

In the following walkthrough, we'll be deploying a sender contract on Sepolia (Ethereum testnet) and a receiver contract on Amoy (Polygon testnet). Then, we'll be sending data from the sender and reading data on the receiver via web3 calls in a node script.

### 1. Deploy sender contract

The sole purpose of the sender contract is to be able to call [syncState](https://github.com/maticnetwork/contracts/blob/e999579e9dc898ab6e66ddcb49ee84c2543a9658/contracts/root/stateSyncer/StateSender.sol#L33) function on the StateSender contract — which is the state syncer contract on Polygon PoS that emits the `StateSynced` event that Heimdall listens for.

Deployed at:

`0x49E307Fa5a58ff1834E0F8a60eB2a9609E6A5F50` on Sepolia

`0x28e4F3a7f651294B9564800b2D01f35189A5bFbE` on Ethereum Mainnet

To be able to call this function, let's first include it's interface in our contract:

```jsx title="Sender.sol"

pragma solidity ^0.5.11;

contract IStateSender {
  function syncState(address receiver, bytes calldata data) external;
  function register(address sender, address receiver) public;
}

...
```

Next, let's write our custom function that takes in the data we'd like to pass on to Polygon and calls `syncState`.

```jsx
function sendState(bytes calldata data) external {
    states = states + 1 ;
    IStateSender(stateSenderContract).syncState(receiver, data);
}
```

In the above function, `stateSenderContract` is the address of the `StateSender` on the network you'll be deploying the sender on. (eg., we'll be using `0x49E307Fa5a58ff1834E0F8a60eB2a9609E6A5F50` for Sepolia), and the receiver is the contract that receives the data we send from here.

It is recommended to use constructors to pass in variables, but for the purpose of this demo, we'll simply hardcode these two addresses:

Following is what our `Sender.sol` looks like:

```jsx title="Sender.sol"

pragma solidity ^0.5.11;

contract IStateSender {
  function syncState(address receiver, bytes calldata data) external;
  function register(address sender, address receiver) public;
}

contract sender {
  address public stateSenderContract = 0xEAa852323826C71cd7920C3b4c007184234c3945;
  address public receiver = 0x83bB46B64b311c89bEF813A534291e155459579e;
  
  uint public states = 0;

  function sendState(bytes calldata data) external {
    states = states + 1 ;
    IStateSender(stateSenderContract).syncState(receiver, data);
  }
  
}
```

We're using a simple `states` counter to keep track of the number of states sent via the sender contract.

Use Remix to deploy the contract and keep a note of the address and ABI.

### 2. Deploy receiver contract

The receiver contract is the one that is invoked by a validator when the `StateSynced` event is emitted. The validator invokes the function `onStateReceive`on the receiver contract to submit the data. To implement it, we first import [StateReceiver](https://github.com/maticnetwork/contracts/blob/release-betaV2/contracts/child/bor/StateReceiver.sol) interface and write down our custom logic — to interpret the transferred data inside onStateReceive.

The following is what our `Receiver.sol` looks like:

```jsx title="Receiver.sol"

pragma solidity ^0.5.11;

// IStateReceiver represents interface to receive state
interface IStateReceiver {
  function onStateReceive(uint256 stateId, bytes calldata data) external;
}

contract receiver {

  uint public lastStateId;
  bytes public lastChildData;

  function onStateReceive(uint256 stateId, bytes calldata data) external {
    lastStateId = stateId;
    lastChildData = data;
 }

}
```

The function simply assigns the last received state ID and data to variables. [`StateId`](https://github.com/maticnetwork/contracts/blob/239a91045622ddcf9ebec2cec81fdc6daa3a33e3/contracts/root/stateSyncer/StateSender.sol#L36) is a simple unique reference to the transferred state (a simple counter).

Deploy your `Receiver.sol` to Amoy testnet and keep a note of the address and ABI.

### 3. Getting your sender and receiver contracts mapped

You can either use the already deployed addresses (mentioned above) for the sender and receiver, or deploy your custom contracts and request a mapping using [the Google form here](https://docs.google.com/forms/d/e/1FAIpQLSeq8HTef2dYpRx35_WWYhyr4C146K9dfhyYJQcoD1RuTTVABg/viewform).

### 4. Sending and receiving data

Now that we have our contracts in place and mapping done, we'll be writing a simple node script to send arbitrary hex bytes, receive them on Polygon and interpret the data!

#### Setup your script

We'll first initialize our web3 objects, wallet to make the transactions and contracts.

```jsx title="test.js"

const Web3 = require('web3')
const Network = require("@maticnetwork/meta/network")

const network = new Network ('testnet', 'amoy')

const main = new Web3(network.Main.RPC)
const matic = new Web3 (network.Matic.RPC)

let privateKey = `0x...` // add or import your private key

matic.eth.accounts.wallet.add(privateKey)
main.eth.accounts.wallet.add(privateKey)

let receiverAddress = `<RECEIVER_CONTRACT_ADDRESS>`
let receiverABI = `` // insert or import ABI
let senderAddress = `<SENDER_CONTRACT_ADDRESS>`
let senderABI = `` // insert of import the ABI

let sender = new main.eth.Contract(JSON.parse(senderABI), senderAddress)
let receiver = new matic.eth.Contract(JSON.parse(receiverABI), receiverAddress)

```

We're using `@maticnetwork/meta` package for the RPCs, the package isn't a requirement to run the script.

`matic` and `main` objects refer to the web3 object initialized with Polygon Amoy and Sepolia network's respective RPC URLs.

`sender` and `receiver` objects refer to the contract objects of `Sender.sol` and `Receiver.sol` that we deployed in Step 1 and 2.

#### Sending data

Next, let's setup our functions to create bytestring of the data and send it via the sender contract:

```jsx
// data to sync
function getData(string) {
  let data = matic.utils.asciiToHex(string);
  return data
}

// send data via sender
async function sendData (data) {
  let r = await sender.methods
    .sendState (getData(data))
    .send({
      from: main.eth.accounts.wallet[0].address,
      gas: 8000000
    })
  console.log('sent data from root, ', r.transactionHash)
}
```

Calling `getData` will convert an ASCII string (eg., `Hello World !`) to a string of bytes (eg., `0x48656c6c6f20576f726c642021`); while the function `sendData`takes in `data` (an ascii string), calls `getData` and passes on the bytestring to sender contract

#### Receiving data

Next, we'll be checking for received data on Receiver.sol.

It should take ~7-8 minutes for the state sync to execute.

Add the following functions to check the number of sent states from sender, and the last received state on the receiver contract.

```jsx
// check `states` variable on sender
async function checkSender () {
  let r = await sender.methods
    .states()
    .call()
  console.log('number of states sent from sender: ', r)
}

// check last received data on receiver
async function checkReceiver () {
  let r = await receiver.methods
    .lastStateId()
    .call()
  let s = await receiver.methods
    .lastChildData()
    .call()
  console.log('last state id: ', r, 'and last data: ', s)
  console.log('interpreted data: ', getString(s))
}
```

The function `checkReceiver` simply calls the variables we defined in the contract — which would be set as soon as the Validator calls `onStateReceive` on the contract. The `getString` function simply interprets the bytestring (converts it back to ASCII)

```jsx
function getString(data) {
  let string = matic.utils.hexToAscii(data);
  return string
}
```

Finally, we'll write up a method to execute our functions:

```jsx
async function test() {
 await sendData ('Sending a state sync! :) ')
 await checkSender ()
 await checkReceiver ()
}
```

#### Putting it all together!

This is how our test script looks like:

```jsx title="test.js"

const Web3 = require('web3')
const Network = require("@maticnetwork/meta/network")

const network = new Network ('testnet', 'amoy')

const main = new Web3(network.Main.RPC)
const matic = new Web3 (network.Matic.RPC)

let privateKey = `0x...`
matic.eth.accounts.wallet.add(privateKey)
main.eth.accounts.wallet.add(privateKey)

let receiverAddress = `<RECEIVER_CONTRACT_ADDRESS>`
let receiverABI = ``
let senderAddress = `<SENDER_CONTRACT_ADDRESS>`
let senderABI = ``

let sender = new main.eth.Contract(JSON.parse(senderABI), senderAddress)
let receiver = new matic.eth.Contract(JSON.parse(receiverABI), receiverAddress)

// data to sync
function getData(string) {
  let data = matic.utils.asciiToHex(string);
  return data
}

function getString(data) {
  let string = matic.utils.hexToAscii(data);
  return string
}

// console.log(getData('Sending a state sync! :) '))

async function sendData (data) {
  let r = await sender.methods
    .sendState (getData(data))
    .send({
      from: main.eth.accounts.wallet[0].address,
      gas: 8000000
    })
  console.log('sent data from root, ', r.transactionHash)
}

async function checkSender () {
  let r = await sender.methods
    .states()
    .call()
  console.log('number of states sent from sender: ', r)
}

async function checkReceiver () {
  let r = await receiver.methods
    .lastStateId()
    .call()
  let s = await receiver.methods
    .lastChildData()
    .call()
  console.log('last state id: ', r, 'and last data: ', s)
  console.log('interpreted data: ', getString(s))
}

async function test() {
 await sendData ('Hello World !')
 await checkSender ()
 // add a timeout here to allow time gap for the state to sync
 await checkReceiver ()
}

test()
```

#### Let's run the script

Successful execution of the above script provide an output as:

```bash
$ node test
> sent data from root 0x4f64ae4ab4d2b2d2dc82cdd9ddae73af026e5a9c46c086b13bd75e38009e5204
number of states sent from sender: 1
last state id: 453 and last data: 0x48656c6c6f20576f726c642021
interpreted data: Hello World ! 
```
