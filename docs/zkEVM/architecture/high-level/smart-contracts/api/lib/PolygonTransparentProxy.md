
Inherits from contract `TransparentUpgradeableProxy` from Openzeppelin v5 with the following modifications:

- Admin is a parameter in the constructor instead of being deployed.
- Let the admin get access to the proxy.
- Replace `_msgSender()` with `msg.sender`

## Functions

### `constructor`

Initializes an upgradeable proxy managed by an instance of a `ProxyAdmin` with an `initialOwner` backed by the implementation at `_logic`, and optionally initialized with `_data` as explained in `ERC1967Proxy-constructor`.

```solidity
  function constructor(
  ) public
```

### `_proxyAdmin`

Returns the admin of this proxy.

```solidity
  function _proxyAdmin(
  ) internal returns (address)
```

### `_fallback`

If caller is the admin process the call internally, otherwise transparently fallback to the proxy behavior.

```solidity
  function _fallback(
  ) internal
```
