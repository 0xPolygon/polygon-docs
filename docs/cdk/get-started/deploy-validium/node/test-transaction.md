# Test Transaction

At the end of the tutorial, there should be some commands in order to verify that everything is working. If you follow the document as-is, you would probably need to do a bridge in order to get any value on L2. So it would probably be useful to show how to do that.

Alternatively, we should probably run the genesis creation step with the `--test` flag in order to start L2 with some pre-mined value. Users in Discord seem to be trying to modify the [1createGenesis.js](https://github.com/0xPolygon/cdk-validium-contracts/blob/c6743885226690788b3474fa216622023f48bd98/deployment/1_createGenesis.js#L297) file to get value on L2 by default. This should work as well.

One quick way to verify that transactions can be mined is to send a zero-priced transaction. E.g