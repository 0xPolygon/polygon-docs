## Functions

### `constructor`

Disables initializers on the implementation, following best practices.

```solidity
  function constructor(
  ) public
```

### `initialize`

```solidity
  function initialize(
  ) external
```

### `setupCommittee`

Allows the admin to setup the members of the committee. 

!!! note
    - The system requires `N/M` signatures where `N` => `_requiredAmountOfSignatures` and `M` => `urls.length`.
    - The number of urls must be the same as addresses encoded in the `addrsBytes`.
    - A member is represented by a url and the address contained in urls[i] and `addrsBytes. [i*_ADDR_SIZE : i*_ADDR_SIZE + _ADDR_SIZE]`.

```solidity
  function setupCommittee(
    uint256 _requiredAmountOfSignatures,
    string[] urls,
    bytes addrsBytes
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`_requiredAmountOfSignatures` | uint256 | Required amount of signatures
|`urls` | string[] | List of urls of the members of the committee
|`addrsBytes` | bytes | Byte array that contains the addressess of the members of the committee

### `verifyMessage`

Verifies that the given signedHash has been signed by the requiredAmountOfSignatures committee members.

```solidity
  function verifyMessage(
    bytes32 signedHash,
    bytes signaturesAndAddrs
  ) external
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`signedHash` | bytes32 | Hash that must have been signed by the requiredAmountOfSignatures of committee members
|`signaturesAndAddrs` | bytes | Byte array containing signatures and all addresses of the committee members in ascending order
[signature 0, ..., signature requiredAmountOfSignatures -1, address 0, ... address N]
note that all signatures are ECDSA, therefore each must be 65 bytes long

### `getAmountOfMembers`

Returns the number of committee members.

```solidity
  function getAmountOfMembers(
  ) public returns (uint256)
```

### `getProcotolName`

Return the protocol name.

```solidity
  function getProcotolName(
  ) external returns (string)
```

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
