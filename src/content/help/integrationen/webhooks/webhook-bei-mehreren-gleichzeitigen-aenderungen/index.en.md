---
title: 'Webhook for several simultaneous changes'
date: 2024-02-13
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/help/webhook-multiple-simultaneous-changes'
aliases:
    - '/help/webhook-bei-mehreren-gleichzeitigen-aenderungen'
seo:
    title: 'Webhooks on Multiple Simultaneous Changes Explained'
    description: 'Learn how SeaTable bundles webhooks for multiple row changes, what the row_count parameter means and how to query all changed rows.'

---

SeaTable usually sends one webhook for every change to a row. However, if one operation changes several rows at the same time, only one webhook is generated, with the additional parameter _row\_count_. This also applies to the API: one API call creates one webhook, regardless of whether it changes one or several rows.

In the web editor, this happens for example when you copy a value to the clipboard with {{< key "CTRL" >}}+{{< key "C" >}} and then paste it into several other rows with {{< key "CTRL" >}}+{{< key "V" >}}. This process generates only one webhook. The following graphic shows the corresponding webhook.

![Multiple simultaneous changes via webhook.](images/webhook_multiple_changes.jpg)

## What the webhook contains

The parameter _row\_count_ states the number of affected rows. The other details such as _row\_id_, _row\_name_ and _row\_data_ refer to a single row only, usually the first row of the operation. _op\_type_ also stays in the singular, that is _insert\_row_, _modify\_row_ or _delete\_row_.

There is currently no option to create a separate webhook for each row. The webhook does not contain a list of all affected rows either.

## Querying changed rows after a webhook

{{< warning headline="Webhooks are not meant for synchronization" text="If you want to synchronize data with another system, the webhook should only be the trigger for the sync. It does not contain all changes, and its delivery is not guaranteed." />}}

After the webhook, query the changed rows via the [SQL interface](https://developer.seatable.com/sql/select/):

```sql
SELECT * FROM Table1 WHERE _mtime >= '2026-11-05T18:30:00+01:00' ORDER BY _mtime, _id LIMIT 1000 OFFSET 0
```

Please keep the following points in mind:

- **Compare with `>=`:** The _\_mtime_ column usually has a precision of one second only. With `>`, you would miss changes made in the same second as your last sync. Since `>=` returns some rows again, your system must be able to handle duplicates.
- **Specify the time zone:** A time without a time zone is not interpreted as UTC. Therefore, always specify the offset, e.g. `+01:00`.
- **Fetch results page by page:** Without `LIMIT`, an SQL query returns at most 100 rows, and the maximum per query is 10,000 rows. Increase `OFFSET` until a query returns fewer rows than the specified `LIMIT`.
- **Deleted rows and links:** Deleted rows do not appear in this query, and adding a link does not change _\_mtime_. Therefore, compare the row IDs and link columns in both systems from time to time.

## Also sync on a regular basis

Webhooks do not guarantee complete delivery: failed deliveries are not retried, a webhook can be [deactivated after errors]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}), and in individual cases it may not be sent at all. Therefore, also run the sync on a fixed schedule and regularly check that the webhook is still active.
