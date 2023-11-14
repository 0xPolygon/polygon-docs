## Validium node

A **policy** is a set of rules that govern what actions are allowed or denied in the transaction pool. Currently, there are two defined policies:

- **SendTx**: governs whether an address may send transactions to the pool.
- **Deploy**: governs whether an address may deploy a contract.

The CDK validium node offers policy management features that include allowlisting[^1], denylisting[^2], and access control lists (ACLs)[^3]. These features are beneficial for validium-based app-chains that require fine-grained control over transaction pools. 

## Architecture

The architecture is divided into the following main components:

- **Policy management layer**: Defined in `policy.go`, this layer is responsible for the core logic of policy management.
- **Data layer**: Defined in `pgpoolstorage/policy.go`, this layer interacts with the data layer (PostgreSQL database) to store and retrieve policy and ACL data.
- **Policy definitions**: Defined in `pool/policy.go`, this layer contains the data structures and utility functions for policies and ACLs.
- **Policy interface**: Defined in `pool/interfaces.go`, this interface outlines the methods that any concrete type must implement to be considered a policy in the system.

## Policy features

- **Fine-grained control**: Developers can specify policies at a granular level, allowing or denying specific actions for specific addresses.
- **Dynamic updates**: Policies and ACLs can be updated on-the-fly without requiring a node restart.
- **Database-backed**: All policy data is stored in a PostgreSQL database.
- **Extensible**: New policies can be easily added to the system.

## Instructions for using policies

| Command name | Description                                           | Flags & parameters                                                                                      |
|--------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `policy add` | Add address(es) to a policy exclusion list            | `--policy` (or `-p`): Policy name<br/>`--csv`: CSV file with addresses                                  |
| `policy remove` | Remove address(es) from a policy exclusion list     | `--policy` (or `-p`): Policy name<br/>`--csv`: CSV file with addresses to remove                        |
| `policy clear`  | Clear all addresses from a policy's exclusion list  | `--policy` (or `-p`): Policy name                                                                       |
| `policy describe` | Describe the default actions for the policies or a specific policy | `--policy` (or `-p`): Policy name (optional)<br/>`--no-header`: Omit header in output (optional)      |
| `policy update`  | Update the default action for a policy             | `--policy` (or `-p`): Policy name<br/>`--allow`: Set policy to 'allow'<br/>`--deny`: Set policy to 'deny' |

!!! note
    For the examples, we are using a `deploy` policy.

### Add addresses to a policy

To add one or more addresses to a specific policy, you can use the `policy add` command. If you have a CSV file containing the addresses, you can use the --csv` flag.

```bash
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy add --policy deploy 0xAddress1
```

### Remove addresses from a policy

To remove addresses from a policy, you can use the `policy remove` command.

```bash
# Remove a single address from the 'deploy' policy
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy remove --policy deploy 0xAddress1

# Remove multiple addresses from the 'deploy' policy using a CSV file
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy remove --policy deploy --csv addresses.csv
```

### Clear all addresses from a policy

To remove all addresses from a policy's ACL, you can use the `policy clear` command.

```bash
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy clear --policy deploy
```

### Describing policies

To get information about a specific policy or all policies, you can use the `policy describe` command.

```bash
# Describe a specific policy
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy describe --policy deploy

# Describe all policies
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy describe
```


[^1]: **Allowlisting**: The process of explicitly allowing addresses to perform certain actions.
[^2]: **Denylisting**: The process of explicitly denying addresses from performing certain actions.
[^3]: **ACL (access control list)**: A list of addresses that are exceptions to a given policy.