---
title: 'Déplacer des lignes vers le stockage de big data'
date: 2022-09-23
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/fr/aide/transferer-lignes-big-data-backend'
aliases:
    - '/fr/aide/zeilen-ins-big-data-backend-verschieben'
seo:
    title: 'Transférer des lignes dans le Big Data de SeaTable – explications'
    description: 'Apprenez à déplacer, archiver et restaurer des lignes dans le Big Data de SeaTable. Guide complet pour activer et reconnaître ces données dans le système.'

---

{{< required-version "Entreprise" >}}

Vous ne pouvez créer **de nouvelles lignes** que dans les **vues normales** de SeaTable. Ensuite, vous pouvez déplacer les lignes de la vue **manuellement ou automatiquement** vers le stockage de big data.

{{< warning  headline="Condition préalable" >}}

Vous ne pouvez déplacer des lignes vers le stockage de big data que si vous l'[avez déjà activé]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) au sein de la base.

{{< /warning >}}

## Déplacer des lignes vers le stockage de big data

![Déplacer des lignes vers le stockage de big data](images/move-rows-to-big-data.gif)

1. Cliquez sur les **trois points** dans les options de vue.
2. Sélectionnez l'option **Archiver la vue**.
3. **Confirmez** le déplacement de toutes les lignes visibles dans la mémoire Big Data.

{{< warning  headline="Conseil" >}}

Si vous souhaitez par exemple **archiver d'anciennes entrées**, vous pouvez filtrer la vue au préalable avec les types de colonnes [Date de création]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Date de dernière modification]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}).

{{< /warning >}}

Les lignes sont ensuite transférées dans la mémoire Big Data. Ainsi, elles ne sont plus visibles dans la vue normale. [Créez une vue Big Data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}) pour afficher les données dans le stockage Big Data.

## Archivage automatisé

Vous pouvez également créer une **règle d'automatisation avec l'action "Archiver"** pour que SeaTable déplace de lui-même les lignes d'une vue vers le stockage de big data à un moment donné.

Pour en savoir plus, consultez [Actions d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Comment savoir si des données se trouvent ou non dans le stockage de big data ?

Les lignes stockées dans la mémoire Big Data ont un petit **triangle gris dans la colonne de numérotation** .

**Bon à savoir**

- Dans une [vue normale]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}), vous ne verrez **pas de lignes provenant de la mémoire Big Data**.
- Dans une [vue Big Data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}), vous pouvez voir **toutes les lignes**, quel que soit l'endroit où elles sont actuellement stockées.

## Récupérer des enregistrements dans le stockage de big data

[Cet article]({{< relref "help/base-editor/big-data/zeilen-aus-dem-big-data-backend-zurueckholen" >}}) vous explique comment récupérer des enregistrements dans le stockage de big data.
