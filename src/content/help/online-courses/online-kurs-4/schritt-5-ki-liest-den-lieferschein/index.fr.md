---
title: 'Étape 5 : laisser l''IA lire le bon de livraison'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-5-laisser-l-ia-lire-le-bon'
aliases:
    - '/fr/aide/schritt-5-ki-liest-den-lieferschein'
seo:
    title: 'Étape 5 du cours SeaTable 4 : extraire les lignes d''un PDF avec l''IA'
    description: 'Laissez SeaTable lire un bon de livraison PDF et en créer les lignes automatiquement — reconnaissance de texte, extraction par IA, script — sans jamais faire de l''IA un maillon critique.'
---

Souvenez-vous de l'étape 2 : vous aviez importé les lignes d'une livraison depuis un tableur bien rangé. Mais un vrai bon de livraison, à l'origine, c'est un document PDF, pas un fichier prêt à l'emploi. Vous allez maintenant laisser SeaTable faire ce travail à votre place : lire le PDF et en tirer les lignes, toutes seules. C'est le moment le plus spectaculaire du cours — et aussi celui où il faut rester lucide sur ce que l'IA sait, et ne sait pas, faire.

Tout se joue dans une automatisation déclenchée à l'arrivée d'un nouveau document, en trois temps : **lire**, **extraire**, **créer**.

## Lire le document

Le bon de livraison arrive dans la colonne `File` de votre document, sous forme de PDF. Première action : une action d'IA de **reconnaissance de texte**. Elle ne demande aucune consigne — vous lui indiquez seulement la colonne à lire, `File`, et la colonne où déposer le résultat, `OCR text`. SeaTable en extrait tout le texte : références, quantités, ce qui figure sur le papier — mais en vrac, tel quel.

![Le résultat de la reconnaissance de texte déposé dans la colonne OCR text à partir du PDF](images/lvl4-ai-extraction.png)

## Extraire les lignes

Ce texte brut, il faut le structurer : isoler chaque produit et sa quantité. C'est le rôle d'une **action d'IA personnalisée**, à laquelle vous donnez cette fois une consigne précise. La voici, à coller telle quelle :

```
From {OCR text}, extract the purchase order reference (look for "purchase order", "PO" or "P.O.") and the delivery reference and, for each product, its product reference and quantity. Write valid JSON (double quotes) into the {JSON} column, as plain text, no code block, with this exact shape:
{
    "delivery": "delivery reference",
    "order": "purchase order reference",
    "products": [
        { "ref": "product reference", "qty": product quantity as a number }
    ]
}
```

<!-- TODO: verifier que la syntaxe des placeholders {OCR text} / {JSON} correspond bien au referencement de colonnes de l'action Custom AI dans la base. -->

La consigne demande à l'IA de répondre en **JSON** — un format que votre script relira sans ambiguïté. Le résultat atterrit dans la colonne `JSON`.

## Créer les lignes

Vous savez déjà, depuis l'étape 3, ce qu'un script sait faire. Celui-ci lit le JSON produit par l'IA et crée une ligne par produit dans `Line items`. Il vous est fourni :

```python
from seatable_api import Base, context
import json

base = Base(context.api_token, context.server_url)
base.auth()

data = json.loads(context.current_row.get('JSON'))
base.update_row(context.current_table, context.current_row['_id'], {
    'Order reference': data['order'],
    'Delivery reference': data['delivery'],
})
lines = [{
    'Product ref': p['ref'],
    'Qty': int(p['qty']),
    'Document reference': 'DN' + data['delivery'],
} for p in data['products']]
if lines:
    base.batch_append_rows('Line items', lines)
```

Et voici l'élégance de l'ensemble : chaque ligne créée déclenche, comme à l'étape 2, votre automatisation « relier par comparaison ». Les nouvelles lignes se rattachent d'elles-mêmes à leur produit et à leur document. Du PDF aux lignes reliées, sans une seule saisie — enchaînez ces trois actions dans une automatisation déclenchée par l'arrivée d'un document, déposez un nouveau bon, et regardez faire.

## L'IA propose, vous validez

Un mot essentiel avant d'aller plus loin. L'IA est impressionnante, mais elle n'est pas infaillible : selon la qualité du scan ou la mise en page du fournisseur, elle peut se tromper sur une quantité, oublier une ligne, ou buter tout court. C'est dans sa nature, et aucun réglage n'y change quoi que ce soit à cent pour cent.

C'est précisément pour cela que l'étape suivante de votre processus est la vérification humaine que vous connaissez déjà. Les lignes proposées par l'IA ne sont pas gravées dans le marbre : elles passent par la réception de l'étape 3, où vous confrontez l'annoncé au réel. L'imperfection de l'IA n'est pas un défaut à contourner, c'est la raison d'être de cette validation.

Et si l'IA déraille complètement sur votre exemple ? Le plugin vous propose un bouton « Charger l'exemple » qui pose directement les bonnes lignes. Votre progression n'est jamais bloquée par un caprice du modèle — et le plugin vérifie que les lignes sont là et validées, pas que l'IA a réussi du premier coup.

{{< warning headline="Ne faites jamais de l'IA un maillon critique" text="Une IA accélère et propose, mais un processus qui doit tourner de façon fiable ne peut pas dépendre de sa réussite. Gardez toujours, derrière elle, une validation humaine et un chemin de secours. Ici, ce filet, c'est la réception de l'étape 3 et le bouton de chargement de l'exemple — l'IA fait gagner du temps, elle ne décide jamais seule." />}}

## Essayez par vous-même

Ouvrez la colonne `OCR text` d'un document déjà traité et lisez ce que la reconnaissance a réellement produit : un texte en vrac, parfois approximatif. Mesurez le chemin parcouru entre ce fouillis et les lignes propres, reliées et vérifiées de votre base — c'est tout ce travail que l'enchaînement OCR, IA et script a abattu pour vous, et c'est aussi pourquoi une relecture humaine reste de mise.

## Article d'aide avec plus d'informations

- [Les actions d'intelligence artificielle]({{< relref "help/ai/ai-automations/" >}})
- [Les scripts Python dans SeaTable]({{< relref "help/skripte/python/" >}})
