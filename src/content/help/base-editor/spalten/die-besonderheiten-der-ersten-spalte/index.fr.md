---
title: 'Les particularités de la première colonne'
date: 2022-10-13
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/fr/aide/specificites-premiere-colonne'
aliases:
  - '/fr/aide/die-besonderheiten-der-ersten-spalte'
seo:
    title: 'Spécificités de la première colonne dans SeaTable détaillées'
    description: 'Découvrez les avantages et restrictions de la première colonne SeaTable, les types disponibles et comment la personnaliser étape par étape.'
---

Dans SeaTable, la **première colonne** d'un tableau présente plusieurs particularités et restrictions par rapport aux autres colonnes. Voici comment personnaliser la première colonne dans SeaTable.

## Les particularités de la première colonne de SeaTable

- Contrairement aux autres colonnes, vous ne pouvez **pas masquer** la première colonne d'un tableau.
- Contrairement aux autres colonnes, vous ne pouvez **pas déplacer** la première colonne d'un tableau.
- Contrairement aux autres colonnes, vous ne pouvez **pas supprimer** la première colonne d'un tableau.
- Mais contrairement aux autres colonnes, vous pouvez **fixer** individuellement la première colonne.
- Pour la **première colonne**, il n'y a que **six types de colonnes** au choix :
  - [Texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
  - [Nombre]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
  - [Date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
  - [Sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
  - [Numéro automatique]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
  - [Formule]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Comment personnaliser le type de la première colonne

![Personnaliser la première colonne](images/change-the-first-column.gif)

1. Cliquez sur l'**icône** triangulaire **déroulante** à droite du nom de la première colonne.
2. Allez sur **Personnaliser le type de colonne**.
3. Cliquez dans le **champ** du type de colonne actuel.
4. Sélectionnez un **nouveau type de colonne** pour la première colonne.
5. Le cas échéant, effectuez **des réglages de format**.
6. Cliquez sur **Envoyer**.
7. Confirmez l'adaptation en cliquant sur **Convertir**.

## Formules dans la première colonne

Si vous définissez une **formule** comme **première colonne** d'un tableau, vous pouvez par exemple utiliser la simple formule **{column name}** pour **citer** les entrées de presque toutes les autres colonnes de votre tableau. Cela est même possible si l'autre type de colonne n'est **pas** pris en charge dans la première colonne.

![Possibilités avec le type de colonne Formule dans la première colonne d'un tableau](images/formular-in-the-first-column-1.png)

## Questions fréquentes

{{< faq "Quelles sont les restrictions de la première colonne ?" >}}La première colonne ne peut être ni **masquée**, ni **déplacée**, ni **supprimée**.
{{< /faq >}}
{{< faq "Est-il possible de modifier ultérieurement le type de la première colonne ?" >}}Oui, c'est possible. Dans certains cas, il peut toutefois arriver que des informations soient **perdues** lors de la [modification du type de colonne]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}), par exemple du texte au nombre. Après une conversion, vérifiez donc que toutes les informations ont été reprises correctement et intégralement.
{{< /faq >}}
{{< faq "Qu'est-ce qu'un numéro automatique ?" >}}Si vos lignes doivent avoir un **numéro d'identification unique**, le type de colonne [Numéro automatique]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}) pourrait vous rendre de fiers services. Les numéros de facture, les cas de test ou les identifiants des collaborateurs en sont des exemples. Le numéro peut en outre être complété par un préfixe de votre choix.

{{< /faq >}}
