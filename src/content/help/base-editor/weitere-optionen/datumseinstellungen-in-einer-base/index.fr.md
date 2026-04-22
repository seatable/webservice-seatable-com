---
title: 'Paramètres de date dans une base'
date: 2025-07-02
lastmod: '2025-07-02'
categories:
    - 'arbeiten-mit-bases'
author: 'kgr'
url: '/fr/aide/parametres-date-base'
aliases:
    - '/fr/aide/datumseinstellungen-in-einer-base'
seo:
    title: 'Paramètres de date adaptés dans votre base SeaTable'
    description: 'Définissez le premier jour de la semaine dans chaque base SeaTable. Choisissez lundi, samedi ou dimanche pour personnaliser vos calendriers selon vos besoins.'

---

Comme c'est le cas en Europe et dans de nombreuses autres régions, SeaTable utilise par défaut **le lundi** comme premier jour de la semaine. Cependant, selon votre pays de résidence, le samedi ou le dimanche peut être considéré comme le **premier jour de la semaine**. Vous pouvez donc adapter SeaTable à votre région : Dans les **Paramètres de date**, le premier jour de la semaine peut être défini individuellement pour chaque base.

{{< warning type="warning" headline="Note importante" >}}
Les paramètres de date d'une base appartenant à un groupe peuvent être modifiés **exclusivement par les propriétaires** et les **administrateurs**. Les membres simples du groupe ne voient **pas** les paramètres de date.
{{< /warning >}}

## Modifier le premier jour de la semaine dans une base

![Paramètres de date dans une base](images/date-settings-of-a-base.gif)

1. Ouvrez la **base** dont vous souhaitez modifier les paramètres de date.
2. Cliquez sur les **trois points** dans l'en-tête de la base.
3. Allez sur **Paramètres** puis sur **Paramètres de date**.
4. Dans la nouvelle fenêtre, choisissez quel jour de la semaine doit être **le premier jour de la semaine**.
5. **Fermez** ensuite la fenêtre. Les réglages que vous avez effectués sont automatiquement **enregistrés**.

## Champ d'application des paramètres de date

Un ajustement dans les paramètres de date fait que dans le contrôle de calendrier de [Colonnes de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}), le jour sélectionné se déplace vers la première colonne. Cela s'applique à la base actuellement ouverte et à toutes les applications basées sur celle-ci.

Dans le [plugin de calendrier]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) ainsi que sur la [page de calendrier dans l'app]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}), vous pouvez cependant continuer à configurer le premier jour de la semaine individuellement et indépendamment du réglage dans la base.