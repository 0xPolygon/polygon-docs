---
hide:
- toc
---

Endpoint details are listed in the [playground](#playground) doc below.

## How to call a method with the terminal

Use the Cardona testnet https://rpc.cardona.zkevm-rpc.com to test the [endpoint methods](#playground) in a terminal. For example: 

### `zkevm_estimateGasPrice`

```sh
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"zkevm_estimateGasPrice","params":[{"from":"0x0000000000000000000000000000000000000001","to":"0x0000000000000000000000000000000000000002","value":"0x1"}],"id":1}' \
    https://rpc.cardona.zkevm-rpc.com
```

#### Result

```sh
{"jsonrpc":"2.0","id":1,"result":"0xe2ea2f0"}
```

## JSON RPC API source 

??? "JSON API source"
    ```json
    {
        "openrpc": "1.0.0-rc1",
        "info": {
          "title": "zkEVM Endpoints",
          "version": "2.0.0"
        },
        "methods": [
          {
            "name": "zkevm_consolidatedBlockNumber",
            "summary": "Returns the latest block number that is connected to the latest batch verified.",
            "params": [],
            "result": {
              "$ref": "#/components/contentDescriptors/BlockNumber"
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": "0x1"
                }
              }
            ]
          },
          {
            "name": "zkevm_isBlockVirtualized",
            "summary": "Returns true if the provided block number is already connected to a batch that was already virtualized, otherwise false.",
            "params": [
              {
                "name": "blockNumber",
                "schema": {
                  "$ref": "#/components/contentDescriptors/BlockNumber"
                }
              }
            ],
            "result": {
              "name": "result",
              "schema": {
                "type": "boolean"
              }
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": true
                }
              }
            ]
          },
          {
            "name": "zkevm_isBlockConsolidated",
            "summary": "Returns true if the provided block number is already connected to a batch that was already verified, otherwise false.",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/BlockNumber"
              }
            ],
            "result": {
              "name": "result",
              "schema": {
                "type": "boolean"
              }
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": true
                }
              }
            ]
          },
          {
            "name": "zkevm_batchNumber",
            "summary": "Returns the latest batch number.",
            "params": [],
            "result": {
              "$ref": "#/components/contentDescriptors/BatchNumber"
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": "0x1"
                }
              }
            ]
          },
          {
            "name": "zkevm_virtualBatchNumber",
            "summary": "Returns the latest virtual batch number.",
            "params": [],
            "result": {
              "$ref": "#/components/contentDescriptors/BatchNumber"
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": "0x1"
                }
              }
            ]
          },
          {
            "name": "zkevm_verifiedBatchNumber",
            "summary": "Returns the latest verified batch number.",
            "params": [],
            "result": {
              "$ref": "#/components/contentDescriptors/BatchNumber"
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": "0x1"
                }
              }
            ]
          },
          {
            "name": "zkevm_batchNumberByBlockNumber",
            "summary": "Returns the batch number of the batch connected to the block.",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/BlockNumber"
              }
            ],
            "result": {
              "$ref": "#/components/contentDescriptors/BatchNumber"
            },
            "examples": [
              {
                "name": "example",
                "description": "",
                "params": [],
                "result": {
                  "name": "exampleResult",
                  "description": "",
                  "value": "0x1"
                }
              }
            ]
          },
          {
            "name": "zkevm_getBatchByNumber",
            "summary": "Gets a batch for a given number",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/BatchNumberOrTag"
              },
              {
                "name": "includeTransactions",
                "description": "If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.",
                "required": true,
                "schema": {
                  "title": "isTransactionsIncluded",
                  "type": "boolean"
                }
              }
            ],
            "result": {
              "$ref": "#/components/contentDescriptors/Batch"
            },
            "examples": [
              {
                "name": "batch without tx details",
                "description": "Batch without transaction details",
                "params": [
                  {
                    "name": "batch number",
                    "value": "0x1"
                  },
                  {
                    "name": "include txs",
                    "value": "false"
                  }
                ],
                "result": {
                  "name": "Batch",
                  "value": {
                    "number": "0x1",
                    "coinbase": "0x0000000000000000000000000000000000000001",
                    "stateRoot": "0x0000000000000000000000000000000000000000000000000000000000000001",
                    "globalExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000002",
                    "mainnetExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000003",
                    "rollupExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000004",
                    "localExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000005",
                    "accInputHash": "0x0000000000000000000000000000000000000000000000000000000000000006",
                    "timestamp": "0x642af31f",
                    "sendSequencesTxHash": "0x0000000000000000000000000000000000000000000000000000000000000007",
                    "verifyBatchTxHash": "0x0000000000000000000000000000000000000000000000000000000000000008",
                    "transactions": [
                      "0x0000000000000000000000000000000000000000000000000000000000000009",
                      "0x0000000000000000000000000000000000000000000000000000000000000010",
                      "0x0000000000000000000000000000000000000000000000000000000000000011"
                    ]
                  }
                }
              },
              {
                "name": "batch with tx detail",
                "description": "Batch with transaction details",
                "params": [
                  {
                    "name": "batch number",
                    "value": "0x1"
                  },
                  {
                    "name": "include txs",
                    "value": "true"
                  }
                ],
                "result": {
                  "name": "Batch",
                  "value": {
                    "number": "0x1",
                    "coinbase": "0x0000000000000000000000000000000000000001",
                    "stateRoot": "0x0000000000000000000000000000000000000000000000000000000000000001",
                    "globalExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000002",
                    "mainnetExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000003",
                    "rollupExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000004",
                    "localExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000005",
                    "accInputHash": "0x0000000000000000000000000000000000000000000000000000000000000006",
                    "timestamp": "0x642af31f",
                    "sendSequencesTxHash": "0x0000000000000000000000000000000000000000000000000000000000000007",
                    "verifyBatchTxHash": "0x0000000000000000000000000000000000000000000000000000000000000008",
                    "transactions": [
                      {
                        "nonce": "0x1",
                        "gasPrice": "0x123456",
                        "gas": "0x59D8",
                        "to": "0x0000000000000000000000000000000000000002",
                        "value": "0x1",
                        "input": "0x",
                        "v": "0xAAA",
                        "r": "0x0000000000000000000000000000000000000000000000000000000000000010",
                        "s": "0x0000000000000000000000000000000000000000000000000000000000000011",
                        "hash": "0x0000000000000000000000000000000000000000000000000000000000000012",
                        "from": "0x0000000000000000000000000000000000000003",
                        "blockHash": "0x0000000000000000000000000000000000000000000000000000000000000013",
                        "blockNumber": "0x1",
                        "transactionIndex": "0x0",
                        "chainId": "0x539",
                        "type": "0x0"
                      }
                    ]
                  }
                }
              }
            ]
          },
          {
            "name": "zkevm_getFullBlockByNumber",
            "summary": "Gets a block with extra information for a given number",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/BlockNumber"
              },
              {
                "name": "includeTransactions",
                "description": "If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.",
                "required": true,
                "schema": {
                  "title": "isTransactionsIncluded",
                  "type": "boolean"
                }
              }
            ],
            "result": {
              "name": "getBlockByNumberResult",
              "schema": {
                "$ref": "#/components/schemas/FullBlockOrNull"
              }
            }
          },
          {
            "name": "zkevm_getFullBlockByHash",
            "summary": "Gets a block with extra information for a given hash",
            "params": [
              {
                "name": "blockHash",
                "required": true,
                "schema": {
                  "$ref": "#/components/schemas/BlockHash"
                }
              },
              {
                "name": "includeTransactions",
                "description": "If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.",
                "required": true,
                "schema": {
                  "title": "isTransactionsIncluded",
                  "type": "boolean"
                }
              }
            ],
            "result": {
              "name": "getBlockByHashResult",
              "schema": {
                "$ref": "#/components/schemas/FullBlockOrNull"
              }
            }
          },
          {
            "name": "zkevm_getNativeBlockHashesInRange",
            "summary": "Returns the list of native block hashes.",
            "params": [
              {
                "name": "filter",
                "schema": {
                  "$ref": "#/components/schemas/NativeBlockHashBlockRangeFilter"
                }
              }
            ],
            "result": {
              "name": "filter",
                "schema": {
                  "$ref": "#/components/schemas/NativeBlockHashes"
                }
            }
          },
          {
            "name": "zkevm_getTransactionByL2Hash",
            "summary": "Returns the information about a transaction requested by transaction l2 hash.",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/TransactionHash"
              }
            ],
            "result": {
              "$ref": "#/components/contentDescriptors/TransactionResult"
            }
          },
          {
            "name": "zkevm_getTransactionReceiptByL2Hash",
            "summary": "Returns the receipt information of a transaction by its l2 hash.",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/TransactionHash"
              }
            ],
            "result": {
              "name": "transactionReceiptResult",
              "description": "returns either a receipt or null",
              "schema": {
                "title": "transactionReceiptOrNull",
                "oneOf": [
                  {
                    "$ref": "#/components/schemas/Receipt"
                  },
                  {
                    "$ref": "#/components/schemas/Null"
                  }
                ]
              }
            }
          },
          {
            "name": "zkevm_getExitRootsByGER",
            "summary": "Gets the exit roots accordingly to the provided Global Exit Root",
            "params": [
              {
                "$ref": "#/components/schemas/Keccak"
              }
            ],
            "result": {
              "$ref": "#/components/schemas/ExitRoots"
            },
            "examples": [
              {
                "name": "exit roots",
                "params": [
                  {
                    "name": "global exit root",
                    "value": "0x0000000000000000000000000000000000000000000000000000000000000001"
                  }
                ],
                "result": {
                  "name": "Exit Roots",
                  "value": {
                    "blockNumber": "0x1",
                    "timestamp": "0x642af31f",
                    "mainnetExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000002",
                    "rollupExitRoot": "0x0000000000000000000000000000000000000000000000000000000000000003"
                  }
                }
              }
            ]
          },
          {
            "name": "zkevm_getLatestGlobalExitRoot",
            "summary": "Returns the latest global exit root used in a batch.",
            "params": [
            ],
            "result": {
              "name": "GER",
                "schema": {
                  "$ref": "#/components/schemas/Keccak"
                }
            }
          },
          {
            "name": "zkevm_estimateCounters",
            "summary": "Estimates the transaction ZK Counters",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/Transaction"
              }
            ],
            "result": {
              "name": "counters",
              "description": "The counters used, limits and revert info when tx reverted",
              "schema": {
                "$ref": "#/components/schemas/ZKCountersResponse"
              }
            }
          },
          {
            "name": "zkevm_estimateFee",
            "summary": "Estimates the transaction Fee following the effective gas price rules",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/Transaction"
              }
            ],
            "result": {
              "name": "fee",
              "description": "The amount of the fee",
              "schema": {
                "$ref": "#/components/schemas/Integer"
              }
            }
          },
          {
            "name": "zkevm_estimateGasPrice",
            "summary": "Estimates the transaction Gas Price following the effective gas price rules",
            "params": [
              {
                "$ref": "#/components/contentDescriptors/Transaction"
              }
            ],
            "result": {
              "name": "gasPrice",
              "description": "The amount of gas price",
              "schema": {
                "$ref": "#/components/schemas/Integer"
              }
            }
          }
        ],
        "components": {
          "contentDescriptors": {
            "BlockNumber": {
              "name": "blockNumber",
              "required": true,
              "schema": {
                "$ref": "#/components/schemas/BlockNumber"
              }
            },
            "BatchNumber": {
              "name": "batchNumber",
              "required": true,
              "schema": {
                "$ref": "#/components/schemas/BatchNumber"
              }
            },
            "BatchNumberOrTag": {
              "name": "batchNumberOrTag",
              "required": true,
              "schema": {
                "title": "batchNumberOrTag",
                "oneOf": [
                  {
                    "$ref": "#/components/schemas/BatchNumber"
                  },
                  {
                    "$ref": "#/components/schemas/BatchNumberTag"
                  }
                ]
              }
            },
            "Batch": {
              "name": "batch",
              "description": "batch",
              "required": true,
              "schema": {
                "$ref": "#/components/schemas/Batch"
              }
            },
            "Block": {
              "name": "block",
              "summary": "A block",
              "description": "A block object",
              "schema": {
                "$ref": "#/components/schemas/Block"
              }
            },
            "Transaction": {
              "required": true,
              "name": "transaction",
              "schema": {
                "$ref": "#/components/schemas/Transaction"
              }
            },
            "TransactionHash": {
              "name": "transactionHash",
              "required": true,
              "schema": {
                "$ref": "#/components/schemas/TransactionHash"
              }
            },
            "TransactionResult": {
              "name": "transactionResult",
              "description": "Returns a transaction or null",
              "schema": {
                "title": "TransactionOrNull",
                "oneOf": [
                  {
                    "$ref": "#/components/schemas/Transaction"
                  },
                  {
                    "$ref": "#/components/schemas/Null"
                  }
                ]
              }
            }
          },
          "schemas": {
            "Null": {
              "title": "null",
              "type": "null",
              "description": "Null"
            },
            "BatchNumberTag": {
              "title": "batchNumberTag",
              "type": "string",
              "description": "The optional batch height description",
              "enum": [
                "earliest",
                "latest"
              ]
            },
            "Integer": {
              "title": "integer",
              "type": "string",
              "pattern": "^0x[a-fA-F0-9]+$",
              "description": "Hex representation of the integer"
            },
            "Keccak": {
              "title": "keccak",
              "type": "string",
              "description": "Hex representation of a Keccak 256 hash",
              "pattern": "^0x[a-fA-F\\d]{64}$"
            },
            "Address": {
              "title": "address",
              "type": "string",
              "pattern": "^0x[a-fA-F\\d]{40}$"
            },
            "BlockHash": {
              "title": "blockHash",
              "type": "string",
              "pattern": "^0x[a-fA-F\\d]{64}$",
              "description": "The hex representation of the Keccak 256 of the RLP encoded block"
            },
            "BlockNumber": {
              "title": "blockNumber",
              "type": "string",
              "description": "The hex representation of the block's height",
              "$ref": "#/components/schemas/Integer"
            },
            "FullBlockOrNull": {
              "title": "fullBlockOrNull",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/FullBlock"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "BatchNumber": {
              "title": "batchNumber",
              "type": "string",
              "description": "The hex representation of the batch's height",
              "$ref": "#/components/schemas/Integer"
            },
            "TransactionHash": {
              "title": "transactionHash",
              "type": "string",
              "description": "Keccak 256 Hash of the RLP encoding of a transaction",
              "$ref": "#/components/schemas/Keccak"
            },
            "NonceOrNull": {
              "title": "nonceOrNull",
              "description": "Randomly selected number to satisfy the proof-of-work or null when its the pending block",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/Nonce"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "Nonce": {
              "title": "nonce",
              "description": "A number only to be used once",
              "$ref": "#/components/schemas/Integer"
            },
            "From": {
              "title": "From",
              "description": "The sender of the transaction",
              "$ref": "#/components/schemas/Address"
            },
            "BlockNumberOrNull": {
              "title": "blockNumberOrNull",
              "description": "The block number or null when its the pending block",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "IntegerOrNull": {
              "title": "integerOrNull",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/Integer"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "AddressOrNull": {
              "title": "addressOrNull",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/Address"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "KeccakOrPending": {
              "title": "keccakOrPending",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/Keccak"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "To": {
              "title": "To",
              "description": "Destination address of the transaction. Null if it was a contract create.",
              "oneOf": [
                {
                  "$ref": "#/components/schemas/Address"
                },
                {
                  "$ref": "#/components/schemas/Null"
                }
              ]
            },
            "BlockHashOrNull": {
              "title": "blockHashOrNull",
              "description": "The block hash or null when its the pending block",
              "$ref": "#/components/schemas/KeccakOrPending"
            },
            "TransactionIndex": {
              "title": "transactionIndex",
              "description": "The index of the transaction. null when its pending",
              "$ref": "#/components/schemas/IntegerOrNull"
            },
            "Batch": {
              "title": "Batch",
              "type": "object",
              "readOnly": true,
              "properties": {
                "number": {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                "globalExitRoot": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "mainnetExitRoot": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "rollupExitRoot": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "accInputHash": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "timestamp": {
                  "$ref": "#/components/schemas/Integer"
                },
                "sendSequencesTxHash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "verifyBatchTxHash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "closed": {
                  "title": "closed",
                  "type": "boolean",
                  "description": "True if the batch is already closed, otherwise false"
                },
                "blocks": {
                  "title": "blocksOrHashes",
                  "description": "Array of block objects, or 32 Bytes block hashes depending on the last given parameter",
                  "type": "array",
                  "items": {
                    "title": "blockOrBlockHash",
                    "oneOf": [
                      {
                        "$ref": "#/components/schemas/Block"
                      },
                      {
                        "$ref": "#/components/schemas/BlockHash"
                      }
                    ]
                  }
                },
                "transactions": {
                  "title": "transactionsOrHashes",
                  "description": "Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter",
                  "type": "array",
                  "items": {
                    "title": "transactionOrTransactionHash",
                    "oneOf": [
                      {
                        "$ref": "#/components/schemas/Transaction"
                      },
                      {
                        "$ref": "#/components/schemas/TransactionHash"
                      }
                    ]
                  }
                },
                "stateRoot": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "coinbase": {
                  "$ref": "#/components/schemas/Address"
                }
              }
            },
            "Block": {
              "title": "Block",
              "type": "object",
              "properties": {
                "number": {
                  "$ref": "#/components/schemas/BlockNumberOrNull"
                },
                "hash": {
                  "$ref": "#/components/schemas/BlockHashOrNull"
                },
                "parentHash": {
                  "$ref": "#/components/schemas/BlockHash"
                },
                "nonce": {
                  "$ref": "#/components/schemas/NonceOrNull"
                },
                "sha3Uncles": {
                  "title": "blockShaUncles",
                  "description": "Keccak hash of the uncles data in the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "logsBloom": {
                  "title": "blockLogsBloom",
                  "type": "string",
                  "description": "The bloom filter for the logs of the block or null when its the pending block",
                  "pattern": "^0x[a-fA-F\\d]+$"
                },
                "transactionsRoot": {
                  "title": "blockTransactionsRoot",
                  "description": "The root of the transactions trie of the block.",
                  "$ref": "#/components/schemas/Keccak"
                },
                "stateRoot": {
                  "title": "blockStateRoot",
                  "description": "The root of the final state trie of the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "receiptsRoot": {
                  "title": "blockReceiptsRoot",
                  "description": "The root of the receipts trie of the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "miner": {
                  "$ref": "#/components/schemas/AddressOrNull"
                },
                "difficulty": {
                  "title": "blockDifficulty",
                  "type": "string",
                  "description": "Integer of the difficulty for this block"
                },
                "totalDifficulty": {
                  "title": "blockTotalDifficulty",
                  "description": "Integer of the total difficulty of the chain until this block",
                  "$ref": "#/components/schemas/IntegerOrNull"
                },
                "extraData": {
                  "title": "blockExtraData",
                  "type": "string",
                  "description": "The 'extra data' field of this block"
                },
                "size": {
                  "title": "blockSize",
                  "type": "string",
                  "description": "Integer the size of this block in bytes"
                },
                "gasLimit": {
                  "title": "blockGasLimit",
                  "type": "string",
                  "description": "The maximum gas allowed in this block"
                },
                "gasUsed": {
                  "title": "blockGasUsed",
                  "type": "string",
                  "description": "The total used gas by all transactions in this block"
                },
                "timestamp": {
                  "title": "blockTimeStamp",
                  "type": "string",
                  "description": "The unix timestamp for when the block was collated"
                },
                "transactions": {
                  "title": "transactionsOrHashes",
                  "description": "Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter",
                  "type": "array",
                  "items": {
                    "title": "transactionOrTransactionHash",
                    "oneOf": [
                      {
                        "$ref": "#/components/schemas/Transaction"
                      },
                      {
                        "$ref": "#/components/schemas/TransactionHash"
                      }
                    ]
                  }
                },
                "uncles": {
                  "title": "uncleHashes",
                  "description": "Array of uncle hashes",
                  "type": "array",
                  "items": {
                    "title": "uncleHash",
                    "description": "Block hash of the RLP encoding of an uncle block",
                    "$ref": "#/components/schemas/Keccak"
                  }
                }
              }
            },
            "FullBlock": {
              "title": "fullBlock",
              "type": "object",
              "properties": {
                "number": {
                  "$ref": "#/components/schemas/BlockNumberOrNull"
                },
                "hash": {
                  "$ref": "#/components/schemas/BlockHashOrNull"
                },
                "parentHash": {
                  "$ref": "#/components/schemas/BlockHash"
                },
                "nonce": {
                  "$ref": "#/components/schemas/NonceOrNull"
                },
                "sha3Uncles": {
                  "title": "blockShaUncles",
                  "description": "Keccak hash of the uncles data in the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "logsBloom": {
                  "title": "blockLogsBloom",
                  "type": "string",
                  "description": "The bloom filter for the logs of the block or null when its the pending block",
                  "pattern": "^0x[a-fA-F\\d]+$"
                },
                "transactionsRoot": {
                  "title": "blockTransactionsRoot",
                  "description": "The root of the transactions trie of the block.",
                  "$ref": "#/components/schemas/Keccak"
                },
                "stateRoot": {
                  "title": "blockStateRoot",
                  "description": "The root of the final state trie of the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "receiptsRoot": {
                  "title": "blockReceiptsRoot",
                  "description": "The root of the receipts trie of the block",
                  "$ref": "#/components/schemas/Keccak"
                },
                "miner": {
                  "$ref": "#/components/schemas/AddressOrNull"
                },
                "difficulty": {
                  "title": "blockDifficulty",
                  "type": "string",
                  "description": "Integer of the difficulty for this block"
                },
                "totalDifficulty": {
                  "title": "blockTotalDifficulty",
                  "description": "Integer of the total difficulty of the chain until this block",
                  "$ref": "#/components/schemas/IntegerOrNull"
                },
                "extraData": {
                  "title": "blockExtraData",
                  "type": "string",
                  "description": "The 'extra data' field of this block"
                },
                "size": {
                  "title": "blockSize",
                  "type": "string",
                  "description": "Integer the size of this block in bytes"
                },
                "gasLimit": {
                  "title": "blockGasLimit",
                  "type": "string",
                  "description": "The maximum gas allowed in this block"
                },
                "gasUsed": {
                  "title": "blockGasUsed",
                  "type": "string",
                  "description": "The total used gas by all transactions in this block"
                },
                "timestamp": {
                  "title": "blockTimeStamp",
                  "type": "string",
                  "description": "The unix timestamp for when the block was collated"
                },
                "transactions": {
                  "title": "transactionsOrHashes",
                  "description": "Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter",
                  "type": "array",
                  "items": {
                    "title": "transactionOrTransactionHash",
                    "oneOf": [
                      {
                        "$ref": "#/components/schemas/FullTransaction"
                      },
                      {
                        "$ref": "#/components/schemas/TransactionHash"
                      }
                    ]
                  }
                },
                "uncles": {
                  "title": "uncleHashes",
                  "description": "Array of uncle hashes",
                  "type": "array",
                  "items": {
                    "title": "uncleHash",
                    "description": "Block hash of the RLP encoding of an uncle block",
                    "$ref": "#/components/schemas/Keccak"
                  }
                }
              }
            },
            "Transaction": {
              "title": "transaction",
              "type": "object",
              "required": [
                "gas",
                "gasPrice",
                "nonce"
              ],
              "properties": {
                "blockHash": {
                  "$ref": "#/components/schemas/BlockHashOrNull"
                },
                "blockNumber": {
                  "$ref": "#/components/schemas/BlockNumberOrNull"
                },
                "from": {
                  "$ref": "#/components/schemas/From"
                },
                "gas": {
                  "title": "transactionGas",
                  "type": "string",
                  "description": "The gas limit provided by the sender in Wei"
                },
                "gasPrice": {
                  "title": "transactionGasPrice",
                  "type": "string",
                  "description": "The gas price willing to be paid by the sender in Wei"
                },
                "hash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "l2Hash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "input": {
                  "title": "transactionInput",
                  "type": "string",
                  "description": "The data field sent with the transaction"
                },
                "nonce": {
                  "title": "transactionNonce",
                  "description": "The total number of prior transactions made by the sender",
                  "$ref": "#/components/schemas/Nonce"
                },
                "to": {
                  "$ref": "#/components/schemas/To"
                },
                "transactionIndex": {
                  "$ref": "#/components/schemas/TransactionIndex"
                },
                "value": {
                  "title": "transactionValue",
                  "description": "Value of Ether being transferred in Wei",
                  "$ref": "#/components/schemas/Keccak"
                },
                "v": {
                  "title": "transactionSigV",
                  "type": "string",
                  "description": "ECDSA recovery id"
                },
                "r": {
                  "title": "transactionSigR",
                  "type": "string",
                  "description": "ECDSA signature r"
                },
                "s": {
                  "title": "transactionSigS",
                  "type": "string",
                  "description": "ECDSA signature s"
                }
              }
            },
            "FullTransaction": {
              "title": "fullTransaction",
              "type": "object",
              "required": [
                "gas",
                "gasPrice",
                "nonce"
              ],
              "properties": {
                "blockHash": {
                  "$ref": "#/components/schemas/BlockHashOrNull"
                },
                "blockNumber": {
                  "$ref": "#/components/schemas/BlockNumberOrNull"
                },
                "from": {
                  "$ref": "#/components/schemas/From"
                },
                "gas": {
                  "title": "transactionGas",
                  "type": "string",
                  "description": "The gas limit provided by the sender in Wei"
                },
                "gasPrice": {
                  "title": "transactionGasPrice",
                  "type": "string",
                  "description": "The gas price willing to be paid by the sender in Wei"
                },
                "hash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "input": {
                  "title": "transactionInput",
                  "type": "string",
                  "description": "The data field sent with the transaction"
                },
                "nonce": {
                  "title": "transactionNonce",
                  "description": "The total number of prior transactions made by the sender",
                  "$ref": "#/components/schemas/Nonce"
                },
                "to": {
                  "$ref": "#/components/schemas/To"
                },
                "transactionIndex": {
                  "$ref": "#/components/schemas/TransactionIndex"
                },
                "value": {
                  "title": "transactionValue",
                  "description": "Value of Ether being transferred in Wei",
                  "$ref": "#/components/schemas/Keccak"
                },
                "v": {
                  "title": "transactionSigV",
                  "type": "string",
                  "description": "ECDSA recovery id"
                },
                "r": {
                  "title": "transactionSigR",
                  "type": "string",
                  "description": "ECDSA signature r"
                },
                "s": {
                  "title": "transactionSigS",
                  "type": "string",
                  "description": "ECDSA signature s"
                },
                "receipt": {
                  "$ref": "#/components/schemas/Receipt"
                }
              }
            },
            "Transactions": {
              "title": "transactions",
              "description": "An array of transactions",
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Transaction"
              }
            },
            "Receipt": {
              "title": "receipt",
              "type": "object",
              "description": "The receipt of a transaction",
              "required": [
                "blockHash",
                "blockNumber",
                "contractAddress",
                "cumulativeGasUsed",
                "from",
                "gasUsed",
                "logs",
                "logsBloom",
                "to",
                "transactionHash",
                "transactionIndex"
              ],
              "properties": {
                "blockHash": {
                  "$ref": "#/components/schemas/BlockHash"
                },
                "blockNumber": {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                "contractAddress": {
                  "title": "ReceiptContractAddress",
                  "description": "The contract address created, if the transaction was a contract creation, otherwise null",
                  "$ref": "#/components/schemas/AddressOrNull"
                },
                "cumulativeGasUsed": {
                  "title": "ReceiptCumulativeGasUsed",
                  "description": "The gas units used by the transaction",
                  "$ref": "#/components/schemas/Integer"
                },
                "from": {
                  "$ref": "#/components/schemas/From"
                },
                "gasUsed": {
                  "title": "ReceiptGasUsed",
                  "description": "The total gas used by the transaction",
                  "$ref": "#/components/schemas/Integer"
                },
                "logs": {
                  "title": "logs",
                  "type": "array",
                  "description": "An array of all the logs triggered during the transaction",
                  "items": {
                    "$ref": "#/components/schemas/Log"
                  }
                },
                "logsBloom": {
                  "$ref": "#/components/schemas/BloomFilter"
                },
                "to": {
                  "$ref": "#/components/schemas/To"
                },
                "transactionHash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "transactionL2Hash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "transactionIndex": {
                  "$ref": "#/components/schemas/TransactionIndex"
                },
                "postTransactionState": {
                  "title": "ReceiptPostTransactionState",
                  "description": "The intermediate stateRoot directly after transaction execution.",
                  "$ref": "#/components/schemas/Keccak"
                },
                "status": {
                  "title": "ReceiptStatus",
                  "description": "Whether or not the transaction threw an error.",
                  "type": "boolean"
                }
              }
            },
            "BloomFilter": {
              "title": "bloomFilter",
              "type": "string",
              "description": "A 2048 bit bloom filter from the logs of the transaction. Each log sets 3 bits though taking the low-order 11 bits of each of the first three pairs of bytes in a Keccak 256 hash of the log's byte series"
            },
            "Log": {
              "title": "log",
              "type": "object",
              "description": "An indexed event generated during a transaction",
              "properties": {
                "address": {
                  "title": "LogAddress",
                  "description": "Sender of the transaction",
                  "$ref": "#/components/schemas/Address"
                },
                "blockHash": {
                  "$ref": "#/components/schemas/BlockHash"
                },
                "blockNumber": {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                "data": {
                  "title": "LogData",
                  "description": "The data/input string sent along with the transaction",
                  "$ref": "#/components/schemas/Bytes"
                },
                "logIndex": {
                  "title": "LogIndex",
                  "description": "The index of the event within its transaction, null when its pending",
                  "$ref": "#/components/schemas/Integer"
                },
                "removed": {
                  "title": "logIsRemoved",
                  "description": "Whether or not the log was orphaned off the main chain",
                  "type": "boolean"
                },
                "topics": {
                  "$ref": "#/components/schemas/Topics"
                },
                "transactionHash": {
                  "$ref": "#/components/schemas/TransactionHash"
                },
                "transactionIndex": {
                  "$ref": "#/components/schemas/TransactionIndex"
                }
              }
            },
            "Topics": {
              "title": "LogTopics",
              "description": "Topics are order-dependent. Each topic can also be an array of DATA with 'or' options.",
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Topic"
              }
            },
            "Topic": {
              "title": "topic",
              "description": "32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256))",
              "$ref": "#/components/schemas/DataWord"
            },
            "DataWord": {
              "title": "dataWord",
              "type": "string",
              "description": "Hex representation of a 256 bit unit of data",
              "pattern": "^0x([a-fA-F\\d]{64})?$"
            },
            "Bytes": {
              "title": "bytes",
              "type": "string",
              "description": "Hex representation of a variable length byte array",
              "pattern": "^0x([a-fA-F0-9]?)+$"
            },
            "NativeBlockHashes": {
              "title": "native block hashes",
              "description": "An array of hashes",
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Keccak"
              }
            },
            "NativeBlockHashBlockRangeFilter": {
              "title": "NativeBlockHashBlockRangeFilter",
              "type": "object",
              "properties": {
                "fromBlock": {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                "toBlock": {
                  "$ref": "#/components/schemas/BlockNumber"
                }
              }
            },
            "ExitRoots": {
              "title": "ExitRoots",
              "type": "object",
              "readOnly": true,
              "properties": {
                "blockNumber": {
                  "$ref": "#/components/schemas/BlockNumber"
                },
                "timestamp": {
                  "title": "timestamp",
                  "type": "string",
                  "description": "The unix timestamp of the block mentioned in the blockNumber field"
                },
                "mainnetExitRoot": {
                  "$ref": "#/components/schemas/Keccak"
                },
                "rollupExitRoot": {
                  "$ref": "#/components/schemas/Keccak"
                }
              }
            },
            "ZKCountersResponse": {
              "title": "ZKCountersResponse",
              "type": "object",
              "readOnly": true,
              "properties": {
                "countersUsed": {
                  "$ref": "#/components/schemas/ZKCountersUsed"
                },
                "countersLimits": {
                  "$ref": "#/components/schemas/ZKCountersLimits"
                },
                "revertInfo": {
                  "$ref": "#/components/schemas/RevertInfo"
                },
                "oocError": {
                  "type": "string"
                }
              }
            },
            "ZKCountersUsed": {
              "title": "ZKCountersUsed",
              "type": "object",
              "readOnly": true,
              "properties": {
                "gasUsed": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedKeccakHashes": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedPoseidonHashes": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedPoseidonPaddings": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedMemAligns": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedArithmetics": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedBinaries": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedSteps": {
                  "$ref": "#/components/schemas/Integer"
                },
                "usedSHA256Hashes": {
                  "$ref": "#/components/schemas/Integer"
                }
              }
            },
            "ZKCountersLimits":{
              "title": "ZKCountersLimits",
              "type": "object",
              "readOnly": true,
              "properties": {
                "maxGasUsed": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedKeccakHashes": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedPoseidonHashes": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedPoseidonPaddings": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedMemAligns": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedArithmetics": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedBinaries": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedSteps": {
                  "$ref": "#/components/schemas/Integer"
                },
                "maxUsedSHA256Hashes": {
                  "$ref": "#/components/schemas/Integer"
                }
              }
            },
            "RevertInfo":{
              "title": "RevertInfo",
              "type": "object",
              "readOnly": true,
              "properties": {
                "message": {
                  "type": "string"
                },
                "data": {
                  "$ref": "#/components/schemas/Integer"
                }
              }
            }
          }
        }
      }
    ```

## zkEVM endpoints

<div class="tablecontainer">
<table><tr><th class="string">openrpc</th><td class="string">1.0.0-rc1</td></tr><tr><th class="object">info</th><td class="object"><table><tr><th class="string">title</th><td class="string">zkEVM Endpoints</td></tr><tr><th class="string">version</th><td class="string">2.0.0</td></tr></table></td></tr><tr><th class="array">methods</th><td class="array"><table><thead><tr><th class="string">name</th><th class="string">summary</th><th class="array">params</th><th class="object">result</th><th class="array">examples</th></tr></thead><tbody><tr><td class="string">zkevm_consolidatedBlockNumber</td><td class="string">Returns the latest block number that is connected to the latest batch verified.</td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BlockNumber</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="string">value</th><td class="string">0x1</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_isBlockVirtualized</td><td class="string">Returns true if the provided block number is already connected to a batch that was already virtualized, otherwise false.</td><td class="array"><table><thead><tr><th class="string">name</th><th class="object">schema</th></tr></thead><tbody><tr><td class="string">blockNumber</td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BlockNumber</td></tr></table></td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">result</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="boolean">value</th><td class="boolean">true</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_isBlockConsolidated</td><td class="string">Returns true if the provided block number is already connected to a batch that was already verified, otherwise false.</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/BlockNumber</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">result</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="boolean">value</th><td class="boolean">true</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_batchNumber</td><td class="string">Returns the latest batch number.</td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BatchNumber</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="string">value</th><td class="string">0x1</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_virtualBatchNumber</td><td class="string">Returns the latest virtual batch number.</td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BatchNumber</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="string">value</th><td class="string">0x1</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_verifiedBatchNumber</td><td class="string">Returns the latest verified batch number.</td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BatchNumber</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="string">value</th><td class="string">0x1</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_batchNumberByBlockNumber</td><td class="string">Returns the batch number of the batch connected to the block.</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/BlockNumber</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/BatchNumber</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">example</td><td class="string"></td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">exampleResult</td></tr><tr><th class="string">description</th><td class="string"></td></tr><tr><th class="string">value</th><td class="string">0x1</td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_getBatchByNumber</td><td class="string">Gets a batch for a given number</td><td class="array"><table><thead><tr><th class="string">$ref</th><th class="undefined">name</th><th class="undefined">description</th><th class="undefined">required</th><th class="undefined">schema</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/BatchNumberOrTag</td><td class="undefined"></td><td class="undefined"></td><td class="undefined"></td><td class="undefined"></td></tr><tr><td class="undefined"></td><td class="string">includeTransactions</td><td class="string">If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.</td><td class="boolean">true</td><td class="object"><table><tr><th class="string">title</th><td class="string">isTransactionsIncluded</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/Batch</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">description</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">batch without tx details</td><td class="string">Batch without transaction details</td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">value</th></tr></thead><tbody><tr><td class="string">batch number</td><td class="string">0x1</td></tr><tr><td class="string">include txs</td><td class="string">false</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">Batch</td></tr><tr><th class="object">value</th><td class="object"><table><tr><th class="string">number</th><td class="string">0x1</td></tr><tr><th class="string">coinbase</th><td class="string">0x0000000000000000000000000000000000000001</td></tr><tr><th class="string">stateRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000001</td></tr><tr><th class="string">globalExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000002</td></tr><tr><th class="string">mainnetExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000003</td></tr><tr><th class="string">rollupExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000004</td></tr><tr><th class="string">localExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000005</td></tr><tr><th class="string">accInputHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000006</td></tr><tr><th class="string">timestamp</th><td class="string">0x642af31f</td></tr><tr><th class="string">sendSequencesTxHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000007</td></tr><tr><th class="string">verifyBatchTxHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000008</td></tr><tr><th class="array">transactions</th><td class="array"><table><tbody><tr><td class="string">0x0000000000000000000000000000000000000000000000000000000000000009</td></tr><tr><td class="string">0x0000000000000000000000000000000000000000000000000000000000000010</td></tr><tr><td class="string">0x0000000000000000000000000000000000000000000000000000000000000011</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><td class="string">batch with tx detail</td><td class="string">Batch with transaction details</td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">value</th></tr></thead><tbody><tr><td class="string">batch number</td><td class="string">0x1</td></tr><tr><td class="string">include txs</td><td class="string">true</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">Batch</td></tr><tr><th class="object">value</th><td class="object"><table><tr><th class="string">number</th><td class="string">0x1</td></tr><tr><th class="string">coinbase</th><td class="string">0x0000000000000000000000000000000000000001</td></tr><tr><th class="string">stateRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000001</td></tr><tr><th class="string">globalExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000002</td></tr><tr><th class="string">mainnetExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000003</td></tr><tr><th class="string">rollupExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000004</td></tr><tr><th class="string">localExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000005</td></tr><tr><th class="string">accInputHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000006</td></tr><tr><th class="string">timestamp</th><td class="string">0x642af31f</td></tr><tr><th class="string">sendSequencesTxHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000007</td></tr><tr><th class="string">verifyBatchTxHash</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000008</td></tr><tr><th class="array">transactions</th><td class="array"><table><thead><tr><th class="string">nonce</th><th class="string">gasPrice</th><th class="string">gas</th><th class="string">to</th><th class="string">value</th><th class="string">input</th><th class="string">v</th><th class="string">r</th><th class="string">s</th><th class="string">hash</th><th class="string">from</th><th class="string">blockHash</th><th class="string">blockNumber</th><th class="string">transactionIndex</th><th class="string">chainId</th><th class="string">type</th></tr></thead><tbody><tr><td class="string">0x1</td><td class="string">0x123456</td><td class="string">0x59D8</td><td class="string">0x0000000000000000000000000000000000000002</td><td class="string">0x1</td><td class="string">0x</td><td class="string">0xAAA</td><td class="string">0x0000000000000000000000000000000000000000000000000000000000000010</td><td class="string">0x0000000000000000000000000000000000000000000000000000000000000011</td><td class="string">0x0000000000000000000000000000000000000000000000000000000000000012</td><td class="string">0x0000000000000000000000000000000000000003</td><td class="string">0x0000000000000000000000000000000000000000000000000000000000000013</td><td class="string">0x1</td><td class="string">0x0</td><td class="string">0x539</td><td class="string">0x0</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_getFullBlockByNumber</td><td class="string">Gets a block with extra information for a given number</td><td class="array"><table><thead><tr><th class="string">$ref</th><th class="undefined">name</th><th class="undefined">description</th><th class="undefined">required</th><th class="undefined">schema</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/BlockNumber</td><td class="undefined"></td><td class="undefined"></td><td class="undefined"></td><td class="undefined"></td></tr><tr><td class="undefined"></td><td class="string">includeTransactions</td><td class="string">If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.</td><td class="boolean">true</td><td class="object"><table><tr><th class="string">title</th><td class="string">isTransactionsIncluded</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">getBlockByNumberResult</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/FullBlockOrNull</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_getFullBlockByHash</td><td class="string">Gets a block with extra information for a given hash</td><td class="array"><table><thead><tr><th class="string">name</th><th class="boolean">required</th><th class="object">schema</th><th class="undefined">description</th></tr></thead><tbody><tr><td class="string">blockHash</td><td class="boolean">true</td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHash</td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">includeTransactions</td><td class="boolean">true</td><td class="object"><table><tr><th class="string">title</th><td class="string">isTransactionsIncluded</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td><td class="string">If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">getBlockByHashResult</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/FullBlockOrNull</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_getNativeBlockHashesInRange</td><td class="string">Returns the list of native block hashes.</td><td class="array"><table><thead><tr><th class="string">name</th><th class="object">schema</th></tr></thead><tbody><tr><td class="string">filter</td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/NativeBlockHashBlockRangeFilter</td></tr></table></td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">filter</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/NativeBlockHashes</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_getTransactionByL2Hash</td><td class="string">Returns the information about a transaction requested by transaction l2 hash.</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/TransactionHash</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/contentDescriptors/TransactionResult</td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_getTransactionReceiptByL2Hash</td><td class="string">Returns the receipt information of a transaction by its l2 hash.</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/TransactionHash</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">transactionReceiptResult</td></tr><tr><th class="string">description</th><td class="string">returns either a receipt or null</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionReceiptOrNull</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Receipt</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_getExitRootsByGER</td><td class="string">Gets the exit roots accordingly to the provided Global Exit Root</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Keccak</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/ExitRoots</td></tr></table></td><td class="array"><table><thead><tr><th class="string">name</th><th class="array">params</th><th class="object">result</th></tr></thead><tbody><tr><td class="string">exit roots</td><td class="array"><table><thead><tr><th class="string">name</th><th class="string">value</th></tr></thead><tbody><tr><td class="string">global exit root</td><td class="string">0x0000000000000000000000000000000000000000000000000000000000000001</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">Exit Roots</td></tr><tr><th class="object">value</th><td class="object"><table><tr><th class="string">blockNumber</th><td class="string">0x1</td></tr><tr><th class="string">timestamp</th><td class="string">0x642af31f</td></tr><tr><th class="string">mainnetExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000002</td></tr><tr><th class="string">rollupExitRoot</th><td class="string">0x0000000000000000000000000000000000000000000000000000000000000003</td></tr></table></td></tr></table></td></tr></tbody></table></td></tr><tr><td class="string">zkevm_getLatestGlobalExitRoot</td><td class="string">Returns the latest global exit root used in a batch.</td><td class="array"><table><tbody></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">GER</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_estimateCounters</td><td class="string">Estimates the transaction ZK Counters</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/Transaction</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">counters</td></tr><tr><th class="string">description</th><td class="string">The counters used, limits and revert info when tx reverted</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/ZKCountersResponse</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_estimateFee</td><td class="string">Estimates the transaction Fee following the effective gas price rules</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/Transaction</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">fee</td></tr><tr><th class="string">description</th><td class="string">The amount of the fee</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr></table></td><td class="undefined"></td></tr><tr><td class="string">zkevm_estimateGasPrice</td><td class="string">Estimates the transaction Gas Price following the effective gas price rules</td><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/contentDescriptors/Transaction</td></tr></tbody></table></td><td class="object"><table><tr><th class="string">name</th><td class="string">gasPrice</td></tr><tr><th class="string">description</th><td class="string">The amount of gas price</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr></table></td><td class="undefined"></td></tr></tbody></table></td></tr><tr><th class="object">components</th><td class="object"><table><tr><th class="object">contentDescriptors</th><td class="object"><table><tr><th class="object">BlockNumber</th><td class="object"><table><tr><th class="string">name</th><td class="string">blockNumber</td></tr><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr></table></td></tr><tr><th class="object">BatchNumber</th><td class="object"><table><tr><th class="string">name</th><td class="string">batchNumber</td></tr><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BatchNumber</td></tr></table></td></tr></table></td></tr><tr><th class="object">BatchNumberOrTag</th><td class="object"><table><tr><th class="string">name</th><td class="string">batchNumberOrTag</td></tr><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">title</th><td class="string">batchNumberOrTag</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/BatchNumber</td></tr><tr><td class="string">#/components/schemas/BatchNumberTag</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">Batch</th><td class="object"><table><tr><th class="string">name</th><td class="string">batch</td></tr><tr><th class="string">description</th><td class="string">batch</td></tr><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Batch</td></tr></table></td></tr></table></td></tr><tr><th class="object">Block</th><td class="object"><table><tr><th class="string">name</th><td class="string">block</td></tr><tr><th class="string">summary</th><td class="string">A block</td></tr><tr><th class="string">description</th><td class="string">A block object</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Block</td></tr></table></td></tr></table></td></tr><tr><th class="object">Transaction</th><td class="object"><table><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="string">name</th><td class="string">transaction</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Transaction</td></tr></table></td></tr></table></td></tr><tr><th class="object">TransactionHash</th><td class="object"><table><tr><th class="string">name</th><td class="string">transactionHash</td></tr><tr><th class="boolean">required</th><td class="boolean">true</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr></table></td></tr><tr><th class="object">TransactionResult</th><td class="object"><table><tr><th class="string">name</th><td class="string">transactionResult</td></tr><tr><th class="string">description</th><td class="string">Returns a transaction or null</td></tr><tr><th class="object">schema</th><td class="object"><table><tr><th class="string">title</th><td class="string">TransactionOrNull</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Transaction</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">schemas</th><td class="object"><table><tr><th class="object">Null</th><td class="object"><table><tr><th class="string">title</th><td class="string">null</td></tr><tr><th class="string">type</th><td class="string">null</td></tr><tr><th class="string">description</th><td class="string">Null</td></tr></table></td></tr><tr><th class="object">BatchNumberTag</th><td class="object"><table><tr><th class="string">title</th><td class="string">batchNumberTag</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The optional batch height description</td></tr><tr><th class="array">enum</th><td class="array"><table><tbody><tr><td class="string">earliest</td></tr><tr><td class="string">latest</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">Integer</th><td class="object"><table><tr><th class="string">title</th><td class="string">integer</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F0-9]+$</td></tr><tr><th class="string">description</th><td class="string">Hex representation of the integer</td></tr></table></td></tr><tr><th class="object">Keccak</th><td class="object"><table><tr><th class="string">title</th><td class="string">keccak</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Hex representation of a Keccak 256 hash</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F\d]{64}$</td></tr></table></td></tr><tr><th class="object">Address</th><td class="object"><table><tr><th class="string">title</th><td class="string">address</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F\d]{40}$</td></tr></table></td></tr><tr><th class="object">BlockHash</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockHash</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F\d]{64}$</td></tr><tr><th class="string">description</th><td class="string">The hex representation of the Keccak 256 of the RLP encoded block</td></tr></table></td></tr><tr><th class="object">BlockNumber</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockNumber</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The hex representation of the block's height</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">FullBlockOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">fullBlockOrNull</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/FullBlock</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">BatchNumber</th><td class="object"><table><tr><th class="string">title</th><td class="string">batchNumber</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The hex representation of the batch's height</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">TransactionHash</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionHash</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Keccak 256 Hash of the RLP encoding of a transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">NonceOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">nonceOrNull</td></tr><tr><th class="string">description</th><td class="string">Randomly selected number to satisfy the proof-of-work or null when its the pending block</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Nonce</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">Nonce</th><td class="object"><table><tr><th class="string">title</th><td class="string">nonce</td></tr><tr><th class="string">description</th><td class="string">A number only to be used once</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">From</th><td class="object"><table><tr><th class="string">title</th><td class="string">From</td></tr><tr><th class="string">description</th><td class="string">The sender of the transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Address</td></tr></table></td></tr><tr><th class="object">BlockNumberOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockNumberOrNull</td></tr><tr><th class="string">description</th><td class="string">The block number or null when its the pending block</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/BlockNumber</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">IntegerOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">integerOrNull</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Integer</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">AddressOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">addressOrNull</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Address</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">KeccakOrPending</th><td class="object"><table><tr><th class="string">title</th><td class="string">keccakOrPending</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Keccak</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">To</th><td class="object"><table><tr><th class="string">title</th><td class="string">To</td></tr><tr><th class="string">description</th><td class="string">Destination address of the transaction. Null if it was a contract create.</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Address</td></tr><tr><td class="string">#/components/schemas/Null</td></tr></tbody></table></td></tr></table></td></tr><tr><th class="object">BlockHashOrNull</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockHashOrNull</td></tr><tr><th class="string">description</th><td class="string">The block hash or null when its the pending block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/KeccakOrPending</td></tr></table></td></tr><tr><th class="object">TransactionIndex</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionIndex</td></tr><tr><th class="string">description</th><td class="string">The index of the transaction. null when its pending</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/IntegerOrNull</td></tr></table></td></tr><tr><th class="object">Batch</th><td class="object"><table><tr><th class="string">title</th><td class="string">Batch</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">number</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr><tr><th class="object">globalExitRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">mainnetExitRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">rollupExitRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">accInputHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">timestamp</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">sendSequencesTxHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">verifyBatchTxHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">closed</th><td class="object"><table><tr><th class="string">title</th><td class="string">closed</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr><tr><th class="string">description</th><td class="string">True if the batch is already closed, otherwise false</td></tr></table></td></tr><tr><th class="object">blocks</th><td class="object"><table><tr><th class="string">title</th><td class="string">blocksOrHashes</td></tr><tr><th class="string">description</th><td class="string">Array of block objects, or 32 Bytes block hashes depending on the last given parameter</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockOrBlockHash</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Block</td></tr><tr><td class="string">#/components/schemas/BlockHash</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">transactions</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionsOrHashes</td></tr><tr><th class="string">description</th><td class="string">Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionOrTransactionHash</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Transaction</td></tr><tr><td class="string">#/components/schemas/TransactionHash</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">stateRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">coinbase</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Address</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">Block</th><td class="object"><table><tr><th class="string">title</th><td class="string">Block</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">number</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumberOrNull</td></tr></table></td></tr><tr><th class="object">hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHashOrNull</td></tr></table></td></tr><tr><th class="object">parentHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHash</td></tr></table></td></tr><tr><th class="object">nonce</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/NonceOrNull</td></tr></table></td></tr><tr><th class="object">sha3Uncles</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockShaUncles</td></tr><tr><th class="string">description</th><td class="string">Keccak hash of the uncles data in the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">logsBloom</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockLogsBloom</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The bloom filter for the logs of the block or null when its the pending block</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F\d]+$</td></tr></table></td></tr><tr><th class="object">transactionsRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTransactionsRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the transactions trie of the block.</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">stateRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockStateRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the final state trie of the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">receiptsRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockReceiptsRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the receipts trie of the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">miner</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/AddressOrNull</td></tr></table></td></tr><tr><th class="object">difficulty</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockDifficulty</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Integer of the difficulty for this block</td></tr></table></td></tr><tr><th class="object">totalDifficulty</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTotalDifficulty</td></tr><tr><th class="string">description</th><td class="string">Integer of the total difficulty of the chain until this block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/IntegerOrNull</td></tr></table></td></tr><tr><th class="object">extraData</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockExtraData</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The 'extra data' field of this block</td></tr></table></td></tr><tr><th class="object">size</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockSize</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Integer the size of this block in bytes</td></tr></table></td></tr><tr><th class="object">gasLimit</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockGasLimit</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The maximum gas allowed in this block</td></tr></table></td></tr><tr><th class="object">gasUsed</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockGasUsed</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The total used gas by all transactions in this block</td></tr></table></td></tr><tr><th class="object">timestamp</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTimeStamp</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The unix timestamp for when the block was collated</td></tr></table></td></tr><tr><th class="object">transactions</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionsOrHashes</td></tr><tr><th class="string">description</th><td class="string">Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionOrTransactionHash</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/Transaction</td></tr><tr><td class="string">#/components/schemas/TransactionHash</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">uncles</th><td class="object"><table><tr><th class="string">title</th><td class="string">uncleHashes</td></tr><tr><th class="string">description</th><td class="string">Array of uncle hashes</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">uncleHash</td></tr><tr><th class="string">description</th><td class="string">Block hash of the RLP encoding of an uncle block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">FullBlock</th><td class="object"><table><tr><th class="string">title</th><td class="string">fullBlock</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">number</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumberOrNull</td></tr></table></td></tr><tr><th class="object">hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHashOrNull</td></tr></table></td></tr><tr><th class="object">parentHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHash</td></tr></table></td></tr><tr><th class="object">nonce</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/NonceOrNull</td></tr></table></td></tr><tr><th class="object">sha3Uncles</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockShaUncles</td></tr><tr><th class="string">description</th><td class="string">Keccak hash of the uncles data in the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">logsBloom</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockLogsBloom</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The bloom filter for the logs of the block or null when its the pending block</td></tr><tr><th class="string">pattern</th><td class="string">^0x[a-fA-F\d]+$</td></tr></table></td></tr><tr><th class="object">transactionsRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTransactionsRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the transactions trie of the block.</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">stateRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockStateRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the final state trie of the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">receiptsRoot</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockReceiptsRoot</td></tr><tr><th class="string">description</th><td class="string">The root of the receipts trie of the block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">miner</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/AddressOrNull</td></tr></table></td></tr><tr><th class="object">difficulty</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockDifficulty</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Integer of the difficulty for this block</td></tr></table></td></tr><tr><th class="object">totalDifficulty</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTotalDifficulty</td></tr><tr><th class="string">description</th><td class="string">Integer of the total difficulty of the chain until this block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/IntegerOrNull</td></tr></table></td></tr><tr><th class="object">extraData</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockExtraData</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The 'extra data' field of this block</td></tr></table></td></tr><tr><th class="object">size</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockSize</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Integer the size of this block in bytes</td></tr></table></td></tr><tr><th class="object">gasLimit</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockGasLimit</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The maximum gas allowed in this block</td></tr></table></td></tr><tr><th class="object">gasUsed</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockGasUsed</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The total used gas by all transactions in this block</td></tr></table></td></tr><tr><th class="object">timestamp</th><td class="object"><table><tr><th class="string">title</th><td class="string">blockTimeStamp</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The unix timestamp for when the block was collated</td></tr></table></td></tr><tr><th class="object">transactions</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionsOrHashes</td></tr><tr><th class="string">description</th><td class="string">Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionOrTransactionHash</td></tr><tr><th class="array">oneOf</th><td class="array"><table><thead><tr><th class="string">$ref</th></tr></thead><tbody><tr><td class="string">#/components/schemas/FullTransaction</td></tr><tr><td class="string">#/components/schemas/TransactionHash</td></tr></tbody></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">uncles</th><td class="object"><table><tr><th class="string">title</th><td class="string">uncleHashes</td></tr><tr><th class="string">description</th><td class="string">Array of uncle hashes</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">title</th><td class="string">uncleHash</td></tr><tr><th class="string">description</th><td class="string">Block hash of the RLP encoding of an uncle block</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">Transaction</th><td class="object"><table><tr><th class="string">title</th><td class="string">transaction</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="array">required</th><td class="array"><table><tbody><tr><td class="string">gas</td></tr><tr><td class="string">gasPrice</td></tr><tr><td class="string">nonce</td></tr></tbody></table></td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">blockHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHashOrNull</td></tr></table></td></tr><tr><th class="object">blockNumber</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumberOrNull</td></tr></table></td></tr><tr><th class="object">from</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/From</td></tr></table></td></tr><tr><th class="object">gas</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionGas</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The gas limit provided by the sender in Wei</td></tr></table></td></tr><tr><th class="object">gasPrice</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionGasPrice</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The gas price willing to be paid by the sender in Wei</td></tr></table></td></tr><tr><th class="object">hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">l2Hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">input</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionInput</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The data field sent with the transaction</td></tr></table></td></tr><tr><th class="object">nonce</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionNonce</td></tr><tr><th class="string">description</th><td class="string">The total number of prior transactions made by the sender</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Nonce</td></tr></table></td></tr><tr><th class="object">to</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/To</td></tr></table></td></tr><tr><th class="object">transactionIndex</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionIndex</td></tr></table></td></tr><tr><th class="object">value</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionValue</td></tr><tr><th class="string">description</th><td class="string">Value of Ether being transferred in Wei</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">v</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigV</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA recovery id</td></tr></table></td></tr><tr><th class="object">r</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigR</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA signature r</td></tr></table></td></tr><tr><th class="object">s</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigS</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA signature s</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">FullTransaction</th><td class="object"><table><tr><th class="string">title</th><td class="string">fullTransaction</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="array">required</th><td class="array"><table><tbody><tr><td class="string">gas</td></tr><tr><td class="string">gasPrice</td></tr><tr><td class="string">nonce</td></tr></tbody></table></td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">blockHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHashOrNull</td></tr></table></td></tr><tr><th class="object">blockNumber</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumberOrNull</td></tr></table></td></tr><tr><th class="object">from</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/From</td></tr></table></td></tr><tr><th class="object">gas</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionGas</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The gas limit provided by the sender in Wei</td></tr></table></td></tr><tr><th class="object">gasPrice</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionGasPrice</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The gas price willing to be paid by the sender in Wei</td></tr></table></td></tr><tr><th class="object">hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">input</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionInput</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The data field sent with the transaction</td></tr></table></td></tr><tr><th class="object">nonce</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionNonce</td></tr><tr><th class="string">description</th><td class="string">The total number of prior transactions made by the sender</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Nonce</td></tr></table></td></tr><tr><th class="object">to</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/To</td></tr></table></td></tr><tr><th class="object">transactionIndex</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionIndex</td></tr></table></td></tr><tr><th class="object">value</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionValue</td></tr><tr><th class="string">description</th><td class="string">Value of Ether being transferred in Wei</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">v</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigV</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA recovery id</td></tr></table></td></tr><tr><th class="object">r</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigR</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA signature r</td></tr></table></td></tr><tr><th class="object">s</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactionSigS</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">ECDSA signature s</td></tr></table></td></tr><tr><th class="object">receipt</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Receipt</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">Transactions</th><td class="object"><table><tr><th class="string">title</th><td class="string">transactions</td></tr><tr><th class="string">description</th><td class="string">An array of transactions</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Transaction</td></tr></table></td></tr></table></td></tr><tr><th class="object">Receipt</th><td class="object"><table><tr><th class="string">title</th><td class="string">receipt</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="string">description</th><td class="string">The receipt of a transaction</td></tr><tr><th class="array">required</th><td class="array"><table><tbody><tr><td class="string">blockHash</td></tr><tr><td class="string">blockNumber</td></tr><tr><td class="string">contractAddress</td></tr><tr><td class="string">cumulativeGasUsed</td></tr><tr><td class="string">from</td></tr><tr><td class="string">gasUsed</td></tr><tr><td class="string">logs</td></tr><tr><td class="string">logsBloom</td></tr><tr><td class="string">to</td></tr><tr><td class="string">transactionHash</td></tr><tr><td class="string">transactionIndex</td></tr></tbody></table></td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">blockHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHash</td></tr></table></td></tr><tr><th class="object">blockNumber</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr><tr><th class="object">contractAddress</th><td class="object"><table><tr><th class="string">title</th><td class="string">ReceiptContractAddress</td></tr><tr><th class="string">description</th><td class="string">The contract address created, if the transaction was a contract creation, otherwise null</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/AddressOrNull</td></tr></table></td></tr><tr><th class="object">cumulativeGasUsed</th><td class="object"><table><tr><th class="string">title</th><td class="string">ReceiptCumulativeGasUsed</td></tr><tr><th class="string">description</th><td class="string">The gas units used by the transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">from</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/From</td></tr></table></td></tr><tr><th class="object">gasUsed</th><td class="object"><table><tr><th class="string">title</th><td class="string">ReceiptGasUsed</td></tr><tr><th class="string">description</th><td class="string">The total gas used by the transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">logs</th><td class="object"><table><tr><th class="string">title</th><td class="string">logs</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="string">description</th><td class="string">An array of all the logs triggered during the transaction</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Log</td></tr></table></td></tr></table></td></tr><tr><th class="object">logsBloom</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BloomFilter</td></tr></table></td></tr><tr><th class="object">to</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/To</td></tr></table></td></tr><tr><th class="object">transactionHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">transactionL2Hash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">transactionIndex</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionIndex</td></tr></table></td></tr><tr><th class="object">postTransactionState</th><td class="object"><table><tr><th class="string">title</th><td class="string">ReceiptPostTransactionState</td></tr><tr><th class="string">description</th><td class="string">The intermediate stateRoot directly after transaction execution.</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">status</th><td class="object"><table><tr><th class="string">title</th><td class="string">ReceiptStatus</td></tr><tr><th class="string">description</th><td class="string">Whether or not the transaction threw an error.</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">BloomFilter</th><td class="object"><table><tr><th class="string">title</th><td class="string">bloomFilter</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">A 2048 bit bloom filter from the logs of the transaction. Each log sets 3 bits though taking the low-order 11 bits of each of the first three pairs of bytes in a Keccak 256 hash of the log's byte series</td></tr></table></td></tr><tr><th class="object">Log</th><td class="object"><table><tr><th class="string">title</th><td class="string">log</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="string">description</th><td class="string">An indexed event generated during a transaction</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">address</th><td class="object"><table><tr><th class="string">title</th><td class="string">LogAddress</td></tr><tr><th class="string">description</th><td class="string">Sender of the transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Address</td></tr></table></td></tr><tr><th class="object">blockHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockHash</td></tr></table></td></tr><tr><th class="object">blockNumber</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr><tr><th class="object">data</th><td class="object"><table><tr><th class="string">title</th><td class="string">LogData</td></tr><tr><th class="string">description</th><td class="string">The data/input string sent along with the transaction</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Bytes</td></tr></table></td></tr><tr><th class="object">logIndex</th><td class="object"><table><tr><th class="string">title</th><td class="string">LogIndex</td></tr><tr><th class="string">description</th><td class="string">The index of the event within its transaction, null when its pending</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">removed</th><td class="object"><table><tr><th class="string">title</th><td class="string">logIsRemoved</td></tr><tr><th class="string">description</th><td class="string">Whether or not the log was orphaned off the main chain</td></tr><tr><th class="string">type</th><td class="string">boolean</td></tr></table></td></tr><tr><th class="object">topics</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Topics</td></tr></table></td></tr><tr><th class="object">transactionHash</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionHash</td></tr></table></td></tr><tr><th class="object">transactionIndex</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/TransactionIndex</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">Topics</th><td class="object"><table><tr><th class="string">title</th><td class="string">LogTopics</td></tr><tr><th class="string">description</th><td class="string">Topics are order-dependent. Each topic can also be an array of DATA with 'or' options.</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Topic</td></tr></table></td></tr></table></td></tr><tr><th class="object">Topic</th><td class="object"><table><tr><th class="string">title</th><td class="string">topic</td></tr><tr><th class="string">description</th><td class="string">32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256))</td></tr><tr><th class="string">$ref</th><td class="string">#/components/schemas/DataWord</td></tr></table></td></tr><tr><th class="object">DataWord</th><td class="object"><table><tr><th class="string">title</th><td class="string">dataWord</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Hex representation of a 256 bit unit of data</td></tr><tr><th class="string">pattern</th><td class="string">^0x([a-fA-F\d]{64})?$</td></tr></table></td></tr><tr><th class="object">Bytes</th><td class="object"><table><tr><th class="string">title</th><td class="string">bytes</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">Hex representation of a variable length byte array</td></tr><tr><th class="string">pattern</th><td class="string">^0x([a-fA-F0-9]?)+$</td></tr></table></td></tr><tr><th class="object">NativeBlockHashes</th><td class="object"><table><tr><th class="string">title</th><td class="string">native block hashes</td></tr><tr><th class="string">description</th><td class="string">An array of hashes</td></tr><tr><th class="string">type</th><td class="string">array</td></tr><tr><th class="object">items</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr></table></td></tr><tr><th class="object">NativeBlockHashBlockRangeFilter</th><td class="object"><table><tr><th class="string">title</th><td class="string">NativeBlockHashBlockRangeFilter</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">fromBlock</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr><tr><th class="object">toBlock</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">ExitRoots</th><td class="object"><table><tr><th class="string">title</th><td class="string">ExitRoots</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">blockNumber</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/BlockNumber</td></tr></table></td></tr><tr><th class="object">timestamp</th><td class="object"><table><tr><th class="string">title</th><td class="string">timestamp</td></tr><tr><th class="string">type</th><td class="string">string</td></tr><tr><th class="string">description</th><td class="string">The unix timestamp of the block mentioned in the blockNumber field</td></tr></table></td></tr><tr><th class="object">mainnetExitRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr><tr><th class="object">rollupExitRoot</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Keccak</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">ZKCountersResponse</th><td class="object"><table><tr><th class="string">title</th><td class="string">ZKCountersResponse</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">countersUsed</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/ZKCountersUsed</td></tr></table></td></tr><tr><th class="object">countersLimits</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/ZKCountersLimits</td></tr></table></td></tr><tr><th class="object">revertInfo</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/RevertInfo</td></tr></table></td></tr><tr><th class="object">oocError</th><td class="object"><table><tr><th class="string">type</th><td class="string">string</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">ZKCountersUsed</th><td class="object"><table><tr><th class="string">title</th><td class="string">ZKCountersUsed</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">gasUsed</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedKeccakHashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedPoseidonHashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedPoseidonPaddings</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedMemAligns</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedArithmetics</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedBinaries</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedSteps</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">usedSHA256Hashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">ZKCountersLimits</th><td class="object"><table><tr><th class="string">title</th><td class="string">ZKCountersLimits</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">maxGasUsed</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedKeccakHashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedPoseidonHashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedPoseidonPaddings</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedMemAligns</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedArithmetics</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedBinaries</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedSteps</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr><tr><th class="object">maxUsedSHA256Hashes</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr></table></td></tr></table></td></tr><tr><th class="object">RevertInfo</th><td class="object"><table><tr><th class="string">title</th><td class="string">RevertInfo</td></tr><tr><th class="string">type</th><td class="string">object</td></tr><tr><th class="boolean">readOnly</th><td class="boolean">true</td></tr><tr><th class="object">properties</th><td class="object"><table><tr><th class="object">message</th><td class="object"><table><tr><th class="string">type</th><td class="string">string</td></tr></table></td></tr><tr><th class="object">data</th><td class="object"><table><tr><th class="string">$ref</th><td class="string">#/components/schemas/Integer</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table>
</div>

<!-- HTML generated by https://www.atatus.com/tools/json-to-html -->


## OpenRPC playground

!!! danger
    At the time of writing, the Playground was not live and may have been deprecated.

The available methods are detailed in the playground description below.

Each method description provides:

- Method name and explanation.
- Parameters required if any and their details. 
- Expected return.
- Examples.

### Instructions for use

<embed type="text/html" src="https://playground.open-rpc.org/?schemaUrl=https://raw.githubusercontent.com/0xPolygon/polygon-docs/3eb44779e7380e91e5c92f160424159a3da1bdba/docs/zkEVM/api/zkevm.openrpc.json&uiSchema[appBar][ui:input]=false&uiSchema[appBar][ui:splitView]=false" width="100%" height="1000px">