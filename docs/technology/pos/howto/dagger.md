---
id: dagger
title: Dagger
sidebar_label: Dagger - Single App
description: Build your next blockchain app on Polygon
keywords:
  - docs
  - matic
  - polygon
  - dagger
image: https://wiki.polygon.technology/img/polygon-logo.png
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::caution Content disclaimer

Please view the third-party content disclaimer [<ins>here</ins>](https://github.com/0xPolygon/wiki/blob/master/CONTENT_DISCLAIMER.md).

:::

---

Dagger is the best way to get realtime updates from Ethereum Blockchain.
It provides a way for your DApps and Backend system to get Ethereum blockchain events i.e. transactions, token transfers, receipts and logs in realtime over websocket or socket.

We maintain infrastructure for reliable and scalable realtime events. `@maticnetwork/dagger` is consumer library for Dagger project written in NodeJS. It uses Dagger server to get realtime updates from Ethereum Network.

## Installation

```sh
# Using Yarn
yarn add @maticnetwork/dagger

# Using NPM
npm install @maticnetwork/dagger --save
```

## Network

### Ethereum Network

#### Mainnet

```sh
Websocket: wss://mainnet.dagger.matic.network
Socket: mqtts://mainnet.dagger.matic.network (You can also use `ssl://` protocol)
```

#### Kovan

```sh
Websocket: wss://kovan.dagger.matic.network
Socket: mqtts://kovan.dagger.matic.network (You can also use `ssl://` protocol)
```

#### Ropsten

```sh
Websocket: wss://ropsten.dagger.matic.network
Socket: mqtts://ropsten.dagger.matic.network (You can also use `ssl://` protocol)
```

#### Goerli

```sh
Websocket: wss://goerli.dagger.matic.network
Socket: mqtts://goerli.dagger.matic.network (You can also use `ssl://` protocol)
```

### Matic Network

#### Mainnet

```sh
Websocket: wss://matic-mainnet.dagger.matic.network
Socket: mqtts://matic-mainnet.dagger.matic.network (You can also use `ssl://` protocol)
```

#### Mumbai Testnet

```sh
Websocket: wss://mumbai-dagger.matic.today
Socket: mqtts://mumbai-dagger.matic.today (You can also use `ssl://` protocol)
```

## Example

- Lets first create a _npm_ project.

```bash
npm init -y
touch index.js
```

- Now we can put following code snippet in `index.js`.

```javascript
const Dagger = require('@maticnetwork/dagger')

// connect to correct dagger server, for receiving network specific events
//
// you can also use socket based connection
const dagger = new Dagger("wss://mainnet.dagger.matic.network")

// get new block as soon as it gets created
dagger.on('latest:block.number', result => {
  console.log(`New block created: ${result}`)
})
```

- Run `index.js` & you'll start receiving block number as soon as new block gets created.

```bash
node index.js
```

## API

### new Dagger(url)

Create dagger object

- `url` is dagger server's address. Check [network section](#network) for all available url values.

Example:

```js
const dagger = new Dagger(<url>)
```

### dagger.on(event, fn)

Subscribe to a topic

- `event` is a `String` topic to subscribe to. `event` wildcard characters are supported (`+` - for single level and `#` - for multi level)
- `fn` - `function (data, removed)`
  fn will be executed when event occurred:
  - `data` data from event
  - `removed` flag saying if data is removed from blockchain due to re-organization.

Example:

```js
dagger.on('latest:block.number', (res, flag) => { console.log(res, flag) })
```

### dagger.once(event, fn)

Same as [on](#daggeronevent-fn) but will be fired only once.

Example:

```js
dagger.once('latest:block.number', (res, flag) => { console.log(res, flag) })
```

### dagger.off(event, fn)

Unsubscribe from a topic

- `event` is a `String` topic to unsubscribe from
- `fn` - `function (data, removed)`

Example:

```js
dagger.off('latest:block.number', (res, flag) => { console.log(res, flag) })
```

### dagger.of(room)

Create room out of dagger. `room` has to be one out of two values
  - `latest`
  - `confirmed`

`room` object has following methods:
  - `on` same as dagger `on`
  - `once` same as dagger `once`
  - `off` same as dagger `off`

```js
const latestRoom = dagger.of('latest')
const confirmedRoom = dagger.of('confirmed')
```

### dagger.end([force])

Close the dagger, accepts the following options:

- `force`: passing it to true will close the dagger right away. This parameter is
optional.

```js
dagger.end({force: true}) // immediate closing
```

### dagger.contract(web3Contract)

Creates web3 contract wrapper to support Dagger.

- First create a web3 contract object.

```javascript
// web3 contract
const web3Contract = new web3.eth.Contract(abi, address)
```

- Now we'll create a dagger contract wrapper on it.

```javascript
// dagger contract
const contract = dagger.contract(web3Contract)
```

- Time to filter out contract events

```javascript
const filter = contract.events.Transfer({
  filter: { from: "0x123456..." },
  room: "latest"
})
```

- Watching contract events

```javascript
// watch
filter.watch((data, removed) => { console.log(data, removed) })

// or watch only once
filter.watchOnce((data, removed) => { console.log(data, removed) })
```

- Stopping event watching

```js
// stop watching
filter.stopWatching();
```

## Events

Every event has a room ∈ {`latest`, `confirmed`}.
  - `latest` : Events are fired immediately after block included in chain.
  - `confirmed` : Events are fired after 12 confirmations.

If you want to show updates on UI in your DApp, use `latest` events. It will help to make UI/UX better and user friendly.

Use `confirmed` events for irreversible tasks from server or on UI. Like sending email, notifications or allow user to do subsequent task on UI after one transaction gets confirmed.

### Network Events

| Ethereum event                                 | When?                                                                   | `removed` flag |
| ---------------------------------------------- | ----------------------------------------------------------------------- | -------------- |
| block                                          | For every new block created                                             | Yes            |
| block.number                                   | For every new block number created                                      |                |
| block.hash                                     | For every new block hash created                                        | Yes            |
| block/`number`                                 | When particular block in future included in chain                       | Yes            |
| addr/`address`/tx                              | On every new transaction for `address`                                  | Yes            |
| addr/`address`/tx/out                          | On every new outgoing transaction for `address`                         | Yes            |
| addr/`address`/tx/in                           | On every new incoming transaction for `address`                         | Yes            |
| tx/`txId`                                      | When given `txId` included in block                                     | Yes            |
| tx/`txId`/success                              | When tx status is success (included in block) for `txId`                | Yes            |
| tx/`txId`/fail                                 | When tx fails (included in block) for `txId`                            | Yes            |
| tx/`txId`/receipt                              | When receipt is generated (included in block) for `txId`                | Yes            |
| addr/`contractAddress`/deployed                | When new `contractAddress` included in block                            | Yes            |
| log/`contractAddress`                          | When new log generated for `contractAddress`                            | Yes            |
| log/`contractAddress`/filter/`topic1`/`topic2` | When new log with `topic1` and `topic2` generated for `contractAddress` | Yes            |

### Dagger Events

| Dagger Event      | When?                          | args           |
| ----------------- | ------------------------------ | -------------- |
| connection.status | When connection status changes | value: Boolean |


Every event has to start with room:

#### block

For every new block

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:block", result => {
  console.log("Current block : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:block", result => {
  console.log("Confirmed block : ", result)
})
```

</TabItem>
</Tabs>


#### block.number

For every new block number

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:block.number", result => {
  console.log("Current block number : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:block.number", result => {
  console.log("Confirmed block number : ", result)
})
```

</TabItem>
</Tabs>

#### block.hash

For every new block hash

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:block.hash", result => {
  console.log("Current block hash : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:block.hash", result => {
  console.log("Confirmed block hash : ", result)
})
```

</TabItem>
</Tabs>

#### block/{number}

When particular block **X**, in future included in chain

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:block/X", result => {
  console.log("Included in chain : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:block/X", result => {
  console.log("Included in chain : ", result)
})
```

</TabItem>
</Tabs>

#### addr/{address}/tx

On every new transaction for `address`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:addr/{address}/tx", result => {
  console.log("New Transaction : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:addr/{address}/tx", result => {
  console.log("New Transaction : ", result)
})
```

</TabItem>
</Tabs>

#### addr/{address}/tx/{dir}

`dir` is transaction direction ∈ {`in`, `out`}. `address` can be omitted to receive notification for any address.

<Tabs
  defaultValue="in"
  values={[
    { label: 'incoming', value: 'in', },
    { label: 'outgoing', value: 'out', },
    { label: 'wild card', value: 'all', },
  ]
}>
<TabItem value="in">

On every new incoming transaction for `address`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:addr/{address}/tx/in", result => {
  console.log("New Incoming Transaction : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:addr/{address}/tx/in", result => {
  console.log("New Incoming Transaction : ", result)
})
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="out">

On every new outgoing transaction for `address`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:addr/{address}/tx/out", result => {
  console.log("New Outgoing Transaction : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:addr/{address}/tx/out", result => {
  console.log("New Outgoing Transaction : ", result)
})
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="all">

Using wildcard notation in place of `address`, to get notified for all incoming & outgooing transactions.

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:addr/+/tx/in", result => {
  console.log("New Incoming Transaction : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:addr/+/tx/in", result => {
  console.log("New Incoming Transaction : ", result)
})
```

</TabItem>
</Tabs>

</TabItem>
</Tabs>

#### tx/{txId}/{status}

`status` is `txId`'s status ∈ {`success`, `fail`, `receipt`}. It can be kept empty too i.e. resulting into `tx/{txId}`, triggered when `txId` gets included in block.

<Tabs
  defaultValue="any"
  values={[
    { label: 'any', value: 'any', },
    { label: 'success', value: 'success', },
    { label: 'fail', value: 'fail', },
    { label: 'receipt', value: 'receipt', },
  ]
}>
<TabItem value="any">

When given `txId` included in block

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:tx/{txId}", result => { console.log(result) })
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:tx/{txId}", result => { console.log(result) })
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="success">

When tx status is success (included in block) for `txId`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:tx/{txId}/success", result => { console.log(result) })
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:tx/{txId}/success", result => { console.log(result) })
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="fail">

When tx fails (included in block) for `txId`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:tx/{txId}/fail", result => { console.log(result) })
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:tx/{txId}/fail", result => { console.log(result) })
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="receipt">

When receipt is generated (included in block) for `txId`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:tx/{txId}/receipt", result => { console.log(result) })
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:tx/{txId}/receipt", result => { console.log(result) })
```

</TabItem>
</Tabs>

</TabItem>
</Tabs>

#### log/{contractAddress}

When log generated for `contractAddress`

<Tabs
  defaultValue="latest"
  values={[
    { label: 'latest', value: 'latest', },
    { label: 'confirmed', value: 'confirmed', },
  ]
}>
<TabItem value="latest">

```javascript
dagger.on("latest:log/{contractAddress}", result => {
  console.log("New Log : ", result)
})
```

</TabItem>
<TabItem value="confirmed">

```javascript
dagger.on("confirmed:log/{contractAddress}", result => {
  console.log("New Log : ", result)
})
```

</TabItem>
</Tabs>

#### log/{contractAddress}/filter/{topic0}/{topic1}/{topic2}

When new log with `topic0`, `topic1` & `topic2` generated for `contractAddress`

```javascript
// Triggers when 1 GNT (Golem token) get transferred to Golem multisig wallet
dagger.on('latest:log/0xa74476443119a942de498590fe1f2454d7d4ac0d/filter/0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef/filter/+/0x7da82c7ab4771ff031b66538d2fb9b0b047f6cf9/#', console.log)

// Triggers when any amount of GNT (Golem token) get sent from Golem multisig wallet
dagger.on('latest:log/0xa74476443119a942de498590fe1f2454d7d4ac0d/filter/0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef/0x7da82c7ab4771ff031b66538d2fb9b0b047f6cf9/#', ...)

// Listen for every Golem token transfer (notice `#` at the end)
dagger.on('latest:log/0xa74476443119a942de498590fe1f2454d7d4ac0d/filter/0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef/#', ...)
```

> Event names are case-sensitive. `address`, `txId` and `topics` must be in lowercase.

> Note: You can use wildcard for events too. There are two type of wildcards: `+` (for single) and `#` (for multiple). Use with caution as it will fetch more data then you need, and can bombard with data to your DApp.



## Test Dagger Server

This library consists `woodendagger` executable which is test dagger server on your local machine. So you can test with TestRPC.

Please do not use `woodendagger` in production. It's only for development purpose. It doesn't support `removed` flag.

```bash
$ woodendagger --url=https://mainnet.infura.io # or http://localhost:8545 for local json-rpc

# If you want to start dagger server on different ports,
# sockport: socket port for backend connection over TCP
# wsport: websocket port for frontend connection over websocket
$ woodendagger --url=http://localhost:8545 --sockport=1883 --wsport=1884

# To connect from dagger:
const dagger = new Dagger('mqtt://localhost:1883')
```

## Support

If you have any queries, feedback or feature requests, feel free to reach out to us on [Telegram](https://t.me/maticnetwork)

## License

MIT
