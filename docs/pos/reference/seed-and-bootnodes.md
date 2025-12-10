
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
