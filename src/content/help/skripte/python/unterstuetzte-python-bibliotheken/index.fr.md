---
title: 'Bibliothèques Python supportées'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/bibliotheques-python-prises-en-charge'
aliases:
    - '/fr/aide/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliothèques Python prises en charge dans SeaTable'
    description: 'Liste complète des bibliothèques Python préinstallées dans SeaTable Cloud et Server — avec instructions pour ajouter des bibliothèques personnalisées.'
weight: 1
star: true
---

L'environnement Python de SeaTable utilise **Python 3.12** et inclut la [bibliothèque standard Python](https://docs.python.org/3.12/library/index.html) complète (par ex. os, sys, datetime, math, random, json, re, io, smtplib). Vous pouvez importer ces modules directement dans vos scripts.

## Bibliothèques préinstallées

En plus de la bibliothèque standard, les paquets suivants sont disponibles dans SeaTable Cloud et dans l'installation standard de SeaTable Server :

Pour certaines de ces bibliothèques, nous proposons des [exemples Python]({{< relref "help/skripte/python" >}}) avec des scripts prêts à l'emploi et des bases d'exemple à télécharger.

| Bibliothèque | Description | Exemple |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | Client API SeaTable | tous les exemples |
| [requests](https://pypi.org/project/requests/) | Requêtes HTTP | [Cours boursiers]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Analyse et traitement de données | |
| [scipy](https://pypi.org/project/scipy/) | Calculs scientifiques | |
| [openai](https://pypi.org/project/openai/) | Client API OpenAI | |
| [qrcode](https://pypi.org/project/qrcode/) | Génération de QR codes | [Générer des QR codes]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Génération de codes-barres | [Générer des codes-barres]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | Support HEIC/HEIF pour Pillow | [Convertir HEIC en PNG]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | Fusion de PDF | [Fusionner des PDF]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/RapidFuzz/) | Correspondance floue de chaînes | |
| [markdown](https://pypi.org/project/Markdown/) | Conversion Markdown vers HTML | |
| [ldap3](https://pypi.org/project/ldap3/) | Opérations LDAP | |
| [dateutils](https://pypi.org/project/dateutils/) | Fonctions utilitaires pour les dates | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | Fonctions TLS/SSL | |
| [PyJWT](https://pypi.org/project/PyJWT/) | Traitement de JSON Web Tokens | |

Grâce aux dépendances des paquets ci-dessus, **Pillow** (traitement d'images) et **numpy** (calculs numériques) sont également disponibles.

{{< warning headline="Cette liste peut changer" text="La liste actuelle des bibliothèques préinstallées se trouve dans le fichier [requirements.txt du Python Runner](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) sur GitHub." />}}

## Installer des bibliothèques personnalisées

Dans **SeaTable Cloud**, vous êtes limité aux bibliothèques listées ci-dessus. Il n'est pas possible d'installer des paquets supplémentaires.

Sur un **serveur SeaTable auto-hébergé**, vous pouvez ajouter des bibliothèques supplémentaires en créant un Python Runner personnalisé. Les instructions se trouvent dans le [manuel d'administration SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
