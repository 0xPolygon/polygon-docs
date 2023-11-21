---
id: peppermint
title: Peppermint 
description: Peppermint is a modified Ethereum-compatible Tendermint
keywords:
  - docs
  - matic
  - polygon
  - tendermint
  - peppermint
image: https://matic.network/banners/matic-network-16x9.png 
---

Peppermint is a modified Tendermint. It is changed to make it compatible with Ethereum addresses and verifiable on Ethereum chain.

## Overview

1. Changes to signature scheme
2. Changes to `vote` to make it verifiable on Ethereum smart contract
3. Changes to `vote` encoding scheme

Peppermint uses `secp256k1` signature scheme to verify Tendermint votes on solidity smart contract.

Source: [https://github.com/maticnetwork/tendermint/blob/peppermint/crypto/secp256k1/secp256k1_nocgo.go](https://github.com/maticnetwork/tendermint/blob/peppermint/crypto/secp256k1/secp256k1_nocgo.go)

It adds `Data` field into `Vote` and `Proposal` struct to get `hash` for transactions in the block. On smart contract, it checks if `Data` matches with checkpoint data hash and majority (⅔+1) of validator signatures. The idea is to verify if majority of the validator set agrees on transaction in the contract.

Peppermint uses RLP to get `Vote` bytes instead of Amino encoding. Here `Data` is `Txs.Hash()` for the block. 

Source: [https://github.com/maticnetwork/tendermint/blob/peppermint/types/canonical.go](https://github.com/maticnetwork/tendermint/blob/peppermint/types/canonical.go)

```go
// [peppermint] create RLP vote to decode in contract
type CanonicalRLPVote struct {
	ChainID string
	Type    byte
	Height  uint
	Round   uint
	Data    []byte
}
```

And using RLP encoding lib to get byte data for signature on Vote.

Source: [https://github.com/maticnetwork/tendermint/blob/peppermint/types/vote.go#L75-L82](https://github.com/maticnetwork/tendermint/blob/peppermint/types/vote.go#L75-L82)

```go
func (vote *Vote) SignBytes(chainID string) []byte {
	// [peppermint] converted from amino to rlp
	bz, err := rlp.EncodeToBytes(CanonicalizeVote(chainID, vote))
	if err != nil {
		panic(err)
	}
	return bz
}
```

Complete Source: [https://github.com/maticnetwork/tendermint](https://github.com/maticnetwork/tendermint)
