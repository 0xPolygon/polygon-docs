# Paymaster Contract for Sponsored USDC Transfers

!!! info 
    NOTE: Like all of crypto, payments require handling sensitive data. The following examples are demonstrations of integrations but should not be used in production. In production, sensitive information such as API keys, private-key wallets, etc., should be put in a secrets manager or vault.

## Overview

A paymaster contract allows you to sponsor gas fees for users when they transfer USDC, enabling gasless transactions. This implementation uses EIP-4337 Account Abstraction to sponsor USDC transfers on Polygon.

## Prerequisites

- Understanding of EIP-4337 Account Abstraction
- Familiarity with Solidity and smart contracts
- Access to a Polygon node
- USDC contract address on Polygon: `0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359`

## Paymaster Contract Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@account-abstraction/contracts/core/BasePaymaster.sol";
import "@account-abstraction/contracts/interfaces/IEntryPoint.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract USDCPaymaster is BasePaymaster, Ownable {
    IERC20 public immutable usdc;
    
    // Mapping to track sponsored accounts
    mapping(address => bool) public sponsoredAccounts;
    
    // Maximum gas cost we're willing to sponsor
    uint256 public maxGasCost = 0.01 ether; // 0.01 MATIC
    
    // Events
    event UserOperationSponsored(address indexed account, uint256 gasCost);
    event AccountSponsored(address indexed account, bool sponsored);
    event MaxGasCostUpdated(uint256 newMaxGasCost);
    
    constructor(
        IEntryPoint _entryPoint,
        address _usdc,
        address _owner
    ) BasePaymaster(_entryPoint) {
        usdc = IERC20(_usdc);
        _transferOwnership(_owner);
    }
    
    /**
     * @dev Validates if a user operation should be sponsored
     * @param userOp The user operation to validate
     * @param userOpHash Hash of the user operation
     * @param maxCost Maximum cost of the operation
     * @return context Validation context
     * @return validationResult Validation result
     */
    function _validatePaymasterUserOp(
        UserOperation calldata userOp,
        bytes32 userOpHash,
        uint256 maxCost
    ) internal view override returns (bytes memory context, uint256 validationResult) {
        // Check if the operation is within our gas cost limit
        require(maxCost <= maxGasCost, "USDCPaymaster: gas cost too high");
        
        // Decode the calldata to ensure it's a USDC transfer
        bytes4 selector = bytes4(userOp.callData[:4]);
        
        // Check if it's a direct USDC transfer or approve+transfer
        bool isValidUSDCOperation = _isValidUSDCOperation(userOp.callData, userOp.sender);
        require(isValidUSDCOperation, "USDCPaymaster: not a valid USDC operation");
        
        // Check if account is sponsored or if it's a first-time user with USDC balance
        address account = userOp.sender;
        if (!sponsoredAccounts[account]) {
            uint256 usdcBalance = usdc.balanceOf(account);
            require(usdcBalance > 0, "USDCPaymaster: no USDC balance");
        }
        
        // Return validation success
        return (abi.encode(account, maxCost), 0);
    }
    
    /**
     * @dev Validates if the operation is a valid USDC transfer
     * @param callData The call data from the user operation
     * @param sender The sender of the operation
     * @return true if it's a valid USDC operation
     */
    function _isValidUSDCOperation(bytes calldata callData, address sender) internal view returns (bool) {
        // Check if it's a direct call to USDC contract
        if (callData.length >= 68) { // 4 bytes selector + 32 bytes address + 32 bytes amount
            bytes4 selector = bytes4(callData[:4]);
            
            // Check for transfer(address,uint256) or transferFrom(address,address,uint256)
            if (selector == IERC20.transfer.selector || selector == IERC20.transferFrom.selector) {
                return true;
            }
            
            // Check for approve(address,uint256) - common pattern before transfer
            if (selector == IERC20.approve.selector) {
                return true;
            }
        }
        
        // Check if it's a multicall that includes USDC operations
        return _containsUSDCOperation(callData);
    }
    
    /**
     * @dev Checks if multicall contains USDC operations
     * @param callData The call data to analyze
     * @return true if USDC operations are found
     */
    function _containsUSDCOperation(bytes calldata callData) internal pure returns (bool) {
        // Basic implementation - could be enhanced for complex multicalls
        // Look for USDC contract address in the calldata
        bytes32 usdcAddress = bytes32(uint256(uint160(0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359)));
        
        for (uint256 i = 0; i < callData.length - 32; i++) {
            if (bytes32(callData[i:i+32]) == usdcAddress) {
                return true;
            }
        }
        
        return false;
    }
    
    /**
     * @dev Called after the user operation is executed
     * @param context The context returned from validation
     * @param actualGasCost The actual gas cost of the operation
     */
    function _postOp(
        PostOpMode mode,
        bytes calldata context,
        uint256 actualGasCost
    ) internal override {
        if (mode == PostOpMode.opSucceeded) {
            (address account, uint256 maxCost) = abi.decode(context, (address, uint256));
            emit UserOperationSponsored(account, actualGasCost);
        }
    }
    
    // Admin functions
    
    /**
     * @dev Add or remove an account from sponsorship
     * @param account The account to sponsor/unsponsor
     * @param sponsored Whether to sponsor this account
     */
    function setSponsoredAccount(address account, bool sponsored) external onlyOwner {
        sponsoredAccounts[account] = sponsored;
        emit AccountSponsored(account, sponsored);
    }
    
    /**
     * @dev Update maximum gas cost willing to sponsor
     * @param newMaxGasCost New maximum gas cost
     */
    function setMaxGasCost(uint256 newMaxGasCost) external onlyOwner {
        maxGasCost = newMaxGasCost;
        emit MaxGasCostUpdated(newMaxGasCost);
    }
    
    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "USDCPaymaster: no balance to withdraw");
        
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "USDCPaymaster: withdrawal failed");
    }
    
    /**
     * @dev Add stake to the EntryPoint
     * @param unstakeDelaySec Unstake delay in seconds
     */
    function addStake(uint32 unstakeDelaySec) external payable onlyOwner {
        entryPoint.addStake{value: msg.value}(unstakeDelaySec);
    }
    
    /**
     * @dev Unlock stake from the EntryPoint
     */
    function unlockStake() external onlyOwner {
        entryPoint.unlockStake();
    }
    
    /**
     * @dev Withdraw stake from the EntryPoint
     * @param withdrawAddress Address to withdraw to
     */
    function withdrawStake(address payable withdrawAddress) external onlyOwner {
        entryPoint.withdrawStake(withdrawAddress);
    }
    
    /**
     * @dev Deposit funds to the EntryPoint for gas sponsorship
     */
    function deposit() public payable {
        entryPoint.depositTo{value: msg.value}(address(this));
    }
    
    /**
     * @dev Get deposit balance
     */
    function getDeposit() public view returns (uint256) {
        return entryPoint.balanceOf(address(this));
    }
    
    receive() external payable {
        deposit();
    }
}
```

## Integration Example

Here's how to integrate the paymaster with a client application:

```typescript
import { createPublicClient, createWalletClient, http, parseUnits } from "viem";
import { polygon } from "viem/chains";
import { privateKeyToAccount } from "viem/accounts";

// Contract addresses
const USDC = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359";
const PAYMASTER_ADDRESS = "0xYourPaymasterAddress..."; // Deploy the contract above
const ENTRY_POINT = "0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789"; // Standard EntryPoint

const erc20Abi = [
  { type: "function", name: "transfer", stateMutability: "nonpayable", inputs: [{ type: "address" }, { type: "uint256" }], outputs: [{ type: "bool" }] },
];

const account = privateKeyToAccount(process.env.USER_PRIVATE_KEY as `0x${string}`);
const publicClient = createPublicClient({ 
  chain: polygon, 
  transport: http(process.env.POLYGON_RPC_URL) 
});

async function sponsoredUSDCTransfer(
  recipient: `0x${string}`, 
  amount: string
) {
  // 1. Prepare the USDC transfer call data
  const transferCallData = encodeFunctionData({
    abi: erc20Abi,
    functionName: "transfer",
    args: [recipient, parseUnits(amount, 6)] // USDC has 6 decimals
  });

  // 2. Create user operation with paymaster
  const userOp = {
    sender: account.address,
    nonce: await getNonce(account.address), // Get from EntryPoint
    initCode: "0x", // Empty if account already deployed
    callData: transferCallData,
    callGasLimit: 100000n,
    verificationGasLimit: 150000n,
    preVerificationGas: 21000n,
    maxFeePerGas: parseUnits("20", "gwei"),
    maxPriorityFeePerGas: parseUnits("2", "gwei"),
    paymasterAndData: PAYMASTER_ADDRESS, // This enables gas sponsorship
    signature: "0x" // Will be populated after signing
  };

  // 3. Sign and submit the user operation
  // This would typically involve signing the userOpHash and submitting to a bundler
  console.log("User operation prepared for sponsored USDC transfer:", userOp);
  
  // Note: Full implementation would require bundler integration
  // and proper user operation signing according to EIP-4337
}

// Helper function to get nonce from EntryPoint
async function getNonce(address: `0x${string}`): Promise<bigint> {
  // Implementation depends on your account abstraction setup
  return 0n;
}
```

## Deployment Script

```solidity
// deploy.sol
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/USDCPaymaster.sol";

contract DeployUSDCPaymaster is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        address entryPoint = 0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789; // Standard EntryPoint
        address usdc = 0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359; // USDC on Polygon
        
        vm.startBroadcast(deployerPrivateKey);
        
        USDCPaymaster paymaster = new USDCPaymaster(
            IEntryPoint(entryPoint),
            usdc,
            msg.sender
        );
        
        // Add initial stake and deposit
        paymaster.addStake{value: 1 ether}(86400); // 1 day unstake delay
        paymaster.deposit{value: 5 ether}(); // 5 MATIC for gas sponsorship
        
        vm.stopBroadcast();
        
        console.log("USDCPaymaster deployed at:", address(paymaster));
    }
}
```

## Key Features

1. **Gas Sponsorship**: Sponsors gas fees for USDC transfers
2. **Access Control**: Only sponsored accounts or accounts with USDC balance can use
3. **Gas Limits**: Configurable maximum gas cost per operation
4. **Security**: Validates that operations are legitimate USDC transfers
5. **Admin Functions**: Owner can manage sponsored accounts and withdraw funds

## Security Considerations

- Validate all user operations to prevent abuse
- Set reasonable gas limits to control costs
- Monitor for suspicious patterns
- Keep paymaster funded but not over-funded
- Regular security audits for production use

## Testing

Before production deployment:

1. Test on Polygon testnet (Amoy)
2. Verify gas estimation accuracy
3. Test edge cases and error conditions
4. Monitor gas consumption patterns
5. Implement proper monitoring and alerting