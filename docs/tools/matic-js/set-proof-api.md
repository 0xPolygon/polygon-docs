!!! note

    The API links have been changed from `https://apis.matic.network` &rarr; `https://proof-generator.polygon.technology`. Please make sure to update the links.

Some of the functions in the MaticJS library are suffixed with the term `faster`. As the name suggests, they generate results more quickly compared to their non-faster counterparts. They do so by utilizing the Proof Generation API at the backend which anyone can host.

[Proof Generator](https://proof-generator.polygon.technology/) is a publicly available proof generation API, hosted by Polygon Labs.

The `setProofApi` method can help in setting the Proof Generation API’s URL to the MaticJS instance as demonstrated in the below snippet.

```js
import { setProofApi } from '@maticnetwork/maticjs'

setProofApi("https://proof-generator.polygon.technology/");
```

!!! info

    Utilizing a self-hosted Proof Generation API service will offer better performance compared to a publicly hosted one.

Please follow the installation instructions provided in the `README.md` file in [this repository](https://github.com/maticnetwork/proof-generation-api) to self-host the service.

Let's say you have deployed the Proof API and your base URL is `https://abc.xyz/`. In this case, you need to set the base URL in `setProofApi` as follows.

```js
import { setProofApi } from '@maticnetwork/maticjs'

setProofApi("https://abc.xyz/");
```

We recommend using faster APIs because some APIs, particularly where proof is being generated, make a lot of RPC calls and it might be very slow with public RPCs.
