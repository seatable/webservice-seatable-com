---
title: 'Instructions for the File audit plugin'
date: 2026-11-24
lastmod: '2026-11-26'
categories:
    - 'plugins'
author: 'bha'
url: '/help/instructions-for-the-file-audit-plugin'
aliases:
    - '/help/anleitung-zum-datei-audit-plugin'
seo:
    title: 'File Audit Plugin Guide in SeaTable'
    description: 'The SeaTable File audit plugin finds the files a base no longer uses, the references to missing files, and what takes up its storage.'
---

The **File audit plugin** looks at the **files stored in your base**: everything uploaded to the base — in file, image and signature columns, in long text, in comments, forms and apps — plus the files in your own custom folders of the [file manager]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). It compares what is in storage with what your base actually references, and reports the gap in both directions: **files nobody uses any more**, and **references to files that no longer exist**. It also shows you where the space goes.

Storage fills up quietly in SeaTable, because removing a file from a cell **does not delete it**: the file stays in the base's file manager, so that it can be [restored]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}). Over time, a base can end up storing far more than its rows show.

The plugin needs no configuration: the first time you open it, the audit runs on its own. Running the audit changes nothing — files are deleted and references removed only when you ask for it, one item or one group at a time.

{{< zoom image="images/file-audit-plugin.png" alt="The File audit plugin showing the storage of a base by folder and its orphaned assets" >}}

You can find out how to activate a plugin in a base [here]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## How the audit works

An audit does three things:

1. It **lists the base's storage**: every file, with its folder and size.
2. It collects every file the base **references**, wherever it is used:
    - the **file and image columns** of every table, and the **signatures** of signature columns,
    - the images inserted in **long text** cells,
    - the images of the **base description** and of the **row comments**,
    - the images of the base's **web forms** and of the forms of its **apps**,
    - the **archived rows**, which are read like the others.
3. It checks the **other bases you have access to**, to find rows there that display files stored in this base (see [Files shared between bases](#files-shared-between-bases) below).

It then compares the lists and shows the result. The audit runs with **your own rights** — there is no token to create — and the report is saved with the base: when you open the plugin again, you find the last result, with its date, rather than a new run. **Rerun audit** starts it again, which you should do after any change.

{{< warning type="warning" headline="Scripts are not audited" text="The base's **scripts** are stored as files of their own, but the plugin does not see them at all: just as in the file manager, they are not listed in the base's asset tree, their size is not counted, and **what they contain is not read** — a file that a script uses is not seen as a reference. Scripts are assets of the base nonetheless: when you export it, **only the *Include assets* option keeps them**." />}}

## What the plugin reports

### Summary and storage by folder

The top of the report sums things up: **total assets in storage**, how many are **referenced in the base**, how many are **orphaned**, and how much of the storage they represent, then the number of **missing references** and **external URLs**.

**Storage by folder** shows where the space goes. Click a folder to drill down into it. Your own folders (**custom folders**) are shown apart from the **system folders** that SeaTable creates for file and image columns, signatures, forms and apps. Some of the system folders hold files SeaTable needs to run the base, which no row references by design — plugin files, the pages and settings of each app, form logos and background images, and page design templates: they are flagged **System folder - DO NOT DELETE**, and never listed as orphaned. The files that users upload through an app, on the other hand, are audited like any other upload.

### Orphaned assets

An **orphaned asset** is a file in storage that no row references any more — typically a file removed from a cell, or one left behind by a deleted row. The list is grouped by folder: you can delete a single file, or every orphaned file of a folder at once.

If one of the places listed [above](#how-the-audit-works) **could not be read** during a run — the comments or the archived rows, for example — the section names it and **deletion is disabled** for that run: every file used only there would otherwise be offered for deletion. Rerun the audit to try again.

Before deleting anything, read the warnings in that section and the [limitations](#limitations) below: an orphan is a file *the plugin found no reference to*, which is not quite the same as a file nobody needs.

{{< warning type="warning" headline="Deleted files go to the trash" text="Files the plugin deletes go to the **trash** of the file manager, where they stay for **60 days** and can be restored. After that, or once the trash is emptied, they are gone for good: snapshots do not include files. To keep a full backup, **export the base with the *Include assets* option** before deleting anything." />}}

### Missing references

A **missing reference** is the opposite: a row whose file or image column points to a file that **no longer exists** in storage. The cell still shows an entry, but there is nothing behind it. You can remove the stale reference from a row, from all the rows of a column, or everywhere at once. The rest of the cell is left untouched.

### External URLs

Image columns can also hold links to files **hosted outside SeaTable**. The plugin lists them, grouped by table and column. They are not checked during the audit, which would slow it down: start the check yourself with **Verify external URLs**. Each link then comes out **OK**, **broken**, or **unverifiable** — many sites do not let a browser check their files from another site, so *unverifiable* does not mean the link is broken. You can then remove the broken links.

### Files shared between bases

The last two sections cover **files that cross from one base to another** — a case that is easy to miss, and the reason the plugin checks your other bases on every audit.

When you **copy a cell or a row** from one base to another, SeaTable copies the reference to the file, **not the file itself**. The file stays stored in the original base, and the other base displays it from there — even if it is in a different workspace. Nothing in either base shows that they are now linked. **Importing a table** from another base works differently: it copies the files too, so the two bases are independent afterwards. **Prefer this method** whenever you need the files in both bases.

- **Files used by other bases** lists the files stored in *this* base that rows in *another* base display. They are kept out of the orphan list, even if nothing in this base references them any more: deleting one would break the other base.
- **References to files in other bases** is the mirror image: rows in *this* base that display a file stored in *another* base. They are neither orphans nor missing references here, and the plugin cannot check whether those files still exist.

A file displayed this way keeps the **permissions of the base that stores it**. People who have no access to that base see an **empty cell** where you see the file — so the same row can look different to two people.

## Permissions and safety

- With **read-only** access to the base, you can read the whole report, but the delete and remove buttons are not available.
- In a **group** you do not administer, you can still delete files, but the plugin warns you that they may have been uploaded by other members, and asks for an explicit confirmation.
- Before it changes a row for the first time — removing a missing reference or a broken link — the plugin takes a **snapshot** of the base. It lets you recover the **cell contents** the plugin removed: the file names and links, not the files themselves. Deleting files changes no row and is not covered: snapshots do not include files (see the warning [above](#orphaned-assets)).

## Limitations

{{< warning type="warning" headline="Only the bases you can access are checked" text="The search for references in other bases covers the bases you can see: those in your workspaces and groups, and those shared with you. A colleague's base you have no access to may well display a file from yours, and the plugin has no way of knowing. **An orphan in the report is therefore never a proof that a file is unused.** Those bases never appear in the report, since the plugin does not know they exist. Only the bases you can see but that the plugin failed to read during a run — after an error, for example — are named in the report, with the reason." />}}

The audit has a few other blind spots worth knowing before you delete:

- **Only the places listed [above](#how-the-audit-works) are read.** A file referred to in any other way is not seen as a reference, and may therefore be listed as orphaned — for example a file whose address is stored in a text or URL column, or used in a script or by an external tool (an orchestrator, etc.).
- **Your own folders count like the rest.** A file you uploaded to a custom folder of the file manager, to keep it there, is listed as orphaned as long as no row references it.
- **Files in custom folders are not traced across bases.** A row refers to them by an identifier that does not say which base stores them, so the plugin cannot tell whether another base uses one.
- **A base created by import or copy can still use files of the original base.** When you import a base from a `.dtable` file or copy it, its files are copied too, but some places keep their links to the original base — depending on how the base was created, the images of the base description, of web forms and app forms, or the files of archived rows. The plugin lists these links under **References to files in other bases**, and the copies they leave unused in this base appear as orphans. Their images are loaded from the original base, and some of them may not display for other people, even if they have access to that base. Row comments are not part of an export or a copy either, so the images inserted in them also end up orphaned in the new base.
- **The report describes the moment it ran.** Anyone can add or remove a reference afterwards, in this base or in another one: rerun the audit before deleting.
- On an account with many bases, checking all of them **takes a while**.

## Other helpful articles

- [All plugins at a glance]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [The file management of a base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
- [Access to deleted files and images]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}})
- [How to remove files permanently]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}})
- [Activating a plugin in a base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
