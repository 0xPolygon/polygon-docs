Polygon zkEVM, as an L2 scaling-solution to Ethereum, processes and rolls up many transactions into batches. 

The batches are sent to Ethereum, sequenced, proved to be valid, as well as being verified. All these steps are carried out under the control of smart contracts.

The aim with this document is to provide a broader sense of the protocol design while stating the currently implemented configuration.

The major components of Polygon zkEVM are:

- Consensus contract (PolygonZkEVM.sol)

- zkNode
    
    - Synchronizer

    - Sequencer & aggregator

    - RPC

- zkProver

- zkEVM bridge

The skeletal architecture of Polygon zkEVM is shown below:

![Skeletal Overview of zkEVM](../../img/zkEVM/fig1-simpl-arch.png)

## Consensus contract

The earlier version, Polygon Hermez 1.0, was based on the Proof of Donation (PoD) consensus mechanism. 

PoD was basically a decentralized auction conducted automatically, with participants (coordinators) bidding a certain number of tokens in order to be selected for creating batches.

It was based on a decentralized auction model to get the right to produce batches in a specific timeframe.

The latest Consensus Contract (PolygonZkEVM.sol) is designed to leverage the experience of the PoD in v1.0 and adds support for the permissionless participation of multiple coordinators to produce batches in L2.

In the PoD mechanism, the economic incentives were set up so the validators need to be very efficient in order to be competitive.

The latest version of the zkEVM Consensus Contract (deployed on Layer 1) is modelled after the [Proof of Efficiency](https://ethresear.ch/t/proof-of-efficiency-a-new-consensus-mechanism-for-zk-rollups/11988).

Although designed to support for permissionless participation of multiple coordinators to produce batches in L2, for security sake and due to the protocol being in its early development stages, only one coordinator (called the Sequencer) is currently brought to service.
​
### Implementation model
​
Unlike the PoD, the Consensus Contract (PolygonZkEVM.sol) employs a simpler technique and is favoured due to its greater efficiency in resolving the challenges involved in PoD.

The strategic implementation of the contract-based consensus ensures that the network:

- Maintains its permissionless feature to produce L2 batches.
- Is highly efficient, a criterion which is key for the overall network performance.
- Attains an acceptable degree of decentralization.
- Is protected from malicious attacks, especially by validators.
- Maintains a fair balance between overall validation effort and network value.

!!!tip
    Good to Know

    Possibilities of coupling the Consensus Contract (previously called Proof of Efficiency or PoE) with a PoS (Proof of Stake) are currently being explored. A detailed description is published on the [Ethereum Research](https://ethresear.ch/t/proof-of-efficiency-a-new-consensus-mechanism-for-zk-rollups/11988) website.

### On-chain data availability
​
A full zk-rollup schema requires on-chain publication of both the transaction data (which users need to reconstruct the full state) and the validity proofs (zero-knowledge proofs).

However, given the Ethereum configuration, publishing data on-chain incurs gas prices, making the choice between a full zk-rollup and a hybrid configurations challenging.

Under a Hybrid schema, either of the following is possible:

- Validium: Data is stored off-chain and only the validity proofs are published on-chain.
- Volition: For some transactions, both the data and the validity proofs remain on-chain while for the remaining ones, only proofs go on-chain.

Unless, among other things, the proving module can be highly accelerated to mitigate costs for the validators, a Hybrid schema remains viable.
​
### `PolygonZkEVM.sol`
​
The underlying protocol in zkEVM ensures that the state transitions are correct by employing a validity proof.

In order to ensure that a set of pre-determined rules have been followed when allowing state transitions, the consensus contract (`PolygonZkEVM.sol`, deployed on L1) is utilized.
​
!!!info
    The consensus contract is currently deployed on both [Ethereum Mainnet](https://etherscan.io/address/0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2) and [Cardona Testnet](https://sepolia.etherscan.io/address/0xa997cfD539E703921fD1e3Cf25b4c241a27a4c7A).
​
A smart contract verifies the validity proofs to ensure that each transition is completed correctly. 

The verification is accomplished by employing zk-SNARK circuits. 

A system of this type requires two processes: transaction batching and transaction validation.

Polygon zkEVM employs two types of participants in order to carry out the two procedures: A sequencer and an aggregator.

Under this two-layer model:

- The sequencer proposes transaction batches to the network for execution. That is, they roll-up transaction requests into batches and add them to the Consensus Contract.
​
- The aggregator checks the validity of the transaction batches and provides validity proofs.

The smart contract, therefore, makes two calls:

- Firstly, to receive batches from the sequencer.
- Secondly to aggregators, requesting batches to be validated.
​
![Simplified proof of efficiency](../../img/zkEVM/fig2-simple-poe.png)

!!!info
    
    Although the current protocol design allows for several sequencers and aggregators, for the sake of security and due to the protocol being in its early development stages, only one sequencer and one aggregator are currently put into service.

    These are henceforth referred to as _trusted sequencer_ and _trusted aggregator_. 

### Tokenomics

The consensus smart contract imposes the following requirements on the trusted sequencer and the trusted aggregator:
​
#### Sequencer

- The trusted sequencer must run the software necessary for a full zkEVM node.

- The trusted sequencer should pay a fee in the form of POL tokens for the right to create and process batches.

- The trusted sequencer is incentivized for proposing valid batches (which consist of valid transactions,) with the fees paid by the users of the network who sent the transactions.

#### Aggregator

An trusted aggregator receives all the transaction information from the trusted sequencer and sends it to the prover, which in turn provides a zk-proof after performing some complex computations. 

A special _verfier_ smart contract validates the validity proof.

The trusted aggregator's task is to therefore:

- Provide validity proofs for the L2 transactions proposed by the trusted sequencer.

- Run zkEVM's zkNode software and the zkProver for creating the zero-knowledge validity proofs.

- For a given batch, the trusted aggregator earns the POL fees (paid by the trusted sequencer) for providing a validity proof.

- In a decentralized setting, an trusted aggregator needs to indicate their intention to validate transactions. And subsequently competes to produce validity proofs based on their own strategy.

## zkNode

zkNode is the software needed to run a zkEVM node. It is a client that the network requires to implement the synchronization and govern the roles of the participants (trusted sequencer or trusted aggregator).

Other than the trusted sequencer and the trusted aggregator, participants in the Polygon zkEVM network can take part as nodes that seek to know the state of the network.

The zkNode architecture is modular in nature. You can dig deeper into zkNode and its components [here](zknode/index.md).

### Incentivization structure

The two permissionless participants of the zkEVM network are the trusted sequencer and the trusted aggregator.

Proper incentive structures have been devised to keep the zkEVM network fast and secure.

Below is a summary of the fee structure for the trusted sequencer and the trusted aggregator:

- Sequencer
    
    - Collects transactions from a designated pool DB and puts them in a batch.
    - Receives fees paid by users who submitted the transactions.
    - Pays L1 transaction fees + POL (depending on pending batches).
    - The POL tokens go to the trusted aggregator.
    - Profitable if: `txs fees` > `L1 call` + `POL` fee.

- Aggregator
    
    - Processes transactions published by the trusted sequencer.
    - Builds zkProof.
    - Receives POL tokens from the trusted sequencer.
    - Static cost: L1 call cost + server cost (to build a proof).
    - Profitable if: `POL fees` > `L1 call cost` + `server cost`

  See the [Effective gas price document](../architecture/effective-gas/index.md) for how users can estimate the gas price to sign transactions with.

## zkProver

zkEVM employs zero-knowledge technology to create validity proofs.

It uses a zero-knowledge prover (zkProver), which is intended to run on a server and is being engineered to be compatible with most consumer hardware.

The trusted aggregator uses the zkProver to validate batches and provide validity proofs.

The zkProver consists of a main state machine executor, a collection of secondary state machines (some with their own executor), a STARK-proof builder, and a SNARK-proof builder.

![Skeletal overview of zkProver](../../img/zkEVM/fig4-zkProv-arch.png)

In a nutshell, the zkEVM expresses state changes in polynomial form. 

As a result, the constraints that each state transition must fulfil are polynomial constraints or polynomial identities.

In other words, all valid batches must satisfy specific polynomial constraints. 

Check out the detailed architecture of the zkProver [here](zkprover/index.md).

## zkEVM bridge

The zkEVM bridge is a smart contract that lets users transfer their assets between two layers, LX and LY.

The L1-L2 in zkEVM is a decentralized bridge for secure deposits and withdrawal of assets.

It is a combination of two smart contracts, one deployed on one chain and the second on the other.

The L1 and L2 contracts in zkEVM are identical except for where each is deployed.

Bridge L1 contract is on the Ethereum mainnet in order to manage asset transfers between rollups, while bridge L2 contract is on a specific rollup and it is responsible for asset transfers between mainnet and the rollup (or rollups).

Layer 2 interoperability allows a native mechanism to migrate assets between different L2 networks. This solution is embedded in the bridge smart contract.

## Verifier

Verifier is a smart contract which is able to verify any zk-SNARK cryptographic proof. 

The SNARK verifier proves the validity of every transaction in the batch.

It is the key entity in any zk-rollup architecture as it verifies the correctness of each proof, and thus ensuring integrity in state transitions.

The verifier contract is currently deployed on the [Ethereum mainnet](https://etherscan.io/address/0x4F9A0e7FD2Bf6067db6994CF12E4495Df938E6e9) and [Cardona testnet](https://sepolia.etherscan.io/address/0x8EdA1d8c254a77a57A6A7A1C0262e9A44A7C6D6d).

## Transaction life cycle

Before getting transactions in the L2 flow, users need some funds to perform any L2 transaction.

To do so, users need to transfer some ether from L1 to L2 through the zkEVM bridge dApp.

- Bridge
    
    - Deposit ETH.
    - Wait until `globalExitRoot` is posted on L2.
    - Perform claim on L2 and receive the funds.

- L2 transactions
    
    - User initiates a transation in a wallet (e.g. MetaMask) and sends it to a trusted sequencer.

    - The transaction gets finalized on L2 once the trusted sequencer commits to adding the transaction to a batch. This is known as the trusted state.

    - Sequencer sends the batch data to L1 smart contract, enabling any L2 node to synchronize from L1 in a trustless way. This is also known as the virtual state.

    - Aggregator will take pending transactions, and build a proof.

    - Once the proof is verified, user's transactions attain L1 finality (important for withdrawal purposes). This is called the consolidated state.

The above process is a summarized version of how transactions are processed in Polygon zkEVM. 

Take a look at the complete description in the [transaction life cycle](protocol/transaction-life-cycle/submit-transaction.md) document.

## Design characteristics

The Polygon zkEVM network is secure, efficient, and comes with verifiable block data.

Development efforts aim at permissionless-ness, that is, allowing anyone with the zkEVM software to participate in the network. For instance, the consensus algorithm could give anyone the opportunity to be an aggregator.

Data availability is most crucial for decentralization, where every user has sufficient data needed to rebuild the full state of a rollup. As a rollup, Polygon zkEVM posts all transaction data and validity proof on Ethereum.

The aim is to ensure that there is no censorship and that no one party can control the network. For this reason, mechanisms such as [force batches](protocol/malfunction-resistance/sequencer-resistance.md) and [force verification](protocol/malfunction-resistance/aggregator-resistance.md) have been activated.

Polygon zkEVM was designed with security in mind. As an L2 solution, it inherits its security from Ethereum.

Smart contracts are deployed to ensure that everyone who executes state changes does so appropriately, creates a proof that attests to the validity of a state change, and makes validity proofs available on-chain for verification.

## Efficiency and overall strategy

Efficiency is key to network performance. Polygon zkEVM applies several implementation strategies to guarantee efficiency. A few of them are listed below:

1. The first strategy is to deploy the consensus contract, which incentivizes the aggregator to participate in the proof generation process.

2. The second strategy is to carry out all computations off-chain while keeping only the necessary data and zk-proofs on-chain.

3. The bridge smart contract's implementation is made efficient by only using Merkle roots of exit trees.

4. Utilization of specialized cryptographic primitives within the zkProver in order to speed up computations and minimize proof sizes, as seen in:
    
    - Running a special zero-knowledge assembly language (zkASM) for interpretation of bytecode.

    - Using zero-knowledge tools such as zk-STARKs for proving purposes; these proofs are very fast though they are big in size.

    - Instead of publishing the sizeable zk-STARK proofs as validity proofs, a zk-SNARK is used to attest to the correctness of the zk-STARK proofs. These zk-SNARKs are, in turn, published as the validity proofs to state changes. This helps in reducing the gas costs from 5M to 350K.
