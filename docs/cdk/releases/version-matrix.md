---
comments: true
hide:
- toc
---

## CDK component versions/releases

The table below shows the version compatibility for CDK releases and related components. 

<table>
<thead>
  <tr>
    <th>CDK version</th>
    <th>Fork ID</th>
    <th>Equivalent zkEVM node</th>
    <th>CDK validium node</th>
    <th>CDK data<br>availability</th>
    <th>zkEVM rollup node</th>
    <th>zkEVM prover</th>
    <th>Contracts</th>
    <th>Bridge</th>
  </tr>
</thead>
<tbody>
<!--
  <tr>
    <td>Rollup</td>
    <td colspan="7">Follow <a href="https://github.com/0xPolygonHermez#testnetmainnet-versions"> zkEVM </a></br><i>Disclaimer - These versions are intended for permissionless nodes</i> </td>
  </tr>-->
  <tr>
    <td>CDK Elderberry 2 Release </td>
    <td>9</td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.6.4">v0.6.4 Elderberry 2</a></td>
    <td><a href="https://hub.docker.com/layers/0xpolygon/cdk-validium-node/0.6.7-cdk.1/images/sha256-dafb15f9355331b4b7174f47ac416b275915ff24a9ed89c211c7c15c8adfc6b8?context=explore">0.6.7+cdk.1</a> </td>
    <td><a href="https://hub.docker.com/layers/0xpolygon/cdk-data-availability/0.0.7/images/sha256-17590789a831259d7a07d8a042ea87e381c5708dec3a7daef6f3f782f50b2c00?context=explore">v0.0.7</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.6.7">v0.6.7 </a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v6.0.0">v6.0.0</a></td>
    <td> <a href="https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v6.0.0-rc.1-fork.9">v6.0.0</a></td>
    <td><a href="https://hub.docker.com/layers/hermeznetwork/zkevm-bridge-service/v0.4.2-cdk.1/images/sha256-f22ad8c9ad058c7a97a3d38f53cac5b1053858916523b96211d33ae40a9b45f8?context=explore">v0.4.2-cdk.1</a></td>
  </tr>
  <!--  <td>CDK Elderberry 1 Release </td>
    <td>8</td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.6.2">v0.6.2 Elderberry</a></td>
    <td><a href="https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.6.2%2Bcdk4">0.6.2+cdk.4</a> </td>
    <td><a href="https://hub.docker.com/layers/0xpolygon/cdk-data-availability/0.0.6-hotfix1/images/sha256-e95ef2cd9110aff8acdd29065f407f04ea6179f71a7848d78eaf0dd73c858207?context=explore">v0.0.6-hotfix1</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v5.0.7">v5.0.7</a></td>
    <td> <a href="https://github.com/0xPolygonHermez/zkevm-contracts/releases/tag/v5.0.1-rc.2-fork.8">v5.0.1</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.4.2">v0.4.2</a></td>
  </tr>
  <tr>
    <td><a href="https://polygontechnology.notion.site/Instructions-zkEVM-Mainnet-Beta-Node-v0-5-7-Prover-v4-0-4-8f5b9d8e2f6a4048b21c608b49a93376" target="_blank" rel="noopener noreferrer">CDK-Etrog Release</a>- <br>BETA TESTING</td>
    <td>7</td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.5.13">v0.5.13 </a>(Etrog+uLxLy)</td>
    <td><a href="https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.5.13%2Bcdk.10">v0.5.13+cdk.10</a> </td>
    <td><a href="https://hub.docker.com/layers/0xpolygon/cdk-data-availability/0.0.6-hotfix1/images/sha256-e95ef2cd9110aff8acdd29065f407f04ea6179f71a7848d78eaf0dd73c858207?context=explore">v0.0.6-hotfix1</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v4.0.19">v4.0.19</a></td>
    <td> <a href="https://github.com/0xPolygonHermez/zkevm-rom/tree/v4.0.0-fork.7">v4.0.0</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.4.2">v0.4.2</a></td>
  </tr>
  <tr>
    <td>Upgraded validium</td>
    <td>6</td>
    <td>0.4.2</td>
    <td><a href="https://github.com/0xPolygon/cdk-validium-node/releases/tag/v0.0.3-hotfix6">v0.0.3-hotfix6</a></td>
    <td>v0.0.3</td>
    <td>zkevm-prover<br>@3.0.2<br>Config files version 3.0.0-RC3-fork.6</td>
    <td><a href="https://github.com/0xPolygon/cdk-validium-contracts/releases/tag/v0.0.2">v0.0.2</a></td>
    <td>v0.3.2-RC1</td> 
  </tr>-->
</tbody>
</table>

### Migrating

- Anyone on earlier versions, we recommend going straight to fork ID 9.

<!--
## zkEVM

The table below shows the version compatibility for Polygon zkEVM releases.

<table>
<thead>
  <tr>
    <th>Node </th>
    <th>Bridge</th>
    <th>Prover</th>
    <th>Fork ID</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.6.4">v0.6.4 </a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.4.2">v0.4.2</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v6.0.0">v6.0.0</a></td>
    <td>Mainnet &amp; Cardona: 4-9 <br>Testnet (Goerli): 1-6</td>
  </tr>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.6.2">v0.6.2 </a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.4.2">v0.4.2</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v5.0.7">v5.0.7</a></td>
    <td>Mainnet &amp; Cardona: 4-8. <br>Testnet (Goerli): 1-6</td>
  </tr>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/tag/v0.5.13">v0.5.13</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-bridge-service/releases/tag/v0.4.2">v0.4.2</a></td>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-prover/releases/tag/v4.0.19">v4.0.19</a></td>
    <td>Mainnet &amp; Cardona: 4-7. <br>Testnet (Goerli): 1-6</td>
  </tr>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/v0.4.0">v0.4.0</a></td>
    <td>v0.3.0</td>
    <td>v3.0.2</td>
    <td rowspan="2">Testnet: 1-6<br>Mainnet: 4-6</td>
  </tr>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/v0.3.3">v0.3.3</a></td>
    <td>v0.2.0</td>
    <td>v3.0.0</td>
  </tr>
  <tr>
    <td><a href="https://github.com/0xPolygonHermez/zkevm-node/releases/v0.3.1">v0.3.1</a> </td>
    <td> v0.2.0</td>
    <td>v2.2.2</td>
    <td>Testnet:  <br>1 - 5 Mainnet: 4-5 </td>
  </tr>
</tbody>
</table>
-->

