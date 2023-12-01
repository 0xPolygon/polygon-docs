Mechanism for transferring data from Polygon to Ethereum is a little different from doing the same for Ethereum to Polygon. The **checkpoint** transactions created by the Validators on the Ethereum chain are used for achieving this. Basically a transaction is initially created on Polygon. While creating this transaction it has to be ensured that an **event is emitted** and the **event logs includes the data we wish to transfer** from Polygon to Ethereum.

In a period of time ( about 10-30 mins ), this transaction is check-pointed on the Ethereum chain by the validators. Once checkpointing is done, the hash of the transaction created on the Polygon chain can be submitted as a proof on the **RootChainManager** contract on the Ethereum chain. This contract, validates the transaction, verifies that this transaction is included in the checkpoint and finally decodes the event logs from this transaction.

Once this phase is over, we can use the **decoded event log data to perform any change** on the root contract deployed on the Ethereum chain. For this we also need to ensure that, the change of state on Ethereum is only done in a secure way. Hence, we make use of a **Predicate** contract which is a special type of contract that can be only triggered by the **RootChainManager** contract. This architecture ensures that the state changes on Ethereum happens only when the transaction on Polygon is check pointed and verified on the Ethereum chain by the **RootChainManager** contract.

## Overview

- A transaction is executed on the child contract deployed on the Polygon chain.
- An event is also emitted in this transaction. The parameters of this **event includes the data which has to be transferred** from Polygon to Ethereum.
- The validators on the Polygon network picks up this transaction in a specific interval of time( probably 10-30mins), validates them and **adds them to the checkpoint** on Ethereum.
- A checkpoint transaction is created on the **RootChain** contract and the checkpoint inclusion can be checked using this [script](https://github.com/rahuldamodar94/matic-learn-pos/blob/transfer-matic-ethereum/script/check-checkpoint.js)
- Once the checkpoint addition is completed, the **matic.js** library can be used to call the **exit** function of the **RootChainManager** contract. **exit** function can be called using the matic.js library as shown in this [example](https://github.com/rahuldamodar94/matic-learn-pos/blob/transfer-matic-ethereum/script/exit.js).

- Running the script, verifies the inclusion of the Polygon transaction hash on Ethereum chain, and then in turn calls the **exitToken** function of the [predicate](https://github.com/rahuldamodar94/matic-learn-pos/blob/transfer-matic-ethereum/contracts/CustomPredicate.sol) contract.
- This ensures that the **state change on the root chain contract** is always done in a **secure** way and **only through the predicate contract**.
- The important thing to note is that the **verification of the transaction hash** from Polygon and **triggering the predicate** contract happens in a **single transaction** and thus ensuring security of any state change on root contract.

## Implementation

This is a simple demonstration of how data can be transferred from Polygon to Ethereum. This tutorial shows an example of transferring a uint256 value across the chain. But you can transfer type of data. But it is necessary to encode the data in bytes and then emit it from the child contract. It can be finally decoded at the root contract.

1. First create the root chain and child chain contract. Ensure that the function that does the state change also emits an event. This event must include the data to be transferred as one of its parameters. A sample format of how the Child and Root contract must look like is given below. This is a very simple contract that has a data variable whose value is set by using a setData function. Calling the setData function emits the Data event. Rest of the things in the contract will be explained in the upcoming sections of this tutorial.

A. Child Contract

```javascript
contract Child {

    event Data(address indexed from, bytes bytes_data);

    uint256 public data;

    function setData(bytes memory bytes_data) public {
     data = abi.decode(bytes_data,(uint256));
     emit Data(msg.sender,bytes_data);
    }

}
```

B. Root Contract

Pass this `0x1470E07a6dD1D11eAE439Acaa6971C941C9EF48f` as the value for `_predicate` in the root contract constructor.

```javascript
contract Root {

    address public predicate;
    constructor(address _predicate) public{
        predicate=_predicate;
    }

   modifier onlyPredicate() {
        require(msg.sender == predicate);
        _;
    }

    uint256 public data;

    function setData(bytes memory bytes_data) public onlyPredicate{
        data = abi.decode(bytes_data,(uint256));
    }

}
```

2. Once the child and root contract is deployed on the Polygon and Ethereum chain respectively, these contracts have to be mapped using the PoS bridge. This mapping ensures that a connection is maintained between these two contracts across the chains. For doing this mapping,the Polygon team can be reached on [discord](https://discord.com/invite/0xPolygon).

3. One important thing to note is that, in the root contract, there is a onlyPredicate modifier. It is recommended to use this modifier always because it ensures that only the predicate contract makes the state change on the root contract. The predicate contract is a special contract that triggers the root contract only when the transaction that happened on the Polygon chain is verified by the RootChainManager on Ethereum chain. This ensures secure change of state on the root contract.

For testing the above implementation, we can create a transaction on the Polygon chain by calling the **setData** function of the child contract. We need to wait at this point for the checkpoint to be completed. The checkpoint inclusion can be checked using this [script](https://github.com/rahuldamodar94/matic-learn-pos/blob/transfer-matic-ethereum/script/check-checkpoint.js). Once checkpoint is completed, call the exit function of the RootChainManager using the matic.js SDK.

```jsx
const txHash =
  "0xc094de3b7abd29f23a23549d9484e9c6bddb2542e2cc0aa605221cb55548951c";

const logEventSignature =
  "0x93f3e547dcb3ce9c356bb293f12e44f70fc24105d675b782bd639333aab70df7";

const execute = async () => {
  try {
    const tx = await maticPOSClient.posRootChainManager.exit(
      txHash,
      logEventSignature
    );
    console.log(tx.transactionHash); // eslint-disable-line
  } catch (e) {
    console.error(e); // eslint-disable-line
  }
};
```

As shown in the above screenshot, the **txHash** is the transaction hash of the transaction that happened on the child contract deployed on Polygon chain.

The **logEventSignature** is the keccack-256 hash of the Data event. This is the same hash that we have included in the Predicate contract. All the contract code used for this tutorial and the exit script can be found [here](https://github.com/rahuldamodar94/matic-learn-pos/tree/transfer-matic-ethereum)

Once the exit script is completed, the root contract on Ethereum chain can be queried to verify if the value of the variable **data** that was set in child contract has also been reflected in the **data** variable of the root contract.
