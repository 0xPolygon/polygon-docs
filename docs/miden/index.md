<div class="flex-figure" markdown="1">
<div class="flex-figure-left" markdown="1">
# Polygon Miden
Polygon Miden is a zero-knowledge (ZK) rollup running the Miden VM, a virtual machine that prioritizes ZK-friendliness over EVM compatibility. Polygon Miden uses a novel, actor-based state model to allow users to prove their own state locally, achieving high throughput and privacy at the same time. Polygon Miden is a general purpose rollup where developers can write and deploy arbitrary smart contracts.
</div>
<div class="flex-figure-right">
<img src="../img/miden/miden.svg" class="figure figure-right" alt="" />
</div>
</div>

Miden is currently in-development. A public testnet for Polygon Miden is expected in Q1 2024.

## Why build with Polygon Miden?
Polygon Miden offers features and benefits that are not available on Ethereum. Developers are empowered to build high-throughput, private dApps.

- **Beyond EVM**: Build novel applications, i.e.,  on-chain order book exchanges, complex incomplete information games, compliant and private asset management apps
- **Privacy**: Control your data with local data storage. In Polygon Miden, privacy is the cheaper option and—if you want—the network only tracks a commitment to your data
- **High throughput**: Build applications that can be used by many users at the same time. Client-side proving reduces the burden on the network and allows for parallel transaction execution
- **Safety**: Account asset storage, account abstraction, privacy, and smart contracts in Rust are less prone to bugs and less exposed to hackers
