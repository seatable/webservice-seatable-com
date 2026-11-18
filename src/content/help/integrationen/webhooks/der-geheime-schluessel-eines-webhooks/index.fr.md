---
title: "La clé secrète d'un webhook"
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/fr/aide/securite-webhook-cle-secrete-seatable'
aliases:
  - '/fr/aide/der-geheime-schluessel-eines-webhooks'
seo:
    title: 'Sécurité des webhooks : secret et signature SeaTable'
    description: 'Comment utiliser une clé secrète et la signature pour sécuriser vos webhooks SeaTable : vérifiez la source et empêchez tout accès indésirable par validation.'

---

Si la cible d'un webhook est accessible au public, il faut s'assurer, pour les requêtes entrantes, qu'elles proviennent du système d'origine souhaité. L'origine d'un webhook peut être garantie à l'aide d'une clé secrète.

## L'idée d'une clé secrète

Pour créer un nouveau webhook, il suffit d'indiquer une URL quelconque. La clé secrète peut également rester vide. Toutefois, si votre URL cible est disponible publiquement, vous devez définir une clé secrète et valider cette valeur lors du traitement des webhooks. Dans le cas contraire, n'importe qui peut vous envoyer des demandes correspondantes à cette URL de webhook, qui seront ensuite traitées par vous. Sans la clé secrète, le système cible n'a aucun moyen fiable de savoir si l'événement provient réellement de SeaTable.

Si vous indiquez une clé secrète, le webhook dispose d'une clé supplémentaire. _X-SeaTable-Signature-Header_Il s'agit d'une clé secrète qui permet de garantir l'origine du webhook. Tant que quelqu'un d'autre ne connaît pas la clé secrète, il n'est pas en mesure de vous envoyer des événements par webhook et d'utiliser la clé correspondante. \_X-SeaTable-Signature-Header_ de produire.

Lorsqu'une clé secrète est définie, une requête de webhook ressemble par exemple à ceci :

```
-- HEADER --
Content-Type: application/json
Content-Length: 625
X-Seatable-Signature: sha256=598b55485e7875def064746867ff220e79d7c75512fdb931a39e313af5abfe60
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: python-requests/2.28.1
Host: example.com

-- CONTENT --
{
  event:update
  data: {
    dtable_uuid: 6c17f178ee724c109c68ecee364027fc
    row_id: Y_aYcE6wTo-IzGWb-oDmaQ
    op_user: 92d8f9b243f8437db0131c2536398403@auth.local
    op_type: insert_row
    op_time: 1677595743.088
    table_id: 0000
    table_name: Table1
    row_name: ""
    row_data: []
  }
}

```

## Le calcul de la signature

La clé secrète est un [secret partagé](https://en.wikipedia.org/wiki/Shared_secret) entre SeaTable et le système récepteur. SeaTable utilise la clé secrète pour calculer une valeur de hachage à partir de l'événement, la signature. Le système récepteur utilise la même clé pour calculer la valeur de hachage à partir du contenu reçu et la compare à la signature. Si les deux valeurs ne correspondent pas, il ne faut pas traiter le webhook.

## Validation de la signature

Dans chaque langage de programmation, il devrait y avoir des fonctions correspondantes pour pouvoir valider une telle signature en conséquence. [Cet article]({{< relref "help/integrationen/webhooks/verarbeitung-eines-webhooks-mit-hilfe-von-php" >}}) vous montre à quoi ressemblerait cette vérification en PHP.

Pour Python, un examen pourrait ressembler à ceci :

```
import hmac
from flask import Flask, request

app = Flask(__name__)

@app.route('/receive-seatable-webhook', methods=['POST'])
def receive_seatable_webhook():
    secret = 'secret'
    seatable_signature = request.headers.get('X-Seatable-Signature', '').replace('sha256=', '')

    signature = hmac.new(
        secret.encode('utf-8'), request.data, digestmod='sha256').hexdigest()

    signature_compare = hmac.compare_digest(signature, seatable_signature)

    if signature_compare:
        # do something
        pass

    return {'success': signature_compare}

```
