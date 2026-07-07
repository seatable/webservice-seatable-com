---
title: 'Étape 6 : notifier le monde extérieur'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-6-notifier-le-monde-exterieur'
aliases:
    - '/fr/aide/schritt-6-webhooks'
seo:
    title: 'Étape 6 du cours SeaTable 4 : webhooks et notifications ntfy'
    description: 'Faites sortir l''information de SeaTable : observez le payload d''un webhook natif, puis notifiez votre téléphone avec ntfy en complétant votre script d''extraction.'
---

Jusqu'ici, tout est resté à l'intérieur de SeaTable : vos automatisations et vos scripts agissaient sur vos données, et le plugin pouvait en vérifier l'effet. À partir de maintenant, vous allez faire sortir l'information — prévenir un service, un téléphone, un autre outil. La brique de base pour cela s'appelle le webhook.

## Entrant, sortant : de quoi parle-t-on ?

Un webhook, c'est un coup de fil automatique entre deux applications. Quand un événement se produit d'un côté, une requête part aussitôt vers une URL de l'autre côté pour l'avertir. On parle de webhook **sortant** quand c'est SeaTable qui appelle l'extérieur — c'est notre cas ici — et de webhook **entrant** quand c'est l'extérieur qui appelle SeaTable, un sens que vous retrouverez à l'étape sur l'API.

## Voir ce que SeaTable envoie

SeaTable sait déclencher un webhook sortant sans code : vous lui donnez une URL, et à chaque événement choisi, il y envoie un message. Mais un message vers où ? Pour l'observer, le plus simple est de l'envoyer d'abord vers un réceptacle de test.

Ouvrez [webhooks.cc/go](https://webhooks.cc/go) : le service vous attribue une URL unique et affiche, en direct, tout ce qu'il reçoit. Configurez un webhook natif dans votre base pointant vers cette URL, provoquez un changement, et regardez arriver la requête. Vous y découvrez le **payload** : le paquet de données que SeaTable envoie, décrivant ce qui vient de se passer.

![Le payload d'un webhook SeaTable reçu et affiché sur un service de test](images/lvl4-webhook-payload.png)

C'est le principe même des webhooks : vous déclenchez d'un côté, vous allez constater de l'autre. Rien à valider dans le plugin cette fois — l'aller-retour, c'est vous qui le faites, et c'est justement la leçon.

## Une vraie notification : ntfy

Un payload brut sur une page web, c'est parfait pour comprendre, mais sur le terrain vous préféreriez être prévenu pour de bon. C'est là qu'entre en scène ntfy : un service qui transforme une simple requête en **notification sur votre téléphone**.

ntfy ne demande aucun compte. Vous choisissez un **topic** — un nom de canal qui fait aussi office de mot de passe — vous vous y abonnez depuis l'application ntfy, et toute requête envoyée à ce topic vous notifie aussitôt.

{{< warning headline="Un topic ntfy est une adresse et un mot de passe à la fois" text="Quiconque connaît votre topic peut vous envoyer des notifications, et lire les vôtres. Choisissez un nom long et difficile à deviner, et n'y faites jamais transiter d'information sensible." />}}

Reste à trouver le bon moment pour déclencher cette notification. Rappelez-vous l'étape 5 : l'extraction par l'IA prend quelques secondes. Plutôt que de fixer l'écran en attendant, faites-vous prévenir quand les lignes sont prêtes — ou quand quelque chose a échoué.

## Brancher ntfy sur votre script

Le webhook natif que vous venez de voir envoie un payload figé vers une URL. Un script, lui, décide de tout : quoi envoyer, quand, et avec quel message. Reprenez donc le script de l'étape 5 et complétez-le pour qu'il notifie à la fin de son travail :

```python
from seatable_api import Base, context
import json, requests

NTFY = 'https://ntfy.sh/votre-topic-secret'

base = Base(context.api_token, context.server_url)
base.auth()

try:
    data = json.loads(context.current_row.get('JSON'))
    products = data.get('products', [])
    if not products:
        raise ValueError('aucun produit extrait')
    base.update_row(context.current_table, context.current_row['_id'], {
        'Order reference': data['order'],
        'Delivery reference': data['delivery'],
    })
    lines = [{
        'Product ref': p['ref'],
        'Qty': int(p['qty']),
        'Document reference': 'DN' + data['delivery'],
    } for p in products]
    base.batch_append_rows('Line items', lines)
    requests.post(NTFY, data=f"Livraison DN{data['delivery']} : {len(lines)} lignes prêtes à vérifier".encode('utf-8'))
except Exception as e:
    requests.post(NTFY, data=f"Échec de l'extraction : {e}".encode('utf-8'),
                  headers={'Priority': 'high', 'Tags': 'warning'})
```

Deux choses à retenir. D'abord, `requests` — la librairie qui envoie la requête — fait partie des outils déjà disponibles dans les scripts SeaTable : rien à installer. Ensuite, le `try / except` : si l'IA a produit un JSON exploitable, vous recevez un message « lignes prêtes » ; sinon, une notification d'erreur en priorité haute. Votre téléphone vous tient au courant dans les deux cas — et voilà pourquoi un script offre plus qu'un webhook natif : il envoie le bon message, au bon moment, selon ce qui s'est réellement passé.

Remplacez le topic par le vôtre, déposez un nouveau bon de livraison, et attendez la vibration.

## Essayez par vous-même

Provoquez volontairement une erreur : déposez un document dont le PDF est illisible, ou videz la colonne `JSON` avant de relancer le script. Vous devriez recevoir la notification d'échec, pas celle de succès. C'est le genre de garde-fou qui, en production, vous prévient d'un problème avant que quelqu'un ne le découvre sur le quai.

## Article d'aide avec plus d'informations

- [Les webhooks de SeaTable]({{< relref "help/integrationen/webhooks/" >}})
- [Les scripts Python dans SeaTable]({{< relref "help/skripte/python/" >}})
- [ntfy — notifications par simple requête](https://ntfy.sh/)
