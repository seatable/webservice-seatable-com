---
title: 'Bibliotecas Python compatibles'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/bibliotecas-python-soportadas'
aliases:
    - '/es/ayuda/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliotecas Python soportadas en SeaTable – guía completa'
    description: 'Lista completa de todas las bibliotecas Python preinstaladas en SeaTable Cloud y Server — con instrucciones para añadir bibliotecas personalizadas.'
weight: 1
star: true
---

El entorno Python de SeaTable utiliza **Python 3.12** e incluye la [biblioteca estándar de Python](https://docs.python.org/3.12/library/index.html) completa (p. ej. os, sys, datetime, math, random, json, re, io, smtplib). Puede importar estos módulos directamente en sus scripts.

## Bibliotecas preinstaladas

Además de la biblioteca estándar, los siguientes paquetes están disponibles en SeaTable Cloud y en la instalación estándar de SeaTable Server:

Para algunas de estas bibliotecas ofrecemos [ejemplos Python]({{< relref "help/skripte/python" >}}) con scripts listos para usar y bases de ejemplo para descargar.

| Biblioteca | Descripción | Ejemplo |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | Cliente API de SeaTable | todos los ejemplos |
| [requests](https://pypi.org/project/requests/) | Solicitudes HTTP | [Consultar cotizaciones]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Análisis y procesamiento de datos | |
| [scipy](https://pypi.org/project/scipy/) | Cálculos científicos | |
| [openai](https://pypi.org/project/openai/) | Cliente API de OpenAI | |
| [qrcode](https://pypi.org/project/qrcode/) | Generación de códigos QR | [Generar códigos QR]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Generación de códigos de barras | [Generar códigos de barras]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | Soporte HEIC/HEIF para Pillow | [Convertir HEIC a PNG]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | Fusión de PDF | [Fusionar archivos PDF]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/RapidFuzz/) | Coincidencia difusa de cadenas | |
| [markdown](https://pypi.org/project/Markdown/) | Conversión de Markdown a HTML | |
| [ldap3](https://pypi.org/project/ldap3/) | Operaciones LDAP | |
| [dateutils](https://pypi.org/project/dateutils/) | Funciones de utilidad para fechas | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | Funciones TLS/SSL | |
| [PyJWT](https://pypi.org/project/PyJWT/) | Procesamiento de JSON Web Tokens | |

Debido a las dependencias de los paquetes anteriores, **Pillow** (procesamiento de imágenes) y **numpy** (cálculos numéricos) también están disponibles.

{{< warning headline="Esta lista puede cambiar" text="La lista actual de bibliotecas preinstaladas se encuentra en el archivo [requirements.txt del Python Runner](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) en GitHub." />}}

## Instalar bibliotecas personalizadas

En **SeaTable Cloud**, está limitado a las bibliotecas listadas arriba. No es posible instalar paquetes adicionales.

En un **servidor SeaTable autohospedado**, puede añadir bibliotecas adicionales creando un Python Runner personalizado. Las instrucciones se encuentran en el [manual de administración de SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
