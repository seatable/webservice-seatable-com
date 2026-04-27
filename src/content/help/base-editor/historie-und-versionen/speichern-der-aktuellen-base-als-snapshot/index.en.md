---
title: 'Saving the current base as a Snapshot'
date: 2022-10-11
lastmod: '2024-06-11'
categories:
    - 'historie-und-versionen'
author: 'nsc2'
url: '/help/save-base-snapshot-seatable'
aliases:
    - '/help/speichern-der-aktuellen-base-als-snapshot'
seo:
    title: 'Save SeaTable base as snapshot – backups and restore FAQ'
    description: 'Save the current state of your SeaTable base as a snapshot for quick backups and easy restores. Snapshots are automatic and can be made manually too.'
---

You can save a base in SeaTable as a **snapshot** at any time. Snapshots are part of SeaTable's DNA: Ever since the first version, you have been able to create **snapshots** of the status of a base and restore them at a later point in time. Snapshots are useful, for example, if you want to save the current version of a base before making extensive changes.

Good to know: SeaTable automatically creates one snapshot per day of each base where changes have been made. This way you always have backup copies of your bases with the latest versions.

{{< warning  headline="Attention"  text="Although snapshots are copies of a base's save states, they **do not contain all** information and settings. You cannot restore **comments**, **webforms**, **automations**, **apps**, **contents in the trash** and **data in the big data storage** with snapshots." />}}

## Manual creation of a snapshot

![Manual creation of a snapshot](images/manual-creation-of-a-snapshot.gif)

1. Click on {{< seatable-icon icon="dtable-icon-history" >}} **versions** at the top right of the base options.
2. Select the **Snapshots** option in the drop-down menu that opens.
3. Click **Create Snapshot**.

{{< warning  headline="Note"  text="You can create a snapshot **every 10 minutes**. If you try to do this before then, a message appears stating that the snapshot could not be created." />}}

## Storage duration of snapshots

The snapshots of bases are kept for a certain period of time and then deleted.

With [SeaTable Cloud](https://cloud.seatable.io/), the storage duration of the snapshots depends on [your team's subscription]({{< relref "pages/prices" >}}):

- With the free **subscription**, the snapshots are saved for one month.
- With the **Plus** or **Enterprise subscription**, snapshots are stored for 6 or 12 months. (The extended storage period applies from the time of the upgrade).

If you operate your own [SeaTable server]({{< relref "pages/product/seatable-server" >}}), you can set the snapshot storage duration individually.

## Want to learn more about snapshots?

You might be interested in the following articles regarding the handling of snapshots:

- [Restoring a snapshot]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})
- [Data recovery options with SeaTable]({{< relref "help/base-editor/historie-und-versionen/moeglichkeiten-der-datenwiederherstellung" >}})

## Frequently asked questions

{{< faq "What information from a base is saved in a snapshot?" >}}A snapshot saves all **table data** (columns and rows) as well as **views** and their settings. **Statistics**, **plugins** and their settings and **scripts** are also saved.
{{< /faq >}}
{{< faq "What information from a base is NOT saved in a snapshot?" >}}**Comments**, **web forms**, **automations**, **apps** and **content in the trash** (deleted tables, columns and rows) are **not** saved in snapshots. Data in the big data storage is also not included in a snapshot.
{{< /faq >}}
{{< faq "How often are automatic snapshots created?" >}}Snapshots are created automatically **once a day** if changes have been made to the base. The time at which this happens cannot currently be influenced.
{{< /faq >}}
{{< faq "How often can you manually create a snapshot?" >}}You can create a snapshot manually every **10 minutes** at most.

{{< /faq >}}
