---
title: 'Supported Python libraries'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/supported-python-libraries'
aliases:
    - '/help/unterstuetzte-python-bibliotheken'
seo:
    title: 'Supported Python libraries in SeaTable – full overview'
    description: 'Complete list of all pre-installed Python libraries in SeaTable Cloud and Server — with instructions for adding custom libraries on self-hosted systems.'
weight: 1
star: true
---

SeaTable's Python environment uses **Python 3.12** and includes the full [Python Standard Library](https://docs.python.org/3.12/library/index.html) (e.g. os, sys, datetime, math, random, json, re, io, smtplib). You can import these modules directly in your scripts.

## Pre-installed libraries

In addition to the Standard Library, the following packages are available in SeaTable Cloud and in the default installation of SeaTable Server:

For some of these libraries, we provide [Python examples]({{< relref "help/skripte/python" >}}) with ready-to-use scripts and example bases for download.

| Library | Description | Example |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | SeaTable API client | all examples |
| [requests](https://pypi.org/project/requests/) | HTTP requests | [Watch stock prices]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Data analysis and processing | |
| [scipy](https://pypi.org/project/scipy/) | Scientific computing | |
| [openai](https://pypi.org/project/openai/) | OpenAI API client | |
| [qrcode](https://pypi.org/project/qrcode/) | QR code generation | [Generate QR codes]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Barcode generation | [Generate barcodes]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | HEIC/HEIF image support for Pillow | [Convert HEIC to PNG]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | PDF merging | [Merge PDF files]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/RapidFuzz/) | Fuzzy string matching | |
| [markdown](https://pypi.org/project/Markdown/) | Markdown to HTML conversion | |
| [ldap3](https://pypi.org/project/ldap3/) | LDAP operations | |
| [dateutils](https://pypi.org/project/dateutils/) | Date utility functions | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | TLS/SSL functions | |
| [PyJWT](https://pypi.org/project/PyJWT/) | JSON Web Token processing | |

Due to dependencies of the above packages, **Pillow** (image processing) and **numpy** (numerical computing) are also available.

{{< warning headline="This list may change" text="The current list of pre-installed libraries can be found in the [requirements.txt of the Python Runner](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) on GitHub." />}}

## Installing custom libraries

In **SeaTable Cloud**, you are limited to the libraries listed above. Additional packages cannot be installed.

On a **self-hosted SeaTable Server**, you can add additional libraries by building a custom Python Runner. Instructions can be found in the [SeaTable Admin Manual](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
