---
id: types
title: Types
description: Description of HeimdallAddress, Pubkey, & HeimdallHash
keywords:
  - docs
  - matic
  - HeimdallAddress
  - polygon
  - Pubkey
  - HeimdallHash
image: https://matic.network/banners/matic-network-16x9.png 
---

# Types

## HeimdallAddress

`HeimdallAddress` represents address on Heimdall. It uses Ethereum's common library for Address. Length of this address is 20 bytes.

```go
// HeimdallAddress represents Heimdall address
type HeimdallAddress common.Address
```

## PubKey

It represents public key used in Heimdall, `ecdsa` compatible uncompressed public key.

```go
// PubKey pubkey
type PubKey [65]byte
```

## HeimdallHash

It represents hash in Heimdall. It uses Ethereum's hash for the same. 

```go
// HeimdallHash represents heimdall address
type HeimdallHash common.Hash
```