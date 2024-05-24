A contract that inherits `AccessControlUpgradeable` from Openzeppelin, but with the following modifications:

- Delete `ERC165Upgradeable` dependencies to save us the "gap" variables and let us have consistent storage.
- Add the legacy `Owner` variable, to be consistent with the previous.
- Add custom errors.
- Replace `_msgSender()` with `msg.sender`.

## Functions

### `__AccessControl_init`

```solidity
  function __AccessControl_init(
  ) internal
```

### `hasRole`

Returns `true` if `account` has been granted `role`.

```solidity
  function hasRole(
  ) public returns (bool)
```

### `_checkRole`

```solidity
  function _checkRole(
  ) internal
```

- Reverts with a standard message if `msg.sender` is missing `role`. Overriding this function changes the behavior of the {onlyRole} modifier.
- Describes the format of the revert message in `{_checkRole}`.
- _Available since v4.6._

### `_checkRole`

```solidity
  function _checkRole(
  ) internal
```

- Reverts with a standard message if `account` is missing `role`.
- The format of the revert reason is given by the following regular expression:

 /^AccessControl: account (0x[0-9a-f]{40}) is missing role (0x[0-9a-f]{64})$/

### `getRoleAdmin`

Returns the admin role that controls `role`. See `grantRole` and `revokeRole`.

```solidity
  function getRoleAdmin(
  ) public returns (bytes32)
```

To change a role's admin, use `_setRoleAdmin`.

### `grantRole`

Grants `role` to `account`. If `account` had not been already granted `role`, it emits a `RoleGranted` event.

```solidity
  function grantRole(
  ) public
```

- The caller must have `role`'s admin role.
- May emit a `RoleGranted` event.

### `revokeRole`

Revokes `role` from `account`. If `account` had been granted `role`, emits a `RoleRevoked` event.

```solidity
  function revokeRole(
  ) public
```



### `renounceRole`

Revokes `role` from the calling account.

```solidity
  function renounceRole(
  ) public
```

- The caller must have `account`'s admin role.
- May emit a `RoleRevoked` event.

Roles are often managed via `grantRole` and `revokeRole`. The purpose of this function is to provide a mechanism for accounts to lose their privileges if they are compromised (such as when a trusted device is misplaced).

Emits a `RoleRevoked`event if the calling account had `role` revoked.

### `_setupRole`

```solidity
  function _setupRole(
  ) internal
```

Grants `role` to `account`.

Emits a `RoleGranted`event if `account` had not been already granted `role`. 
Note that unlike `grantRole`, this function doesn't perform any checks on the calling account.

May emit a `RoleGranted` event.

!!! warn
    - This function should only be called from the constructor when setting up the initial roles for the system.
    - Using this function in any other way is effectively circumventing the admin system imposed by `AccessControl`.

!!! note
    - This function is deprecated in favor of `_grantRole`.

### `_setRoleAdmin`

Sets `adminRole` as `role`'s admin role.

```solidity
  function _setRoleAdmin(
  ) internal
```

Emits a `RoleAdminChanged` event.

### `_grantRole`

Grants `role` to `account`. Internal function without access restriction.

```solidity
  function _grantRole(
  ) internal
```

May emit a `RoleGranted` event.

### `_revokeRole`

Revokes `role` from `account`. Internal function without access restriction.

```solidity
  function _revokeRole(
  ) internal
```

May emit a `RoleRevoked` event.
