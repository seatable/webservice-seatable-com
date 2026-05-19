---
title: 'La formule Countlinks'
date: 2023-01-11
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/fr/aide/formule-countlinks-seatable'
aliases:
    - '/fr/aide/die-countlinks-formel'
seo:
    title: 'Countlinks SeaTable : calcul des liaisons entre tables'
    description: 'Utilisez Countlinks pour connaître en temps réel le nombre de liens dans vos colonnes reliées. Idéal pour listes de membres, références croisées et projets.'

---

La formule Countlinks compte le nombre d'entrées liées du type de colonne **Lien vers d'autres entrées** dans la ligne correspondante.

{{< warning  headline="La liaison des tableaux est une condition de base" >}}

Vous ne pouvez créer une colonne avec la formule Countlinks que si vous avez lié deux tableaux entre elles. Lisez [ici comment créer un tel lien]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Champ d'application de la formule Countlinks

La **formule Countlinks** devrait être utilisée chaque fois que vous souhaitez afficher le **nombre d'entrées** d'un autre tableau en tant que référence croisée.

Par exemple, lors de la planification d'un atelier, il est possible de représenter le nombre de participants inscrits à partir d'un tableau séparé. La [colonne de liaison]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) conserverait ainsi les noms de tous les participants.

![La formule Countlinks.](images/countlinks-2.png)

L'utilisation de la formule Countlinks n'a de sens que si vous activez l'option **Autoriser les liens vers plusieurs lignes** lors de la création d'une colonne de type **Lien vers d'autres entrées**. Si cette option était désactivée, le champ de la formule Countlinks contiendrait toujours un un.

## Création d'une formule Countlinks

![La formule Countlinks.](images/countlink.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Donnez un **nom** approprié à la colonne.
3. Définissez l'option **Countlinks** comme formule.
4. Dans le champ **Sélectionner une colonne de liens dans ce tableau**, sélectionnez maintenant la colonne de liens dont vous souhaitez compter les entrées.
5. Cliquez sur **Envoyer**.
