---
title: 'Webhook en cas de modifications multiples et simultanées'
date: 2024-02-13
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/fr/aide/webhook-modifications-simultanees'
aliases:
    - '/fr/aide/webhook-bei-mehreren-gleichzeitigen-aenderungen'
seo:
    title: 'Webhooks pour modifications simultanées dans SeaTable'
    description: 'Découvrez comment SeaTable regroupe les webhooks lors de modifications multiples, le rôle du paramètre row_count et comment récupérer toutes les lignes modifiées.'

---

SeaTable envoie généralement un webhook pour chaque modification apportée à une ligne. Toutefois, si une opération modifie plusieurs lignes à la fois, un seul webhook est généré avec le paramètre supplémentaire _row\_count_. Cela vaut également pour l'API : un appel API génère un webhook, qu'il modifie une ou plusieurs lignes.

Dans l'éditeur web, ce cas se produit par exemple lorsque vous copiez une valeur dans le presse-papiers avec {{< key "CTRL" >}}+{{< key "C" >}}, puis la collez dans plusieurs autres lignes avec {{< key "CTRL" >}}+{{< key "V" >}}. Ce processus ne génère qu'un seul webhook. Le graphique suivant montre le webhook correspondant.

![Plusieurs modifications simultanées par webhook.](images/webhook_multiple_changes.jpg)

## Contenu du webhook

Le paramètre _row\_count_ indique le nombre de lignes concernées. Les autres informations, comme _row\_id_, _row\_name_ et _row\_data_, ne concernent qu'une seule ligne, en général la première de l'opération. _op\_type_ reste également au singulier, c'est-à-dire _insert\_row_, _modify\_row_ ou _delete\_row_.

Actuellement, il n'est pas possible de créer un webhook distinct pour chaque ligne. Le webhook ne contient pas non plus de liste de toutes les lignes concernées.

## Récupérer les lignes modifiées après un webhook

{{< warning headline="Les webhooks ne sont pas conçus pour la synchronisation" text="Si vous souhaitez synchroniser des données avec un autre système, le webhook doit uniquement servir de déclencheur à la synchronisation. Il ne contient pas toutes les modifications et sa livraison n'est pas garantie." />}}

Après le webhook, récupérez les lignes modifiées via l'[interface SQL](https://developer.seatable.com/sql/select/) :

```sql
SELECT * FROM Table1 WHERE _mtime >= '2026-11-05T18:30:00+01:00' ORDER BY _mtime, _id LIMIT 1000 OFFSET 0
```

Tenez compte des points suivants :

- **Comparer avec `>=` :** La colonne _\_mtime_ n'a généralement qu'une précision d'une seconde. Avec `>`, vous manqueriez les modifications effectuées dans la même seconde que votre dernière synchronisation. Comme `>=` renvoie à nouveau certaines lignes, votre système doit pouvoir gérer les doublons.
- **Indiquer le fuseau horaire :** Une heure sans fuseau horaire n'est pas interprétée comme UTC. Indiquez donc toujours le décalage, par exemple `+01:00`.
- **Récupérer les résultats page par page :** Sans `LIMIT`, une requête SQL renvoie au maximum 100 lignes, et le maximum par requête est de 10 000 lignes. Augmentez `OFFSET` jusqu'à ce qu'une requête renvoie moins de lignes que le `LIMIT` défini.
- **Lignes supprimées et liens :** Les lignes supprimées n'apparaissent pas dans cette requête, et l'ajout d'un lien ne modifie pas _\_mtime_. Comparez donc de temps en temps les identifiants de lignes et les colonnes de liens dans les deux systèmes.

## Synchroniser également à intervalles réguliers

Les webhooks ne garantissent pas une livraison complète : les livraisons échouées ne sont pas renouvelées, un webhook peut être [désactivé après des erreurs]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}) et, dans certains cas, il peut ne pas être envoyé du tout. Exécutez donc également la synchronisation selon un calendrier fixe et vérifiez régulièrement que le webhook est toujours actif.
