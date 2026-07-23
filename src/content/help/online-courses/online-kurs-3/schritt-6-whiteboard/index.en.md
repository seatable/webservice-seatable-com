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
    description: 'Collaborate in real time on the SeaTable whiteboard in a base of its own — live cursors and messages — then agree a convention to track who did what.'
---

Not every collaboration happens in a table. Sometimes a team needs to sketch a process, map out an idea, or rough out a layout together — the kind of thinking that belongs on a shared canvas rather than in rows and columns. SeaTable has one for exactly that: the whiteboard plugin.

Unlike everything so far, the whiteboard holds none of your data — and, the catch that shapes this whole step, it keeps no record of who did what; there is no activity log for a drawing. What it does brilliantly is the other half of collaboration: working together live, in the same space, at the same time.

## A board of its own

A whiteboard needs a base that everyone drawing on it can edit. You have just spent four steps learning not to hand that kind of access to a base full of sensitive data, and the same habit applies here: keep coordination and sketches out of your production tables, exactly as your customer master stays separate from Marketing's working copy. So in our use case where you want to use it with a colleague from another department, the whiteboard better fits a base not containing any sensitive data.

Marketing keeps a board explaining how the customer data reaches them — but it still shows the old way, back when they worked from a manual copy. Now that the data arrives as a common dataset, the picture needs redrawing, and since you set up that new flow, you will update it together. In Malika's window 🕶, import the following base into the `Marketing` group — you are both members, so you will both be able to draw on it:

[SeaTable Course 3 - Marketing Whiteboard.dtable](/SeaTable-Course-3-Marketing-Whiteboard.dtable)

The whiteboard plugin comes already set up inside it, with a starter diagram already on it — so there is nothing to install; just open it from the base's plugin area.

A Read-Only share would not work here: drawing on a whiteboard needs edit access, so a Read-Only colleague cannot contribute at all. That is one more reason it belongs in a base you can both edit, never in `Sales CRM`.

## Working on it together

With the board open in both windows, you are on one shared canvas — and the two of you are present on it at the same time. That live side is easiest to feel if you tile the windows side by side: in your window 🌐, move your cursor across the board, run the laser pointer along a shape, or leave a short message under your cursor — then glance at Malika's window 🕶 and watch each one appear there as it happens. The travelling cursor, the fading laser trail, the brief message: this is the in-the-moment collaboration a table cannot give you.

The one thing you cannot quite do alone is the back-and-forth — acting and watching the other at the very same instant. With a real colleague you each simply work in your own window; on your own, the clip below shows the duet.

{{< zoom image="images/lvl3-whiteboard-collab.gif" alt="Two cursors on the shared whiteboard gesturing to each other, with a laser trail and a message under one cursor" >}}

## The board remembers nothing

{{< warning headline="The whiteboard records no history" text="Unlike your base, the whiteboard keeps no log of who drew what, and no way to undo by author. Step 4's activity log has no equivalent here. If it matters who added something, or when, you have to put that on the board yourselves." />}}

So before you fill it, agree on a simple convention — the way a team agrees on naming rules for its data. One lightweight scheme works well:

- one colour per person or department, used for your own additions — since the board keeps no log, the colours are how you tell afterwards who did what;
- draw data and structure as rectangles, and represent people as notes — a sticky note names who, with a date or a done-marker if useful;
- group what belongs together inside a no-fill rectangle, so a glance shows the shape of things.

This is only a starting point — your team may settle on its own. The point is that the board carries its own "who and when", because SeaTable will not.

## Update it together

The starter board still shows the old way: the customer list reaching Marketing through a `manual export` into `Customer list (manual)`. You spent this whole course replacing exactly that, so bring the board up to date — together, live, each in your department's colour. The change is deliberately small; the point is doing it side by side, not the drawing.

| Window | What to change |
|---|---|
| 🌐 You (Commercial) | Rename the arrow to `common dataset` and repoint it to `Customers (live)`, then add a blue note for Commercial by the source — the new path is yours. |
| 🕶 Malika (Marketing) | Mark `Customer list (manual)` as no longer used, and add a green note for Marketing (Malika) on that side. |

A minute's work between the two of you — and because you each drew in your own colour, the finished board shows at a glance who changed what, even though SeaTable kept no record of it.

That is the whole collaboration toolkit. Time to look back at everything you have learned — and put it to the test.

## Help article with further information

- [Instructions for the whiteboard plugin (tldraw)]({{< relref "help/base-editor/plugins/anleitung-zum-whiteboard-plugin-tldraw/" >}})
