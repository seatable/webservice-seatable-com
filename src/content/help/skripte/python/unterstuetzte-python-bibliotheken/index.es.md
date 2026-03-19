---
title: 'Bibliotecas Python compatibles'
date: 2023-05-12
lastmod: '2024-10-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/bibliotecas-python-soportadas'
aliases:
    - '/es/ayuda/unterstuetzte-python-bibliotheken'
seo:
    title: 'Bibliotecas Python soportadas en SeaTable – guía completa'
    description: 'Descubre qué paquetes y módulos Python están disponibles en SeaTable Cloud, Enterprise y servidor. Opciones para ejecutar código propio.'
---

El entorno Python de SeaTable 6.0 (octubre 2025) utiliza Python 3.12 e importa la [Python Standard Library](https://docs.python.org/3.12/library/index.html). La Biblioteca Estándar contiene módulos de uso frecuente como os, sys, datetime, math y random. Puede utilizarlos directamente en sus scripts Python importándolos a su script.

## Nube SeaTable

Además de los módulos de la biblioteca estándar, el entorno Python de SeaTable Cloud también incluye algunos paquetes Python populares. Puede encontrar una lista de los paquetes Python disponibles en el [Manual del desarrollador de SeaTable](https://developer.seatable.com/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

No se pueden importar otros paquetes de Python.

## Servidor SeaTable

Si ejecuta su propio servidor SeaTable, puede añadir paquetes Python adicionales al entorno Python. En el [Manual de administración de SeaTable](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/) encontrará instrucciones sobre cómo crear su ejecutor Python personalizado.
