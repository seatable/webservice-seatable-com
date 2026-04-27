---
title: "Définir la valeur par défaut d'une colonne"
date: 2023-11-07
lastmod: '2024-06-11'
categories:
    - 'arbeiten-mit-spalten'
author: 'kgr'
url: '/fr/aide/definir-valeur-par-defaut-colonne'
aliases:
    - '/fr/aide/standardwert-fuer-eine-spalte-festlegen'
seo:
    title: 'Définir une valeur par défaut pour une colonne'
    description: 'Apprenez à définir des valeurs par défaut pour vos colonnes SeaTable et remplissez automatiquement les nouvelles lignes afin de gagner du temps.'
---

Lorsque vous définissez une **valeur par défaut** pour une colonne, celle-ci est **automatiquement** insérée **dans chaque nouvelle ligne** du tableau. Les valeurs par défaut prédéfinies vous permettent donc d'économiser quelques clics lors de l'[ajout de nouvelles lignes]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}}). Vous pouvez bien sûr ensuite adapter manuellement les valeurs saisies automatiquement.

## Comment définir des valeurs par défaut

![Définir la valeur par défaut d’une colonne](images/Standardwert-festlegen.gif)

1. Cliquez sur l'**icône** triangulaire **déroulante** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} à droite du nom de la colonne pour laquelle vous souhaitez définir une valeur par défaut.
2. Sélectionnez l'option **Définir la valeur par défaut**.
3. Saisissez la **valeur par défaut** souhaitée. Selon le type de colonne, vous avez le choix entre plusieurs possibilités.
4. Confirmez l'opération en appuyant sur la **touche Entrée** ou en **cliquant** en dehors de la boîte de dialogue.
5. Si vous **créez** maintenant une **nouvelle ligne**, SeaTable y inscrit automatiquement les valeurs correspondantes. Vous pouvez ensuite **adapter** les données comme d'habitude.

{{< warning  headline="Attention"  text="Les valeurs par défaut sont utilisées de **manière universelle** lors de la création de nouvelles lignes, c'est-à-dire que les lignes créées par une action automatisée ou par un bouton contiennent également les valeurs par défaut." />}}

En outre, vous pouvez déjà définir directement une valeur par défaut lors de la [création d'une nouvelle colonne]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

## les types de colonnes pour lesquels vous pouvez définir des valeurs par défaut

Les valeurs par défaut peuvent être définies pour de nombreux [types de colonnes dans SeaTable]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}), mais pas pour tous. Les colonnes dont le contenu est généré automatiquement par SeaTable[(Formules]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}), de [fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) et [de signatures]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}}).

**Voici un aperçu des types de colonnes pour lesquelles vous pouvez définir des valeurs par défaut :**

| Type de colonne        | supporte les valeurs par défaut                               |
| ---------------------- | ------------------------------------------------------------- |
| Numéro automatique     | {{< icon "circle-xmark" >}}                                   |
| Image                  | {{< icon "circle-xmark" >}}                                   |
| Case à cocher          | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fichier                | {{< icon "circle-xmark" >}}                                   |
| Date                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Durée                  | {{< icon "circle-xmark" >}}                                   |
| Sélection unique       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Courriel :             | {{< icon "circle-xmark" >}}                                   |
| Créateur               | {{< icon "circle-xmark" >}}                                   |
| Créé                   | {{< icon "circle-xmark" >}}                                   |
| Texte formaté          | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Formule                | {{< icon "circle-xmark" >}}                                   |
| Formule pour les liens | {{< icon "circle-xmark" >}}                                   |
| Géoposition            | {{< icon "circle-xmark" >}}                                   |
| Dernier responsable    | {{< icon "circle-xmark" >}}                                   |
| Sélection multiple     | {{< icon "circle-xmark" >}}                                   |
| Employés               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Rating                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Bouton                 | {{< icon "circle-xmark" >}}                                   |
| Signature              | {{< icon "circle-xmark" >}}                                   |
| Texte                  | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                    | {{< icon "circle-xmark" >}}                                   |
| Nombre                 | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Dernièrement édité     | {{< icon "circle-xmark" >}}                                   |

## Valeurs par défaut référencées dans les colonnes de texte

Si vous définissez comme valeur par défaut dans une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) la référence **{creator.name}** ou **{creator.id}**, le **nom** ou l'**ID de l'utilisateur** qui a ajouté la ligne sera automatiquement inscrit.

![Référencer le nom d'utilisateur avec une valeur par défaut](images/Set-creator-name-as-default-value.png)

## Le champ d'action des valeurs par défaut

Les valeurs par défaut s'appliquent **partout** où vous pouvez créer de nouvelles lignes :

- dans un [tableau]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}})
- dans une [colonne de liens]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- par [bouton]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) (action : "Copier une ligne dans un autre tableau")
- par [automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) (actions : "Ajouter une ligne" et "Ajouter une nouvelle entrée dans un autre tableau")
- dans la [vue du calendrier, du Kanban, de la galerie et de l'arborescence]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- via [des formulaires web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- sur [les pages de tableaux]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), de [formulaires]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) et [de Kanban]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kanbanseiten-in-universellen-apps" >}}) des apps

![La valeur par défaut s'applique à toutes les nouvelles lignes](images/Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

## Valeurs par défaut dans les formulaires web

En plus des valeurs par défaut définies dans le tableau, vous avez la possibilité, pour les [formulaires web]({{< relref "help/base-editor/webformulare/webformulare" >}}), de définir des valeurs par défaut pour les champs de formulaire liés aux colonnes. Ce faisant, vous pouvez également définir si les utilisateurs sont autorisés à **modifier** ces **valeurs par défaut** lorsqu'ils remplissent le formulaire.

![Définir des valeurs par défaut dans les formulaires web](images/Set-default-values-in-web-forms.png)

{{< warning  headline="Remarque importante"  text="Si une valeur par défaut est définie à la fois dans le tableau et dans le formulaire web, la valeur du formulaire s'applique à toutes les lignes créées via le formulaire web. Les valeurs par défaut définies dans le tableau n'ont d'**effet que** si vous ne définissez pas de valeurs par défaut dans l'éditeur de formulaires." />}}

## Valeurs par défaut dans les apps

Les valeurs par défaut définies dans la base affectent également les lignes saisies dans les pages de **tableau, de formulaire et de kanban** des [apps]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Le seul [type de page]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) pour lequel vous pouvez tout de même définir des valeurs par défaut dans l'app est la [page de formulaire]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}). Les paramètres fonctionnent de la même manière que pour les formulaires web : Activez pour cela les curseurs, comme vous pouvez le voir sur la capture d'écran ci-dessus.
