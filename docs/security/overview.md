The purpose of this document is to provide an overview of the security measures and capabilities of Polygon Labs.

At Polygon Labs, ensuring the security of our information systems and safeguarding the sensitive data of our clients and employees is of paramount importance. We prioritize security throughout every facet of our operations, from implementing robust security policies and guidelines to adopting industry best practices, such as adhering to the OWASP recommendations for secure software development. We invest heavily in continuous security training for our employees, keeping them informed of emerging threats and equipping them with the necessary skills to protect our digital assets. In addition, we embrace a proactive approach by incorporating security by design principles and utilizing state-of-the-art security tools to detect and mitigate vulnerabilities at every stage of the development lifecycle.

## Commitment to security

**Dedicated security team**

Security comes first at Polygon Labs and our commitment is proven by our in-house security team of 10+ full-time security engineers & leaders. The team remains involved in the web3 space and together with other major organizations is driving new innovations and best practices for all. 

**Continuous Monitoring**

Polygon Labs monitors the bridge and related smart contracts for suspicious activities. Polygon’s in-house security team works alongside the Polygon development teams  and other industry experts to stay updated on known vulnerabilities in the space.

**Periodic Security Assessments**

Polygon Labs periodically assesses the security its products and applications through extensive internal testing and external engagements, such as audits and penetration testing. All products and applications have been assessed multiple times to date. Security assessments continue as the ecosystem matures.

**Bug Bounty Program**

Developers of Polygon have ongoing bug bounty programs on leading Bug Bounty platforms with rewards of up to $1M for reported vulnerabilities in Polygon contracts. It was the most significant bounty program in the web3 community at the time of launch.

**Enable developer community**

Polygon Labs is committed to enabling the developer community, allowing them to surface vulnerabilities and patching them before they are exploited.  Polygon Labs has a strict focus on security in our development lifecycle, heavily testing all code and following best practices and standards such as the Secure Software Development Lifecycle.

## Security Governance & Management 

Polygon Labs' security program is designed and implemented following the ISO/IEC 27001 standards, an internationally recognized framework for managing and securing sensitive information assets. By adhering to these standards, Polygon Labs demonstrates a strong commitment to the protection of its clients' and employees' data, ensuring that confidentiality, integrity, and availability are maintained at all times.

The ISO27001-based security program at Polygon Labs involves the establishment of an Information Security Management System (ISMS), which is a systematic approach to managing sensitive information and minimizing risk. This includes conducting regular risk assessments to identify, analyze, and evaluate potential threats and vulnerabilities, as well as implementing appropriate security controls and measures to mitigate those risks.

In addition to risk assessments, Polygon Labs' ISMS incorporates a comprehensive set of policies, procedures, and guidelines that cover various aspects of information security, such as access control, incident management, and business continuity planning. Employee training and awareness programs are also an integral part of the security program, ensuring that staff members understand their roles and responsibilities in safeguarding the organization's information assets.

Polygon Labs has a security team led by a CISO reporting to founders.

## Security Risk Management
Polygon Lab's approach to security risk management leverages a process driven approach using a risk management framework to systematically assess, manage and mitigate risk, while aligning security controls to international compliance requirements. The program provides a real-time view of Polygon Labs's current security posture while informing the security roadmap as new controls are continuously implemented and re-assessed to adjust for a dynamic threat environment. Some key initiatives and aspects of the Polygon Infrastructure Information Risk Management Program include:

- **Risk Assessment:** The objective of a risk assessment is to enumerate threats, identify vulnerabilities, determine the organizational impact of a threat along with the likelihood of the threat occurring. This process informs other aspects of the risk management process, including assessing the implementation or enhancement of security controls and measuring organizational residual risk. A risk assessment provides a risk-based approach to systematically identify high-risk areas of focus.
- **Standardized Controls:** while every situation is unique, we understand the benefit of leveraging best practices. For the cloud we leverage the CIS v8 control set. 
- **Residual Risk:** Any risk identified in the risk assessment requires analysis and a plan of action (i.e. Reduce, Avoid, Transfer, Accept). The implementation of mitigating controls is driven by a cost-benefit analysis of the impact and mitigation using both the Factor Analysis of Information Risk (FAIR) and qualitative approaches. FAIR is an internationally accepted standard which quantifies risk in financial terms.
- **Compliance**: Polygon Labs maps security controls to various compliance initiatives such as ISO 27002. ISO 27002 controls provide near-universal mapping to other compliance requirements.
- **Security Roadmap:** The risk management program continuously maps to the controls implementation framework as we adjust to new threats and evolving internal product suite.
- **Monitoring:** We strive for continuous monitoring for situational awareness and security posture management.
- **Benchmarks:** Where possible, we leverage benchmarks that provide specific and measurable metrics for compliance with control requirements and policies. This provides KPIs that guide implementation efforts and feed into our residual risk and any continuous risk assessment activities. We strive to automate metrics, for example using scanning tools that directly measure control compliance to benchmarks.

The risk management framework is supported by various internal and external resources including penetration testers and auditors for independent verification and validation.

## Human Resources Security

Polygon supports onboarding and offboarding employees by following a process that begins with each employee receiving a preconfigured laptop that auto enrolls in one of our Mobile Device Management Systems (MDM). MDM supports control of application usage and enforces security policy requirements on approved operating system versions and patch requirements.  User access to shared services and Polygon approved SaaS tools is aligned with the secure approach of providing the least amount of privileges required for an employee to perform their tasks.  Privileges are role based and given to each employee based on the functional team they are assigned to.   

Polygon uses single sign-on technologies to automate the administration of users access and permissions across all of our SaaS tools.  Automating the provisioning and removal of users' access privileges limits the risk of human error and supports efficient auditing procedures. 

When an employee exits the company, HR changes their status in our HRIS system,automatically removing their access to our SSO integrated SaaS platforms, and IT is immediately notified to initiate the wipe and recovery of their corporate system.  

### Security Awareness Training

Polygon utilizes a SaaS platform to provide an integrated approach to email and security awareness training for all of our employees.  All employees are required to pass the training during their first weeks of employment.  The key features of the platform are::
  
- **Industry-specific modules** - Reinforce critical concepts mapped to key industry standards and security frameworks, including ISO, NIST, PCI DSS, GDPR, and HIPAA
- **Real-world assessment** -  Safely test employees on real-world threats with de-weaponized phishing attacks
- **Comprehensive reporting** - Track primary indicators of risk across the awareness training platform and take remedial action with easily discernible user risk scores
- **Integrated risk insight** - Leverage real-world click behavior to identify high risk users
- **Effortless administration**- 12-month programs with rapid deployment. 


## Infrastructure Security 

### Polygon Bridge Security

Polygon develops and maintains bridges to transfer assets to-and-from the Ethereum blockchain for both the Polygon PoS network and Polygon zkEVM scaling solution. These bridges implement a lock-and-mint architecture which results in assets being controlled (locked) by the bridge smart contract implementations. As the aggregate value of locked assets on Polygon bridges is significant, we apply a corresponding focus on bridge security. Much of the security efforts documented here are rigorously applied to bridge security, including risk management, secure software development practices, auditing, vulnerability management, CI/CI and bug bounties. We leverate dedicated on-chain bridge monitoring.

### Bridge Monitoring

The bridge on-chain infrastructure is monitored for real-time events as a way to augment the application security efforts associated with product development (i.e. threat modeling, code auditing, library and supply-chain risk and bug bounties). The real time monitoring includes both on-chain machine learning models to detect unknown threats in real time as well as empirical rule-based algorithms to capture known adversarial or error scenarios. 

The monitoring infrastructure was developed both in-house and by vendors as needed to augment our capabilities in specific analysis areas. Any adverse bridge events detected by our models and tools are evaluated, triaged and, if necessary, escalated to the proper team for further analysis. The monitoring process is integrated with our enterprise incident response process for seamless integration with internal processes.

### Multisig Security

Specific requirements are followed by any Polygon Labs employee that is a signer on a corporate multisig contract. Multisig contacts are corporately owned  and control treasury assets or smart contract deployments. They consist of Safes (previously Gnosis Safes) and other smart contract multisig implementations. Hardware wallets are hardware-based cold storage such as Trezor or Ledger devices that store private keys and enable signing multisig transactions offline. Signer multisig requirement include:

- **Hardware Wallet:** Polygon requires Cold storage from an accepted vendor dedicated for company official use only and secured by a PIN
- **Hot Wallets:** Hot wallets are not allowed for use on Polygon multisigs
- **Corporate Workstation:** Signing must be performed from a company system  managed by  our enterprise mobile device management (MDM) platform  complete with anti-virus (AV) and endpoint detection and device (EDR).
- **Clean Key:** All signers are required to create a clean key that has never been exposed to a hot wallet
- **Mnemonic Storage:** Polygon mandates safe storage of mnemonic passphrases and provides guidance to its employees
- **Secure Communication:** All multisig signing events are coordinated using Polygon’s accepted communication protocols for multisigs.

**All corporate multisigs are monitored 24/7 by the Polygon security team.**

## Secure Software Development

Polygon engineering teams are trained and instructed to use secure coding guidelines, which follow industry standards for secure development such as OWASP. These  provide guidelines, tools, and resources to help our developers identify and mitigate security risks.

Starting with activities such as threat modeling and risk assessments, Polygon Labs can systematically identify and prioritize potential security threats and vulnerabilities in our systems and applications. These proactive measures enable us to allocate resources effectively, focusing on areas that pose the greatest risks.

Continuous integration and continuous deployment (CI/CD) activities are enforced in all code repositories, which implement automated security testing and scanning tools into the CI/CD pipeline to detect vulnerabilities early in the development process.

Following development and testing phases, all applications expected to go into production are further tested via internal or external assessments such as penetration testing, security audits  and bug bounty programs. These efforts help validate the effectiveness of our security controls, detect weaknesses, and address them before they can be exploited by malicious actors.

## Vulnerability Management

Our Vulnerability management lifecycle takes the output of  secure development lifecycle activities, together with results from vulnerability tools, such as security scanners  and ensures effective reduction of risk they present. 

Vulnerabilities are sent to a centralized issue and findings tracker ensuring that all identified vulnerabilities are effectively managed. This system enables appropriate validation, triage, assessment, and remediation/mitigation of vulnerabilities by assigning them to relevant teams and stakeholders. Polygon Labs establishes a clear workflow and procedures to prioritize and address issues based on their severity, potential impact, and exploitability.

Polygon Labs maintains open communication channels with vendors and security researchers, enabling us to stay informed of newly discovered vulnerabilities, patches, and updates. This collaboration significantly contributes to maintaining a secure environment by ensuring that systems and applications are up-to-date and protected against known threats.

All these activities, and others, are part of our robust vulnerability management lifecycle, which effectively reduces the risks associated with security vulnerabilities, strengthens the overall security posture, and maintains the trust and confidence of our clients, partners, and employees.
Authentication & Access Control

Polygon Labs establishes standards for authentication & access control in its information security policy and information security standards documents.

To ensure the security of our corporate systems, all employees must adhere to strict password guidelines. Passwords must be a minimum of 12 characters in length and contain at least one uppercase letter, one lowercase letter, one numeral, and one special character. Passwords should be changed every 90 days and two-factor authentication is mandatory for accessing sensitive systems. Default, shared, or easily guessable passwords are strictly prohibited.

Polygon Labs performs entitlement reviews for sensitive systems on a yearly basis. Where applicable and available, systems are accessed via single sign-n (SSO).


## Security Operations

**Logging**

Polygon Labs leverages a variety of SaaS and bespoke infrastructure. Where audit logs are provided from those services, they are collected into a centralized repository and stored for a minimum of 30 days to support investigations should a security incident arise.
Logs are reviewed automatically for anomalies to feed Polygon Labs' threat detection models.

**Monitoring**

Polygon Labs relies on a variety of sources generating alerts for potential security incidents. Those sources include, but are not limited to, Google Workspace, Falcon CrowdStrike, AWS GuardDuty, GCP Security Command Center, Cloudflare, and Okta. Every system with built in anomaly or threat detection directs their findings to a centralized SIEM, Coralogix, for our security analysts to review.

Polygon Labs has security analysts distributed globally to help ensure timely triage of security alerts.

**Incident Response**

Polygon Labs established an incident response policy and process modeled after industry best practices. We designate key people to act as subject matter experts to join the incident response team as needed depending on the nature of a given cyber security incident. We also leverage third-party agencies to complement our incident response team from top tier security vendors.

The life cycle of a cyber security incident begins with detection and discovery. At Polygon Labs we leverage a variety of tools such as anti-virus, endpoint detection and response, network intrusion detection, phish screening and anomaly detection to help ensure we identify potential cyber security events early. We also provide our employees and community with mechanisms to proactively report suspicious activity including a ticketing system, instant messaging channels and a dedicated phone number for emergencies.

When an incident is identified the security operations team performs triage and draws on our roster of subject matter experts to help with investigation and analysis. If an incident is declared a true positive we move from analysis to containment, remediation and recovery. Along the way, we document the timeline of the incident and preserve evidence. Our incident response team works closely with our legal and compliance teams to help ensure we take the correct steps in handling information that may be required for legal or regulatory responses.

Polygon Labs carefully considers when, how and who to communicate with during incident response. Impacted stakeholders are sent notifications in a timely manner to ensure they can take reasonable steps to protect their information if necessary. Polygon Labs also makes every effort to work with law enforcement to the degree required by the laws of the jurisdictions that we operate in, which may be different depending on the nature of the cyber security incident.

In order to ensure the incident response process remains relevant, we conduct regular incident response exercises if no real security incident has occurred after a given period.

## Conclusion

In summary, our organization stands as one of the leaders in the web3 security sector. Our distinction arises from our commitment to not only implementing the best security practices but also dedicating substantial resources to this endeavor. Through tireless efforts, we have cultivated a culture of continuous improvement.

Our success is related to our dedication to measuring our performance rigorously. This steadfast focus on self-assessment empowers us to not only maintain the highest standards but to push the boundaries of excellence in web3 security.

As we stride forward, we are driven by the belief that leadership is not just a position, but a relentless pursuit. Our unceasing investments in both human and technological resources, combined with our unwavering dedication to improvement, have positioned us at the forefront of the web3 security domain. Our journey towards excellence continues through our unassailable commitment to safeguarding the web3 landscape.
