
This document provides a comprehensive list of seeds and bootnodes for both the Mainnet and Amoy Testnet, including Bor and Heimdall.


!!! info
    
    You don't need to configure seeds separately for the Amoy Testnet, as they are already included in the genesis file. However, if you're having trouble connecting to peers, feel free to use them.

## PoS mainnet

!!! info "Selecting a URL"

    Triple-click a URL to select it, and then copy it using the appropriate keyboard shortcut.

### Bor

```bash
enode://48e6326841ce106f6b4e229a1be7e98a1d12be57e328b08cb461f6744ae4e78f5ec2340996ce9b40928a1a90137aadea13e25ca34774b52a3600d13a52c5c7bb@34.185.209.56:30303
enode://8ab6905fe76aa9001adb77135250e918db888cac216870c0e95cf26650d83d31d8c2c93d54c3333e0a2196517c41651d174b743ec3e11f44e595f62b77fec7ba@34.185.162.14:30303
enode://02e0b33cf60fb1f88f853c7c04830156151f4acd1c36173cd3fe1f375801fb4f5be5b3a89c98527915d37ed217752933c3faf4c820df740c9dd681294caebcf6@34.179.171.228:30303
enode://079c387b65b09674825462ea63c528ca996af7b03d19b1b2ab6557347434838067db6dd7ae5e0c2e08d5ba164117f3d7faffbf3e890cb91cffbdf45a433ddfce@35.246.166.189:30303
enode://191d06720948ae0119343e5798098f5b1f95a308174c4119d226da91833bc0176009bcc8bf5012e490500562d4d5b5427c307b01f3485b2e8351ac5afd946864@34.142.28.190:30303
enode://30a4651b245e9a0cec674b9ecb5a06ca01553aa727e14a77d0f1ccdb9e48a975f3be631505f417aae438be545ac3b290cd3ed00bef96efd7fb0fb7f916397b3f@34.39.56.114:30303
enode://b950b98b92e118551d79c7280b97ddfcdf3dacb620367ebd45e8382f8e69390df192055386221025ffd3c03912da2aadf668ae6ea7b35f391d82ef87452b3f02@34.147.169.102:30303
enode://92ef18168f6c281a313d0ca76d6122b913a101352b5069af9cea6c8dd0f8b51d669601d59fdf250e972cf9a547d8a10f21ecf5b99ce8511605f328e5f66e845f@34.105.180.11:30303
```

### Heimdall

```bash
a0ef6f328949adc077c59ab1f6b03711ae8d32d2@34.185.209.56:26656
f1e632758dfaf616a833900c0b8845bb2547b7c2@34.185.162.14:26656
e49bb5d9cb22943fb2b9f49a4c5d0f773917efaf@34.179.171.228:26656
babb8151d6fae45fcbb9229bd9faba173f3feaf3@35.246.166.189:26656
9c92984a5aad02c43955da94bb0a979a8dadbcfe@34.142.28.190:26656
3643aeae6a5965053709303e97257f62012fdd9c@34.39.56.114:26656
830d44b0d11ab25c9a03135859049d55daf73a03@34.147.169.102:26656
b0e795afc432ea3557b377d7763f6fb6dd102e60@34.105.180.11:26656
```

## Amoy testnet

### Bor

```bash
enode://d40ab6b340be9f78179bd1ec7aa4df346d43dc1462d85fb44c5d43f595991d2ec215d7c778a7588906cb4edf175b3df231cecce090986a739678cd3c620bf580@34.89.255.109:30303
enode://13abba15caa024325f2209d3566fa77cd864281dda4f73bca4296277bfd919ac68cef4dbb508028e0310a24f6f9e23c761fa41ac735cdc87efdee76d5ff985a7@34.185.137.160:30303
enode://fc5bd3856a4ce6389eef1d6bc637ce7617e6ba8013f7d722d9878cf13f1c5a5a95a9e26ccb0b38bcc330343941ce117ab50db9f61e72ba450dd528a1184d8e6a@34.89.119.250:30303
enode://945e11d11bdeed301fb23a5c05aae77bfdde39a8f70308131682a5d2fc1f080531314554afc78718a72ae25cc09be7833f760bf8681516b4315ed36217fa8dab@34.89.40.235:30303
```

### Heimdall

```bash
be818a0ebc61a8ffefdfaf4d3fcfed72ca2d7188@34.89.255.109:26656
81a5aa40d8bf6782e6f3fb0498406ebe707e576c@34.185.137.160:26656
42b0aa4c784a93c4797ff965d75793e099dc0b11@34.89.119.250:26656
5d532264fe8592bf8c1dc8abfa11ff52b381eb2c@34.89.40.235:26656
```

Alternatively, you can find more seeds [here](https://docs.stakepool.dev.br/polygon/live-peers).

## Enhancing Bor Peering with DNS Discovery

To further enhance bor peering capabilities, the DNS discovery flag can be utilized. The ENR trees for the mainnet and Amoy testnet are provided below:

* **Mainnet** - `enrtree://AKUEZKN7PSKVNR65FZDHECMKOJQSGPARGTPPBI7WS2VUL4EGR6XPC@pos.polygon-peers.io`
* **Amoy Testnet** - `enrtree://AKUEZKN7PSKVNR65FZDHECMKOJQSGPARGTPPBI7WS2VUL4EGR6XPC@amoy.polygon-peers.io`

### Configuration Steps

To configure DNS discovery, follow these steps:

1. Edit your `config.toml` file:
   * Locate the `[p2p]` section.
   * Set `maxpeers` to:
       * 2000 for Mainnet
       * 500 for Amoy Testnet
   * Set `maxpendpeers` to:
       * 500 for Mainnet
       * 100 for Amoy testnet
2. Add the DNS under `[p2p.discovery]` section.

!!! note

    Increasing the number of peers can significantly enhance node connectivity, enabling connection to hundreds of peers almost instantly. However, please be aware that this adjustment may lead to increased bandwidth usage. Adjusting maxpeers and maxpendpeers is optional but can improve peering efficiency. Read more [here](https://forum.polygon.technology/t/introducing-our-new-dns-discovery-for-polygon-pos-faster-smarter-more-connected/19871).
