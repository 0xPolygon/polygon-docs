## Functions

### `initialize`

```solidity
  function initialize(
  ) external
```

### `setupCommittee`

Allows the admin to setup members of the committee. 

```solidity
  function setupCommittee(
    uint256 _requiredAmountOfSignatures,
    string[] urls,
    bytes addrsBytes
  ) external
```

!!! note
    - The system requires N/M signatures where N => `_requiredAmountOfSignatures` and M => `urls.length`.
    - The number of urls must be the same as the addresses encoded in the `addrsBytes`.
    - A member is represented by a url and the address contained in `urls[i]` and `addrsBytes[i*_ADDR_SIZE : i*_ADDR_SIZE + _ADDR_SIZE]`.


##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_requiredAmountOfSignatures` | uint256 | Required amount of signatures
|`urls` | string[] | List of urls of the members of the committee
|`addrsBytes` | bytes | Byte array that contains the addressess of the members of the committee

### `getAmountOfMembers`

```solidity
  function getAmountOfMembers(
  ) public returns (uint256)
```

### `verifySignatures`

Verifies that the given `signedHash` has been signed by `requiredAmountOfSignatures` committee members.

```solidity
  function verifySignatures(
    bytes32 signedHash,
    bytes signaturesAndAddrs
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`signedHash` | bytes32 | Hash that must have been signed by requiredAmountOfSignatures of committee members
|`signaturesAndAddrs` | bytes | Byte array containing the signatures and all the addresses of the committee in ascending order
[signature 0, ..., signature requiredAmountOfSignatures -1, address 0, ... address N]
note that each ECDSA signatures are used, therefore each one must be 65 bytes

## Events

### `CommitteeUpdated`

Emitted when the committee is updated.

```solidity
  event CommitteeUpdated(
    bytes32 committeeHash
  )
```

##### Parameters

| Name                           | Type          | Description                                    |
| :----------------------------- | :------------ | :--------------------------------------------- |
|`committeeHash`| bytes32 | hash of the addresses of the committee members |

