---
title: 'Étape 3 : réceptionner et mettre à jour le stock'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-3-receptionner-et-mettre-a-jour-le-stock'
aliases:
    - '/fr/aide/schritt-3-bestand-aktualisieren'
seo:
    title: 'Étape 3 du cours SeaTable 4 : un script pour mettre à jour le stock'
    description: 'Réceptionnez une livraison, constatez les quantités reçues, puis découvrez le script Python de SeaTable pour mettre à jour le stock — là où le no-code atteint sa limite.'
---

Vos lignes sont dans la base et reliées à leurs produits. Place à la réception proprement dite : constater ce que vous avez réellement reçu, puis répercuter ce constat sur votre stock. C'est ici que vous rencontrez un nouvel outil — le script — car vous allez vite buter sur une limite du no-code.

## Réceptionner sur le quai

Sur le terrain, on ne réceptionne pas depuis une grille de tableur. Votre base est livrée avec une petite application : une page qui n'affiche que les lignes en attente de réception, pensée pour l'écran d'une tablette ou d'un téléphone. Ouvrez-la et, pour chaque ligne, renseignez deux choses :

- `Received qty`: la quantité que vous comptez réellement.
- `Status`: l'état du lot — `As expected` s'il est conforme, sinon `Too many`, `Too few`, `Missing` ou `Damaged`.

![L'application de réception affichant les lignes à vérifier, avec les champs de quantité reçue et de statut](images/lvl4-receiving-app.png)

{{< warning headline="Le statut est un constat humain" text="Le statut n'est pas calculé automatiquement, et c'est volontaire : un carton peut arriver au complet mais abîmé. Aucun rapprochement de quantités ne saurait le deviner. C'est vous, sur le quai, qui tranchez — et tout le reste du cours s'appuie sur ce constat." />}}

## Là où le no-code s'arrête aujourd'hui

Vous avez constaté la réception. Reste à mettre à jour le stock : ajouter les quantités reçues au `Stock` du produit concerné. Et là, l'automatisation no-code que vous venez d'apprendre bute.

Une automatisation agit sur la ligne qui la déclenche, ici une ligne de `Line items`. Or le stock vit dans une **autre** table, `Products`, sur l'enregistrement `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` qui lui est *lié*. Écrire dans un enregistrement lié depuis une automatisation n'est, à ce jour, pas possible sans code — c'est d'ailleurs une évolution prévue de SeaTable.

Qu'à cela ne tienne : c'est l'occasion idéale de rencontrer l'outil qui, lui, ne connaît pas cette limite — le script. Un script vous laisse aller au-delà des fonctions intégrées, pour ce besoin-ci comme pour quantité d'autres. Et même le jour où le no-code saura écrire dans un enregistrement lié, ce petit script restera un excellent premier terrain : vous n'apprenez pas à sortir l'artillerie lourde pour une broutille, mais un outil qui vous resservira partout où l'intégré s'arrête.

## Votre premier script

SeaTable vous laisse écrire des scripts dans deux langages : Python et JavaScript. Tout au long de ce cours, nous utilisons Python — l'un des langages les plus répandus pour l'automatisation et le traitement de données, réputé pour sa lisibilité, et donc une bonne porte d'entrée si vous débutez. Ce que vous apprenez ici se transpose sans peine à JavaScript si vous le préférez.

L'éditeur est intégré à votre base : rien à installer. Et un script y bénéficie d'un atout précieux, l'objet `context`, qui lui donne accès à la base et à la ligne courante sans que vous manipuliez la moindre clé.

Écrivons-le ensemble — c'est court. (Pressé, ou déjà à l'aise avec Python ? Le script complet est juste en dessous, à copier-coller.)

D'abord, la connexion à la base. Grâce à `context`, aucun jeton à coller : SeaTable fournit les identifiants à la volée.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

Ensuite, la ligne qui a lancé le script — `context.current_row` — et le calcul de ce qu'il faut ajouter au stock, selon le statut constaté :

```python
row = context.current_row
status = row.get('Status')
if status == 'As expected':
    delta = row.get('Qty') or 0
elif status in ('Missing', 'Damaged'):
    delta = 0                       # rien de vendable n'entre en stock
else:                               # Too many / Too few
    delta = row.get('Received qty') or 0
```

Enfin, on remonte de la ligne jusqu'au produit lié et on ajoute ce `delta` à son `Stock`.

<!-- TODO: coller ici le script complet et testé (récupération du Product lié via son row_id + base.update_row sur Products), et le proposer en bloc à copier-coller. -->

{{< warning headline="Gardez vos identifiants hors du code" text="Dans un script SeaTable, ne codez jamais un jeton en dur. Passez toujours par context.api_token et context.server_url : le secret ne figure pas dans le code et n'est jamais envoyé à un navigateur. À retenir : ceci protège le secret parce que seules les personnes autorisées à exécuter le script y ont accès — ce n'est pas le code qui le cache, c'est le contrôle de qui peut le lancer." />}}

## Lancer le script au bon moment

Un script peut se déclencher de plusieurs façons ; ici, vous le reliez à un bouton — la colonne `Validate` de vos lignes. L'opérateur vérifie une ligne, clique sur `Validate`, et le stock se met à jour.

Pourquoi un bouton, plutôt qu'une automatisation qui réagirait à la saisie ? Parce qu'ajouter au stock n'est pas une opération rejouable. Une automatisation qui se redéclencherait à chaque modification de la ligne ajouterait les quantités deux fois. Le bouton, lui, est un geste volontaire, fait une seule fois — et la ligne quitte ensuite la liste à traiter, ce qui écarte tout risque de double comptage.

Cliquez sur `Validate` pour une ligne conforme, puis ouvrez la fiche de son produit : le `Stock` a augmenté. C'est le bon moment pour faire vérifier votre travail par le plugin.

## Essayez par vous-même

Rejouez la réception avec un lot marqué `Damaged` : renseignez une quantité reçue, validez, puis vérifiez le stock du produit. Il ne bouge pas — le script a bien traité ce cas à part. Ce petit test vous montre pourquoi le statut valait la peine d'être saisi à la main plutôt que déduit d'un simple écart de quantités.

## Article d'aide avec plus d'informations

- [Les scripts Python dans SeaTable]({{< relref "help/skripte/python/" >}})
- [Lancer un script depuis un bouton ou une automatisation]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/" >}})
- [Documentation développeur : bien démarrer avec Python](https://developer.seatable.com/)
- [Débuter en Python en automatisant des tâches (Automate the Boring Stuff, gratuit)](https://automatetheboringstuff.com/)
