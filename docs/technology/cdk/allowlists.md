---
id: allowlists
title: CDK Validium Allowlists
sidebar_label: Allowlists
description: "Learn about allowlists and access control in the Polygon CDK."
keywords:
  - docs
  - polygon
  - layer 2
  - validium
  - allowlist
  - access
  - access control
  - acl
---

The CDK Validium node offers policy management features, including allowlisting and Access Control Lists (ACLs). These features are particularly beneficial for Validium-based app-chains that require fine-grained control over transaction pools. It is the Sequencer node that enforces these policies, and any change operations should be applied directly through the Sequencer. This document provides an overview on these administrative capabilities and explains how to use them.

## Key Concepts

- **Policy**: A set of rules that govern what actions are allowed or denied in the transaction pool. Currently, there are two defined policies:
   - **SendTx**: Governs whether an address may send transactions to the pool.
   - **Deploy**: Governs whether an address may deploy a contract.
- **ACL (Access Control List)**: A list of addresses that are exceptions to a given policy.
- **Allowlisting**: The process of explicitly allowing addresses to perform certain actions.
- **Denylisting**: The process of explicitly denying addresses from performing certain actions.

## Architecture

The architecture is divided into the following main components:

- **Policy Management Layer**: Defined in `policy.go`, this layer is responsible for the core logic of policy management.
- **Data Layer**: Defined in `pgpoolstorage/policy.go`, this layer interacts with the data layer (PostgreSQL database) to store and retrieve policy and ACL data.
- **Policy Definitions**: Defined in `pool/policy.go`, this layer contains the data structures and utility functions for policies and ACLs.
- **Policy Interface**: Defined in `pool/interfaces.go`, this interface outlines the methods that any concrete type must implement to be considered a policy in the system.

## Capabilities

- **Fine-Grained Control**: Developers can specify policies at a granular level, allowing or denying specific actions for specific addresses.
- **Dynamic Updates**: Policies and ACLs can be updated on-the-fly without requiring a node restart.
- **Database-Backed**: All policy data is stored in a PostgreSQL database.
- **Extensible**: New policies can be easily added to the system.

## How to Use Policies

| Command Name | Description                                           | Flags & Parameters                                                                                      |
|--------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `policy add` | Add address(es) to a policy exclusion list            | `--policy` (or `-p`): Policy name<br/>`--csv`: CSV file with addresses                                  |
| `policy remove` | Remove address(es) from a policy exclusion list     | `--policy` (or `-p`): Policy name<br/>`--csv`: CSV file with addresses to remove                        |
| `policy clear`  | Clear all addresses from a policy's exclusion list  | `--policy` (or `-p`): Policy name                                                                       |
| `policy describe` | Describe the default actions for the policies or a specific policy | `--policy` (or `-p`): Policy name (optional)<br/>`--no-header`: Omit header in output (optional)      |
| `policy update`  | Update the default action for a policy             | `--policy` (or `-p`): Policy name<br/>`--allow`: Set policy to 'allow'<br/>`--deny`: Set policy to 'deny' |

We will use the "deploy" policy as an example.

### Adding Addresses to a Policy

To add one or more addresses to a specific policy, you can use the `policy add` command. If you have a CSV file containing the addresses, you can use the --csv` flag.

```bash
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy add --policy deploy 0xAddress1
```

### Removing Addresses from a Policy

To remove addresses from a policy, you can use the `policy remove` command.

```bash
# Remove a single address from the 'deploy' policy
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy remove --policy deploy 0xAddress1

# Remove multiple addresses from the 'deploy' policy using a CSV file
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy remove --policy deploy --csv addresses.csv
```

### Clearing All Addresses from a Policy

To remove all addresses from a policy's ACL, you can use the `policy clear` command.

```bash
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy clear --policy deploy
```

### Describing Policies

To get information about a specific policy or all policies, you can use the `policy describe` command.

```bash
# Describe a specific policy
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy describe --policy deploy

# Describe all policies
docker exec -it cdk-validium-aggregator /app/cdk-validium-node policy describe
```
