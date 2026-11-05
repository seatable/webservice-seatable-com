---
title: 'The secret key of a webhook'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/help/webhook-secret-key-seatable'
aliases:
  - '/help/der-geheime-schluessel-eines-webhooks'
seo:
    title: 'Webhook security: secret key and signature in SeaTable'
    description: 'Learn how a secret key secures your SeaTable webhooks: validate the signature, verify event origins and block unauthorized access using shared secrets.'

---

If the destination of a webhook is publicly reachable, it is necessary to ensure that incoming requests come from the desired source system. A secret key can be used to ensure the origin of a webhook.

## The idea of a secret key

To create a new webhook, simply specify any URL. The secret key may also remain empty. However, if your target URL is publicly available, you should set a secret key and validate this value when processing the webhooks. Otherwise, anyone can send you appropriate requests to this webhook URL, which will be processed by you. Without the secret key, the target system has no reliable way to know if the event really comes from SeaTable.

If you specify a secret key, the webhook has an additional _X-SeaTable-Signature-Header_, which can be used to ensure the origin of the webhook. As long as someone else doesn't know the secret key, they won't be able to send you events via webhook and get the matching _X-SeaTable-Signature-Header_ to generate.

For example, if a secret key is set, a webhook request looks like this:

```
-- HEADER --
Content-Type: application/json
Content-Length: 625
X-Seatable-Signature: sha256=598b55485e7875def064746867ff220e79d7c75512fdb931a39e313af5abfe60
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: python-requests/2.28.1
Host: example.com

-- CONTENT --
{
  event:update
  data: {
    dtable_uuid: 6c17f178ee724c109c68ecee364027fc
    row_id: Y_aYcE6wTo-IzGWb-oDmaQ
    op_user: 92d8f9b243f8437db0131c2536398403@auth.local
    op_type: insert_row
    op_time: 1677595743.088
    table_id: 0000
    table_name: Table1
    row_name: ""
    row_data: []
  }
}

```

## Calculating the signature

The secret key is a [shared secret](https://en.wikipedia.org/wiki/Shared_secret) between SeaTable and the receiving system. SeaTable uses the secret key to calculate a hash value from the event, the signature. The receiving system uses the same key to calculate the hash value from the content it received and compares it with the signature. If the two values do not match, the webhook should not be processed.

## Validation of the signature

In every programming language there should be corresponding functions to be able to validate such a signature accordingly. How this check would look like in PHP, you will learn in [this article]({{< relref "help/integrationen/webhooks/verarbeitung-eines-webhooks-mit-hilfe-von-php" >}}).

For Python, a check might look like this:

```
import hmac
from flask import Flask, request

app = Flask(__name__)

@app.route('/receive-seatable-webhook', methods=['POST'])
def receive_seatable_webhook():
    secret = 'secret'
    seatable_signature = request.headers.get('X-Seatable-Signature', '').replace('sha256=', '')

    signature = hmac.new(
        secret.encode('utf-8'), request.data, digestmod='sha256').hexdigest()

    signature_compare = hmac.compare_digest(signature, seatable_signature)

    if signature_compare:
        # do something
        pass

    return {'success': signature_compare}

```
