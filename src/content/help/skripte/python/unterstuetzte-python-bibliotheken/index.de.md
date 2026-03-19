---
title: 'Unterstützte Python Bibliotheken'
date: 2023-05-12
lastmod: '2024-10-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/unterstuetzte-python-bibliotheken'
seo:
    title: 'Unterstützte Python Bibliotheken in SeaTable'
    description: 'Erfahren Sie, welche Python-Module und -Pakete in SeaTable Cloud, Enterprise und auf dem Server unterstützt und wie sie integriert werden können.'
---

Die Python Umgebung von SeaTable 6.1 (März 2026) nutzt Python 3.12 und importiert die [Python Standard Library](https://docs.python.org/3.12/library/index.html). Die Standard Library enthält häufig genutzte Module wie os, sys, datetime, math und random. Diese können Sie unmittelbar in Ihren Python Skripten verwenden, indem Sie diese in Ihr Skript importieren.

## SeaTable Cloud

Neben den Modulen der Standard Library stehen in der Python Umgebung von SeaTable Cloud auch einige populäre Python Pakete zur Verfügung. Eine Liste der verfügbaren Python Pakete finden Sie im [Developer Handbuch von SeaTable](https://developer.seatable.com/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

Weitere Python Pakete lassen sich nicht importieren.

## SeaTable Server

Wenn Sie Ihren eigenen SeaTable Server betreiben, dann können Sie der Python Umgebung weitere Python Pakete hinzufügen. Im [SeaTable Admin Manual](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/) finden Sie eine Anleitung, wie Sie Ihren Custom Python Runner bauen.
