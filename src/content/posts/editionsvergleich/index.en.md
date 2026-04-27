---
title: 'SeaTable Developer and Enterprise Edition Compared'
description: 'SeaTable is available in two different editions. While the Enterprise edition offers the full range of functions and is therefore used for SeaTable Cloud and dedicated systems, the Developer edition can be used free of charge and is ideal for developers as a flexible database.'
color: '#069214'
categories:
    - 'product-features'
lastmod: '2025-07-22'
url: '/compare-editions'
aliases:
    - /editionsvergleich
seo:
    title: 'SeaTable Developer vs Enterprise Edition Comparison'
    description: 'SeaTable offers two self-hosted No-Code editions: Enterprise and Developer. Discover features and use cases for each platform edition.'
---

SeaTable Server is SeaTable for your own server. By installing SeaTable in your own infrastructure, you have full control over where your data is and who accesses it. SeaTable is also recommended for use cases where you do not want to take your data off-site. You can also operate SeaTable Server exclusively in the local network without access via the Internet.

## SeaTable Server is available in two different editions

### SeaTable Enterprise Edition

The SeaTable Server Enterprise Edition is the perfect [no-code]({{< relref "posts/20250307-low-code" >}}) solution for teams and organisations of all sizes that want full functionality and data control. Only the Enterprise Edition offers the possibility to use external authentication via LDAP or SAML. The extended release permissions and automations are also only available in this edition.  
You can get a SeaTable Enterprise licence for up to three users at any time. You will find the corresponding registration form [under this link]({{< relref "pages/product/seatable-server" >}}). The installation is carried out according to the [administration manual](https://admin.seatable.com) using Docker.

### SeaTable Developer Edition

The SeaTable Server Developer Edition is primarily aimed at developers who want to use SeaTable as a flexible database and who may not use the frontend at all. Here, the Developer Edition scores with the powerful [SeaTable API](https://api.seatable.com/), the apps for the various automation platforms and the full support of all column types. The Developer Edition can be used free of charge. You can find the installation instructions [here](https://admin.seatable.com).

## Differences in the comparison

|                                 | Developer Edition                                                                                | Enterprise Edition                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Platform and environment        |                                                                                                  |                                                                                                  |
| Server operating system         | Linux                                                                                            | Linux                                                                                            |
| Installation method             | Docker                                                                                           | Docker                                                                                           |
| Docker Images                   | [Docker Hub](https://hub.docker.com/r/seatable/seatable-developer)                               | [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise)                               |
| Licence                         |                                                                                                  |                                                                                                  |
| Licence type                    | [hybrid (open source and proprietary)](https://admin.seatable.com/introduction/requirements/#license)                 | [proprietary]({{< relref "pages/legal/terms-of-service" >}})                                     |
| Licence price model             | Free of charge                                                                                   | User-based                                                                                       |
| Limits                          |                                                                                                  |                                                                                                  |
| Unlimited bases                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Unlimited tables                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Unlimited rows                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(but no archive backend)**       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Unlimited memory                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Unlimited users                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} **(licence required)**             |
| Versioning (snapshots)          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Data acquisition and processing |                                                                                                  |                                                                                                  |
| 24 column types                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Views                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Private views                   |                                                                                                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Filter                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Grouping                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Sorting                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Conditional formatting          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Forms                           | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Common datasets                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Data processing                 | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Statistics                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Import from CSV and XLSX        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Export to CSV and XLSX          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Notifications                   | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Automations                     | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Archive function                | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| JavaScript support              | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Python support                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(separate installation required)_ | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(separate installation required)_ |
| Collaboration                   |                                                                                                  |                                                                                                  |
| Real-time collaboration         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| External links                  | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Invitation links                | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Base sharing                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| View sharing                    | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Custom sharing permissions      | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Table permissions               | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Column permissions              | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Row locking                     | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Plugins and extensions          |                                                                                                  |                                                                                                  |
| Calendar                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Timeline                        | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Gallery                         | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Kanban                          | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Maps                            | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Page design                     | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| Advanced statistics             | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| SQL query                       | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}}                                    |
| ONLYOFFICE integration          | {{< icon "circle-xmark" >}}                                                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} _(separate installation required)_ |

---

|                                               | Developer Edition                                             | Enterprise Edition                                            |
| --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| API and integration options                   |                                                               |                                                               |
| REST API                                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zapier                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Integromat (Make)                             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| n8n                                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Locoia                                        | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Branding and customising                      |                                                               |                                                               |
| Custom templates                              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Custom URL                                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Custom logo                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Logo in web form                              | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Cover picture in web form                     | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Hide "Powered by"                             | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| User administration and permission management |                                                               |                                                               |
| Local user database                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| 2-factor authentication                       | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Authentication via AD/LDAP                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single sign-on via SAML                       | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| User roles                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Backend and scalability                       |                                                               |                                                               |
| S3 support                                    | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Cluster support                               | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Differences in Versions

Both the **SeaTable Enterprise Edition** and the **Developer Edition** can be conveniently downloaded from Docker Hub:

- https://hub.docker.com/r/seatable/seatable-enterprise
- https://hub.docker.com/r/seatable/seatable-developer

**The main difference between the editions lies in their versioning:**

The Developer Edition provides only a single base version, such as **5.3.0**, which is based on the initial release of the corresponding Enterprise Edition. In contrast, the Enterprise Edition is continuously developed and maintained. This means the latest version, e.g., **5.3.12**, is always available on Docker Hub.

Issues identified in the Developer Edition are only addressed with the next major release (e.g., from 5.3.x to 5.4.0).

## Differences in Testing and Support

The **SeaTable Enterprise Edition** undergoes thorough testing to ensure it is as stable and error-free as possible. In contrast, **systematic testing is not performed** for the **Developer Edition**.

**Paid support** is only available for the Enterprise Edition; **no official support** is provided for the Developer Edition.

If you have questions about the Developer Edition, we recommend using the [SeaTable Community Forum](https://forum.seatable.com). However, please note that most discussions there relate to the Enterprise Edition, as it is more widely used and officially supported.
