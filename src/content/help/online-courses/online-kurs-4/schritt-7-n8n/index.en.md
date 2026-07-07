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
    description: 'Chain SeaTable and Seafile together with n8n: automatically archive every delivery note and pull its link back into the base. A step to follow as a demo or replay yourself.'
---

A webhook sends a message; a script sends a custom one. But when you need to **chain several services together** — pick up a file here, drop it there, grab a link to it, write that back somewhere else — it pays to bring out a dedicated tool: an orchestrator. Ours is called n8n.

This step is a demonstration: you can simply follow along to see how these pieces fit together. If you want to replay it yourself, an n8n account and a Seafile account are all you need, and we provide the ready-made workflow.

## A workflow orchestrator

This kind of tool has a name: a **workflow orchestrator**. The principle is always the same — you connect applications together as a sequence of actions, without writing any code: you configure each step, a node, and the tool passes the data from one to the next. Several solutions share this space and feel very similar in use; you may already have come across *Zapier* or *Make*, which offer comparable services.

We put n8n forward for two specific reasons. First, it is **open source** and you can host it yourself: your data does not necessarily pass through a third-party service. Second, and most importantly, it is SeaTable that **develops and maintains** the official n8n node — you stay within an ecosystem the vendor controls and documents, rather than being at the mercy of a connector built by someone else. The other tools can talk to SeaTable too, most often through its API; but with n8n, you are on ground you master from end to end.

## The scenario: archive the delivery note

Your delivery notes are valuable: in case of a dispute, you need to be able to lay your hands on the original. Rather than leaving them to sleep in the base, let's archive them in a dedicated storage space — **Seafile**.

Seafile is from the same family as SeaTable: the same interfaces, the API token in the same place. You won't feel out of place, and it is a consistent choice — here again, we stay within what we master. A free trial, with no credit card, is more than enough for this step.

## The workflow, step by step

Here is the workflow, as it appears in n8n:

{{< image-hotspots image="images/lvl4-n8n-workflow.png" alt="The n8n workflow: from the SeaTable trigger through to writing the Seafile link into the base" >}}
[
  {"x":1,"y":2,"w":9,"h":45,"img":"images/lvl4-n8n-node-trigger.png","label":"Trigger: a new document with a file"},
  {"x":16,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-geturl.png","label":"Get the file's address in SeaTable"},
  {"x":32,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-download.png","label":"Download the file"},
  {"x":49,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-upload.png","label":"Upload the file to Seafile"},
  {"x":65,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-getlink.png","label":"Ask Seafile for a link"},
  {"x":81,"y":2,"w":10,"h":45,"img":"images/lvl4-n8n-node-update.png","label":"Write the link into the document's Backup URL"}
]
{{< /image-hotspots >}}

Click a node to open its configuration in detail.

It forms a full round trip between the two services:

1. **The trigger** watches the `Documents` table: as soon as a document with a file appears, the workflow starts.
2. n8n **retrieves the file's address** in SeaTable, then **downloads** it.
3. It **uploads it to Seafile**, into an archive folder (`/Delivery notes/2026/`).
4. It **asks Seafile for a link** to the file thus archived.
5. It **writes that link back** into the document's `Backup URL` column, on the SeaTable side.

In short: the file leaves SeaTable, is filed away in Seafile, and its archive address comes back to settle in the base. The strength of n8n is not a spectacular node — it is this **composition** of simple gestures between two tools.

## Replay it yourself

If you want to see it truly run, there's no need to rebuild it node by node: import it ready-made.

<!-- TODO: check that the file is actually served at this URL after build. -->
[Download the n8n workflow](/n8n/lvl4-seafile-archive.json)

In your n8n, create a new workflow and import this file. All that's left is to install the community node `n8n-nodes-seafile`, then fill in your own credentials — your SeaTable and Seafile accounts, and the ID of your Seafile library in place of the `YOUR_SEAFILE_LIBRARY` value. Then run the workflow, and drop a delivery note into your base.

{{< warning headline="A backup is not a showcase" text="The link the workflow saves points to a private archive, not to a page meant to be shared. This is intentional: backing up a document and presenting it to the public are two distinct needs. Here, the goal is to keep the original in a safe place and to keep a trace of it in the base, nothing more." />}}

## Try it yourself

Head to your Seafile library after processing a note: the PDF is there, filed away in its archive folder. Then come back to the base and open the document: its `Backup URL` column now holds the link that leads to it. You have just made two applications talk to each other without writing a single line of code — that is the whole point of an orchestrator.

## Help article with further information

- [SeaTable's n8n integration]({{< relref "help/integrationen/n8n/" >}})
- [n8n — workflow automation](https://n8n.io/)
- [Seafile — file storage](https://www.seafile.com/en/home/)
