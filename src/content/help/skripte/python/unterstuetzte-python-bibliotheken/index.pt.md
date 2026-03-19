---
title: 'Bibliotecas Python suportadas'
date: 2023-05-12
lastmod: '2024-10-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/bibliotecas-python-suportadas'
aliases:
    - '/pt/ajuda/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliotecas Python suportadas no SeaTable – guia detalhado'
    description: 'Veja quais módulos Python podem ser usados no SeaTable Cloud, Enterprise e server e saiba incluir bibliotecas personalizadas.'
---

O ambiente Python do SeaTable 6.0 (outubro de 2025) utiliza o Python 3.12 e importa a [Biblioteca Padrão do Python](https://docs.python.org/3.12/library/index.html). A Biblioteca Padrão contém módulos frequentemente utilizados, tais como os, sys, datetime, math e random. Pode utilizá-los diretamente nos seus scripts Python importando-os para o seu script.

## SeaTable Cloud

Além dos módulos da biblioteca padrão, o ambiente Python do SeaTable Cloud também inclui alguns pacotes Python populares. Uma lista dos pacotes Python disponíveis pode ser encontrada no [Manual do desenvolvedor do SeaTable](https://developer.seatable.com/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

Outros pacotes Python não podem ser importados.

## Servidor SeaTable

Se executar o seu próprio servidor SeaTable, pode adicionar pacotes Python adicionais ao ambiente Python. No [Manual de Administração do SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/), encontrará instruções sobre como construir o seu executor Python personalizado.
