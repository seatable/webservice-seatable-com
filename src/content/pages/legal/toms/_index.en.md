---
title: 'Technical & Organizational Measures <br />pursuant to Art. 32 GDPR'
description: ''
seo:
    title: 'TOMs'
    description: '...'
date: 2025-10-16
version: '1.1.5'
type: 'legal'
url: '/technical-and-organizational-measures'
---

{{< alert icon="empty" cardColor="gradient" textColor="#fff" >}}

These technical and organizational measures are only available in English and German. The English version is an non-binding, convenience translation.
The **[German original version]({{< relref path="pages/legal/toms" lang="de" >}})** is legally binding.

{{< /alert >}}<br />

## Preamble

Taking into account the state of the art, implementation costs, nature, scope, circumstances, and purposes of processing, as well as the varying likelihood and severity of risks to the rights and freedoms of natural persons, SeaTable GmbH has implemented appropriate technical and organizational measures (TOMs) to ensure a level of protection for personal data appropriate to the risk.

This documentation contains the implemented TOMs. The presentation follows the measures explicitly named in Art. 32(1) GDPR. These apply generally or specifically to the data processing systems rented from Akenes SA (Exoscale), on which the offered online service is operated, where explicitly mentioned.

---

## 1. Pseudonymization and Encryption (Art. 32(1)(a) GDPR)

| Technical Measures             | Organizational Measures                                              |
| ------------------------------ | -------------------------------------------------------------------- |
| Encryption of database backups | Timely deletion of personal data unless other regulations prevent it |

_Note:_ Pseudonymization and encryption of the controller's data are generally not part of the services to be provided and would technically only be possible with significant functional restrictions.

---

## 2. Capabilities to Ensure Confidentiality (Art. 32(1)(b) GDPR)

### 2.1 Physical Access Control

| Technical Measures                               | Organizational Measures                |
| ------------------------------------------------ | -------------------------------------- |
| Biometric access barriers and logging of entries | Key management / list                  |
| Doors with external knobs                        | Visitors accompanied by employees      |
|                                                  | Careful selection of cleaning services |

### 2.2 Logical Access Control

| Technical Measures                    | Organizational Measures                                               |
| ------------------------------------- | --------------------------------------------------------------------- |
| Firewall in router and server         | Dedicated management of user permissions                              |
| Use of IP blockers                    | Process documentation for access deactivation upon employee departure |
| Linux operating systems on servers    | General data protection policy                                        |
| Use of VPN for remote access          |                                                                       |
| Centralized user administration       |                                                                       |
| Two-factor authentication (2FA)       |                                                                       |
| Minimum password complexity           |                                                                       |
| Current operating systems             |                                                                       |
| Antivirus software on Windows systems |                                                                       |
| Local firewall                        |                                                                       |

**Technical Measures (Exoscale) and Organizational Measures (Exoscale)**

| Technical Measures (Exoscale)                                   | Organizational Measures (Exoscale) |
| --------------------------------------------------------------- | ---------------------------------- |
| Securing web access with CAPTCHA, IP blockers, and optional 2FA | Dedicated administrators           |
| Securing API access with IP blockers and optional 2FA           |                                    |
| Remote access via SSH with certificate                          |                                    |
| SSH hardening (e.g., no root login)                             |                                    |
| Monitoring SSH access with IP blockers                          |                                    |
| Software firewall on servers                                    |                                    |
| Logging of user logins                                          |                                    |
| Regular software updates                                        |                                    |
| Encryption of backups                                           |                                    |

### 2.3 Access Control

| Technical Measures                                                       | Organizational Measures                     |
| ------------------------------------------------------------------------ | ------------------------------------------- |
| Centralized authorization management                                     | Implementation of authorization concepts    |
| Logging of access to server infrastructure                               | Minimum number of administrators            |
| Password safe with dedicated authorization management and access control | Management of user rights by administrators |

## 3. Capabilities to Ensure Integrity

_Art. 32(1)(b) GDPR_

| Technical Measures                                                      | Organizational Measures                                                         |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Separation of production and test environments                          | Authorization concept                                                           |
| Information exchange via SSL-encrypted data connections                 | Traceability of data entry, modification, and deletion via individual usernames |
| Use of SSH, VPN, and certified remote maintenance software (TeamViewer) |                                                                                 |
| Logging of access and retrievals                                        |                                                                                 |
| Manual or automated control of logs                                     |                                                                                 |

## 4. Capabilities to Ensure Availability and Resilience

_(Art. 32(1)(b) GDPR)_

| Technical Measures                                      | Organizational Measures                               |
| ------------------------------------------------------- | ----------------------------------------------------- |
| Regular system maintenance                              | Logging of system maintenance                         |
| Regular data backups                                    | Control of backup process                             |
| Firewalls                                               | Regular data restoration tests and logging of results |
| Redundant data storage                                  | Data backups at secure third locations                |
| Uninterruptible power supply                            | No sanitary connections in or above the server room   |
| Penetration tests by professional IT security companies |                                                       |

## 5. Timely Data Restoration

_Art. 32(1)(c) GDPR_

| Technical Measures       | Organizational Measures                      |
| ------------------------ | -------------------------------------------- |
| Regular data backups     | Appropriate verbal instructions to employees |
| Spare hardware available | Mobile number of admin(s) known              |
| LTE modem available      |                                              |

## 6. Procedures for Regular Testing, Assessment, and Evaluation

_Art. 32(1)(d) GDPR; Art. 25(1) GDPR_

| Technical Measures                                                                                   | Organizational Measures                                                                                   |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Centralized documentation of all data protection procedures and regulations                          | Employees trained and bound by confidentiality/data secrecy                                               |
| Regular review of access authorizations                                                              | Annual employee awareness training                                                                        |
| Regular review of data protection provisions and assessment of appropriateness of technical measures | Regular review of data protection provisions and assessment of appropriateness of organizational measures |
|                                                                                                      | Disciplinary measures in case of data protection breach                                                   |
