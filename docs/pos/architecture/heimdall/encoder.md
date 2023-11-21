---
id: encoder
title: Encoder (Pulp)
description: RLP encoding to produce special transactions, like checkpoint
keywords:
  - docs
  - matic
  - rlp encoding
  - checkpoint
  - encoder
  - polygon
image: https://matic.network/banners/matic-network-16x9.png 
---

# Encoder (Pulp)

Heimdall needs to verify the transactions of Heimdall on the Ethereum chain. For that it uses RLP encoding to produce special transactions, like checkpoint.

This special transaction uses `pulp` (RLP based) encoding instead of default amino encoding.

Pulp uses a prefix-based simple encoding mechanism to solve interface decoding. Check `GetPulpHash` method.

Source: [https://github.com/maticnetwork/heimdall/blob/master/auth/types/pulp.go](https://github.com/maticnetwork/heimdall/blob/master/auth/types/pulp.go)

```go
const (
	// PulpHashLength pulp hash length
	PulpHashLength int = 4
)

// GetPulpHash returns string hash
func GetPulpHash(name string) []byte {
	return crypto.Keccak256([]byte(name))[:PulpHashLength]
}
```

The below returns prefix-bytes for a given `msg`.  Here is an example on how to register an object for pulp encoding:

```go
RegisterConcrete(name, obj) {
	rtype := reflect.TypeOf(obj)
	// set record for name => type of the object
	p.typeInfos[hex.EncodeToString(GetPulpHash(name))] = rtype
}

// register "A"
pulp.RegisterConcrete("A", A{})
```

Encoding is just RLP encoding and prepending hash of `GetPulpHash` of the `name`:

```go
// EncodeToBytes encodes msg to bytes
txBytes, err := rlp.EncodeToBytes(obj)
if err != nil {
	return nil, err
}

result := append(GetPulpHash("A"), txBytes[:]...), nil
```

Decoding works as follows:

```go
// retrieve type of object based on prefix 
rtype := typeInfos[hex.EncodeToString(incomingData[:PulpHashLength])]

// create new object
newMsg := reflect.New(rtype).Interface()

// decode without prefix and inject into newly created object
if err := rlp.DecodeBytes(incomingData[PulpHashLength:], newMsg); err != nil {
	return nil, err
}

// result => newMsg
```

:::info For more information

The Cosmos SDK utilizes two binary wire encoding protocols, [Amino](https://github.com/tendermint/go-amino/) and [Protocol Buffers](https://developers.google.com/protocol-buffers), where Amino is an object encoding specification. It is a subset of Proto3 with an extension for interface support. See the [Proto3 spec](https://developers.google.com/protocol-buffers/docs/proto3) for more information on Proto3, which Amino is largely compatible with (but not with Proto2).

More here: [https://docs.cosmos.network/master/core/encoding.html](https://docs.cosmos.network/master/core/encoding.html)

:::
