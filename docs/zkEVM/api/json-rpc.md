---
hide:
- toc
---

## Terminal

Use the Cardona testnet https://rpc.cardona.zkevm-rpc.com to test the [endpoint methods](#playground) in a terminal. For example: 

### `zkevm_estimateGasPrice`

```sh
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"zkevm_estimateGasPrice","params":[{"from":"0x0000000000000000000000000000000000000001","to":"0x0000000000000000000000000000000000000002","value":"0x1"}],"id":1}' \
    https://rpc.cardona.zkevm-rpc.com
```

#### Result

```sh
{"jsonrpc":"2.0","id":1,"result":"0xe2ea2f0"}
```

## Playground

The available methods are detailed in the playground description below.

Each method description provides:

- Method name and explanation.
- Parameters required if any and their details. 
- Expected return.
- Examples.

<embed type="text/html" src="https://playground.open-rpc.org/?schemaUrl=https://raw.githubusercontent.com/0xPolygon/polygon-docs/3eb44779e7380e91e5c92f160424159a3da1bdba/docs/zkEVM/api/zkevm.openrpc.json&uiSchema[appBar][ui:input]=false&uiSchema[appBar][ui:splitView]=false" width="100%" height="1000px">
