---
title: "Les colonnes Dernier éditeur et Date de dernière modification"
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/fr/aide/dernier-editeur-date-modifiee-seatable'
aliases:
    - '/fr/aide/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum'
seo:
    title: 'Dernier éditeur et date modification : colonnes SeaTable'
    description: 'Les colonnes système SeaTable révèlent qui édite une ligne et à quelle date, pour un suivi fiable, l’automatisation et la gestion d’équipe précise.'
weight: 23
---

Les colonnes **Dernier éditeur** et **Date de dernière modification** sont exclusivement remplies **automatiquement** par SeaTable et constituent donc des types de colonnes particuliers. Elles sont très utiles si vous souhaitez savoir **quand** et **par qui** une entrée a été **modifiée pour la dernière fois**.

Comme les deux colonnes enregistrent automatiquement les modifications apportées aux entrées, elles conviennent bien, par exemple, comme déclencheurs pour [les automatisations]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) et [les tris]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}).

## Les colonnes Dernier éditeur et Date de dernière modification

Alors que SeaTable remplit la colonne **Dernier éditeur** avec le nom de l'utilisateur qui a modifié une ligne pour la dernière fois, la colonne **Date de dernière modification** enregistre la date et l'heure exacte à laquelle la dernière modification a été effectuée.

![Les colonnes Dernier éditeur et Date de dernière modification après la création par un utilisateur](images/last-modifiere-and-last-modified-time.png)

## Particularités des deux types de colonnes

- Vous ne pouvez **pas** modifier manuellement les valeurs saisies automatiquement dans les colonnes Dernier éditeur et Date de dernière modification. Les valeurs se mettent à jour d'elles-mêmes dès qu'une modification est apportée à une ligne.
- Lors de la **création** des deux types de colonnes, vous ne disposez d'**aucune** option, à l'exception du nom de la colonne.
- **Une seule** colonne de chaque type peut être créée par tableau. Si vous essayez de créer une autre colonne du même type, le message "Une autre colonne a ce type de colonne" apparaît.

![Message d'erreur en cas d'autre colonne Dernier éditeur](images/Fehlermeldung-bei-weiterer-Letzter-Bearbeiter-Spalte.png)

- C'est pourquoi vous ne pouvez **pas dupliquer** les colonnes Dernier éditeur et Date de dernière modification, **ni adapter leur type de colonne**.
