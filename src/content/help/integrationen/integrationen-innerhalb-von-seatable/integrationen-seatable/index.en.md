---
title: 'Overview of all integrations in and with SeaTable'
date: 2023-03-22
lastmod: '2023-07-19'
categories:
    - 'skripte-api-integrationen'
author: 'cdb'
url: '/help/seatable-integrations'
aliases:
    - '/help/integrationen-seatable'
seo:
    title: 'SeaTable Integrations: API, Webhooks & Automation at a Glance'
    description: 'Discover all SeaTable integrations: REST API, webhooks, JS/Python, email, Zapier, Make & custom plugins for efficient workflows.'
---

Integrations extend the way you can work and interact with SeaTable. For example, integrations allow you to access your data within SeaTable with other tools and software solutions, or you can design workflows that automate certain steps. Alternatively, you could develop your own apps or programs that use SeaTable as a backend.

You may have already noticed. There is no "one" SeaTable integration, but depending on the application area, other integrations are available. This article will give you an overview of the different integrations and possibilities.

## Overview of the available integrations

Currently, SeaTable offers five different integration options, which will be presented in more detail below.

- Javascript and Python
- Integrations within SeaTable
- SeaTable API
- Webhooks
- Automation platforms

## Scripts in SeaTable

SeaTable allows you to run custom JavaScript and Python scripts in a base. This allows users who have some programming experience to automate steps or recurring tasks. The scripts can be started either manually, using a button, or through automation.

## Integrations within SeaTable

In a base, SeaTable offers the possibility to enable **third-party integrations**. Currently, only the integration with an email account is available within this integration. This email integration allows sending emails from SeaTable using automations or buttons. Another option is to enable email synchronization, which makes all emails from the email account available in SeaTable.

## SeaTable API

The SeaTable API provides a universal interface through which you can interact with the data within SeaTable using any software or programming language. For example, using the SeaTable API, data captured in other software can be automatically written to SeaTable. Or you may want to build a custom front-end for some SeaTable data, then you can use the API to access the data directly without the web interface.

## Webhooks

Webhooks are set up within SeaTable for one base at a time. Once a webhook is set up, SeaTable sends a message to a URL of your choice whenever a change is made in that base. At this URL, software receives the webhooks and processes them. Depending on what change was made in the base, you can perform a corresponding follow-up activity.

A typical example of a webhook would be monitoring the payment status of an invoice or subscription. As soon as you set an invoice to the status _Paid_ in SeaTable, another software should perform a corresponding action. You could easily implement this with a webhook. Every change to the invoices in SeaTable is sent via webhook to the other software and it only reacts to the status message that is relevant for you.

Webhooks are typically used when you do not want to query the status of information on a regular basis, but when you want to be informed proactively when changes occur. For regular status queries, the SeaTable API is typically the best choice.

## Automation platforms

In everyday life, people often work not only with one software, but with many solutions at the same time. Business contacts are stored in a CRM such as Hubspot or Pipedrive, appointments and e-mails are stored in Google, and newsletters are sent with [Mailchimp](https://mailchimp.com/) or Brevo(https://www.brevo.com/). Often you want an event in one software to lead to an activity in another software. So if you send a new newsletter with Brevo, that you then automatically also send a Facebook post. Or if someone sends an appointment request on your website, that the contact data is then automatically transferred to your CRM.

Exactly in these cases, one of the many automation platforms can help you. These help you to connect two or more software solutions without programming experience and to react to certain triggers with certain actions.

Currently, the following automation platforms offer support for SeaTable:

- [Zapier](https://zapier.com/apps/seatable/integrations)
- [Make (formerly Integromat)](https://www.make.com/en/integrations/seatable)
- [n8n](https://n8n.io/integrations/seatable/)
- [Locoia](https://www.locoia.com/connector-integrations/)
- [Integrately](https://integrately.com/integrations/seatable)

## Own development

You have found SeaTable to your liking, but you are missing one or another function? You want to automate certain tasks and you want to integrate SeaTable into existing systems? With SeaTable you have all these possibilities! The ability to integrate and extend is part of the SeaTable DNA.

The plugins of SeaTable Market are based on the Realtime SDK of SeaTable. With this you can develop your own plugins with little effort. In the [developer documentation you can find all details about the SeaTable SDK](https://developer.seatable.com). The import of your own plugins is done via the Plugin Manager.

There are almost no limits to SeaTable's integration with other systems thanks to SeaTable's powerful REST API. All information about the SeaTable API can be found in [SeaTable's API documentation](https://api.seatable.com).

For both the plugins and the integration, you use well-known programming languages like JavaScript and Python. Your developers can get started right away.
