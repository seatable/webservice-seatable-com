---
title: 'Validation de la saisie dans les champs de texte avec expressions régulières'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/fr/aide/validation-texte-regex-seatable'
aliases:
    - '/fr/aide/validierung-der-eingabe-bei-textfeldern'
seo:
    title: 'Validation de texte SeaTable : expressions régulières'
    description: 'Vérifiez et signalez les valeurs saisies dans SeaTable avec des regex. Détectez automatiquement les formats incorrects et améliorez la qualité de vos données.'

---

Lorsque vous utilisez des colonnes de texte dans vos tableaux, vous avez la possibilité de valider les entrées. La validation, qui prend en charge les expressions régulières, vous permet de vérifier les valeurs des cellules et de mettre en évidence les cellules dont le contenu diffère du format valide.

{{< warning  headline="Remarque" >}}

En principe, vous disposez de deux méthodes différentes pour valider les entrées dans les colonnes de texte. Une validation peut être effectuée au cours de l'**ajout d'une nouvelle** [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) **déjà créées**.

{{< /warning >}}

## Valider les entrées

![Activation de la validation de la saisie des colonnes de texte](images/activate-validation-1.png)

1. Si vous souhaitez effectuer une validation des saisies dans une colonne de texte déjà créée, cliquez d'abord sur le **symbole triangulaire** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} de la colonne correspondante.
2. Sélectionnez **Personnaliser le type de colonne** dans le menu déroulant.
3. Activez le curseur **Valider la saisie**
4. Définir un **format cible**.
5. Confirmez en cliquant sur **Envoyer**.

![Définition du format cible](images/define-specific-format-2.png)

## Conséquence de la validation

Une fois la validation réussie, les **cellules** dont **le contenu diffère** du format cible sont mises en évidence en rouge.

![Cellules surlignées en rouge dont le contenu diffère du format cible](images/marked-entries-which-not-match-the-format.png)

## Expressions régulières

Pour valider vos entrées dans les colonnes de texte, SeaTable prend en charge les expressions régulières **(regular expressions)**.  
Vous trouverez quelques exemples dans le tableau ci-dessous :

| Expression régulière            | Fonction                                                                        |     |     |     |     |
| ------------------------------- | ------------------------------------------------------------------------------- | --- | --- | --- | --- |
| \[123456\]                      | Vérifier si une entrée correspond à une note d'école de 1 à 6.                  |     |     |     |     |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Vérifier le format d'un numéro de maison allemand (3 chiffres + 1 lettre)       |     |     |     |     |
| \[0-9\]{5}                      | Vérification du format des codes postaux allemands (5x un chiffre entre 0 et 9) |     |     |     |     |
| \[0-9/. \\-\]+                  | Vérification du format d'un numéro de téléphone                                 |     |     |     |     |
| Max.\*Mustermann                | Recherche d'un éventuel deuxième prénom d'un auteur                             |     |     |     |     |

{{< warning  headline="Conseil"  text="Vous trouverez un **tutoriel** détaillé sur l'utilisation des expressions régulières pour la vérification des chaînes de caractères [ici (allemand)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) et [ici (anglais)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
