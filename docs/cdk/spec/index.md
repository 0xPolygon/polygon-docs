This section gives a comparison between a validium and a zk-rollup. 

The main difference is the fact that a validium has a data availability layer whereas a zk-rollup does not. This difference alone is the reason for the substantially reduced gas fees for a validium compared to the zk-rollup.

However, with this off-chain data availability, there is a trade-off between gas fees and security. Unlike in the zk-rollup, where forced batches are activated, the validium suffers from the possibility for the sequencer to go offline or the DAC to collude among themselves to withhold state data.

What remains common between the two architectures is the generation of proofs.