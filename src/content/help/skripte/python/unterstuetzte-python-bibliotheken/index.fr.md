---
title: 'Bibliothèques Python supportées'
date: 2023-05-12
lastmod: '2024-10-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/bibliotheques-python-prises-en-charge'
aliases:
    - '/fr/aide/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliothèques Python prises en charge dans SeaTable'
    description: 'Liste des modules et packages Python utilisables dans SeaTable Cloud, dédiée et serveur. Explications sur l’ajout et la prise en charge.'
---

L'environnement Python de SeaTable 6.0 (octobre 2025) utilise Python 3.12 et importe la [bibliothèque standard Python](https://docs.python.org/3.12/library/index.html). La bibliothèque standard contient des modules fréquemment utilisés tels que os, sys, datetime, math et random. Vous pouvez les utiliser directement dans vos scripts Python en les important dans votre script.

## SeaTable Cloud

Outre les modules de la bibliothèque standard, l'environnement Python de SeaTable Cloud propose également quelques paquets Python populaires. Une liste des paquets Python disponibles est disponible dans le [manuel du développeur de SeaTable](https://developer.seatable.com/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

Il n'est pas possible d'importer d'autres paquets Python.

## Serveur SeaTable

Si vous exploitez votre propre serveur SeaTable, vous pouvez ajouter d'autres paquets Python à l'environnement Python. Vous trouverez dans le [manuel d'administration de SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/) des instructions sur la manière de construire votre Custom Python Runner.
