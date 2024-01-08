!!! caution "Content disclaimer"
    Please view the third-party content disclaimer [here](https://github.com/0xPolygon/polygon-docs/blob/main/CONTENT_DISCLAIMER.md).

### Context

Polygon blockchain reduces transaction costs to store data versus Ethereum mainnet; however, even these lower costs add up quickly when storing sizable files. Developers also must consider block size constraints and transaction speed limitations when storing data onchain. One solution which addresses all of these concerns is IPFS, the InterPlanetary File System.

#### What is IPFS?

IPFS is a distributed system for storing and accessing files, websites, applications, and data. IPFS uses decentralization, content addressing, and a robust peer-to-peer network of active participants to allow users to store, request, and transfer verifiable data with each other.

Decentralization makes it possible to download a file from many locations that aren't managed by one organization, providing resilience and censorship resistance right out of the box.

Content addressing uses cryptography to create a uniquely verifable hash based upon what is in a file rather than where it is located. The resulting content identifier (CID) provides assurance a piece of data is identical regardless of where it is stored.

Finally, an ever growing active community of users makes this peer-to-peer sharing of content possible. Developers upload and pin content to IPFS while Filecoin or Crust storage providers help to ensure persistent storage of that content.

IPFS based storage allows you to simply store the CID for your content rather than loading entire files to Polygon blockchain; allowing for decreased costs, larger file sizes, and provably persistent storage. For more details refer [IPFS Docs](https://docs.ipfs.io/).

### Example projects

1. Tutorial in scaffold-eth that demonstrates how to mint an NFT on Polygon with IPFS - [link](https://github.com/scaffold-eth/scaffold-eth/tree/simple-nft-example).

2. Building a full stack web3 app with Next.js, Polygon, Solidity, The Graph, IPFS, and Hardhat - [link](https://dev.to/dabit3/the-complete-guide-to-full-stack-web3-development-4g74).
