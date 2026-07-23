---
title: 'Step 2: Sharing and permissions'
date: 2026-06-18
lastmod: '2026-06-18'
categories:
    - 'online-kurs-3'
author: 'bha'
url: '/help/step-2-sharing-and-permissions'
aliases:
    - '/help/schritt-2-teilen-und-berechtigungen'
seo:
    title: 'Step 2 in SeaTable Course 3: sharing and permissions'
    description: 'Invite a colleague to your base and choose the right permission level — Read only, Read-Write, or Custom per table and view.'
---

You have a base full of valuable data. Collaboration begins the moment someone else needs to work with it. In this step you bring in your colleague Malika from Marketing and decide, deliberately, how much of your base she is allowed to see and change.

This is where your two windows come into play. You act as the owner of the base in your main window 🌐, and you check the result through Malika's eyes in her private window 🕶. From here on, every instruction is tagged with the window it belongs to.

## Team membership is not the same as base access

In the introduction you added Malika to your team. It is worth being clear about what that did and did not do. Being a team member means Malika exists in your team — you can share bases with her, @mention her, and add her to groups. It does **not** give her access to any of your bases. Each base is shared separately and on purpose, so nothing is exposed until you decide to share it.

So Malika is in the team, but looking at her home page right now, your `Sales CRM` base is nowhere to be seen. Let's change that.

## Sharing your base with a colleague

Malika needs to work in your base, so you will share it with her. Because Malika is in Marketing and your base lives with Commercial, the right tool here is a direct **user share** — you hand access to one named person.

In your window 🌐, on the SeaTable home page, open the `Sales CRM` tile's menu and choose `Share`. Under `Share to user`, select Malika, set the permission to `Read-Write`, and submit.

![The Share dialog with Share to user open, Malika selected and the permission set to read and write](images/lvl3-share-base-with-user.gif)

You can also open this dialog from inside the base, through the share icon {{< seatable-icon icon="dtable-icon-share" >}} in the top-right base options.

Please note that you'll have to type either the username or the **whole user email address** for the system to find the corresponding user.

You can also share a base with a whole **group**, but only a group you are a member of — and then everyone in it sees the base. That makes group sharing the way to give the rest of *your own* Commercial team access, not a way to reach another department. To get data to a separate team like Marketing without adding yourself to their group, you use a common dataset — which is exactly what Step 5 is about.

Now switch to Malika's window 🕶. The first thing she sees is the **notification bell** {{< seatable-icon icon="dtable-icon-notice" >}} at the top right of her home page showing a new alert: SeaTable has told her that a base was shared with her. Refresh the page and the `Sales CRM` base also appears in her workspace, in the `{{< seatable-icon icon="dtable-icon-share-with-me" >}} Shared with me` section. Open it, and you can read and edit the data — Malika is now collaborating on your base.

{{< warning headline="Two places notifications show up" text="The bell at the top right is the notification center, and you can open it both from the home page and from inside a base. Where a notification appears depends on what it is about. Account-wide events, like a base being shared with you, always land on the home page. Events that happen inside a base — comments, mentions, automations — show up in that base instead. That is why Malika received this share notification on her home page, while the comment notifications you send in the next step will be waiting for her inside the base." />}}

## Choosing the right permission level

When you share a base, there is an important decision to make. SeaTable offers three ways to share a base, from the simplest to the most precise.

| Permission | What the colleague can do | When to use it |
|---|---|---|
| Read-Only | See every table, view and value, but change no data. They can still add comments and be @mentioned, so they can take part in the discussion — read-only locks the data, not the conversation. They can also make their own private copy of the base, which is not connected to yours. | The colleague only needs to consult the data, but can still discuss it. |
| Read-Write | See and edit the whole base. They cannot rename the base, install plugins, or re-share it — those stay with the owner. | The colleague is a full working partner on all of the data. |
| Custom sharing | See and edit only the specific tables and views you pick, each set individually to read-write, read-only, or no access at all. | The colleague should work with part of the base but be kept out of the rest. |

For this course you chose `Read-Write`, so that Malika can take a full part in the steps that follow — commenting, editing, and showing up in the activity log. It also means she can change your data, and even get something wrong, as you will see in Step 4. Keep that share in place.

{{< warning headline="A read-only share is not a lockbox" text="Someone with a read-only share cannot change your base, but they can still make their own copy of it and do whatever they like in that copy. Read-only protects your data from being changed, not from being seen or duplicated. If some of the data should never reach a colleague at all, do not share it with them in the first place." />}}

## When a colleague should see only part of the base

Read-Write gave Malika the whole base — including the `Deals` table and the confidential `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Total Deal Value` and `{{< seatable-icon icon="dtable-icon-formula" >}} Weighted Value` figures you flagged in Step 1. For a close working partner that may be fine. But Malika is in Marketing, and the sales pipeline is need-to-know. This is exactly what **Custom sharing** is for.

With a custom share you build one permission that bundles several tables and views, each with its own level. For Malika you could, for example:

- give Read-Write access to the `Customers` table, so she can still work with the contact list.
- give no access at all to the `Deals` table, keeping the whole pipeline out of her hands.
- or, more finely, share only the `{{< seatable-icon icon="dtable-icon-main-view" >}} Active Customers` view rather than `{{< seatable-icon icon="dtable-icon-main-view" >}} All Customers`, so the confidential columns hidden in that view never reach her.

This is the precise tool for "work with these contacts, but the revenue figures are not yours to see."

{{< warning headline="Custom sharing needs a paid plan" text="Custom sharing of individual tables and views is available on the Plus and Enterprise plans, not on the free plan. On a free plan you share a base as a whole, either Read-Only or Read-Write. Do not worry if you cannot try this part: in Step 5 you will learn the common dataset, which distributes only a chosen, safe view to another team and is available on every plan. For most cross-team sharing it is the better tool anyway." />}}

Custom sharing is not the only way to narrow down what someone sees. You can also share an individual view on its own — directly with a team member or a group, or as a Read-Only **external link** for people who have no SeaTable account at all. Because a view already carries its own filter and hidden columns, sharing just the `{{< seatable-icon icon="dtable-icon-main-view" >}} Active Customers` view hands over exactly that slice and nothing more. Like custom sharing, sharing a view is a Plus and Enterprise feature.

A different route avoids base sharing altogether: build a **Universal App** on top of the base. In an app you design pages of several types, and table pages can use preset filters, sorting and hidden columns, so the people who use the app only ever see the slice you chose to expose — never the underlying base. This suits a wider audience of data consumers rather than collaborators working inside your team.

## Taking access away again

Sharing is not permanent. To stop sharing, open the share dialog again and remove Malika.

It is worth seeing this from the other side. While Malika has the base open in her window 🕶, revoke her share from your window 🌐. Back in Malika's window, refresh or click into the base, and SeaTable tells you the permission was denied — the access is gone the moment you remove it. This is the safety net behind sharing: access is something you grant and can withdraw at any time. For the rest of the course, share the base with Malika again as `Read-Write` so she can keep working alongside you.

## Try it yourself

If you are on a Plus or Enterprise plan, go further than the whole-base share you just set up: build a custom share that gives Malika the `Customers` table but no access to `Deals`, and confirm in her window 🕶 that `Deals` has vanished entirely. That is the precise table-level control the free plan does not offer — and one reason Step 5's common dataset exists as the free way to share only part of your data. Switch back to a plain Read-Write share afterwards, so Malika keeps full access for the next steps.

Malika can now see and edit your data. But editing in silence is a recipe for confusion — next you will learn how to discuss specific records in context.

## Help article with further information

- [Base and view shares at a glance]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick/" >}})
- [Set table permissions]({{< relref "help/base-editor/tabellen/tabellenberechtigungen-setzen/" >}})
- [Access to the notifications]({{< relref "help/startseite/benachrichtigungen/alle-benachrichtigungen-loeschen-oder-als-gelesen-markieren#access-to-the-notifications" >}})
- [Table pages in SeaTable apps]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps/" >}})
