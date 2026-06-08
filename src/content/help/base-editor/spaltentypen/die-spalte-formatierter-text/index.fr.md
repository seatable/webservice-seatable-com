---
title: 'Les colonnes Texte et Texte formaté'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/fr/aide/colonne-texte-ou-texte-formate-seatable'
aliases:
    - '/fr/aide/die-spalten-text-und-formatierter-text'
seo:
    title: 'Colonne texte ou texte formaté dans SeaTable ?'
    description: 'Utilisez la colonne texte standard pour champs courts, la colonne texte formaté pour contenus longs ou structurés.'

---

Deux types de colonnes sont disponibles dans SeaTable pour la saisie de **chaînes de caractères** et **de textes** de toute sorte : **Texte** et **Texte formaté**. Mais en quoi ces deux types de colonnes diffèrent-ils exactement ? Et dans quels cas est-il utile de recourir à la colonne Texte formaté ?

## La colonne de texte

La colonne de texte est l'un des **types de colonne** les plus basiques de SeaTable et est également affichée en premier dans le menu de sélection du type de colonne.

![La colonne de texte régulier](images/select-regular-text-column.png)

De plus, SeaTable ajoute automatiquement une **colonne de texte** comme première colonne à chaque nouveau tableau créé.

![La colonne de texte "régulière ](images/text-column-new.png)

La **première colonne** d'un tableau présente plusieurs [particularités]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), comme vous pouvez le lire dans l'article en lien.

### Utilisation de la colonne de texte

La colonne "texte" est particulièrement adaptée à la collecte d'entrées courtes, par exemple **des termes**, **des noms**, des **mots** ou d'autres **chaînes de caractères** qui n'ont pas de valeur numérique calculable, comme les adresses et les numéros de téléphone.

![Exemple d'utilisation de la colonne de texte régulière](images/regular-text-example.png)

Lors de l'utilisation de la colonne, il est judicieux de garder les entrées **courtes**, car seul un **nombre limité de caractères** peut être affiché sans qu'il soit nécessaire d'augmenter la largeur de la colonne.

![Les entrées trop longues ne peuvent pas être entièrement affichées dans une colonne de texte sans augmenter la largeur de la colonne.](images/use-short-entries.png)

{{< warning  headline="Remarque importante"  text="Notez qu'**aucune option de mise en forme** n'est disponible pour les entrées de la colonne de texte régulier." />}}

Il existe dans SeaTable deux autres types de colonnes basées sur le texte pour des applications spécifiques : la [colonne e-mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) et la [colonne URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}).

### Définir la valeur par défaut

Vous pouvez définir une [valeur par défaut]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) prédéfinie pour chaque colonne de texte. Celle-ci sera automatiquement insérée dans chaque nouvelle ligne du tableau.

Si vous définissez la référence **{creator.name}** ou **{creator.id}** comme valeur par défaut, le **nom** ou l'**ID de l'utilisateur** qui a ajouté la ligne sera automatiquement saisi.

![Référencer le nom d'utilisateur avec une valeur par défaut](images/Set-creator-name-as-default-value.png)

## La colonne Texte formaté

Le type de colonne **Texte formaté** fait partie des types de colonne plus spécifiques et s'affiche en deuxième position lorsque vous sélectionnez le type de colonne.

![La colonne Texte formaté](images/formatted-text-column.png)

### Utilisation de la colonne Texte formaté

Les colonnes de texte formatées sont particulièrement adaptées pour conserver **des textes plus longs**, par exemple des descriptions de produits, des listes de contrôle ou des posts de médias sociaux.

Vous ne rédigez **pas** vos entrées directement dans la cellule, mais dans un **éditeur** accessible en un clic, qui offre différentes **options de formatage**. Ainsi, contrairement à la colonne de texte, vous pouvez également structurer des textes plus longs.

![Exemple d'utilisation d'une colonne de texte formatée](images/long-text-example.png)

Vous pouvez, entre autres, choisir un **format de paragraphe**, mettre la **police** en italique ou en gras et insérer **des liens**, des **citations**, des **listes**, des **tableaux** et **des images**.

{{< warning  headline="Limite de caractères"  text="Pour les cellules individuelles de type Texte formaté, la limite est de 100.000 caractères. Cela correspond à environ 25 pages A4 de texte. La limite de caractères ne devrait donc avoir des répercussions sur votre travail que dans des cas exceptionnels." />}}
