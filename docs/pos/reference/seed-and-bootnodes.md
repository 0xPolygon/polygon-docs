
This document provides a comprehensive list of seeds and bootnodes for both the Mainnet and Amoy Testnet, including Bor and Heimdall.


!!! info
    
    You don't need to configure seeds separately for the Amoy Testnet, as they are already included in the genesis file. However, if you're having trouble connecting to peers, feel free to use them.

## PoS mainnet

!!! info "Selecting a URL"

    Triple-click a URL to select it, and then copy it using the appropriate keyboard shortcut.

### Bor

```bash
enode://07bc4cf87ff8f4e7dc51280991809940f26e846c944609ae4726309be73742a830040cd783989f6941e1b41c02405834bc6365059403a59ca9255ac695156235@34.89.75.187:30303
enode://2c3be2e637a68dc694498a44b6e0d57b5c762925ea97f941079a91f8a080b032fe2eb9e6c3230076e9fb046f626b5dcd3fb045dc9c194689a359aa7167ae0f6c@34.142.43.249:30303
enode://a0bc4dd2b59370d5a375a7ef9ac06cf531571005ae8b2ead2e9aaeb8205168919b169451fb0ef7061e0d80592e6ed0720f559bd1be1c4efb6e6c4381f1bdb986@35.246.99.203:30303
enode://f2b0d50e0b843d38ddcab59614f93065e2c82130100032f86ae193eb874505de12fcaf12502dfd88e339b817c0b374fa4b4f7c4d5a4d1aa04f29c503d95e0228@35.197.233.240:30303
enode://8a3f21c293c913a1148116a295aa69fdf41b9c5b0b0628d49be751aa8c025ae2ec1973d6d84cea8e2aba5541b5d76219dfaae41a124d42d0f56d4e1af50b74f8@35.246.95.65:30303
enode://f5cfe35f47ed928d5403aa28ee616fd64ed7daa527b5ae6a7bc412ca25eaad9b6bf2f776144fd9f8e7e9c80b5360a9c03b67f1d47ea88767def7d391cc7e0cd1@34.105.180.11:30303
enode://fc7624241515f9d5e599a396362c29de92b13a048ad361c90dd72286aa4cca835ba65e140a46ace70cc4dcb18472a476963750b3b69d958c5f546d48675880a8@34.147.169.102:30303
enode://7400e4bc70c56de26d5d240474a1b78af0bf8f0db567edfa851c9724ed697ca7692a92483369e9633d4342a036d10223958007160765d0317a1073f86f2a80c8@34.89.55.74:30303
```

### Heimdall

```bash
7f3049e88ac7f820fd86d9120506aaec0dc54b27@34.89.75.187:26656
1f5aff3b4f3193404423c3dd1797ce60cd9fea43@34.142.43.249:26656
2d5484feef4257e56ece025633a6ea132d8cadca@35.246.99.203:26656
17e9efcbd173e81a31579310c502e8cdd8b8ff2e@35.197.233.240:26656
72a83490309f9f63fdca3a0bef16c290e5cbb09c@35.246.95.65:26656
00677b1b2c6282fb060b7bb6e9cc7d2d05cdd599@34.105.180.11:26656
721dd4cebfc4b78760c7ee5d7b1b44d29a0aa854@34.147.169.102:26656
4760b3fc04648522a0bcb2d96a10aadee141ee89@34.89.55.74:26656
```

## Amoy testnet

### Bor

```bash
enode://0ef8758cafc0063405f3f31fe22f2a3b566aa871bd7cd405e35954ec8aa7237c21e1ccc1f65f1b6099ab36db029362bc2fecf001a771b3d9803bbf1968508cef@35.197.249.21:30303
enode://c9c8c18cde48b41d46ced0c564496aef721a9b58f8724025a0b1f3f26f1b826f31786f890f8f8781e18b16dbb3c7bff805c7304d1273ac11630ed25a3f0dc41c@34.89.39.114:30303
enode://5b8d436677fb545b1c3fd1ae84553d478d9d21ad3b06a908b9d34d2df367ead5bb8823d84a370e26bdde8896ba8a870e21ba3a6dce19c0ded086296df5f04f15@35.242.167.175:30303
enode://a2ec3671e553ba3e711639033912be55fe1e7fa4b61a93f6a1ac0cd3cea34f9d7eec1d718e04049531cf5dd7efc1ac677df1cf0e1f24f5e677706d7bcb3917de@34.105.128.110:30303
enode://9e15bc58779c32119140d54a8384940b57a10a001506ce173cc4cdb10876b14a2ac9ae91f9389caf9fd385c3b72825f8bbbe937e7e57b1f032561703e900da59@34.89.21.99:30303
enode://42203e9b423aba24e1e9386f94d0d0397a42770427e8e9e22f9e2a9523f66abb13b1f5a6addee68ad5986f94a8f6de626f5829492599a2f9484f98e86e26149d@34.89.101.16:30303
```

### Heimdall

```bash
2e6f1342416c5d758f5ae32f388bb76f7712a317@34.89.101.16:26656
2833f06a5e33da2e80541fb1bfde2a7229877fcb@34.89.21.99:26656
2f16f3857c6c99cc11e493c2082b744b8f36b127@34.105.128.110:26656
2ec15d1d33261e8cf42f57236fa93cfdc21c1cfb@35.242.167.175:26656
811c3127677a4a34df907b021aad0c9d22f84bf4@34.89.39.114:26656
e4eabef3111155890156221f018b0ea3b8b64820@35.197.249.21:26656
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
