---
title: 'La colonne de texte'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/fr/aide/colonne-de-texte'
aliases:
    - '/fr/aide/validierung-der-eingabe-bei-textfeldern'
    - '/fr/aide/validation-texte-regex-seatable'
seo:
    title: 'La colonne de texte dans SeaTable'
    description: "Utilisez la colonne de texte pour saisir de courtes chaînes alphanumériques et validez vos entrées à l’aide d’expressions régulières."
weight: 1
---

La colonne de texte est l'un des **types de colonne** les plus élémentaires de SeaTable et s'affiche également en première position dans le menu de sélection du type de colonne.

![La colonne de texte régulière](images/select-regular-text-column.png)

Par défaut, SeaTable ajoute automatiquement une **colonne de texte** comme première colonne à chaque nouveau tableau créé. Par ailleurs, vous pouvez ajouter manuellement autant de colonnes de texte que vous le souhaitez à votre tableau. Vous découvrirez comment procéder [ici]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![La colonne de texte](images/text-column-new.png)

La **première colonne** d'un tableau présente plusieurs [particularités]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), comme vous pouvez le lire dans l'article en lien.

## Utilisation de la colonne de texte

La colonne de texte est particulièrement adaptée à la saisie et au [tri]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) de courtes chaînes alphanumériques, par exemple des **termes**, des **noms**, des **mots de passe**, des **plaques d'immatriculation** ou des **IBAN**.

![Exemple d'utilisation de la colonne de texte régulière](images/regular-text-example.png)

{{< warning  headline="UTF-8"  text="SeaTable prend en charge tous les caractères selon la norme UTF-8, car UTF-8 est l'encodage de caractères le plus répandu au monde pour Internet." />}}

Lors de l'utilisation de la colonne, il est judicieux de garder les entrées aussi **courtes** que possible, car seul un **nombre limité de caractères** peut être affiché sans qu'il soit nécessaire d'augmenter la largeur de la colonne.

![Les entrées trop longues ne peuvent pas être entièrement affichées dans une colonne de texte sans augmenter la largeur de la colonne](images/use-short-entries.png)

## Autres types de colonnes basées sur le texte

Notez qu'**aucune option de mise en forme** n'est disponible pour les entrées de la colonne de texte. Si vous souhaitez saisir des textes structurés comportant des retours à la ligne, des listes, des images, etc., il est préférable d'utiliser la colonne [Texte formaté]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}).

Il existe dans SeaTable trois autres types de colonnes basées sur le texte pour des applications spécifiques :
- la [colonne e-mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- la [colonne URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- la [colonne numéro de téléphone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

{{< warning  headline="Remarque" >}}
Il existe de nombreuses fonctions de texte pour les [colonnes de formule]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), qui se comportent comme des colonnes de texte lorsque les résultats sont des **chaînes de caractères**.
{{< /warning >}}

## Définir la valeur par défaut

Vous pouvez définir une [valeur par défaut]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) prédéfinie pour chaque colonne de texte. Celle-ci sera automatiquement insérée dans chaque nouvelle ligne du tableau.

Si vous définissez la référence **{creator.name}** ou **{creator.id}** comme valeur par défaut, le **nom** ou l'**ID de l'utilisateur** qui a ajouté la ligne sera automatiquement saisi.

![Référencer le nom d'utilisateur avec une valeur par défaut](images/Set-creator-name-as-default-value.png)

## Valider les entrées

Lorsque vous utilisez des colonnes de texte dans vos tableaux, vous avez la possibilité de valider les entrées. La validation, qui prend en charge les expressions régulières, vous permet de **vérifier les valeurs des cellules** et de mettre en évidence les cellules dont le contenu diffère du format valide.

Vous pouvez configurer la vérification du format dès la création d'une colonne de texte en activant le curseur.

![Activation de la validation de la saisie des colonnes de texte](images/activate-validation-1.png)

Si vous souhaitez effectuer une validation des saisies dans une colonne de texte déjà créée, cliquez d'abord sur le **symbole triangulaire** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} de la colonne correspondante et sélectionnez **Personnaliser le type de colonne** dans le menu déroulant.

1. Activez le curseur **Valider la saisie**
2. Définissez un **format cible**.
![Définition du format cible](images/define-specific-format-2.png)
3. Confirmez en cliquant sur **Envoyer**.

### Conséquence de la validation

Une fois la validation réussie, les **cellules** dont **le contenu diffère** du format cible sont mises en évidence en rouge.

![Cellules surlignées en rouge dont le contenu diffère du format cible](images/marked-entries-which-not-match-the-format.png)

### Expressions régulières

Pour valider vos entrées dans les colonnes de texte, SeaTable prend en charge les **expressions régulières**. Vous trouverez quelques exemples dans le tableau ci-dessous :

| Expression régulière            | Fonction                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------- |
| \[123456\]                      | Vérifier si une entrée correspond à une note d'école de 1 à 6.                  |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Vérifier le format d'un numéro de maison allemand (3 chiffres + 1 lettre)       |
| \[0-9\]{5}                      | Vérification du format des codes postaux allemands (5x un chiffre entre 0 et 9) |
| \[0-9/. \\-\]+                  | Vérification du format d'un numéro de téléphone                                 |
| Max.\*Mustermann                | Recherche d'un éventuel deuxième prénom d'un auteur                             |

{{< warning  headline="Conseil"  text="Vous trouverez un **tutoriel** détaillé sur l'utilisation des expressions régulières pour la vérification des chaînes de caractères [ici (allemand)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) et [ici (anglais)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
