This document explores best practices for running a Polygon PoS validator node.

!!! info "Deploying a validator node"

    Get started with the process of deploying a validator node by reading the doc on [prerequisites](../../how-to/validator/prerequisites.md).

## Owner and signer wallets

The *signer wallet* is an address that is used for signing Heimdall blocks, checkpoints, and other signing-related activities. This wallet's private key will be on the validator node for signing purposes. It cannot manage staking, rewards, or delegations.

The validator must keep two types of balances in this wallet:

- MATIC tokens on Heimdall (through top-up transactions) to perform validator responsibilities on Heimdall
- ETH on Ethereum chain to send checkpoints on Ethereum

The *owner wallet* is an address that is used for staking, re-staking, changing the signer key, withdrawing rewards, and managing delegation related parameters on the Ethereum chain. 

!!! warning

    The private key for this address **MUST** be kept secure.

All transactions through this key will be performed on the Ethereum chain.

!!! tip

    Validators are advised to take all precautions to safely generate and store wallet keys. It is important to not expose key details to anyone that does not require the information.

## Wallet setup and maintenance

- Key storage and maintenance are critically important. Use a secrets manager, or password manager for key management when setting up a wallet for your validator. If you choose to use another method, please ensure you have a solid understanding of the associated processes.
- Refer to the information provided by [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html).
- Hardware wallets can provide an additional layer of security, but do not rely on them to be completely fault proof, or to protect you in case your key is compromised.
- Rotate keys at least once a year. Also, it is important to rotate your keys if, at any point, you believe them to be compromised.
- Please do your own research for your specific needs.


## Operating system

The operating system of your choice is also a key factor in securing your validator and preventing exploitation. 

- Please keep your system up to date using common practices like using your operating system package manager, such as `yum`, `apt`, `brew`, `pacman`, etc. There are many package managers, and each one has its own best practices guide related to suggestions to follow.
- *NEVER* run unnecessary software on your node. Limit the number of services and applications running on your node.
- Run single-purpose nodes. For example, you should not run a validator as an RPC endpoint for the public to consume. This is a known issue and can be avoided by not using the node for multiple purposes.
- Validator nodes should only be running the required Bor, Heimdall, and RabbitMQ services. Anything else running on the host outside of a monitoring tool, or firewall could open you up to exploits.
- Limit access to your validator node to as few people as possible. This includes limiting SSH access only to selected people or having no access to the host at all. The fewer people with access to the nodes, the fewer potential key disclosures, accidental events, and attack surfaces.
- Accessing your machine can be accomplished in a couple of ways. On AWS, you could use an SSM or GCP cloud shell. You can also use Docker containers if you wish to rely on SSH. Please understand the risks of key and credential disclosure and any accounts that have access to the host(s).

If you require SSH access and need to expose that port publicly, the following best practices can increase the security of such access:

- SSH access should be IP-restricted and on a different port.
- SSH access should use SSH keys and not passwords.
- Disable password login.
- Disable all root access; use individual accounts with sudo.
- Add brute-force SSH protection: Fail2Ban.
- Add 2FA for SSH access.

## Networking

- Do not expose any ports publicly for your validator node. Instead, use a sentry/full node configured with port `30303` for Bor and port `26656` for Heimdall available publicly.
- Configure your validator to operate as a static node in the Bor config.toml file and as a seed node/persistent peer in the Heimdall config. This allows your validator to be isolated from the public internet and uses your sentry/full node instead of relying on unknown peers, which allows for greater security.

An example of this would look like the following:

![network setup](../../../img/pos/best-practices-1.png)

In this example, we can see the validator will send outbound requests to the network but not allow any inbound connections except for the sentry/full node we have configured to do so. Do note that this does not mean you can be careless with your network configurations and operating system maintenance for the Sentry node either. This is just a way to allow for common attack vectors to be avoided and/or mitigated. 

There are a number of ways to achieve this. If you are using AWS, you can specifically set up your security groups to only allow traffic from the sentry node to your validator, and vice versa. It is important to note that in this model, you will need to make sure that you have proper monitoring and observability tools for your network to keep an eye on things.

!!! warning "Docker and UFW"

    Be careful when using UFW to restrict ports if your services are using Docker, as Docker automatically opens the Linux firewall for ports it "maps" to the host, therefore bypassing UFW rules. For more information, check [this post](https://www.baeldung.com/linux/docker-container-published-port-ignoring-ufw-rules).

Every cloud provider provides a number of tools to allow for the use of this type of networking, including the VPC, Security Group, or equivalent tools for the provider. This method, while more secure than leaving the hosts exposed on the internet, also has an overhead with engineering time, resource management, and observability.

!!! warning "Public ports"

    A validator node, under no circumstances, should have any ports reachable by the public internet. 

In your topology, you may have other scenarios to consider. Beware of the risks involved with what ports or nodes have access to your host(s).

## Node deployment and configuration

### Ansible

You can use the available packages and a series of tools to deploy your validator node as long as you have SSH access. You may choose to forego SSH access later, but it is important to understand your tooling selection for config management. 

There are industry-standard options, such as Ansible, that can be used to deploy configurations and manage nodes simply with playbooks and roles. This public repository can also be utilized to set up your nodes: https://github.com/maticnetwork/node-ansible

!!! info "Ansible"

    See [Ansible GitHub](https://github.com/ansible/ansible) for more detailed info on Ansible and how it works.

Ansible playbooks will setup the required bootnodes, static nodes, seed nodes, and persistent peers for Bor and Heimdall, respectively. Each of the installation tools provided will set your node up with our internal nodes to bootstrap and use as a static node, persistent peer, or Heimdall seed. You may want to extend this further with other nodes, which you can add to the playbooks for your own needs and make them more useful for yourself.

### Installing Bor

An example of installing Bor with the Ansible repo for a validator would be the following command:

```bash
ansible-playbook -i $inventory playbooks/bor/bor.yml --extra-var="bor_version=v1.2.7 network=mainnet node_type=validator"
```
The `$inventory` variable is your inventory file for the IP addresses or hostnames for your nodes, depending on your setup. This playbook will install Bor and the appropriate configuration for use with the Polygon Mainnet. This setup would include your static nodes and bootnodes. 

### Installing Heimdall

To install Heimdall utilizing this repo, you would run the following playbook command: 

```bash
ansible-playbook -i $inventory playbooks/heimdall/heimdall.yml --extra-var="heimdall_version=v1.0.4 network=mainnet node_type=validator"
```

The `$inventory` variable is your inventory file containing IP addresses or hostnames for your node, depending on your setup. This will install Heimdall with the appropriate configuration. As this is a validator, it will also install the required RabbitMQ service for you. 

### Validator backup

There is also now a validator backup playbook available from the node-ansible repo. This tool will allow you to backup your current configuration for your validator. This can be quite useful for migrating to a new host. To use this tool, run the following command: 

```bash
ansible-playbook -i $inventory playbooks/validator-backup.yml -e "destination=$WHERE_YOU_WANT_TO_SAVE_LOCALLY bor_path=PATH_TO_YOUR_BOR_INSTALL heimdall_path=PATH_TO_YOUR_HEIMDALL_PATH"
```

This tool requires you to define a destination variable, the path to your Bor config location, and the path to your Heimdall config location. It will then create a tarball and store it locally on your machine in the directory path you have provided. 

### Host migration

If you are migrating a host, you may want to create an existing snapshot of your chain data for Bor and Heimdall. You can do this by running the following commands: 

```bash
ansible-playbook -i $inventory playbooks/bor/snapshot-create -e "chaindata=$path target=$target_save_dir"
ansible-playbook -i $inventory playbooks/heimdall/snapshot-create -e "data=$path target=$target_save_dir"
```

This will start a screen session while generating the tarball, which also implies that you have enough disk space on the host that you defined as your target variable to store the output. From here, you can copy the tarball to any host. 

## Monitoring and observability

If you already ship your logs to Coralogix, Datadog, or Splunk, then your monitoring will be centered around this information. You could also be using Nagios or a similar software solution to actively monitor your validator nodes. A few key things to consider when starting to monitor your node revolve around the following:

- Is the Bor service up?
- Is the Heimdall service up?
- Is the chain out of sync?
- Traffic inbound (RPC calls to your sentry)
- Disk space usage
- Memory usage
- Network usage

These factors and how to monitor them will be challenges based on what you have or do not have in place for logging and other existing tooling. Monitoring is a cost to consider when running these nodes and can ultimately provide you peace of mind as an operator. You will also want to find a balance of signal to noise ratio for the alerting, which will take some fine-tuning.