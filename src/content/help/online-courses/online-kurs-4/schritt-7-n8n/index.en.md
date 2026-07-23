---
title: 'Step 7: Orchestrate with n8n'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-7-orchestrate-with-n8n'
aliases:
    - '/help/schritt-7-n8n'
seo:
    title: 'Step 7 of SeaTable course 4: orchestrate a workflow with n8n'
    description: 'Chain SeaTable and Google Drive together with n8n: automatically archive every delivery note and pull its link back into the base. A step to follow as a demo or replay yourself.'
---

A webhook sends a message; a script sends a custom one. But when you need to **chain several services together** — pick up a file here, drop it there, grab a link to it, write that back somewhere else — it pays to bring out a dedicated tool: an orchestrator. Ours is called n8n.

This step is a demonstration: you can simply follow along to see how these pieces fit together. If you want to replay it yourself, an n8n account and a Google account are all you need, and we provide the ready-made workflow.

## A workflow orchestrator

This kind of tool has a name: a **workflow orchestrator**. The principle is always the same — you connect applications together as a sequence of actions, without writing any code: you configure each step, a node, and the tool passes the data from one to the next. Several solutions share this space and feel very similar in use; you may already have come across *Zapier* or *Make*, which offer comparable services.

We put n8n forward for two specific reasons. First, it is **open source** and you can host it yourself: your data does not necessarily pass through a third-party service. Second, and most importantly, it is SeaTable that **develops and maintains** the official n8n node — you stay within an ecosystem the vendor controls and documents, rather than being at the mercy of a connector built by someone else. The other tools can talk to SeaTable too, most often through its API; but with n8n, you are on ground you master from end to end.

## The scenario: archive the delivery note

Your delivery notes are valuable: in case of a dispute, you need to be able to lay your hands on the original. Rather than leaving them to sleep in the base, let's archive them in a dedicated storage space — **Google Drive**.

Google Drive is a place almost everyone already has, and n8n talks to it through a **built-in node** that the tool maintains itself: the connection is solid and there is nothing extra to install. It is a fitting partner for this step — a well-known destination, reached over a channel we can rely on.

One honest caveat: connecting Google is not a two-click affair. You have to create a project in the Google Cloud console, switch on the Drive API, and set up an OAuth consent screen before n8n can act on your behalf. It can feel like a lot for a single backup workflow — but it is worth it.

{{< warning headline="Why the setup is worth it" text="First, this is the price of a properly secured service: instead of handing over a permanent password, you grant scoped, revocable access that you can withdraw at any time. Second, it is an investment you make only once — the very same connection then opens the door to Google's other services (Sheets, Gmail, Calendar, and more), simply by enabling the matching API. The effort pays off well beyond this step." />}}

## The workflow, step by step

Here is the workflow, as it appears in n8n:

{{< n8n-demo src="/n8n/lvl4-gdrive-archive.json" >}}

Click a node to open its configuration in detail.

It forms a full round trip between the two services:

1. **The trigger** watches the `Documents` table: as soon as a document with a file appears, the workflow starts.
2. n8n **retrieves the file's address** in SeaTable, then **downloads** it.
3. It **uploads it to Google Drive**, into an archive folder (`Delivery Notes 2026`) — and Google hands back a shareable link to the stored file.
4. It **writes that link back** into the document's `Backup URL` column, on the SeaTable side.

Want to see what actually travels along those wires? Step through the run below — each click advances one node and shows the data it hands on: watch the SeaTable row become a download link, then a file on Drive, then the link that lands back in the base.

{{< lvl4-n8n-simulator src="/n8n/lvl4-gdrive-archive.json" >}}

In short: the file leaves SeaTable, is filed away in Google Drive, and its archive address comes back to settle in the base. The strength of n8n is not a spectacular node — it is this **composition** of simple gestures between two tools.

## Replay it yourself

If you want to see it truly run, there's no need to rebuild it node by node: import it ready-made.

[Download the n8n workflow](/n8n/lvl4-gdrive-archive.json)

In your n8n, create a new workflow and import this file. Google Drive is a built-in node, so there is nothing extra to install — you simply connect two accounts, your SeaTable and your Google account (the OAuth step from earlier), and choose the destination folder in place of the `REPLACE_WITH_YOUR_FOLDER_ID` value. Then run the workflow, and drop a delivery note into your base.

{{< warning headline="A backup is not a showcase" text="The link the workflow saves points to a private archive, not to a page meant to be shared. This is intentional: backing up a document and presenting it to the public are two distinct needs. Here, the goal is to keep the original in a safe place and to keep a trace of it in the base, nothing more." />}}

## Try it yourself

Head to your Google Drive after processing a note: the document is there, filed away in its archive folder. Then come back to the base and open the document: its `Backup URL` column now holds the link that leads to it. You have just made two applications talk to each other without writing a single line of code — that is the whole point of an orchestrator.

## Help article with further information

- [SeaTable's n8n integration]({{< relref "help/integrationen/n8n/" >}})
- [n8n — workflow automation](https://n8n.io/)
- [Google Drive](https://www.google.com/drive/)
