## Test transactions

Once everything is up and running you can do a quick test of the running stack by sending a zero-value transaction.

Run the following command where the mnemonic is for testing and the address can be any account address.

```sh
cast send --legacy --mnemonic 'code code code code code code code code code code code quality' --value 0 --gas-price 0 --rpc-url http://127.0.0.1:8123 0x0bb7AA0b4FdC2D2862c088424260e99ed6299148
```

You should see something like this as output:

```sh
blockHash               0x5d6d45f46e54c5d0890dd8a4ede989dc8042d7d3aeada375ea11d2e77c91a298
blockNumber             1
contractAddress        
cumulativeGasUsed       21000
effectiveGasPrice       0
from                    0x85dA99c8a7C2C95964c8EfD687E95E632Fc533D6
gasUsed                 21000
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    0x97b15537641583db08f1e3db15cb1e89212ed8d147670a11f93f368d5960e72f
status                  1
transactionHash         0xd5443cff8dcc1147ead09d978d3abe9179615aa3eecbe4819c6768390bc467a3
transactionIndex        0
type                    0
to                      0x66ec…89fd
```

Status `1` signifies a successful transaction.