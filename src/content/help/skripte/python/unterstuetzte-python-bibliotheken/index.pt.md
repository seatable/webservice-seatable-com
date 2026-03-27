---
title: 'Bibliotecas Python suportadas'
date: 2023-05-12
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/bibliotecas-python-suportadas'
aliases:
    - '/pt/ajuda/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliotecas Python suportadas no SeaTable – guia detalhado'
    description: 'Lista completa de todas as bibliotecas Python pré-instaladas no SeaTable Cloud e Server — com instruções para adicionar bibliotecas personalizadas.'
---

O ambiente Python do SeaTable utiliza **Python 3.12** e inclui a [biblioteca padrão do Python](https://docs.python.org/3.12/library/index.html) completa (por ex. os, sys, datetime, math, random, json, re, io, smtplib). Pode importar estes módulos diretamente nos seus scripts.

## Bibliotecas pré-instaladas

Além da biblioteca padrão, os seguintes pacotes estão disponíveis no SeaTable Cloud e na instalação padrão do SeaTable Server:

Para algumas destas bibliotecas, oferecemos [exemplos Python]({{< relref "help/skripte/python" >}}) com scripts prontos a usar e bases de exemplo para download.

| Biblioteca | Descrição | Exemplo |
|---|---|---|
| [seatable-api](https://pypi.org/project/seatable-api/) | Cliente API do SeaTable | todos os exemplos |
| [requests](https://pypi.org/project/requests/) | Pedidos HTTP | [Consultar cotações]({{< relref "help/skripte/python/aktienkurs-abfragen" >}}) |
| [pandas](https://pypi.org/project/pandas/) | Análise e processamento de dados | |
| [scipy](https://pypi.org/project/scipy/) | Computação científica | |
| [openai](https://pypi.org/project/openai/) | Cliente API OpenAI | |
| [qrcode](https://pypi.org/project/qrcode/) | Geração de códigos QR | [Gerar códigos QR]({{< relref "help/skripte/python/qr-code-generieren" >}}) |
| [python-barcode](https://pypi.org/project/python-barcode/) | Geração de códigos de barras | [Gerar códigos de barras]({{< relref "help/skripte/python/barcode-generieren" >}}) |
| [pillow-heif](https://pypi.org/project/pillow-heif/) | Suporte HEIC/HEIF para Pillow | [Converter HEIC para PNG]({{< relref "help/skripte/python/heic-zu-png-konvertieren" >}}) |
| [pdfmerge](https://pypi.org/project/pdfmerge/) | Fusão de PDF | [Fundir ficheiros PDF]({{< relref "help/skripte/python/pdf-zusammenfuehren" >}}) |
| [rapidfuzz](https://pypi.org/project/rapidfuzz/) | Correspondência difusa de strings | |
| [markdown](https://pypi.org/project/Markdown/) | Conversão de Markdown para HTML | |
| [ldap3](https://pypi.org/project/ldap3/) | Operações LDAP | |
| [dateutils](https://pypi.org/project/dateutils/) | Funções utilitárias para datas | |
| [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) | Funções TLS/SSL | |
| [PyJWT](https://pypi.org/project/PyJWT/) | Processamento de JSON Web Tokens | |

Devido às dependências dos pacotes acima, **Pillow** (processamento de imagens) e **numpy** (computação numérica) também estão disponíveis.

{{< warning headline="Esta lista pode mudar" text="A lista atual das bibliotecas pré-instaladas pode ser encontrada no ficheiro [requirements.txt do Python Runner](https://github.com/seatable/python-pipeline/blob/main/runner/requirements.txt) no GitHub." />}}

## Instalar bibliotecas personalizadas

No **SeaTable Cloud**, está limitado às bibliotecas listadas acima. Não é possível instalar pacotes adicionais.

Num **servidor SeaTable auto-hospedado**, pode adicionar bibliotecas adicionais construindo um Python Runner personalizado. As instruções encontram-se no [manual de administração do SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/).
