---
title: 'Disabling a webhook in case of errors'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/help/deactivating-webhooks-on-errors'
aliases:
    - '/help/deaktivierung-eines-webhooks-bei-fehlern'
seo:
    title: 'Deactivating Webhooks on Errors: SeaTable Explained'
    description: 'Learn how SeaTable disables webhooks after repeated HTTP errors and how to reactivate invalid hooks for reliable automation.'

---

If a webhook is set up for a SeaTable base, SeaTable sends a _POST request_ to the target URL whenever a change is made. Normally, the receiving system returns a status message in the form of a [three-character status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), which SeaTable then processes and disables the webhook if necessary.

## The most common HTTP status codes

There is a whole range of status codes, but it is enough to know the most common feedbacks:

- **200** - Successful
- **400** - Bad request
- **403** - Forbidden
- **500 - 511** - Server errors

By far the most important status code is 200, which indicates that the request has been received and successfully processed. SeaTable treats all status codes from 200 to 299 as success.

## SeaTable disables webhooks on errors

When SeaTable sends a webhook, SeaTable expects a response in the form of such an HTTP status code. In case of errors, the webhook is set to _invalid_ status and execution is interrupted. When this happens depends on the type of error:

| Error                          | Examples                                                                              | Deactivation                   |
| ------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------ |
| **Faulty or missing response** | Status code outside 200 to 299, no response within 30 seconds                         | after five errors in a row     |
| **Delivery not possible**      | Name cannot be resolved, connection refused, certificate error, non-public target URL | immediately on the first error |

Redirects are not followed: a status code such as 301 or 302 counts as an error. A successful delivery resets the error counter.

![Invalid webhook](images/invalid-webhook.png)

{{< warning headline="Public target URLs only since version 7.0.10" text="Since version 7.0.10 of SeaTable, the target URL must point to a public address. Webhooks to internal addresses are not delivered and are deactivated immediately." />}}

## Failed deliveries are not retried

SeaTable does not send a webhook again if delivery fails. Changes made while a webhook is deactivated are not delivered later either. If your system needs complete data, you should therefore [sync the data regularly]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

## Reactivate an inactive webhook

An invalid webhook can be reactivated at any time. Switch to editing the invalid webhook by clicking {{< seatable-icon icon="dtable-icon-rename" color="grey" >}} and save the webhook again without making any changes. This will make the webhook active again immediately.

To avoid deactivation again, the receiving system should process the webhooks reliably and return the status code 200 within 30 seconds.
