## Polygon network infrastructure security

Polygon Labs has developed network infrastructure via smart contracts that automatically transfers assets to-and-from the Ethereum blockchain for both the Polygon PoS network and Polygon zkEVM scaling solution. This infrastructure implements a lock-and-mint architecture which results in assets being locked by the smart contract implementations. 

On behalf of the Polygon community and broader industry, Polygon Labs has implemented certain monitoring features over the network infrastructure to enhance security.  Much of the security efforts noted here are rigorously applied to network infrastructure, including risk management, secure software development practices, auditing, vulnerability management, CI/CI, on-chain monitoring, and bug bounties.

## Monitoring

The on-chain infrastructure is monitored for real-time events as a way to augment the application security efforts associated with software development (i.e. threat modeling, code auditing, library and supply-chain risk, and bug bounties). The real time monitoring includes both on-chain machine learning models to detect unknown threats in real-time, as well as empirical rule-based algorithms to capture known adversarial or error scenarios. 

The monitoring infrastructure was developed both in-house, and by vendors as needed, to augment our capabilities in specific analysis areas. Any adverse events detected by our models and tools are evaluated, triaged and, if necessary, escalated to the proper team for further analysis. The monitoring process is integrated with our enterprise incident response process.

## Multisig security

Specific requirements are followed by any Polygon Labs employee that is a signer on a multisig contract, which are used for various security reasons.  Multisigs consist of Safes (previously Gnosis Safes) and other smart contract multisig implementations. Hardware wallets are hardware-based cold storage, such as Trezor or Ledger devices that store private keys and enable signing multisig transactions offline. Signer multisig requirements include:

- Hardware wallet: Polygon Labs requires cold storage from an accepted vendor dedicated for company official use only and secured by a PIN.
- Hot wallets: Hot wallets are not allowed for use on Polygon Labs’ multisigs.
- Corporate workstation: Signing must be performed from a company system managed by our enterprise mobile device management (MDM) platform complete with anti-virus (AV) and endpoint detection and device (EDR).
- Clean key: All signers are required to create a clean key that has never been exposed to a hot wallet.
- Mnemonic storage: Polygon Labs mandates safe storage of mnemonic passphrases and provides guidance to its employees.
- Secure communication: All multisig signing events are coordinated using Polygon Labs’ accepted communication protocols for multisigs.

**All corporate multisigs are monitored 24/7 by the Polygon security team.**

