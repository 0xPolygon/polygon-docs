This contract is a helper for all functions related to the sparse Merkle tree. And it is based on the implementation of the deposit eth2.0 contract https://github.com/ethereum/consensus-specs/blob/dev/solidity_deposit_contract/deposit_contract.sol.

## Functions

### `getRoot`

Computes and returns the Merkle root.

```solidity
  function getRoot(
  ) public returns (bytes32)
```

### `_addLeaf`

Adds a new leaf to a merkle tree.

```solidity
  function _addLeaf(
    bytes32 leaf
  ) internal
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`leaf` | bytes32 | Leaf. | 

### `verifyMerkleProof`

Verifies a Merkle proof.

```solidity
  function verifyMerkleProof(
    bytes32 leaf,
    bytes32[32] smtProof,
    uint32 index,
    bytes32 root
  ) public returns (bool)
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`leaf` | bytes32 | Leaf. | 
|`smtProof` | bytes32[32] | Smt proof. | 
|`index` | uint32 | Index of the leaf. | 
|`root` | bytes32 | Merkle root. | 
