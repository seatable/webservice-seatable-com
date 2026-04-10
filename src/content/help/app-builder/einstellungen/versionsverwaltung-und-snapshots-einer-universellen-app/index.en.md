---
title: 'Version management and snapshots of an app'
date: 2023-11-29
lastmod: '2024-02-16'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/help/version-control-and-snapshots-universal-app'
aliases:
    - '/help/versionsverwaltung-und-snapshots-einer-universellen-app'
seo:
    title: 'Version control & snapshots in the SeaTable App Builder'
    description: 'Learn how to use snapshots in the SeaTable App Builder to save, view, restore and manage app versions, ensuring control over changes and settings.'
---

You can use **snapshots** to save the current version of an app. You can **create**, **view**, **restore** and **delete** snapshots in the version management of the SeaTable App Builder. You can also make **notes** on the individual snapshots to record information about a version.

{{< warning  headline="Authorization required in the group"  text="To be able to use app snapshots, you must be the **owner** or **administrator of the group** in which the underlying **base** is located. Simple **group members** do not have access to version management." />}}

## When app snapshots are useful

App snapshots are **snapshots** of the state of an app and work in a similar way to [base snapshots]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). You can use app snapshots to save the current version of an app as a backup copy, which can be useful, for example, if you want to make extensive changes and possibly restore a previous state.

{{< warning  headline="Beware of data loss"  text="Unlike base snapshots, app snapshots **do not** save **data records**, but only the **structure** and **settings** of the app. This means that if you change or delete certain entries in the underlying base via the app, you cannot restore them via the app snapshots." />}}

### What an app snapshot saves

An app snapshot saves the following elements and settings:

- [Settings]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) such as **name**, **icon** and **color scheme** of the app
- [Pages and folders]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) of the app
- Settings and [authorizations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) for the individual pages

### What an app snapshot does not save

An app snapshot does not save:

- the **user-defined URL** of an app
- the **data** of the underlying base
- the **comments** on individual data records
- the app's [user roles and invitation links]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}})

## Create app snapshot

1. Open an **app** in [edit mode]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).

![SeaTable App Builder in edit mode with opened app list](images/Apps-bearbeiten.png)

3. Click on {{< seatable-icon icon="dtable-icon-history" >}} **Version management** at the top left of the page.

![Version management of an app showing list of existing snapshots](images/Version-management-in-Universal-App-Builder.png)

5. A window opens. Create a **new snapshot** there.
6. Optionally, you can add a **note** to the snapshot.
7. Confirm with **Submit**.

![Creating a new app snapshot in version management with optional note text](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Numbering of the versions"  text="The exact **creation time** and a **version number** are recorded for each snapshot. Do not be surprised if your snapshots do not receive consecutive numbers (1, 2, 3 ...). SeaTable counts every change you make in an app as a separate version. This means that there can quickly be dozens of versions between two snapshots." />}}

As soon as you have created a snapshot, you have four operations to choose from:

- **View version**
- **Restore version**
- **Note**
- **Delete version**

## View app snapshot

Before you restore a snapshot and hastily jump back to another version, you should first take a look at this version. To do this, follow the same procedure as above: Click on the **three dots** at the right-hand end of a snapshot and select the **View version** operation from the drop-down menu.

![Preview of a saved app version in the SeaTable App Builder](images/Preview-version-of-app-snapshot.png)

## Restore app snapshot

To restore an app snapshot, click on the **three dots** and select the corresponding operation from the drop-down menu.

![Dialog for restoring an app snapshot as the current version](images/Restore-version-of-app-snapshot.png)

{{< warning  headline="Attention"  text="The snapshot restore in the SeaTable App Builder works differently than in the base, where the snapshot is restored in a new base and the current version is retained. **In the SeaTable App Builder, however, the current version is discarded when you restore a snapshot.**" />}}

As soon as you restore a snapshot, the app is reset to the memory status of this earlier version. Any **changes** you have made to pages, folders and settings in the app since then will be **lost**. It is therefore advisable to also save the current version in a snapshot before restoring a snapshot. This allows you to jump back and forth between different versions.

## Edit note

If you want to add, change or delete the note for a version at a later date, you can do this at any time. Open the corresponding text field by clicking on the **three dots** at the right-hand end of a snapshot and selecting **Note** from the drop-down menu. Save your changes by clicking **Submit**.

![Dialog to edit or add a note to an app snapshot](images/Modify-notes-of-app-snapshot.png)

## Delete app snapshot

You can delete a snapshot that you no longer need at any time. Click on the **three dots** at the right-hand end of a snapshot and select the **Delete version** operation from the drop-down menu.

![Confirmation dialog for permanently deleting an app snapshot](images/Delete-version-of-app-snapshot.png)

{{< warning  headline="Attention"  text="The deletion of an app snapshot is final. The memory status of the previous version is irrevocably lost and cannot be restored." />}}
