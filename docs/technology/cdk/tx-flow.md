## zkEVM

All transaction data is published on L1. 

## Validium

Validium only publishes the hash of the transaction data. This hash, termed the _Accumulated Input Hash_, must be approved by a majority of the DAC members. 

The Sequencer sends both the hash and the transaction data to the DAC for verification. Once approved, the hash, along with the signatures from the DAC members, is sent to the Consensus L1 contract of the Validium protocol. 

After verification, the hash and the ZK-proof are added to the L1 State, forming the _Consolidated State_.