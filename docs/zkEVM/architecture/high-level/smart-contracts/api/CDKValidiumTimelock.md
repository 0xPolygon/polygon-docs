Contract module which acts as a time-locked controller.
It provides time, for users of the controlled contract, to exit before any risky maintenance operation is applied.

However, if the emergency mode of the CDKValidium contract system is active, any timelock is bypassed without delay.

## Functions

### constructor

```solidity
  function constructor(
    uint256 minDelay,
    address[] proposers,
    address[] executors,
    address admin,
    contract CDKValidium _cdkValidium
  ) public
```

##### Parameters

| Name | Type | Description                                                          |
| :--- | :--- | :------------------------------------------------------------------- |
|`minDelay` | uint256 | initial minimum delay for operations
|`proposers` | address[] | accounts to be granted proposer and canceller roles
|`executors` | address[] | accounts to be granted executor role
|`admin` | address | optional account to be granted admin role; disable with zero address
|`_cdkValidium` | contract CDKValidium | cdkValidium address

### getMinDelay

Returns the minimum delay for an operation to become valid.

```solidity
  function getMinDelay(
  ) public returns (uint256 duration)
```

The minimum delay value can be changed by executing any operation that calls `updateDelay`. If CDKValidium is in an emergency state the `minDelay` is 0 instead.
