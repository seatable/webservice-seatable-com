---
title: 'Segurança na SeaTable Cloud'
description: ''
seo:
    title: 'Segurança dos seus dados na SeaTable Cloud'
    description: 'Saiba como a SeaTable Cloud mantém seus dados protegidos, privados e sempre acessíveis com as melhores práticas de segurança.'
date: 2024-10-28
type: 'legal'
url: '/pt/seguranca'
---

{{< alert icon="empty" cardColor="gradient" textColor="#fff" >}}

Esta página está disponível apenas em inglês e alemão. A versão em inglês é uma tradução de conveniência, não vinculativa.
O **[original alemão]({{< relref path="pages/legal/security" lang="de" >}})** é juridicamente vinculativo.

{{< /alert >}}

When you manage your data in SeaTable, you trust us and expect us to store it safely, privately, and keep it available to you at all times. Rightfully so! We take this responsibility very seriously.

Five principles guide our decisions in terms of architecture and operation of SeaTable Cloud:

- Partnerships with first-class (European) partners
- Use of the best available techniques and best practices
- Continuous staff training
- Security through redundancy
- Open, active error culture

## Data Storage

We rely on the infrastructure of [Akenes SA (Exoscale)](https://www.exoscale.com/) for the operation of SeaTable Cloud. Exoscale was founded in 2011 and is headquartered in Lausanne, Switzerland. Since 2017, it is a subsidiary of A1 Digital International GmbH and, as such, a part of the public-stock company [A1 Telekom Austria Group](https://a1.com/de//).

Exoscale operates [multiple data centers in Germany, Austria, Switzerland, and Bulgaria](https://www.exoscale.com/datacenters/) (as of October 2024). All data centers are [ISO 9001 and 27001 certified](https://www.exoscale.com/compliance) and have N+1 redundancy for all core components such as power supply, cooling, fire detection and suppression. Exoscale’s data centers meet or exceed the Tier III requirements of the [Uptime Institute](https://uptimeinstitute.com/tiers).

All user data in SeaTable Cloud, except subscription and payment data, is stored and processed in the DE-FRA-1 and DE-MUC-1 data centers in Frankfurt and Munich, Germany. Your user data never leaves Europe.

All user data is backed up daily. The backed up data allows restoration of operation with a few hours in the event of a disaster.

## Data Access

### Physical connection

Exoscale’s data centers are connected via multiple 10Gbits links to various Tier 1 and Tier 2 transit providers. Additionally, there are several peering connections with major local data center service providers. As a result, SeaTable has resilient connectivity and offers best-in-class access speeds.

Exoscale’s data centers are interconnected via a 100Gbits backbone.

### Server administration

The administration and maintenance of the infrastructure is carried out by the employees of SeaTable GmbH and European partner companies. The partner companies and their authorized personnel have administrative access to the infrastructure of SeaTable Cloud in order to carry out their contractual obligations. We have concluded agreements with all partner companies regarding data processing and confidentiality. Employees are individually bound to comply with data privacy rules.

Apart from the authorized employees at SeaTable GmbH and our partner companies, no other party has unsupervised, administrative access to the infrastructure of SeaTable Cloud. In exceptional circumstances (e.g., for bug fixes), it may be necessary or sensible for employees of Seafile Ltd. to be given access to SeaTable Cloud’s infrastructure. Seafile Ltd. is the developer of the SeaTable software. In any such case, access is supervised by an employee of SeaTable GmbH or a partner company.

### Access control

We use state of the art technology and best practices to control access to SeaTable Cloud’s infrastructure:

- Firewalls
- Public key authentication
- IP address whitelist
- Password policy
- 2-factor authentication
- Captcha
- API throtteling
- Intrusion detection system (e.g., monitoring of IP addresses)
- Logging of administrative logins

## Data Transmissions

To ensure secure transmission of your data over the Internet, all user data, including subscription and payment data, is encrypted using up-to-date cryptographic methods. This applies to data transfer between you and the application servers, between components in a data center, and between the two data centers used.

For the HTTPS connection between your browser and SeaTable, we only allow the more recent TLS protocols 1.2 and 1.3 and use only current algorithms for encryption, authentication, and key exchange. SeaTable Cloud’s [SSL configuration gets an A+ rating](https://www.ssllabs.com/ssltest/) by IT security firm Qualys (last update October 2024).

## Data Availability

All central components of SeaTable Cloud are monitored 24/7 by our support team. Failures or malfunctions can thus be detected and eliminated within a short time – most often before you even notice a service disruption or limitation.

We regularly update all software components of SeaTable Cloud. The updates are carried out in maintenance windows, which are announced in advance. Before an update, especially of SeaTable itself, extensive automated tests (e.g., API) and manual tests are performed in a separate test system to ensure security and stability.

All user data is regularly backed up in a remote data center (see Data Storage). In the event of a disaster, this allows the disaster recovery within a short time. Data loss is limited to the changes made since the last backup.

SeaTable offers various recovery functions to undo unintentional data deletion and modification by users. Deleted Bases are kept in the recycle bin for 30 days before they are permanently deleted. Earlier versions of bases can be restored using the integrated snapshot function. Individual changes can be tracked and undone via the log. The duration for which snapshots and the log are retained depends on the [subscription]({{< relref "pages/prices" >}}), but is at least 1 month. More information about SeaTable’s features for restoring previous data states can be found in the SeaTable Manual in [Versioning & Snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}).

You can export your data stored in SeaTable at any time. SeaTable offers three export options:

- Export via the web interface to a CSV or XLSX file
- Export via the web interface to a DTABLE file
- Export via the API

More information about the DTABLE file format can be found in the [SeaTable Admin Manual]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}). The SeaTable API is fully documented in the [SeaTable API Reference](https://api.seatable.com).

## Audit and Certification

The data centers of our infrastructure partner Exoscale are ISO 9001 and 27001 certified in addition to some, partly stricter certifications.

In September 2024, the IT security firm SRC Security Research & Consulting GmbH, based in Bonn, Germany, performed a penetration test of SeaTable Server. You can download the management report (in German) [here](/Seatable-2401_Management_Summary_v1.2.pdf). We provide the full report (in German) upon request. Please contact security@seatable.com.

There is currently no certification for SeaTable. A certification of SeaTable Server by the German Federal Office for Information Security (BSI) is planned for the second half of 2025.

## Report a Bug

If you discover or become aware of a security vulnerability, please email us at security@seatable.com. We will work with high intensity to eliminate the vulnerability.

A bug bounty program is currently under construction. It is expected to launch in 2025.

## Data Privacy

Privacy is an invaluable asset and we want to do our utmost to protect it. We therefore do not use any non-essential cookies and refrain from using any trackers.

We attach great importance to making transparent how we collect, use, and treat your data when you use our website and SeaTable Cloud. Details can be found in the [Privacy Policy]({{< relref "pages/legal/data-privacy" >}}).
