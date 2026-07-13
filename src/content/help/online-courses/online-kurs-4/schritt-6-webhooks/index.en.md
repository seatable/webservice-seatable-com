---
title: 'Step 6: Notify the outside world'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-6-notify-the-outside-world'
aliases:
    - '/help/schritt-6-webhooks'
seo:
    title: 'Step 6 of SeaTable course 4: webhooks and ntfy notifications'
    description: 'Get information out of SeaTable: inspect the payload of a native webhook, then notify your phone with ntfy by completing your extraction script.'
---

So far, everything has stayed inside SeaTable: your automations and your scripts acted on your data, and the plugin could check the result. From now on, you are going to send information out — alerting a service, a phone, another tool. The building block for that is called the webhook.

## Inbound, outbound: what are we talking about?

A webhook is an automatic phone call between two applications. When an event happens on one side, a request immediately goes out to a URL on the other side to notify it. We speak of an **outbound** webhook when it is SeaTable calling the outside world — which is our case here — and of an **inbound** webhook when it is the outside world calling SeaTable, a direction you will meet again in the step on the API.

## See what SeaTable sends

SeaTable can trigger an outbound webhook without any code: you give it a URL, and on every event you choose, it sends a message there. But a message to where? To observe it, the simplest way is to send it first to a test endpoint.

Open [webhooks.cc/go](https://webhooks.cc/go): the service assigns you a unique URL and displays, live, everything it receives. Set up a native webhook in your base pointing to that URL, trigger a change, and watch the request arrive. There you discover the **payload**: the packet of data that SeaTable sends, describing what has just happened.

![The payload of a SeaTable webhook received and displayed on a test service](images/lvl4-webhook-payload.png)

That is the very principle of webhooks: you trigger on one side, you observe on the other. Nothing to validate in the plugin this time — the round trip is yours to make, and that is precisely the lesson.

## A real notification: ntfy

A raw payload on a web page is perfect for understanding, but in the field you would rather be alerted for real. This is where ntfy comes in: a service that turns a simple request into a **notification on your phone**.

ntfy asks for no account. You pick a **topic** — a channel name that also acts as a password — you subscribe to it from the ntfy app, and any request sent to that topic notifies you right away.

{{< warning headline="A ntfy topic is both an address and a password" text="Anyone who knows your topic can send you notifications, and read yours. Choose a long name that is hard to guess, and never let any sensitive information pass through it." />}}

Now to find the right moment to fire this notification. Remember step 5: the AI extraction takes a few seconds. Rather than staring at the screen while you wait, have yourself alerted when the lines are ready — or when something has failed.

## Wiring ntfy into your script

The native webhook you just saw sends a fixed payload to a URL. A script, on the other hand, decides everything: what to send, when, and with what message. So take the script from step 5 and complete it so that it notifies at the end of its work:

```python
from seatable_api import Base, context
import json, requests

NTFY = 'https://ntfy.sh/your-secret-topic'

base = Base(context.api_token, context.server_url)
base.auth()

try:
    data = json.loads(context.current_row.get('JSON'))
    products = data.get('products', [])
    if not products:
        raise ValueError('no products extracted')
    base.update_row(context.current_table, context.current_row['_id'], {
        'PO reference': data['order'],
        'Delivery reference': data['delivery'],
    })
    lines = [{
        'Product ref': p['ref'],
        'Qty': int(p['qty']),
        'Document reference': 'DN' + data['delivery'],
    } for p in products]
    base.batch_append_rows('Line items', lines)
    requests.post(NTFY, data=f"Delivery DN{data['delivery']}: {len(lines)} lines ready to check".encode('utf-8'))
except Exception as e:
    requests.post(NTFY, data=f"Extraction failed: {e}".encode('utf-8'),
                  headers={'Priority': 'high', 'Tags': 'warning'})
```

Two things to remember. First, `requests` — the library that sends the request — is one of the tools already available in SeaTable scripts: nothing to install. Second, the `try / except`: if the AI produced usable JSON, you get a "lines ready" message; otherwise, an error notification at high priority. Your phone keeps you informed either way — and that is why a script offers more than a native webhook: it sends the right message, at the right moment, based on what actually happened.

Replace the topic with your own, drop in a new delivery note, and wait for the buzz.

## Try it yourself

Deliberately cause an error: drop in a document whose PDF is unreadable, or empty the `JSON` column before you rerun the script. You should receive the failure notification, not the success one. That is the kind of safeguard that, in production, warns you of a problem before someone discovers it out on the dock.

## Help article with further information

- [SeaTable webhooks]({{< relref "help/integrationen/webhooks/" >}})
- [Python scripts in SeaTable]({{< relref "help/skripte/python/" >}})
- [ntfy — notifications from a simple request](https://ntfy.sh/)
