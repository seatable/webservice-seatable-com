---
title: "Exemple de formule : Fusionner des colonnes de texte à l'aide d'une formule"
date: 2023-01-28
lastmod: '2023-09-18'
categories:
    - 'formeln'
author: 'nsc2'
url: '/fr/aide/exemple-formule-fusion-colonnes-texte'
aliases:
    - '/fr/aide/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel'
seo:
    title: 'Exemple de formule : fusion de colonnes texte SeaTable'
    description: 'Découvrez comment fusionner des colonnes texte avec une formule SeaTable et créer facilement des chaînes ou noms personnalisés.'
---

Les formules de SeaTable vous offrent différentes possibilités de travailler avec les données de vos tableaux. L'une d'entre elles consiste à fusionner les contenus de différentes [colonnes de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}). En utilisant une formule appropriée, vous pouvez fusionner autant de contenus que vous le souhaitez provenant de différentes colonnes dans une seule colonne de formule.

## Fusionner des colonnes de texte

Dans l'exemple concret, l'objectif est de combiner, à l'aide d'une formule, les contenus (nom, prénom et titre) des trois premières colonnes en un **nom complet**.

![Exemple de tableau pour la fusion de différents contenus dans une colonne de formules](images/example-table-zusammenfuehren-von-inhalten-mit-Formel.png)

Pour cela, vous ajoutez d'abord une **colonne de formule** au tableau, dans l'éditeur de laquelle vous pouvez ensuite insérer la formule.

![Ajouter une formule dans la zone de texte prévue à cet effet](images/insert-formular-example-1.png)

Pour fusionner des contenus de différentes colonnes de texte dans une seule colonne, vous devez toujours faire référence aux **noms des colonnes** dans lesquelles se trouvent les contenus correspondants dans votre tableau. Il est particulièrement important que les noms des colonnes soient encadrés par des **accolades**, sinon SeaTable ne pourra **pas** identifier les contenus à fusionner.

{{< warning  headline="Conseil"  text="Les **noms de colonne** dans le tableau ouvert sont affichés à gauche dans l'**éditeur de formule** et peuvent être insérés dans la formule par un **double-clic**." />}}

![Lorsque vous faites référence à des noms de colonnes dans vos tableaux, entourez-les toujours d'accolades.](images/verweis-auf-spaltennamen-in-formel-beispiel-2.png)

Pour réunir les contenus des colonnes de texte dans une colonne de formule, organisez d'abord les noms des colonnes dans l'**ordre** souhaité dans la formule et séparez-les à chaque fois par un **symbole &** que vous trouverez dans l'éditeur de formule près des **opérandes**.

![Organisez les différents noms de colonnes dans l'ordre souhaité dans la formule et séparez-les par le symbole &.](images/insert-symbols.png)

Pour que les différents contenus soient séparés par un **espace**, ajoutez un **symbole &** et deux **guillemets (en haut)** **après** les deux premiers noms de colonne.

![Ajout d'un symbole & supplémentaire et de deux guillemets après les deux premiers noms de colonne](images/insert-and-22-22-to-the-formular.png)

Après confirmation de la formule saisie, les contenus des colonnes de texte sont automatiquement fusionnés et le **résultat** apparaît automatiquement dans la colonne de formule.

![Colonne de formules après la confirmation de la formule saisie.](images/table-example-2-after-formular.png)

{{< warning  headline="Conseil de pro" >}}

Chaque fois que vous utilisez des colonnes de texte dans une formule et que ces colonnes peuvent aussi être vides, il est recommandé d'utiliser la fonction _trim( )_. Celle-ci permet de supprimer les espaces au début et à la fin d'un texte. La formule complète est alors par exemple

```
trim( {Title} & " " & {Surname} & " " & {Name} )
```

{{< /warning >}}
