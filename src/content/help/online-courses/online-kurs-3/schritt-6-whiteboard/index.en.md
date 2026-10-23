---
title: 'Step 6: Whiteboard'
date: 2026-06-18
lastmod: '2026-06-18'
categories:
    - 'online-kurs-3'
author: 'bha'
url: '/help/step-6-whiteboard'
aliases:
    - '/help/schritt-6-whiteboard'
seo:
    title: 'Step 6 in SeaTable Course 3: the whiteboard'
    description: 'Collaborate in real time on the SeaTable whiteboard in Marketing''s base — live cursors and messages — then agree on a few graphic rules to show whose is what.'
---

Not every collaboration happens in a table. Sometimes a team needs to sketch a process, map out an idea, or rough out a layout together — the kind of thinking that belongs on a shared canvas rather than in rows and columns. SeaTable has one for exactly that: the whiteboard plugin.

Unlike everything so far, the whiteboard holds none of your data — and, the catch that shapes this whole step, it keeps no record of who did what; there is no activity log for a drawing. What it does brilliantly is the other half of collaboration: working together live, in the same space, at the same time.

## The right base for the board

A whiteboard needs a base that everyone drawing on it can edit. You have just spent four steps learning not to hand that kind of access to a base full of sensitive data, and the same habit applies here: keep coordination and sketches out of your production tables, exactly as your customer master stays separate from Marketing's working copy. The board goes in a base your colleague may edit — never in `Sales CRM`.

`Campaign Hub` is that base. It is Marketing's own, every member of the `Marketing` group can edit it, and your confidential figures never reached it — the common dataset left them in `Sales CRM`. It also holds the board that belongs there: `Customers data flow`, Marketing's diagram of how customer data reaches them, and so a picture of this very base. But it still shows the old way, back when they worked from a manual copy. Now that the data arrives as a common dataset, the picture needs redrawing, and since you set up that new flow, you are the one to update it.

The whiteboard plugin is already set up in `Campaign Hub`, so there is nothing to install: open `Customers data flow` from the base's plugin area. (On a self-hosted server, the whiteboard is a separate component: if it does not open, your system administrator may first need to [install it](https://admin.seatable.com/installation/components/whiteboard/).)

A Read-Only share would not have worked here anyway: drawing on a whiteboard needs edit access, so a Read-Only colleague cannot contribute at all.

## Working on it together

Open the board and you are on a shared canvas: everyone who has it open at the same time is present on it together. Each person's cursor travels across the board in the others' windows, a laser pointer leaves a fading trail along a shape, and a short message can appear under a cursor for a moment. The traveling cursor, the fading laser trail, the brief message: this is the in-the-moment collaboration a table cannot give you. The clip below shows it with two people on the same board.

{{< zoom image="images/lvl3-whiteboard-collab.gif" alt="Two cursors on the shared whiteboard gesturing to each other, with a laser trail and a message under one cursor" >}}

## The board remembers nothing

{{< warning headline="The whiteboard records no history" text="Unlike your base, the whiteboard keeps no log of who drew what, and no way to undo by author. Step 4's activity log has no equivalent here. If it matters who added something, the board has to show it itself." />}}

Since the board keeps no record of its own, it is worth agreeing on a few graphic rules before you fill it — the way a team agrees on naming rules for its data. The starter board uses two:

- one color per department, so a glance tells you which team each element belongs to;
- no-fill rectangles around what belongs together, here one per base.

These are only a starting point: your team may settle on its own. Keep them simple, and keep to them.

## Update the board

The starter board still shows the old way: the customer list reaching Marketing through a `manual export` into `Customers list (manual)`. You spent this whole course replacing exactly that, so bring the board up to date: rename elements and change colors so that it shows how the customer data reaches Marketing now. In this simplified case, the point is to get your hands on the whiteboard's tools, so make all the changes yourself, keeping to the rules above.

That is the whole collaboration toolkit. Time to look back at everything you have learned — and put it to the test.

## Going further

Feel the live side for yourself, with Malika. Open a private (incognito) window in your browser, sign in there with her account, and open the same board — she can, because she is a member of the `Marketing` group. A private window keeps the two sessions apart, so you stay signed in as yourself in your usual window. Tile the two windows side by side, then, in your window, move your cursor across the board, run the laser pointer along a shape, or leave a short message under your cursor — and watch each one appear in her window as it happens.

Then work the other way round: change something on the board from her window, and watch it appear in yours — the way you would work on it with a real colleague, both on the board at the same time.

## Help article with further information

- [Instructions for the whiteboard plugin (tldraw)]({{< relref "help/base-editor/plugins/anleitung-zum-whiteboard-plugin-tldraw/" >}})
